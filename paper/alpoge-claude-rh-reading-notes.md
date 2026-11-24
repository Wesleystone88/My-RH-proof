# From prime-power counts to zero exclusion: three theorems extracted from the Alpöge formalization

Nov 22, 2026 · @Timmy

## The proof on one page

The proof turns RH into a bound on a prime-power count. It then proves that bound with Chebyshev's squeeze, run on a much larger object. Two of its inputs are machine-checked in Lean but not yet written as paper proofs.

**The picture.** Take the middle binomial coefficient C(2n, n). Two facts pull against each other: it is a whole number below 4^n, and every prime between n and 2n divides it. A number with many forced prime factors must be large, so the size cap limits how many primes fit in that range. Divisibility against size is Chebyshev's method for counting primes.

The Alpöge–Claude proof runs the same squeeze on a lattice instead of a binomial coefficient. Divisibility becomes "gains": a map that lands inside a high power of a prime. Size becomes the lattice's slope, computed exactly from periods. The squeeze pins a prime-power count to within about √x of its expected value, and that is RH.

**The five steps.**

1. **RH as a counting bound (§1, §4).** For each character, a weighted prime-power sum must stay below x^(1/2+ε) on long windows. Theorem 3, a window form of Landau's theorem, shows such bounds exclude zeros right of the line. *Proved here.*
2. **The count as characters (§2, Theorem 1).** The gap between an actual prime-power count and its expected value is an exact combination of those sums. *Proved here; algebra.*
3. **The squeeze (§3, Theorem 2).** If a lattice construction meets seven slope and degree bounds, the gap is at most x/m + m + √x. With m ≈ √x theta lifts, that is about √x. *Proved here, given the seven bounds.*
4. **The construction (Construction Hypothesis).** A chain of m theta lifts meets all seven bounds. Everything new lives here. *Machine-checked in Lean only, certified 21 Nov 2026.* Our audit (§6–§12) traces its two hardest bounds, divisibility (Dv) and gain (G).
5. **The bridge (§5, B).** The averaged count controls each target character, provided the auxiliary twists stay quiet. Its inputs are classical: Siegel–Walfisz, Page, Siegel and zero density. *Machine-checked; read in source, not re-derived.*

Steps 3–5 give the window bound for every character. Step 1 turns it into GRH, and the trivial character gives RH.

**What a human-readable proof still needs.**

- **A paper proof of step 4.** Experts flag one point inside it: the same map must give the lattice inclusion, the height bound and the rank bound (Rubinstein H8 and O25; Zhang Lemma 4.2 and Prop. 4.3). Our lemma (§12) ties the integer map to the period map by an exact coefficient identity. A second lemma shows the same map meets all three: inclusion, height, and the archimedean block that feeds the rank estimate. Both lemmas compile in Lean using only the three standard axioms. Naming the classical objects is still open.
- **A paper proof of step 5.** It is long but classical.
- **One caution for any write-up.** The Lean route fills a "geometry" slot with an always-true condition (`anyGeometry`). Validity is unaffected, since the final statement is Mathlib's own RH with only standard axioms. A paper proof should not claim a geometric input at that step.

## Scope and status

The formalization's headline reduces to three theorems: an exact identity, a conditional amplified bound, and a window version of Landau's theorem. This note proves the identity and the window theorem completely. It proves the amplified bound from one explicitly stated hypothesis, the Construction Hypothesis, which it does not prove.

Together with the Construction Hypothesis and a bridge step (§5), the three give GRH for every Dirichlet L-function. Ordinary RH is the case of the trivial character.

- **Proved here:** Theorem 1 (algebra), Lemmas 2.1–2.3 and Theorem 2 (geometry of numbers, class field theory and linear inequalities), Lemma 3.2, Theorem 3 (complex analysis), and Proposition 1.2 (from the standard explicit formula).
- **Stated, not proved here:** the Construction Hypothesis (§3) and the bridge (§5). The formalization claims machine-checked proofs of both, and they make up most of its 17 million lines. We have read their statements in source but have not re-derived them.
- **Not used:** any Lean notation in the main argument. The appendix maps each statement to its source location.

Attribution: Addendum 27 of the handoff, which this note expands, was written by Claude. It was not written by Codex.

## 1. The zero detectors

Each Dirichlet L-function gets a detector: a ramp-weighted prime sum minus its predictable part. What is left is a sum over the zeros only.

**Notation.** Λ is the von Mangoldt function, γ is Euler's constant, and (v)₊ = max(v, 0). For a primitive Dirichlet character χ and real y > 0 define the following (when y < 1 the sums are empty, so only the linear terms remain; Theorem 1 uses these values at a/w(πg), which may be below 1)

```latex
G_1(y)=\sum_{n\le y}\Lambda(n)\Big(\frac yn-1\Big)-y\log y+(1+\gamma)\,y,
\qquad
G_\chi(y)=\sum_{n\le y}\Lambda(n)\chi(n)\Big(\frac yn-1\Big)+y\,\frac{L'}{L}(1,\chi)\quad(\chi\ne 1).
```

Since L(s, χ̄) is the complex conjugate of L(s̄, χ), we have G\_χ̄(y) = conj G\_χ(y).

**Lemma 1.1 (Mellin transform).** For Re s > 1,

```latex
H_\chi(s):=\int_1^\infty G_\chi(y)\,y^{-s-1}\,dy=-\frac{L'}{L}(s,\chi)\,\frac{1}{s(s-1)}+\frac{c_\chi}{s-1}+\frac{b_\chi}{(s-1)^2},
```

where c\_χ = L′/L(1, χ) and b\_χ = 0 for χ ≠ 1, and c\_1 = 1 + γ, b\_1 = −1. H\_χ extends meromorphically to ℂ and is holomorphic at s = 1. In Re s > 0 its poles are exactly the zeros ρ of L(s, χ), with residue −ord\_ρ L(s, χ) / (ρ(ρ − 1)).

*Proof.* For n ≥ 1 and Re s > 1, the integral of (y/n − 1) y^(−s−1) over \[n, ∞) equals n^(−s) / (s(s − 1)). Summing gives the first term. The integrals of y and y log y against y^(−s−1) are 1/(s − 1) and 1/(s − 1)².

For χ ≠ 1, L(1, χ) ≠ 0 (Dirichlet), so −L′/L(s, χ)/(s(s − 1)) has a simple pole at 1 with residue −c\_χ, which the second term cancels. For χ = 1, −ζ′/ζ(s) = 1/(s − 1) − γ + O(s − 1), and 1/s = 1 − (s − 1) + O((s − 1)²). Hence −ζ′/ζ(s)/(s(s − 1)) = 1/(s − 1)² − (1 + γ)/(s − 1) + O(1), which the two correction terms cancel. The residues at the zeros come from the simple poles of L′/L. ∎

**Proposition 1.2 (GRH gives y^(1/2) with no logarithm).** If every nontrivial zero of L(s, χ) has real part 1/2, then |G\_χ(y)| ≤ C\_χ y^(1/2) for all y ≥ 2.

*Proof.* The standard explicit formula (\[Davenport, ch. 17 and 19\]; \[Montgomery–Vaughan, ch. 12\]) gives

```latex
G_\chi(y)=-\sum_{\rho}\frac{y^{\rho}}{\rho(\rho-1)}+O_\chi(1+\log y),
```

with the sum over nontrivial zeros. The O-term collects the trivial zeros and the point s = 0, where an even χ has a double pole and so contributes a multiple of log y. The ramp weight makes the integrand decay like |s|^(−2), so the contour shift is justified and the sum converges absolutely, because Σ 1/|ρ|² < ∞. Under GRH, |y^ρ| = y^(1/2), so the zero sum is at most y^(1/2) Σ 1/|ρ(ρ − 1)|. ∎

