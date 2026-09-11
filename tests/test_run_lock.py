import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

from tools.run_lock import LOCK_ENV, hold_run_lock, lock_path, read_payload


REPO = Path(__file__).resolve().parents[1]


class RunLockTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.saved_env = os.environ.pop(LOCK_ENV, None)

    def tearDown(self):
        os.environ.pop(LOCK_ENV, None)
        if self.saved_env is not None:
            os.environ[LOCK_ENV] = self.saved_env
        self.temporary.cleanup()

    def test_records_holder_chapter_and_stage(self):
        with hold_run_lock(self.root, holder="run_until", chapter=27, stage="prepare", until=100) as lock:
            payload = read_payload(lock.path)
            self.assertEqual(payload["holder"], "run_until")
            self.assertEqual(payload["chapter"], 27)
            self.assertEqual(payload["stage"], "prepare")
            self.assertEqual(payload["until"], 100)
            self.assertEqual(payload["pid"], os.getpid())
            lock.update(stage="draft", chapter=27)
            payload = read_payload(lock.path)
            self.assertEqual(payload["stage"], "draft")
            self.assertEqual(payload["holder"], "run_until")

    def test_same_process_joins_and_keeps_owner_identity(self):
        with hold_run_lock(self.root, holder="run_until", chapter=27, stage="starting", until=100):
            with hold_run_lock(self.root, holder="run_next", chapter=27, stage="workflow") as nested:
                self.assertFalse(nested.owned)
                payload = read_payload(nested.path)
                self.assertEqual(payload["holder"], "run_until")
                self.assertEqual(payload["stage"], "workflow")
                self.assertEqual(payload["until"], 100)
                self.assertEqual(payload["pid"], os.getpid())
            payload = read_payload(lock_path(self.root))
            self.assertEqual(payload["stage"], "workflow")
            self.assertNotEqual(payload.get("stage"), "released")
        payload = read_payload(lock_path(self.root))
        self.assertEqual(payload["stage"], "released")

    def test_stale_file_without_holder_can_be_acquired(self):
        path = lock_path(self.root)
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps({"pid": 1, "holder": "run_until", "stage": "draft"}), encoding="utf-8")
        with hold_run_lock(self.root, holder="run_next", chapter=27, stage="starting") as lock:
            self.assertTrue(lock.owned)
            payload = read_payload(lock.path)
            self.assertEqual(payload["holder"], "run_next")
            self.assertEqual(payload["pid"], os.getpid())

    def test_unrelated_process_is_rejected(self):
        holder = subprocess.Popen(
            [
                sys.executable,
                "-c",
                "import sys, time\n"
                "from pathlib import Path\n"
                "sys.path.insert(0, sys.argv[1])\n"
                "from tools.run_lock import hold_run_lock\n"
                "with hold_run_lock(Path(sys.argv[2]), holder='run_until', chapter=27, stage='prepare', until=100):\n"
                "    print('LOCKED', flush=True)\n"
                "    time.sleep(30)\n",
                str(REPO),
                str(self.root),
            ],
            cwd=REPO,
            text=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        try:
            deadline = time.time() + 5
            payload = {}
            while time.time() < deadline:
                payload = read_payload(lock_path(self.root))
                if payload.get("stage") == "prepare" and payload.get("holder") == "run_until":
                    break
                if holder.poll() is not None:
                    err = holder.stderr.read() if holder.stderr else ""
                    self.fail(f"holder exited early: {err}")
                time.sleep(0.05)
            else:
                self.fail("holder did not publish run.lock")
            with self.assertRaises(SystemExit) as error:
                with hold_run_lock(self.root, holder="run_next", chapter=28, stage="starting"):
                    pass
            message = str(error.exception)
            self.assertIn("already in progress", message)
            self.assertIn("run_until", message)
            self.assertIn("27", message)
            self.assertIn("prepare", message)
        finally:
            holder.terminate()
            try:
                holder.wait(timeout=5)
            except subprocess.TimeoutExpired:
                holder.kill()
                holder.wait(timeout=5)
            if holder.stderr:
                holder.stderr.close()

    def test_child_process_joins_parent_lock(self):
        with hold_run_lock(self.root, holder="run_until", chapter=27, stage="run_next", until=100):
            result = subprocess.run(
                [
                    sys.executable,
                    "-c",
                    "import json, sys\n"
                    "from pathlib import Path\n"
                    "sys.path.insert(0, sys.argv[1])\n"
                    "from tools.run_lock import hold_run_lock, read_payload, lock_path\n"
                    "root = Path(sys.argv[2])\n"
                    "with hold_run_lock(root, holder='run_next', chapter=27, stage='workflow') as lock:\n"
                    "    print(json.dumps({'owned': lock.owned, **read_payload(lock_path(root))}))\n",
                    str(REPO),
                    str(self.root),
                ],
                cwd=REPO,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertFalse(payload["owned"])
            self.assertEqual(payload["holder"], "run_until")
            self.assertEqual(payload["stage"], "workflow")
            self.assertEqual(payload["until"], 100)


if __name__ == "__main__":
    unittest.main()
