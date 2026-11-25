#!/usr/bin/env python3
"""
drop_one.py -- which hypotheses of the engine (Deduction.ch_top) are ESSENTIAL?   [COMPUTED]

Rule (pre-registered in DROP-ONE.md): a hypothesis is ESSENTIAL if numbers are found that satisfy all the
OTHER hypotheses but violate the conclusion; otherwise UNKNOWN (not shown redundant).

Model.  After `ch_top_main_eq` (which is where IdentU is used) the conclusion reads
        ASK(u) - Main(u)  <=  B_final := x^(CErr*eps) * errorBracketSizeWindows(...)        (ChTop.lean:37)
and the sharp intermediate bound proved by `each_unit_bound_statement` is  ASK - Main <= ErrX5at.
We test small instances of the abstract record `Data`:
    one translate u0, nw in {1,2} words over it (weights d = 1), m = 1, f = 1, |Top| = 1, |H| = 1,
    T2 = empty (nT2 = 0)   [all of these are allowed by the hypotheses; a counterexample on a small
    instance is a counterexample].
For fixed global constants and fixed HH, del, eta, e, uF the clauses of SizeData2 are LINEAR in the
remaining real unknowns (slopes, h, Ee, log T, log w, muCC, Fo, Ga, ASK, IO ...), so "is there an
instance with all other hypotheses true and ASK - Main > bound" is a linear program.  The solver is
scipy/HiGHS; every claimed counterexample is re-checked in mpmath (60 digits) with a stated margin.

Sanity check (must pass before any result is believed): with ALL hypotheses the LP maximum of ASK-Main
must not exceed ErrX5at, because Lean proves  ASK <= Main + ErrX5at.

IdentU (h1) is not tested numerically: it is the identification of the abstract record with the arithmetic
(gapA is defined from `ArithData`), and no other hypothesis mentions the arithmetic data, so a numeric
instance would have to exhibit an `ArithData`; that is not attempted (reported UNKNOWN, with this note).
"""
import json, sys, itertools
import numpy as np
from mpmath import mp, mpf
from scipy.optimize import linprog

mp.dps = 60
PI = mp.pi
EULER = mp.euler


# ---------------------------------------------------------------- linear expressions
class Lin(dict):
    """var -> coefficient; key None is the constant term."""
    def __add__(s, o):
        r = Lin(s)
        if isinstance(o, Lin):
            for k, v in o.items():
                r[k] = r.get(k, mpf(0)) + v
        else:
            r[None] = r.get(None, mpf(0)) + mpf(o)
        return r
    __radd__ = __add__
    def __neg__(s):
        return Lin({k: -v for k, v in s.items()})
    def __sub__(s, o):
        return s + (-o)
    def __rsub__(s, o):
        return (-s) + o
    def __mul__(s, c):
        return Lin({k: v * mpf(c) for k, v in s.items()})
    __rmul__ = __mul__


def V(name):
    return Lin({name: mpf(1)})


def lsum(xs):
    r = Lin()
    for x in xs:
        r = r + x
    return r


# ---------------------------------------------------------------- instances
def gen(x=800, eps=1, K='0.2', cHH='0.25', eK=1):
    """A consistent base instance for given x, eps, K, cHH, eK (all hypotheses meant to hold)."""
    x = mpf(x); eps = mpf(eps); K = mpf(K); cHH = mpf(cHH); eK = mpf(eK)
    xe = x ** eps
    P = dict(
        x=x, eps=eps, a=10 * x, b=mpf(1), bp=mpf(2), k=x, L=min(mpf(100), xe), La=min(mpf(100), xe),
        B0=min(mpf(100), xe), Nc=mpf(0), A=min(mpf(1000), 10 * x), Xpp=mpf(10),
        n=1, nT2=0, lg=mpf(1), logGam=mpf(1), LpL=mpf('0.3'), v=mpf(3), gam=EULER,
        delBar=mpf('0.5'), etaBar=mpf('0.1'), eBar=mpf('0.01'),
        K=K, eK=eK, cHH=cHH, eDiv=mpf(0), eLoss=mpf(0),
        cDiv=K, cE=K, cH=K, cCount=K, cSlope=K, cSl1=K, cLoss=K,
        dl=mpf('0.3'), eta=mpf('0.05'), e=mpf('0.005'),
        HH=min(mpf(2), x ** cHH / 2), uF0=mpf(50), nw=2, f0=False, dzero=False)
    return P


def upd(P, **kw):
    Q = dict(P)
    for k, v in kw.items():
        Q[k] = mpf(v) if isinstance(v, (int, float, str)) and not isinstance(v, bool) else v
    return Q