*Remark (on GPT's two cautions).*

- The familiar √x (log x)² belongs to the unweighted sum ψ(x, χ). The ramp weight (y/n − 1) is what removes the logarithms.
- A bound on a positive combination of detectors does not bound each detector. Theorem 3 does not need that: with positive weights, the zeros of every member still show up as poles, and their residues add without cancelling.

## 2. Theorem 1: the arithmetic identity

A prime-power count restricted to Frobenius classes off an index-2 subgroup, minus its main term, equals a finite combination of the detectors of §1 with explicit weights. The identity is pure algebra. It holds for any constants ℓ(ψ), and the arithmetic enters only when ℓ is chosen.

**Setting.**

- G is a finite abelian group, written additively, with an index-2 subgroup Φ. Let κ be the character of G with kernel Φ.
- Fix c ∈ G \\ Φ and t ∈ Φ. Put π(g) = c + g + t. Then π is a bijection from G \\ Φ onto Φ.
- Each prime p has an element Frob\_p ∈ G and a subgroup I\_p ≤ G. There is a finite set S = {2, q, d} of primes with:
  - I\_p = 0 for p ∉ S;
  - for p ∈ {2, q}: Frob\_p ∈ Φ and I\_p ≤ Φ;
  - I\_d = {0, e} with e ∉ Φ.
- For a character ψ of G, define the multiplicative function ψ̃ by averaging over inertia:

```latex
\tilde\psi(p^v)=\frac1{|I_p|}\sum_{h\in I_p}\psi\big(v\,\mathrm{Frob}_p+h\big).
```

- Fix complex numbers ℓ(ψ) for ψ ≠ 1. Let G\_1 be as in §1, and for ψ ≠ 1 let G\_ψ(y) = Σ\_{n≤y} Λ(n) ψ̃(n)(y/n − 1) + ℓ(ψ) y.

**The count and its main term.** For a > 0 and weights w : Φ → (0, ∞), define

```latex
A=\sum_{p\notin S}\ \sum_{\substack{v\ge1\\ v\,\mathrm{Frob}_p\notin\Phi}}2\log p\,\Big(\frac a{p^v}-w\big(\pi(v\,\mathrm{Frob}_p)\big)\Big)_{+}
\;+\;\log d\sum_{v\ge1}\ \sum_{\substack{g\in v\,\mathrm{Frob}_d+I_d\\ g\notin\Phi}}\Big(\frac a{d^v}-w(\pi g)\Big)_{+},
```

```latex
\mathrm{Main}=a\Big(\log a-1-\gamma+\ell(\kappa)-\frac1{|\Phi|}\sum_{\rho\in\Phi}\log w(\rho)\Big).
```

**Theorem 1.** In this setting,

```latex
A-\mathrm{Main}=\frac1{|\Phi|}\sum_{g\in G\setminus\Phi}w(\pi g)\sum_{\psi\in\widehat G}\overline{\psi(g)}\;G_\psi\!\Big(\frac{a}{w(\pi g)}\Big).
```

*Proof.* Write w\_g = w(πg) and y\_g = a/w\_g. For n ≤ y\_g, w\_g(y\_g/n − 1) = (a/n − w\_g)₊, and for n > y\_g the positive part is 0. So w\_g G\_ψ(y\_g) splits into a prime part, Σ\_n Λ(n) ψ̃(n)(a/n − w\_g)₊, and a smooth part. The smooth part is −a log(a/w\_g) + (1 + γ)a for ψ = 1, and a ℓ(ψ) for ψ ≠ 1.

*Prime part.* The coefficient of Λ(p^v)(a/p^v − w\_g)₊ is (1/|Φ|) Σ\_ψ conj ψ(g) ψ̃(p^v). By orthogonality on G, and since |G| = 2|Φ|, this equals

```latex
\frac{2}{|I_p|}\;\#\{h\in I_p:\ g=v\,\mathrm{Frob}_p+h\}.
```

- For p ∉ S, it is 2 when g = v Frob\_p and 0 otherwise.
- For p ∈ {2, q}, every v Frob\_p + h lies in Φ while g does not, so it is 0.
- For p = d, it is 2/|I\_d| = 1 when g ∈ v Frob\_d + I\_d.

Summing over g ∉ Φ gives exactly A, because Λ(p^v) = log p.

*Smooth part.* For ψ ≠ 1, Σ\_{g∉Φ} conj ψ(g) = Σ\_{g∈G} − Σ\_{g∈Φ}. This is −|Φ| if ψ = κ and 0 otherwise. There are |Φ| elements g ∉ Φ, and π is a bijection onto Φ. So the smooth parts add up to

```latex
-a\log a+(1+\gamma)a+\frac a{|\Phi|}\sum_{\rho\in\Phi}\log w(\rho)-a\,\ell(\kappa)=-\mathrm{Main}.\qquad\blacksquare
```

**Reading.**

- For p ∉ S, v Frob\_p ∉ Φ means κ(Frob\_p) = −1 and v is odd. So the first sum in A carries the weight Λ(n)(1 − κ(n)): it counts odd powers of primes inert in the quadratic field cut out by κ.
- In the application, κ cuts out K = ℚ(√−d) with d ≡ 7 (mod 8). Three hypotheses force this:
  - d ramifies, since I\_d contains e ∉ Φ;
  - 2 splits, since Frob\_2 and I\_2 lie in Φ;
  - complex conjugation lies outside Φ.

**Lemma 2.3 (the characters are Dirichlet characters).** Let F/ℚ be a finite abelian extension and G = Gal(F/ℚ). For each prime p, let I\_p be its inertia group and Frob\_p any element of its Frobenius coset, which is well defined modulo I\_p. For ψ ∈ Ĝ, let χ\_ψ be the primitive Dirichlet character that corresponds to ψ under class field theory. Then ψ̃(n) = χ\_ψ(n) for every n ≥ 1. Hence, with ℓ(ψ) = L′/L(1, χ\_ψ), G\_ψ is the detector of χ\_ψ from §1.

*Proof.* By Kronecker–Weber, F ⊂ ℚ(ζ\_N) for some N, and G is a quotient of (ℤ/N)^×. So ψ is a Dirichlet character mod N, and χ\_ψ is the primitive character inducing it, with conductor f dividing N. There are three cases:

- p ∤ N. Then I\_p = 0, so ψ̃(p^v) = ψ(Frob\_p)^v = χ\_ψ(p)^v.
- p | N. Then I\_p is the image of the factor (ℤ/p^(v\_p(N)))^×, so ψ is trivial on I\_p exactly when p ∤ f.
  - If p | f, then ψ̃(p^v) averages a nontrivial character over I\_p. So it is 0, which equals χ\_ψ(p^v).
  - If p ∤ f, then p is unramified in the fixed field of ker ψ. So ψ(Frob\_p) is well defined and equals χ\_ψ(p). ∎

*In the source.* The group data of Theorem 1 are abstract. The source attaches a Dirichlet character to each group character as part of its host data, and asks for agreement only on integers prime to the host conductor. Agreement at the ramified primes 2, q and d is used inside Bridge (B), and this note does not re-derive it.

With Lemma 2.3, an upper bound on A − Main is an upper bound on a weighted sum of detectors of Dirichlet characters, evaluated at the scales a/w(ρ).

## 3. Theorem 2: the amplified bound

The source proves an averaged inequality. If a finite family of Hermitian lattices satisfies seven explicit slope and degree bounds, then the prime-power count ASK exceeds Main by at most a list of explicit error terms. On the way, the ambient slope and the place-sum gain cancel. The proof below is complete. That the construction satisfies the seven bounds with the right sizes is the Construction Hypothesis, which is left open.

**Definitions.**

- A Euclidean lattice L is a free abelian group of finite rank r with a Euclidean norm on L ⊗ ℝ.
- covol(L) is the volume of (L ⊗ ℝ)/L, and deg L = −log covol(L).
- The slope is μ(L) = deg L / r for L ≠ 0.
- μ\_max(M) is the largest slope of a nonzero saturated sublattice of M, with the induced norm.

**Lemma 2.1 (divisible means big).** Let L ≠ 0 and M be Euclidean lattices, φ : L → M an injective homomorphism, and D ≥ 1 an integer with φ(L) ⊂ D·M. Then

```latex
\log D\;\le\;\log\|\varphi\|+\mu_{\max}(M)-\mu(L),
```

where ‖φ‖ is the operator norm of φ ⊗ ℝ.

*Proof.* Put N = D⁻¹φ(L), a nonzero sublattice of M of rank r = rank L. The map D⁻¹φ : L → N is a group isomorphism, so covol(N) = |det(D⁻¹φ)| covol(L). The determinant is the product of the r singular values, each at most ‖φ‖/D. Hence

```latex
\mu(N)\;\ge\;\mu(L)-\log\|\varphi\|+\log D.
```

The saturation of N has the same rank and smaller covolume, so μ(N) ≤ μ\_max(M). ∎

In rank one, with L = ℤv, M = ℤw and φ(v) = c·w for c ∈ ℤ \\ {0}, the lemma reads log D ≤ log|c|. That is the product formula: a nonzero integer divisible by D is at least D in absolute value. With D = 1 the lemma is Bost's slope inequality.

**Lemma 2.2 (where Main comes from).** Fix the following data:

- integers m, f ≥ 1;
- a finite set T of tops, with numbers a\_t ≥ 0 and A = Σ\_t a\_t;
- weights w\_{jρ} > 0 for j < m and ρ < f;
- reals v > 0, ℓ, g and κ\_c.

Put ph(y) = y log y − y and

```latex
\log\Omega=\gamma+\log\frac{\pi}{v}-\ell,\qquad
\Lambda_0=\sum_{j<m}\frac1f\sum_{\rho<f}\log\frac{w_{j\rho}\,v}{\pi}+m\,g-\kappa_c,\qquad
\mathrm{Main}=\sum_{j<m}\sum_{t\in T}a_t\Big(\log a_t-1-\gamma+\ell-\frac1f\sum_{\rho<f}\log w_{j\rho}\Big).
```

Then

```latex
\sum_{t\in T}m\big(\mathrm{ph}(a_t)-a_t\log\Omega\big)-A\,\Lambda_0+mA\,g=\mathrm{Main}+A\,\kappa_c .
```

*Proof.* Expand both sides. The term −mA log(π/v), from log Ω, cancels the term −mA log(v/π), from Λ₀. What remains on each side is mΣ\_t ph(a\_t) − mAγ + mAℓ − AΣ\_j (1/f)Σ\_ρ log w\_{jρ} + Aκ\_c. ∎

In the source, log Ω is the archimedean period of the Chowla–Selberg formula, with ℓ = L′/L(1, χ\_K). It enters through the degree bound (Dv) below, while Λ₀ is the lower bound for a count. The period v cancels between them, leaving exactly γ and L′/L(1, χ\_K): the constants built into the detectors of §1.

**Theorem 2 (the averaged inequality).** Keep the data of Lemma 2.2, with κ\_c ≥ 0. Let W be a finite nonempty set with weights d\_u > 0. Take real numbers μ\_CC, Ga, Fo, ASK, E\_div, SL, B, LoP and Φ. For each u ∈ W, take real numbers μ\_N(u), μ\_M(u), h(u), Ee(u), Lo(u) and τ(u) > 0. Put s = Σ\_u d\_u(μ\_N(u) − h(u)) / Σ\_u d\_u. Assume that for every u ∈ W

```latex
\begin{aligned}
&(\mathrm G)&&\mu_M(u)+\mathrm{Ga}+\mathrm{Fo}-\mathrm{Ee}(u)-\mathrm{Lo}(u)\le\mu_N(u)\\
&(\mathrm{Dv})&&\mu_{CC}+h(u)-\mathrm{Fo}\le\textstyle\sum_{t\in T}\big[m(\mathrm{ph}(a_t)-a_t\log\Omega)-a_t\log\tau(u)\big]+E_{\mathrm{div}}\\
&(\mathrm{Ct})&&\Lambda_0\le\log\tau(u)\\
&(\mathrm E)&&\mathrm{Ee}(u)\le mA\,g+mB\\
&(\mathrm{Sl})&&-\mathrm{SL}\le\mu_M(u)
\end{aligned}
```

and that for the family as a whole

```latex
(\mathrm{SI})\quad s-\log|W|-\Phi\le\mu_{CC},\qquad\qquad(\mathrm L)\quad \mathrm{ASK}-\mathrm{Ga}\le\mathrm{LoP}.
```

Then

```latex
\mathrm{ASK}-\mathrm{Main}\ \le\ \mathrm{LoP}+A\kappa_c+\mathrm{SL}+mB+E_{\mathrm{div}}+\frac{\sum_u d_u\,\mathrm{Lo}(u)}{\sum_u d_u}+\log|W|+\Phi .
```

*Proof.* Fix u and write P = Σ\_t m(ph(a\_t) − a\_t log Ω). Move every term of (G), (Dv), A·(Ct), (E) and (Sl) to the left, so that each reads "≤ 0". Multiplying (Ct) by A is allowed because A ≥ 0.

```latex
\begin{aligned}
&(\mathrm G)&&\mu_M+\mathrm{Ga}+\mathrm{Fo}-\mathrm{Ee}-\mathrm{Lo}-\mu_N\le 0\\
&(\mathrm{Dv})&&\mu_{CC}+h-\mathrm{Fo}-P+A\log\tau-E_{\mathrm{div}}\le 0\\
&A\cdot(\mathrm{Ct})&&A\Lambda_0-A\log\tau\le 0\\
&(\mathrm E)&&\mathrm{Ee}-mAg-mB\le 0\\
&(\mathrm{Sl})&&-\mathrm{SL}-\mu_M\le 0
\end{aligned}
```

Add the five. Each of Fo, Ee, log τ and μ\_M appears once with each sign and cancels, which leaves

```latex
\mathrm{Ga}+\mu_{CC}+h-\mu_N-\big(P-A\Lambda_0+mAg\big)-mB-E_{\mathrm{div}}-\mathrm{SL}-\mathrm{Lo}(u)\le 0 .
```

By Lemma 2.2 the bracket equals Main + Aκ\_c. Rearranged,

```latex
\mu_N(u)-h(u)\ \ge\ \mathrm{Ga}+\mu_{CC}-\mathrm{Main}-A\kappa_c-\mathrm{SL}-mB-E_{\mathrm{div}}-\mathrm{Lo}(u).
```

Average over u with weights d\_u to get

```latex
s\ \ge\ \mathrm{Ga}+\mu_{CC}-\mathrm{Main}-A\kappa_c-\mathrm{SL}-mB-E_{\mathrm{div}}-\overline{\mathrm{Lo}}.
```

Adding (SI) removes μ\_CC. Adding (L) replaces Ga by ASK. ∎

Two quantities cancel: the ambient slope μ\_CC and the place-sum gain Ga. The per-u step and the final step are also checked in Lean in exactly this notation, with (Dv) oriented as written; that is the source's DIV, unchanged (Theorem2Check.lean). None of (G), (Dv), (SI), (L) can be dropped. For each one, explicit integers satisfy the other hypotheses and violate the conclusion; we compiled these counterexamples.

**What the numbers are in the source** (read in source).

- **The slopes.** μ\_N(u), μ\_M(u) and μ\_CC are normalized slopes, 2μ − log 2 + log|disc k|/\[k : ℚ\], of Hermitian lattices over the ring of integers of a number field k. For each member u of a finite family W there is a twisted lattice N(u) and an untwisted lattice M(u). There is one ambient lattice CC. The weight d\_u counts the indices attached to u.
- **The place sums.** Ga, Fo and Ee(u) are sums over a finite set of places w of 2·length(w)·e(w)·(…), where e(w) is the ramification index. Ga is the slope gained by twisting at the places that record the prime powers counted by ASK. Hypothesis (L) says this gain captures ASK up to LoP.
- **Where m enters.** ASK = Σ\_{t∈T} Σ\_{j\<m} A(a\_t, t, w\_j), with A as in Theorem 1. So ASK, Main and Ee grow linearly in m, while SL, log|W| and Φ do not. This is the amplification.
- **Hypothesis (SI).** It is a family version of Lemma 2.1: the weighted mean slope is at most the ambient slope plus log|W| + Φ. The defect is

```latex
\Phi=(1-\delta)^{-1}\big(4u_F\log(1+H/u_F)+(\eta+4\sqrt e)\,H\big),
```

where u\_F is the spread of the family, H ≤ x^c b, and δ, η, e are near-orthogonality parameters.

**Model case (heuristic only).** With one map and no family, Lemma 2.1 gives the same shape. Suppose φ is divisible by D with log D ≥ mS, and log‖φ‖ + μ\_max − μ ≤ m·Main + Cx^ε(x + m² + m√x). Then S − Main ≤ 5Cx^(1/2+ε) for m ≈ √x. This shows how to read Theorem 2. The source does not prove it, and the single-map hypothesis of the earlier draft is withdrawn in favour of Theorem 2.

**Construction Hypothesis (CH), restated.** Fix a primitive ψ and ε > 0. At every x on the windows, the source's construction must supply Hermitian lattices and place data that satisfy (G)–(L) of Theorem 2, together with the size bounds of Remark 2.4. These are a subset of the eleven inputs the source proves for its construction, with the same constants. So (CH) is not stronger than the formalized result. The constants are also uniform. In the source, each input has the form "there are constants and an x₀ such that, for every x ≥ x₀ on the windows, …", and these are combined in that order. So the constants are fixed per family, meaning per ψ and ε, before x and m are chosen (read in source). This settles uniformity at the level of quantifiers, not the content of the proofs.

**Remark 2.4 (where the error sizes come from).**

The left side of Theorem 2 is ASK − Main = Σ\_t Σ\_j (A\_{t,j} − Re Main\_{t,j}), summed over |T| tops and m pieces, with b = exp(x^ε). The source bounds the right side using its estimates for Φ, Lo and E\_div, and obtains (read in source, not re-derived)

```latex
\sum_{t\in T}\sum_{j<m}\big(A_{t,j}-\mathrm{Re\,Main}_{t,j}\big)\ \le\ x^{C'\varepsilon}\Big(|T|\,a\,\big(1+\tfrac{m^2}{k}\big)+m\,(B_0+N_c)\Big)
```

under the following size conditions:

- a ≤ 2xb;
- |T| ≥ n x^(−ε/8)/2;
- |T₂| ≤ n;
- x^(1/2−ε) ≤ m ≤ x^(1/2+ε/2);
- xm ≤ k ≤ n²x^(1/2−ε);
- B₀ ≤ 2nmb x^ε;
- N\_c ≤ |T₂| k b x^(2ε)/n².

Dividing by |T| m b, the three terms are at most:

- 2x/m + 2;
- 4m x^(9ε/8);
- 2x^(1/2+9ε/8).

These are the costs x/m, m and √x. Picture: some costs are paid once per top and shared among m pieces, some are paid per piece, and one is fixed. m ≈ √x balances the first two.

**Remark 2.5 (what the construction must supply).** The source proves the hypotheses of Theorem 2 for its construction from four ingredients:

1. **Divisibility that grows like m.** An m-fold chain of theta lifts on CM abelian varieties, each divisible at an inert prime p to order about a/p + a/p³ + ⋯. The local engine is the Frobenius congruence in Witt vectors over 𝔽\_{p^f}, plus collapse modulo √p.
2. **Archimedean size equal to Main.** The Chowla–Selberg period formula (log Ω = γ + log(2π/√d) − L′/L(1, χ\_−d), up to normalization), the Rallis inner product formula and the Siegel mass formula.
3. **Flatness.** Exact orthogonality of a projected kernel (symmetry), with errors at most exp(−6x^ε) (scale).
4. **A loss from Iwasawa theory that stays bounded on windows.** This uses the Ferrero–Washington theorem (μ = 0). It is the reason the bound holds only on windows \[Y, Y^(3/2)\].

Status: (CH) is the open lemma of this note. It is now stated with exactly the inequalities the source proves, so it asks for nothing beyond the formalized result. The formalization claims machine-checked proofs of these inequalities for its construction. We have read the statements and the chain, but we have not re-derived the constructions.

## 4. Theorem 3: zero exclusion from window bounds

Take a positive combination of detectors. If it lies below y^θ on arbitrarily long windows \[Y, Y^(1+δ)\], then every L-function in the combination is zero-free on Re s > θ. The proof below is complete. It uses the same mechanism as the source, high derivatives that localize the Mellin integral to one window, but it was written independently.

**Theorem 3.** Let χ₁, …, χ\_J be distinct primitive Dirichlet characters. Suppose the set is closed under complex conjugation, and take weights w\_j > 0 that are equal on conjugate pairs. Put M(y) = Σ\_j w\_j G\_{χ\_j}(y), which is real. Suppose there are θ ∈ (0, 1), δ > 0, A > 0 and arbitrarily large Y with

```latex
M(y)\le A\,y^{\theta}\qquad\text{for all }y\in[Y,\,Y^{1+\delta}].
```

Then no L(s, χ\_j) has a zero with Re s > θ.

**Lemma 3.1 (no persistent cancellation).** Let R₁, …, R\_n be nonzero complex numbers and φ₁, …, φ\_n distinct modulo 2π. Then there is c₀ > 0 such that, for every integer k₀, some k ∈ {k₀, …, k₀ + n − 1} has |Σ\_q R\_q e^(ikφ\_q)| ≥ c₀.

*Proof.* The vector of these n sums equals V applied to (R\_q e^(ik₀φ\_q))\_q, where V = (e^(ii′φ\_q)) is an invertible Vandermonde matrix. The input vector has norm ‖R‖ for every k₀, so the output has norm at least ‖R‖/‖V⁻¹‖. ∎

*Proof of Theorem 3.*

*Step 0 (transforms).* By Lemma 1.1, H(s) = ∫₁^∞ M(y) y^(−s−1) dy is meromorphic on ℂ and holomorphic at 1. In Re s > 0 its poles are the points ρ where some L(s, χ\_j) vanishes, with residue −m(ρ)/(ρ(ρ − 1)), where m(ρ) = Σ\_j w\_j ord\_ρ L(s, χ\_j) > 0. Positive weights mean the zeros of different members never cancel.

By Chebyshev, M(y) = O(y log y). Put f(y) = A y^θ − M(y) and K(s) = ∫₁^∞ f(y) y^(−s−1) dy = A/(s − θ) − H(s). Let P be the point θ together with the poles of H. K is holomorphic off P. If a pole of H at θ happens to cancel A/(s − θ), then P is larger than needed, which is harmless. No L(s, χ\_j) vanishes on Re s ≥ 1, and H is holomorphic at 1, so every point of P has real part less than 1. Suppose, for a contradiction, that H has a pole with real part > θ.

*Step 1 (geometry).* Fix a real σ > 1, to be chosen in Step 3. Let r be the distance from σ to P, and let N be the set of points of P at that distance. Since θ ∈ P, r ≤ σ − θ. Every point of P lies to the left of σ, by Step 0. Suppose N contains no non-real point. Distinct real numbers to the left of σ are at distinct distances from σ, so N is then a single real point p. Moreover p ≥ θ, because θ itself is at distance σ − θ. So a real pole of H to the left of θ is never nearest, and a pole of H at θ itself is the point θ of case 2. Exactly one of the following therefore holds:

1. N contains a non-real q. Put z = σ + i Im q. Then |z − q| = σ − Re q < |σ − q| = r.
2. N = {θ}. Take a pole ρ₀ of H with Re ρ₀ > θ. It is not real, since a real one would be nearer to σ than θ. Put z = σ + i Im ρ₀. Then |z − ρ₀| = σ − Re ρ₀ < r.
3. N = {β}, a real pole of H with θ < β < 1.

In cases 1 and 2, the distance d from z to the poles of H satisfies d < r. Moreover |z − θ| ≥ σ − θ ≥ r.

*Step 2 (localization).* Put u = log y, U = log Y and W = \[U, (1+δ)U\]. For Re z = σ,

```latex
(-1)^kH^{(k)}(z)=\frac{A\,k!}{(z-\theta)^{k+1}}-\int_0^\infty f(e^u)\,u^k e^{-zu}\,du .
```

On W we have f ≥ 0. So the part of the integral over W has absolute value at most ∫\_W f u^k e^(−σu) du, which equals (−1)^k K^(k)(σ) minus the same integral over the complement of W. Write T\_k = ∫ over the complement of W of |f(e^u)| u^k e^(−σu) du. The complement enters only through absolute values, at both points. At z, its part of the integral has absolute value at most T\_k. At σ, the window part equals (−1)^k K^(k)(σ) minus the complement part, so it is at most |K^(k)(σ)| + T\_k. Whatever the sign of f off the window, cancellation from the complement can only make the left side smaller. Altogether

```latex
\frac{|H^{(k)}(z)|}{k!}\le \frac{A}{|z-\theta|^{k+1}}+\frac{|K^{(k)}(\sigma)|}{k!}+\frac{2T_k}{k!},\qquad\qquad
\frac{(-1)^kK^{(k)}(\sigma)}{k!}\ge-\frac{T_k}{k!}.
```

*Step 3 (tails).* By Chebyshev, |f(e^u)| ≤ B(1 + u)e^u for u ≥ 0. Put λ = σ − 1 and η = δ/(4(1 + δ)), so 0 < η ≤ 1/4.

**Lemma 3.2 (Gamma tails).** For every integer j ≥ 1,

```latex
\int_{|u-j/\lambda|\,\ge\,\eta j/\lambda}u^{\,j-1}e^{-\lambda u}\,du\ \le\ 2\,(j-1)!\,\lambda^{-j}\,e^{-j\eta^2/4}.
```

*Proof.* The function λ^j u^(j−1) e^(−λu)/(j − 1)! is the density of a Gamma variable X with mean j/λ, and E e^(tX) = (1 − t/λ)^(−j) for t < λ. Apply Markov's inequality to e^(tX) and e^(−tX) with the optimal t. This gives

- P(X ≥ (1 + η)j/λ) ≤ e^(−j(η − log(1+η)));
- P(X ≤ (1 − η)j/λ) ≤ e^(−j(−η − log(1−η))).

For 0 < η ≤ 3/4, both exponents are at least jη²/4. ∎

*Choosing k.* Take k with (k + 1)/λ in \[(1 + δ/4)U, (1 + 3δ/4)U\]. Our choice of η satisfies η < δ/(4 + 3δ) and η ≤ δ/(4 + δ). So for U large, the η-neighbourhoods of both centres (k + 1)/λ and (k + 2)/λ lie inside W = \[U, (1 + δ)U\]. Apply Lemma 3.2 with j = k + 1 to the u^k part of the tail and with j = k + 2 to the u^(k+1) part. This gives

```latex
\frac{T_k}{k!}\ \le\ 2B\Big(1+\frac{k+1}{\lambda}\Big)\lambda^{-k-1}e^{-(k+1)\eta^2/4}.
```

*Choosing σ.* Take σ so large that (σ − θ)/(σ − 1) < e^(η²/8). This depends only on θ and δ. Then λe^(η²/8) > σ − θ ≥ r, so T\_k/k! = O(k·(re^(η²/8))^(−k)). In particular T\_k/k! = o(r^(−k)).

As Y runs through the hypothesis, U → ∞. The admissible k then form runs of more than λδU/2 − 1 consecutive integers, so these runs become arbitrarily long.

*Step 4 (the pole wins).*

- **Cases 1 and 2.** Near z, H(w) = Σ\_q R\_q/(w − q) + g(w). The sum runs over the poles q at distance d, each with R\_q ≠ 0. The function g is holomorphic on a disc of radius d₁ > d. So H^(k)(z)/k! equals ±d^(−k−1) Σ\_q R\_q e^(−i(k+1)φ\_q) + O(d₂^(−k)) for any d₂ < d₁, where the φ\_q are distinct. By Lemma 3.1, every run of n consecutive k contains one with |H^(k)(z)|/k! ≥ ½c₀ d^(−k−1). On the other side, pick r′ strictly between d and r. Cauchy's estimate on the disc of radius r about σ, where K is holomorphic, gives |K^(k)(σ)|/k! = O(r′^(−k)). With A r^(−k−1) and the tail, every term on the right of Step 2 is O(r′^(−k)), which is o(d^(−k)). That is a contradiction.
- **Case 3.** Near σ, K(w) = R/(w − β) + g(w) with g holomorphic beyond radius r. Here R = m(β)/(β(β − 1)) < 0, because 0 < β < 1 and m(β) > 0. So (−1)^k K^(k)(σ)/k! = R r^(−k−1) + o(r^(−k)), which is negative and of size r^(−k). The bound from Step 2 says it is at least −T\_k/k! = o(r^(−k)). That is a contradiction. ∎

**Uniformity.** Once σ is fixed, the following are fixed numbers: the point z, the distances d < r′ < r, the residues, and the constant c₀ of Lemma 3.1. Only U and k vary. So every implied constant above is independent of the window. The contradiction comes from letting U, and with it k, tend to infinity along the admissible runs.

**Coincident zeros.**

- *Several members vanish at the same ρ.* H has one pole there, with residue carrying m(ρ) = Σ\_j w\_j ord\_ρ L(s, χ\_j) > 0. Positive weights rule out cancellation.
- *One member has a multiple zero.* This is still a simple pole of H, because L′/L has only simple poles.
- *Several distinct poles lie at the same distance from z.* This is covered by Lemma 3.1.
- *Case 3.* The nearest singularity to σ is unique by construction, so no cancellation can occur.

**Where positivity is used.** The positive weights are used twice:

- so that a zero of any member is a pole of H (m(ρ) > 0);
- for the sign of R in case 3.

Positivity of the Dirichlet coefficients is not needed. Without positive weights the statement fails. For example, if ζ had a real zero β > θ, then M = −G\_1 ≈ −c y^β would satisfy every window bound.

**Corollary 3.2 (the family of Theorem B).** Let ψ be primitive of order o. Let ψ\_j be the primitive character inducing ψ^j, and put

```latex
M_\psi(y)=G_1(y)+\frac{1}{3o+1}\sum_{j=1}^{o-1}\operatorname{Re}G_{\psi_j}(y).
```

The following are equivalent:

- for every ε > 0, M\_ψ(y) ≤ y^(1/2+ε) on \[Y, Y^(3/2)\] for arbitrarily large Y;
- ζ and every L(s, ψ\_j) have no zeros with Re s > 1/2.

The first implies the second by Theorem 3 with θ = 1/2 + ε, δ = 1/2. The family is closed under conjugation and Re G = (G\_χ + G\_χ̄)/2. The second implies the first by Proposition 1.2, which gives the bound at every large y, with no restriction to windows.

## 5. How the pieces combine, and what is still open

Two statements stand between Theorems 1–3 and GRH for all Dirichlet L-functions: the Construction Hypothesis and a bridge from the averaged count to the target family. Everything else is proved in this note.

**Bridge (B), read in source and not re-derived.** Fix a primitive ψ of order o and ε > 0. At every point x of the windows, the source chooses an abelian field F as in §2, a set T of tops, and data a\_t, w\_j such that

```latex
\frac{\delta_2}{2}\Big(M_\psi(x)-\Sigma_{\mathrm{aux}}(x)-4x^{1/2+\varepsilon}\Big)\ \le\ \mathcal D(x)+\frac2x .
```

The terms are:

- 𝒟(x) is the average of A − Re Main over tops and pieces, divided by b. This is the ASK − Main of Theorem 2, divided by |T|·m·b.
- δ₂ ≥ x^(−ε).
- Σ\_aux is a weighted sum of the detectors of three auxiliary characters, (a/q), (a/d) and (a/q)(a/d). Each of these is bounded in absolute value by y^(1/2+ε/2).

The proof in the source combines three pieces:

- Theorem 1, applied at each top.
- A choice of tops that works for every prime at once.
- Twist control for the auxiliary characters, which come from a family of huge primes q. A mean-square bound Σ\_q |S\_q(y)|² ≤ C y log y |P| forces almost every q to be quiet at size y^(1/2+ε/2). This uses only classical inputs: Siegel–Walfisz, Page, Siegel, and zero density near Re s = 1.

**Assembly.**

1. On the windows, (CH), Theorem 2 and the error sizes of Remark 2.4 give 𝒟(x) ≤ x^(1/2+O(ε)).
2. Bridge (B) then gives M\_ψ(x) ≤ x^(1/2+O(ε)) on \[Y, Y^(3/2)\], for arbitrarily large Y.
3. Corollary 3.2 gives: ζ and every L(s, ψ\_j) are zero-free on Re s > 1/2.
4. ψ was arbitrary, so this is GRH for all Dirichlet L-functions. For ψ = 1 we have o = 1 and M\_ψ = G\_1, which is RH.

| Component | Statement | Status |
| --- | --- | --- |
| Proposition 1.2 | GRH implies \|G\_χ(y)\| ≤ C y^(1/2), with no log factor | Proved here, from the standard explicit formula |
| Theorem 1 | A − Main is an explicit character combination of detectors | Proved here |
| Lemma 2.3 | For data from an abelian field, ψ̃ is the primitive Dirichlet character of ψ | Proved here; the source uses it inside (B) |
| Lemma 2.1 | Divisible means big (Bost) | Proved here |
| Lemma 2.2 | The period cancels against the count, leaving γ and L′/L(1, χ\_K) | Proved here |
| Theorem 2 | Seven slope and degree bounds imply ASK − Main ≤ explicit errors | Proved here; same statement as the source's chain |
| Remark 2.4 | The errors reduce to x/m + m + √x | Algebra proved here; size conditions read in source |
| Theorem 3 and Lemma 3.2 | Positive window bounds exclude zeros right of θ | Proved here; an independent analytic audit is still worthwhile |
| Corollary 3.2 | Window bound for every ε is equivalent to GRH for the family | Proved here |
| Lemma 6.1 | Period cancellation: the main term of (Dv) | Proved here; its inputs (P2) and (H1)–(H4) are open |
| Theorem 7.0 | Frobenius congruence implies w-divisibility of a 2×2 minor | Proved here; on the chain through the κ bound, not the gains (§8) |
| Proposition 7.1 | Twisting by an ideal changes the slope by 2Σℓ(w)σ(w) | Proved here (standard); Lean check for rank 2 over ℤ |
| Theorem 7.2 | Gain lower bound: (G) from twisting and quotient lengths | Proved here; Lean check on an instance |
| Construction Hypothesis | The construction satisfies Theorem 2's seven bounds, with Remark 2.4's sizes | Open here; claimed machine-checked in the source. (Dv) is reduced in §6 to the ambient degree bound and the theta-jet height bounds. (G) is reduced in §7 to the inputs `LinkG` and `LinkMu`; the capture clause `LinkG` (d) is the arithmetic heart. |
| Bridge (B) | Averaged count controls M\_ψ, given quiet twists | Read in source; classical inputs; not re-derived |
| LinkG (d) | Capture inequality | Numeric inequality between defined quantities. The gain is set equal to gainP by a family field. Its valuation clause is met by a zero chain map. The proof of Conclusion1 is not checked (§8). |
| LinkMu | Slope of the twisted lattice | Holds by definition: the actual lattice is defined as the twist by the gains (family field nprimeDef) (§9.1). |
| Receipt for the gains | The actual map sends NuLat into 𝔭^⌊e·sg⌋ times the dual lattice | Proved from the service branch for the real lattice instance (CmpV, formal-group bounds). Its inputs SysTw and CmpLite are not yet traced (§9). |
| Zero-map test | Can numerical gains plus a zero map yield the final bound? | No. The upper pan needs Bk's matrix inside a near-isometry; Bk can vanish only on words carrying about delp·sg of the rank (Lemma Z, §10). Derived, not compiled. |

**What another mathematician would need to supply.**

- **A paper proof of (CH).** This is where everything new lives: the m-fold chain of theta lifts, its divisibility at inert primes, the archimedean evaluation by periods, and the Iwasawa bound on windows.
- **A paper proof of (B).** It needs only classical analytic number theory and combinatorics, but it is long.

Nothing else is missing. If both are written out, Theorems 1–3 turn them into GRH for Dirichlet L-functions with no software involved.

## 6. Inside (CH): the degree bound (Dv)

(Dv) is not a divisibility statement. It bounds two archimedean quantities: the slope of the ambient lattice and the size of the map. The CM period enters both with opposite signs and cancels, leaving exactly the main term m·Σ\_t(ph(a\_t) − a\_t log Ω) − A log τ. Divisibility enters (G), not (Dv). Lemma 6.1 below is the mechanism, with a complete proof. The four inputs it needs are listed in 6.3 with their status.

**6.1 The objects** (read in source).

- **Base field and slopes.** K is a CM field with ring of integers 𝒪\_K. A Hermitian lattice is an 𝒪\_K-lattice L ⊂ K^d together with a positive-definite Hermitian matrix at each infinite place. Its normalized slope is μ(L) = 2·(Arakelov slope) − log 2 + log|disc K|/\[K : ℚ\].
- **The ambient lattice.** CC is the dual R^∨ of a lattice R. R is a twisted product, over the m lifts j, of Hermitian lattices M\_j. At each finite place y, its localization has a local type μ(y), which differs from the base type only at finitely many places; the twisted places Tw are among these. At the infinite places, its metric is a product of the factor metrics scaled by κ.
- **The maps.** For each family member u there is a lattice N\_u and an 𝒪\_K-linear map B\_u : N\_u → R^∨. It factors as a chain of maps: a column chain, followed by a final pairing.
- **The height.** h(u) is a logarithmic upper bound for the archimedean size of B\_u: the mean over infinite places v of log‖B\_u‖\_v² is at most h(u).

**6.2 The mechanism.**

**Lemma 6.1 (period cancellation).** Fix the following data:

- a finite set J with |J| = m, a finite set Π of slots, and tops T ⊂ Π with numbers a\_t;
- reals μ\_C, μ₀, L\_pass, Fo, E\_b, h, h\_P, λ, e₆, e\_P, log τ, log Ω and k;
- for each j ∈ J, reals q\_j, h\_j and e\_j;
- for each pair (j, ρ) ∈ J × Π, reals w\_{jρ}, φ\_{jρ}, f\_{jρ}, n\_{jρ}, δ\_{jρ} and e\_{jρ}.

Assume

```latex
\begin{aligned}
&(\mathrm{P1})&&\mu_C\le\mu_0+L_{\mathrm{pass}}\\
&(\mathrm{P2})&&\mu_0\le\textstyle\sum_{j,\rho}q_j\,w_{j\rho}\log\Omega+2\,\mathrm{Fo}+E_b\\
&(\mathrm{H1})&&h=h_P+\textstyle\sum_j h_j-\lambda\\
&(\mathrm{H2})&&h_j\le\textstyle\sum_\rho\big(\varphi_{j\rho}-n_{j\rho}\log\Omega\big)+e_j\\
&(\mathrm{H3})&&\textstyle\sum_{j,\rho}f_{j\rho}-e_6\le\lambda\\
&(\mathrm{H4})&&h_P\le-\textstyle\sum_{t\in T}a_t\log\tau+e_P\\
&(\mathrm{W1})&&\varphi_{j\rho}-f_{j\rho}\le\mathrm{ph}(a_\rho)\,[\rho\in T]+e_{j\rho}\\
&(\mathrm{W2})&&n_{j\rho}=a_\rho\,[\rho\in T]+k\,w_{j\rho}+\delta_{j\rho}
\end{aligned}
```

Then, with E = E\_b + L\_pass + e\_P + Σ\_j e\_j + e₆ + Σ\_{j,ρ} e\_{jρ},

```latex
\mu_C+h-2\,\mathrm{Fo}\ \le\ \sum_{t\in T}\Big[m\big(\mathrm{ph}(a_t)-a_t\log\Omega\big)-a_t\log\tau\Big]+\sum_{j,\rho}\big[(q_j-k)\,w_{j\rho}-\delta_{j\rho}\big]\log\Omega+E .
```

*Proof.* By (P1), (P2), (H1), (H3) and (H4),

```latex
\mu_C+h-2\,\mathrm{Fo}\le\sum_{j,\rho}q_jw_{j\rho}\log\Omega-\sum_{t\in T}a_t\log\tau+\sum_j h_j-\sum_{j,\rho}f_{j\rho}+(E_b+L_{\mathrm{pass}}+e_P+e_6).
```

Apply (H2) and substitute (W2):

```latex
\sum_j h_j\le\sum_{j,\rho}\varphi_{j\rho}-\sum_{j}\sum_{t\in T}a_t\log\Omega-\sum_{j,\rho}(k\,w_{j\rho}+\delta_{j\rho})\log\Omega+\sum_j e_j.
```

The two period terms combine to Σ\_{j,ρ} \[(q\_j − k)w\_{jρ} − δ\_{jρ}\] log Ω − m Σ\_{t∈T} a\_t log Ω. By (W1), Σ\_{j,ρ}(φ\_{jρ} − f\_{jρ}) ≤ mΣ\_{t∈T} ph(a\_t) + Σ e\_{jρ}. Adding gives the claim. ∎

**Reading.**

- **(P2) contributes +q\_j w log Ω.** This is the ambient metric, normalized by the period.
- **(H2) with (W2) contributes −(a + kw + δ) log Ω.** Jets of total order n = a + kw + δ cost n log Ω at the archimedean places. Their size is weighted by the factorials ph(n) = n log n − n ≈ log n!.
- **The kw parts cancel up to q\_j − k.** Only the a-part survives, once for each of the m lifts. That is where the factor m in Main comes from. With Lemma 2.2, it is also where γ and L′/L(1, χ\_K) come from.

The cancellation is checked in Lean on an instance with two lifts, two slots and one top (DvCore.lean). The leftover comes out as exactly 2(ph(a₁) − a₁ log Ω) − a₁ log τ plus the stated error terms.

**From Lemma 6.1 to (Dv)** (read in source). The source's size conditions bound the leftover:

- |q\_j − k| ≤ m;
- 0 ≤ w ≤ 2b;
- |log Ω| ≤ La;
- |δ| and e\_{jρ} at most C₀(…)La.

With these, the leftover is at most C|T|a·La + Cm(B₀ + N\_c)x^(Cε). In the source, μ\_C is the slope of R^∨ minus the mean log of κ, h − mean log κ = h(u), and 2Fo is the Fo of Theorem 2. This is exactly (Dv).

**6.3 Where each input comes from.**

| Input | Mathematical content | Status |
| --- | --- | --- |
| (P2) ambient degree | Product formula for the Gram determinant of a twisted product of m Hermitian lattices over a CM field. The archimedean part is the log-eigenvalue sum; the finite part gives 2Fo at the twisted places plus small local terms. | General Arakelov geometry (product formula; slopes add under products). The precise statement is proved in the source and not re-derived here. |
| Period normalization (part of P2) | The archimedean log-eigenvalues are at most Σ\_ρ q\_j w\_{jρ} log Ω plus a small error. | Uses the CM period. Its Chowla–Selberg value gives γ and L′/L(1, χ\_K) in Main (Lemma 2.2). The scaling is new; not re-derived. |
| (P1) passage | Moving from the base lattice to the column lattice costs at most 1 + C₀mλ₀. | New; not re-derived. |
| (H1)–(H4) height of B\_u | B\_u factors through a chain. The last map has norm at most e^(h\_P), and the steps are bounded by factorial-weighted jet sizes. | Theta-jet estimates on CM abelian varieties. New, and the main open content of (Dv). |
| (W1), (W2) jet orders | Total jet order a\_ρ + kw\_{jρ} + δ\_{jρ}, with factorial weights. | New combinatorics (the multiplicity bookkeeping of the handoff); statements read. |
| Final combination | Lemma 6.1 plus the size conditions. | Main-term form proved here. The source's explicit form is an elementary real inequality, proved in the source. |

**6.4 Where divisibility actually enters.** Two other clauses of the same source package carry the divisibility:

- every pairing value B\_u(φ, F) has valuation at least σ(w) at each finite place w;
- twisting N\_u by σ raises its slope by 2Σ\_w ℓ(w)σ(w).

These feed (G) and (SI), not (Dv). The only finite-place term in (Dv) is Fo. It appears in (G) with the opposite sign and cancels in Theorem 2.

**6.5 Portable form.** Lemma 6.1 is elementary and fully general. As a principle, it needs three ingredients:

- an ambient lattice whose archimedean metric is a product of m factors normalized by a period Ω;
- maps whose archimedean size is controlled by factorial-weighted jets measured with the same Ω;
- a jet-order budget n = a + kw + δ.

Then the period-dependent kw parts cancel, and the slope plus the height is at most mΣ\_t(ph(a\_t) − a\_t log Ω) − A log τ plus errors. The first and third ingredients are not specific to ζ. The second needs a period whose logarithm equals the analytic constant of the detector, γ + log(π/v) − L′/L(1, χ). For abelian CM fields, the Colmez formula gives such periods, which makes Hecke characters of those fields a plausible extension. For GL(2) and beyond, no period formula of this form is known. Whether the principle transfers is therefore not established.

## 7. Inside (CH): the gain (G)

The gain does not outgrow the main term. Both are sums over the m lifts and they match lift by lift. What grows more slowly is the cost. Costs paid once per top do not depend on m, so after dividing by m they shrink like x/m. The costs that do grow with m add only about m per lift. The accounting that turns per-lift gains into slope is standard twisting plus elementary algebra, proved in 7.2 and 7.4. The claim that each lift's gain covers its local share of the main term is the capture clause of the constructed input `LinkG`, which this note does not prove.

Labels: READ means read in the source at e50d098. DERIVED means reasoning in this note. COMPILED means checked in Lean 4.33.1 (GainCheck.lean).

**7.1 The local divisibility theorem.**

**Theorem 7.0 (READ; proof DERIVED).** Let A be a commutative ring, p a prime, and w ∈ A with w² = p. Let k, e ≥ 0. Let u, u′ ∈ A^(k+1) satisfy w | u(b) and w | u′(b) for every index b ≠ 0. Let M and N′ be (k+1)×(k+1) matrices over A whose entries satisfy the Frobenius congruence M(b, a)^(p^e) ≡ N′(b, a) (mod pA). Then for every column c,

```latex
w\ \Big|\ \Big(\sum_b u'_bN'_{bc}\Big)\Big(\sum_b u_bM_{b0}\Big)^{p^e}-\Big(\sum_b u'_bN'_{b0}\Big)\Big(\sum_b u_bM_{bc}\Big)^{p^e}.
```

*Proof.* Work modulo w. There p = w² ≡ 0, so M(0, a)^(p^e) ≡ N′(0, a), and u(b) ≡ u′(b) ≡ 0 for b ≠ 0. The four sums reduce as follows:

- Σ u′(b)N′(b, c) ≡ u′(0)N′(0, c);
- (Σ u(b)M(b, 0))^(p^e) ≡ u(0)^(p^e)N′(0, 0);
- Σ u′(b)N′(b, 0) ≡ u′(0)N′(0, 0);
- (Σ u(b)M(b, c))^(p^e) ≡ u(0)^(p^e)N′(0, c).

The expression becomes u′(0)N′(0, c)·u(0)^(p^e)N′(0, 0) − u′(0)N′(0, 0)·u(0)^(p^e)N′(0, c) = 0. ∎

**Remark 7.0a (hypotheses).** The proof uses only w² = p, which gives p ≡ 0 mod w, and the stated congruence. Primality of p is not used. In the source, the congruence is supplied by `frobCong`, the Frobenius congruence in the unramified Witt ring, where p is prime (§8.5).

In the source this is `key_minor_dvd` (KeyMinorDvd.lean:132), and it is applied in `kW_ord` (READ). There A is a polynomial ring over a discrete valuation ring O over the Witt vectors W(𝔽\_{p^{n′}}), with uniformizer w and w² = p. The matrices M and N′ are two Frobenius twists of g⁻¹ for some g ∈ GL\_{m+1}(W(𝔽\_{p^{n′}})). The conclusion is that a specific key polynomial has w-adic order at least 1.

*Not established here.* We have not traced how this order-1 divisibility becomes the gains of 7.3. `key_minor_dvd` is used only inside its own file. `LinkG` is supplied by a separate admissibility argument (AdmissibleFamilyNoKernel.lean:230). So the theorem is identified and proved, but its role in the gain is not. Accordingly it is labelled READ, not COMPILED.

**7.2 The twisting operation and its slope change.**

For a finitely supported σ from finite places to ℤ, the twist of an 𝒪\_K-lattice N is

```latex
N[\sigma]=\mathfrak a_\sigma N,\qquad \mathfrak a_\sigma=\prod_w\mathfrak p_w^{-\sigma(w)}.
```

**Proposition 7.1.** For a Hermitian 𝒪\_K-lattice N of rank d ≥ 1,

```latex
\mu(N[\sigma])=\mu(N)+2\sum_w\ell(w)\,\sigma(w),\qquad \ell(w)=\frac{\log\mathrm N\mathfrak p_w}{[K:\mathbb Q]}.
```

*Proof (DERIVED; standard).* For an integral ideal 𝔞, the sublattice 𝔞N ⊂ N has index N(𝔞)^d, computed place by place. So covol(𝔞N) = N(𝔞)^d·covol(N). By multiplicativity the same holds for fractional ideals, giving log covol(N\[σ\]) = log covol(N) − dΣ\_w σ(w) log N𝔭\_w. The normalized slope is μ = −2·log covol/(d\[K:ℚ\]) plus a constant. ∎

The source proves exactly this statement (`shift_slope_mu`, TwistedLatticeNaturality.lean:145; READ). COMPILED: the rank-2 case over ℤ, i.e. K = ℚ, where covolume is |det| (`det2_smul`). The index form, covol(N) = \[N′ : N\]·covol(N′) for any N ⊂ N′, is `det2_mul`. It has two worked instances at p = 3: a scalar twist with index 9, and a non-scalar local twist with index 3.

**7.3 From local data to Ga and Fo** (definitions READ, DataParams₂.lean:208–231).

The source stores the following real numbers for each place w in a finite support and each lift j ∈ {1, …, m}:

- gain\_j(w), F\_j(w) and E\_j(u, w);
- τ(w) and io(w), which do not depend on j;
- e(w), the ramification index.

These are data, not valuations computed from the lattices. They define

```latex
\begin{aligned}
s(u,w)&=\textstyle\sum_{j=1}^m\big(\mathrm{gain}_j(w)+F_j(w)-E_j(u,w)\big)\\
\mathrm{Ga}&=\textstyle\sum_w 2\ell(w)e(w)\big(\sum_j\mathrm{gain}_j(w)-\tau(w)\big)\\
\mathrm{Fo}&=\textstyle\sum_j\sum_w 2\ell(w)e(w)\,F_j(w),\qquad \mathrm{Ee}(u)=\textstyle\sum_j\sum_w 2\ell(w)e(w)\,E_j(u,w).
\end{aligned}
```

So Σ\_w 2ℓ(w)e(w)(s(u, w) − τ(w)) = Ga + Fo − Ee(u). This identity is DERIVED, and COMPILED for two places and two lifts (`claimSg`). By Proposition 7.1, a twist by exactly s raises the slope by Ga + Fo − Ee(u). The twist exponent is a sum over the m lifts, while τ(w) is paid once per place.

What the source requires of these numbers is the constructed input `LinkG` (READ; GlobalTheoremInputs.lean). It has four clauses:

- **(a) local containment:** away from the prime T(u), the lattice lies inside a shift of the ramified lattice by ⌊ur(τ(w))⌋;
- **(b) length:** len(u, w) ≤ d\_u(τ(w) + io(w)) for the quotient length;
- **(c) size:** 0 ≤ gain\_j(w) ≤ 4|T|a/p at inert w with p ≤ X″;
- **(d) capture:**

```latex
\sum_{j=1}^m\sum_{t\in T}\big(V_{j,t}(p)-\mathrm{lo}(p)\big)-m\,\mathrm{fl}(p)\ \le\ \sum_{j=1}^m\mathrm{gain}_j(w)-\tau(w),\qquad V_{j,t}(p)=\sum_{i\ \mathrm{odd}}\max\Big(0,\ \frac{a_t}{p^i}-w_{j,t,p,i}\Big).
```

Here V\_{j,t}(p) is the local ramp sum that ASK carries at p. A second input, `LinkMu`, gives the slope of the actual twisted lattice up to C·X″: |μ(N\_u) − μ(N\_u^H) − Σ\_w 2ℓ(w)e(w)s(u, w)| ≤ C·X″.

Clause (d) is the arithmetic heart of (G): each lift captures the full local ramp sum at p. Fo cancels against (Dv). The main part of Ee, mA·log(g₀g₁), cancels against the count in Lemma 2.2, with g = log(g₀g₁).

**7.4 The gain inequality, with Ee and Lo in full.**

**Theorem 7.2 (DERIVED; source `ClaimLow`, READ; instance COMPILED as `claimLow`).** Take the following data:

- finite sets of places W\_T ⊂ W, with weights ℓ(w) ≥ 0;
- lift data g\_j, F\_j, E\_j, with s(w) as above;
- reals τ(w) ≥ 0 vanishing on W\_T, io(w) ≥ 0, len(w) and σ′(w);
- d\_M > 0, 0 ≤ δ < 1 and d\_u = (1 − δ)d\_M.

Assume:

- (T) μ\_N = μ\_Mu + Σ\_w 2ℓ(w)(σ′(w) − τ(w)) − Σ\_w 2ℓ(w)(len(w) − d\_uτ(w))/d\_u;
- (L1) len(w) ≤ d\_M(τ(w) + io(w)) for w ∉ W\_T;
- (L2) Σ\_{w∈W\_T} 2ℓ(w)len(w)/d\_u ≤ P\_T;
- (R) Σ\_w 2ℓ(w)(s(w) − σ′(w)) ≤ R\_d.

Then, with IO = Σ 2ℓ·io and Ta = Σ 2ℓτ,

```latex
\mu_N\ \ge\ \mu_{Mu}+\mathrm{Ga}+\mathrm{Fo}-\mathrm{Ee}-R_d-P_T-\frac{\mathrm{IO}}{1-\delta}-\frac{\delta}{1-\delta}\,\mathrm{Ta}.
```

*Proof.* For w ∉ W\_T, (L1) and d\_M/d\_u = 1/(1 − δ) give (len(w) − d\_uτ(w))/d\_u ≤ τ(w)δ/(1 − δ) + io(w)/(1 − δ). On W\_T, τ = 0 and (L2) applies. By (R), Σ 2ℓ(σ′ − τ) ≥ Σ 2ℓ(s − τ) − R\_d, which by the identity of 7.3 equals Ga + Fo − Ee − R\_d. Substitute into (T). ∎

The source then converts the error terms (`ClaimLow2`, READ). It uses five size conditions:

- μ\_Mu = μ\_M − f log(T − 1)/(T − 2);
- δ ≤ 2f/T ≤ 1/2;
- Ta ≤ b², which follows from Mertens' theorem;
- 4fb²/T + f log(T − 1)/(T − 2) ≤ 1, which holds because T(u) ≥ b^(m/2);
- P\_T ≤ L\_T and R\_d ≤ R\_X.

The result is (G), μ(N\_u) ≥ μ(M\_u) + Ga + Fo − Ee(u) − Lo(u), with

```latex
\mathrm{Lo}(u)=C\cdot\mathrm{IOsum}+C\,|T|\,m\Big(\frac ak+b'\Big)\log T(u)+C\,X''(n)+1,\qquad \mathrm{IOsum}=\textstyle\sum_w\ell(w)e(w)\,io(w).
```

The matching upper bound on μ\_max(N\_u) carries an extra + C·m·B₀. Ee(u) is defined in 7.3. Its required bound (READ) is |Σ\_w 2ℓ(w)e(w)E\_j(u, w) − A·log(g₀g₁)| ≤ C·B₀ for each j. So Ee(u) = mA·log(g₀g₁) ± mCB₀.

**7.5 Every dependence on m.**

| Term | Growth in m | Bound comes from | After dividing by \|T\|·m·b |
| --- | --- | --- | --- |
| Σ\_j gain\_j(w) in Ga | linear: one gain per lift | definition and `LinkG` (d) | matches the m in Main, lift by lift |
| τ(w), Ta ≤ b² | none | Mertens; size condition | paid once |
| Fo | linear | definition | cancels against (Dv) |
| Ee(u), main part mA·log(g₀g₁) | linear | E-comparison | cancels against the count (Lemma 2.2) |
| Ee(u), error mCB₀ with B₀ = f·m·b·x^ε | quadratic | E-comparison | the m term |
| C·IOsum in Lo, with IOsum ≤ C\|T\|m·b·x^(e\_Lε) | linear | loss input | x^(O(ε)) |
| C\|T\|m(a/k + b′)log T(u), with log T ≤ CmL | quadratic | count input | at most x^(O(ε)), since k ≥ xm and mkb′ ≤ a |
| C·X″(n) + 1 in Lo | none | scale | small |
| C·m·B₀ in the upper half | quadratic | upper half of (G) | the m term |
| SL, log\|W\|, Φ, and the \|T\|a·La part of E\_div (Theorem 2) | none | Theorem 2 | the x/m term |
| m(B₀ + N\_c)x^ε in E\_div | quadratic in the B₀ part | (Dv) | the m and √x terms |

Two further facts come from the amplifier audit in the handoff folder, written by another agent and not re-verified here. First, the construction takes m = 2⌈A/2⌉ with A = x^(1/2−ε/16), and k ∈ \[x^(9/2+10ε), 2x^(9/2+10ε)\]. Second, one internal input grows like m⁵: log ΓP = C\_Γ·m⁵·f·L.

**7.6 Portable form, and what it rests on.**

**Corollary 7.3 (amplified twist gain; DERIVED).** Let N arise from M by twisting with exponent s(w) = Σ\_{j=1}^m g\_j(w), up to the defects of Theorem 7.2. Then the slope gain is additive over lifts, and each place's defect τ(w) is paid once. Suppose in addition that each lift captures a local quantity, Σ\_j g\_j(w) ≥ m·V(w) − τ(w). Then the per-lift gain is at least the per-lift main term, minus fixed costs divided by m, minus per-lift costs. If the fixed costs are of order x and the per-lift costs of order m, the balance point is m ≈ √x. Nothing in this uses ζ. The capture hypothesis is where arithmetic must enter.

| Item | Content | Label | Class |
| --- | --- | --- | --- |
| Proposition 7.1 | Twisting by 𝔞 scales covolume by N(𝔞)^d | READ (`shift_slope_mu`); COMPILED for rank 2 over ℤ | standard |
| Place-sum identity | Σ 2ℓe(s − τ) = Ga + Fo − Ee | DERIVED; COMPILED instance | algebra proved here |
| Theorem 7.2 | gain lower bound | DERIVED; COMPILED instance | algebra proved here |
| Error conversion to Lo | δ ≤ 2f/T, T ≥ b^(m/2) | READ | elementary |
| Mertens | Ta ≤ b² | READ | standard published |
| Theorem 7.0 | Frobenius congruence implies w-divisibility | READ; proof DERIVED | elementary algebra; on the chain through the κ bound (adm8), not through the gains (§8) |
| `LinkG` (a)–(d) | containment, lengths, gain sizes, capture | READ (statement) | construction input, unverified; (d) is the arithmetic heart |
| `LinkMu` | slope of the actual twisted lattice, up to C·X″ | READ (statement) | construction input, unverified |
| E-comparison, count, loss inputs | the m-scalings in 7.5 | READ | construction inputs, unverified |
| `MuRank`, `TuSize`, `SettingEventually`, crystalline comparison | the other inputs to the place conditions | READ (names only) | construction inputs, not read |

**Answer to the main question.** Repetition does not make the gain outgrow the main term: both are sums of m per-lift copies. It makes the fixed costs negligible, because they are paid once and shared across m lifts. The per-lift costs stay of order m. The exact statement that each lift earns its full share is `LinkG` clause (d), the capture inequality. It is a numeric inequality between explicitly defined quantities, with the gains set by a family field (§8). Theorem 7.0 is not its engine: it feeds the κ bound instead. The step from per-lift gains to slope is proved: Proposition 7.1 together with Theorem 7.2.

## 8. Tracing the capture clause LinkG (d) backward

**Picture first.** Think of a gain as an entry in a ledger, and of a valuation statement as the receipt showing the gain was earned. The question was where the receipt for gainⱼ(w) is. On the path that actually reaches RH, the ledger entry is written by definition. The one place on that path that asks for a receipt accepts an empty one: the map whose image is being measured is replaced by the zero map, and zero passes every valuation test. Theorem 7.0 does sit on the proof chain, but it pays a different bill. It feeds the bound on κ (how often the local lattice step fails), not the gain values.

### 8.1 The chain (READ, src-relative)

1. `linkG_concrete5` → `linkG_concrete_noKer` → `link_of_local_closed` → `linkG_fam_noKer` → `linkG_without_kernels` (LinkGConcreteNoKer.lean; AdmissibleFamilyNoKernel.lean:230). These lie on the unambiguous path to `riemannHypothesis` at depths 11 to 15 in the reach table. The variant that takes real chain maps, `linkG_concrete` with `LocalDataSystem` hypotheses, is not reached, and neither is `link_of_numbers_proved`.
2. `linkG_without_kernels` gets the admissibility package from `admissible_family_no_kernel` (line 186), feeds it to `AuxBlock8.Pf.stmtF` to obtain `Conclusion₂`, and passes that to `linkG_at_of` (PlaneCountTheoremWithConstants.lean:811), which calls `linkG_at_core` (line 718).
3. Inside `linkG_at_core`, clause (d) is assembled from three pieces. First, `ParametersFill` (IsResidueClassZero.lean:401) sets the stored gain equal to `gainP`, the stored τ equal to `tauP`, the stored io equal to `ioP`, the top set equal to `TTP`, and the stored partner weights equal to `fill` at the partner slot. Second, `AuxBlock8.Conclusion1` (SmallOrderPrimes.lean:15) says that for each prime p ≤ X″ in the residue class or split: 0 ≤ gainP ≤ 4|T|a/p, and Σ over lifts j and tops s in TTP of (askG − lo), minus m·fl, is at most (Σ over j of gainP) − tauP. Third, `lo_le_loG` and the top-set identity rewrite the von Mangoldt class sum into askG.
4. `Conclusion1` is one part of `Conclusion₂`, which `stmtF` proves from the admissibility package: adm1, adm2, adm3, the archimedean signature condition, adm5 to adm9, the twisted-place unit bound, `admG1`, and the size conditions.
5. `ParametersFill` itself is not derived. It is the field `fills` of the family structure `FamP` (ParConsts.lean:62). Any family the theorem is applied to must arrive with its gain already set equal to gainP.

### 8.2 The three questions

**Iteration.** Nothing on the path to LinkG (d) applies an order-one divisibility repeatedly, and no theorem on it establishes higher valuations. The gains are defined numbers.

**Accounting.** The odd-power terms enter by definition (IsResidueClassZero.lean):

- `g0` (line 246): the sum over tops s and odd exponents e (not excluded) of max(0, a(s)/p^e − capU(s, e)), minus a loss dl.
- `gU` (line 252): γ(p)·Σ a(s), minus the sum over non-V tops and odd e of min(a(s)/p^e, capU(s, e)), minus dl.
- `gainP` (line 355): over served orbits, max(gU − Pr, max(g0, 0)); over all other orbits, max(g0, 0). It is set to zero in the excluded case and for p > X″.
- `askG` (line 368): the sum over odd e of max(0, a(s)/p^e − fill at the partner slot).

So V(j, t, p) of §7 is askG, with w(j, t, p, i) equal to the partner fill, and the same odd-power ramps are written into gainP through g0. The capture inequality compares two sums of the same ramps, with dl, lo, fl, Pr and τ as the error terms.

**Transfer.** `ParametersFill`, which the family structure carries as a field. No valuation theorem produces it.

### 8.3 The one valuation statement on the path, and how it is discharged

`admG1` (SmallOrderPrimes.lean:220) has three clauses at each place w: (i) the sublattice NP lies inside p^⌈τ⌉ times the ramified lattice; (ii) the length of the quotient is at most v·d·(τ + io); (iii) every F in NP satisfies `vKge` at level (Σ over j of gainP) + lowFE. Clause (iii) says the theta-jet chain image of F lies in ϖ^⌈g·v⌉ times the lattice. That is the receipt.

In `admissible_family_no_kernel` the lattice instance is replaced by `zeroCh`, whose chain map is identically zero. `vKge_zero` then proves clause (iii) for every level g, because 0 lies in every lattice. The same lemma discharges `unitBoundAtTwistedPlaces` and `ServiceLowerValuation`. Clauses (i) and (ii) come from `gluing_statement_of_proof` and `gluing_statement_holds` (TopChoiceBounds.lean:1107, 1639).

This is logically valid. `Conclusion₂` does not mention the lattice instance, so `stmtF` may be fed any instance that makes the package true. What it shows is that the valuation clause plays no part in proving LinkG (d) (DERIVED from READ).

**Consequence.** LinkG (d) is a numeric inequality between explicitly defined quantities. Whether gainⱼ(w) is an actual valuation gain of the twisted theta-jet lattice has to be settled where the gain is used as a twist (the slope formula, LinkMu), not here. The real-chain valuation predicate `vKge` is reached on another branch: `WeilJacquetShalikaLaw.CmpV` → `Cp.SelectionServed` → `Fc.HypsAlt`. §9 traces it.

### 8.4 Where Theorem 7.0 actually sits

It is on the chain, by two routes (single-target lexical edges, usage-refs.csv).

1. **Into LinkG, through the κ bound.** `key_minor_dvd` → `kW_ord` → `key3Ord` (KeyMinorDvd.lean:222) → `stmtEExt_of_15c` (CoarseMultiplicity.lean:30) → `extendedClosedForm` (StandardPolynomials.lean:23) → field p15 of `local_flatness_results` (AdmissibleFamilyNoKernel.lean:65) → `loc8All_of` → `extended_windows_theorem` → `first_theorem_admitted_closed` (the κ-share bounds) → `first_theorem_threshold_functions` → the family First Theorem → adm8 → `linkG_without_kernels`. adm8 bounds the average of κ over the (a, b) box by Cm·|T|·N1/x^(A/2).
2. **Straight to RH.** `key3Ord` → `RangeOne.tensor_closed` → `G4.wClosed` → `windowShareRequirementClosedForm_proof` → `recS` → `classSel` → … → `everyCharacter` (depth 19).

`kW_ord` proves that the coefficients of a specific key polynomial, after a lifting substitution by an invertible matrix over the unramified Witt ring W(F of size p^n′), are divisible by w once. That is an order-one bound feeding a coarse multiplicity count, a count of where the local lattice step can fail. Through κ it controls which orbits are served (Sig ≤ x^−ε) and the io cost. It is not what produces the gain values. The sentence in §7 calling Theorem 7.0 the engine of clause (d) was wrong and has been corrected.

Not checked: whether the proof of `stmtF` uses adm8 for `Conclusion1` itself or only for the other parts of `Conclusion₂`. The lexical path shows that LinkG depends on adm8. It does not show that clause (d) does.

### 8.5 The proposed correction to Theorem 7.0

In the source, p is a natural number with a primality hypothesis, w² = p in A, and the congruence M^(p^e) ≡ N′ mod p is an assumption. The body uses only w² = p (so p ≡ 0 mod w) and that congruence; the primality hypothesis is never used. The Frobenius identity enters one level up: `kW_ord` supplies the congruence from `frobCong` (FrobeniusPaths/LatticeCountingFormula.lean:29), the Frobenius congruence in the unramified Witt ring, where p is prime. So the lemma is correct for an arbitrary commutative ring as stated. Stating p as a prime matches the source and costs nothing. The Frobenius identity belongs to verifying the lemma's hypothesis, not to its proof. Remark 7.0a records this.

### 8.6 Labels and open items

| Claim | Label |
| --- | --- |
| Chain 8.1, steps 1–5 | READ (source and reach tables) |
| Odd-power terms enter gainP and askG by definition | READ |
| Valuation clause of admG1 discharged by the zero chain map | READ; its consequence DERIVED |
| Theorem 7.0 on the chain via adm8 and via RangeOne | READ (lexical graph) |
| Primality unused in the proof of Theorem 7.0 | READ |
| Anything in this section | not COMPILED |

Open: (1) read the proof of `stmtF` for `Conclusion1` and record which admissibility inputs it consumes; (2) trace where the gain is used as a twist with the real chain map (the CmpV / SelectionServed branch, LinkMu). Item (2) is where the receipt question now lives.

## 9. Is the gain earned by the actual map?

**Picture first.** Picture two offices. The accounting office (LinkG) checks that the amounts written in the ledger beat the prime sums. It never looks at receipts, so a blank one is fine there. The receipts office is a different building: before the slope argument may use the twisted lattice, someone has to prove that the real theta-column map is divisible by ϖ to the ledger amount. That office exists, it checks the real map, and it uses the same ledger numbers. The zero map from §8 never goes there.

### 9.1 LinkMu: the slope change is bookkeeping too (READ)

- `LinkMu` is `NprimeMuR` (GlobalTheoremInputs.lean:69, 74): |μ(N(u)) − μ(NuH(u)) − Σ over places w of sz(w, sg(u, w))| ≤ C·X″. Here NuH(u) is the same Hermitian space with the lattice replaced by `L.NuLat u`, and sg(u, w) = Σ over lifts j of (gain + F − E) (DataParams₂.lean:215).
- It is proved by `J.linkMu` (SumLogPrimeFactorsLe.lean:728) through `nprimeMuR_at` (:694), using the family field `nprimeDef` (ParConsts.lean:71).
- `NprimeDef` (DataDIVDefs.lean:22) says the lattice of N(u) equals the span of a·y with a in Iu and y in NuLat(u), where Iu is the product over w of 𝔭(w)^(−⌊e(w)·sg(u, w))⌋) (line 17). The actual lattice is defined as the twist of NuLat by the gains.
- So LinkMu is Proposition 7.1, the twisting slope identity, applied to a lattice that is the twist by definition. It turns the numerical gain into a slope change without any arithmetic. The arithmetic question becomes whether that enlarged lattice is legitimate input for the slope inequality.

