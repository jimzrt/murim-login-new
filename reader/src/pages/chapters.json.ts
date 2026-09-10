import type { APIRoute } from "astro";
import { allChapters, toCompact, toIndex } from "../lib/chapters";

export const GET: APIRoute = async () => {
  const chapters = toCompact(toIndex(await allChapters()));
  return new Response(JSON.stringify(chapters), {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
};
