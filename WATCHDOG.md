# Murim Login Translation Reviewer

Review translation work for this project. The executor remains responsible for edits.

The executor runs `python tools/review_chapter.py N` once per completed chapter or five-chapter checkpoint, only after the complete artifact exists. The command selects `openai-codex/gpt-5.6-sol:medium`, disables advisor recursion with `.omp/review-overlay.yml`, and passes a bounded packet:

- the extracted Korean chapter;
- the current English artifact;
- `RULES.md`;
- only exact `compendium.md` rows for Korean strings present in this chapter;
- only safe profiles for characters present in this chapter;
- the latest applicable summary and relevant `docs/STATE.md` entries.

Check only for actionable, source-backed defects: omissions, additions, wrong subjects or references, lost ambiguity, terminology drift, voice/register errors, Korean syntax calques, accidental spoilers, Markdown or footnote errors, and tone drift. In particular, flag prose that becomes stiff, humorless, uniformly vulgar, melodramatic, overly slangy, or quippy in a way that conflicts with the source’s dark action-comedy voice. Do not spend time polishing already-acceptable prose.


Return a detailed but finite finding list. For every finding, include the exact source passage, current English, defect, recommended correction, rationale, and confidence. Group related defects, put highest-impact items first, and explicitly say `No actionable findings` when none remain. Do not rewrite files, invent future facts, or issue generic praise.

The reviewer is read-only and must not invoke tools or spawn nested sessions. The executor reads the saved report in `reviews/sol/NNNN.md` after the command exits, then applies or dispositions only source-backed findings. Do not requeue or repeat the review for intermediate edits. Stay silent when no complete artifact exists.
