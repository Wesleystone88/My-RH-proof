import Formalism.SharpRestriction.GlobalSchurBounds.QuadraticLogDerivCongr

/-!
# H11 · rank of every glued source lattice
READ (4e8bb36). MuRank is wordwise positive rank (SumLogPrimeFactorsLe.lean:717).
LinkMin.lean:680,709,716 supplies it and the stronger LatF on the same family.
Lat_at also compares the mean and maximum (QuadraticLogDerivCongr.lean:185,255).
TieGlobal.lean:65 identifies the rank with the weight d in HidaSetting
(MeanBoundSecondForm.lean:111). Word nonemptiness separately uses TieGlobal.lean:13.
DERIVED. The two wordwise conclusions hold beyond the single LatF threshold.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h11_positive_source_rank {eps : ℝ} (Fm : FamP eps) (hLat : Lnk.LatF Fm) :
    ∃ x0 : ℝ, ∀ x ≥ x0, ∀ (i : Fm.Ix x) (u : (Fm.D x i).what₂.Word),
      1 ≤ ((Fm.D x i).div.Nu u).rank ∧
      ((Fm.D x i).div.Nu u).mu ≤ ((Fm.D x i).div.Nu u).muMax := by
  obtain ⟨x0, h⟩ := hLat
  refine ⟨x0, fun x hx i u => ?_⟩
  exact (h x hx i).1 u

end RHX

end

#print axioms RHX.h11_positive_source_rank
