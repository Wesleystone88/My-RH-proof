import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Real scalar consequences of the size-window inequality. The observable
and the design data are free variables, so these lemmas expose the external
arithmetic assumptions in any application. -/
namespace RHExtraction

/-- Once the derivative estimate has been divided by the isolated pole's
growth rate, its two geometric errors cannot dominate a positive residue
along an unbounded sequence of derivative orders. -/
theorem geometric_pole_contradiction {c M C u v : ℝ} (hc : 0 < c)
    (hu : 0 ≤ u) (hu' : u < 1) (hv : 0 ≤ v) (hv' : v < 1)
    (late : ∀ N : ℕ, ∃ k ≥ N, c ≤ M * u^k + C * v^k) : False := by
  have U := (tendsto_pow_atTop_nhds_zero_of_lt_one hu hu').const_mul M
  have V := (tendsto_pow_atTop_nhds_zero_of_lt_one hv hv').const_mul C
  have small := (U.add V).eventually_lt_const (show M * 0 + C * 0 < c by simpa using hc)
  obtain ⟨N, hN⟩ := Filter.eventually_atTop.1 small
  obtain ⟨k, hk, h⟩ := late N
  exact (not_lt_of_ge h) (hN k hk)

/-- Divide the design inequality exactly, before making any estimates.
In the last term the density of T₂ cancels. Here h is x^ε, P is x^(Cε)
and X is x^(1/2+ε). The statement only needs their actual values. -/
theorem normalized_bridge {n t s m b k x h P X a G err : ℝ}
    (hn : 0 < n) (ht : 0 < t) (hs : 0 < s) (hm : 0 < m)
    (hb : 0 < b) (hk : 0 < k) (hx : 0 < x)
    (balance : t*m*b*(s/n/2)*(G-4*X) ≤ err + 2*t*m*b/x)
    (budget : err ≤ P*(t*a*(1+m^2/k) +
        2*n*m^2*b*h + m*s*k*b*h^2/n^2)) :
    G ≤ 4*X + P*(2*(n/s)*(a/(m*b))*(1+m^2/k) +
      4*(n/s)*(n/t)*m*h + 2*(k/n^2)*(n/t)*h^2) + 4*(n/s)/x := by
  let L := t*m*b*(s/n/2)
  have hL : 0 < L := by dsimp [L]; positivity
  apply le_of_mul_le_mul_left (a := L) _ hL
  have cancel : L*(4*X + P*(2*(n/s)*(a/(m*b))*(1+m^2/k) +
      4*(n/s)*(n/t)*m*h + 2*(k/n^2)*(n/t)*h^2) + 4*(n/s)/x) =
      L*(4*X) + P*(t*a*(1+m^2/k) + 2*n*m^2*b*h + m*s*k*b*h^2/n^2)
      + 2*t*m*b/x := by
    dsimp [L]
    field_simp
    ring
  rw [cancel]
  change L*(G-4*X) ≤ _ at balance
  linarith only [budget, balance, mul_sub L G (4*X)]

/-- A window at every positive loss excludes every real part above 1/2,
provided the window contradiction holds at every exponent strictly between
1/2 and the proposed zero. Smallness thresholds can depend on the loss. -/
theorem exclude_right_zero {Window : ℝ → Prop} {β c ε₀ : ℝ}
    (hε₀ : 0 < ε₀) (hc : 0 < c)
    (supply : ∀ ε, 0 < ε → ε < ε₀ → Window (1/2 + c*ε))
    (pole : ∀ θ, 1/2 < θ → θ < 1 → θ < β → ¬ Window θ) : β ≤ 1/2 := by
  by_contra! hβ
  let b := min β 1
  have hb : 1/2 < b := lt_min hβ (by norm_num)
  let ε := min (ε₀/2) ((b-1/2)/(2*c))
  have hε : 0 < ε := lt_min (by positivity) (div_pos (by linarith) (by positivity))
  have hsmall : ε < ε₀ := lt_of_le_of_lt (min_le_left _ _) (by linarith)
  have hgap : ε * (2*c) ≤ b-1/2 :=
    (le_div_iff₀ (by positivity : 0 < 2*c)).mp (min_le_right _ _)
  have hθ : 1/2 + c*ε < b := by linarith
  exact pole _ (by linarith [mul_pos hc hε]) (hθ.trans_le (min_le_right _ _))
    (hθ.trans_le (min_le_left _ _)) (supply ε hε hsmall)

#print axioms normalized_bridge
#print axioms geometric_pole_contradiction
#print axioms exclude_right_zero
end RHExtraction