def Bfinal(P):
    x, eps = P['x'], P['eps']
    CErr = P['eDiv'] + P['eLoss'] + 3
    n = mpf(P['n']); nT2 = mpf(P['nT2']); k = P['k']; b = P['b']; a = P['a']
    br = a * (1 + 1 / k) + (2 * n * b * x ** eps + nT2 * k * b * x ** eps / (n * (n * x ** (-eps))))
    return x ** (CErr * eps) * br


def ErrX5at(P):
    """ErrX5at (QuotientSlopeBoundsWith.lean:45) with m = nT = 1."""
    x, eps, a, La, k, L, B0, Nc, A = (P[t] for t in 'x eps a La k L B0 Nc A'.split())
    cDiv, cE, cH, cCount, cSlope, cSl1, cLoss = (P[t] for t in 'cDiv cE cH cCount cSlope cSl1 cLoss'.split())
    LoP = cLoss * P['b'] * x ** (P['eLoss'] * eps)
    EDiv = cDiv * a * La + cDiv * (B0 + Nc) * x ** (P['eDiv'] * eps)
    MLo5 = cSl1 * LoP + cSl1 * (a / k + P['bp']) * (cCount * L) + cSl1 * P['Xpp'] + 1
    Vvar = 2 * cE * B0 + cH * (a * La + B0) + A * (cCount * mp.log(k))
    UBar5 = cSlope * a * La * (2 + 1 / k) + Vvar + cSl1 * B0 + MLo5
    return (A * (cCount * (La + La / k)) + EDiv + cE * B0 + cSlope * a * La * (1 + 1 / k)
            + mp.log(P['nw']) + LoP + MLo5
            + (1 / (1 - P['delBar'])) * (4 * mp.log(1 + x ** P['cHH']) * (UBar5 + P['b'])
                                         + (P['etaBar'] + 4 * mp.sqrt(P['eBar'])) * (x ** P['cHH'] * P['b'])))


def atoms(P):
    """Every conjunct of the hypotheses that mentions only global constants.  name -> bool.
    Prefix = hypothesis: Hida (HidaSetting), EW (ErrWindows), BN (BNBoundsU), LX (LargeX),
    FP (FParams), HHB (HHBound, constant parts)."""
    x, eps, a, b, bp, k, L, La, B0, Nc, A = (P[t] for t in 'x eps a b bp k L La B0 Nc A'.split())
    n = mpf(P['n']); nT2 = mpf(P['nT2'])
    K = P['K']; xe = x ** eps
    R = {}
    R['Hida.x>0'] = x > 0
    R['Hida.b>0'] = b > 0
    R['Hida.a>=0'] = a >= 0
    R['Hida.bp>=0'] = bp >= 0
    R['Hida.k>0'] = k > 0
    R['Hida.v>0'] = P['v'] > 0
    R['Hida.aT>=0'] = A >= 0
    R['Hida.cSl1>=0'] = P['cSl1'] >= 0
    R['Hida.delBar<1'] = P['delBar'] < 1
    R['Hida.etaBar>=0'] = P['etaBar'] >= 0
    R['Hida.eBar>=0'] = P['eBar'] >= 0
    R['Hida.eBar<=1/4'] = P['eBar'] <= mpf(1) / 4
    R['EW.x>=1'] = x >= 1
    R['EW.eps>0'] = eps > 0
    R['EW.eps<=1'] = eps <= 1
    R['EW.b>=1'] = b >= 1
    R['EW.xb<=a'] = x * b <= a
    R['EW.m<=x^(1/2+eps/2)'] = 1 <= x ** (mpf(1) / 2 + eps / 2)
    R['EW.xm<=k'] = x <= k
    R['EW.eK>=0'] = P['eK'] >= 0
    R['EW.k>=1'] = k >= 1
    R['EW.k<=x^eK'] = k <= x ** P['eK']
    R['EW.k<=a'] = k <= a
    R['EW.L>=0'] = L >= 0
    R['EW.L<=2x^eps'] = L <= 2 * xe
    R['EW.La>=0'] = La >= 0
    R['EW.La<=2x^eps'] = La <= 2 * xe
    R['EW.bp>=0'] = bp >= 0
    R['EW.k*bp<=a'] = k * bp <= a
    R['EW.Xpp>=0'] = P['Xpp'] >= 0
    R['EW.Xpp<=a'] = P['Xpp'] <= a
    R['EW.aT>=0'] = A >= 0
    R['EW.aT<=2a'] = A <= 2 * a
    R['EW.B0>=0'] = B0 >= 0
    R['EW.Nc>=0'] = Nc >= 0
    R['EW.log|W|<=(k-3)log2'] = mp.log(P['nw']) <= (k - 3) * mp.log(2)
    R['EW.delBar<=1/2'] = P['delBar'] <= mpf(1) / 2
    R['EW.etaBar>=0'] = P['etaBar'] >= 0
    R['EW.eBar>=0'] = P['eBar'] >= 0
    cs = [P[t] for t in 'cDiv cE cH cCount cSlope cSl1 cLoss'.split()]
    R['EW.ConstsBound'] = (all(0 <= c <= K for c in cs) and P['eDiv'] >= 0 and P['eLoss'] >= 0
                           and P['cHH'] >= 0)
    R['EW.etaterm'] = ((P['etaBar'] + 4 * mp.sqrt(P['eBar']) if P['eBar'] >= 0 else mpf(10) ** 9)
                       * (x ** P['cHH'] * b) <= K * xe * a)
    R['BN.B0'] = B0 <= 2 * n * b * xe
    R['BN.Nc'] = Nc <= nT2 * k * b * xe / (n * (n * x ** (-eps)))
    R['LX.log x<=x^eps'] = mp.log(x) <= xe if x > 0 else False
    R['LX.KBig<=x^eps'] = 200 * (1 + K) ** 2 * (1 + P['cHH']) * (1 + P['eK']) <= xe
    R['FP.del>=0'] = P['dl'] >= 0
    R['FP.del<=delBar'] = P['dl'] <= P['delBar']
    R['FP.eta>=0'] = P['eta'] >= 0
    R['FP.eta<=etaBar'] = P['eta'] <= P['etaBar']
    R['FP.e>=0'] = P['e'] >= 0
    R['FP.e<=eBar'] = P['e'] <= P['eBar']
    R['HHB.HH>0'] = P['HH'] > 0
    R['HHB.HH<=x^cHH*b'] = P['HH'] <= x ** P['cHH'] * b
    return R


