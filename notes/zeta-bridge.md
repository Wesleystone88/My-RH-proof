# Follow the zeta: how the headline proof reaches Mathlib's `riemannZeta`

**DERIVED.** On the route `riemannHypothesis → rhOfAll → allChi → everyCharacter`, the link between Mathlib's `riemannZeta` / `RiemannHypothesis` and the proof's own objects is **not** supplied by `rfl`, `HEq.rfl`, a copied field or an unproved hypothesis. It is two project theorems with real tactic proofs (`rh_of_every`, `rh_of_right`) plus one Mathlib lemma. The project does not have its own L-function: its zero-freeness predicates are written directly with Mathlib's `DirichletCharacter.LFunction`, so there is no separate link to prove. Pre-registered test: Nielsen's claim, as quoted, is **not supported** by the zeta-link steps. One structure on the headline route is filled by a copied term (`OpenLiteratureStatements`, in `everyCharacter_of_row`); its fields are about Galois representations, not zeta, so it does not meet her description. Details, and what I did not trace, below.

Source: Alpöge's Lean proof at `4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e` (Mathlib at `0df444a360eaa60ab8c11dca51a86af692955474`, from `lake-manifest.json`). I read 22 project files and 2 Mathlib files from GitHub at that commit; no Lean was run and `C:\rhc` was not touched. Labels: **READ** quoted from a file, **DERIVED** our reasoning, **GUESS** not checked.

## The claim being tested

Nielsen (X, 23 Nov): the code "assigns a bundle to hold zeta, and that bundle holds content that matches the Riemann hypothesis. That isn't proving anything." Pre-registered reading: if she is right, the link is supplied by `rfl`, `HEq.rfl`, a copied structure field, or a hypothesis never proved. If she is wrong, the link is a theorem with a real proof term.

## 1. The statement

**READ.** [Main.lean:4][main4]:

```lean
theorem riemannHypothesis : RiemannHypothesis := rhOfAll
```

The theorem has no binders, so there are no extra hypotheses. [Main.lean][main4] has no `open` and sits in no namespace; it imports `Statements` and `Supplements.Kernels.MainTheoremsAll`. `Statements` imports only Mathlib ([Statements.lean:1][stm1]).

**READ.** Mathlib's definition at the pinned revision ([RiemannZeta.lean:185–186][mz]):

```lean
def RiemannHypothesis : Prop :=
  ∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1), s.re = 1 / 2
```

**DERIVED.** The `RiemannHypothesis` in `Main.lean` is Mathlib's. It resolves to the root name, and a project file that imports Mathlib cannot declare another root `RiemannHypothesis` (Lean rejects a duplicate declaration). There are no extra hypotheses in the statement. I did **not** run `#print axioms riemannHypothesis`: `Main` is outside our build, so whether it depends on axioms beyond the standard three is not checked here. I grepped 20 of those project files (all but `Statements.lean` and `HalfPlane.lean`) for `sorry`, `axiom`, `native_decide` and `admit`; none appears.

**READ, side note.** The project's own `RiemannZetaZerosOnLine` ([Statements.lean:3–4][stm3]) is the same formula written out. [Main.lean:6][main6] states `riemannZeta_eq_zero_re : RiemannZetaZerosOnLine := rhOfAll`. **DERIVED:** this typechecks by unfolding the two definitions, so it is a restatement, not a proof step, and it is off the `riemannHypothesis` route.

## 2. The bridge

**READ.** The chain, with where each piece comes from and how it is proved:

| Step | Declaration | From | How it is proved (READ) |
|---|---|---|---|
| 1 | `riemannHypothesis := rhOfAll` ([Main.lean:4][main4]) | project | term: one declaration applied |
| 2 | `rhOfAll := Formalism.VW.rh_of_every allChi` ([MainTheorems.lean:9][mt9]) | project | term: one declaration applied |
| 3 | `Formalism.VW.rh_of_every` ([CritLine.lean:29–32][cl29]) | project | `rh_of_right fun s hs hs1 => by have := h 1 (1 : DirichletCharacter ℂ 1) s hs (Or.inr hs1); rwa [LFunction_modOne_eq] at this` |
| 4 | `DirichletCharacter.LFunction_modOne_eq : LFunction χ = riemannZeta` for `χ : DirichletCharacter ℂ 1` ([DirichletContinuation.lean:67–69][mdc]) | **Mathlib** | `ext; rw [LFunction, ZMod.LFunction_modOne_eq, …]`, a real proof in Mathlib |
| 5 | `Formalism.VW.rh_of_right` ([RhOfRight.lean:5–62][rr5]) | project | 58-line tactic proof: for Re s < 1/2 it uses Mathlib's functional equation `riemannZeta_one_sub` (line 28), `Complex.Gamma_ne_zero_of_re_pos` (line 33) and `Complex.cos_eq_zero_iff` (line 35); Re s = 1/2 is immediate; Re s > 1/2 contradicts the hypothesis |
| 6 | `allChi := UpperTheory.FinalTheorems.everyCharacter` ([MainTheorems.lean:7][mt7]) | project | term |
| 7 | `UpperTheory.EveryCharacter` ([EveryCharacter.lean:13–14][ec13]) | project (a `def`) | the statement `∀ N χ s, 1/2 < s.re → (χ ≠ 1 ∨ s ≠ 1) → DirichletCharacter.LFunction χ s ≠ 0`, written with **Mathlib's** `LFunction` |

