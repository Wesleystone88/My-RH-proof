import Formalism.SharpRestriction.GlobalSchurBounds.QuadraticLogDerivCongr

/-!
# H4 · counts of forms
READ (4e8bb36). QuadraticLogDerivCongr.lean:167,252 gives all three bounds.
JointsL.lean:1152 and LinkMin.lean:711 supply CountF to the headline.
LossesSmallShares.lean:194 transports it to Count5 (QuotientSlopeBoundsWith.lean:27).
DERIVED. The same constant and threshold work for every index and both words.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions
open Formalism.MainNotions.Lnk

namespace RHX

theorem h4_word_counts {eps : ℝ} (Fm : FamP eps) (hCount : CountF Fm) :
    ∃ C x0 : ℝ, 0 ≤ C ∧ ∀ x ≥ x0, ∀ i : Fm.Ix x,
      let D := Fm.D x i
      let L := Fm.L x i
      ∀ u : D.what₂.Word,
        ((∑ j ∈ SizeData₂.lifts D, (1 / (D.R.f : ℝ)) * ∑ τ : D.what₂.Tau,
            Real.log (wj D j τ * D.host.v / Real.pi)) + (D.R.m : ℝ) * lgG D -
          C * (L.La + (D.R.m : ℝ) ^ 2 * L.La / D.R.k) ≤ Real.log ((D.mem u).A.T : ℝ)) ∧
        Real.log ((D.mem u).A.T : ℝ) ≤ C * D.R.m * L.sc.L ∧
        ∀ u', |Real.log ((D.mem u).A.T : ℝ) - Real.log ((D.mem u').A.T : ℝ)| ≤
          C * Real.log D.R.k := by
  exact hCount

end RHX

end

#print axioms RHX.h4_word_counts