# ---------------------------------------------------------------- the linear program
def build(P, dropr, istar, sib):
    """Rows (tag, Lin) meaning Lin <= 0; and the gap Lin = ASK - Main.
    dropr: set of row tags that are NOT enforced.  istar: which word attains max(muMaxN - h).
    sib: 'on' (SlopeIneq guard true, SlopeIneq row enforced) or 'off' (guard false, SlopeIneq vacuous)."""
    nw = int(P['nw']); A = P['A']; a = P['a']; La = P['La']; L = P['L']; k = P['k']
    B0 = P['B0']; Nc = P['Nc']; x = P['x']; eps = P['eps']
    cDiv, cE, cH, cCount, cSlope, cSl1, cLoss = (P[t] for t in 'cDiv cE cH cCount cSlope cSl1 cLoss'.split())
    rows = []

    def add(tag, lin):
        if tag not in dropr:
            rows.append((tag, lin))

    lw = V('lw'); muCC = V('muCC'); muMinCC = V('muMinCC'); Fo = V('Fo'); Ga = V('Ga')
    ASK = V('ASK'); IO = V('IO')
    muN = [V('muN%d' % i) for i in range(nw)]
    h = [V('h%d' % i) for i in range(nw)]
    muM = [V('muM%d' % i) for i in range(nw)]
    muMaxM = [V('muMaxM%d' % i) for i in range(nw)]
    Ee = [V('Ee%d' % i) for i in range(nw)]
    lT = [V('lT%d' % i) for i in range(nw)]
    s = Lin({None: mpf(0)}) if P['dzero'] else lsum([muN[i] - h[i] for i in range(nw)]) * (mpf(1) / nw)
    muMaxN = [V('muMaxN%d' % i) for i in range(nw)]
    uF0 = P['uF0']
    muMaxN[istar] = h[istar] + s + uF0                      # uF = max(muMaxN - h) - s = uF0
    for i in range(nw):
        if i != istar:
            add('uF.max', muMaxN[i] - h[i] - (muMaxN[istar] - h[istar]))
    logOm = P['gam'] + mp.log(PI / P['v']) - P['LpL']
    phA = A * mp.log(A) - A
    LoP = cLoss * P['b'] * x ** (P['eLoss'] * eps)
    f0 = P['f0']
    for i in range(nw):
        add('Hida.muN<=muMaxN', muN[i] - muMaxN[i])
        # DIV
        add('DIV', muCC + h[i] - Fo - ((phA - A * logOm) + (-A) * lT[i]
                                     + cDiv * a * La + cDiv * (B0 + Nc) * x ** (P['eDiv'] * eps)))
        # EComp5
        add('EComp.up', Ee[i] - A * P['lg'] - cE * B0)
        add('EComp.lo', A * P['lg'] - cE * B0 - Ee[i])
        # Count5
        if f0:
            lo = Lin({None: P['lg'] - cCount * (L + L / k)}) - lT[i]
        else:
            lo = lw + (mp.log(P['v']) - mp.log(PI)) + P['lg'] - cCount * (L + L / k) \
                - 2 * P['logGam'] / k - lT[i]
        add('Count.lo', lo)
        add('Count.hi', lT[i] - cCount * L)
        for j in range(nw):
            if j != i:
                add('Count.var', lT[i] - lT[j] - cCount * mp.log(k))
                add('HComp', (h[i] + A * lT[i]) - (h[j] + A * lT[j]) - cH * (a * La + B0))
        # Slopes
        add('Slopes.lo', Lin({None: -cSlope * a * La * (1 + 1 / k)}) - muM[i])
        add('Slopes.hi', muMaxM[i] - cSlope * a * La)
        # QuotientSlopeBoundsWith
        add('QSB.up', muMaxN[i] - muMaxM[i] - Ga - Fo + Ee[i] - cSl1 * B0)
        Lo5 = cSl1 * IO + lT[i] * (cSl1 * (a / k + P['bp'])) + (cSl1 * P['Xpp'] + 1)
        add('QSB.lo', muM[i] + Ga + Fo - Ee[i] - Lo5 - muN[i])
    # LossBounds
    add('Loss.ASK', ASK - Ga - LoP)
    add('Loss.IO', IO - LoP)
    # SlopeIneq with its guard
    HH, dl, eta, e = P['HH'], P['dl'], P['eta'], P['e']
    guard_const = (0 <= dl < 1) and eta >= 0 and (0 <= e <= mpf(1) / 4) and HH > 0
    guard = s - muMinCC - HH                                   # guard true  <=>  guard <= 0
    if 'SI' in dropr or not guard_const:
        add('HHB.guard', guard)                                # SI absent or vacuous
    else:
        if sib == 'on':
            add('HHB.guard', guard)
            uF = uF0
            term = 4 * uF * mp.log(abs(1 + HH / uF)) if (uF != 0 and 1 + HH / uF != 0) else mpf(0)
            Phi = (1 / (1 - dl)) * (term + (eta + 4 * mp.sqrt(e)) * HH)
            add('SI', s - mp.log(nw) - Phi - muCC)
        else:                                                  # guard false: need s - muMinCC > HH
            if 'HHB.guard' not in dropr:
                return None                                    # cannot be false when HHBound enforces it
            rows.append(('guard-off', Lin({None: HH + mpf('1e-6')}) - (s - muMinCC)))
    gap = ASK - (A * (mp.log(A) - 1 - P['gam'] + P['LpL']))
    if not f0:
        gap = gap + A * lw
    return rows, gap


