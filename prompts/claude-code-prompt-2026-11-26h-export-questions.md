# Claude Code: answer open questions in leanprover-community/riemann-hypothesis from Sutherland's export (26 Nov 2026)

Written by Claude in chat. Reading only: no builds, nothing in `C:\rhc`, no git in `../rh-source`. Stop if C: would drop below 25 GB free. Label claims READ / COMPUTED / DERIVED / GUESS.
**Do not post anything on GitHub.** Timmy writes any comment himself (Lean community rule: no LLM-written comments on their GitHub or Zulip).

## Run it in the same pass as 25c

`prompts/claude-code-prompt-2026-11-25c.md` already streams Sutherland's export (`solution.ndjson.zst`) once. Collect what this prompt needs **in that same pass** (one decompression, one stream), keeping the two tasks' outputs and verdicts separate. If combining is not practical, run this as its own pass afterwards and say why.

## Why

Two open issues ask things the export answers directly. The export holds exactly the declarations the headline theorems depend on (1,468,418), so "in the export" means "on the dependency path of `Main`" and "absent" means "not used by it".
- **Issue #5** (JoseClaudioSJr, reader's map): asks for a plain-text list of constant names to `grep`; which `LinkMu` provider the final path uses (`linkMu_of_sizes`, `linkMu_of_full`, `J.linkMu`, `J.linkMu_of_linkDIV`); which declaration consumes `omTied_retie_of_cube`.
- **Issue #2** (joni15, import cone): whether structures such as `GeneralHyps`, `GeneralHypU`, `GeneralHypV`, defined but apparently never instantiated, are on the path; it says this needs a proof-term dependency trace, which the export is.

## Questions (pre-registered: copy this section to the top of the note before scanning)

1. **Name list.** Write every declaration name in the export, one per line, sorted, to `results/export-names/names.txt`, then zstd-compress it. Record the count (expected 1,468,418, the figure from our earlier scan) and the sha256 of the compressed file. Commit the compressed file only if it is under 25 MB; otherwise keep it local and report the size.
2. **LinkMu providers.** For every declaration whose last name component is `linkMu_of_sizes`, `linkMu_of_full`, `linkMu` or `linkMu_of_linkDIV`: is it in the export (full name), and which declarations mention it, split into "in the proof/body" and "in the statement only"?
3. **`omTied_retie_of_cube`.** Is it in the export, and which declarations mention it (proof/body vs statement only)?
4. **`GeneralHyps`, `GeneralHypU`, `GeneralHypV`.** Is each in the export as a declaration (match by last component, list full names)? If present, which declarations mention it (proof/body vs statement only)?

**Positive control (the run is VOID if it fails):** `riemannHypothesis` must be found to mention `rhOfAll` in its body (Main.lean:4: `theorem riemannHypothesis : RiemannHypothesis := rhOfAll`), and the name list must contain `riemannHypothesis`.

## Output

`notes/export-side-questions.md`: the pre-registered questions, one answer per question with the evidence lists (full declaration names), the control result, and limits: the export covers what `Main` depends on, so it says nothing about declarations outside that closure; "mentions" means the constant appears in the declaration's type or value, not that a proof uses it in any deeper sense. Also add a short plain-language summary Timmy can use when he writes his own comments on issues #5 and #2 (facts only, with the issue each fact answers). Keep the scanning script in `results/export-names/`.

## Last step

Commit and push the note, the script, the compressed list (if under 25 MB) and this prompt, saying Claude Code did the scan and Claude in chat wrote the prompt. Report the four answers in one line each.
