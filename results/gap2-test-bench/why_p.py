"""Why is the naive Z[i] theta kernel exactly one factor of p short?

Companion to gap2_lemniscate_check.py (same folder). Exact rational arithmetic only.

Setup (lemniscatic lattice g2 = 4, g3 = 0, primes p = 3 mod 4, i.e. supersingular):
  naive kernel        f(u) = sigma(u)^2 wp(u)
  its EGF numbers     r_n  = n! [u^n] f      (Rubinstein's r_k, up to the unit 16^k)
  slow rate (seen)    v_p(r_n) ~ n/(p^2-1)
  full rate (needed)  v_p(r_n) ~ n p/(p^2-1)   (what sl's EGF numbers A_n get, Hurwitz)

Sections
  A. denominator growth per degree of each ordinary-coefficient series
  B. where the first 1/p sits in log(sigma/u), and how big it is on the disk where sigma lives
  C. remove that single term and remeasure the EGF numbers
  D. two checks that did NOT explain it (kept for the record)
  E. the bookkeeping identity

Run:  python why_p.py            (about a minute)
Author: Timothy Wesley Stone, with Claude (Opus, chat). Numerical, not a proof.
"""
import math, os, sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gap2_lemniscate_check import wp_coeffs, series_exp, vpq, lemniscate_A

if '--extended' in sys.argv:          # T2 extension; the default output below is unchanged
    from why_p_extended import run
    run()
    sys.exit(0)

N = 240
PRIMES = (3, 7, 11, 19)

def mul(a, b, M):
    c = [Fr(0)] * (M + 1)
    for i in range(M + 1):
        if a[i]:
            for j in range(M + 1 - i):
                if b[j]:
                    c[i + j] += a[i] * b[j]
    return c

def series_log(a, M):          # log of a series with a[0] = 1
    out = [Fr(0)] * (M + 1)
    for n in range(1, M + 1):
        out[n] = (n * a[n] - sum(k * out[k] * a[n - k] for k in range(1, n))) / n
    return out

