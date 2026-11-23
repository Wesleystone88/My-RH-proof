# Checking the exceptional squarefree class

Fix a modulus $m$, a cutoff $N$, and nonnegative weights $c(1),\ldots,c(N)$. For each integer $a$, record one bit per prime outside $m$. The bit is the parity of that prime's exponent in $a$. Let $A(v)$ be the sum of the weights with bit vector $v$. Missing vectors have weight zero.

For any squarefree product class $r$, let $s$ be its bit vector. If $ab$ belongs to class $r$, the vector of $b$ equals the vector of $a$ with the bits of $s$ toggled. Write that permutation as $v\mapsto v\oplus s$. Nonnegativity gives the first inequality below. Summing $(A(v)-A(v\oplus s))^2\ge0$ gives the second.

$$
 \sum_{a,b:\,\operatorname{rep}_m(ab)=r} c(a)c(b)
 \;\le\;\sum_v A(v)A(v\oplus s)
 \;\le\;\sum_v A(v)^2
 \;=\;\sum_{a,b:\,\operatorname{rep}_m(ab)=1}c(a)c(b).
$$

This compares the *exceptional* class to the entire *trivial* class, including pairs of different integers with the same parity vector. For instance, 2 and 8 have the same parity at every prime. The formula works for every cutoff and every nonnegative sequence. The bound has constant one. For $m=1,N=2,c(1)=c(2)=1,r=2$, both ends equal 2.

In the original mean-square proof, Page's theorem and separation of quadratic characters leave at most one exceptional class. Its character correlation has absolute value at most the number of primes in the family. Once the trivial class has been estimated, the display therefore pays for both classes at a cost of at most twice the trivial-class budget. This removes the need for a separate bound on the maximum weight of a single prime bucket in this step. Constants can differ across the two estimates. The prime correlation estimate and the geometric transfer to zeta remain inputs to their respective steps.

The original proof uses a finer split according to whether the exceptional label is prime or composite. Its inequality is $2B^2+2B R$, with $B=C_2\log y$ and $R\le5C_1\sqrt y$. Both estimates fit the $O(y\log y)$ budget. [Original pair estimates](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/MSqPairs.lean#L307) · [Application](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/meanSqK.lean#L149)

## Lean files

* `Squarefree.lean` defines the representative as the product of primes with odd exponent outside the modulus. Its theorem `class_le_trivial` states the displayed bound directly over the integers $1,\ldots,N$, represented by `Fin N` plus one.
* `ParityEnergy.lean` gives the underlying identity over a commutative ring using Lean's standard library. It expresses the exact difference of the two sums as a sum of squares.
* `ScalarBridge.lean` divides the arithmetic design inequality by its positive multiplier. The density of the second subset cancels from the term involving $k$. Two further lemmas isolate the analytic contradiction from decaying geometric powers and the choice of a window exponent below a putative zero.

The toolchain and Mathlib dependency are pinned in this directory. To replay the declarations from this directory with Lean and Lake installed:

```text
lake update
lake exe cache get Mathlib.Analysis.SpecialFunctions.Pow.Real Mathlib.Data.Nat.Squarefree Mathlib.Tactic.FieldSimp Mathlib.Tactic.Linarith Mathlib.Tactic.Positivity Mathlib.Tactic.Ring
lake build
```
