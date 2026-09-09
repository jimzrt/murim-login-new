# Independent KR–EN smoke gold

Do not score draft models against this project's own *Murim Login*
reading copies. Those were produced by the same harness, so token overlap
only measures self-consistency.

## Pair

| File | Text |
| --- | --- |
| `kuunmong-opening.ko.txt` | Opening of Kim Man-jung, *구운몽* (late 17th c.). Public-domain Korean from the [Wikisource 상권 원문](https://ko.wikisource.org/wiki/구운몽), respelt in modern Hangul so the test matches the webnovel script. The Wikisource page is 완판 옛한글; this file is an orthographic transcription of that same passage, not a new translation. |
| `kuunmong-opening.en.md` | Matching span from James Scarth Gale, *The Cloud Dream of the Nine* (London, 1922), public domain. Gale is a published human KR–EN literary translation, independent of this repo. Source text: [ibiblio / University of Virginia](https://www.ibiblio.org/eldritch/jsg/cloud9.txt) (also circulated via Project Gutenberg). |

The excerpt stops when Song-jin leaves for the Dragon King, before the
eight fairies arrive, so both sides stay short enough for a cheap OMP call.

## How to read the scores

Gale is a **literary expansion**: he interpolates names, ages, and
doctrine that the Korean paragraph does not spell out, and his diction is
1922 missionary English. A good contemporary translation of the Korean
can therefore have a modest `token_f1` against Gale and still be correct.

`tools/model_smoke.py` therefore treats:

- **fact coverage** as the quality signal (mountains, Queen Wee / 위부인,
  Tang priest from India, Lotus Peak, Yook-kwan / 육관, Song-jin / 성진,
  Dragon King as a white-clothed old man, the volunteer);
- **Hangul leftovers / wrappers** as hard QA;
- **token F1 vs Gale** as a resemblance metric, not a pass/fail.

## What this is not

This is classical narrative Korean, not *Murim Login*. It does not test
System windows, manhwa epithets, or the project glossary. It tests whether
a cheap model can render a real published KR–EN pair without collapsing
names, counts, and plot beats.

A closer *modern* literary gold exists (for example Heinz Insu Fenkl's
2019 *Nine Cloud Dream*), but that text is copyrighted and must not be
vendored here.
