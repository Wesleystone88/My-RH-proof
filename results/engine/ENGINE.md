# The engine card: `Deduction.ch_top`

Source: `homeowmorphism/riemann-hypothesis-original` at `4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e`. Read from the pinned checkout; nothing was built for this card. Labels: **READ** (quoted), **DERIVED** (our reasoning), **GUESS**.

**READ.** Rubinstein's §9 table (v2, pp. 219–222) lists `Deduction.ch_top (ChTop:37)` as the last declaration in the chain `key_identity`, `phi_bound`, `each_unit_bound_statement`, `errX5at_le`, `core_ineq`, `CErr/KBig/LargeX` for his Theorem M. His Remark (1) says the end of the proof (`ch_balance`, `ch_core`, `ch_top`) is stated with the arithmetic quantities `characterSumData.ASK` and `.MAIN`, that `Data.ASK` is a field of the abstract record, and that `IdentU` ties it to the arithmetic. **DERIVED:** I did not check that the statement of his (III.357) is `ch_top`'s conclusion; I only read what `ch_top` proves, below.

## 1. The statement

**READ.** [ChTop.lean:37–44](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L37-L44):

```lean
theorem ch_top {H : Type} [AddCommGroup H] [Fintype H] [DecidableEq H] {U0 : Type} [Fintype U0] {W : U0 → Type}
    [∀ u0, Fintype (W u0)] [∀ u0, Nonempty (W u0)] {Top : Type} [Fintype Top] {m f : ℕ}
    (Dd : Data U0 W Top m f) (tr : U0 → H) (C : Consts) (Xpp eK K : ℝ)
    (D : ArithData H) (ell : AddChar (E0 × H) ℂ → ℂ) (N : ℕ) (TT T2 : Finset H) (a : H → ℝ)
    (w : H → Fin m → E0 × H → ℝ) (eT : Top ≃ TT) (eP : Fin f ≃ PhiSet (H := H))
    (h1 : IdentU Dd tr D N ell TT a w eT eP) (h2 : SizeData₂ Dd C Xpp) (h3 : ErrWindows Dd C Xpp eK K)
    (h4 : BNBoundsU Dd T2) (h5 : LargeX Dd.x Dd.ε K C.cHH eK) (u : U0) :
    gapA D N ell TT a w (tr u) ≤
      Dd.x ^ (CErr C * Dd.ε) * errorBracketSizeWindows Dd.x Dd.ε (Fintype.card H) TT.card T2.card m Dd.b Dd.k Dd.a
```

