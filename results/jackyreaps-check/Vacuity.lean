import Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen

/-!
His covolume stand-in `∃ C0 : ℝ, 0 ≤ C0 ∧ surviving ≤ C0`
(X-files @ 433c7c6, ThetaConstraints.lean:98-99) holds for every real number `surviving`.
-/

theorem RHX.covolume_model_vacuous (s : ℝ) : ∃ C0 : ℝ, 0 ≤ C0 ∧ s ≤ C0 :=
  ⟨max s 0, le_max_right _ _, le_max_left _ _⟩

#print axioms RHX.covolume_model_vacuous
