"""Gap 2 test bench: independently recompute Rubinstein v2's worked lemniscate example
(Sec. III.12, Thm Le18, Le13, Le20a) and the naive Z[i] theta kernel failure (Sec. I.4).

Everything below is exact integer/rational arithmetic, except the cross-check of the
theta identity, which uses mpmath at high precision.
"""
import math, sys, time
from fractions import Fraction as Fr

def vp(n, p):
    if n == 0:
        return math.inf
    n = abs(n); v = 0
    while n % p == 0:
        n //= p; v += 1
    return v

def vpq(x, p):
    return vp(x.numerator, p) - vp(x.denominator, p)

# ---------------------------------------------------------------- 1. lemniscate sine coefficients
# sl'' = -2 sl^3, sl(0)=0, sl'(0)=1.  With A_n = sl^(n)(0) (EGF coefficients):
#   B_m = [EGF] sl^2 = sum_i C(m,i) A_i A_{m-i};  C_n = [EGF] sl^3 = sum_m C(n,m) B_m A_{n-m};  A_{n+2} = -2 C_n.
def lemniscate_A(N):
    A = [0] * (N + 1); B = [0] * (N + 1)
    A[1] = 1
    for n in range(0, N - 1):
        # B_n needs A_0..A_n (all known)
        if n % 4 == 2:
            B[n] = sum(math.comb(n, i) * A[i] * A[n - i] for i in range(1, n, 4))
        if n % 4 == 3:
            C = sum(math.comb(n, m) * B[m] * A[n - m] for m in range(2, n, 4))
            A[n + 2] = -2 * C
    return A

# ---------------------------------------------------------------- 2. naive theta kernel
# Theta(z)/T0 = sigma(u)^2 wp(u), u = varpi z / (2 pi), lattice g2=4, g3=0.
# r_k = T_{4k} / (T0 (varpi/pi)^{4k}) = (4k)! / 16^k * [u^{4k}] (sigma^2 wp).
def wp_coeffs(K, g2=Fr(4), g3=Fr(0)):
    c = {1: g2 / 20, 2: g3 / 28}
    for k in range(3, K + 1):
        c[k] = Fr(3, (2 * k + 3) * (k - 2)) * sum(c[m] * c[k - 1 - m] for m in range(1, k - 1))
    return c  # wp(u) = u^-2 + sum_k c_k u^{2k}

def series_exp(a, M):
    # a: list of coefficients a[0..M] with a[0] = 0; returns exp(a) coefficients up to M
    e = [Fr(0)] * (M + 1); e[0] = Fr(1)
    for n in range(1, M + 1):
        s = Fr(0)
        for k in range(1, n + 1):
            if a[k]:
                s += k * a[k] * e[n - k]
        e[n] = s / n
    return e

