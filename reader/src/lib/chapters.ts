import { getCollection, type CollectionEntry } from "astro:content";

export type ChapterEntry = CollectionEntry<"chapters">;

export interface ChapterIndexItem {
  id: string;
  chapter: number;
  title: string;
  href: string;
}

export function chapterHref(chapter: number): string {
  return `/chapter/${chapter}/`;
}

export async function allChapters(): Promise<ChapterEntry[]> {
  return (await getCollection("chapters")).sort((left, right) => left.data.chapter - right.data.chapter);
}

export function toIndex(entries: ChapterEntry[]): ChapterIndexItem[] {
  return entries.map((entry) => ({
    id: entry.id,
    chapter: entry.data.chapter,
    title: entry.data.title,
    href: chapterHref(entry.data.chapter),
  }));
}

export function neighbors(entries: ChapterEntry[], chapter: number) {
  const index = entries.findIndex((entry) => entry.data.chapter === chapter);
  return {
    previous: index > 0 ? entries[index - 1] : undefined,
    next: index >= 0 && index + 1 < entries.length ? entries[index + 1] : undefined,
  };
}

export function groupedChapters(items: ChapterIndexItem[], size = 50) {
  const groups: { label: string; items: ChapterIndexItem[] }[] = [];
  for (const item of items) {
    const start = Math.floor(item.chapter / size) * size;
    const label = `${start}–${start + size - 1}`;
    const current = groups.at(-1);
    if (!current || current.label !== label) {
      groups.push({ label, items: [item] });
    } else {
      current.items.push(item);
    }
  }
  return groups;
}

export function readingMinutes(wordCount: number): number {
  return Math.max(1, Math.ceil(wordCount / 220));
}
