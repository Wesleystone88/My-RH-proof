# Hilbert–Pólya operator discovery

**READ.** The strongest candidate is a finite-dimensional theta operator on Hecke eigenspaces. For a selected chain map \(T_t\), the source obtains an actual eigenvalue equation
\[
       T_tT_t^*x=\kappa_0\left(\prod_{i=0}^{m-1}z_i\right)x .
\]
Here \(x\) belongs to a specified Hecke subspace, \(\kappa_0>0\), and each \(z_i\) is a positive special value of a twisted partial automorphic \(L\)-function at \((1+t_R)/2\). This is stronger than a norm bound. It holds under explicit model, compatibility and scalar-factor hypotheses. [RealLowestKTypeCoeffSquareIntegrable 40–48](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L40-L48) [LabelSettingScalars 30–33](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/LabelSettingScalars.lean#L30-L33) [LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift 350–384](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift.lean#L350-L384)

**BLOCKED.** No inspected identity identifies those eigenvalues with the imaginary parts of the nontrivial zeros of \(\zeta\). The repository also has a prime-power expansion for \(-\zeta'/\zeta\), a local sum over actual zeta zeros, and a trace formula for a compact automorphic quotient. The operators and test functions in these three statements have different definitions. An equality identifying their spectral measures is the missing result.

## Repository baseline and scope

**READ.** The read-only checkout and the requested revision are both `e50d09817ad81469f737e8f637561e6ccf86c670`. The repository pins Lean 4.33.1 and Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`. I matched all 175,188 tracked Lean source files under `src/` byte-for-byte to their Git blob IDs. The search covered operator, theta, Gram/adjoint, Hecke, trace, explicit-formula, prime-power and zero terminology, together with direct use-site searches for the distinctive declarations. A nearby-text search for operator spectra and zeta zeros produced a false positive involving the algebraic type `HeightOneSpectrum`. The negative finding here concerns the inspected mathematics. A differently formulated identity could evade a text search. [Toolchain](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/lean-toolchain) · [Mathlib revision](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/lake-manifest.json#L4-L14)

**READ.** The main theorem is the root declaration `riemannHypothesis : RiemannHypothesis`. Its complete proposition is
\[
 \forall s\in\mathbb C,\quad
 \zeta(s)=0\ \Longrightarrow\ 
 (\neg\exists n\in\mathbb N,\ s=-2(n+1))\ \Longrightarrow\
 s\ne1\ \Longrightarrow\ \Re(s)=1/2 .
\]
It has no theorem parameters. Its proof term is `rhOfAll`, which applies `Formalism.VW.rh_of_every` to `allChi`. The latter invokes `UpperTheory.FinalTheorems.everyCharacter`. The stronger input quantifies over every \(N\ne0\), Dirichlet character modulo \(N\), and \(s\) with \(\Re s>1/2\), and asserts \(L(\chi,s)\ne0\) when \(\chi\ne1\) or \(s\ne1\). The zeta step uses the character of modulus one. `everyCharacter_of_row` calls the literature-and-window theorem with the Galois row, the reciprocity existence result and the window provider. [Main, lines 1–6](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Main.lean#L1-L6) · [Mathlib definition](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/NumberTheory/LSeries/RiemannZeta.lean#L185-L186) [MainTheorems 7–16](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Supplements/Kernels/MainTheorems.lean#L7-L16) [CritLine 29–32](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L29-L32) [EveryCharacter 13–14](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean#L13-L14) [MainConclusion 7–11](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean#L7-L11) [EveryCharacterOfLiteratureOfVWin 810–813](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L810-L813)

**READ / BLOCKED.** The complete *repository module* import closure of `Main` is every tracked `src/**/*.lean` including the root modules, except `src/Challenge.lean`: 175,187 files including `Main` itself. A traversal of local import headers found 348 distinct external import names, supplied by Lean/Mathlib and their packages. This gives an exact description of the module set. The transitive *proof-constant* footprint and actual kernel axiom list of the compiled headline remain unverified in this project. The comparator permits `propext`, `Quot.sound`, `Classical.choice`. The textual scan found no explicit `axiom` or `opaque` declarations or proof-hole tokens in the solution import closure after comment/string filtering. The challenge template is outside that closure. Supplied measures, kernels, decomposition hypotheses, arithmetic parameters and literature propositions below still carry mathematical content. I use RH only as the question's provisional assumption. No step of the experiments inserts zeta zeros. [Comparator](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/comparator.json)

## A. Operator inventory

| Evidence and object | Domain, codomain and construction | Adjoint, spectrum and arithmetic content |
|---|---|---|
| **READ / DERIVED.** Lattice theta lift | For number field \(K\), sesquilinear \(h\) on \(V\), finite representatives \(s\) and \(\tau\in\mathbb C\), `thetaLift` takes \(f:\operatorname{Sub}_{\mathcal O_K}(V)\to\mathbb C\) to one complex number. Varying \(\tau\) produces a function. The finite sum is linear in \(f\); its kernel is a lattice-vector series. | Positive finite automorphism weights give a domain inner product. Evaluation alone supplies no target Hilbert norm. A specified finite coefficient projection has a genuine adjoint and a computable arithmetic Gram matrix (section G). [StatementTheta 23–32](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/HermitianLattices/StatementTheta.lean#L23-L32) [Statement 132–154](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L132-L154) |
| **READ / COMPILED.** Weighted finite kernels | `kerOp` sends \(R^I\to R^J\), \(f\mapsto(\sum_iw_i f_iK_{ij})_j\), over a commutative semiring. `chainOp` takes \(R^{I_0}\to R^{I_m}\); `kerMul` gives the intervening weighted matrix product. | `kerAdj` is conjugate transpose. I kernel-checked the weighted pairing identity in a temporary independent file. It specializes to a Hilbert adjoint for complex coefficients and positive real weights. An arbitrary \(K\) encodes only its entries; the lattice theta coefficients in G give it arithmetic content. [Statement 10–45](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L10-L45) |
| **READ.** Adelic theta integral | For fixed \(D,V,W,\omega,\phi,\mu_G,\mathcal F_G\), `thetaLift` maps functions \(GA(W)\to\mathbb C\) to functions \(GA(V)\to\mathbb C\) by the integral in C. `thetaKO` evaluates the supplied Weil action at zero. | Pairings are Petersson-type integrals. The definition accepts arbitrary functions and measures; integrability and a positive Hilbert realization must be established on the chosen domain. The coefficient field, Weil action, Schwartz vector, quotient and automorphic form enter the integral. [LocalNewformFunction 55–79](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean#L55-L79) [RallisInnerProductFormula 15–65](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/RallisInnerProductFormula.lean#L15-L65) |
| **READ.** Realized theta operators | In `RealDat`, \(T_t=R.Th(t):(R.HX(t)).H\to_\mathbb C R.HE.H\) and \(R.thG(i,t):(R.HV(i,t)).H\to_\mathbb C(R.HW(i,sg_0)).H\). `HMod` bundles a finite-dimensional complex inner-product space and a linear realization into functions. The maps are fields. The theorems in C constrain them. | Their adjoints exist in finite dimension. `AForm` and `BForm` specify their Gram actions on Hecke pieces. The strongest read theorem is `ChainScalar.bForm`. No discreteness or boundedness issue arises for each fixed finite matrix; an infinite family has additional domain issues. [LinksDefs 161–168](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/IndefiniteReal/LinksDefs.lean#L161-L168) [LinksDefs 582–612](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/IndefiniteReal/LinksDefs.lean#L582-L612) [RealLowestKTypeCoeffSquareIntegrable 40–48](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L40-L48) |
| **READ.** Inert Hecke operations | For a selected good label \(i\), \(op_i\in{\rm End}_{LL}((A.MtCSD(j,t)).Forms)\). The theorem takes \(op\) and a Hecke compatibility witness, with valid family/model data, a conjugation-fixed good place and an ordered list of label integers. | Rational matrix entries lie in `cmMax` and the pairing `csum` satisfies \([op_i f,g]=[f,op_i g]\). A positive complex realization gives a self-adjoint finite operator. Eigenlabels carry place and Hecke information. No ordinate enters. [InertHeckeOperatorsLiftsRationalSelfAdjointLabelStatement 14–15](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/InertHeckeOperatorsLiftsRationalSelfAdjointLabelStatement.lean#L14-L15) [InertHeckeOperatorsRowsRationalSelfAdjointLabelsStatement 14–15](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/InertHeckeOperatorsRowsRationalSelfAdjointLabelsStatement.lean#L14-L15) |
| **READ.** Integrated right-regular representation | \(R_\Gamma(f)\) is convolution by a compactly supported continuous test function acting on \(L^2(G/\Gamma)\) in the repository's right-coset convention. The trace theorem assumes a discrete cocompact subgroup, the stated topological/Haar hypotheses and trace class of that operator. | The theorem sums traces of restricted operators with representation multiplicities. The same trace equals a sum of orbital integrals. The decomposition assumptions and the test function matter. This is a genuine infinite-dimensional spectral candidate, with no specified zeta Hamiltonian. [TraceFormulaCompact 19–26](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/GroundTheory/AutomorphicForms/TraceFormulaCompact.lean#L19-L26) [TraceFormulaCompact 112–142](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/GroundTheory/AutomorphicForms/TraceFormulaCompact.lean#L112-L142) |
| **READ.** Frobenius matrix | A representation \(r:\Gamma\to GL_a(\overline{\mathbb Q}_\ell)\), element \(s\), and field identification into \(\mathbb C\) give a finite complex matrix \(M\). `iota_trc` and `trace_pow_of_charpoly` compute its power traces. The arithmetic specialization requires a compatible Galois triple and a good Frobenius place. | Power traces preserve eigenvalues with algebraic multiplicity. Frobenius need not be self-adjoint. These are actual local spectral invariants. Section D gives the exact local generating function. [ExistsRationalLocalOperators 44–51](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsRationalLocalOperators.lean#L44-L51) [CharpolySmulOfProd 398–416](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/CharpolySmulOfProd.lean#L398-L416) |
| **READ / DERIVED.** Finite Fourier, Weil and Gauss operators | `weilS` is the normalized polar-character transform on \(\mathbb C^D\); `weilT` multiplies by a quadratic phase. `gaussOp` is \(\sum_{c\in\mathbb F^\times}\psi(c)\rho(c)\in{\rm End}_{\mathbb C}V\) for a finite field and a representation. | `gaussOp_eq` proves that both products with the designated dual are \(qI\) on vectors with zero multiplicative orbit sum, for nontrivial \(\psi\). Under unitarity of \(\rho\), conjugation of the additive character and \(\rho(c)^*=\rho(c^{-1})\) identify the dual with the adjoint. This gives the singular value \(\sqrt q\) on that sector. [StatementTheta 14–20](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/HermitianLattices/StatementTheta.lean#L14-L20) [Statement 200–213](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L200-L213) [GaussOp 37–72](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/GaussOp.lean#L37-L72) |
| **READ.** Conditional extension with zero fallback | `TripleAssembly.thetaLift` returns a complex linear map from complex functions on adelic matrices to a supplied module \(P\). It chooses a \(q\) with \(q({\rm thO}(\Psi))=p_D(\Psi)\) for all \(\Psi\in S\) if such a map exists; otherwise it returns zero. | Neither uniqueness outside the prescribed subspace nor a Hilbert metric on \(P\) is part of this definition. This occurrence of the word “lift” does not establish a canonical spectrum. [ExistsRtensOp 62–67](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRtensOp.lean#L62-L67) |

## B. Amplifier audit

**READ.** There are three named definitions of `gainP` and a separate structure field with this name. The usual local gain has type
\[
 {\rm Inst}(D,L)\to{\rm Consts}\to(H\to\mathbb Z)\to(H\to\mathbb Z)\to\mathbb N_p\to\mathbb N_j\to\mathbb R .
\]
Writing \(R_p={\rm reps}(X,p)\), \(V_p={\rm VV}(X,K,a,b,p)\), \(b_r=[g_0(r)]_+\), its exact formula is zero when \(({\rm inertClass}(p)\land h_p=0)\) or \(p>X''\); otherwise it is
\[
 \sum_{r\in V_p}\max\{g_U(r)-{\rm Pr}(r),b_r\}
       +\sum_{r\in R_p\setminus V_p} b_r .
\]
\(V_p\) is the good representatives if `Cand` and \({\rm Sig}=m\sum_{\rm good}\kappa_r\le x^{-\varepsilon}\), and is empty otherwise. `Cand` demands primality, \(p<X'\), inert class, a lower bound on the order of \(h_p\), and a band exclusion conditional on the cutoff. \(h_p\) is selected from the projected arithmetic Frobenius set for primes over \(p\). `kapLoc` switches between a numerical small-prime term and input `Inst.kapI`. The parameter tables, selected representatives, offsets, and correction constants are inputs to this calculation. The inhabitation view agrees by `rfl`. The local arithmetic version takes an explicit offset \(o_j\) and base residue \(h\); the formula has the same two branches. [IsResidueClassZero 93–106](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L93-L106) [IsResidueClassZero 138–197](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L138-L197) [IsResidueClassZero 225–305](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L225-L305) [IsResidueClassZero 355–368](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L355-L368) [IsResidueClassZero 196–239](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/IsResidueClassZero.lean#L196-L239) [TiesCore 229–232](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/InertJacobiLevels/TiesCore.lean#L229-L232) [TiesView 33–41](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/InertJacobiLevels/TiesView.lean#L33-L41)

**READ.** Prime powers enter *inside* the gain. Set \(A_s=a(s)-2c_G\) and \(U_{s,e}={\rm fillG}(b,j,{\rm partner}(p,s,e))+c_G\). Then
\[
 \begin{split}
 g_0(r)&=\sum_{s\in{\rm topsOn}(r)}\sum_{e\ {\rm odd},\neg{\rm Excl}(p,s,e)}
                  [A_s/p^e-U_{s,e}]_+-d_\ell(r),\\
 g_U(r)&={\rm gam}(p)\sum_{s\in{\rm topsOn}(r)}A_s
       -\sum_{s\in{\rm topsOn}(r),\neg{\rm IsV}(s)}
           \sum_{e\ {\rm odd}}\min(A_s/p^e,U_{s,e})-d_\ell(r).
 \end{split}
\]
The partner follows the residue/Frobenius orbit. `Excl` detects an odd first arrival at a different top. `Pr` and \(d_\ell\) subtract explicit losses. Thus the gain retains orbit type, selected tops, exponents and size deficits but discards signs and phase by clipping, summation and branch selection. The local place gain becomes this number through the `ParametersFill` equality on supported inert/signal places. The derived total below the cutoff is \(2\log p\,[\mathbf1_{\rm inert/signal}\sum_j{\rm gainP}(p,j)-\tau_p]\) in the tied weight model. [IsResidueClassZero 225–295](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L225-L295) [IsResidueClassZero 400–410](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L400-L410) [TieTTwValsOfMem 222–248](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/InertJacobiLevels/TieTTwValsOfMem.lean#L222-L248)

**READ.** Nonnegativity of `gainP` follows by unfolding and taking maxima with zero; cutoff vanishing and the good-representative containment also follow from the branch definitions. By contrast `gainD_le_gainS` assumes ParametersFill at every place, a dropped-prime condition and lift membership. Its proof uses the support, drop, and served-place cases. These are different claims. In the numerical ledger `LossP.gainP : Fin m → ℕ → ℝ` is supplied by a record. The explicit model `lm_Lp` assigns `lm_gn`, the sum of \([a_t/p^e-w(j,{\rm partner}(t,e{\rm Fr}_p))]_+\) over tops and the selected \(1\le e\le N\) with \(e{\rm Fr}_p\notin\Phi\), on inert primes up to the cutoffs, and zero elsewhere. It sets \(\tau,{\rm lo},{\rm fl}\) to zero. `log_derivative_identity` in **this** model proves equality of two finite cost ledgers by rewriting. Section D identifies the distinct analytic logarithmic-derivative theorem. [WeightDegreeSizes 922–934](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/WeightDegreeSizes.lean#L922-L934) [WeilJacquetShalikaLaw 538–575](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/WeilJacquetShalikaLaw.lean#L538-L575) [Chain2aCoreNoAnalytic 403–418](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/Chain2aCoreNoAnalytic.lean#L403-L418) [SecondKindBucket 95–96](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/SecondKindBucket.lean#L95-L96) [ChainLatticeSizesModelEventually 438–473](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/ChainLatticeSizesModelEventually.lean#L438-L473) [ChainLatticeSizesModelEventually 2184–2199](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/ChainLatticeSizesModelEventually.lean#L2184-L2199)

**READ / DERIVED.** `zeroCh : LatInst D → LatInst D` retains the place assignment, fills, levels and ramification submodule and replaces every `Kz j` by the zero linear map. An ordinary local chain takes \(K_j:F_j\to_{K_f}F_{j+1}\) as data and composes them, with identity at level zero. Hence for \(m\ge1\) the modified composition is zero. Theorem `vKge_zero` accepts any real requested gain \(g\). The proof chooses an irreducible uniformizer and uses zero membership in the scaled lattice. The eventual `admissible_family_no_kernel` and `linkG_without_kernels` applications still require admissibility 1–9, stabilizer, lattice, orbit-window and descent data. They use this simplification for the valuation demands. A zero output attains every such lower valuation threshold and supplies no spectral information about the numerical gain. The direct dependency arrow from `gainP` to `zeroCh` is absent: one computes a scalar from arithmetic inputs, the other changes a witness in a valuation proof. [DataGChain 61–87](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/DataGChain.lean#L61-L87) [IsResidueClassZero 411–428](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L411-L428) [AdmissibleFamilyNoKernel 166–240](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L166-L240)

## C. From a theta lift to an arithmetic Gram operator

**READ / DERIVED.** The first explicit arithmetic kernel one can evaluate without selecting an automorphic representation is
\[
 \Theta_L(\gamma,\tau)=\sum_{x\in L}
   e^{\pi i\tau\,{\rm Tr}_{K/\mathbb Q}h(\gamma+x,\gamma+x)},\qquad
 (\Theta f)(\tau)=\sum_{L\in s}\frac{f(L)\Theta_L(0,\tau)}{\#\operatorname{Aut}(h,L)} .
\]
For a positive definite lattice, \(\Im\tau>0\) gives Gaussian decay. The bare Lean definition is a totalized infinite sum; analytic interpretations require summability. Finite stabilizers give positive weights. A supplied kernel on two finite class sets likewise gives \(Tf(j)=\sum_i w_iK_{ij}f_i\). Its Gram kernel, with target weights \(v_j\), is \(C_{ik}=\sum_jv_j\overline{K_{ij}}K_{kj}\), acting with source weights \(w_k\). This is a cross-correlation between different classes. The coefficient specialization in G exhibits a nonzero off-diagonal entry. `LatSeeSaw` specifies the adjoint identity for arbitrary lattice kernels, while the raw theta function itself supplies one analytic variable and no preferred target inner product. [StatementTheta 23–32](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/HermitianLattices/StatementTheta.lean#L23-L32) [Statement 132–154](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L132-L154) [Statement 186–198](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L186-L198) [LatLiftIndep 78–106](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/LatLiftIndep.lean#L78-L106)

**READ.** In the adelic realization, for a fixed Weil action \(\omega\), \(\theta_\omega(h,g;\phi)=(\omega(h,g)\phi)(0)\) and
\[
 (T_\phi f)(h)=\int_{\mathcal F_G}\overline{\theta_\omega(h,g;\phi)}f(g)\,d\mu_G(g).
\]
On a common integrable domain this is linear in \(f\) and conjugate-linear in \(\phi\). `InnerProductFormula` requires integrability of both lifts, their product, both matrix coefficients and the doubled integrand. Its equality expresses a Petersson pairing of outputs as the volume times a doubling integral. The packet `RFconcl` separately expresses a theta pairing via the original pairing, continued partial Euler product and local zeta integrals, subject to the rank gap, Witt-index, Satake and nonvanishing conditions. `normBig_innerProduct` supplies a specialized nonzero constant times a product of Hecke \(L\)-values for selected bottom data. The conventions in `SchurIrreducible.thetaLift` conjugate the input form instead. These conventions matter before composing a lift with its adjoint. [RallisInnerProductFormula 22–65](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/RallisInnerProductFormula.lean#L22-L65) [SchurIrreducible 489–502](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/SchurIrreducible.lean#L489-L502) [SchurIrreducible 547–556](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/SchurIrreducible.lean#L547-L556) [PeterssonNormHeckeProduct 27–46](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/PeterssonNormHeckeProduct.lean#L27-L46)

**READ.** For an actual selected chain, `LiftChain` identifies its top row with \(F\) and requires \(G_j=vth_j(G_{j+1})\). The spaces are cusp spaces on possibly different unitary groups. `lift_eq_cI_io` identifies a step of the theta integral with a scalar times a linear multiplicity-space map for a compatible family satisfying PkHyp and RowOK. For the realized end-to-end map, `ChainScalar.bForm` assumes Core, SchurAll, Scalars, Kept, and IsSF. `Scalars` supplies positive stage constants and `IsLValue` matches the label to the *positive* partial twisted \(L\)-value. The proof sets \(\kappa_0=\prod_i\kappa(i+1)\). `thetaChainStep_positive_scalar_standingHypotheses` in turn derives Scalars under Given, \(D.host.ccK=\top\), and its ten published/local representation-theoretic premises. The exact hypotheses are reproduced below. Applying the displayed conclusion needs \(x\in EEc(R,SF,c)\) and all the IsLval witnesses. When this space contains a nonzero vector, the product is a genuine eigenvalue, including its arithmetic variation with compatible labels. A zero-dimensional component is vacuous. [ZetaProductPairs 238–251](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/ZetaProductPairs.lean#L238-L251) [ThetaLiftChainScalar 57–66](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftChainScalar.lean#L57-L66) [ThetaChainStepPositiveScalarStandingHypothesesStatement 26–27](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaChainStepPositiveScalarStandingHypothesesStatement.lean#L26-L27) [NormalFam 128–135](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/GaloisGeometry/NormalFam.lean#L128-L135) [RealLowestKTypeCoeffSquareIntegrable 28–48](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L28-L48) [LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift 350–384](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift.lean#L350-L384)

**DERIVED.** If \(TT^*x=\lambda x\) with \(\lambda>0\) and \(x\ne0\), then \(\|T^*x\|^2=\lambda\|x\|^2>0\), and \(T^*T(T^*x)=\lambda T^*x\). In the opposite direction use \(T\); scaling by \(1/\lambda\) gives inverse maps between the eigenspaces. This supplies the requested \(T^*T\) on the original source with the same nonzero multiplicity. The determinant-swap and eigenvalue-swap propositions specify precisely this finite-dimensional setting. The abstract `RallisAdj` requires the pairing identity throughout a subspace *and* invariance under \(T^*T\); without invariance the identity controls the compression. A finite Gram determinant or agreement of nonzero spectra does not give a Fredholm determinant for zeta. [Statement 232–251](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L232-L251) [Statement 284–299](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L284-L299) [ChainScalar 10–30](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/ChainScalar.lean#L10-L30) [EigenSwap 7–25](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/EigenSwap.lean#L7-L25)

## D. Exact prime-power and spectral identities

1. **READ.** For \(\Re s>1\), \(-\zeta'(s)/\zeta(s)=\sum_n\Lambda(n)n^{-s}\). The Dirichlet version inserts \(\chi(n)\). The repository actually uses this identity to prove, for the modulus-one character,
   \[
   \int_1^\infty G_\chi(y)y^{-s-1}dy=
   -\frac{\zeta'(s)/\zeta(s)+1/(s-1)+1-(1+\gamma)s}{s(s-1)} .
   \]
   This is an exact transform of a smoothed prime sum. [Mathlib, Dirichlet.lean 436–439](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/NumberTheory/LSeries/Dirichlet.lean#L436-L439) [LRight 88–94](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LandauZeroFreeBounds/ExceptionalZeroBounds/LRight.lean#L88-L94) [mellinGchiModOne 115–119](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiModOne.lean#L115-L119) [mellinGchiModOne 185–195](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiModOne.lean#L185-L195)
2. **READ.** Put \(a=3/2+it\). In \(|s-a|\le2/3\) off the pole and zeros, the difference between \(\zeta'/\zeta(s)+1/(s-1)\) and \(\sum_{|\rho-a|\le5/6}m_\rho/(s-\rho)\) has norm at most \(C\log(|t|+2)\). The sum takes actual zeta zeros with their analytic orders. It is local and has a remainder. It does not compute the trace of the theta Gram operator. [LogDerivRiemannZetaLocalZeroSum 87–101](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LogDerivRiemannZetaLocalZeroSum.lean#L87-L101)
3. **READ / DERIVED.** At an unramified \(p\), the character weight in `primVal` at \(p^e\) equals \(\psi(e{\rm Fr}_p)\). With inertia, the coset mean equals that value multiplied by the invariant-space projector in the one-dimensional character representation: averaging a nontrivial character over inertia gives zero by translating its sum. Thus the untruncated character coefficient really is a local trace on inertia invariants. The positive-part cost `askP` and the local gain apply additional nonlinear functions to arithmetic weights. [FirstPrimeNeSecondPrime 61–91](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/FirstPrimeNeSecondPrime.lean#L61-L91) [IsResidueClassZero 245–264](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L245-L264)
4. **READ / DERIVED.** If the local matrix \(M\) has roots \(\alpha_j\) of its characteristic polynomial with multiplicities, \({\rm tr}(M^e)=\sum_j\alpha_j^e\). Therefore, as formal power series,
   \[
   -u\frac{d}{du}\log\det(I-uM)=\sum_{e\ge1}{\rm tr}(M^e)u^e .
   \]
   Factor the determinant as \(\prod_j(1-u\alpha_j)\) and expand each geometric series. For \(u=p^{-s}\), the logarithmic derivative of the inverse Euler factor with a minus sign is \(\log p\sum_e{\rm tr}(M^e)p^{-es}\). Taking the trivial one-dimensional \(M=1\) gives zeta's local terms exactly. It has the same sole eigenvalue 1 at every prime. `IsTripleWith.charpoly_frob` supplies arithmetic characteristic-polynomial data under the hypotheses in A. None of these local spectra by itself specifies the global zero spectrum. [ExistsRationalLocalOperators 44–51](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsRationalLocalOperators.lean#L44-L51) [CharpolySmulOfProd 398–416](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/CharpolySmulOfProd.lean#L398-L416)
5. **READ.** The compact quotient trace formula identifies \({\rm tr}\,R_\Gamma(f)\) both with \(\sum_\pi m_\Gamma(\pi){\rm tr}\,\pi(f)\) and with the volume-weighted sum of orbital integrals over conjugacy classes. It requires a Hilbert sum of complete invariant irreducible subspaces, compatible centralizer measures and trace class. The multiplicities are those of the regular representation, and orbital classes have no declared identification here with rational prime powers. [TraceFormulaCompact 112–142](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/GroundTheory/AutomorphicForms/TraceFormulaCompact.lean#L112-L142)

## E. Hilbert–Pólya gap

| Candidate | Self-adjointness and domain | Spectrum or multiplicity established | Missing bridge |
|---|---|---|---|
| **READ / DERIVED.** Selected theta chain | \(T_tT_t^*\) on all of a finite-dimensional complex Hilbert space, and \(T_t^*T_t\) on its source | Special-value products on compatible nonzero Hecke blocks. Nonzero multiplicity transfers; a complete list of all blocks would be extra data. | A canonical common infinite space, compatible inclusions or limiting operator, and a global zero-counting trace identity. |
| **DERIVED.** Finite theta coefficient map | Finite positive Gram operator after choosing coefficients and target weights | Multiplicity is ordinary matrix multiplicity. Arithmetic correlations are visible in G. | Canonical choice of target norm/test space, control as the cutoff grows, and identification with zeta rather than a lattice theta series. |
| **READ.** Hecke and Frobenius | Symmetric Hecke actions under the metric ties; finite Frobenius matrices have no asserted Hilbert self-adjointness | Hecke labels, Satake data and local power traces distinguish arithmetic inputs. | Turning a collection of local labels into a single self-adjoint generator with the required global multiplicities. |
| **READ.** Compact quotient convolution | Bounded integrated operator on \(L^2\), trace class under an explicit premise. Arbitrary \(f\) need not give a self-adjoint operator. | Automorphic multiplicities contribute to a genuine spectral trace. | A selected group, quotient and test-function calculus identifying the orbital side with zeta's explicit formula, including archimedean and pole terms. |
| **READ.** Gain and zero chain | The gain is real-valued. The modified positive-length chain is the zero map, generally between different spaces. | The valuation inequality survives zero output. | Neither quantity supplies observable zeta ordinates. |

**BLOCKED.** To assert \(H\psi_n=\gamma_n\psi_n\) one needs a single, independently defined Hilbert space and operator, a dense self-adjoint domain if unbounded, spectral type and multiplicity including a convention for the \(\pm\gamma\) symmetry, and an equality connecting its resolvent, test-function traces or normalized determinant to completed zeta. Positivity restricts a Gram spectrum to \([0,\infty)\); using only positive ordinates would already be a choice needing justification. Under the working RH assumption the ordinates are real, but no operator domain, eigenvector, multiplicity correspondence or arithmetic trace identity follows from their reality.

## F. Three research leads, in order of evidence

1. **READ / HYPOTHESIS.** The selected theta Gram operator has the most direct evidence: a proved conditional eigenvalue formula with named arithmetic \(L\)-values. The test is to extract two nonzero Hecke components from one common \(R,t,SF\) and check whether their normalized products differ. This would distinguish arithmetic spectral variation on a single operator from changing its normalization. [RealLowestKTypeCoeffSquareIntegrable 40–48](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L40-L48) [LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift 350–384](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift.lean#L350-L384)
2. **READ / DERIVED.** The lattice theta coefficient kernel is directly computable from a form and a lattice. Cross-class entries and rank can be checked without global host witnesses. Section G gives an exact example and the next invariance test. [StatementTheta 23–32](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/HermitianLattices/StatementTheta.lean#L23-L32) [Statement 136–154](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L136-L154)
3. **READ / HYPOTHESIS.** The compact trace formula and local Frobenius power traces give two exact trace mechanisms. Their difficult compatibility test is whether a specified family of quotient test functions recovers the prime weights and the archimedean term of the zeta explicit formula simultaneously. Generic trace-class and Euler-factor identities alone leave this open. [TraceFormulaCompact 112–142](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/GroundTheory/AutomorphicForms/TraceFormulaCompact.lean#L112-L142) [ExistsRationalLocalOperators 44–51](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsRationalLocalOperators.lean#L44-L51) [mellinGchiModOne 115–119](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiModOne.lean#L115-L119)

## G. Independent experiment

**DERIVED.** I tested the natural Fourier coefficients of two integral lattices in the same rational positive plane. Take \(K=\mathbb Q\) and the symmetric form with matrix \(\left(\begin{smallmatrix}2&1\\1&12\end{smallmatrix}\right)\). On \(L_1=\mathbb Z^2\) its squared length is \(2Q_1\), \(Q_1=x^2+xy+6y^2\). On the basis \((1/2,1/2),(-3/2,1/2)\) of \(L_2\) it is \(2Q_2\), \(Q_2=2x^2+xy+3y^2\). The determinant of the change of basis is 1. The lattices are equivalent locally at each odd prime, since this change of basis is integral and invertible there. At 2 take a 2-adic root \(\alpha\equiv0\bmod2\) of \(2\alpha^2+\alpha+2=0\), which lifts because the derivative is odd. In the \(Q_2\) plane use columns \((\alpha,1)\), \((\alpha(2\alpha+1)-1,2\alpha+1)\). They have determinant 1, first norm 1, and polar cross-term 1. The common discriminant \(-23\) forces second norm 6. Hence this tests two representatives of one genus. Their different minima distinguish them globally.

**DERIVED.** For the coefficient projection \(1\le n\le N\), use \(r_i(n)=\#\{v:Q_i(v)=n\}\). This is precisely the coefficient of \(e^{2\pi i n\tau}\) in `thetaL`. The source weights \(w_i=1/\#\mathrm{Aut}(L_i)\) are \(1/4,1/2\). I chose ordinary counting measure on the retained coefficient indices. Thus \(G_{ij}=w_j\sum_{n\le N}r_i(n)r_j(n)\). Exact integer enumeration gives:

| \(N\) | \(G=T^*T\) in the class basis | Trace | Determinant |
|---:|---|---:|---:|
| 1 | \(\left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right)\) | 1 | 0 |
| 2 | \(\left(\begin{smallmatrix}1&0\\0&2\end{smallmatrix}\right)\) | 3 | 2 |
| 6 | \(\left(\begin{smallmatrix}6&6\\3&8\end{smallmatrix}\right)\) | 14 | 30 |
| 12 | \(\left(\begin{smallmatrix}15&20\\10&20\end{smallmatrix}\right)\) | 35 | 100 |

**DERIVED.** Reproduction requires only counting integer pairs. For \(N=12\) the two rows are \((2,0,0,2,0,4,0,4,2,0,0,4)\) and \((0,2,2,2,0,2,0,2,2,0,0,4)\). Both forms satisfy \(Q_i(x,y)\ge(x^2+y^2)/2\) by \(2|xy|\le x^2+y^2\). Automorphisms are ordered integer columns with determinant \(\pm1\), column norms \(Q_i(e_1),Q_i(e_2)\), and cross coefficient 1; the same bound makes that enumeration exhaustive. Self-adjointness is for the weighted class inner product: \(w_iG_{ij}=w_jG_{ji}\). This calculation establishes a cutoff-dependent, non-scalar arithmetic spectrum. The evidence at this stage is a two-class coefficient restriction. At cutoff 6 its eigenvalues are \(7\pm\sqrt{19}\). [StatementTheta 23–26](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/HermitianLattices/StatementTheta.lean#L23-L26) [Statement 136–154](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L136-L154)

**COMPILED.** In a temporary independent Lean 4.33.1 file I copied the pinned `kerOp`, `kerMul`, `wip`, `kerAdj`, `chainOp` and proposition signatures, then proved `HPCheck.weightedAdjoint : KerAdjoint` by distributing the sums, using self-conjugacy of the input weights, and interchanging the two finite sums. Lean exited successfully. `#print axioms` reported `propext`, `Classical.choice` and `Quot.sound`. The enumeration above used exact rational arithmetic in Python. Both checks have strictly smaller scope than the selected automorphic-chain theorem. [Statement 10–38](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L10-L38)

**DERIVED — a good-prime check.** I independently constructed the 3-neighbor operator, then compared it with the theta coefficients. Both forms have two isotropic lines modulo 3. For each line choose a primitive lift \(v\) with \(9\mid Q(v)\), and \(u\) with \(\det(v,u)=1\). The neighbor has basis \(v/3,3u\): the vectors pairing with \(v\) to zero modulo 3 are generated by \(v,3u\), and adjoining \(v/3\) gives the claimed index-3 neighbor. Its quadratic coefficients are \((Q(v)/9,B(v,u),9Q(u))\), with \(B\) the polarization of \(Q\). Here are the complete transitions. The last column gives the unimodular basis columns sending the neighbor form to the indicated target form.

| Source | \(v,\ u\) | Neighbor coefficients | Target and basis columns |
|---|---|---|---|
| \(Q_1\) | \((-3,-1),(1,0)\) | \((2,-7,9)\) | \(Q_2:\ (-1,0),(-2,-1)\) |
| \(Q_1\) | \((-1,-2),(0,-1)\) | \((3,25,54)\) | \(Q_2:\ (-4,1),(1,0)\) |
| \(Q_2\) | \((-3,1),(-1,0)\) | \((2,11,18)\) | \(Q_2:\ (-1,0),(-3,1)\) |
| \(Q_2\) | \((-2,1),(-1,0)\) | \((1,7,18)\) | \(Q_1:\ (-1,0),(3,-1)\) |

**DERIVED.** The resulting class matrix \(A_3=\left(\begin{smallmatrix}0&2\\1&1\end{smallmatrix}\right)\) is self-adjoint for weights \(1/4,1/2\) by detailed balance. Its characteristic polynomial is \((\lambda-2)(\lambda+1)\). For \(r(n)=(r_1(n),r_2(n))^\mathsf{T}\), independent integer enumeration through \(n=36\) verified
\[
 A_3r(n)=r(3n)+\mathbf1_{3\mid n}r(n/3),\qquad 1\le n\le12 .
\]
This is the split-prime weight-one coefficient rule (\(-23\equiv1\bmod3\)). Yet the cutoff Gram matrix fails a stricter test: \(G_6 A_3-A_3G_6=\left(\begin{smallmatrix}0&2\\-1&0\end{smallmatrix}\right)\). Thus one concrete prime operator has an arithmetic spectrum and passes the coefficient test, while the most immediate norm on the truncated theta coefficients fails to commute with it. This two-class experiment was constructed independently from the pinned lattice-kernel definition. Its finite eigenvalues \(2,-1\) are neighbor eigenvalues. [StatementTheta 23–26](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/HermitianLattices/StatementTheta.lean#L23-L26) [Statement 136–154](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L136-L154)

**HYPOTHESIS — next independent experiment.** Prove or falsify the coefficient identity at \(p=3\) for every \(n\) by a multiplicity-preserving count of lattice vectors in the four neighbors above. The test requires no extra fitted parameters. It would promote the 12 coefficient checks to an exact prime-to-theta intertwiner on this two-class sector. Then evaluate whether the source's Petersson pairing gives a Gram operator commuting with \(A_3\). The nonzero cutoff commutator provides a control for that test. The global zero-spectrum question still requires section E.

## Local gain computation, from inputs to output

**READ.** The following gives the evaluation order for the primary geometric gain. Each linked definition has its constants and arguments in the source. The external leaves are the scale, host, ranks, prime, two integer weight functions, and the local record of orbit representatives, offsets and loss parameters. Frobenius is chosen from a prime-over-prime condition. No choice of a local chain map is an input to this calculation.

- `hG` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 37–37](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L37-L37)
- `KG` — `hG`. [IsResidueClassZero 39–39](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L39-L39)
- `rG` — `KG`. [IsResidueClassZero 41–41](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L41-L41)
- `N1` — `hG`, `rG`. [IsResidueClassZero 43–43](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L43-L43)
- `cG` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 47–47](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L47-L47)
- `Nm` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 49–49](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L49-L49)
- `L1` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 51–51](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L51-L51)
- `L2` — `L1`. [IsResidueClassZero 53–54](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L53-L54)
- `Nstar` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 56–56](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L56-L56)
- `La` — `N1`. [IsResidueClassZero 58–58](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L58-L58)
- `rho` — `N1`, `Nstar`, `La`. [IsResidueClassZero 60–61](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L60-L61)
- `rhoB` — `Nstar`, `La`, `rho`. [IsResidueClassZero 63–64](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L63-L64)
- `InBand` — `rhoB`. [IsResidueClassZero 83–85](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L83-L85)
- `gam` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 89–89](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L89-L89)
- `frobSet` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 93–95](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L93-L95)
- `hP` — `frobSet`. [IsResidueClassZero 97–98](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L97-L98)
- `IsResidueClassZero` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 100–100](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L100-L100)
- `IsSg` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 102–102](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L102-L102)
- `partner` — `hP`, `IsSg`. [IsResidueClassZero 131–132](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L131-L132)
- `fill` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 154–155](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L154-L155)
- `kaJ` — scale, host, numerical or supplied record inputs. [IsResidueClassZero 157–157](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L157-L157)
- `fillG` — `fill`, `kaJ`. [IsResidueClassZero 159–159](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L159-L159)
- `stepP` — `hP`, `IsSg`. [IsResidueClassZero 161–161](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L161-L161)
- `nP` — `hP`, `IsSg`. [IsResidueClassZero 163–164](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L163-L164)
- `reps` — `stepP`. [IsResidueClassZero 166–166](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L166-L166)
- `topsOn` — `stepP`. [IsResidueClassZero 168–169](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L168-L169)
- `Nv` — `topsOn`. [IsResidueClassZero 171–171](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L171-L171)
- `topsPos` — `hP`. [IsResidueClassZero 173–174](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L173-L174)
- `wPos` — `hP`. [IsResidueClassZero 176–177](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L176-L177)
- `IsV` — `hP`, `stepP`, `nP`. [IsResidueClassZero 179–180](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L179-L180)
- `Good` — `hG`, `KG`, `rG`, `L2`, `hP`, `topsPos`. [IsResidueClassZero 182–184](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L182-L184)
- `kapIIf` — `rG`. [IsResidueClassZero 202–203](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L202-L203)
- `kapLoc` — `kapIIf`. [IsResidueClassZero 227–228](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L227-L228)
- `al` — `cG`. [IsResidueClassZero 230–230](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L230-L230)
- `capU` — `cG`, `partner`, `fillG`. [IsResidueClassZero 232–233](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L232-L233)
- `IsDist` — `partner`. [IsResidueClassZero 235–236](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L235-L236)
- `Excl` — `IsDist`. [IsResidueClassZero 238–239](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L238-L239)
- `dl` — `Nm`, `nP`, `Nv`. [IsResidueClassZero 241–243](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L241-L243)
- `g0` — `topsOn`, `al`, `capU`, `Excl`, `dl`. [IsResidueClassZero 247–250](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L247-L250)
- `gU` — `gam`, `topsOn`, `IsV`, `al`, `capU`, `dl`. [IsResidueClassZero 254–258](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L254-L258)
- `Pr` — `rG`, `cG`, `Nm`, `fillG`, `nP`, `topsOn`, `Nv`, `IsV`. [IsResidueClassZero 262–267](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L262-L267)
- `kapv` — `hP`, `topsPos`, `wPos`, `kapLoc`. [IsResidueClassZero 276–277](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L276-L277)
- `Cand` — `InBand`, `hP`, `IsResidueClassZero`. [IsResidueClassZero 279–281](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L279-L281)
- `goodReps` — `reps`, `Good`. [IsResidueClassZero 285–285](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L285-L285)
- `Sig` — `kapv`, `goodReps`. [IsResidueClassZero 287–288](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L287-L288)
- `VV` — `Cand`, `goodReps`, `Sig`. [IsResidueClassZero 292–293](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L292-L293)
- `gainP` — `hP`, `IsResidueClassZero`, `reps`, `g0`, `gU`, `Pr`, `VV`. [IsResidueClassZero 355–358](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L355-L358)