### 9.2 Where the receipt is (READ)

The slope inequality takes the map B(u) = `D.div.Bk u` and needs, from `LinkDIV_at` (GlobalTheoremInputs.lean:77):

1. `OneMapIntoCC` (DataArith.lean:180): B(u) sends the lattice of N(u) into the dual lattice of R. Since that lattice is NuLat enlarged by Iu, this is a divisibility statement: B(u) sends NuLat into 𝔭^⌊e·sg⌋ times the dual lattice. **This is the receipt for the gains.**
2. The archimedean height bound htMap(B(u)) ≤ h(u), required only when B(u) ≠ 0 (`htMap` sums over infinite places only; StatementPl.lean:60).

The receipt is proved on this path:

- `linkDIV_at_words` (RecBridge.lean:327) takes `WordFacts`, whose clause 1 is exactly the receipt (RecBridge.lean:128).
- `DivisionPackageFace.wordFacts` (RecBridge.lean:633) proves `WordFacts`. The package ties the pairing to the real map: B(u)(eNu x, eRR y) equals the column pairing, and the pairing equals the period `perCol` (field `dcPt`).
- Its valuation input is `ServJointF.val2AllAtRF` (ServJointF.lean:84): for φ in the untwisted lattice, the pairing is 0 or has w-adic valuation ≥ ⌊e·sg⌋.
- That comes from `LocalQuadraticParts.adm2` (LocalQuadraticParts.lean:206): for every φ in NuLat(u) and every test vector F, the actual period perCol(u, μ(w), φ, F) is 0 or has valuation ≥ ⌊e(w)·sg(u, w)⌋.
- `admissible_level_two` (AdmissibleAtGeneratorPlaces.lean:214) proves adm2. Away from the twist and generator places it calls `admissible_off_twist_places` (:171), which uses three things: the service statement for the real lattice instance Fm.Gy, `gainLe_of_fills` (the stored gain is at most gainS, which is gainP), and `period_geTU` (a column valuation gives a period valuation).
- The service statement is `WeilJacquetShalikaLaw.Conclusion1` (WeilJacquetShalikaLaw.lean:97): for x in NP, the actual theta column has valuation ≥ Σ over j of (gainS + F − ES) + vDG. It is proved by `kernel_valuation_served` (:348) from two inputs:
  - `CmpV` (:156): a valuation bound for the lattice chain at cmp(x) implies the same bound for the actual column. It is proved by `cmpV_of_cmpLite` (ColumnWeightComparison.lean:37), whose hypothesis `CmpLite` ties the chain to the actual column through `exists_chain`.
  - The lattice valuations for that tied chain, Σ gainP + low. These come from `SysTw` and the formal-group computations (`FormalGroupSystem.Pf.stmt_proved`) through `unit_bound_of_sum_over_primes` (JointsTw.lean:243) in `sum_over_primes_service` (SumOverPrimesHypotheses.lean:187).