**DERIVED.** The exact place a statement about "the project's characters or L-functions" becomes a statement about `riemannZeta` is step 3, through the Mathlib lemma in step 4 (trivial character mod 1) and the project's own step 5. Steps 3 and 5 are ordinary proofs, not definitions. There is nothing to bridge at step 7: `EveryCharacter` already speaks of Mathlib's `DirichletCharacter.LFunction`. Mathlib's name cannot be shadowed by a project declaration of the same name, so every `DirichletCharacter.LFunction` in these files is Mathlib's.

**READ.** A second, independent proof of the same implication exists, off the `Main.lean` route: `UpperTheory.zeta_ne_zero_of_everyCharacter` (same `LFunction_modOne_eq` rewrite) and `UpperTheory.riemannHypothesis_of_everyCharacter`, a direct tactic proof ([RiemannHypothesisOfEveryCharacter.lean:211–226][rhe211]). It feeds `UpperTheory.FinalTheorems.riemannHypothesis` ([MainConclusion.lean:13–14][mc13]).

**READ.** How `EveryCharacter` is obtained (for the cut-off point of this audit):

- `everyCharacter := everyCharacter_of_row galoisLocalGlobalStrong_recParameter` ([MainConclusion.lean:10–11][mc10]).
- `everyCharacter_of_row h := every_character_of_literature_of_vWin ⟨h, recTExists, h⟩ (vwin_of_row h)` ([MainConclusion.lean:7–8][mc7]).
- After the h-rat chain, `UpperTheory.Top.every_character_of_green_v_win` is `imprimitive (zero_free_all_of_green_v_win hG hV h)` ([TopPlug.lean:12–18][tp12]).
- `UpperTheory.Top.imprimitive : ZeroFreeAll → ∀ N χ s, 1/2 < s.re → (χ ≠ 1 ∨ s ≠ 1) → LFunction χ s ≠ 0` is a real proof ([Imprimitive.lean:5–35][imp5]). At [line 10][imp5] it uses `h (PChar.of χ) trivial s hs`, which typechecks because `ZeroFreeAll` unfolds to exactly that instance (below).
- `ZeroFreeAll := ZeroFreeOn fun _ => True`, `ZeroFreeOn Q := ∀ ψ, Q ψ → ψ.ZeroFreeAbove (1/2)`, and `PChar.ZeroFreeAbove ψ θ := ∀ s, θ < s.re → DirichletCharacter.LFunction ψ.χ s ≠ 0` ([ExplicitFormulaErrorOfHostConditions.lean:10–17][efe10]).
- `zero_free_all_of_green_v_win` proves `ZeroFreeAll` from `zeroFreeAll_of_topG` ([ZeroFreeAllOfTopG.lean:26–34][zf26]) applied to `TopG`, which comes from `forall_goal_of_shape_of_hyps … h`, with `supplyChi ψ (hV ψ)` ([TopPlug.lean:12–15][tp12]).

## 3. The bundle

**READ.** Structures, and predicates that behave like structures, whose fields or statements mention `riemannZeta`, `LSeries`, zero-freeness or a zero-free region, and how the headline fills each:

