# Rubinstein’s H1 and H6 on the headline family

**COMPILED · 23 Nov 2026.** The files state what holds at every index of the selected family once the scale passes a common threshold. Each takes premises supplied along the headline proof. Each was run through Lean 4.33.1 in the pinned 705-module closure (`lake env lean`); every `#print axioms` shows only `propext`, `Classical.choice` and `Quot.sound`. The statements are unchanged from the drafts.

| File | Theorem | Status | Lean output | Match to Rubinstein (audit) |
|---|---|---|---|---|
| [H1.lean](H1.lean) | `RHX.h1_pairing_size` | **COMPILED** | [H1.out](H1.out) | **same** |
| [H2.lean](H2.lean) | `RHX.h2_level_corrections` | **COMPILED** | [H2.out](H2.out) | **same** |
| [H3.lean](H3.lean) | `RHX.h3_height_comparison` | **COMPILED** | [H3.out](H3.out) | **same** |
| [H6.lean](H6.lean) | `RHX.h6_glued_lattice` | **COMPILED** | [H6.out](H6.out) | **same** |
| [H9.lean](H9.lean) | `RHX.h9_target_slope` | **COMPILED** | [H9.out](H9.out) | **same** |

The match column is from [`notes/batch1-audit.md`](../../notes/batch1-audit.md). H8 is [`CommonPeriodMap2.lean`](../common-period-map/CommonPeriodMap2.lean); the same audit finds it **different**: it does not state Rubinstein's inequality (III.330) and does not connect his three maps to `Bk`.

**Read "same" with this caveat.** In H1, H2, H3, H9 and H6(i) the conclusion is one conjunct of the premise `LinkDIV`, and in `CommonPeriodMap2.lean` (8a) and (8b) are too. So these files show where each hypothesis sits in the code, not a new proof of it. Only H6(ii)(iii) and (8c) go through real source theorems (`slopesNF_of`, `matKF_of`).

**Totals across all 13 hypotheses (H0–H12):** **same** H1, H2, H3, H4, H5, H6, H9 (7); **weaker** H0, H12 (2); **different** H7, H8, H10, H11 (4).

The prose below was written for H1 and H6 while they were drafts; its READ and DERIVED labels describe how the statements were obtained from the source, not their Lean status.

| Draft | Rubinstein v2 | Family statement |
|---|---|---|
| [H1.lean](H1.lean) · `RHX.h1_pairing_size` | H1, equation (III.324) | From `LinkDIV Fm Cabs CH`, one pair of constants `C, x0` works for every scale $x\ge x_0$, index and word. The conclusion displays both error terms. |
| [H6.lean](H6.lean) · `RHX.h6_glued_lattice` | H6(i–iii), equation (III.328) | From `LinkDIV Fm Cabs CH` and `Lnk.PlacesF Fm`, one threshold gives integral inclusion and both slope bounds at the same index. The slope constant is uniform and nonnegative. |

