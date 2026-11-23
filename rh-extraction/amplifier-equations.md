# The theta-lift amplifier

**DERIVED.** The scalar test is (8). Its left side contains the density of thick translates, the number of top indices, the lift count and the common weight. It bounds a signed, smoothed prime sum on the scales for which the geometric and character hypotheses hold. Source keys refer to [the pinned declarations](amplifier-sources.md). The [variable table](amplifier-variables.md) gives the inputs and their admissible ranges.

**1. The degree rule. READ [S1–S3].** For every word \(v\) of one admissible geometric record,
\[
 \mu_{\rm Dual}+h(v)-F_o\ \le\
 M_{\rm geom}(v)+C_D n_T aL_a+C_Dm(B_0+N_c)x^{C_{\rm abs}\varepsilon}. \tag{1}
\]
The sign, parentheses and power match lines 82–84. The constant in both terms is the same. The other eight clauses of the predicate are given in [the audit](amplifier-audit.md). In particular,
\[
 M_{\rm geom}(v)=\sum_{t\in TT}\{m[a_t\log a_t-a_t-a_t\log\Omega]-a_t\log T(v)\},
 \qquad F_o=\sum_{j=1}^{m}\sum_{p\in{\rm supp}}\mathrm{sz}_p(F_{jp}). \tag{2}
\]
Only the bracket in the summand has the explicit multiplier \(m\). The slope transfer uses (1) as its DIV premise.

**2. From degrees to a pointwise arithmetic cost. READ [S8–S11].** For \(z\in A_0\), take a preimage under the base map \({\rm tr}\). Write \(w_j=w(z,j,\cdot)\), \(f=|\Phi|\), \(\gamma\) for Euler's constant and \(\chi_C\) for the first sign character. With \([s]_+=\max(s,0)\), put \(P(g)= [a_t/p^i-w_j({\rm partner}(t,g))]_+\) inside a sum indexed by \(p,i,t,j\). The cost for one lift is
\[
 \begin{aligned}
 A_{tj}&=2\sum_{\substack{p\le N\\p\ {\rm inert}}}\log p
       \sum_{\substack{1\le i\le N\\i{\rm Fr}_p\notin\Phi}}P(i{\rm Fr}_p)
       +(\log d)\sum_{i=1}^N\ \sum_{g\in(i{\rm Fr}_d+I_d)\setminus\Phi}P(g)\big|_{p=d},\\
 M_{tj}&=a_t\big(\log a_t-1-\gamma+\ell(\chi_C)-f^{-1}\textstyle\sum_{\rho\in\Phi}\log w_j(\rho)\big),\\
 \Delta(z)&=\sum_{t\in TT}\sum_{j=1}^m(A_{tj}-\Re M_{tj})
     \ \le\ {\rm ErrX5at}({\rm tr}^{-1}z)\ \le\ x^{C_{\rm err}\varepsilon}{\rm ErrText}
     \ \le\ x^{C_*\varepsilon}B .
 \end{aligned}\tag{3}
\]
Here \({\rm tr}^{-1}z\) denotes any chosen preimage. The first inequality uses the eleven ledger hypotheses, including DIV. The second uses the strong trace window and large-\(x\) conditions. The last uses the two budget bounds and \(C_{\rm err}=e_{\rm Div}+e_{\rm Loss}+3\le C_* = e_D+e_L+3\). All addends of the pointwise error are expanded in the variable table. In particular,
\[
 {\rm ErrText}=n_Ta_E(1+m^2/k)+m(B_0+N_c),\qquad
 B=n_Ta_E(1+m^2/k)+2n m^2 b x^\varepsilon+
             m n_2 k b x^{2\varepsilon}/n^2 . \tag{4}
\]