| Candidate | What it holds (READ) | How the headline fills it |
|---|---|---|
| `PChar.ZeroFreeAbove`, `ZeroFreeOn`, `ZeroFreeAll` (defs, [ExplicitFormulaErrorOfHostConditions.lean:10–17][efe10]) | Zero-freeness of Mathlib's `LFunction` above Re = 1/2, for primitive characters `PChar`. This **is** the RH-flavoured content: it is the goal, defined as the statement. | **Real proof.** `ZeroFreeAll` is proved by `zeroFreeAll_of_topG` from `TopG`, `GChi`/`HostExW` and the tied-window theorems ([ZeroFreeAllOfTopG.lean:26–34][zf26]). It is not a field anyone assigns. |
| `Level` (structure, field `o`), `Level.ZeroFreeLevel`, `ChebyshevGrowthImpliesZeroFree` ([lines 7–40][efe10]) | Per-level zero-freeness; `zeroFreeOn_of_levels` assembles `ZeroFreeOn` from it. | `zeroFreeOn_of_levels` has a short proof. I did **not** find where `ChebyshevGrowthImpliesZeroFree` is used; **GUESS:** it is an unused or off-route statement. |
| `TopG` ([ZeroFreeAllOfTopG.lean:12–14][zf12]) | `∀ la G, 1 < la → HostExW la G.req → (… HypV …) → FamilyClassConnected (G.cls la)`; a Prop about families, with no zeta symbol. | Taken as hypothesis `h : TopG` in `zeroFreeAll_of_topG`; supplied by `forall_goal_of_shape_of_hyps` at [TopPlug.lean:14–15][tp12]. Not traced further. |
| `Claim.HalfPlane`, `Claim.Strip`, `Claim.Zeta` ([ClaimStrip.lean][cs59]) | `Claim.zeta_iff : Zeta ↔ RiemannHypothesis := Iff.rfl` ([line 102][cs102]): `Claim.Zeta` **is** the RH statement by definition. | `Claim.zeta (h : HalfPlane) : Zeta` has a real tactic proof ([lines 75–100][cs59]) using `riemannZeta_zero`, `riemannZeta_def_of_ne_zero`, `riemannZeta_ne_zero_of_one_le_re`. Used only by `claimAll` ([MainTheorems.lean:15][mt15]), not by `riemannHypothesis`. |
| `UpperTheory.LiteratureTheorems.OpenLiteratureStatements` (structure : Prop, [EveryCharacterOfLiteratureOfVWin.lean:215–218][ocl215]) | Three fields: `caraianiLocalGlobalDual : One.M.Row`, `localLanglandsExists : Zero.LLC.RecTExists`, `galoisRepOfPolarizedPairLit : One.M.Row`. **No zeta, `LSeries` or zero-free field.** | `⟨h, recTExists, h⟩` ([MainConclusion.lean:8][mc7]): the **same term `h`** fills two fields. Here `h` is the theorem `galoisLocalGlobalStrong_recParameter : Row0b recT := galoisRepresentations_of_thetaLift UpperTheory.TP.K.tLiftK` ([RowSrc.lean:6][rs6]), a term proof; I did not trace `tLiftK`. |

**DERIVED.** If "a bundle assigned to hold zeta" means a structure with a zeta-related field, none on this route is filled by copying or by definition: the zero-free content is a defined Prop proved from `TopG` and related theorems, and `Claim.Zeta` is proved. The one structure on the headline route whose fields are filled by a copied term is `OpenLiteratureStatements`, with `⟨h, recTExists, h⟩`. That is the pattern Nielsen names, but the fields are about Galois representations and local Langlands, not zeta or RH, and `h` is a theorem name, not an unproved hypothesis. The nearest zeta-flavoured named statement in that file is `partial_zeta_functional_equation_of_literature (O) : GlobalTheory.Published.PartialZetaFunctionalEquation := PositivityTheory.Prw.partialZetaFunctionalEquation_holds` ([line 227–228][ocl215]). It ignores `O` and is filled by a named theorem; I did not read that theorem's proof, and it is about partial zeta functions, not `riemannZeta`.

## 4. The inventory

**READ.** Declarations on or next to the route (the files named by `notes/h-rat-verify.md`, plus the bridge files above) whose text mentions `riemannZeta` or `RiemannHypothesis`, found by grepping the project files I read (22):

On the `riemannHypothesis` route:

1. `riemannHypothesis` ([Main.lean:4][main4]).
2. `rhOfAll` ([MainTheorems.lean:9][mt9]).
3. `Formalism.VW.rh_of_every` ([CritLine.lean:29][cl29]).
4. `Formalism.VW.rh_of_right` ([RhOfRight.lean:5, 13, 28][rr5]); `riemannZeta` appears in its statement and proof.

Elsewhere in the same files, off that route:

