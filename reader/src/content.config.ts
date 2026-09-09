import { defineCollection, z } from "astro:content";
import type { Loader } from "astro/loaders";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const translationsDir = fileURLToPath(new URL("../../translations", import.meta.url));
const chapterFile = /^\d{4}\.md$/;

function selectedChapters(): Set<number> | null {
  const raw = process.env.MURIM_CHAPTERS?.trim();
  if (!raw) {
    return null;
  }
  return new Set(
    raw
      .split(",")
      .map((value) => Number.parseInt(value.trim(), 10))
      .filter((value) => Number.isInteger(value) && value >= 0),
  );
}

function wordCount(markdown: string): number {
  return markdown
    .replace(/^#\s+.+$/m, "")
    .replace(/\[\^[^\]]+\]:?/g, " ")
    .replace(/[*_>#`[\]()-]/g, " ")
    .trim()
    .split(/\s+/)
    .filter(Boolean).length;
}

function titleOf(markdown: string, chapter: number): string {
  return markdown.match(/^#\s+(.+?)\s*$/m)?.[1] ?? `Chapter ${chapter}`;
}

function bodyOf(markdown: string): string {
  return markdown.replace(/^#\s+.+?\r?\n+/, "");
}

const chapterLoader: Loader = {
  name: "translation-chapters",
  load: async ({ store, watcher, parseData, renderMarkdown, generateDigest }) => {
    watcher?.add(translationsDir);
    const wanted = selectedChapters();
    const names = (await fs.readdir(translationsDir)).filter((name) => chapterFile.test(name)).sort();
    store.clear();
    for (const name of names) {
      const chapter = Number.parseInt(name, 10);
      if (wanted && !wanted.has(chapter)) {
        continue;
      }
      const filepath = path.join(translationsDir, name);
      const raw = await fs.readFile(filepath, "utf8");
      const id = String(chapter);
      const data = await parseData({
        id,
        data: {
          chapter,
          title: titleOf(raw, chapter),
          wordCount: wordCount(raw),
        },
      });
      store.set({
        id,
        data,
        body: raw,
        filePath: path.posix.join("..", "translations", name),
        digest: generateDigest(raw),
        rendered: await renderMarkdown(bodyOf(raw)),
      });
    }
  },
};

const chapters = defineCollection({
  loader: chapterLoader,
  schema: z.object({
    chapter: z.number().int().nonnegative(),
    title: z.string(),
    wordCount: z.number().int().nonnegative(),
  }),
});

export const collections = { chapters };