- All of these meet at `shape_closed_link_n_of_green` (TopShape.lean:33). There the service hypothesis feeds the adm2 package (`closed_family_admissible_twist_link_alt`), which feeds the bridge rows for LinkDIV. LinkG is supplied separately (`closed_linkG_of_duty`).
- `cmpV_of_cmpLite` is on the unambiguous path to RH at depth 20: rowTwU\_of\_models → servH\_row → … → row\_hServ\_of\_link\_alt → hServ\_of\_linkR → allRows\_of\_open0\_alt.

**Caveat on the reach tables.** The lexical graph does not resolve dot-notation calls such as `P.wordFacts`. So `DivisionPackageFace.wordFacts` and `val2AllAtRF` show as unreached although `linkDIVt_of_rowsF` calls them. Those links are confirmed by reading the source.

### 9.3 The four checks

1. **LinkMu to the slope theorem.** LinkMu holds by definition of the twisted lattice (9.1). The slope theorem that consumes the twist is the frame argument (`frameReal_at_of`, TopDensityNGeSixteen.lean:679). It takes OneMapIntoCC and the conditional height bound from LinkDIV.
2. **Map requirements.** OneMapIntoCC and the height clause do not, by themselves, force B(u) ≠ 0: a zero map satisfies both. Nondegeneracy enters through a separate input, the matrix realization `MatReal_at` (Ball = Bf·Vr with Vr unitary and Gram matrices near the identity, built using LinkS). That is where a nonzero, nearly isometric map is required. In the off-chain record `FamRec.MatRec` the blocks are visibly B(u)'s matrices; the on-chain version of that tie is not yet checked.
3. **Same map?** No, and the difference is harmless. `admG1` (iii) concerns the chain map of the lattice instance, which the LinkG route replaces by zero. Nothing on that route reads clause (iii): `linkG_at_core` discards it, and NP and the length bound do not depend on the chain, because `yProd` (IsResidueClassZero.lean:453) uses only the vertex map. The slope map B(u) gets its receipt from the real lattice instance Fm.Gy through CmpV, whose chain is tied to the actual column. The zero map is a disposable witness; its vacuous bound never reaches the slope argument.
4. **Window-share branch.** `tensor_closed` (TensorOfPairLift.lean:597) is a second proof of the same extended closed form (field p15), fed through `inputs` into the First Theorem and then `wClosed` (the weight condition from mean excess, using the κ mean bound). It supplies counting bounds, not a valuation statement for the actual map.