def _arrays(rows, gap, margin):
    names = sorted({k for _, l in rows for k in l if k is not None} | {k for k in gap if k is not None})
    idx = {n: i for i, n in enumerate(names)}
    Aub = np.zeros((len(rows), len(names))); bub = np.zeros(len(rows))
    for r, (_, l) in enumerate(rows):
        sc = 1 + sum(abs(float(v)) for kk, v in l.items() if kk is not None)
        for kk, v in l.items():
            if kk is None:
                bub[r] = -float(v) - margin * sc
            else:
                Aub[r, idx[kk]] = float(v)
    g = np.zeros(len(names))
    for kk, v in gap.items():
        if kk is not None:
            g[idx[kk]] = float(v)
    return names, idx, Aub, bub, g


def maxgap(rows, gap):
    """('opt', value) / ('unbounded', inf) / ('infeasible', None)."""
    if not rows:
        return ('unbounded', float('inf'))
    names, idx, Aub, bub, g = _arrays(rows, gap, 0.0)
    if not (np.all(np.isfinite(Aub)) and np.all(np.isfinite(bub)) and np.all(np.isfinite(g))):
        return ('error-nonfinite', None)
    try:
        res = linprog(-g, A_ub=Aub, b_ub=bub, bounds=[(None, None)] * len(names), method='highs')
    except ValueError:
        return ('error-value', None)
    if res.status == 2:
        return ('infeasible', None)
    if res.status == 3:
        return ('unbounded', float('inf'))
    if res.status == 0:
        return ('opt', float(gap.get(None, 0)) + (-res.fun))
    return ('error%d' % res.status, None)


def certify(rows, gap, target):
    """Find a point with gap >= target satisfying every enforced row; re-check it in mpmath.
    Returns (ok, point, worst_residual, margin_used)."""
    for margin in (1e-6, 1e-4, 1e-2, 1.0):
        r2 = rows + [('target', Lin({None: mpf(target)}) - gap)]
        names, idx, Aub, bub, g = _arrays(r2, gap, margin)
        if not (np.all(np.isfinite(Aub)) and np.all(np.isfinite(bub)) and np.all(np.isfinite(g))):
            return False, None, None, None
        try:
            res = linprog(g, A_ub=Aub, b_ub=bub, bounds=[(None, None)] * len(names), method='highs')
        except ValueError:
            continue
        if res.status != 0:
            continue
        pt = {n: mpf(float(res.x[i])) for n, i in idx.items()}
        worst = mpf('-inf')
        for _, l in r2:
            val = sum((v * pt[kk] if kk is not None else v) for kk, v in l.items())
            worst = max(worst, val)
        if worst <= 0:
            return True, pt, worst, margin
    return False, None, None, None


