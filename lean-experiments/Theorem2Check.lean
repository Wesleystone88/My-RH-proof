import Std

/-! Check of Theorem 2 in the notation of the doc
"From prime-power counts to zero exclusion" (rev 15).
Hypotheses are copied with the doc's orientation; (Dv) is the source's
`DIV` (MeanBoundSecondForm.lean:118-121), unchanged. -/
namespace RHCheck
open Lean.Grind

variable {R : Type} [CommRing R] [LE R] [LT R] [Std.IsLinearOrder R]
  [Std.LawfulOrderLT R] [OrderedRing R]

/-- Theorem 2, pointwise step. `hCt` is A times (Ct), valid because A ≥ 0.
`hKey` is Lemma 2.2. -/
theorem thm2_pointwise
    (muM muN muCC h Ga Fo Ee Lo P A logtau Lam0 Ediv g m B SL Main kc : R)
    (hG   : muM + Ga + Fo - Ee - Lo ≤ muN)
    (hDv  : muCC + h - Fo ≤ P - A * logtau + Ediv)
    (hCt  : A * Lam0 ≤ A * logtau)
    (hE   : Ee ≤ m * A * g + m * B)
    (hSl  : -SL ≤ muM)
    (hKey : P - A * Lam0 + m * A * g = Main + A * kc) :
    Ga + muCC - Main - A * kc - SL - m * B - Ediv - Lo ≤ muN - h := by
  grind

/-- Theorem 2, final step: (SI) removes muCC, (L) replaces Ga by ASK. -/
theorem thm2_final (ASK Ga Main muCC s E logW Phi LoP : R)
    (hAvg : Ga + muCC - Main - E ≤ s)
    (hSI  : s - logW - Phi ≤ muCC)
    (hL   : ASK - Ga ≤ LoP) :
    ASK - Main ≤ LoP + E + logW + Phi := by
  grind

/-- (Dv) rearranged correctly: it gives a LOWER bound on Fo - h. -/
theorem dv_gives_lower_bound (muCC h Fo P A logtau Ediv : R)
    (hDv : muCC + h - Fo ≤ P - A * logtau + Ediv) :
    muCC - P + A * logtau - Ediv ≤ Fo - h := by
  grind

/-- The review's rearrangement `Fo - h ≤ P - A log τ + E_div - μ_CC`
does not follow from (Dv): explicit integers satisfy (Dv) and violate it. -/
theorem review_rearrangement_fails :
    ∃ muCC h Fo P A logtau Ediv : Int,
      muCC + h - Fo ≤ P - A * logtau + Ediv ∧
      ¬ (Fo - h ≤ P - A * logtau + Ediv - muCC) :=
  ⟨0, 0, 1, 0, 0, 0, 0, by decide⟩

end RHCheck

#print axioms RHCheck.thm2_pointwise
#print axioms RHCheck.thm2_final
#print axioms RHCheck.dv_gives_lower_bound
#print axioms RHCheck.review_rearrangement_fails