### 9.4 Verdict and what moves down

The gains are not empty. The design splits them across two theorems that use the same numbers:

- the service branch proves that the actual theta-column map is divisible by ϖ to the amount Σ gainP (+ corrections), which licenses the twisted lattice in the slope inequality;
- the LinkG branch proves that those amounts beat the von Mangoldt prime sums.

The zero map belongs only to the second, where no map is needed (DERIVED from READ). The receipt question now moves one level down, to the two inputs of the service branch:

- `SysTw`: formal-group admissibility and the LowAt bounds for the tied chain;
- `CmpLite`: the chain computes the actual column.

Both are supplied by the row-service chain under the UpperTheory.Lit layer and are not yet traced. The tie of the frame's matrix blocks to B(u) (check 2) is also open.

| Claim | Label |
| --- | --- |
| LinkMu holds by the definition of the twisted lattice | READ |
| The receipt is OneMapIntoCC, proved from LocalQuadraticParts.adm2 on the actual period map | READ |
| adm2 comes from the service statement for the real lattice instance, via CmpV and formal-group bounds | READ |
| The zero chain never reaches the slope argument | DERIVED from READ |
| Window-share branch gives counting bounds only | READ |
| Anything in this section | not COMPILED |

## 10. Removing the zero-map shortcut: does the slope bound need a real map?

