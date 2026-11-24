import Formalism.SharpRestriction.GlobalSchurBounds.QuadraticLogDerivCongr

/-!
# H10 · discarded rank fraction
READ (4e8bb36). LinkIRR gives exponential decay (GlobalTheoremInputs.lean:55).
LossesSmallShares.lean:210 uses this in FParams (MeanBoundSecondForm.lean:161).
QuadraticLogDerivCongr.lean:841,1050 gives the half bound used for the error window.
DERIVED. Increasing the family threshold to at least one gives both estimates.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h10_discarded_fraction {eps : ℝ} (Fm : FamP eps) (hI : LinkIRR Fm) :
    ∃ x0 : ℝ, ∀ x ≥ x0, ∀ i : Fm.Ix x,
      0 ≤ (Fm.D x i).what₂.delp ∧
      (Fm.D x i).what₂.delp ≤ Real.exp (-(x ^ (Fm.ez / 7))) ∧
      (Fm.D x i).what₂.delp ≤ 1 / 2 := by
  obtain ⟨t, h⟩ := hI
  refine ⟨max t 1, fun x hx i => ?_⟩
  obtain ⟨hn, hu⟩ := h x ((le_max_left _ _).trans hx) i
  have hz : 0 < Fm.ez := by
    rw [← Fm.L_ez x i]
    exact (Fm.L x i).sc.ez_pos
  have hp : 1 ≤ x ^ (Fm.ez / 7) :=
    Real.one_le_rpow ((le_max_right _ _).trans hx) (by positivity)
  exact ⟨hn, hu, hu.trans (Lnk.exp_neg_le_half hp)⟩

end RHX

end

#print axioms RHX.h10_discarded_fraction
