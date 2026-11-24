# Nielsen's "it holds by rfl" claim, checked against the source

Author: Timothy Wesley Stone, with Claude (Opus, chat), 24 Nov 2026.
Source: Alpöge's Lean proof pinned at `4e8bb36` (src tree identical to upstream `e50d098`; the line numbers below were read there).

Labels: **READ** means quoted from the source. **DERIVED** means our reading.

## Her claims (X, 23 Nov 2026)

1. "The lattice conditions hold by rfl / HEq.rfl because the seed is a copy of the row-side data."
2. "The height is installed by setDiv with the explicit formula from the same data, so that equality also holds by rfl."

## What the source says

| Piece | How it is proved | Verdict |
|---|---|---|
| The record's lattices, metric and map equal the column data (`hNu`, `hRR`, `hBk`) | Ties between the record and the column data it was built from; `HEq.rfl` and `rfl` appear in these transport steps. | **Her claim is right here.** These are copies, by construction. |
| The height *equation* `h u = hExpl6 …` (equivalently `R.hu − meanLog κ = h u`) | A definition. `setDiv` sets `h := h` ([SetUnipotentTranslate.lean:25](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/SetUnipotentTranslate.lean#L25)), and `linkDIV_at_words` takes `hh : h u = hExpl6 D L Z Csz u` ([RecBridge.lean:327](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L327)). | **Her claim is right here.** h is an explicit formula, not the measured height of the map. |
| (8a) Lattice *inclusion*: `Bk u` sends the source lattice into `cc` | `WordFacts`, clause 1 ([RecBridge.lean:128](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L128)). It comes from `DivClausesR` clause 1, the column map sending the shifted lattice into the dual lattice ([ConstantGeTwentyEight.lean:111](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/ConstantGeTwentyEight.lean#L111)). That is proved in `divClausesR_of` by `P.cols.intoDual divIntoDualShift latticeGlue …` from valuation inputs ([:184](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/ConstantGeTwentyEight.lean#L184)). | **Not rfl.** An integrality argument, transported through the ties. |
| (8b) Height *bound*: `htMap (Bk u) ≤ h u` | `WordFacts` clause 2, from `DivClausesR` clause 2: operator-norm bounds at every infinite place whose mean log equals the explicit h. These are proved by `height_chain_atR` ([:123](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/ConstantGeTwentyEight.lean#L123)), a chain of norm bounds through the column chain plus an eigenvalue bound, and turned into the height bound by `htMap_le_of_bound` ([RecBridge.lean:161](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L161)). | **Not rfl.** A real inequality: the map's actual height is at most the formula. |
| Budget (Rubinstein H1) | `DivClausesR` clause 3, proved by `P.base.boundsMu … specDet reduction_lemma_zero latticeGlue ramBasic …` in `divClausesR_of`. | **Not rfl.** |
| (8c) `MatK_at`, the near-orthogonal frame | `matKF_of` ([TopDensityNGeSixteen.lean:1348](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1348)), using Hilbert–Schmidt bounds. | Not touched by her claim. |

## Summary (DERIVED)

She is right about the plumbing. The record is a copy of the column data, and the height h is defined by an explicit formula, so those equalities are by construction. That is normal: you define a quantity, then prove things about it.

The inequalities that do the work are not by construction. The integrality behind the lattice inclusion, the bound of the map's actual height by that formula, and the budget all come from `DivClausesR`, which `divClausesR_of` proves with norm-chain, eigenvalue and valuation arguments.

## Also seen

`divEx_prov` ([TupPinsOfMuIsW.lean:204](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L204)) is stated for slots whose geometry setting is `anyGeometry`, and uses `trivial` for that filter. The objects it produces are still built with real geometric data, via `geoOver_stages` and `geo := hG` in `exists_divT`. The filter just is not re-checked at that interface.

## Limits

- `divClausesR_of` takes `DivInputsR` (valuations, norm bounds, eigenvalue bounds). We have not traced how each input is supplied for the headline family. That is the next layer down.
- This is a reading of the source. The proof itself is kernel-checked, but our verdicts on what each step means are not.