**Picture first.** The final inequality is a balance with two pans. The left pan is a lower bound on the slope of each twisted lattice N(u), and the gains are loaded here (through LinkG and LinkMu). The right pan is an upper bound coming from the map B(u) out of N(u) (the frame argument). A zero map could only cheat by sitting in the right pan. It cannot: the right pan is weighed using B(u)'s own matrix, and its inputs require that matrix to be most of a near-isometry, which a zero map is not.

### 10.1 Dependency structure (READ)

- `zeroCh` feeds only LinkG, through the auxiliary clauses of `admG1`, and nothing on that route reads the valuation clause (§8, §9).
- LinkMu does not depend on LinkG. In `topDesWin` (on the unambiguous path, depth 10) it comes from `linkMu_of_linkDIV` (SumLogPrimeFactorsLe.lean:775): LinkDIV's ZeroAbove clause, NuFull, MuRank, MuTu, MuDGam and the family field `nprimeDef`.
- The final slope bound is `linkCore` (LossesSmallShares.lean:38). The inputs that matter here:
  - **Lower pan, SlopesNF** (QuadraticLogDerivCongr.lean:181, 254): μ(N(u)) ≥ μ(base lattice) + Ga + Fo − Ee(u) − Lo(u), with a matching upper bound on μmax. It comes from `slopesNF_of` (TopDensityNGeSixteen.lean:1544) applied to PlacesF, and `placesF_of` (PlacesP.lean:638) needs both LinkG and LinkMu. The gains enter here, through Ga.
  - **Upper pan, FrameF** (QuadraticLogDerivCongr.lean:258): the rank-weighted average of μ(N(u)) − h(u), minus small terms, is at most μdual(R). It comes from `frame_at_of` (TopDensityNGeSixteen.lean:538) applied to `FrameReal_at` (:519), which carries D.div.Bk, OneMapIntoCC and the height bound.
  - **LatF** (positive ranks, μ ≤ μmax) from LinkDIV.

