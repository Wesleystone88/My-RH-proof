"""Extended why-p test (T2 of prompts/claude-code-prompt-2026-11-25d.md).
Run via:  python why_p.py --extended      (appends to why_p_extended_results.txt; pre-registration is at its top).
Same series as why_p.py, degrees up to NX = 600, primes 3,7,11,19 (comparison) and 23,31,43,47 (new).
Exact fractions.  Numerical, not a proof."""
import math, sys, time
from fractions import Fraction as Fr
from gap2_lemniscate_check import wp_coeffs, series_exp, vpq

NX = 600
PRIMES_X = (3, 7, 11, 19, 23, 31, 43, 47)
OUT = 'why_p_extended_results.txt'


def mul(a, b, M):
    c = [Fr(0)] * (M + 1)
    for i in range(M + 1):
        if a[i]:
            for j in range(M + 1 - i):
                if b[j]:
                    c[i + j] += a[i] * b[j]
    return c


def run():
    t0 = time.time()
    lines = []

    def log(s):
        print(s); sys.stdout.flush(); lines.append(s)
        with open(OUT, 'a') as fh:
            fh.write(s + '\n')

    c = wp_coeffs(NX // 2 + 2)
    L = [Fr(0)] * (NX + 1); u2wp = [Fr(0)] * (NX + 1); u2wp[0] = Fr(1)
    for k, ck in c.items():
        if 2 * k + 2 <= NX:
            L[2 * k + 2] = -ck / ((2 * k + 1) * (2 * k + 2)); u2wp[2 * k + 2] = ck
    F = mul(series_exp([2 * x for x in L], NX), u2wp, NX)
    log('series built in %.0f s; n up to %d' % (time.time() - t0, NX))
    ns = [m for m in range(4, NX + 1, 4) if F[m] != 0]
    nmax = max(ns)
    fails = []
    log('%3s | %-26s | %-34s | %-s' % ('p', '(1) dev of naive v_p(n! r) from n/(p^2-1): [min,max]',
                                       'largest n: naive / removed / full rate', '(2) gap closed'))
    for p in PRIMES_X:
        q = p * p - 1
        devs = [vpq(math.factorial(n) * F[n], p) - Fr(n, q) for n in ns]
        lo, hi = float(min(devs)), float(max(devs))
        ok1 = (lo >= -2 and hi <= 2)
        Lc = L[:]; Lc[p + 1] = Fr(0)
        Fc = mul(series_exp([2 * x for x in Lc], NX), u2wp, NX)
        vn = vpq(math.factorial(nmax) * F[nmax], p); vr = vpq(math.factorial(nmax) * Fc[nmax], p)
        full = Fr(nmax * p, q)
        frac = float((vr - vn) / (full - vn)) if full != vn else float('nan')
        ok2 = True if p < 7 else (frac >= 0.8)
        note2 = ('n/a (p<7)' if p < 7 else ('%.3f %s' % (frac, 'ok' if ok2 else 'FAIL')))
        if p < 7:
            note2 += ' [for the record: %.3f]' % frac
        log('%3d | [%+6.2f, %+6.2f] %-6s | n=%d: %d / %d / %.1f | %s' % (
            p, lo, hi, 'ok' if ok1 else 'FAIL', nmax, vn, vr, float(full), note2))
        if not ok1: fails.append((p, 'rate'))
        if not ok2: fails.append((p, 'gap closed'))
        log('      (elapsed %.0f s)' % (time.time() - t0))
    log('')
    log('VERDICT: ' + ('PASS' if not fails else 'FAIL, failing: ' + ', '.join('p=%d (%s)' % f for f in fails)))
