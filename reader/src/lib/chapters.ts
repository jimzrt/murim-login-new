import { getCollection, type CollectionEntry } from "astro:content";

export type ChapterEntry = CollectionEntry<"chapters">;

export interface ChapterIndexItem {
  id: string;
  chapter: number;
  title: string;
  href: string;
}

export interface ChapterRef {
  chapter: number;
  title: string;
}

export interface ChapterGroup {
  label: string;
  start: number;
  end: number;
  items: ChapterIndexItem[];
}

export interface CompactChapter {
  n: number;
  t: string;
  h: string;
}

export function withBase(path: string): string {
  const base = import.meta.env.BASE_URL ?? "/";
  return `${base}${path.replace(/^\//, "")}`;
}

export function chapterHref(chapter: number): string {
  return withBase(`chapter/${chapter}/`);
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

export function toCompact(items: ChapterIndexItem[]): CompactChapter[] {
  return items.map((item) => ({ n: item.chapter, t: item.title, h: item.href }));
}

export function neighbors(entries: ChapterEntry[], chapter: number) {
  const index = entries.findIndex((entry) => entry.data.chapter === chapter);
  return {
    previous: index > 0 ? entries[index - 1] : undefined,
    next: index >= 0 && index + 1 < entries.length ? entries[index + 1] : undefined,
  };
}

export function toRef(entry?: ChapterEntry): ChapterRef | null {
  return entry ? { chapter: entry.data.chapter, title: entry.data.title } : null;
}

export function groupedChapters(items: ChapterIndexItem[], size = 50): ChapterGroup[] {
  const groups: ChapterGroup[] = [];
  for (const item of items) {
    const start = Math.floor(item.chapter / size) * size;
    const end = start + size - 1;
    const current = groups.at(-1);
    if (!current || current.start !== start) {
      groups.push({ label: `${start}–${end}`, start, end, items: [item] });
    } else {
      current.items.push(item);
    }
  }
  return groups;
}

export function readingMinutes(wordCount: number): number {
  return Math.max(1, Math.ceil(wordCount / 220));
}
