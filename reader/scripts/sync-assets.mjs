import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const readerDir = join(dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = join(readerDir, "..");
const publicDir = join(readerDir, "public");

mkdirSync(publicDir, { recursive: true });
copyFileSync(join(repoRoot, "cover.jpg"), join(publicDir, "cover.jpg"));