def evalgap(gap, pt):
    return sum((v * pt[kk] if kk is not None else v) for kk, v in gap.items())


# ---------------------------------------------------------------- the search
FACT = [mpf(10) ** j for j in range(-8, 9) if j != 0]
SIGNED = FACT + [mpf(0), mpf(-1), mpf(-10), mpf(-1000)]
UF = [mpf('0.5'), mpf(5), mpf(50), mpf(500)]
UFNEG = [mpf('-0.5'), mpf(-5), mpf(-50), mpf(-500)]


def lp_variants(P, dropr, ufs, hhs):
    """yield (descr, rows, gap) for the small structural choices."""
    for nw in (1, 2):
        for uF0 in ufs:
            for HH in hhs:
                Q = dict(P); Q['nw'] = nw; Q['uF0'] = uF0; Q['HH'] = HH
                for istar in range(nw):
                    for sib in ('on', 'off'):
                        r = build(Q, dropr, istar, sib)
                        if r is None:
                            continue
                        yield (dict(nw=nw, uF0=uF0, HH=HH, istar=istar, SI=sib), Q) + r


def search(P0, dropr, dropa, muts, ufs=UF, extra_variants=(), budget=None):
    """Try the base instance and each mutated instance.  Return the best finding."""
    best = None
    cands = [('base', P0)]
    for desc, upd_ in muts:
        cands.append((desc, upd_))
    for desc, P in cands:
        try:
            fail = [n for n, ok in atoms(P).items() if not ok and n not in dropa]
        except (ZeroDivisionError, ValueError, TypeError):
            continue
        if fail:
            continue
        hhs = [P['HH']]
        for var in (list(extra_variants) or [{}]):
            Pv = dict(P); Pv.update(var)
            try:
                variants_ = list(lp_variants(Pv, dropr, (ufs + (UFNEG if 'Hida.muN<=muMaxN' in dropr else [])), hhs))
            except (ZeroDivisionError, ValueError, TypeError):
                continue
            for vdesc, Q, rows, gap in variants_:
                st, val = maxgap(rows, gap)
                if st == 'infeasible' or st.startswith('error'):
                    continue
                try:
                    B = Bfinal(Q); E = ErrX5at(Q)
                except (ZeroDivisionError, ValueError, TypeError):
                    continue
                if B <= 0 or E <= 0:
                    continue
                ratioB = (mpf('inf') if st == 'unbounded' else mpf(val) / B)
                ratioE = (mpf('inf') if st == 'unbounded' else mpf(val) / E)
                key = (ratioB, ratioE)
                rec = dict(inst=desc, var=dict(vdesc, **{k: v for k, v in var.items()}), status=st,
                           gapmax=val, B=B, E=E, ratioB=ratioB, ratioE=ratioE, P=Q, rows=rows, gap=gap)
                if best is None or key > (best['ratioB'], best['ratioE']):
                    best = rec
                if ratioB > 1:
                    return best
    return best


def finalize(best):
    """Turn a best record into a verdict string and, when ESSENTIAL, a verified certificate."""
    if best is None:
        return dict(verdict='UNKNOWN', note='no feasible instance found with the other hypotheses true')
    out = dict(best_ratio_to_Bfinal=str(mp.nstr(best['ratioB'], 6)),
               best_ratio_to_ErrX5at=str(mp.nstr(best['ratioE'], 6)),
               status=best['status'], where=best['inst'],
               structure={k: str(v) for k, v in best['var'].items()})
    if best['ratioB'] > 1:
        target = 2 * best['B'] + 1 if best['status'] == 'unbounded' else (best['B'] * mpf('1.0001'))
        target = max(target, mpf(1)) if best['status'] == 'unbounded' else target
        ok, pt, worst, margin = certify(best['rows'], best['gap'], target)
        out['verdict'] = 'ESSENTIAL' if ok else 'UNKNOWN'
        out['certificate_verified'] = bool(ok)
        if ok:
            P = best['P']
            out['counterexample'] = dict(
                gap=str(mp.nstr(evalgap(best['gap'], pt), 12)), B_final=str(mp.nstr(best['B'], 12)),
                ErrX5at=str(mp.nstr(best['E'], 12)), worst_row_residual=str(mp.nstr(worst, 6)),
                margin_used=margin,
                globals={k: str(mp.nstr(v, 10)) if isinstance(v, mpf) else str(v)
                         for k, v in P.items() if k not in ('gam',)},
                unknowns={k: str(mp.nstr(v, 14)) for k, v in sorted(pt.items())})
        else:
            out['note'] = 'LP says gap can exceed B_final but the exact re-check did not pass; not claimed'
    else:
        out['verdict'] = 'UNKNOWN'
        if best['ratioE'] > 1:
            out['note'] = ('violates the sharp bound ErrX5at but not the (much larger) conclusion bound '
                           'B_final; not claimed ESSENTIAL for ch_top')
    return out


