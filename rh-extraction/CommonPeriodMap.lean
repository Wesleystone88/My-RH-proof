import Formalism.SharpRestriction.GlobalTheoremInputs

/-!
# The common period map (expert-map gaps 2 and 4)

Pinned source: Deicyde/riemann-hypothesis @ e50d09817ad81469f737e8f637561e6ccf86c670
(the `original` branch of leanprover-community/riemann-hypothesis). This file adds nothing to
the proof. It checks that three inputs the proof uses at one family member are statements about
one and the same linear map:

* the divisibility receipt `OneMapIntoCC` (part of `LinkDIV_at`) is about `D.div.Bk u`;
* `BesselId` (also part of `LinkDIV_at`) says `D.div.Bk u` is, after the field embedding, a nonzero
  multiple `a` of the Bessel period `D.besS u`, up to isometries `U` (per word) and `V` (common);
* `D.besS u` is the matrix coefficient of the period map `D.s.Pu u` (`besS_eq`), and the
  near-isometry in `LinkS_at` is a bound on `S.KD D u u = S.Kmat D.s u u`, the Gram operator of
  the same `D.s.Pu u` normalized by `S.c0` (`KD_eq`; see `Kmat` in RelevantZeroGramTerms.lean:339).
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

/-- The Bessel period is the matrix coefficient of the period map `D.s.Pu u` against `D.sEE F`.
This restates the source definition (RhoDetPrimeEqMuTildeMulChiPow.lean:353). -/
theorem besS_eq (D : D7) (u : D.what₂.Word) (φ : D.what₂.Mu u) (F : D.what₂.EE) :
    D.besS u φ F =
      inner ℂ (D.sEE F) (D.s.Pu u ((D.s_Cu u).symm ⟨(D.eMu u φ).1, (D.eMu u φ).2.1⟩)) :=
  rfl

/-- The operator measured by `hsDiagFull` (and so by `LinkS_at`) is the normalized Gram operator
`Kmat` of the period maps `D.s.Pu` (RelevantZeroGramTerms.lean:339, 509). -/
theorem KD_eq (D : D7) (u u' : D.what₂.Word) : S.KD D u u' = S.Kmat D.s u u' :=
  rfl

/-- One family member. The receipt, the Bessel identity and the near-isometry all concern the
map `D.div.Bk u`, which equals `a • besS u (U ·) (V ·)` on rational vectors. -/
theorem common_period_map {D : D7} {L : SizeData₂ D} {C Cabs CH C0 Gam eta0 eta1 e0 : ℝ}
    (hD : LinkDIV_at L C Cabs CH) (hS : LinkS_at L C0 Gam eta0 eta1 e0)
    (hP : ∀ u, C0⁻¹ ≤ (D.duS u : ℝ) * Gam ^ 2 / D.what₂.Dstar ∧
      (D.duS u : ℝ) * Gam ^ 2 / D.what₂.Dstar ≤ C0) :
    D.div.OneMapIntoCC ∧
    (∃ V : D.what₂.EE ≃ₗᵢ[ℂ] D.what₂.EE, ∀ u, ∃ a : ℂ, a ≠ 0 ∧
      ∃ U : D.what₂.Mu u ≃ₗᵢ[ℂ] D.what₂.Mu u,
        ∀ (φ : (D.div.Nu u).V) (x : D.div.RR.V),
          D.what₂.embLL (D.div.Bk u φ x) = a * D.besS u (U (D.jN u φ)) (V (D.jEE x))) ∧
    (∀ u, hsDiagFull D u ≤ e0 * (D.duS u : ℝ)) := by
  obtain ⟨h1, -, -, hB, -⟩ := hD
  obtain ⟨hRat, V, hV⟩ := hB
  refine ⟨h1, ⟨V, fun u => ?_⟩, (hS hP).2.1⟩
  obtain ⟨a, ha, U, hU⟩ := hV u
  exact ⟨a, ha, U, fun φ x => by rw [← hRat u φ x, hU]⟩

/-- The family version, from the three inputs the headline proof supplies
(`LinkDIV`, `LinkS`, `ChosenProviso`; see `matKF_of`, TopDensityNGeSixteen.lean:1348). -/
theorem common_period_map_family {eps : ℝ} (Fm : FamP eps) {Cabs CH C0 : ℝ}
    (lD : LinkDIV Fm Cabs CH) (lS : LinkS Fm C0) (cPr : ChosenProviso Fm C0) :
    ∃ x0 : ℝ, ∀ x ≥ x0, ∀ i : Fm.Ix x, ∃ e0 : ℝ, Real.sqrt e0 ≤ Real.exp (-(x ^ (eps / 8))) ∧
      (Fm.D x i).div.OneMapIntoCC ∧
      (∃ V : (Fm.D x i).what₂.EE ≃ₗᵢ[ℂ] (Fm.D x i).what₂.EE, ∀ u, ∃ a : ℂ, a ≠ 0 ∧
        ∃ U : (Fm.D x i).what₂.Mu u ≃ₗᵢ[ℂ] (Fm.D x i).what₂.Mu u,
          ∀ (φ : ((Fm.D x i).div.Nu u).V) (y : (Fm.D x i).div.RR.V),
            (Fm.D x i).what₂.embLL ((Fm.D x i).div.Bk u φ y) =
              a * (Fm.D x i).besS u (U ((Fm.D x i).jN u φ)) (V ((Fm.D x i).jEE y))) ∧
      (∀ u, hsDiagFull (Fm.D x i) u ≤ e0 * ((Fm.D x i).duS u : ℝ)) := by
  obtain ⟨a0, lS⟩ := lS
  obtain ⟨a1, cPr⟩ := cPr
  obtain ⟨C, a2, lD⟩ := lD
  refine ⟨max a0 (max a1 a2), fun x hx i => ?_⟩
  have g0 : x ≥ a0 := le_trans (le_max_left _ _) hx
  have g1 : x ≥ a1 := le_trans (le_trans (le_max_left _ _) (le_max_right _ _)) hx
  have g2 : x ≥ a2 := le_trans (le_trans (le_max_right _ _) (le_max_right _ _)) hx
  obtain ⟨eta0, eta1, e0, -, -, -, hse, hS⟩ := lS x g0 i
  exact ⟨e0, hse, common_period_map (lD x g2 i) hS (cPr x g1 i)⟩

end RHX

end

#print axioms RHX.besS_eq
#print axioms RHX.KD_eq
#print axioms RHX.common_period_map
#print axioms RHX.common_period_map_family