**3. What is amplified. READ [S7, S12, S14].** Denote the von Mangoldt function by \(\Lambda_{\rm vM}\) and the fixed character level by \(\mathcal L\). At \(y\ge1\) set
\[
 \begin{aligned}
 Z(y)&=\sum_{r\le y}\Lambda_{\rm vM}(r)(y/r-1)-y\log y+(1+\gamma)y,\\
 g_\chi(y)&=\sum_{1\le r\le y}\Lambda_{\rm vM}(r)\chi(r)(y/r-1)+y(L'/L)(1,\chi)\quad(\chi\ne1),\\
 E_{\mathcal L}(y)&=Z(y)+\sum_{\psi\in{\rm KEPT}\setminus\{1\}}
             \omega_\psi\,\Re g_{\psi.\chi}(y)=G_m^A(y),\\
 G(y)&=E_{\mathcal L}(y)-\Sigma(y),\qquad
 \Sigma(y)=\sum_{\psi\in\Psi_A\setminus K_p}|G_\psi(y)|.
 \end{aligned}\tag{5}
\]
Sums over integers begin at 1. The principal character uses \(Z\). The distinguished optional character has weight 1, all other nonprincipal kept characters have weight \(c=(3o+1)^{-1}\). The last equality on the third line uses host compatibility. With no nonprincipal kept characters the observable is \(Z\). The statement is one-sided.

**4. The factor \(m\). READ [S12–S13].** Write \(e_1(t)=((1,0),t)\), \(y_t=a_t/b\), \(X=x^{1/2+\varepsilon}\), \(Q=n_Tmb\), \(\delta=n_2/n\). The character comparison and the exact thick-translate average are
\[
 \begin{aligned}
 n_T(G(x)-4X)&\le S_\psi:=\sum_{t\in TT}\Re\sum_{\psi\in\Psi_A}
               \psi(e_1(t))G_\psi(y_t),\\
 \sum_{z\in A_0,t\in TT,j}\Re{\rm Th}(z,t,y_t)
        &=|A_0|\,m b(\delta/2)S_\psi,\\
 {\rm Th}(z,t,y)&= f^{-1}\sum_{s\in T_2}\sum_\psi
                  \psi(-e_1(s+z-t))\,bG_\psi(y).
 \end{aligned}\tag{6}
\]
The thick contribution repeats for every \(j\). The replacement by \({\rm Th}\) costs at most
\[
 2f[3(x+1)(\eta+1)+(x+1)b\theta]\le 2b/x
 \quad\text{per top and lift}. \tag{7}
\]
Summing the upper bounds (3) over the same base and cancelling \(|A_0|>0\) yields the unsimplified scalar inequality
\[
 \boxed{\quad Q\,{\delta\over2}
   [E_{\mathcal L}(x)-\Sigma(x)-4x^{1/2+\varepsilon}]
   \le x^{C_*\varepsilon}
   [n_Ta_E+n_Ta_E m^2/k+2nm^2b x^\varepsilon
          +m n_2 k b x^{2\varepsilon}/n^2]+2Q/x .\quad} \tag{8}
\]
The base average creates the density factor. The top bound is paid once per base after summing over all its top indices and lifts. Counting it again for every \(j\) would lose the amplification.

**5. Scalar verification. DERIVED [S9, S13–S14].** On the stated windows \(Q,\delta>0\). The following four bounds are in the order of the four bracket terms in (8), after division by \(Q\):
\[
 \frac{B}{Q}=\frac{a_E}{mb}+\frac{a_E m}{kb}
  +2\frac n{n_T}m x^\varepsilon+\frac{n_2}{n_T}\frac{k}{n^2}x^{2\varepsilon}
 \ \le\ \frac{2x}{m}+2+4m x^{9\varepsilon/8}
                +2x^{1/2+9\varepsilon/8}
 \ \le\ 10x^{1/2+13\varepsilon/8}. \tag{9}
\]
Use \(a_E\le2xb,\ xm\le k,\ n/n_T\le2x^{\varepsilon/8},\ n_2\le n,\ k/n^2\le x^{1/2-\varepsilon}\) and the lower and upper bounds for \(m\) in the variable table. With \(\delta\ge x^{-\varepsilon}\), \(x\ge3\), \(C_*\ge0\), (8) gives
\[
 G(x)\le 26x^{1/2+(C_*+21/8)\varepsilon}
 \le x^{1/2+(C_*+3)\varepsilon}\qquad(26\le x^{3\varepsilon/8}). \tag{10}
\]
This works throughout the simultaneous scalar windows. No minimization step is needed.

**6. Restore the omitted characters. READ / DERIVED [S4, S14–S15].** At a host satisfying the independent pointwise character premise,
\[
 \Sigma(x)\le4o\,x^{1/2+\varepsilon},\qquad
 E_{\mathcal L}(x)\le x^{1/2+(e_D+e_L+7)\varepsilon}
                 = x^{1/2+9\varepsilon}\quad((e_D,e_L)=(2,0)). \tag{11}
\]
The last absorption uses \(1+4o\le x^\varepsilon\). Precisely, for fixed level, \(e_D,e_L,K,c_{HH},e_K,C_E\) and \(\varepsilon>0\), there exists \(x_1\) such that for every \(x\ge x_1\), frame, axiomatized host on it and \(TT\), the conjunction of **EAtH** and **CoreAtH** implies the first upper bound on \(E_{\mathcal L}\) in (11). The concrete family supplies its records on selected windows. The exponent 9 specializes those two exponents only.
