import Std
/-! Checks for §7 (the gain (G)) of the note
"From prime-power counts to zero exclusion".
(1) Slope change under twisting, rank 2 over ℤ (base field ℚ): covolume = |det|.
    Twisting by an ideal is scaling by q = p^σ; a general enlargement N' ⊃ N
    multiplies the covolume by the index det B. Both are 2×2 determinant identities.
(2) The place-sum identity Sg(s) = Ga + Fo − Ee (source `ClaimSg`), 2 places × 2 lifts.
(3) The gain lower bound (source `ClaimLow`), 2 places × 2 lifts, with the
    division by d_u already carried out (hypotheses on be(w) directly). -/
set_option linter.unusedSectionVars false
namespace GainCheck
open Lean.Grind
variable {R : Type} [CommRing R] [LE R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]

def det2 (a b c d : R) : R := a * d - b * c

/-- Index formula: if N = A·ℤ² and N = A'·B·ℤ² (B integral), covol N = covol N' · |det B|. -/
theorem det2_mul (a b c d e f g h : R) :
    det2 (a*e + b*g) (a*f + b*h) (c*e + d*g) (c*f + d*h) = det2 a b c d * det2 e f g h := by
  unfold det2; grind

/-- Ideal twist over ℚ is scaling: covol(q·N) = q² covol(N) in rank 2,
so the slope −(2/d)·log covol changes by 2·log q = 2·σ·log p for q = p^σ. -/
theorem det2_smul (q a b c d : R) : det2 (q*a) (q*b) (q*c) (q*d) = q^2 * det2 a b c d := by
  unfold det2; grind

/-- Concrete instance at p = 3: N = 3·N', index 3² = 9. -/
example : det2 (3*2 : Int) (3*1) (3*0) (3*5) = 9 * det2 (2 : Int) 1 0 5 := by decide

/-- A non-scalar local twist at p = 3: N' ⊃ N with N'/N ≅ ℤ/3 (B = diag(3,1)). -/
example : det2 (2*3 + 1*0 : Int) (2*0 + 1*1) (0*3 + 5*0) (0*0 + 5*1) = det2 (2 : Int) 1 0 5 * 3 := by decide

/-- (2) Sg(s) = Ga + Fo − Ee with s(w) = Σ_j (g_j + F_j − E_j)(w); places w ∈ {1,2}, lifts j ∈ {1,2}. -/
theorem claimSg (l1 l2 t1 t2 g11 g21 g12 g22 F11 F21 F12 F22 E11 E21 E12 E22 : R) :
    (2*l1*((g11+F11-E11) + (g21+F21-E21) - t1) + 2*l2*((g12+F12-E12) + (g22+F22-E22) - t2))
    = (2*(l1*((g11+g21) - t1) + l2*((g12+g22) - t2)))
      + (2*((l1*F11 + l2*F12) + (l1*F21 + l2*F22)))
      - (2*((l1*E11 + l2*E12) + (l1*E21 + l2*E22))) := by
  grind

/-- (3) Gain lower bound (ClaimLow), place 1 ordinary, place 2 in W_T (τ₂ = 0).
`hT` is the twisting slope identity; `hbe1` is be(w₁) ≤ τ₁·δ' + io₁·ι' with δ' = δ/(1−δ), ι' = 1/(1−δ);
`hPT` bounds the W_T part; `hR` compares the realized twist σ' with s. -/
theorem claimLow (muN muMu l1 l2 t1 io1 sg1 sg2 be1 lenT PT Rd dp ip
    g11 g21 g12 g22 F11 F21 F12 F22 E11 E21 E12 E22 : R)
    (hl1 : 0 ≤ l1)
    (hT : muN = muMu + (2*l1*(sg1 - t1) + 2*l2*(sg2 - 0)) - (2*l1*be1 + lenT))
    (hbe1 : be1 ≤ t1*dp + io1*ip) (hPT : lenT ≤ PT)
    -- s(w) = Σ_j (g_j + F_j − E_j)(w), substituted
    (hR : 2*l1*(((g11+F11-E11) + (g21+F21-E21)) - sg1)
        + 2*l2*(((g12+F12-E12) + (g22+F22-E22)) - sg2) ≤ Rd) :
    muMu + (2*(l1*((g11+g21) - t1) + l2*((g12+g22) - 0)))
      + (2*((l1*F11 + l2*F12) + (l1*F21 + l2*F22)))
      - (2*((l1*E11 + l2*E12) + (l1*E21 + l2*E22)))
      - Rd - PT - (2*l1*io1)*ip - dp*(2*l1*t1) ≤ muN := by
  have h1 : 2*l1*be1 ≤ 2*l1*(t1*dp + io1*ip) := by
    have h2 : 0 ≤ 2*l1 := by grind
    exact OrderedRing.mul_le_mul_of_nonneg_left hbe1 h2
  grind

end GainCheck
#print axioms GainCheck.det2_mul
#print axioms GainCheck.det2_smul
#print axioms GainCheck.claimSg
#print axioms GainCheck.claimLow
