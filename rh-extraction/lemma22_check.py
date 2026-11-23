import sympy as sp
# Symbolic check of Lemma 2.2 for |T| = 3 tops, m = 2 pieces, f = 3 slots.
m, f = 2, 3
a = sp.symbols('a0:3', positive=True)
w = [[sp.Symbol(f'w{j}{r}', positive=True) for r in range(f)] for j in range(m)]
v, ell, g, kc = sp.symbols('v ell g kappa_c', positive=True)
gam, pi = sp.EulerGamma, sp.pi
A = sum(a)
ph = lambda y: y*sp.log(y) - y
logOm = gam + sp.log(pi/v) - ell
Lam0 = sum(sp.Rational(1, f)*sum(sp.log(w[j][r]*v/pi) for r in range(f)) for j in range(m)) + m*g - kc
Main = sum(sum(at*(sp.log(at) - 1 - gam + ell - sp.Rational(1, f)*sum(sp.log(w[j][r]) for r in range(f))) for at in a) for j in range(m))
lhs = sum(m*(ph(at) - at*logOm) for at in a) - A*Lam0 + m*A*g
print('Lemma 2.2 residual:', sp.simplify(sp.expand_log(lhs - (Main + A*kc), force=True)))