Corrected diagram: LinkG and LinkMu both feed PlacesF → SlopesNF (lower pan); LinkDIV (receipt), LinkS and LinkIRR feed MatK → FrameReal → FrameF (upper pan); `linkCore` compares the pans. `zeroCh` sits only on the LinkG input.

### 10.2 The upper pan uses the real map and requires it to be nondegenerate (READ)

- `MatK_at` (TopDensityNGeSixteen.lean:807), required on the chain through `matKF_of` (:1348), asks for matrices Ball(u) = Bf(u)·Vr(u) such that:
  - Vr(u) has orthonormal columns;
  - the rows of Ball(u) indexed by R are exactly the matrix of B(u) = `D.div.Bk u` at an infinite place, after invertible changes of basis; the other rows number Dall − Drows;
  - the normalized Gram KdG(u) = γ(u)·Bf(u)ᴴBf(u) is within e0·duS(u) of the identity in squared Hilbert–Schmidt norm, and each cross Gram KpG(u, u′) has squared HS norm at most (1 + η0)·duS(u)·duS(u′)/D\*.
- `matKF_of` builds this from BesselId (part of LinkDIV) through `blockReal_at_of` (:1283), and from the LinkS Gram bounds. `BlockReal_at` (:1087) identifies the R-rows of the period matrix with B(u)'s matrix.
- B(u) is one field, `D.div.Bk`, of the same datum. The receipt (OneMapIntoCC, §9) and the near-isometry constrain the same map.
- `D_eq` (DataRows.lean:71) gives Drows = (1 − delp)·Dall, so there are exactly delp·Dall extra rows. LinkIRR gives delp ≤ exp(−x^(ez/7)).

### 10.3 The zero-map test (DERIVED, with a numeric check)

**Lemma Z.** Let C(u), for u in a set W, be complex matrices whose columns all lie in one subspace of dimension e. Then (Σ over u of ‖C(u)‖²)² ≤ e·Σ over u, u′ of ‖C(u)ᴴC(u′)‖² (Frobenius norms).

*Proof.* P = Σ C(u)C(u)ᴴ is positive semidefinite with rank at most e. Its trace is Σ‖C(u)‖² and tr(P²) = Σ‖C(u)ᴴC(u′)‖². Cauchy–Schwarz on its at most e nonzero eigenvalues gives (tr P)² ≤ e·tr(P²). ∎

**Application.** Let W0 be the set of words where B(u) = 0. For u in W0 the R-rows of Ball(u) vanish, so the columns of C(u) = √γ(u)·Ball(u) lie in the e = delp·Dall extra coordinates. C(u)ᴴC(u′) = Vr(u)ᴴ·KpG(u, u′)·Vr(u′), so its norm is at most that of KpG. Write S0 for the sum of duS(u) over W0. Combine:

- the near-identity Grams, which give ‖C(u)‖² ≥ (1 − de − √e0)·duS(u) (using du ≥ (1 − de)·duS, the ramified-share bound);
- the cross bound;
- Dall ≤ (1 + η1)·D\* (LinkS).

Lemma Z then gives

S0·\[(1 − de − √e0)² − delp·(1 + η1)(1 + η0)\] ≤ delp·(1 + η1)(1 + √e0)²·D\*.

The error parameters e0, η0, η1, de are at most exp(−x^(ε/8)), and LinkIRR gives delp ≤ exp(−x^(ez/7)). So the words where B vanishes carry total rank at most about delp·D\*. The total rank is at least D\*/sg (the word-count step in `frame_at_of`), so they are a fraction of at most about delp·sg. In particular B(u) = 0 for every word is impossible: that would need delp close to 1.

A numeric check (`zero_map_check.py`) tests Lemma Z on 2,000 random instances (maximum ratio 1.000, which is equality in rank one). It also evaluates the all-words case: Bk = 0 everywhere would need delp ≥ 0.93 when every error parameter is 0.01, and delp ≥ 0.9993 when they are 10⁻⁴. This is a sanity check, not a proof.

### 10.4 Verdict

The decisive question was whether the critical hypotheses can be met by numerical gains plus a zero map while the final theorem still follows. They cannot.

- The zero map appears only in LinkG's auxiliary clause, which is never used.
- The final bound weighs the gains against an upper pan built from `D.div.Bk`. That pan's inputs require Bk to send the twisted lattice integrally into the dual lattice (the receipt). They also require Bk's matrix to be the main block of a near-isometry. By Lemma Z, that forbids Bk from vanishing except on words carrying a fraction of about delp·sg of the rank.

So the formal argument needs one map that both earns the gains and is nondegenerate (DERIVED from READ).

Not settled here:

- whether a datum satisfying all these constraints at once is actually built from the L-function. Until the construction is checked they are hypotheses on the datum, and this is where the empty-family and meaning questions now sit;
- the internal step BesselId → BlockReal (how Bk relates to the Bessel map Bu).

| Claim | Label |
| --- | --- |
| LinkMu is independent of LinkG; both feed PlacesF → SlopesNF | READ |
| The frame (upper pan) uses Bk's own matrix inside a near-isometry (MatK, BlockReal) | READ |
| Receipt and near-isometry constrain the same field `D.div.Bk` | READ |
| Lemma Z and the zero-map exclusion | DERIVED; numeric check only |
| Anything in this section | not COMPILED |

## 11. How the expert readings line up with this note

**Picture first.** Several people have now drawn maps of the same building from different doors. This section lays them on top of ours to see where the walls match, where we drew a room nobody else drew, and which rooms we have not entered yet. Source: Codex's report `rh-extraction/expert-map.md` (Nov 23). Expert statements are READ as reported there; the verdicts are DERIVED.

**Sources compared.**

- Alpöge's four-page announcement, with its twenty-step discovery journal.
- Rubinstein's draft v2 (Nov 22, 265 pages). It reduces the zeta case to hypotheses H0–H12.
- Robin Zhang's reconstruction (Nov 22, 76 pages).
- Tao's blog comments.
- The Lean FRO / Mathlib joint statement.
- The Lean Zulip discussion.

### 11.1 Agreement

The skeleton matches across all accounts:

- the window form of Landau's theorem (our Theorem 3);
- the exact character identity (Theorem 1);
- a chain of about √x theta lifts whose divisibility gains pay for the main term (Theorem 2);
- a comparison of divisibility with size through Bost's slope inequality;
- a rank estimate showing the family of maps covers enough directions.

Rubinstein's H1–H12 map onto our inputs (G), (Dv), (Ct), (E), (Sl), (SI), (L) and onto LinkS/LinkIRR, item by item. Zhang's Proposition 1.2 is the window bound our Theorem 2 delivers.

### 11.2 What this note adds

No other account traces both the divisibility receipt (§9) and the near-isometry used in the rank estimate (§10) to the same map, `D.div.Bk`. None of them gives the quantitative zero-map test either. Rubinstein's draft flags this common-map identification as unresolved (H8, O25). §§9–10 settle it at the level of the formal objects. Matching it to the classical period maps, with all normalizations, is still open (gap 4 below).

### 11.3 Corrections to this note

- **Theorem 3's anchor.** `zero_free_of_Chebyshev_growth` (Landau.lean:538) assumes growth bounds for all large x. The sparse-window step the proof actually uses is `level_of_tiedWin` (TopWin.lean:68) → `FormBAt` (Window.lean:30). The statement in §4 is the window version, as it should be; only the source pointer was wrong.
- **Literature count.** The namespace has 195 theorem declarations, counting the final implication; 194 precede it. Only 177 names contain `of_literature`. The handoff's "194 literature theorems, all of one form" overstated how uniform they are.
- **Single-integer picture.** An analogy in the handoff (a single integer divisible by many primes yet small) is only an illustration. The source compares a map, its image lattice and a mean slope, as Rubinstein says and as §10 confirms.

### 11.4 Open gaps, in order of consequence

1. **Denominators to height.** How the denominators of a Hecke projector become a cost in the height of the actual period map. This runs through the Iwasawa and Galois-cohomology window and lands in the summed error (Zhang §5; Rubinstein S8, H1, H9).
2. **Classical theta kernel versus the integral map in the receipts.** We need a worked normalization showing that the analytic kernel satisfies the integrality hypothesis and is the column that `CmpLite` ties the chain to. Rubinstein's lemniscate example, and a naive kernel that fails, make this testable.
3. **Size through the linear term.** Carry the covolume, norm, mass, dimension and level-change allowances to H1 with one normalization and an error small enough after averaging.
4. **One dictionary for rank and valuation.** Match the experts' classical period maps and inner products to `Bk`, `MatK_at` and `BlockReal_at`, with every rank and scaling.
5. **Good primes for each family member.** At each scale x on the detector window, use the actual prime pair from its supply scale, with uniform constants.
6. **Expository models.** Alpöge's abandoned routes, the 2/3 barrier and Rubinstein's worked examples. These explain the search; they are not missing premises.

Gaps 2 and 4 continue directly from §§9–10.

## 12. The common period map (closing gap 4; narrowing gap 2)

**Picture first.** Picture one camera lens, the period map P(u). Two photographs are taken through it. One is taken with a magnifying filter tuned to a prime: it shows the picture is divisible by that prime many times (the receipt). The other is taken with an even-light filter: it shows the lens barely distorts shapes (the near-isometry). The question the experts left open is whether the two photos really came through the same lens. This section shows they did, and names every filter setting.

**Theorem 12.1 (common period map).** Let D be one member of the family, at a scale x where the proof's inputs LinkDIV and LinkS hold. For each word u there are a nonzero complex number a(u), an isometry U(u) of the column space, and one isometry V of the target space (the same for all words) such that the following hold.

1. **One map.** For every rational column vector φ and every rational target vector x,

   ι(B(u)(φ, x)) = a(u) · ⟨ s(V x), P(u)(U(u) φ) ⟩.

   Here B(u) = `D.div.Bk u` is the map in the slope inequality, ι is the fixed complex embedding of the coefficient field, P(u) = `D.s.Pu u` is the period map from the column space into the cusp-form space H, and s = `D.sEE` embeds the target space in H. The right side is the Bessel period `D.besS`.
2. **Receipt.** B(u) sends the twisted lattice (NuLat enlarged by the gains, §9) into the dual lattice of the target. So the Bessel periods in part 1 are divisible by ϖ to the gain at every inert place.
3. **Near-isometry.** The normalized Gram operator K(u, u) = c(u)⁻¹ · P(u)\* P(u), with c(u) = vol(N)·vol(H)/dim π(u), satisfies ‖K(u, u) − 1‖² ≤ e0 · dim, with √e0 ≤ exp(−x^(ε/8)). LinkS also bounds the cross terms K(u, u′).

So the divisibility estimate and the rank estimate are statements about the same period map P(u). The normalizations between them are a(u), U(u), V, ι and c(u), and nothing else.

*Proof.* Part 2 is `OneMapIntoCC`, the first clause of LinkDIV\_at. Part 1 combines two clauses of BesselId, also inside LinkDIV\_at:

- BuRational: ι ∘ B(u) = Bu on rational vectors.
- The Bessel identity: Bu = a · besS(U·, V·).
- The definition besS(φ, F) = ⟨s F, P(u) φ⟩ (RhoDetPrimeEqMuTildeMulChiPow.lean:353).

Part 3 is the diagonal clause of LinkS\_at, with `hsDiagFull D u = ‖KD(u, u) − 1‖²` and `KD = Kmat` (RelevantZeroGramTerms.lean:339, 509). On the headline path, LinkDIV, LinkS and ChosenProviso are supplied for the family that `matKF_of` uses (TopDensityNGeSixteen.lean:1348). ∎

**Status.**

- The statement and proof are DERIVED from READ source.
- A Lean version is written: `rh-extraction/CommonPeriodMap.lean`, with `common_period_map`, the family version, `besS_eq` and `KD_eq`.
- Codex is to compile it against the preserved original project with its prebuilt cache and print its axioms (`codex-prompt-common-period-map.md`). It becomes COMPILED only when that run passes.

**What this settles and what it does not.**

- **Gap 4 (one set of objects): partly closed at the formal level; both lemmas compile (COMPILED, 23 Nov).** Rubinstein's H8/O25 and Zhang's Lemma 4.2 / Prop. 4.3 ask whether the rank estimate and the valuation estimate concern the same period maps. In the formal proof the integer map and the period map are tied by an exact coefficient identity, with the normalizations listed above. The first lemma carries the lattice inclusion and the Gram bound (Codex source check, 23 Nov). The second, below, adds the third section for the same map. Identifying the classical objects is still open. Both lemmas compiled on 23 Nov, against a source build of the 705 modules they import, using only the three standard axioms.
- **Gap 2 (classical theta kernel): narrowed.** What remains is classical: identifying P(u) = `D.s.Pu u` with the textbook theta-lift period map, including c(u) and the relative-trace expansion of K (`KExpansion`, RelevantZeroGramTerms.lean:345). The formal side of the receipt now ends at P(u).
- **Scale.** This is a bridging identification, not new mathematics. Its value is that it is exact, uses the source's own objects, and can be checked by machine.

**One map, three sections (READ, 23 Nov).** H8 asks whether one map β\_w gives (8a) the lattice inclusion, (8b) the height bound and (8c) the archimedean block of a larger complex map whose Grams obey Zhang's Lemma 4.2. In the source all three concern the same `D.div.Bk u`:

| Section | Formal statement | Where |
| --- | --- | --- |
| (8a) inclusion | `OneMapIntoCC` | `LinkDIV_at`, GlobalTheoremInputs.lean:77 |
| (8b) height | `htMap (Bk u) ≤ h u` when `Bk u ≠ 0` | `LinkDIV_at`, same line |
| (8c) archimedean block | `MatK_at`: matrix of `Bk u` at v, in normalized coordinates, is the top block of `Bf u · Vr u`; `Vr u` is an isometry; `Bf` meets the off-diagonal and diagonal Hilbert–Schmidt bounds | `matKF_of`, TopDensityNGeSixteen.lean:1348, from `BesselId` via `blockReal_at_of` (:1283) |