**READ · H1.** In `WordFacts` the integral inclusion, the height bound for a nonzero pairing, and the budget use the same word. The seventh conjunct of `LinkDIV_at` supplies the budget. Its `MAIN u` expands to the sum over the host columns, including the logarithm of that word’s level. The scalar mean-bound proof takes exactly this conjunct, raises its constant to `max Cd 0`, and invokes `M.data_DIV` to get the bundled `DIV`. The generic bridge retains the given exponent `Cabs`. The call to `topDesWin` in `shapeWin` sets it to 2. [Rubinstein, p. 204](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=204) · [RecBridge.lean:128](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L128) · [GlobalTheoremInputs.lean:77](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalTheoremInputs.lean#L77) · [DataParams₂.lean:232](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataParams%E2%82%82.lean#L232) · [MeanBoundSecondForm.lean:118](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L118) · [LossesSmallShares.lean:169](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L169) · [ShapeWin.lean:46](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/ShapeWin.lean#L46)

**READ · H6.** Clause (i) is `OneMapIntoCC`: the image of each source lattice under `D.div.Bk u`, restricted to the ring of integers, lies in the same `D.div.cc`. The second conjunct of `SlopesN_at` gives (ii), the lower bound on mean slope with loss `LoU L C u`. Its first conjunct gives (iii), the upper bound on maximum slope with allowance $C m B_0$. In the source, `slopesN_at_of` uses the local place estimates and `slopesNF_of` lifts it to the family. `LinkMin` supplies those estimates using `placesF_min'` and passes the result to `linkCore` alongside `lD`. `topDesWin` constructs `hD` at the family it selected. [Rubinstein, p. 205](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=205) · [DataArith.lean:180](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataArith.lean#L180) · [QuadraticLogDerivCongr.lean:177](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L177) · [TopDensityNGeSixteen.lean:1529](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1529) · [TopDensityNGeSixteen.lean:1544](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1544) · [LinkMin.lean:714](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L714) · [DesWin.lean:27](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean#L27)

**READ · import check.** Both direct imports occur in the existing [705-module closure list](../common-period-map/closure-files.txt). The selected-family comparison and formulas above use the source pinned at `4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e`.

## Batch 2 hypotheses

**DERIVED.** All seven batch 2 files compiled on 24 Nov 2026 (`lake env lean` in the pinned closure; H12 after building its two extra modules). Each `.out` shows only `propext`, `Classical.choice` and `Quot.sound`. COMPILED means Lean accepted the statement and its proof as written; it does not mean the statement matches Rubinstein's. The match column is from [`notes/batch2-audit.md`](../../notes/batch2-audit.md): only **same** counts as a match to his statement; **weaker** and **different** mean the Lean theorem says something else about the selected family. These statements use the selected-family premises at source commit `4e8bb36`. The first six drafts import modules in the [recorded closure](../common-period-map/closure-files.txt). H12 identifies its two additional imports at the top of the file.

| File | Theorem | Status | Match to Rubinstein (audit) | Family statement and source (READ) |
|---|---|---|---|---|
| [H0.lean](H0.lean) | `RHX.h0_window_sizes` | **COMPILED** ([H0.out](H0.out)) | **weaker** | At every sufficiently late family window scale, the selected model has the required sizes, positivity, nonempty words and set densities. TieGlobal.lean:97, SChain.lean:17,33,53. |
| [H4.lean](H4.lean) | `RHX.h4_word_counts` | **COMPILED** ([H4.out](H4.out)) | **same** | One constant bounds the log level from below and above and controls its variation between words at every family index. QuadraticLogDerivCongr.lean:167,252. |
| [H5.lean](H5.lean) | `RHX.h5_bottom_lattice` | **COMPILED** ([H5.out](H5.out)) | **same** | At level zero the mean slope has a uniform lower bound and the maximum slope a uniform upper bound. QuadraticLogDerivCongr.lean:173,253. |
| [H7.lean](H7.lean) | `RHX.h7_gain_and_losses` | **COMPILED** ([H7.out](H7.out)) | **different** | On late window scales each index has the local gain estimate. Every selected translate has both the prime-sum shortfall and the integral loss bounded by the same allowance. GlobalTheoremInputs.lean:122, LossesSmallShares.lean:201. |
| [H10.lean](H10.lean) | `RHX.h10_discarded_fraction` | **COMPILED** ([H10.out](H10.out)) | **different** | The exponential upper bound from LinkIRR implies the discarded fraction lies in $[0,1/2]$ at every sufficiently large index. GlobalTheoremInputs.lean:55, QuadraticLogDerivCongr.lean:841. |
| [H11.lean](H11.lean) | `RHX.h11_positive_source_rank` | **COMPILED** ([H11.out](H11.out)) | **different** | Every word has source rank at least one, and the mean slope is at most the maximum slope. SumLogPrimeFactorsLe.lean:717, QuadraticLogDerivCongr.lean:185. |
| [H12.lean](H12.lean) | `RHX.h12_family_windows` | **COMPILED** ([H12.out](H12.out)) | **weaker** | A single family and uniform constants work throughout arbitrarily late intervals. The companion theorem `RHX.h12_pair_supply` exposes the good pair and cohomology bound at the supply scale. CharacterBoxes/WinPairs.lean:5, ZeroFreeAllOfTopG.lean:26. |

## Who drafted what

- **H1, H6, and all of batch 2** (H0, H4, H5, H7, H10, H11, H12) were drafted by **Codex**.
- **H2, H3 and H9** were drafted by **Claude** (Opus, in the chat app).
- Commit `d7908cd` labeled H2, H3 and H9 as "Codex drafts". That label is wrong. History is not rewritten; this note is the correction. All compiling was done by Claude Code, and no statement was edited to make it pass.
