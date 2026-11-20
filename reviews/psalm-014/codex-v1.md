# Psalm 14 — Codex review v1

Verdict: CHANGES

English: `6bc205c`, `english/psalm-014.md` (Translator branch `agent/clark-translator--mwp7htk2`). Latin: `841d7b8`, `latin/psalm-014.md`.

1. **Scribe finding — transcription slip (v. 3).**
   - Latin file: “Nam omnis qui res temporales pluris œstimat, quam valeant”.
   - Current English: “For every one who esteemeth temporal things at more than they are worth”.
   - Problem: the scan prints *æstimat*, not *œstimat*. Location: PDF p. 84, printed p. 73, left column, v. 3 commentary line 6, beginning “pluris æstimat, quam valeant”. Confirmed in a 300-dots-per-inch crop (`/tmp/jo-crop84.png`). English is correct; the Latin is not yet clean.
   - Suggested fix: Scribe changes *œstimat* to *æstimat*. Translator updates the source-commit header when the correction is committed; no English prose change needed for this finding.

Checked independently line by line. No meaning-affecting English findings. The title note and seven-to-five verse map agree with the [Douay-Rheims Psalm 14](https://www.drbo.org/chapter/21014.htm). The treatment of *macula*, venial sin, usury, and the two Hebrew readings preserves the Latin. The money quotation uses the [Douay-Rheims I Timothy 6](https://www.drbo.org/chapter/61006.htm) wording with *cupiditas* supplied beside it. All 31 content blocks and two page markers correspond.

Independent Latin scan proof: compared the entire unit word by word with PDF pp. 83–84 (printed pp. 72–73), both columns, including margins, Hebrew, title and lemmas. Only the transcription slip above found. CHANGES is required by the Latin-clean sign-off rule, although the English already gives the correct sense.