5. `riemannZeta_eq_zero_re` ([Main.lean:6][main6]) and `RiemannZetaZerosOnLine` ([Statements.lean:3–4][stm3]).
6. `UpperTheory.FinalTheorems.riemannHypothesis` ([MainConclusion.lean:13][mc13]).
7. `UpperTheory.zeta_ne_zero_of_everyCharacter` and `UpperTheory.riemannHypothesis_of_everyCharacter` ([RiemannHypothesisOfEveryCharacter.lean:211, 215][rhe211]).
8. `Claim.zeta` and `Claim.zeta_iff` ([ClaimStrip.lean:75–102][cs59]).

**READ.** The declarations in the chain of `notes/h-rat-verify.md` from `every_character_of_literature_of_vWin` through `buRational_of` contain no `riemannZeta` or `RiemannHypothesis` in the files I read (`EveryCharacterOfLiteratureOfVWin`, `TopPlug`, `TopShape`, `SiegelEisensteinSecondTermHypotheses`, `LinkBrest`, `BrestFinalAll`, `BurrbPlug`, `RationalFamilyRemainingClosed`). The only matches are an import of `RiemannHypothesisOfEveryCharacter` ([line 192][ocl215]), unused in the text, and the partial-zeta statement above.

**How far I looked.** I read the 22 project files named in this note, in full where it matters. I did not clone the whole project, so this is a grep of those files, not of all 175,188 source files. I did not trace the hypotheses `hG : GLq.Green`, `hV : VWin` and `h : Nonempty (HypsAlt …)` upstream of `zero_free_all_of_green_v_win`, the proof of `tLiftK`, or any declaration outside these files. A mention of `riemannZeta` in a file I did not read would be missed.

## 5. The verdict

**DERIVED.** No step from `riemannHypothesis` to `UpperTheory.EveryCharacter` matches the "if she is right" pattern for the zeta link. The statement is Mathlib's `RiemannHypothesis` with no hypotheses ([Main.lean:4][main4]); the passage from the project's `EveryCharacter` to `riemannZeta` is `rh_of_every` plus `rh_of_right`, ordinary tactic proofs using Mathlib's `LFunction_modOne_eq` and functional equation ([CritLine.lean:29–32][cl29], [RhOfRight.lean:5–62][rr5]); and the project states its zero-freeness predicates with Mathlib's `LFunction`, so there is no separate bridge. The definitional pieces I found are `Claim.zeta_iff := Iff.rfl` ([ClaimStrip.lean:102][cs102]) and the `RiemannZetaZerosOnLine` restatement ([Main.lean:6][main6]); neither carries the proof of RH. The one copied-field pattern on the headline route is `⟨h, recTExists, h⟩` at [MainConclusion.lean:8][mc7]. Its fields are not zeta content, and whether `h` and `recTExists` are genuinely proved goes through `galoisRepresentations_of_thetaLift` and `tLiftK`, which I did not trace, so this note says nothing against Nielsen on that point. In the 20 files I grepped I found no `sorry`, `axiom`, `native_decide` or `admit`. I did not check the axioms of `riemannHypothesis` itself, which needs `Main` built.

*Written by Claude Code (reading task, 24 Nov 2026), from `prompts/codex-prompt-2026-11-24b.md`.*

[main4]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Main.lean#L4
[main6]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Main.lean#L6
[stm1]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Statements.lean#L1
[stm3]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Statements.lean#L3-L4
[mz]: https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/NumberTheory/LSeries/RiemannZeta.lean#L185-L186
[mdc]: https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/NumberTheory/LSeries/DirichletContinuation.lean#L67-L69
[mt7]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Supplements/Kernels/MainTheorems.lean#L7
[mt9]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Supplements/Kernels/MainTheorems.lean#L9
[mt15]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Supplements/Kernels/MainTheorems.lean#L15-L16
[cl29]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L29-L32
[rr5]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/GammaFactorNonvanishing/RhOfRight.lean#L5-L62
[ec13]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean#L13-L14
[mc7]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean#L7-L8
[mc10]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean#L10-L11
[mc13]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean#L13-L14
[tp12]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean#L12-L18
[imp5]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/Imprimitive.lean#L5-L35
[efe10]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean#L10-L40
[zf12]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean#L12-L14
[zf26]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean#L26-L34
[rhe211]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/RiemannHypothesisOfEveryCharacter.lean#L211-L226
[cs59]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L75-L102
[cs102]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L102
[ocl215]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L215-L218
[rs6]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean#L6
