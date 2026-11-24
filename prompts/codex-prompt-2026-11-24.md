# Codex: tasks for 24 Nov 2026

Rules: read and write only. No git, no builds, no `lake`, nothing in `C:\rhc`.
Source: Alpöge's Lean proof pinned at `4e8bb36` (src tree = upstream `e50d098`).
Label every claim **READ** (quoted from a file), **DERIVED** (our reasoning) or **GUESS**.
Either answer is fine on every question. Report what the source says, including if it contradicts our notes.
Do the tasks in this order. Each writes one new file; do not edit other files.

## 1. Verify the H-rat note (priority)

Check `notes/h-rat-three-identities.md` (written by Claude in chat) against the pinned source and Adriazola's `manuscript/sec14_bessel.tex` at `a29e055` (github.com/jimjamzola/RH-Alpoge-Reconstruction). His Hypothesis H-rat is at line 180 and Lemma `w2:see:rat` at line 372.

- For each row of the note's table, confirm or reject the match, with file:line.
- Check that `jN` and `jEE` really act as φ ↦ φ⊗1 (σ_v-semilinear base change) and that `embLL` plays the role of σ_v.
- Trace whether the proof of the final RH theorem actually reaches `buRat_rrFull_closed` or `BurrbPlug`. Give the chain of declarations, or say where you lose it.

Write to `notes/h-rat-verify.md`.

## 2. Map where anyGeometry enters

`anyGeometry` is defined in `src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean:19` and mentioned in about 24 files.

- List every declaration that uses it and what each one feeds into.
- Follow the chain up to the premises our compiled theorems take: `LinkDIV`, `LinkS`, `ChosenProviso`, `TopG`, `VWin`. For each premise, say whether its construction for the headline family reaches `anyGeometry`, and through which declarations.
- Note `divEx_prov` (`TupPinsOfMuIsW.lean:204`): it uses `trivial` for the filter while `exists_divT` still builds the geometry (`geoOver_stages`, `geo := hG`). Confirm or correct that reading.
- Confirm that `OverIx.lean` and `EveryCharacterE.lean` are absent from `results/common-period-map/closure-files.txt` and from `results/rubinstein-hypotheses/h12-extra-closure.txt`.

Write to `notes/anygeometry-footprint.md`.

## 3. The next layer under Nielsen's rfl claim

`notes/nielsen-rfl-check.md` (Claude, chat) found that the real inequalities come from `divClausesR_of` (`ConstantGeTwentyEight.lean:184`), which takes `DivInputsR`.

- List each field of `DivInputsR` (for example `val2`, `nP`, `nKcb`, `eig6`, `cb`, the `boundsMu` inputs).
- For the headline family, say where each one is supplied and whether that supply is a real proof or holds by construction (`rfl`, `HEq.rfl`, a copied field). Give file:line.

Write to `notes/divinputs-trace.md`.
