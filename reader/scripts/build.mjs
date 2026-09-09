import { spawnSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { copyFileSync, mkdirSync } from "node:fs";

const readerDir = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = resolve(readerDir, "..");
const outDir = resolve(process.env.ASTRO_OUT_DIR || resolve(repoRoot, "build/html"));
const publicDir = resolve(readerDir, "public");

mkdirSync(publicDir, { recursive: true });
copyFileSync(resolve(repoRoot, "cover.jpg"), resolve(publicDir, "cover.jpg"));

const env = { ...process.env, ASTRO_OUT_DIR: outDir };
const bin = (name) => resolve(readerDir, "node_modules", ".bin", name);

function run(command, args) {
  const result = spawnSync(command, args, { cwd: readerDir, stdio: "inherit", env });
  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

run(bin("astro"), ["build"]);
run(bin("pagefind"), ["--site", outDir]);
