import Formalism.SharpRestriction.GlobalSchurBounds.QuadraticLogDerivCongr

/-!
# H5 · slopes of the bottom lattice
READ (4e8bb36). LinkMin.lean:713 supplies SlopesMF to the headline using
slopesMF_of_count_fam (SlopesMFOfCountFam.lean:25). QuadraticLogDerivCongr.lean:173,253
identifies the lattice at level zero. LossesSmallShares.lean:196 transports the two
bounds to Data.Slopes (MeanBoundSecondForm.lean:139).
DERIVED. One nonnegative constant bounds the mean below and the maximum above.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h5_bottom_lattice {eps : ℝ} (Fm : FamP eps) (hSM : Lnk.SlopesMF Fm) :
    ∃ C x0 : ℝ, 0 ≤ C ∧ ∀ x ≥ x0, ∀ i : Fm.Ix x,
      let D := Fm.D x i
      let L := Fm.L x i
      ∀ u : D.what₂.Word,
        -(C * D.host.TT.card * L.sc.a * L.La * (1 + (D.R.m : ℝ) / D.R.k)) ≤
          ((D.fm u).lat 0).mu ∧
        ((D.fm u).lat 0).muMax ≤ C * D.host.TT.card * L.sc.a * L.La := by
  exact hSM

end RHX

end

#print axioms RHX.h5_bottom_lattice