def theta_r(Kmax):
    M = 4 * Kmax  # need [u^M]
    c = wp_coeffs(M // 2 + 2)
    # u^2 wp(u) = 1 + sum_k c_k u^{2k+2}
    u2wp = [Fr(0)] * (M + 1); u2wp[0] = Fr(1)
    for k, ck in c.items():
        if 2 * k + 2 <= M:
            u2wp[2 * k + 2] = ck
    # sigma(u)^2 / u^2 = exp(-2 sum_k c_k u^{2k+2} / ((2k+1)(2k+2)))
    a = [Fr(0)] * (M + 1)
    for k, ck in c.items():
        if 2 * k + 2 <= M:
            a[2 * k + 2] = -2 * ck / ((2 * k + 1) * (2 * k + 2))
    s2 = series_exp(a, M)
    f = [sum(s2[i] * u2wp[n - i] for i in range(0, n + 1)) for n in range(M + 1)]
    r = {k: math.factorial(4 * k) * f[4 * k] / Fr(16) ** k for k in range(0, Kmax + 1)}
    return r, f

def main():
    out = []
    def say(*a):
        line = ' '.join(str(x) for x in a); print(line); out.append(line)

    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2001
    t0 = time.time()
    A = lemniscate_A(N)
    say(f'# Lemniscate: computed A_n for n <= {N} in {time.time()-t0:.1f}s')
    say('A1, A5, A9, A13, A17 =', A[1], A[5], A[9], A[13], A[17])
    say('A17 == 21224560896:', A[17] == 21224560896, '; nonzero only for n = 1 mod 4:',
        all(A[n] == 0 for n in range(N + 1) if n % 4 != 1))

    say('\n## Thm Le18: v_p(A_n) >= floor(n p/(p^2-1)) for inert p (p = 3 mod 4)')
    say('n | v3 floor(3n/8) | v7 floor(7n/48) | v11 floor(11n/120)')
    for n in [17, 49, 101, 201]:
        if n <= N:
            row = [str(n)]
            for p in (3, 7, 11):
                row.append(f'{vp(A[n], p)} {n * p // (p * p - 1)}')
            say(' | '.join(row))
    inert = [p for p in range(3, 200) if all(p % d for d in range(2, int(p ** 0.5) + 1)) and p % 4 == 3]
    viol = []; eq3 = 0; cnt3 = 0; maxex = (-1e9, None, None)
    for n in range(1, N + 1, 4):
        for p in inert:
            v = vp(A[n], p); pred = n * p // (p * p - 1)
            if v < pred:
                viol.append((n, p, v, pred))
            ex = v - n * p / (p * p - 1)
            if ex > maxex[0]:
                maxex = (ex, p, n)
        cnt3 += 1; eq3 += vp(A[n], 3) == n * 3 // 8
    say(f'violations for n <= {N}, inert p < 200: {len(viol)}', viol[:5])
    say(f'p = 3: equality v3 = floor(3n/8) for {eq3} of {cnt3} values of n')
    say(f'largest excess over np/(p^2-1): {maxex[0]:.3f} at p = {maxex[1]}, n = {maxex[2]}')

    say('\n## Split primes (p = 1 mod 4)')
    for p in (5, 13, 17, 29):
        say(f'p = {p} divides some A_n (n = 1 mod 4, n <= {N}):', any(A[n] % p == 0 for n in range(1, N + 1, 4)))
    say('157 | A_101:', A[101] % 157 == 0, ', v_157 =', vp(A[101], 157))
    say('A_{4k+1} = 3^k mod 5 for all k:', all((A[4 * k + 1] - pow(3, k, 5)) % 5 == 0 for k in range((N - 1) // 4 + 1)))
    split = [p for p in range(5, 2000) if all(p % d for d in range(2, int(p ** 0.5) + 1)) and p % 4 == 1]
    hits = sorted({p for p in split for n in range(1, N + 1, 4) if A[n] % p == 0})
    say(f'split primes p < 2000 dividing some A_n, n <= {N}:', hits)

    say('\n## Naive theta kernel over Z[i]')
    t0 = time.time()
    r, f = theta_r(30)
    say(f'(series to u^120 in {time.time()-t0:.1f}s)')
    say('r1..r5 =', [str(r[k]) for k in range(1, 6)], 'expected 1/4, 17/16, -111/64, 12513/256, -146079/1024')
    say('denominator of r_k divides 4^k for k <= 30:', all((4 ** k) % r[k].denominator == 0 for k in range(1, 31)))
    say('v_3(r_30) =', vpq(r[30], 3), '; prediction n*3/8 at n = 120 =', 120 * 3 / 8)
    say('v_3(r_k) vs floor(4k*3/8) for k = 1..30:')
    say('  ', [(4 * k, vpq(r[k], 3), 4 * k * 3 // 8) for k in range(1, 31)])
    say('v_7(r_k) vs floor(4k*7/48):', [(4 * k, vpq(r[k], 7), 4 * k * 7 // 48) for k in range(1, 31, 3)])

    # sizes: T_{4k} = r_k T0 (varpi/pi)^{4k}; T0 = sqrt(2) varpi / pi
    import mpmath as mp
    mp.mp.dps = 60
    varpi = 2 * mp.quad(lambda t: 1 / mp.sqrt(1 - t ** 4), [0, 1])
    T0 = mp.sqrt(2) * varpi / mp.pi
    say('varpi =', mp.nstr(varpi, 12), '; T0 =', mp.nstr(T0, 12))
    logT120 = mp.log(abs(mp.mpf(r[30].numerator) / r[30].denominator)) + mp.log(T0) + 120 * mp.log(varpi / mp.pi)
    say('log|T120| =', mp.nstr(logT120, 6), '; 0.5 log(120!/pi^120) =', mp.nstr(0.5 * (mp.log(mp.factorial(120)) - 120 * mp.log(mp.pi)), 6))

    # direct cross-check of the identity Theta/T0 = sigma^2 wp by brute-force lattice sums
    mp.mp.dps = 50
    def Tn(n, R=12):
        s = mp.mpf(0)
        for a in range(-R, R + 1):
            for b in range(-R, R + 1):
                lam = mp.mpc(a, b)
                s += lam ** n * mp.e ** (-mp.pi * (a * a + b * b))
        return s
    for k in (0, 1, 2, 3):
        direct = Tn(4 * k)
        via = mp.mpf(r[k].numerator) / r[k].denominator * T0 * (varpi / mp.pi) ** (4 * k)
        say(f'T_{4*k}: lattice sum {mp.nstr(direct.real, 15)}  vs  r_k formula {mp.nstr(via, 15)}')

    say('\n## Le13 (Hazewinkel form): arcsl(t) + (1/p) arcsl(t^(p^2)) is p-integral; with minus it is not')
    # arcsl(t) = sum_k kappa_k t^(4k+1)/(4k+1), kappa_k = C(2k,k)/4^k
    D = 4000
    arc = {4 * k + 1: Fr(math.comb(2 * k, k), 4 ** k) / (4 * k + 1) for k in range(0, (D - 1) // 4 + 1)}
    for p in (3, 7, 11):
        q = p * p
        for sign, name in ((1, '+'), (-1, '-')):
            bad = []
            for n in range(1, D + 1):
                cf = arc.get(n, Fr(0))
                if n % q == 0 and (n // q) in arc:
                    cf += sign * arc[n // q] / p
                if cf and vpq(cf, p) < 0:
                    bad.append(n)
            say(f'p = {p}, sign {name}: degrees <= {D} with negative p-valuation: {len(bad)}', bad[:4])

    with open('gap2_lemniscate_results.txt', 'w') as fh:
        fh.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()
