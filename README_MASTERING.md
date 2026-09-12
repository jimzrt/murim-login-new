# Two-Model Mastering Overlay

This overlay is the last automatic stage of a normal chapter run. After
`accept`, `run_next.py` runs the two-model mastering overlay, promotes the
verified copy into `translations/`, and includes those artifacts in
`Accept Chapter N`. The pre-master English remains at
`reviews/mastering/<chapter>/baseline.md`.

Manual overlay commands still work for reruns and retrospective chapters:

```text
accepted translation
      ↓
GPT-5.6 Sol full master edit
      ↓
paragraph-aware deterministic diff
      ↓
DeepSeek V4.1 Flash adjudicates every changed hunk
      ↓
SOL / BASE / REPAIR per hunk
      ↓
assembled final chapter
      ↓
existing deterministic QA
      ↓
promote into translations/ (automatic on run_next; manual promote still requires --confirm)
```

There are exactly **two LLM calls per chapter**. DeepSeek writes a replacement only for a `REPAIR` decision; there is no third model or second Sol call.

## Files added by this overlay

```text
MASTERING_EDITORIAL.md
MASTERING_ADJUDICATOR.md
docs/mastering.json
tools/mastering.py
tests/test_mastering.py
README_MASTERING.md
```

Runtime artifacts go under:

```text
reviews/mastering/0001/
    source.txt                 # immutable transaction snapshot
    baseline.md               # immutable accepted-English snapshot
    master-packet.md
    sol.md
    sol-qa.json
    diff.json
    diff.md
    adjudicator-packet.md
    adjudication.json
    final.md
    qa.json
    metrics.json
    omp/
```

The accepted `translations/0001.md` is untouched unless you explicitly run `promote`.

## Install

Extract/copy the overlay into the **root of your existing `murim-login-new` repository**, preserving directories.

Then run:

```bash
python tools/mastering.py doctor
```

`doctor` checks the installation and model configuration but makes no paid model call.

Primary mastering selectors live in `docs/mastering.json`. Sol is requested on
the OpenAI Codex subscription first; OMP falls back through Cursor Sol to paid
OpenRouter Sol using the chains in `.omp/config.yml`. The adjudicator requests
Cursor Grok first and falls through to DeepSeek via `.omp/adjudicator-overlay.yml`.

```json
{
  "models": {
    "master": "openai-codex/gpt-5.6-sol:low",
    "adjudicator": "cursor/cursor-grok-4.6:low"
  }
}
```

Change only these strings if your local OMP naming differs.

## Ten-chapter test

Run the complete pipeline on chapters 1–10:

```bash
python tools/mastering.py run 1-10
```

The workflow is resumable. Paid stages that already have valid output are skipped. If chapter 6 fails, fix the problem and run the same command again; chapters/stages already completed will not be charged again.

You can also run stages separately:

```bash
python tools/mastering.py master 1
python tools/mastering.py adjudicate 1
python tools/mastering.py assemble 1
python tools/mastering.py qa 1
```

Use `--force` only on `master` or `adjudicate` when you deliberately want to pay for a rerun:

```bash
python tools/mastering.py adjudicate 1 --force
```

## Inspect the test

Status:

```bash
python tools/mastering.py status 1-10
```

Cost and decision report:

```bash
python tools/mastering.py report 1-10
```

For each chapter, the most useful files to read are:

```text
reviews/mastering/0001/baseline.md
reviews/mastering/0001/sol.md
reviews/mastering/0001/diff.md
reviews/mastering/0001/adjudication.json
reviews/mastering/0001/final.md
reviews/mastering/0001/qa.json
```

The report records actual OMP/provider-reported costs for Sol and DeepSeek separately, plus how many hunks were kept as SOL, reverted to BASE, or repaired.

## Retrospective context safety

Do **not** feed present-day `docs/CONTEXT.json` blindly into old chapters. It can contain future plot facts.

This overlay instead uses:

- exact glossary rows matched to the current Korean source;
- the latest summary whose end chapter is strictly earlier than the chapter being mastered;
- tails of up to two prior chapters; when a prior chapter has already reached VERIFIED in this mastering run, its mastered final is preferred, otherwise the accepted translation is used;
- compact identity/voice/relationship fields from character profiles only when
  their `Safe through: Chapter N` marker is strictly earlier than the chapter
  being mastered; archived chapter-by-chapter continuity is not injected.

For chapters 1–10, current character profiles will therefore usually be excluded, which is intentional. This prevents later character knowledge from contaminating early-chapter edits.

You can disable profile injection entirely in `docs/mastering.json`:

```json
"include_safe_profiles": false
```

## Diff/adjudication semantics

The diff is paragraph-aware. A hunk can contain one or several adjacent paragraphs when Sol restructures them.

DeepSeek receives:

- complete Korean source (once, with line numbers);
- complete baseline English (once, with `P#` paragraph labels);
- complete Sol English (once, with `P#` paragraph labels);
- exact glossary rows;
- project fidelity rules;
- numbered changed hunks containing the exact changed BASE/SOL prose, paragraph references, and Korean line citations;
- terminology-risk annotations when a preferred baseline term disappears from Sol's hunk.

After assembly, deterministic QA is followed by a bounded whole-chapter fidelity gate. The gate receives both the Korean source and the accepted baseline, so it can catch regressions as well as new mistranslations. Major/critical findings and high-confidence minor findings are repaired automatically and checked again; unresolved major/critical findings block promotion.

Changed prose is repeated in each hunk for reliable direct comparison. Both complete numbered chapters remain available for neighboring context and for judging adjacent hunks that split or restructure one baseline sentence as assembled prose.

It must return exactly one of:

- `SOL` — keep Sol's edit;
- `BASE` — revert that hunk to the accepted baseline;
- `REPAIR` — neither version is satisfactory; DeepSeek supplies a narrowly bounded replacement.

The adjudicator prompt is neutral when both versions are faithful: it keeps Sol
only when the improvement is concrete, while preserving the accepted baseline's
established terminology, formatting, and source-specific texture.

## Safety against accidental overwrites

At the start of mastering a chapter, the script snapshots and hashes the Korean source and accepted English. Later stages abort if either live file changes during the transaction. After promotion, the live translation must keep matching the promoted copy.

`python tools/workflow.py master N` and `run_next.py` promote automatically once mastering QA passes. Manual overlay commands other than `promote` never modify `translations/`.

Manual promotion of an already-verified chapter still requires:

```bash
python tools/mastering.py promote 1-10 --confirm REPLACE_TRANSLATIONS
```

Promotion only accepts chapters whose final deterministic QA passed. The original baseline remains in `reviews/mastering/<chapter>/baseline.md`.

## Recommended evaluation after chapters 1–10

The important numbers are:

- total Sol cost;
- total DeepSeek cost;
- Sol hunks proposed;
- percentage kept as `SOL`;
- percentage reverted to `BASE`;
- percentage repaired;
- QA/terminology warnings;
- your reading preference for `final.md` versus `baseline.md`.

A healthy result should show that DeepSeek mostly accepts Sol, while selectively rejecting concrete fidelity/terminology regressions. If it reverts large amounts of harmless prose editing, the adjudicator prompt is too conservative. If it accepts known terminology or semantic regressions, it is too permissive.