`frameReal_at_of` (:679) puts all three into one `LatGeom` record with a single `B`. `frame_at_of` (:538) then applies `joint_a_ramified_holds`, which turns them into the mean-slope bound `Frame_at`. This is the shape of Zhang's Proposition 4.3.

`CommonPeriodMap2.lean` states this as one theorem, `RHX.one_map_three_sections`. From the headline's own premises (`LinkDIV`, `LinkS`, `ChosenProviso`) on one family, every member eventually satisfies (8a), (8b) and `MatK_at`, with η0 and √e0 at most exp(−x^(ε/8)). It packages what the source proves and adds no new mathematics. COMPILED on 23 Nov: Lean reports only propext, Classical.choice and Quot.sound. The script `compile-closure.ps1` builds the 705 modules it needs from source.

## 13. Gap 5: one pair of primes per window

The formal proof answers Rubinstein's H12 witness by witness. It picks one pair (q, d) for each detector window and uses that same pair at every point x in the window. Every constant is fixed before the window is chosen. The argument is `winPairs` (WinPairs.lean:5), about 70 lines of elementary bookkeeping (READ).

**The chain.**

| Step | What it gives | Where |
| --- | --- | --- |
| Good pairs exist | For every scale Y ≥ Y1, some pair (q, d) is good on all of \[Y, Y^A\]: prime-sum and log-derivative bounds for the twisted characters, plus zero-free boxes (`PairGood`) | `QH.pairEx`, MeanSquareBounds/pairEx.lean:112, from the mean-square bound |
| Cohomology window | For X ≥ X0 and any pair of the right shape at scale X^(1/J), there is W with X^(1/J) ≤ W and W² ≤ X, and the Galois-cohomology bound holds for every x′ in \[W, W²\] (`VWinAt`) | ExistsPageN.lean:44 |
| Detector window | For every y there is Z ≥ y such that every x in \[Z, Z^(3/2)\] has a `WinDatum`: a scale Y in \[x^(1/J), x\], a pair good on \[Y, x\], and the cohomology bound at x | `winPairs`, WinPairs.lean:5 |
| Hosts | One host per scale on the detector window, built from the window's own pair, with constants CT2, C8, c6, Cb and x1 fixed before the scale | `supplyOfAdmOf`, ShortNorms/supplyOfAdmOf.lean |

**The argument, in classical terms.** Fix ψ, ε < 1/52 and c ≥ 1, and put k = c^(1/(2+8ε)).

1. Choose M ≥ max(1, y, Y1, k³, k⁴⁰⁰) and X ≥ max(X0, M^J). Put Y = X^(1/J), so Y ≥ M.
2. Take the pair (q, d) that is good at scale Y. It is good on \[Y, Y^J\] = \[Y, X\].
3. Apply the cohomology window to this X and this pair to get W. Put Z = kW.
4. Take x in \[Z, Z^(3/2)\]. Since W ≥ k³, Z^(3/2) ≤ W² ≤ X. So Y ≤ W ≤ x ≤ X and x^(1/J) ≤ Y, and the pair is good on \[Y, x\].
5. The point x/k lies in \[W, W²\], so the cohomology bound holds there. The exponent e = e(x/k) gives 2^e of size x^(2+8ε)/c, and k⁴⁰⁰ ≤ x/k turns the bound at level 401 into the level 400 the detector needs.

So the two windows serve different quantifiers, as the expert map says. The detector window \[Z, Z^(3/2)\] is the cohomology window \[W, W²\] shrunk by the factor k. One pair, chosen at the window's starting scale, serves every x in it.

**Estimates B and C (DERIVED mapping).** [Rubinstein v2](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf) (§I.6(e), pp. 17–18) separates what the pair must satisfy from what follows for it.

| Rubinstein | Statement | Lean |
| --- | --- | --- |
| Estimate B, the pair must satisfy it | \|Gχ(x)\| ≤ x^(1/2+ε) for χ\_q, χ\_d and χ\_qχ\_d on \[Y, Y^(3/2)\]; proved as Thm III.1.1(d) | `PairGood.bounds` at modulus one: the twists with (i, j) ≠ (0, 0) are exactly these three characters. It is word for word his Thm III.1.1(d) (p. 61, eq. III.2): \|Gχ(y)\| ≤ y^(1/2+ε/2) and \|L′/L(1, χ)\| ≤ 4 log y, which implies Estimate B. `qdq_of_pair` (PairRows.lean:299) turns it into `QDq`. |
| Estimate C, follows for such pairs | \|Gχ(y)\| ≤ y·exp(−κ x^(ε/8)) for very large y; Thm III.2.1, using a further property of the pair, Thm III.1.1(e) | Derived from `PairGood.boxes` (zero-free boxes near Re s = 1) through `boxq_of_pair` (PairRows.lean:170). Thm III.1.1(e) (p. 61, eq. III.3) is exactly `PairGood.boxes`. Both state no zeros for Re s > 1 − 1/400 and \|Im s\| ≤ 8M·exp(Y^(ε/5))·exp(Y^(ε/5)(log Y)²), the Lean `height` at j = 1. His Remark (4) says (e) excludes exceptional real zeros when deriving C. Read through a GPT quotation; every number matches the Lean definition. |

One more point settles the compatibility worry. `VWinAt` is applied to this very pair, and the number fields in the cohomology bound are cut out by ψ, q and d (`IsChiField`). So the analytic estimates and the arithmetic bound concern the same (q, d).

**Prior work (READ, 23 Nov).** [Adriazola's 225-page manuscript](https://github.com/jimjamzola/RH-Alpoge-Reconstruction) gives the same window structure in conventional terms (§18, admissible data with a base Y₀, and Proposition `dataexist`). It also states that the constant is uniform. So the classical version of §13 is his, and credit goes to him. What this section adds is the exact Lean route (`winPairs`, `supplyOfAdmOf`) and the B/C match with Rubinstein. His Selmer bound on windows is still listed as open (class O) in his §19.

## 14. Gap 2: a test bench for the theta kernel

Rubinstein's worked lemniscate example and his failing theta kernel reproduce exactly in an independent computation. The failing kernel misses the needed divisibility rate by exactly one factor of p, not just at the single point he reports. Script and output: `rh-extraction/gap2_lemniscate_check.py` and `gap2_lemniscate_results.txt`. Exact integer and rational arithmetic, 14 s (COMPUTED).

| Check (Rubinstein v2) | His value | Ours |
| --- | --- | --- |
| Hurwitz numbers A\_n = sl^(n)(0): A₁, A₅, A₉, A₁₃, A₁₇ | 1, −12, 3024, −4390848, 21224560896 | same |
| Thm Le18: v\_p(A\_n) ≥ ⌊np/(p²−1)⌋, inert p < 200, n ≤ 2001 | no violations | no violations |
| p = 3: equality cases; largest excess over np/(p²−1) | 418 of 501; 4.625 at n = 1945 | 418 of 501; 4.625 at n = 1945 |
| Split primes 5, 13, 17, 29 never divide A\_n; A\_(4k+1) ≡ 3^k mod 5 | yes; yes | yes; yes |
| Split p < 200 dividing some A\_n, n ≤ 2001 | 157, 181 | 157, 181 (up to p < 2000 there are 30 such primes) |
| Le13: arcsl(t) + (1/p)·arcsl(t^(p²)) is p-integral; with minus it fails at degree p² | yes | integral to degree 4000 for p = 3, 7, 11; minus fails first at 9, 49, 121 |
| Naive Θ over ℤ\[i\]: r₁…r₅ | 1/4, 17/16, −111/64, 12513/256, −146079/1024 | same; denominators divide 4^k for k ≤ 30 |
| Θ/T₀ = σ²℘ | stated | lattice sums T₀…T₁₂ agree with the formula to 15 digits |
| Failure: v₃(r₃₀) vs 120·3/8 | 14 vs 45 | 14 vs 45 |
| Size: log\|T₁₂₀\| vs ½ log(120!/π¹²⁰) | 119.0 vs 160.2 | 119.0 vs 160.2 |

**New observation (numerical, not proved).** For the naive kernel, v\_p(r\_k) stays within 2 of n/(p²−1), where n = 4k. This holds for every n ≤ 300 and p = 3, 7, 11, 19. The lemniscate reaches np/(p²−1), so the naive kernel falls short by exactly a factor of p in the rate. At n = 300 and p = 3 the values are 38, 37.5 and 112.5. The match with n/(p²−1) is most telling at p = 3, where that rate reaches 37.5. At p = 11 and 19 both numbers stay small, so those primes mainly confirm the shortfall against np/(p²−1), which is 27.5 and 15.8 at n = 300.

**The Lean side (READ).** The integral-coordinate hypothesis is `BHyp` (GaussJetBounds/Statement.lean:85). It requires four things:

- coefficients in an unramified field;
- invariance under the torus action;
- no terms of low bidegree;
- after the substitution `letterLog`, which is the model logarithm Σ X^(l^(2e))/l^e, the series exp(de1 β) and exp(de2 β) have integral coefficients.

A column's theta series must have `HasThetaProductForm` (ColDefs.lean): written in logarithm coordinates, it is an integral factor times exp(Σ ±β), with `BHyp` for each β. `bHyps_of_beStd` (StandardSeriesBConditionsLargePrime.lean:145) proves `BHyp` for every standard β built from level-one biextension data, for primes l ≥ 5. That has the shape of Rubinstein's β̃(z, w) = m(z+w) − m(z) − m(w).

Two things remain. First, the dictionary: show that the classical theta kernel is a column of this form with standard β. Second, the prime 3: Lean's prover assumes l ≥ 5, while Rubinstein's worked case is ℓ = 3.

**Prior work (READ, 23 Nov).** Adriazola's 225-page manuscript builds its kernel from the normalized σ-function of a CM curve, with a height-two formal group at inert primes. Its LaTeX source never mentions the lemniscate or a naive kernel, so this test bench does not repeat anything there. His §19 also lists the dictionaries between the abstract Bessel realization and the automorphic objects (Hypotheses H-dict and H-rat) as open (class O). That is the same open point as Part B and gap 4.

## Appendix: source locations and references

Paths are relative to `src/` at commit e50d09817ad81469f737e8f637561e6ccf86c670 of the [riemann-hypothesis repository](https://github.com/Deicyde/riemann-hypothesis/tree/e50d09817ad81469f737e8f637561e6ccf86c670/src).

| Statement in this note | Source location |
| --- | --- |
| GRH for all Dirichlet L-functions | `Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean:13` |
| RH as the modulus-1 case; reflection to Re s = 1/2 | `Formalism/GammaFactorNonvanishing/CritLine.lean:29` (`rh_of_every`), same file (`critLine`) |
| Detectors G\_1, G\_χ (§1) | `Formalism/StatementOC.lean:11–13`; `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Analytic.lean:11–24` |
| Group setting of Theorem 1 | `Formalism/ThickAverageLoss/PartnersToFactorsAt.lean:13–26` |
| A, Main, ψ̃, G\_ψ and the identity as a statement | `Formalism/SizeWindowBrackets/FirstPrimeNeSecondPrime.lean` (`HostFacts`, `primVal`, `GPsi`, `ASK`, `MAIN`, `AskMainBalance`) |
| Theorem 1, proof in source | `Formalism/SizeWindowBrackets/ChainSlopeWindows/StronglyIrreducible.lean:695` (`colour_balance`) |
| Lemma 2.3: character attachment in source | `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Analytic.lean:106` (`IsPrimOf`) |
| Lemma 2.1 with D = 1 | `Formalism/LatticeSlopes/Statement.lean:75`; proof `Formalism/LatticeSlopes/LatticeSlopesProofs/SlopeInequality.lean:111` |
| Lemma 2.2 (period cancels) | `Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean:105` (`key_identity5`) |
| Theorem 2 (the averaged chain) | `LevelOfCongruence.lean:50` (`s_lower5`), `:113` (`Ga_bound5`), `:175` (`each_unit_bound_statement`); hypotheses `Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean:19–35` and `Formalism/RankGapBounds/MeanBoundSecondForm.lean:107–163` |
| What the numbers are (slopes, place sums) | `Formalism/SizeWindowBrackets/Chain2aCoreNoAnalytic.lean:226` (`mkData`); slope normalization `Formalism/HarderNarasimhan/StatementPl.lean:64` |
| The source proves the hypotheses for its construction | `Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean:158–211` |
| Remark 2.4: error bound and size conditions | `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean:37`; `QuotientSlopeBoundsWith.lean:45` (`ErrX5at`); `Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean:16, 133`; `Formalism/SizeWindowBrackets/SChain.lean:53, 114` |
| (CH): local divisibility engine | `Formalism/SharpRestriction/GrowthBounds/CoarseMultiplicity/KeyMinorDvd.lean:132` |
| (CH): flatness (exact orthogonality with tiny errors) | `Formalism/SharpRestriction/GlobalTheoremInputs.lean:144–157` |
| (CH): Iwasawa loss on windows | `Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:104`; `…/DenseThresholdCases/HVCore.lean:18` |
| Bridge (B) | `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChCore.lean:283, 343, 427`; `…/LandauTheorems/ChBalance.lean:200`; `Development/AutomorphicArithmetic/MeanSquareBounds/meanSqK.lean:51`, `twistK.lean:148` |
| Family M\_ψ and weight 1/(3o+1) | `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean` (`Level.Gm`, `Level.cyc`) |
| Theorem 3: the source's own window argument | `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/` (`WindowHypOfRpow`, `lemmaL`, `poleData`, `landauWindow`); windows \[Y, Y^(3/2)\] at `EveryCharacter.lean:8` |
| Load-bearing check of Theorem 2's hypotheses (ours, compiled) | `rh-extraction/TransferSkeleton.lean` in the handoff folder |

**Standard references (cited by title).**

- H. Davenport, *Multiplicative Number Theory*, chapters 17 and 19: the explicit formulas.
- H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I*, chapter 12: explicit formulae.
- J.-B. Bost, "Périodes et isogénies des variétés abéliennes sur les corps de nombres", Séminaire Bourbaki 795: the slope inequality.
- B. Ferrero and L. Washington (1979): μ = 0 for abelian number fields.
- S. Chowla and A. Selberg (1967): periods of CM elliptic curves.
