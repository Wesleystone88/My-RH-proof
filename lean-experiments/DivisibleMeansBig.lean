/-!
# Divisible means big (core Lean, no Mathlib)

The one-dimensional case of Bost's slope inequality (`slopeInequality_of` in the repo):
for lattices `L = ℤ·v`, `M = ℤ·w` and `φ(v) = c·w` with `c ≠ 0`,
`slope L ≤ μmax M + log ‖φ‖` reduces to `0 ≤ log |c|`, i.e. `|c| ≥ 1`.
If moreover `N ∣ c`, then `φ / N` is still a lattice map, which gives `N ≤ |c|`:
the total divisibility, measured as `Σ k_p · log p = log N`, is at most the size `log |c|`.
-/

/-- A nonzero whole number divisible by `N` is at least `N`. -/
theorem divisible_means_big (N c : Nat) (hc : 0 < c) (h : N ∣ c) : N ≤ c :=
  Nat.le_of_dvd hc h

/-- The same statement with the divisor written prime by prime. -/
theorem prime_powers_le (p q a b c : Nat) (hc : 0 < c) (h : p ^ a * q ^ b ∣ c) :
    p ^ a * q ^ b ≤ c :=
  Nat.le_of_dvd hc h

/-- Nonzero is essential: `0` is divisible by everything. -/
theorem zero_divisible_by_all (N : Nat) : N ∣ 0 := Nat.dvd_zero N

/-- Factorial, defined here so the file needs only core Lean. -/
def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

/-- 3 divides 100! exactly 48 times (Legendre: 33 + 11 + 3 + 1 = 48) ... -/
example : 3 ^ 48 ∣ fact 100 ∧ ¬ (3 ^ 49 ∣ fact 100) := by decide

/-- ... so by `divisible_means_big`, 3^48 ≤ 100!. -/
example : 3 ^ 48 ≤ fact 100 :=
  divisible_means_big _ _ (by decide) (by decide)

#print axioms divisible_means_big
#print axioms prime_powers_le