# ---------------------------------------------------------------- the series, ordinary coefficients in u
c = wp_coeffs(N // 2 + 2)                                   # wp = u^-2 + sum c_k u^{2k}
L = [Fr(0)] * (N + 1)                                       # log(sigma/u) = -sum c_k u^{2k+2}/((2k+1)(2k+2))
u2wp = [Fr(0)] * (N + 1); u2wp[0] = Fr(1)                   # u^2 wp
for k, ck in c.items():
    if 2 * k + 2 <= N:
        L[2 * k + 2] = -ck / ((2 * k + 1) * (2 * k + 2))
        u2wp[2 * k + 2] = ck
E = series_exp([2 * x for x in L], N)                       # (sigma/u)^2
F = mul(E, u2wp, N)                                         # f = sigma^2 wp
A = lemniscate_A(N + 2)
slu = [Fr(A[n + 1], math.factorial(n + 1)) for n in range(N + 1)]   # sl(u)/u

def min_rate(ser, p, lo=40):
    return min(vpq(ser[n], p) / n for n in range(lo, N + 1) if ser[n] != 0)

def egf_dev(ser, p, rate):
    devs = [vpq(math.factorial(n) * ser[n], p) - n * rate for n in range(4, N + 1, 4) if ser[n] != 0]
    return min(devs), max(devs)

print('A. Denominator growth per degree: min over n>=40 of v_p([u^n] series)/n')
print('   (full rate allows -1/(p^2-1); the slow rate corresponds to -p/(p^2-1))')
for p in PRIMES:
    q = p * p - 1
    print(f'   p={p:2d}: allowed -1/(p^2-1) = {-1/q:+.4f}, -p/(p^2-1) = {-p/q:+.4f} | '
          f'sl/u {min_rate(slu, p):+.4f}  log(sigma/u) {min_rate(L, p):+.4f}  '
          f'(sigma/u)^2 {min_rate(E, p):+.4f}  sigma^2 wp {min_rate(F, p):+.4f}')

print('\nB. The first 1/p in log(sigma/u)')
for p in PRIMES:
    q = p * p - 1
    first = min(n for n in range(2, N + 1) if L[n] != 0 and vpq(L[n], p) < 0)
    cp = c[(p - 1) // 2]                                    # coefficient of u^(p-1) in wp
    on_circle = vpq(L[p + 1], p) + Fr(p * (p + 1), q)       # v(L_{p+1} u^{p+1}) when v(u) = p/(p^2-1)
    first_wp = min((2 * k for k, ck in c.items() if 2 * k <= N and ck != 0 and vpq(ck, p) < 0), default=None)
    print(f'   p={p:2d}: first p-denominator of log(sigma/u) at u^{first}; L_{p+1} = {L[p + 1]} '
          f'= -c/(p(p+1)), c = [u^{p-1}]wp = {cp}, v_p(c) = {vpq(cp, p)}; '
          f'on the circle v(u)=p/(p^2-1) this term has v = {on_circle} (exp needs > 1/(p-1) = {Fr(1, p - 1)}); '
          + (f'wp itself first has a p-denominator at u^{first_wp}' if first_wp else f'wp has no p-denominator up to u^{N}'))

print('\nC. EGF numbers v_p(n! [u^n] f): deviation from the full rate np/(p^2-1) and from the slow rate n/(p^2-1)')
for p in PRIMES[:3]:
    q = p * p - 1
    Lc = L[:]; Lc[p + 1] = Fr(0)
    Fc = mul(series_exp([2 * x for x in Lc], N), u2wp, N)
    for name, ser in (('naive', F), ('only u^(p+1) term removed', Fc)):
        lo_f, hi_f = egf_dev(ser, p, p / q); lo_s, hi_s = egf_dev(ser, p, 1 / q)
        n = max(m for m in range(4, N + 1, 4) if ser[m] != 0)
        print(f'   p={p:2d} {name:27s}: vs full [{lo_f:+.1f}, {hi_f:+.1f}]   vs slow [{lo_s:+.1f}, {hi_s:+.1f}]   '
              f'at n={n}: v={vpq(math.factorial(n) * ser[n], p)}, full rate {n * p / q:.1f}')

print('\nD1. (did not explain it) degrees divisible by p^2-1 are just as bad as the rest')
for p in (3, 7, 11):
    q = p * p - 1
    inv = [(m, vpq(F[m], p)) for m in range(q, N + 1, q) if F[m] != 0]
    print(f'   p={p:2d}: (degree, v_p) at multiples of {q}: {inv[:8]}')

print('\nD2. (did not explain it) rewriting f in the formal-group coordinate t = sl(u) keeps the same growth')
M = 120
arc = [Fr(0)] * (M + 1)
for k in range(0, (M - 1) // 4 + 1):
    arc[4 * k + 1] = Fr(math.comb(2 * k, k), 4 ** k) / (4 * k + 1)
G = [Fr(0)] * (M + 1); P = [Fr(0)] * (M + 1); P[0] = Fr(1); G[0] = F[0]
for n in range(1, M + 1):
    P = mul(P, arc, M)
    if F[n]:
        for k in range(M + 1):
            if P[k]:
                G[k] += F[n] * P[k]
for p in (3, 7, 11):
    print(f'   p={p:2d}: min over m>=40 of v_p([t^m] f(arcsl t))/m = {min(vpq(G[m], p) / m for m in range(40, M + 1) if G[m] != 0):+.4f}'
          f'   (p/(p^2-1) = {p / (p * p - 1):.4f})')

print('\nE. Bookkeeping: n! supplies n/(p-1) = (p+1) * n/(p^2-1) factors of p.')
print('   sl spends 1 share on denominators and keeps p shares   -> np/(p^2-1)  (full rate)')
print('   sigma^2 wp spends p shares and keeps 1                  -> n/(p^2-1)   (slow rate)')
print('   p shares spent = one term L_{p+1}u^{p+1} with a single 1/p, compounded by exp:')
print('   (L_{p+1}u^{p+1})^m/m! costs m + m/(p-1) = mp/(p-1) factors of p at degree m(p+1), i.e. p/(p^2-1) per degree.')
