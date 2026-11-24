# Claude Code: tasks for 24 Nov 2026

You build and you handle git. Codex reads and writes files only, and may be writing in `notes/` while you work.
Rules: one Lean process at a time, never two builds at once. Do not run `lake exe cache get` for the project.
Stop and report if C: free space drops under 25 GB.

## 1. Compile batch 2

The files are in `results/rubinstein-hypotheses/`. Codex drafted them; `notes/batch2-audit.md` has its audit.

- For each of H4, H5, H0, H7, H10 and H11, in that order:
  1. Make sure the file ends with `#print axioms` for every theorem it declares. Append if missing; do not change any statement.
  2. Copy it into `C:\rhc` and run `lake env lean`.
  3. Save the output as `H*.out` next to the `.lean` file.
- H12 last:
  1. Add the 104 paths in `h12-extra-closure.txt` to the sparse checkout.
  2. `lake build` the two modules H12 imports.
  3. Run it the same way.
- If a file fails, save the error output as its `.out` and move on. Do not edit statements to make them pass.

## 2. Update the README honestly

In `results/rubinstein-hypotheses/README.md`:

- Mark a file COMPILED only if its output shows nothing but `propext`, `Classical.choice`, `Quot.sound`.
- Add each file's match from `notes/batch2-audit.md` (same / weaker / different). Only "same" counts as a match to Rubinstein's statement.
- Attribution: H1, H6 and batch 2 were drafted by Codex; H2, H3 and H9 were drafted by Claude (Opus, chat). Commit `d7908cd` mislabeled H2, H3 and H9 as Codex drafts. Say so in the README, and do not rewrite history.

## 3. Commit and push

Commit everything uncommitted, in logical commits:

- batch 2 and the `.out` files
- `notes/batch2-audit.md`, `notes/adriazola-six-open.md`, `notes/denominator-chain.md` (Codex)
- `notes/h-rat-three-identities.md`, `notes/nielsen-rfl-check.md`, `results/gap2-test-bench/WHY-P.md`, `why_p.py`, `why_p_results.txt` (Claude, chat)
- `notes/RH-proof-handoff.md` (Addendum 41)
- `prompts/` (today's prompt files)

Add `__pycache__/` to `.gitignore`.

If Codex has not finished `notes/h-rat-verify.md`, `notes/anygeometry-footprint.md` or `notes/divinputs-trace.md`, leave those out and commit them in a later run.

Each commit message says who drafted what. Push.

## 4. GitHub topics

If the repo has no topics yet, add `lean4`, `riemann-hypothesis`, `formal-verification` and `number-theory` with `gh repo edit --add-topic`.

## 5. Kernel check for anyGeometry (only after Codex writes notes/anygeometry-footprint.md)

Codex's note names the declarations that build our premises (`LinkDIV`, `LinkS`, `ChosenProviso`, `TopG`, `VWin`) for the headline family.

For each one whose module is already inside the existing build:

1. Write a small Lean file, `results/anygeometry-check/DependsOn.lean`. It walks the constants each declaration uses, transitively, through the environment's `ConstantInfo` values. It reports whether `anyGeometry` appears.
2. Include our own theorems (`RHX.one_map_three_sections`, `RHX.common_period_map`, H1–H9) as a control. They should come out clean, since `OverIx.lean` is not in their closure.
3. Save the output next to the file.

Do not start a new large build for this without asking Timmy first. Either result is fine; report it as it comes out.

## 6. Report

List each H file with its status (COMPILED / failed) and audit match. Give the anyGeometry check results if step 5 ran. Then list the commits you pushed.