**READ.** The declaration of the alternate offset version is under the namespace of the local arithmetic model; the GC view equality is definitional. For the separate ledger see the field assignment and the actual sum in B. The local valuation chain follows the branch `Levels.Fm → Chain.Kz → Chain.chainK → LatInst.vKge → vKge_zero → admissible_family_no_kernel → linkG_without_kernels`. Here the arrows indicate construction or use; the spaces vary by lift. [DataGChain 61–87](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/DataGChain.lean#L61-L87) [AdmissibleFamilyNoKernel 166–240](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L166-L240)

## Exact Lean types and hypotheses

**READ.** These excerpts fix the dependent types and the local hypotheses behind the conventional formulas. Each is from the inspected revision. Definitions marked `Prop` specify a condition. Theorems returning one of these conditions are cited separately.

<details><summary>Formalism/LocalToGlobal/IndefiniteReal/LinksDefs.lean, lines 161–168</summary>

[LinksDefs 161–168](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/IndefiniteReal/LinksDefs.lean#L161-L168)

```lean
structure HMod (X : Type) [AddCommGroup X] [Module ℂ X] where

  H : Type
  [nH : NormedAddCommGroup H]
  [iH : InnerProductSpace ℂ H]
  [fH : FiniteDimensional ℂ H]

  e : H →ₗ[ℂ] X
```

</details>

<details><summary>Formalism/LocalToGlobal/IndefiniteReal/LinksDefs.lean, lines 601–609</summary>

[LinksDefs 601–609](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/IndefiniteReal/LinksDefs.lean#L601-L609)

```lean
Th : ∀ t, (HX t).H →ₗ[ℂ] HE.H

  BV : ∀ i, D.what₂.Tau → Matrix (Fin (Vc D i).rank) (Fin (Vc D i).rank) ℂ

  ioP : ∀ i, LowT (MW i (sg0 D A)) →ₗ[ℂ] (cV i).W →ₗ[ℂ] PolF D (Wc D i).rank (Vc D i).rank

  thF : ∀ i t, (HV i t).H →ₗ[ℂ] MMap (MW i (sg0 D A))

  thG : ∀ i t, (HV i t).H →ₗ[ℂ] (HW i (sg0 D A)).H
```

</details>

<details><summary>Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean, lines 37–48</summary>

[RealLowestKTypeCoeffSquareIntegrable 37–48](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L37-L48)

```lean
def IsLval (i : Fin D.R.m) (t : T) (c : Eig D) (z : ℝ) : Prop :=
  ∃ B, GlobalTheory.LFun.IsSysParamD D (GlobalTheory.IndefiniteRowSideFullHecke.LabelSettingScalars.badPl R t) D.R.r c B ∧ GlobalTheory.IndefiniteRowSideFullHecke.LabelSettingScalars.IsLValue R t B ((i : ℕ) + 1) z

variable (SF : Finset (HeightOneSpectrum (𝓞 D.host.F)))

def AForm : Prop :=
  ∃ a : Fin D.R.m → ℝ, (∀ i, 0 < a i) ∧ ∀ i t c, GlobalTheory.Hk3.Wcc R SF i c ≠ ⊥ → ∃ z : ℝ, IsLval R i t c z ∧
    ∀ x ∈ GlobalTheory.Hk3.Wcc R SF i c, R.thG i t (LinearMap.adjoint (R.thG i t) x) = ((a i * z : ℝ) : ℂ) • x

def BForm : Prop :=
  ∃ κ₀ : ℝ, 0 < κ₀ ∧ ∀ t c (z : Fin D.R.m → ℝ), (∀ i, IsLval R i t c (z i)) →
    ∀ x ∈ GlobalTheory.Hk3.EEc R SF c, R.Th t (LinearMap.adjoint (R.Th t) x) = ((κ₀ * ∏ i, z i : ℝ) : ℂ) • x
```

</details>

<details><summary>Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/LabelSettingScalars.lean, lines 30–33</summary>

[LabelSettingScalars 30–33](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/LabelSettingScalars.lean#L30-L33)

```lean
def IsLValue (t : T) (B : GlobalTheory.LFun.Fam D.host.E) (j : ℕ) (l : ℝ) : Prop :=
  GlobalTheory.LFun.Converges (GlobalTheory.LFun.above D.host.E (badPl R t : Set (HeightOneSpectrum (𝓞 D.host.F))))
               (GlobalTheory.LFun.twist B (GlobalTheory.LFun.val (R.toLevCh.mu t j))⁻¹) ((1 + (D.R.t : ℂ)) / 2) ∧
    0 < l ∧ GlobalTheory.LFun.LSD D (badPl R t) B (R.toLevCh.mu t j) ((1 + (D.R.t : ℂ)) / 2) = (l : ℂ)
```

</details>

<details><summary>Development/AbelianVarietyTheory/Proofs/TwistedOperators/LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift.lean, lines 350–350</summary>

[LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift 350–350](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift.lean#L350-L350)

```lean
theorem bForm : ∀ {D : D7} {G : Type} [Group G] [Fintype G] {Pl0 T : Type} {A : FamIn D.what₂.LL G Pl0 T D.R.m} {Ks : Type} [Field Ks] [NumberField Ks] [Algebra Ks D.what₂.LL] (R : RealDat D A Ks) (F : Face D A), GlobalTheory.Hk3.Core R F → GlobalTheory.Hk3.SchurAll R → GlobalTheory.IndefiniteRowSideFullHecke.LabelSettingScalars.Scalars R → Kept R → ∀ SF, GlobalTheory.Hk3.IsSF R SF → BForm R SF
```

</details>

<details><summary>Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaChainStepPositiveScalarStandingHypothesesStatement.lean, lines 26–26</summary>

[ThetaChainStepPositiveScalarStandingHypothesesStatement 26–26](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaChainStepPositiveScalarStandingHypothesesStatement.lean#L26-L26)

```lean
theorem _root_.GlobalTheory.T.thetaChainStep_positive_scalar_standingHypotheses : GlobalTheory.Published.DiscreteSeriesCover → GlobalTheory.Published.HarishChandraFinite → GlobalTheory.Published.HarishChandraModules → GlobalTheory.Published.CasselmanWallach → GlobalTheory.Published.CuspRapidDecay → GlobalTheory.Hk3.HoweUnram → GlobalTheory.Published.WeilSiegelFormulaUnitary → (∀ D' : Formalism.BasicNotions.D7, GlobalTheory.Core.Rk.SW.HeckeFormNS D') → GlobalTheory.Published.SiegelEisensteinContinuation → GlobalTheory.Published.UnramifiedDoublingGL → ∀ {D : D7} {G : Type} [Group G] [Fintype G] {Pl0 T : Type} {A : FamIn D.what₂.LL G Pl0 T D.R.m} {Ks : Type} [Field Ks] [NumberField Ks] [Algebra Ks D.what₂.LL] (R : RealDat D A Ks) (F : Face D A), Given R F → D.host.ccK = ⊤ → GlobalTheory.IndefiniteRowSideFullHecke.LabelSettingScalars.Scalars R
```

</details>

<details><summary>Development/AbelianVarietyTheory/Proofs/SatakeParameters/InertHeckeOperatorsLiftsRationalSelfAdjointLabelStatement.lean, lines 14–14</summary>

[InertHeckeOperatorsLiftsRationalSelfAdjointLabelStatement 14–14](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/InertHeckeOperatorsLiftsRationalSelfAdjointLabelStatement.lean#L14-L14)

```lean
theorem _root_.GlobalTheory.T.inertHeckeOperators_lifts_rational_selfAdjoint_labels : ∀ {D : D7} {G : Type} [Group G] [Fintype G] {Pl0 T : Type} {A : FamIn D.what₂.LL G Pl0 T D.R.m} {Ks : Type} [Field Ks] [NumberField Ks] [Algebra Ks D.what₂.LL] (R : RealDat D A Ks) (F : Face D A), R.toLevCh.Is A.μ0 → R.IsFam → R.IsModels → ∀ j t, ∀ (I : Type) (pl : I → Pl D.host.E) (ty : I → List ℤ) (op : I → Module.End D.what₂.LL (A.MtCSD j t).Forms) (inR : I → Prop), (∀ i, inR i → Good R t (pl i) ∧ conjPl (pl i) = pl i ∧ (ty i).Pairwise (fun a b => b ≤ a)) → Bridge.HeckeTie (Bridge.ratF (Vc D j)) (R.B.L j t).pres op inR (fun i => IsLabElt (Vc D j) (pl i) (ty i)) (fun i => IsLocElt (Vc D j) (pl i)) → ∀ i, inR i → (∀ a b, LinearMap.toMatrix (A.MtCSD j t).basis (A.MtCSD j t).basis (op i) a b ∈ cmMax D.what₂.LL) ∧ (∀ f g : (A.MtCSD j t).Forms, (A.MtCSD j t).csum ((op i f : (A.MtCSD j t).Forms) : (A.MtCSD j t).Cl → (A.MtCSD j t).V) (g : (A.MtCSD j t).Cl → (A.MtCSD j t).V) = (A.MtCSD j t).csum (f : (A.MtCSD j t).Cl → (A.MtCSD j t).V) ((op i g : (A.MtCSD j t).Forms) : (A.MtCSD j t).Cl → (A.MtCSD j t).V)) ∧ IsLab (Vc D j) (pl i) (ty i) ∧ ∀ h, IsOpsV R j t h → ∀ f, R.jV j t (op i f) = h (pl i) (Finsupp.single (ty i) 1) (R.jV j t f)
```

</details>

<details><summary>GroundTheory/AutomorphicForms/TraceFormulaCompact.lean, lines 112–135</summary>

[TraceFormulaCompact 112–135](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/GroundTheory/AutomorphicForms/TraceFormulaCompact.lean#L112-L135)

```lean
theorem traceFormula (f : CompactlySupportedContinuousMap G ℂ)
    (hf : IsTraceClass ((rightRegularRep Γ μ).integrated μ (UnitaryRep.ccToL1 μ f)))
    {s : Set (Submodule ℂ (Lp ℂ 2 (quotientMeasure Γ μ)))}
    [∀ V : s, CompleteSpace (V : Submodule ℂ (Lp ℂ 2 (quotientMeasure Γ μ)))]
    (hinv : ∀ V : s, (rightRegularRep Γ μ).IsInvariant V)
    (hsum : IsHilbertSum ℂ (fun V : s => (V : Submodule ℂ (Lp ℂ 2 (quotientMeasure Γ μ))))
      fun V => (V : Submodule ℂ (Lp ℂ 2 (quotientMeasure Γ μ))).subtypeₗᵢ)
    (hirr : ∀ V : s, ((rightRegularRep Γ μ).restrict V (hinv V)).IsIrreducible)
    (r : ConjClasses Γ → Γ) (hr : ∀ c, ConjClasses.mk (r c) = c)
    (ν : ∀ c : ConjClasses Γ, Measure (Subgroup.centralizer {((r c : Γ) : G)}))
    (hν : ∀ c, (ν c).IsHaarMeasure)
    (ρ : ∀ c : ConjClasses Γ, Measure (RightCosetSpace (Subgroup.centralizer {((r c : Γ) : G)})))
    (hρ : ∀ c, IsWeilMeasure (Subgroup.centralizer {((r c : Γ) : G)}) μ (ν c) (ρ c)) :
    HasSum (fun π : Quotient (UnitaryRep.restrictSetoid (rightRegularRep Γ μ) hinv) =>
        (UnitaryRep.multiplicity (rightRegularRep Γ μ) hinv π : ℂ) *
          trace (((rightRegularRep Γ μ).restrict π.out (hinv π.out)).integrated μ
            (UnitaryRep.ccToL1 μ f)))
      (trace ((rightRegularRep Γ μ).integrated μ (UnitaryRep.ccToL1 μ f))) ∧
    HasSum (fun c : ConjClasses Γ =>
        (quotientMeasure (centralizerLattice Γ ((r c : Γ) : G)) (ν c) univ).toReal •
          ∫ y, conjOrbitFun (Subgroup.centralizer {((r c : Γ) : G)}) le_rfl f y ∂ρ c)
      (trace ((rightRegularRep Γ μ).integrated μ (UnitaryRep.ccToL1 μ f))) ∧
    ∀ c, Integrable (conjOrbitFun (Subgroup.centralizer {((r c : Γ) : G)}) le_rfl f) (ρ c)
```

</details>

<details><summary>Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean, lines 173–176</summary>

[AdmissibleFamilyNoKernel 173–176](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L173-L176)

```lean
theorem chainK_zero {p : ℕ} {G : GAtP p} {Fl : Fills G} (Lv : Levels Fl) :
    ∀ m : ℕ, 1 ≤ m → ∀ F : Lv.Fm 0, (⟨fun _ => 0⟩ : Chain Lv).chainK m F = 0
  | 0, h, _ => absurd h (by omega)
  | n + 1, _, F => by simp [Chain.chainK]
```

</details>

<details><summary>Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean, lines 178–181</summary>

[AdmissibleFamilyNoKernel 178–181](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L178-L181)

```lean
theorem vKge_zero (Y : LatInst D) (hm : 1 ≤ D.R.m) (u : D.what₂.Word) (w : D.what₂.places.Pl)
    (hg : GIdx D.host (D.mem u).A.T (D.what₂.places.resChar w)) (F : (D.gat u w hg).Fn) (g : ℝ) :
    (zeroCh Y).vKge u w hg F g
```

</details>

<details><summary>Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean, lines 188–197</summary>

[AdmissibleFamilyNoKernel 188–197](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L188-L197)

```lean
theorem admissible_family_no_kernel {eps : ℝ} (Fm : FamP eps)
    (h1 : Adm1F Fm) (h2 : Adm2F Fm) (h3 : Adm3F Fm) (h4 : Adm4F Fm) (h5 : Adm5F Fm) (h6 : Adm6F Fm) (h7 : Adm7F Fm)
    (h8 : Adm8F Fm) (h9 : Adm9F Fm)
    (hE : Ev Fm fun x i => TrivialStabiliserFiniteClasses (Fm.D x i)) (hY : Ev Fm fun x i => OperatorsPreserveLattices (Fm.D x i))
    (hLP : Ev Fm fun x i => CornerGLContinuity.OrbitLatticeBounds (Fm.D x i) (Fm.L x i) (Fm.Gx x i) (Fm.Gy x i) Fm.GK)
    (hEp : Ev Fm fun x i => CornerGLContinuity.LatticeSandwich (Fm.D x i) (Fm.L x i) (Fm.Gx x i))
    (hd : NPDescF Fm) : AuxBlock8.AdmF Fm Fm.GK Fm.Gx (fun x i => zeroCh (Fm.Gy x i)) ∧
    Ev Fm fun x i => AuxBlock8.unitBoundAtTwistedPlaces (Fm.D x i) (Fm.L x i) (Fm.Gx x i) (zeroCh (Fm.Gy x i)) Fm.GK ∧
      AuxBlock8.admG1 (Fm.D x i) (Fm.L x i) (Fm.Gx x i) (zeroCh (Fm.Gy x i)) Fm.GK
```

</details>

<details><summary>Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean, lines 355–358</summary>

[IsResidueClassZero 355–358](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L355-L358)

```lean
def gainP (X : Inst D L) (K : Consts) (a b : HH D → ℤ) (p j : ℕ) : ℝ :=
  if (IsResidueClassZero D p ∧ hP D p = 0) ∨ L.sc.X'' D.R.n < (p : ℝ) then 0 else
    (∑ t0 ∈ VV X K a b p, max (gU X K a b p j t0 - Pr X K b p j t0) (max (g0 X K a b p j t0) 0)) +
    ∑ t0 ∈ reps X p \ VV X K a b p, max (g0 X K a b p j t0) 0
```

</details>

<details><summary>Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean, lines 401–410</summary>

[IsResidueClassZero 401–410](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L401-L410)

```lean
def ParametersFill (X : Inst D L) (K : Consts) (w : D.what₂.places.Pl) : Prop :=
  let p := D.what₂.places.resChar w
  (∀ j ∈ SizeData₂.lifts D, ∀ (τ : D.what₂.Tau) (z : Bool × HH D), (D.eTau τ : D.R.GG) = plGG D z →
    fill X (bL L) j z = wj D j τ) ∧
  (∀ j (t : D.host.TT) e, L.wPart j t p e = fill X (bL L) j (partner D p t e)) ∧
  (L.TTw w).map (Function.Embedding.subtype _) = TTP X K (aL L) (bL L) p ∧
  (w ∈ L.supp → (IsResidueClassZero D p ∨ IsSg D p) →
    ∀ j ∈ SizeData₂.lifts D, L.gain j w = gainP X K (aL L) (bL L) p j) ∧
  L.tau w = tauP X K (aL L) (bL L) p ∧ L.io w = ioP X K (aL L) (bL L) p ∧
  La K L.sc = L.LaG
```

</details>

<details><summary>Formalism/SharpRestriction/GrowthBounds/WeilJacquetShalikaLaw.lean, lines 552–554</summary>

[WeilJacquetShalikaLaw 552–554](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/WeilJacquetShalikaLaw.lean#L552-L554)

```lean
theorem gainD_le_gainS {X : Inst D L} {K : Consts} (hF : ∀ w, ParametersFill X K w)
    (hcs : ∀ p : ℕ, p.Prime → IsCs D p → p ∈ L.drop) (w : D.what₂.places.Pl) (j : ℕ)
    (hj : j ∈ SizeData₂.lifts D) : L.gainD j w ≤ gainS X K (D.what₂.places.resChar w) j
```

</details>

<details><summary>Formalism/SizeWindowBrackets/ChainSlopeWindows/ChainLatticeSizesModelEventually.lean, lines 2184–2199</summary>

[ChainLatticeSizesModelEventually 2184–2199](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/ChainLatticeSizesModelEventually.lean#L2184-L2199)

```lean
def lm_gn (D : ArithData H) (N : ℕ) (TT : Finset H) (a : H → ℝ) (w : Fin m → E0 × H → ℝ) (Xpp : ℝ) (j : Fin m)
    (p : ℕ) : ℝ :=
  if p ∈ inertPs D N ∧ (p : ℝ) ≤ Xpp then
    ∑ t ∈ TT, DeficitSplitLemmas.askAt ((Finset.Icc 1 N).filter (fun i => ¬ InPhi (i • D.frob p))) (a t) p
      (fun i => w j (partner t (i • D.frob p)))
  else 0

def lm_Lp (D : ArithData H) (N : ℕ) (TT : Finset H) (a : H → ℝ) (w : H → Fin m → E0 × H → ℝ) (P : PrimeWindowSizeBounds.Par)
    (u0 : H) : LossP H m where
  cl := fun p => if (p : ℝ) ≤ P.Xpp then DeficitSplitLemmas.PClass.served else DeficitSplitLemmas.PClass.high
  TTp := fun _ => TT
  gainP := lm_gn D N TT a (w u0) P.Xpp
  tauP := fun _ => 0
  lo := fun _ => 0
  fl := fun _ => 0
  L₁ := fun p => Real.logb p P.K₀ + 1
```

</details>

<details><summary>Formalism/ThetaLiftIndependence/Statement.lean, lines 237–251</summary>

[Statement 237–251](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L237-L251)

```lean
def RallisAdj : Prop :=
  ∀ (𝕜 E F P : Type) [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
    [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F]
    (θ : E →ₗ[𝕜] F) (S : Submodule 𝕜 E) (Pset : Finset P) (c L : 𝕜) (Z : P → 𝕜),
    RallisHyp θ S Pset c L Z → (∀ x ∈ S, LinearMap.adjoint θ (θ x) ∈ S) →
    ∀ x ∈ S, LinearMap.adjoint θ (θ x) = (c * L * ∏ v ∈ Pset, Z v) • x

def ChainScalar : Prop :=
  ∀ (𝕜 : Type) [RCLike 𝕜] (E : ℕ → Type) [∀ j, NormedAddCommGroup (E j)]
    [∀ j, InnerProductSpace 𝕜 (E j)] [∀ j, FiniteDimensional 𝕜 (E j)]
    (T : ∀ j, E (j + 1) →ₗ[𝕜] E j) (S : ∀ j, Submodule 𝕜 (E j)) (c : ℕ → 𝕜),
    (∀ j, ∀ x ∈ S j, T j (LinearMap.adjoint (T j) x) = c j • x) →
    (∀ j, ∀ x ∈ S j, LinearMap.adjoint (T j) x ∈ S (j + 1)) →
    ∀ (m : ℕ), ∀ x ∈ S 0,
      downChain T m (LinearMap.adjoint (downChain T m) x) = (∏ j ∈ Finset.range m, c j) • x
```

</details>

<details><summary>Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/CharpolySmulOfProd.lean, lines 398–405</summary>

[CharpolySmulOfProd 398–405](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/CharpolySmulOfProd.lean#L398-L405)

```lean
theorem IsTripleWith.charpoly_frob (ha : IsGlobalArtin art) (h : IsTripleWith C art ρ s σ π r ν w red) {P : PlE D.host}
    (hl : P ∉ placesOver D.host.E (X.l i)) (hg : ∀ k, P ∉ placesOver D.host.E (D.host.g k))
    {B : ValuationSubring D.nd.Om} (hB : IsPlaceOver B P) {g : GalE D} (hF : IsFrob (F := D.host.E) B (normV P) g) :
    ((X.rhoS i s g : GL (Fin D.R.r) (X.O0 i)) : Matrix (Fin D.R.r) (Fin D.R.r) (X.O0 i)).charpoly.map ρ.toC =
      ((D.naut.frobEig (D.naut.locG π P)).map fun a => Polynomial.X - Polynomial.C
        (a * ((normV P : ℕ) : ℂ) ^ (((1 - (D.R.r : ℝ)) / 2 : ℝ) : ℂ) * (((shiftChar C).val P : ℂˣ) : ℂ)⁻¹)).prod
```

</details>

<details><summary>Formalism/LandauZeroFreeBounds/ExceptionalZeroBounds/LRight.lean, lines 88–89</summary>

[LRight 88–89](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LandauZeroFreeBounds/ExceptionalZeroBounds/LRight.lean#L88-L89)

```lean
lemma negLD_eq_LSeries_mul_vonMangoldt {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ} (hs : 1 < s.re) :
    negLD χ s = L (↗χ * ↗Λ) s
```

</details>

<details><summary>Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/RallisInnerProductFormula.lean, lines 26–28</summary>

[RallisInnerProductFormula 26–28](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/RallisInnerProductFormula.lean#L26-L28)

```lean
def thetaLift (om : GA D V × GA D W →* Module.End ℂ (WO V W → ℂ)) (μG : Measure (GA D W)) (𝓕G : Set (GA D W))
    (φ : WO V W → ℂ) (f : GA D W → ℂ) : GA D V → ℂ :=
  fun h => ∫ g in 𝓕G, liftFun om φ f h g ∂μG
```

</details>

<details><summary>Formalism/ThetaLiftIndependence/Statement.lean, lines 148–150</summary>

[Statement 148–150](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/Statement.lean#L148-L150)

```lean
def thetaLift (h : V →ₗ⋆[K] V →ₗ[K] K) (s : Finset (Submodule (NumberField.RingOfIntegers K) V))
    (f : Submodule (NumberField.RingOfIntegers K) V → ℂ) (τ : ℂ) : ℂ :=
  latLift h s f (fun L => Formalism.HermitianLatticesTheory.thetaL h L 0 τ)
```

</details>

<details><summary>Formalism/SharpRestriction/GrowthBounds/DataGChain.lean, lines 77–87</summary>

[DataGChain 77–87](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/DataGChain.lean#L77-L87)

```lean
structure Chain {p : ℕ} {G : GAtP p} {Fl : Fills G} (Lv : Levels Fl) where
  Kz : ∀ j, Lv.Fm j →ₗ[G.Kf] Lv.Fm (j + 1)

namespace Chain

variable {p : ℕ} {G : GAtP p} {Fl : Fills G} {Lv : Levels Fl} (Ch : Chain Lv)

def chainK : (j : ℕ) → Lv.Fm 0 →ₗ[G.Kf] Lv.Fm j
  | 0 => LinearMap.id
  | j + 1 => (Ch.Kz j).comp (chainK j)
```

</details>

<details><summary>Formalism/ThetaLiftIndependence/ThetaOrbitSums/GaussOp.lean, lines 37–40</summary>

[GaussOp 37–40](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/GaussOp.lean#L37-L40)

```lean
theorem gaussOp_eq : GaussOp
```

</details>

<details><summary>Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRtensOp.lean, lines 62–67</summary>

[ExistsRtensOp 62–67](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRtensOp.lean#L62-L67)

```lean
def thetaLift {m k d : ℕ} {Y : GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.Spc D.host.F D.host.E m} {Z : GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.Spc D.host.F D.host.E k}
    (Mo : GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.Model D.sp.cm.sig Y Z) (ψ : AddChar (AF D.host.F) ℂ) (G : Matrix (Fin m) (Fin m) D.host.E)
    (e : Fin k ≃ Fin d) (S : Submodule ℂ ((Fin m × Fin k → AF D.host.F) → ℂ)) {P : Type} [AddCommGroup P] [Module ℂ P]
    (pD : ((Fin m × Fin k → AF D.host.F) → ℂ) →ₗ[ℂ] P) : (Matrix (Fin d) (Fin m) (AE D) → ℂ) →ₗ[ℂ] P :=
  if H : ∃ q : (Matrix (Fin d) (Fin m) (AE D) → ℂ) →ₗ[ℂ] P, ∀ Ψ ∈ S, q (GlobalTheory.TripleRead.thO Mo ψ G e Ψ) = pD Ψ
  then H.choose else 0
```

</details>

<details><summary>Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsRationalLocalOperators.lean, lines 44–46</summary>

[ExistsRationalLocalOperators 44–46](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsRationalLocalOperators.lean#L44-L46)

```lean
theorem trace_pow_of_charpoly {a : ℕ} (M : Matrix (Fin a) (Fin a) ℂ) (B : Multiset ℂ)
    (h : M.charpoly = (B.map fun b => X - C b).prod) (n : ℕ) : (M ^ n).trace = (B.map (· ^ n)).sum
```

</details>

<details><summary>Formalism/SharpRestriction/Divisibility/SchurIrreducible.lean, lines 489–496</summary>

[SchurIrreducible 489–496](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/SchurIrreducible.lean#L489-L496)

```lean
def Ith (ph : O.SchD) (g : O.GhQ) : ℂ := ∫ h, O.thetaD ph g h ∂O.muH

def thetaLift {π : O.Pi} (f : O.Vec π) (φ : O.Sch) (h : O.HQ) : ℂ :=
  ∫ g, star (O.form π f g) * O.thetaK φ g h ∂O.muG

def thetaIP {π : O.Pi} (f₁ f₂ : O.Vec π) (φ₁ φ₂ : O.Sch) : ℂ :=
  ∫ h, thetaLift O f₁ φ₁ h * star (thetaLift O f₂ φ₂ h) ∂O.muH
```

</details>

## Source locations

**READ.** Paths below are exact and relative to the pinned repository root. Each entry names the intersecting declarations or the structure supplying the quoted fields. The line links above identify the precise portions used.

- `src/Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/RallisInnerProductFormula.lean` — `GlobalTheory.IndefiniteRowSideFullHecke.RallisInnerProductFormula.prodFun`, `GlobalTheory.IndefiniteRowSideFullHecke.RallisInnerProductFormula.prodOn`, `GlobalTheory.IndefiniteRowSideFullHecke.RallisInnerProductFormula.liftFun`, `GlobalTheory.IndefiniteRowSideFullHecke.RallisInnerProductFormula.thetaLift`, `GlobalTheory.IndefiniteRowSideFullHecke.RallisInnerProductFormula.doublingFun`, `GlobalTheory.IndefiniteRowSideFullHecke.RallisInnerProductFormula.InnerProductFormula`, `GlobalTheory.IndefiniteRowSideFullHecke.RallisInnerProductFormula.RallisInnerProduct`.
- `src/Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/LabelSettingScalars.lean` — `GlobalTheory.IndefiniteRowSideFullHecke.LabelSettingScalars.IsLValue`.
- `src/Development/AbelianVarietyTheory/Definitions/GaloisGeometry/NormalFam.lean` — `GlobalTheory.Hk3.EEc`, `GlobalTheory.Hk3.Wcc`.
- `src/Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/CharpolySmulOfProd.lean` — `GlobalTheory.Triple.IsTripleWith.charpoly_frob`.
- `src/Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean` — `GlobalTheory.LiftRows.Given`, `GlobalTheory.LiftRows.IsLval`, `GlobalTheory.LiftRows.AForm`, `GlobalTheory.LiftRows.BForm`.
- `src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaChainStepPositiveScalarStandingHypothesesStatement.lean` — `GlobalTheory.T.thetaChainStep_positive_scalar_standingHypotheses`.
- `src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftChainScalar.lean` — `GlobalTheory.Fam.LiftVol.lift_eq_cI_io`.
- `src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/PeterssonNormHeckeProduct.lean` — `GlobalTheory.RallisBottom.normBig_innerProduct`.
- `src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LogDerivRiemannZetaLocalZeroSum.lean` — `GlobalTheory.ZetaLocal.logDeriv_riemannZeta_local`.
- `src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsRationalLocalOperators.lean` — `GlobalTheory.FrobOps.trace_pow_of_charpoly`, `GlobalTheory.FrobOps.iota_trc`.
- `src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/InertHeckeOperatorsLiftsRationalSelfAdjointLabelStatement.lean` — `GlobalTheory.T.inertHeckeOperators_lifts_rational_selfAdjoint_labels`.
- `src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/InertHeckeOperatorsRowsRationalSelfAdjointLabelsStatement.lean` — `GlobalTheory.T.inertHeckeOperators_rows_rational_selfAdjoint_labels`.
- `src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRtensOp.lean` — `GlobalTheory.TripleAssembly.thetaLift`.
- `src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/LevelGroupActionOnAdelicFunctionsEqZeroOfNoLift.lean` — `GlobalTheory.ChainScalar.bForm`.
- `src/Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean` — `UpperTheory.EveryCharacter`.
- `src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean` — `UpperTheory.FinalTheorems.everyCharacter_of_row`, `UpperTheory.FinalTheorems.everyCharacter`.
- `src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiModOne.lean` — `Deduction.mellin_Gchi_modOne`.
- `src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean` — `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin`.
- `src/Formalism/GammaFactorNonvanishing/CritLine.lean` — `Formalism.VW.rh_of_every`.
- `src/Formalism/HermitianLattices/StatementTheta.lean` — `Formalism.HermitianLatticesTheory.weilT`, `Formalism.HermitianLatticesTheory.weilS`, `Formalism.HermitianLatticesTheory.thetaL`, `Formalism.HermitianLatticesTheory.thetaN`.
- `src/Formalism/LandauZeroFreeBounds/ExceptionalZeroBounds/LRight.lean` — `Formalism.ZeroFreeDirichlet.negLD_eq_LSeries_mul_vonMangoldt`.
- `src/Formalism/LocalToGlobal/GlobalTheory/IsResidueClassZero.lean` — `Formalism.L2.GlobalTheoryTheory.Arith.Loc.Sig`, `Formalism.L2.GlobalTheoryTheory.Arith.Loc.VV`, `Formalism.L2.GlobalTheoryTheory.Arith.Loc.Sv`, `Formalism.L2.GlobalTheoryTheory.Arith.Loc.tauP`, `Formalism.L2.GlobalTheoryTheory.Arith.Loc.ioP`, `Formalism.L2.GlobalTheoryTheory.Arith.Loc.gainP`, `Formalism.L2.GlobalTheoryTheory.Arith.Loc.TTP`, `Formalism.L2.GlobalTheoryTheory.Arith.Loc.askG`.
- `src/Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean` — `Formalism.L2.G.zeroCh`, `Formalism.L2.G.chainK_zero`, `Formalism.L2.G.vKge_zero`, `Formalism.L2.G.admissible_family_no_kernel`, `Formalism.L2.G.linkG_without_kernels`.
- `src/Formalism/LocalToGlobal/IndefiniteReal/LinksDefs.lean` — `Formalism.IndefR.Links.HMod`, `Formalism.IndefR.Links.RealDat`.
- `src/Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean` — `Formalism.IndefR.Datum.IsWeilDatumO`, `Formalism.IndefR.Datum.thetaKO`.
- `src/Formalism/SharpRestriction/Divisibility/SchurIrreducible.lean` — `Formalism.MainNotions.SchurIrreducible.Ith`, `Formalism.MainNotions.SchurIrreducible.thetaLift`, `Formalism.MainNotions.SchurIrreducible.thetaIP`, `Formalism.MainNotions.SchurIrreducible.ZS`, `Formalism.MainNotions.SchurIrreducible.LS`, `Formalism.MainNotions.SchurIrreducible.RFconcl`.
- `src/Formalism/SharpRestriction/Divisibility/WeightDegreeSizes.lean` — `Formalism.MainNotions.WeightDegreeSizes.gainP_nonneg`, `Formalism.MainNotions.WeightDegreeSizes.gainS_nonneg`, `Formalism.MainNotions.WeightDegreeSizes.gainLe_of_fills`.
- `src/Formalism/SharpRestriction/Divisibility/ZetaProductPairs.lean` — `Formalism.MainNotions.ZetaProductPairs.vth`, `Formalism.MainNotions.ZetaProductPairs.LiftChain`, `Formalism.MainNotions.ZetaProductPairs.InChain`.
- `src/Formalism/SharpRestriction/GrowthBounds/DataGChain.lean` — `Formalism.MainNotions.G.Levels.comp`, `Formalism.MainNotions.G.Levels.lev`, `Formalism.MainNotions.G.Levels.Fm`, `Formalism.MainNotions.G.Levels.Int`, `Formalism.MainNotions.G.Levels.Tm`, `Formalism.MainNotions.G.Chain`, `Formalism.MainNotions.G.Chain.chainK`.
- `src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean` — `Formalism.MainNotions.G.hG`, `Formalism.MainNotions.G.KG`, `Formalism.MainNotions.G.rG`, `Formalism.MainNotions.G.N1`, `Formalism.MainNotions.G.cG`, `Formalism.MainNotions.G.Nm`, `Formalism.MainNotions.G.L1`, `Formalism.MainNotions.G.L2`, `Formalism.MainNotions.G.Nstar`, `Formalism.MainNotions.G.La`, `Formalism.MainNotions.G.rho`, `Formalism.MainNotions.G.rhoB`, `Formalism.MainNotions.G.InBand`, `Formalism.MainNotions.G.gam`, `Formalism.MainNotions.G.frobSet`, `Formalism.MainNotions.G.hP`, `Formalism.MainNotions.G.IsResidueClassZero`, `Formalism.MainNotions.G.IsSg`, `Formalism.MainNotions.G.HEv`, `Formalism.MainNotions.G.IsCs`, `Formalism.MainNotions.G.partner`, `Formalism.MainNotions.G.IsThinPl`, `Formalism.MainNotions.G.Inst`, `Formalism.MainNotions.G.fill`, `Formalism.MainNotions.G.kaJ`, `Formalism.MainNotions.G.fillG`, `Formalism.MainNotions.G.stepP`, `Formalism.MainNotions.G.nP`, `Formalism.MainNotions.G.reps`, `Formalism.MainNotions.G.topsOn`, `Formalism.MainNotions.G.Nv`, `Formalism.MainNotions.G.topsPos`, `Formalism.MainNotions.G.wPos`, `Formalism.MainNotions.G.IsV`, `Formalism.MainNotions.G.Good`, `Formalism.MainNotions.G.NplusF`, `Formalism.MainNotions.G.DIIf`, `Formalism.MainNotions.G.DIf`, `Formalism.MainNotions.G.tIIf`, `Formalism.MainNotions.G.kapIIf`, `Formalism.MainNotions.G.tIf`, `Formalism.MainNotions.G.kapLoc`, `Formalism.MainNotions.G.al`, `Formalism.MainNotions.G.capU`, `Formalism.MainNotions.G.IsDist`, `Formalism.MainNotions.G.Excl`, `Formalism.MainNotions.G.dl`, `Formalism.MainNotions.G.g0`, `Formalism.MainNotions.G.gU`, `Formalism.MainNotions.G.Pr`, `Formalism.MainNotions.G.Dp`, `Formalism.MainNotions.G.tv`, `Formalism.MainNotions.G.kapv`, `Formalism.MainNotions.G.Cand`, `Formalism.MainNotions.G.goodReps`, `Formalism.MainNotions.G.Sig`, `Formalism.MainNotions.G.VV`, `Formalism.MainNotions.G.ServedOrbitsContained`, `Formalism.MainNotions.G.served_orbits_in_set`, `Formalism.MainNotions.G.winA`, `Formalism.MainNotions.G.gainP`, `Formalism.MainNotions.G.TTP`, `Formalism.MainNotions.G.askG`, `Formalism.MainNotions.G.ParametersFill`, `Formalism.MainNotions.G.vUnit`, `Formalism.MainNotions.G.vGeLat`, `Formalism.MainNotions.G.LatInst`, `Formalism.MainNotions.G.LatInst.vKge`.
- `src/Formalism/SharpRestriction/GrowthBounds/WeilJacquetShalikaLaw.lean` — `Formalism.MainNotions.WeilJacquetShalikaLaw.pair_gain_nonneg`, `Formalism.MainNotions.WeilJacquetShalikaLaw.served_gain_nonneg`, `Formalism.MainNotions.WeilJacquetShalikaLaw.gainD_le_gainS`.
- `src/Formalism/SharpRestriction/InertJacobiLevels/TieTTwValsOfMem.lean` — `Formalism.MainNotions.Inhab.tie_gainTot_below`, `Formalism.MainNotions.Inhab.gainP_eq_zero_of_lt`.
- `src/Formalism/SharpRestriction/InertJacobiLevels/TiesCore.lean` — `Formalism.MainNotions.Inhab.GC.gainP`.
- `src/Formalism/SharpRestriction/InertJacobiLevels/TiesView.lean` — `Formalism.MainNotions.Inhab.VV_view`, `Formalism.MainNotions.Inhab.TTP_view`, `Formalism.MainNotions.Inhab.tauP_view`, `Formalism.MainNotions.Inhab.ioP_viewX`, `Formalism.MainNotions.Inhab.gainP_eq_gainP_viewX`.
- `src/Formalism/SizeWindowBrackets/Chain2aCoreNoAnalytic.lean` — `Formalism.LFunctionChainParameters.LChain2.LossP`.
- `src/Formalism/SizeWindowBrackets/ChainSlopeWindows/ChainLatticeSizesModelEventually.lean` — `Formalism.LFunctionChainParameters.LChain2.log_derivative_identity`, `Formalism.LFunctionChainParameters.LChain2.losses_of_window`, `Formalism.LFunctionChainParameters.LChain2.lm_gn`, `Formalism.LFunctionChainParameters.LChain2.lm_Lp`.
- `src/Formalism/SizeWindowBrackets/FirstPrimeNeSecondPrime.lean` — `Formalism.LFunctionChainParameters.characterSumData.cosetMean`, `Formalism.LFunctionChainParameters.characterSumData.primVal`, `Formalism.LFunctionChainParameters.characterSumData.GPsi`, `Formalism.LFunctionChainParameters.characterSumData.IsInert`, `Formalism.LFunctionChainParameters.characterSumData.askP`, `Formalism.LFunctionChainParameters.characterSumData.askD`, `Formalism.LFunctionChainParameters.characterSumData.ASK`, `Formalism.LFunctionChainParameters.characterSumData.MAIN`.
- `src/Formalism/SizeWindowBrackets/SecondKindBucket.lean` — `Formalism.LFunctionChainParameters.DeficitSplitLemmas.askAt`.
- `src/Formalism/ThetaLiftIndependence/Statement.lean` — `Formalism.ThetaLiftIndependence.kerOp`, `Formalism.ThetaLiftIndependence.kerMul`, `Formalism.ThetaLiftIndependence.wip`, `Formalism.ThetaLiftIndependence.kerAdj`, `Formalism.ThetaLiftIndependence.chainOp`, `Formalism.ThetaLiftIndependence.KerAdjoint`, `Formalism.ThetaLiftIndependence.KerComp`, `Formalism.ThetaLiftIndependence.ChainInt`, `Formalism.ThetaLiftIndependence.autL`, `Formalism.ThetaLiftIndependence.latWt`, `Formalism.ThetaLiftIndependence.IsClassReps`, `Formalism.ThetaLiftIndependence.latLift`, `Formalism.ThetaLiftIndependence.thetaLift`, `Formalism.ThetaLiftIndependence.latIp`, `Formalism.ThetaLiftIndependence.LatSeeSaw`, `Formalism.ThetaLiftIndependence.gaussOp`, `Formalism.ThetaLiftIndependence.gaussOpDual`, `Formalism.ThetaLiftIndependence.GaussOp`, `Formalism.ThetaLiftIndependence.RallisHyp`, `Formalism.ThetaLiftIndependence.RallisAdj`, `Formalism.ThetaLiftIndependence.ChainScalar`, `Formalism.ThetaLiftIndependence.DetSwap`, `Formalism.ThetaLiftIndependence.EigenSwap`.
- `src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/ChainScalar.lean` — `Formalism.ThetaLiftIndependence.ChainScalarLemmas.adjoint_downChain_succ_apply`, `Formalism.ThetaLiftIndependence.ChainScalarLemmas.mem`.
- `src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/EigenSwap.lean` — `Formalism.ThetaLiftIndependence.EigenvalueSwapLemmas.eig_le`.
- `src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/GaussOp.lean` — `Formalism.ThetaLiftIndependence.gaussOp_eq`.
- `src/Formalism/ThetaLiftIndependence/ThetaOrbitSums/LatLiftIndep.lean` — `Formalism.ThetaLiftIndependence.latLiftIndep`.
- `src/GroundTheory/AutomorphicForms/TraceFormulaCompact.lean` — `GroundTheory.Automorphic.RightCosetSpace.hasSum_orbitalIntegral_of_rep`, `GroundTheory.Automorphic.RightCosetSpace.traceFormula`.
- `src/Supplements/Kernels/MainTheorems.lean` — `allChi`, `rhOfAll`, `critAll`, `claimAll`.
