# Concrete check of key_minor_dvd in A = Z[w]/(w^2 - p): elements are pairs (a, b) = a + b*w.
# Claim: if w^2 = p, u_b and u'_b are multiples of w for b != 0, and M[b][a]^(p^e) = N'[b][a] + p*T,
# then w divides (u'N')_c * (uM)_0^(p^e) - (u'N')_0 * (uM)_c^(p^e).
import random
def mul(x, y, p): return (x[0]*y[0] + p*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def sub(x, y): return (x[0]-y[0], x[1]-y[1])
def pw(x, n, p):
    r = (1, 0)
    for _ in range(n): r = mul(r, x, p)
    return r
def divisible_by_w(x, p): return x[0] % p == 0          # a + b w = w*(b + (a/p) w)  iff  p | a
def rnd(): return (random.randint(-5, 5), random.randint(-5, 5))
def trial(p, e, k, break_rule=None):
    W = (0, 1)
    n = k + 1
    u  = [rnd() if b == 0 else mul(W, rnd(), p) for b in range(n)]
    u2 = [rnd() if b == 0 else mul(W, rnd(), p) for b in range(n)]
    if break_rule == "u_not_divisible": u[1] = (1, 0)        # drop the w-divisibility of one entry
    M  = [[rnd() for a in range(n)] for b in range(n)]
    N2 = [[sub(pw(M[b][a], p**e, p), mul((p, 0), rnd(), p)) for a in range(n)] for b in range(n)]
    if break_rule == "no_frobenius": N2[0][0] = add(N2[0][0], (1, 0))   # break the Frobenius congruence
    def row(x, Q, a):
        s = (0, 0)
        for b in range(n): s = add(s, mul(x[b], Q[b][a], p))
        return s
    c = random.randrange(1, n)
    minor = sub(mul(row(u2, N2, c), pw(row(u, M, 0), p**e, p), p),
                mul(row(u2, N2, 0), pw(row(u, M, c), p**e, p), p))
    return divisible_by_w(minor, p)
random.seed(1)
for p, e in [(2, 1), (3, 1), (5, 1), (3, 2)]:
    ok = all(trial(p, e, 2) for _ in range(300))
    b1 = sum(not trial(p, e, 2, "u_not_divisible") for _ in range(300))
    b2 = sum(not trial(p, e, 2, "no_frobenius") for _ in range(300))
    print(f"p={p} e={e}: lemma holds in 300/300 random cases: {ok}; "
          f"fails when w-divisibility dropped: {b1}/300; fails when Frobenius congruence broken: {b2}/300")
