"""Numeric sanity check for Lemma Z (zero-map exclusion), doc section 10.3.

Lemma Z: for complex matrices C_u (u in W) whose columns all lie in a space of
dimension e,  (sum_u ||C_u||_F^2)^2 <= e * sum_{u,u'} ||C_u^H C_u'||_F^2.

Scalar consequence: if every C_u^H C_u is near the identity and the cross terms
obey the LinkS bound, the columns cannot fit in e <= delp * Dall dimensions
unless delp is close to 1.
"""
import numpy as np

rng = np.random.default_rng(0)


def lemma_z_trial(e, ranks, ambient):
    Q, _ = np.linalg.qr(rng.standard_normal((ambient, e)) + 1j * rng.standard_normal((ambient, e)))
    Cs = [Q @ (rng.standard_normal((e, d)) + 1j * rng.standard_normal((e, d))) for d in ranks]
    lhs = sum(np.linalg.norm(C, "fro") ** 2 for C in Cs) ** 2
    rhs = e * sum(np.linalg.norm(A.conj().T @ B, "fro") ** 2 for A in Cs for B in Cs)
    return lhs, rhs


worst = 0.0
for _ in range(2000):
    e = int(rng.integers(1, 8))
    ranks = [int(r) for r in rng.integers(1, 6, size=int(rng.integers(1, 6)))]
    lhs, rhs = lemma_z_trial(e, ranks, ambient=e + int(rng.integers(0, 6)))
    worst = max(worst, lhs / rhs)
print(f"Lemma Z: max lhs/rhs over 2000 random trials = {worst:.6f} (must be <= 1)")


def delp_lower_bound(e0, eta0, eta1, de, sg):
    """Smallest delp compatible with Bk = 0 on all words, from
    (1 - de - sqrt e0)^2 <= delp (1+eta1) [ (1+sqrt e0)^2 sg + 1 + eta0 ]."""
    s = np.sqrt(e0)
    return (1 - de - s) ** 2 / ((1 + eta1) * ((1 + s) ** 2 * sg + 1 + eta0))


for small in [0.25, 0.1, 1e-2, 1e-4]:
    print(f"all error parameters = {small:g}: Bk = 0 needs delp >= {delp_lower_bound(small**2, small, small, small, small):.4f}")
