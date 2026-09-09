#!/usr/bin/env python3
"""Exclusive lock for one in-flight translation or audit run.

The kernel flock on `.work/run.lock` is the mutex. The file's JSON is only a
status record (pid, holder, chapter, stage). Nested `run_until` → `run_next` →
`workflow.py` processes join the holder instead of taking a second lock.
A dead process releases the flock even if the JSON file remains.
"""

from __future__ import annotations

import fcntl
import json
import os
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

LOCK_ENV = "MURIM_RUN_LOCK"
LOCK_NAME = "run.lock"
IDENTITY_KEYS = ("pid", "holder", "started")


def lock_path(root: Path) -> Path:
    return root / ".work" / LOCK_NAME


def utcnow() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def pid_is_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _ppid(pid: int) -> int | None:
    try:
        text = Path(f"/proc/{pid}/stat").read_text(encoding="utf-8")
    except OSError:
        return None
    close = text.rfind(")")
    if close < 0:
        return None
    parts = text[close + 1 :].split()
    if len(parts) < 2:
        return None
    try:
        return int(parts[1])
    except ValueError:
        return None


def ancestor_pids() -> set[int]:
    pids: set[int] = set()
    pid = os.getppid()
    while pid > 1 and pid not in pids:
        pids.add(pid)
        parent = _ppid(pid)
        if parent is None or parent == pid:
            break
        pid = parent
    return pids


def in_lock_family(holder_pid: int) -> bool:
    if holder_pid == os.getpid():
        return True
    if holder_pid in ancestor_pids():
        return True
    token = os.environ.get(LOCK_ENV)
    return token == str(holder_pid) and pid_is_alive(holder_pid)


def read_payload(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _encoded(payload: dict) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _write_fd(fd: int, payload: dict) -> None:
    data = _encoded(payload)
    os.lseek(fd, 0, os.SEEK_SET)
    os.write(fd, data)
    os.ftruncate(fd, len(data))
    os.fsync(fd)


def _write_path(path: Path, payload: dict) -> None:
    data = _encoded(payload)
    fd = os.open(str(path), os.O_RDWR | os.O_CLOEXEC)
    try:
        os.write(fd, data)
        os.ftruncate(fd, len(data))
        os.fsync(fd)
    finally:
        os.close(fd)


def format_payload(payload: dict) -> str:
    lines = []
    for key in ("holder", "pid", "chapter", "stage", "until", "started", "updated"):
        if key in payload and payload[key] is not None:
            lines.append(f"  {key}: {payload[key]}")
    return "\n".join(lines)


def conflict_message(path: Path, payload: dict) -> str:
    pid = payload.get("pid")
    live = isinstance(pid, int) and pid_is_alive(pid)
    details = format_payload(payload) or f"  path: {path}"
    liveness = "active" if live else "lock held, recorded pid is not running"
    return (
        f"Another translation run is already in progress ({liveness}):\n"
        f"{details}\n"
        f"Stop that process before starting another run. Lock: {path}"
    )


class RunLock:
    def __init__(self, root: Path, *, owned: bool, fd: int | None, payload: dict) -> None:
        self.root = root
        self.path = lock_path(root)
        self.owned = owned
        self._fd = fd
        self.payload = payload

    def _persist(self, payload: dict) -> None:
        self.payload = payload
        if self._fd is not None:
            _write_fd(self._fd, payload)
        else:
            _write_path(self.path, payload)

    def update(self, **fields: object) -> dict:
        current = read_payload(self.path) or dict(self.payload)
        incoming = {key: value for key, value in fields.items() if value is not None}
        merged = dict(current)
        merged.update(incoming)
        if not self.owned:
            for key in IDENTITY_KEYS:
                if key in current:
                    merged[key] = current[key]
            if current.get("until") is not None:
                merged["until"] = current["until"]
        merged["updated"] = utcnow()
        self._persist(merged)
        return merged

    def release(self) -> None:
        if not self.owned:
            return
        self.owned = False
        fd = self._fd
        self._fd = None
        if fd is None:
            return
        try:
            released = dict(self.payload)
            released["stage"] = "released"
            released["released"] = utcnow()
            released["updated"] = released["released"]
            _write_fd(fd, released)
            self.payload = released
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)
        if os.environ.get(LOCK_ENV) == str(os.getpid()):
            del os.environ[LOCK_ENV]


def acquire_or_join(
    root: Path,
    *,
    holder: str,
    chapter: int | None = None,
    stage: str | None = None,
    until: int | None = None,
) -> RunLock:
    path = lock_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(path), os.O_RDWR | os.O_CREAT | os.O_CLOEXEC, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        os.close(fd)
        existing = read_payload(path)
        holder_pid = existing.get("pid")
        if isinstance(holder_pid, int) and in_lock_family(holder_pid):
            os.environ[LOCK_ENV] = str(holder_pid)
            lock = RunLock(root, owned=False, fd=None, payload=existing)
            lock.update(chapter=chapter, stage=stage, until=until)
            return lock
        raise SystemExit(conflict_message(path, existing)) from None

    started = utcnow()
    payload = {
        "pid": os.getpid(),
        "holder": holder,
        "chapter": chapter,
        "stage": stage or "starting",
        "until": until,
        "started": started,
        "updated": started,
    }
    _write_fd(fd, payload)
    os.environ[LOCK_ENV] = str(os.getpid())
    return RunLock(root, owned=True, fd=fd, payload=payload)


@contextmanager
def hold_run_lock(
    root: Path,
    *,
    holder: str,
    chapter: int | None = None,
    stage: str | None = None,
    until: int | None = None,
) -> Iterator[RunLock]:
    lock = acquire_or_join(root, holder=holder, chapter=chapter, stage=stage, until=until)
    try:
        yield lock
    finally:
        lock.release()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    path = lock_path(root)
    payload = read_payload(path)
    if not payload:
        print("No run lock.")
        return 0
    pid = payload.get("pid")
    live = isinstance(pid, int) and pid_is_alive(pid)
    print(f"Run lock ({'live pid' if live else 'stale pid'}): {path}")
    print(format_payload(payload) or "  (empty)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