def mut_single(P, params, factors=FACT):
    r = []
    for p in params:
        for f in factors:
            r.append(('%s*%s' % (p, mp.nstr(f, 3)), upd(P, **{p: P[p] * f})))
    return r


def mut_abs(P, p, values):
    return [('%s=%s' % (p, mp.nstr(v, 3)), upd(P, **{p: v})) for v in values]


def main():
    P0 = gen()
    results = {}
    # ---- sanity checks -----------------------------------------------------------------------
    fails = [n for n, ok in atoms(P0).items() if not ok]
    print('base instance: failing global atoms =', fails)
    print('B_final(base) = %s,  ErrX5at(base) = %s' % (mp.nstr(Bfinal(P0), 8), mp.nstr(ErrX5at(P0), 8)))
    sane = []
    for vdesc, Q, rows, gap in lp_variants(P0, set(), UF, [P0['HH']]):
        st, val = maxgap(rows, gap)
        sane.append((vdesc, st, val, ErrX5at(Q)))
        if st == 'opt':
            print('  all hypotheses, %s: max(ASK-Main) = %.6g  <=  ErrX5at = %s ? %s' % (
                vdesc, val, mp.nstr(ErrX5at(Q), 8), val <= float(ErrX5at(Q)) * (1 + 1e-9) + 1e-6))
        else:
            print('  all hypotheses, %s: %s' % (vdesc, st))
    bad = [s for s in sane if s[1] == 'unbounded' or (s[1] == 'opt' and s[2] > float(s[3]) * (1 + 1e-9) + 1e-6)]
    if bad:
        print('SANITY CHECK FAILED: model is wrong or the base instance is inconsistent'); sys.exit(2)
    feas = [s for s in sane if s[1] == 'opt']
    if not feas:
        print('SANITY: no feasible instance with all hypotheses; base instance is bad'); sys.exit(2)
    print('SANITY OK: %d feasible variants, none above ErrX5at' % len(feas))
    results['_sanity'] = dict(variants=len(sane), feasible=len(feas),
                              worst_ratio_to_ErrX5at=max(s[2] / float(s[3]) for s in feas))

    # ---- targets: (name, dropped row tags, dropped atoms, mutated candidate instances) ----------
    T = []

    def rowt(name, tags, **kw):
        T.append(dict(name=name, dropr=set(tags), dropa=set(), muts=[], **kw))

    def atomt(name, atomnames, params, factors=FACT, base=None):
        b0 = base or P0
        T.append(dict(name=name, dropr=set(), dropa=set(atomnames), muts=mut_single(b0, params, factors)))

    # h2 clause 2..11 (rows) --------------------------------------------------------------
    rowt('h2.2 DIV', ['DIV'])
    rowt('h2.3 EComp5 (both sides)', ['EComp.up', 'EComp.lo'])
    rowt('h2.3a EComp5 upper', ['EComp.up'])
    rowt('h2.3b EComp5 lower', ['EComp.lo'])
    rowt('h2.4 HComp', ['HComp'])
    rowt('h2.5 Count5 (all three)', ['Count.lo', 'Count.hi', 'Count.var'])
    rowt('h2.5a Count5 lower bound on log T', ['Count.lo'])
    rowt('h2.5b Count5 log T <= cCount m L', ['Count.hi'])
    rowt('h2.5c Count5 |log T - log T\'|', ['Count.var'])
    rowt('h2.6 Slopes (both)', ['Slopes.lo', 'Slopes.hi'])
    rowt('h2.6a Slopes lower: -SL <= muM', ['Slopes.lo'])
    rowt('h2.6b Slopes upper: muMaxM <= SL', ['Slopes.hi'])
    rowt('h2.7 QuotientSlopeBoundsWith (both)', ['QSB.up', 'QSB.lo'])
    rowt('h2.7a QSB upper (muMaxN <= ...)', ['QSB.up'])
    rowt('h2.7b QSB lower (G): muM+Ga+Fo-Ee-Lo5 <= muN', ['QSB.lo'])
    rowt('h2.8 LossBounds (both)', ['Loss.ASK', 'Loss.IO'])
    rowt('h2.8a LossBounds ASK-Ga <= LoP', ['Loss.ASK'])
    rowt('h2.8b LossBounds IO <= LoP', ['Loss.IO'])
    rowt('h2.9 SlopeIneq (SI)', ['SI'])
    rowt('h2.10c HHBound: s - muMinCC <= HH', ['HHB.guard'])
    # clause 1 pieces that are not repeated in ErrWindows ---------------------------------
    rowt('h2.1 Hida: muN <= muMaxN', ['Hida.muN<=muMaxN'])
    # the variants need special flags; handled below
    for t in T:
        pass
    # atoms ---------------------------------------------------------------------------------
    atomt('h2.1 Hida: 0<x', ['Hida.x>0'], ['x'], SIGNED)
    atomt('h2.1 Hida: 0<b', ['Hida.b>0'], ['b'], SIGNED)
    atomt('h2.1 Hida: 0<=a', ['Hida.a>=0'], ['a'], SIGNED)
    atomt('h2.1 Hida: 0<=b\'', ['Hida.bp>=0'], ['bp'], SIGNED)
    atomt('h2.1 Hida: 0<k', ['Hida.k>0'], ['k'], SIGNED)
    atomt('h2.1 Hida: 0<v', ['Hida.v>0'], ['v'], SIGNED)
    atomt('h2.1 Hida: 0<=aT', ['Hida.aT>=0'], ['A'], SIGNED)
    atomt('h2.1 Hida: 0<=cSl1', ['Hida.cSl1>=0'], ['cSl1'], SIGNED)
    atomt('h2.1 Hida: delBar<1', ['Hida.delBar<1'], ['delBar'], [mpf(2), mpf(10), mpf(100)])
    atomt('h2.1 Hida: 0<=etaBar', ['Hida.etaBar>=0'], ['etaBar'], SIGNED)
    atomt('h2.1 Hida: 0<=eBar', ['Hida.eBar>=0'], ['eBar'], SIGNED)
    atomt('h2.1 Hida: eBar<=1/4', ['Hida.eBar<=1/4'], ['eBar'], [mpf(10), mpf(100), mpf(1000)])
    # FParams
    atomt('h2.11a FParams: 0<=del', ['FP.del>=0'], ['dl'], SIGNED)
    atomt('h2.11b FParams: del<=delBar', ['FP.del<=delBar'], ['dl'], [mpf(2), mpf(2.9), mpf(3)])
    atomt('h2.11c FParams: 0<=eta', ['FP.eta>=0'], ['eta'], SIGNED)
    atomt('h2.11d FParams: eta<=etaBar', ['FP.eta<=etaBar'], ['eta'], FACT)
    atomt('h2.11e FParams: 0<=e', ['FP.e>=0'], ['e'], SIGNED)
    atomt('h2.11f FParams: e<=eBar', ['FP.e<=eBar'], ['e'], FACT)
    # HHBound constants
    atomt('h2.10a HHBound: 0<HH', ['HHB.HH>0'], ['HH'], SIGNED)
    atomt('h2.10b HHBound: HH<=x^cHH*b', ['HHB.HH<=x^cHH*b'], ['HH'], FACT)
    # h3 ErrWindows, one atom at a time
    ew = {
        'EW.x>=1': ['x'], 'EW.eps>0': ['eps'], 'EW.eps<=1': ['eps'], 'EW.b>=1': ['b'], 'EW.xb<=a': ['a', 'b', 'x'],
        'EW.xm<=k': ['k', 'x'], 'EW.eK>=0': ['eK'], 'EW.k>=1': ['k'], 'EW.k<=x^eK': ['k', 'eK'], 'EW.k<=a': ['k', 'a'],
        'EW.L>=0': ['L'], 'EW.L<=2x^eps': ['L'], 'EW.La>=0': ['La'], 'EW.La<=2x^eps': ['La'],
        'EW.bp>=0': ['bp'], 'EW.k*bp<=a': ['bp', 'k', 'a'], 'EW.Xpp>=0': ['Xpp'], 'EW.Xpp<=a': ['Xpp'],
        'EW.aT>=0': ['A'], 'EW.aT<=2a': ['A'], 'EW.B0>=0': ['B0'], 'EW.Nc>=0': ['Nc'],
        'EW.log|W|<=(k-3)log2': ['k'], 'EW.delBar<=1/2': ['delBar'], 'EW.etaBar>=0': ['etaBar'],
        'EW.eBar>=0': ['eBar'],
        'EW.ConstsBound': ['cDiv', 'cE', 'cH', 'cCount', 'cSlope', 'cSl1', 'cLoss', 'eDiv', 'eLoss', 'cHH'],
        'EW.etaterm': ['etaBar', 'eBar'],
    }
    for an, ps in ew.items():
        atomt('h3 ' + an, [an], ps, SIGNED if ('>=' in an or '>' in an or 'Consts' in an) else FACT)
    atomt('h4a BN.B0', ['BN.B0'], ['B0'], [mpf(10) ** j for j in range(1, 17)])
    T.append(dict(name='h4b BN.Nc', dropr=set(), dropa={'BN.Nc'}, muts=mut_abs(P0, 'Nc', [mpf(10) ** j for j in range(1, 17)])))
    # h5 LargeX: re-generate consistent instances at smaller x / eps (K is irrelevant to the LP)
    lx = []
    for xv in (2, 5, 10, 30, 100, 300, 600):
        for ev in (1, mpf('0.5'), mpf('0.1'), mpf('0.02')):
            for Kv in ('0.2', '5', '100'):
                lx.append(('x=%s,eps=%s,K=%s' % (xv, ev, Kv), gen(x=xv, eps=ev, K=Kv)))
    T.append(dict(name='h5a LargeX: log x <= x^eps', dropr=set(), dropa={'LX.log x<=x^eps'}, muts=lx))
    T.append(dict(name='h5b LargeX: KBig <= x^eps', dropr=set(), dropa={'LX.KBig<=x^eps'}, muts=lx))
    # whole-unit drops for the global hypotheses
    allEW = {k for k in atoms(P0) if k.startswith('EW.')}
    allBN = {k for k in atoms(P0) if k.startswith('BN.')}
    allLX = {k for k in atoms(P0) if k.startswith('LX.')}
    allH = {k for k in atoms(P0) if k.startswith('Hida.')}
    allFP = {k for k in atoms(P0) if k.startswith('FP.')}
    allHHB = {k for k in atoms(P0) if k.startswith('HHB.')}
    ewp = sorted({p for ps in ew.values() for p in ps})
    allmuts = mut_single(P0, ewp, FACT) + lx
    T.append(dict(name='h3 ErrWindows (whole)', dropr=set(), dropa=allEW, muts=allmuts))
    T.append(dict(name='h4 BNBoundsU (whole)', dropr=set(), dropa=allBN, muts=mut_single(P0, ['B0'], [mpf(10) ** j for j in range(1, 17)])
                  + mut_abs(P0, 'Nc', [mpf(10) ** j for j in range(1, 17)])))
    T.append(dict(name='h5 LargeX (whole)', dropr=set(), dropa=allLX, muts=lx))
    T.append(dict(name='h2.1 HidaSetting (whole)', dropr={'Hida.muN<=muMaxN'}, dropa=allH,
                  muts=mut_single(P0, ['x', 'b', 'a', 'bp', 'k', 'v', 'A', 'cSl1', 'delBar', 'etaBar', 'eBar'], SIGNED),
                  variants=[{}, {'f0': True}, {'dzero': True}, {'f0': True, 'dzero': True}]))
    T.append(dict(name='h2.11 FParams (whole)', dropr=set(), dropa=allFP,
                  muts=mut_single(P0, ['dl', 'eta', 'e'], SIGNED)))
    T.append(dict(name='h2.10 HHBound (whole)', dropr={'HHB.guard'}, dropa=allHHB,
                  muts=mut_single(P0, ['HH'], SIGNED)))
    # special-variant atoms of HidaSetting that are not real constants
    T.append(dict(name='h2.1 Hida: 0<f  (f=0 allowed: 1/f = 0 in Lean)', dropr=set(), dropa=set(), muts=[],
                  variants=[{'f0': True}]))
    T.append(dict(name='h2.1 Hida: 0<d  (d=0: wmean = 0/0 = 0)', dropr=set(), dropa=set(), muts=[],
                  variants=[{'dzero': True}]))

    for t in T:
        variants = t.get('variants')
        best = search(P0, t['dropr'], t['dropa'], t['muts'], extra_variants=variants or ())
        results[t['name']] = finalize(best)
        r = results[t['name']]
        print('%-58s %-9s  ratio(B_final)=%-10s ratio(ErrX5at)=%-10s %s' % (
            t['name'], r['verdict'], r.get('best_ratio_to_Bfinal', '-'), r.get('best_ratio_to_ErrX5at', '-'),
            r.get('note', '')))
        sys.stdout.flush()

    # not tested --------------------------------------------------------------------------
    for nm, why in [
        ('h1 IdentU', 'not tested numerically: identifies the abstract record with the arithmetic (needs an ArithData); '
                      'no other hypothesis mentions the arithmetic data'),
        ('h2.1 Hida: 0<w, 0<T', 'not tested: only logs of w and T occur and Real.log |.| already reaches every real value, '
                                 'so a negative w or T gives nothing new in this model'),
        ('h3 nT>=1, m<=x^(1/2+eps/2)', 'not tested: the model fixes |Top| = 1 and m = 1'),
    ]:
        results[nm] = dict(verdict='UNKNOWN', note=why)
        print('%-58s UNKNOWN    %s' % (nm, why))

    def tojson(o):
        if isinstance(o, (mpf,)):
            return str(o)
        return str(o)
    with open('drop_one_results.json', 'w') as fh:
        json.dump(results, fh, indent=1, default=tojson)
    print('wrote drop_one_results.json')


if __name__ == '__main__':
    main()
