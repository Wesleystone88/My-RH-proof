import Std
/-! Main-term form of the degree bookkeeping behind (Dv)
(source: `DivIneqRecord`, Formalism/QuotientMetricDivisors/ScalarLiftLowerBoundFull.lean:52),
instance with two lifts j ∈ {1,2}, two slots ρ ∈ {1,2}, tops T = {1}.
The period log Ω cancels except for the part carried by a₁. -/
namespace DvCheck
open Lean.Grind
variable {R : Type} [CommRing R] [LE R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]

theorem dv_core
    (muC mu0 Lpass Fo Eb q1 q2 w11 w12 w21 w22 lO h hP h1 h2 lam e1 e2 f11 f12 f21 f22 e6
     a1 lt eP p11 p12 p21 p22 ph1 e11 e12 e21 e22 k d11 d12 d21 d22 : R)
    -- (P1) passage, (P2) ambient degree via Gram determinant and periods
    (P1 : muC ≤ mu0 + Lpass)
    (P2 : mu0 ≤ q1*w11*lO + q1*w12*lO + q2*w21*lO + q2*w22*lO + 2*Fo + Eb)
    -- (H1)-(H4) height of the map
    (H1 : h = hP + h1 + h2 - lam)
    (H2a : h1 ≤ (p11 - (a1 + k*w11 + d11)*lO) + (p12 - (k*w12 + d12)*lO) + e1)
    (H2b : h2 ≤ (p21 - (a1 + k*w21 + d21)*lO) + (p22 - (k*w22 + d22)*lO) + e2)
    (H3 : f11 + f12 + f21 + f22 - e6 ≤ lam)
    (H4 : hP ≤ -(a1*lt) + eP)
    -- (W1) factorial weights; (W2) is substituted into H2a/H2b above
    (W11 : p11 - f11 ≤ ph1 + e11) (W12 : p12 - f12 ≤ e12)
    (W21 : p21 - f21 ≤ ph1 + e21) (W22 : p22 - f22 ≤ e22) :
    muC + h - 2*Fo ≤ (2*(ph1 - a1*lO) - a1*lt)
      + ((q1 - k)*w11 - d11)*lO + ((q1 - k)*w12 - d12)*lO
      + ((q2 - k)*w21 - d21)*lO + ((q2 - k)*w22 - d22)*lO
      + (Eb + Lpass + eP + e1 + e2 + e6 + e11 + e12 + e21 + e22) := by
  grind

end DvCheck
#print axioms DvCheck.dv_core
