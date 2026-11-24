# Psalm 38: Codex review v1

Verdict: CHANGES

English: `6a314f5`, `english/psalm-038.md`, branch `agent/clark-translator--mwp7htk2`. Latin: `d058035`, `latin/psalm-038.md`, branch `agent/mose-scribe--mwp7hse4`. STYLE.md and GLOSSARY.md checked at the English commit.

1. **Scribe transcription error — join *expositionem*.**
   - Latin, verses 5–6 commentary: “Hanc esse veram ex positionem sequentes versiculi docebunt.”
   - Current English: “That this is the true exposition the following verses will teach.”
   - Problem: PDF p. 261 (printed p. 250), left column, has the single word *expositionem* divided between lines. It has been transcribed as two words. Clark has already reported this.
   - Suggested fix: join *expositionem* in Latin. English is correct and needs only the updated source header after correction. No translator's note. Source correction requested from Mose.

2. **Scribe reading error — the worn final letter requires *contineri*.**
   - Latin, title and argument: “existimamus longe altiorem doctrinam in hoc divino Spiritus Sancti cantico per Prophetam edito continere”. The header describes *continere* as a reading supplied for a worn final sort.
   - Current English: “we … judge that a far higher doctrine is contained in this divine canticle of the Holy Ghost, put forth by the Prophet”.
   - Problem: the accusative *doctrinam* is the subject of a passive infinitive: the doctrine is contained in the canticle. The worn/ink-filled final sort on PDF p. 260 must be read as *i*, giving *contineri*, under the standing rule for worn or wrong-fount sorts. The reading *continere* does not give the required construction.
   - Suggested fix: read *contineri* and amend the Latin header accordingly. Retain the correct English; no translator's note is needed for this source correction. Source correction requested from Mose. Enlarged crop: `/tmp/jo38-continere-word.png`.

3. **STYLE §3 — the Matthew quotation needs a note for reversed garments.**
   - Latin, title and argument: “et volenti pallium nobis eripere, demus illi et tunicam”, cited to *Matth.* V.
   - Current English: “and to him who would take away our cloak, we should give our coat also”.
   - Problem: the English correctly follows Bellarmine, but [Matthew v, 40](https://www.drbo.org/drl/chapter/47005.htm) has *tunicam tuam tollere, dimitte ei et pallium*: the coat is taken and the cloak also yielded. Bellarmine reverses which garment is taken and which is given. This changes their roles; it is not merely word order or a grammatical adaptation.
   - Suggested fix: retain Bellarmine's wording and add a short translator's note: “Bellarmine reverseth the garments of Matt. v, 40; the Vulgate has tunicam tuam tollere, dimitte ei et pallium, in the Douay-Rheims ‘take away thy coat, let go thy cloak also unto him’.”

The entire English was compared sentence by sentence against the Latin, independently of the other critic. No further mistranslation, omission, addition or doctrinal finding. The distinction between fatherly correction and judicial punishment, God's use of an evil will which he did not make, sin as a punishment of sin, and the continued existence of the damned are preserved.

All 78 body blocks correspond, including six page markers and the divided words at page breaks; three translator's notes. The verse numbering note correctly maps Bellarmine's eighteen verses to the fourteen of [Douay-Rheims Psalm 38](https://www.drbo.org/chapter/21038.htm). His variant readings and the Latin words needed beside the Douay-Rheims quotations are preserved. *Plagæ* and *flagella* remain distinct in the prose. The notes concerning Augustine/Ambrose and the Semei reference are appropriate. The spacing *in demeditari* does not require an English note. The three broken marginal glosses remain explicitly uncertain; the English does not invent their missing words.

Independent Latin proof completed word by word against PDF pp. 260–265 (printed pp. 249–254), excluding the editor's material. Findings 1–2 are the source corrections required; no other source slip found. The quoted garments, the printed attribution inconsistency, the Greek and Hebrew, page divisions and damaged margins were checked. The shortened Romans i quotations retain the words and sequence given by the author; no additional note is needed for their omissions. Local proof images: `/tmp/jo38-260.png` through `/tmp/jo38-265.png`; enlarged PDF p. 260: `/tmp/jo38-hi-260.png`.

## Source correction checked

Latin `2b9db59` checked by complete diff from `d058035`: *expositionem*, *contineri* and the header are corrected, with no other changes. The Latin is cleared. English still needs the updated source header and finding 3's Matthew note before PASS.
