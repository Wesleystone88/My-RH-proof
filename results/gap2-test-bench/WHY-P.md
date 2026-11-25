# Why the naive kernel is exactly one factor of p short

Author: Timothy Wesley Stone, with Claude (Opus, chat). This is a numerical finding, not a proof.
Script: `why_p.py` (same folder, exact fractions, runs in seconds). Output: `why_p_results.txt`.

## The question

The test bench (`gap2_lemniscate_check.py`) found two divisibility rates. The rate is how many factors of p the n-th number carries:

| Numbers | Rate | Status |
|---|---|---|
| A_n, the lemniscate sine's | n·p/(p²−1) | the full rate |
| r_n, the naive kernel σ²℘'s | n/(p²−1) | the slow rate |

Why is the gap a factor of exactly p? The primes tested are p ≡ 3 mod 4 (the supersingular ones): 3, 7, 11 and 19.

## The answer, as a budget

Think of each n-th number as being paid in coins, where one coin is one factor of p.

- The factorial n! hands out n/(p−1) coins. That equals (p+1) shares of n/(p²−1).
- Any denominators in the series' ordinary coefficients spend some of those shares. What is left is the rate.

| Series | Shares spent on denominators | Shares kept | Rate |
|---|---|---|---|
| sl(u) | 1 | p | n·p/(p²−1), the full rate |
| σ²℘ | p | 1 | n/(p²−1), the slow rate |

So the two series are mirror images, and a factor of p falls out of the bookkeeping (section E of the output).

## Who spends the extra p−1 shares

One single term does it: log(σ/u) at degree p+1.

To get log σ you integrate ℘ twice, which divides the u^(p−1) term of ℘ by p·(p+1).

- That coefficient of ℘ is a p-unit in every case computed. So log(σ/u) picks up its first 1/p at exactly u^(p+1), with L_(p+1) = −c/(p(p+1)).
- ℘ itself has no p-denominator until u^(p²−3), much later: for example u^46 at p = 7 and u^118 at p = 11.
- σ = u·exp(log(σ/u)). The exponential turns one 1/p into a compounding debt. (L_(p+1)·u^(p+1))^m / m! costs m + m/(p−1) = m·p/(p−1) coins at degree m(p+1). That is p/(p²−1) coins per degree: exactly p shares.

There is also a geometric picture. On the disk where σ's series lives, at radius v(u) = p/(p²−1), this one term has size exactly 1/(p−1). That is the edge where exp stops converging. The output checks this for all four primes (section B).

## The decisive check (section C)

Delete only that one term and remeasure.

| p | Naive, at n = 240 | One term removed | Full rate |
|---|---|---|---|
| 3 | 28 | 68 | 90 |
| 7 | 4 | 30 | 35 |
| 11 | 1 | 20 | 22 |

Removing a single coefficient moves the numbers from the slow rate most of the way to the full rate. What is left is smaller and comes from later terms of log σ that also carry a p. It is largest at p = 3, where those terms come early.

## What did not explain it (kept on purpose)

- **D1:** degrees divisible by p²−1 are just as bad as the others. So the defect is not about averaging over the unit group.
- **D2:** rewriting the kernel in the formal-group coordinate t = sl(u) keeps the same denominator growth. A change of coordinate does not remove it; the debt is in σ itself.

## What is open

- This is measured, not proved, and only for the lemniscate at p = 3, 7, 11, 19 up to degree 240.
- The size of the p-adic sigma function at supersingular primes is a studied topic: Bannai, Kobayashi and Yasuda, *The radius of convergence of the p-adic sigma function*, Math. Z. 286 (2017) 751–781. We could not read their theorem (paywalled), so we do not know whether it states this exact radius. This is likely known there and should be checked before calling anything here new.
- A pointer, not tested: the proof's model logarithm (`letterLog`, L+ = Σ X^(l^(2e))/l^e) first divides by l at degree l², not at degree l+1. That is the structural opposite of the naive kernel's early 1/p.

## Extension to p = 23, 31, 43, 47 and n up to 600 (25 Nov 2026, COMPUTED)

Run: `python why_p.py --extended` (code in `why_p_extended.py`; the default output of `why_p.py` is unchanged, checked by diff). Pre-registered criteria and full output: `why_p_extended_results.txt`. Written by Claude Code from `prompts/claude-code-prompt-2026-11-25d.md` (written by Claude in chat).

**Verdict: FAIL as pre-registered, because of one prime, p = 3, and only on criterion (1).**

| p | (1) deviation of naive v_p(n!·r_n) from n/(p²−1), n ≤ 600 | (2) gap closed by removing L_(p+1), n = 600 |
|---|---|---|
| 3 | [−2.50, +1.50] **outside ±2** | 0.667 (p < 7, not required) |
| 7 | [−1.17, +1.42] ok | 0.861 ok |
| 11 | [−1.00, +0.97] ok | 0.902 ok |
| 19 | [−1.00, +0.99] ok | 0.946 ok |
| 23 | [−1.00, +0.99] ok | 0.955 ok |
| 31 | [−0.61, +0.87] ok | 0.980 ok |
| 43 | [−0.32, +0.99] ok | 0.931 ok |
| 47 | [−0.27, +1.74] ok | 0.940 ok |

Reading: for every p ≥ 7, including the four new inert primes, the naive kernel stays on the slow rate n/(p²−1) (within ±1.74) and removing the single term L_(p+1) closes 86–98% of the gap to the full rate n·p/(p²−1), rising with p. The failure is at p = 3 only: the deviation reaches −2.50 at n ≤ 600 (it was −2.0 at n ≤ 240), so the pre-registered ±2 band is exceeded by a bounded-looking but growing-with-n wobble; at p = 3 removing the term also closes only 67% (the earlier note already says p = 3 has later p-denominator terms that come early). I did not change the criterion after seeing the result. Whether the p = 3 deviation keeps growing with n was not tested beyond 600.
