# Adriazola's H-rat: the three identities in the Lean source

Author: Timothy Wesley Stone, with Claude (Opus, chat), 24 Nov 2026. This replaces Codex task 4.
Source: Alpöge's Lean proof, pinned at `4e8bb36` (src tree identical to upstream `e50d098`; the line numbers below were read there).
Manuscript: Adriazola, `RH-Alpoge-Reconstruction` at `a29e055`, `manuscript/sec14_bessel.tex`.

Labels: **READ** means quoted from the files. **DERIVED** means our reading of how they match.

## What Adriazola needs

**READ.** Hypothesis H-rat (sec14_bessel.tex:180): for φ ∈ V_u and y ∈ Y, (B_{u,v}(φ⊗1))(y⊗1) lies in σ_v(K) and equals σ_v(B_u(φ)(y)).

**READ.** His new Lemma w2:see:rat (sec14_bessel.tex:372) derives H-rat from three identities:

1. B_u(φ)(y) = Pt_{μ0}(φ, q_y), where q_y is the K-rational vector of the good part with ι0(q_y) = y.
2. perCol_{μ0}(φ⊗1, q⊗1) = σ_v(Pt_{μ0}(φ, q)).
3. (B_{u,v}φ)(ι0 q) = perCol_{μ0}(φ, q).

## Where the Lean source has each one

| His item | Lean | Match (DERIVED) |
|---|---|---|
| H-rat itself | `D7.BuRational`: `Bu u (jN u φ) (jEE x) = embLL (Bk u φ x)`. [RhoDetPrimeEqMuTildeMulChiPow.lean:364](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L364). Here `jN`, `jEE` are `embLL`-semilinear maps taking K-bases to ℂ-bases ([:185](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L185), [:189](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L189)). | Same statement, with `Bu` = B_{u,v}, `Bk` = B_u, `jN`/`jEE` = ⊗1, `embLL` = σ_v. |
| (1) | `colsBk`: `Bk u (eNu x) (eRR y) = C.B (wU u) x y` ([TupUsed.lean:124](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/TupUsed.lean#L124)), and `PairingFactorsThroughPeriods`: `Dc.Pt u t φ F = ζ(u,t) · C.B u φ (ι_t (Pq_t F))` with `ζ(u, μ0) = 1` ([IndefSide.lean:383](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/IndefiniteForms/IndefSide.lean#L383)). | Same at the base tuple. Lean also states it at every tuple t, up to a factor ζ(u,t) ≠ 0, and ζ(u, μ_w) has valuation 0 at w. That looks like his remark that c(t)/c(μ0) is a unit at the primes of the chain (GUESS; not checked). |
| (2) | `RowsHoldDcPt3`: `embLL (Dc.Pt (wU u) t x F) = perCol u (tup t) (jN u (eNu u x)) (jA t (rV0 F))` ([ColumnsFunctionAtSubspaces.lean:141](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/HilbertRowConditions/ColumnsFunctionAtSubspaces.lean#L141)). | Same, and stated at every tuple t, not only μ0. |
| (3) | `Rows.BuDefQ`: `Bu u φ x = perCol u mu0 φ (sec mu0 x)` ([DataBu.lean:32](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataBu.lean#L32)), with `sec (ι q) = q` ([DataBu.lean:22](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataBu.lean#L22)). The literal form is `Rows.PeriodIdentityOnDegreeZero` ([DataBu.lean:38](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataBu.lean#L38)). | Same. |
| His lemma | `buRational_of` uses exactly these three inputs (`hBu`, `hPt`, `hF.l1b` with `hR.colsBk`) and returns `D.BuRational` ([BuRationalOf.lean:26](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/DivisibilityRemainder/RationalColumns/BuRationalOf.lean#L26)). | Same argument as his one-line proof. |
| On the family | `buRat_rrFull_closed` gives `BuRational` at every late index of the selected family, taking `bu_def` from the family's ties ([RationalFamilyRemainingClosed.lean:13](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/Divisibility/DivisibilityRemainder/RationalColumns/RationalFamilyRemainingClosed.lean#L13), [DataTies.lean:42](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataTies.lean#L42)). `RowsHoldDcPt3` is derived for the selected family in WireSel.lean:42. | All three are supplied, not only assumed (DERIVED; see the limits below). |

## Corrections after Codex's check (24 Nov 2026, `notes/h-rat-verify.md`)

Codex checked every row against the source and the manuscript. These corrections stand; the table above is kept as written so the change is visible.

- **H-rat row: confirmed**, for the record's chosen embedding. `BuRational` does not quantify over all embeddings.
- **Row (1): confirmed** after projection and coordinate transport. Our GUESS that ζ matches his c(t)/c(μ0) would need an extra normalization identity; it is not shown.
- **Row (2): confirmed** with the coordinate maps. On the selected realization it also needs "all tuples used", which Lean proves.
- **Row (3): confirmed on good q only.** Calling `PeriodIdentityOnDegreeZero` the literal form was wrong. That statement covers the larger space `V0`, and extending to it also needs vanishing on `Usp` (`PerKillsU`).
- **The lemma: confirmed**, but "exactly these three inputs" overstated it. Lean also proves extra descent and realization steps.
- **Family: confirmed, conditional on the family premises.** The headline route uses the alternate version `buRat_rrFull_closed_alt` in `BurrbPlug.lean`, not the theorem named above. WireSel.lean converts an input (`hDcPtG`); it does not build the period comparison there.
- **The base-change reading is confirmed:** `jN`/`jEE` act as φ ↦ φ⊗1 via a basis argument. Matching `embLL` to his specific place σ_v is part of the model comparison (H-dict).
- **Headline chain traced:** `riemannHypothesis` → `rhOfAll` → `allChi` → `everyCharacter` → … → `shape_closed_link_n_of_green` → `link_brest_alt` → `bRest_all_alt` → `buRat_rrFull_closed_alt` → `buRational_of`. The final theorem does reach this lemma.

## Limits

- The match between Lean names and his symbols (`Bu` ↔ B_{u,v}, `Dc.Pt` ↔ Pt, `jN`/`jEE` ↔ ⊗1 and so on) is our reading of the definitions. It is part of what he calls H-dict, which stays open.
- The route from `riemannHypothesis` to `buRational_of` is now traced at the source level (see the corrections above). This is a reading of declaration bodies, not a kernel-level dependency check.
- Nothing here is compiled by us yet. A Lean file restating the lemma would need modules outside our 705-file list.