**In plain words.** Take an abstract record `Dd` of real numbers (a scale `x`, an exponent `ε`, sizes `a, b, b', k, L, La, B0, Nc, v, …`, tops `aT`, weights `w`, and, for every translate `u0` and every word `u` over it, the slopes `muN, muMaxN, muM, muMaxM`, the height `h`, the weights `d`, the level `T`, the lift errors `EeJ`, and per-translate `muCC, muMinCC, Fo, Ga, Ta, ASK, IO, HH, del, η, e`). Suppose five groups of hypotheses. Then for any translate `u`, the arithmetic gap
`gapA = Σ_{t∈TT} Σ_{j<m} (ASK(t,j) − Re MAIN(t,j))` ([SplitInertia.lean:50](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean#L50)) is at most
`x^{CErr·ε} · errorBracketSizeWindows(…)` with `CErr = eDiv + eLoss + 3` ([ErrorFormsWeakWindowsFalse.lean:19, 133](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean#L133)), where `errorBracketSizeWindows = nT·aE·(1 + m²/k) + m·(2n·m·b·x^ε + nT2·k·b·x^ε / (n·(n·x^{-ε})))`.

## 2. The inputs and the hypotheses

**READ.** The record `Data` ([MeanBoundSecondForm.lean:37–77](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L37-L77)) has the 15 scalars above, `aT : Top → ℝ`, `w : U0 → Fin m → Fin f → ℝ`, and the per-word and per-translate fields listed in §1; `Consts` ([:15](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L15)) has `cDiv eDiv cE cH cCount cSlope cSl1 cLoss eLoss cHH`. `h` is just a field `h : (u0) → W u0 → ℝ`.

| Hyp | Statement (READ) | Where |
|---|---|---|
| `h1 : IdentU` | (1) `Dd.aT τ = a (eT τ)`; (2) `Dd.w u j ρ = w (tr u) j (eP ρ)`; (3) `Dd.gam = Real.eulerMascheroniConstant`; (4) `Dd.LpL = (ell chC).re`; (5) `Dd.ASK u = ∑ t∈TT, ∑ j, ASK D N (a t) t (w (tr u) j)` | [SplitInertia.lean:67](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean#L67) |
| `h2 : SizeData₂ Dd C Xpp` | the conjunction of **eleven** clauses (table below) | [SChain.lean:17–19](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SizeWindowBrackets/SChain.lean#L17-L19) |
| `h3 : ErrWindows` | `ErrWindows0` (about 25 size conditions: `1 ≤ x`, `0<ε≤1`, `1 ≤ b`, `x·b ≤ a`, `m ≤ x^{1/2+ε/2}`, `x·m ≤ k ≤ x^{eK}`, `k ≤ a`, `0 ≤ L, La ≤ 2x^ε`, `k·b' ≤ a`, `0 ≤ aT ≤ 2a`, `log\|W u0\| ≤ (k−3) log 2`, `delBar ≤ 1/2`, `ConstsBound C K`, …) and `(etaBar + 4√eBar)·(x^{cHH}·b) ≤ K·x^ε·(nT·a)` | [ErrorFormsWeakWindowsFalse.lean:43–50](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean#L43-L50) |
| `h4 : BNBoundsU Dd T2` | `B0 ≤ 2n·m·b·x^ε` and `Nc ≤ nT2·k·b·x^ε / (n·(n·x^{-ε}))`, `n = card H` | [SplitInertia.lean:74](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean#L74) |
| `h5 : LargeX` | `log x ≤ x^ε` and `KBig K cHH eK ≤ x^ε`, `KBig = 200(1+K)²(1+cHH)(1+eK)` | [ErrorFormsWeakWindowsFalse.lean:52](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean#L52) |

**The eleven clauses of `SizeData₂`** (READ; `Data` fields written `D.…`):

| # | Clause | Statement in words |
|---|---|---|
| 1 | `HidaSetting` | positivity and sizes: `0<x, 0<b, 0≤a, 0≤b', 0<k, 0<v, 0<f`, `0≤aT`, `0<w`, `0<d`, `0<T`, `muN ≤ muMaxN`, `0≤cSl1`, `delBar<1`, `0≤etaBar`, `0≤eBar≤1/4` |
| 2 | `DIV` | `muCC + h − Fo ≤ Σ_t(m(ph(aT t) − aT t·logOm) − aT t·log T) + cDiv·nT·a·La + cDiv·m(B0+Nc)·x^{eDiv ε}`, `logOm = gam + log(π/v) − LpL` |
| 3 | `EComp5` | `\|Ee − m·sumA·lg\| ≤ cE·m·B0` |
| 4 | `HComp` | for two words `u,u'` over one translate: `\|(h u + A log T u) − (h u' + A log T u')\| ≤ cH(nT·a·La + m·B0)` |
| 5 | `Count5` | a lower bound `(Σ_j mean_ρ log(w v/π)) + m·lg − cCount(La + m²La/k) ≤ log T`; `log T ≤ cCount·m·L`; `\|log T u − log T u'\| ≤ cCount·log k` |
| 6 | `Slopes` | `−cSlope·nT·a·La(1+m/k) ≤ muM` and `muMaxM ≤ cSlope·nT·a·La` |
| 7 | `QuotientSlopeBoundsWith` | `muMaxN ≤ muMaxM + Ga + Fo − Ee + cSl1·m·B0` and `muM + Ga + Fo − Ee − Lo5 ≤ muN`, `Lo5 = cSl1·IO + cSl1·nT·m·(a/k+b')·log T + cSl1·Xpp + 1` |
| 8 | `LossBounds` | `ASK − Ga ≤ LoP` and `IO ≤ LoP`, `LoP = cLoss·nT·m·b·x^{eLoss ε}` |
| 9 | `SlopeIneq` | if `0≤del<1`, `0≤η`, `0≤e≤1/4`, `s − muMinCC ≤ HH`, `0<HH`, then `s − log\|W\| − (1−del)⁻¹(4·uF·log(1+HH/uF) + (η+4√e)·HH) ≤ muCC`, `s` = d-weighted mean of `muN − h`, `uF` = max of `muMaxN − h` minus `s` |
| 10 | `HHBound` | `s − muMinCC ≤ HH`, `0<HH`, `HH ≤ x^{cHH}·b` |
| 11 | `FParams` | `0≤del≤delBar`, `0≤η≤etaBar`, `0≤e≤eBar` |

Sources: clauses 1–2, 4, 6, 9–11 in [MeanBoundSecondForm.lean:111–163](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L111-L163); clauses 3, 5, 7, 8 in [QuotientSlopeBoundsWith.lean:19–36](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean#L19-L36).

## 3. How the proof goes (READ, [ChTop.lean:45–72](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L45-L72))

1. `ch_top_main_eq` + `h1` give `gapA = Dd.ASK u − Dd.Main u`. This is where `IdentU` is used and nowhere else.
2. `each_unit_bound_statement` ([LevelOfCongruence.lean:175](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L175)) takes the eleven clauses and bounds `ASK u − Main u ≤ ErrX5at u`.
3. `errX5at_le` ([PChain.lean:613](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/PChain.lean#L613)) bounds `ErrX5at ≤ x^{CErr ε}·ErrText` from `h3` and `h5`.
4. `h4` gives `ErrText ≤ errorBracketSizeWindows`, and a `calc` finishes.

**DERIVED.** The only place `h` (the height) can enter is inside the clauses `DIV`, `HComp`, `SlopeIneq`, where it is a free field; `ch_top` never mentions how `h` is computed.

## 4. Map from the paper's seven bounds (Theorem 2 of `paper/alpoge-claude-rh-reading-notes.md`)

| Paper bound | Source clause | Match |
|---|---|---|
| (G) `μ_M + Ga + Fo − Ee − Lo ≤ μ_N` | clause 7, second conjunct (`Lo5`); the first conjunct is the upper half (`C·m·B0`) | match, the paper's `Lo` is the source's `Lo5` |
| (Dv) `μ_CC + h − Fo ≤ Σ_t[m(ph(a_t) − a_t log Ω) − a_t log τ] + E_div` | clause 2 `DIV`, with `E_div = cDiv·nT·a·La + cDiv·m(B0+Nc)·x^{eDiv ε}` | match |
| (Ct) `Λ₀ ≤ log τ(u)` | clause 5 `Count5`, first conjunct; its other two conjuncts have no paper counterpart | match for the lower bound |
| (E) `Ee ≤ m·A·g + m·B` | clause 3 `EComp5` (two-sided: `\|Ee − m·sumA·lg\| ≤ cE·m·B0`) | match for the upper side |
| (Sl) `−SL ≤ μ_M` | clause 6 `Slopes`, first conjunct; the second (`muMaxM ≤ …`) has no paper counterpart | match |
| (SI) `s − log\|W\| − Φ ≤ μ_CC` | clause 9 `SlopeIneq`, with `Φ` controlled by clauses 10 `HHBound` and 11 `FParams` | match, but `Φ` is an explicit expression in `uF, HH, del, η, e` |
| (L) `ASK − Ga ≤ LoP` | clause 8 `LossBounds`, first conjunct; the second (`IO ≤ LoP`) feeds `Lo5` | match |
| weights `d_u > 0`, `W` finite nonempty | record fields `d`, instance `Nonempty (W u0)`, clause 1 (`0<d`) | match |

**Source clauses with no counterpart in the paper's seven:** clause 1 `HidaSetting` (positivity and ranges), clause 4 `HComp` (differences of `h + A·log T` across words), the two extra conjuncts noted above, clauses 10–11 (the data that make `Φ` explicit), and the groups `h1` (identification), `h3`, `h4`, `h5` (the size windows). **DERIVED:** the paper states the engine with the seven bounds and treats the size windows and the identification as part of "Remark 2.4"; the source makes them explicit hypotheses.
