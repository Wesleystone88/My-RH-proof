# RH proof investigation — complete VS Code handoff

## Start here

Read this file as the project context. The goal is to extract a short, human-readable explanation of what excludes an off-line zeta zero in Alpöge’s Lean formalization. We want to identify the functions and inequalities doing the work, show where their hypotheses come from, and eventually compile a small Lean extraction.

Repository: https://github.com/Deicyde/riemann-hypothesis
Pinned commit: e50d09817ad81469f737e8f637561e6ccf86c670
Source root: https://github.com/Deicyde/riemann-hypothesis/tree/e50d09817ad81469f737e8f637561e6ccf86c670/src
Toolchain reported for this commit: Lean v4.33.1
Mathlib commit: 0df444a360eaa60ab8c11dca51a86af692955474
Published verification: https://math.mit.edu/~drew/grh/
Headline axiom audit: https://math.mit.edu/~drew/grh/audit.log

Evidence status: We read pinned Lean declarations and proof bodies and independently reconstructed several calculations on paper. We have not compiled our own extraction or independently proved every upstream input. The published verification concerns the original formalization.

## 1. What function detects the zeros?

For x ≥ 1, let Λ(p^j) = log p for every prime power p^j, and let Λ vanish elsewhere. Write γ for Euler’s constant. The ordinary zeta component is

    Gζ(x) = Σ_{n≤x} Λ(n)(x/n − 1) − x log x + (1+γ)x.

Every prime power q switches on a linear ramp x/q − 1 at x=q. The reason for this weight can be checked on one term. For Re(s)>1,

    ∫[q,∞) (x/q − 1)x^(−s−1) dx = q^(−s)/[s(s−1)].

Sum over prime powers. The Euler product turns the transform of the ramp sum into

    −(ζ′/ζ)(s)/[s(s−1)].

The smooth correction terms contribute rational functions with a possible pole at 1. A nontrivial zero ρ of multiplicity h gives the continued transform a pole of residue −h/[ρ(ρ−1)]. This explains how primes encode the zero. Getting enough control inside the critical strip is the substantive issue.

Source: src/Formalism/StatementOC.lean, lines 11–13.

## 2. Which route reaches the headline theorem?

    Main.riemannHypothesis
    → rhOfAll
    → rh_of_every allChi
    → ordinary zeta by the modulus-one trivial character.

Right-side nonvanishing excludes zeros with Re(s)>1/2. The functional equation reflects a hypothetical zero on the left to the right.

The arithmetic route uses plugWin with window power 3/2, then zeroFreeAll_of_topG and level_of_tiedWin. The analytic input FormB goes through zeroFree_of_rpow_window → lemmaL → poleData and landau_window.

Correction to an earlier trace: landau_entire in Landau.lean belongs to an alternative using a bound for all sufficiently large x. Its real-zero contradiction 0 ≤ h/[β(β−1)] < 0 is readable, but the headline route uses the window argument below.

## 3. How a good window excludes a zero

A good window controls G(x) ≤ C x^θ for EVERY x in [Y,Y^(1+δ)]. Such windows must occur arbitrarily far out. The bound is one-sided. On each window its nonnegative majorant costs

    ∫[Y,Y^(1+δ)] |C| y^θ y^(−θ−1) dy = |C|δ log Y ≤ Y^η

for every fixed η>0 once Y is sufficiently large.

Why can this exclude a complex pole? For f(z)=1/(z−ρ), at distance d from the pole,

    |f^(k)(z)|/k! = d^(−k−1).

High derivatives distinguish nearby poles from more distant contributions. After isolating a pole and controlling tails, the Lean argument reduces the conflict to

    c/d^k ≤ M/r^k + C exp(ηU)/R^k,
    where c>0, 0<d<r≤R, U=log Y, and k≥U.

Multiply by d^k. Choose 0<η<log(r/d). The right side is at most

    |M|(d/r)^k + |C|[exp(η)d/r]^k → 0,

while c stays positive. This is the short contradiction at the end of the actual window argument. It works for any admissible θ. Arithmetic supplies how close θ gets to 1/2.

## 4. Where the arithmetic enters

The window consumer uses

    Gm(x) ≤ x^[1/2+(eD+eL+7)ε].

The constants eD,eL and ε₁ are fixed before ε. Given a putative zero with real part β>1/2, put Δ=min(β−1/2,1/2). Choose 0<ε<ε₁ with (eD+eL+7)ε≤Δ/2. Then θ=1/2+Δ/2<β. The family, windows and starting threshold may depend on ε.

For ordinary zeta the kept set contains just the trivial character and Gm=Gζ. Internally the calculation still controls three auxiliary characters. The two square-root estimates below do different jobs.

## 5. First square root: balancing the design errors

Write n for the ambient group size, nT and nT2 for two subset sizes, m for the design parameter, Q=nT·m·b and L=Q(nT2/n)/2. The scalar input is

    L(G−4x^(1/2+ε)) ≤ Err + 2Q/x.

Before the common multiplier x^(Cε), the error bracket is

    nT·aE·(1+m²/k) + 2n·m²·b·x^ε + m·nT2·k·b·x^(2ε)/n².

The relevant conditions include aE≤2xb, nT≥n x^(−ε/8)/2,
nT2/n≥x^(−ε), x^(1/2−ε)≤m≤x^(1/2+ε/2), xm≤k, and
k≤n²x^(1/2−ε).

After division by L:

| Piece | Upper estimate before x^(Cε) | Main scale |
|---|---|---|
| aE term | 4x^(1+ε)(1+m²/k)/m | x/m |
| m² term | 8m x^(17ε/8) | m |
| k term | 4(k/n²)x^(17ε/8) | k/n² |

Put m=x^u and momentarily suppress ε losses. The first two powers are 1−u and u. Their maximum is minimized at u=1/2. The k term has its own cap. This explains the choice √x within this error estimate. It gives an upper bound, not a lower bound on the true error.

The proof body proposition_size_bound splits the error into four terms, obtaining

    Err ≤ 10Q x^(Cε) x^(1/2+13ε/8).

Removing the density factor costs x^ε. The assumption 26≤x^(3ε/8) absorbs constants, producing G≤x^[1/2+(C+3)ε]. On the headline route ch_core applies this scalar estimate after subtracting SigA.

The admissible-rank construction takes δ₁=x^(−ε/8), A=√(xδ₁), and m=2⌈A/2⌉. Thus A≤m≤2A. Claude found a parallel PChain witness m=⌈A⌉ at the same scale. Preserve the distinction between the two constructions. The quarter-power split in ch_core absorbs a logarithm and a constant. In the zeta-only explicit inequality moveCost=Cd+3[log(x+1)+Cd+CL log x], which grows logarithmically for fixed Cd,CL.

## 6. Why three characters remain

At the trivial target the cyclic subgroup has order o=1. The source gives |PsiA|=4o=4. The kept characters map injectively onto the singleton KEPT, and the trivial character belongs to PsiA. Hence three indices are omitted. This exact count is a source-based deduction that remains to be compiled separately.

On integers coprime to the modulus, the three twists are

    (a/q),    (a/d),    (a/q)(a/d),

where the parentheses denote Jacobi symbols and q,d are selected primes. The theorem tracks the associated primitive characters.

PairGood.bounds supplies |gχ(y)|≤y^(1/2+ε/2) and
|L′(1,χ)/L(1,χ)|≤4 log y throughout the same interval. boundedTw passes the first bound to EAtH.bdG with ε allowance. sigA_le sums the omitted terms. The source uses the coarse count 4o.

pair_share first leaves a nonempty set of good q, then for each good q leaves a nonempty set of compatible d. pair_exists takes an excluded fraction of 1/2 to get nonemptiness. That fraction is unrelated to the exponent 1/2 on y. The selected pair may change with scale.

## 7. Second square root: the mean square of prime twists

Define

    c(y,n) = Λ(n) min(1,y/n),
    S_q(y) = Σ_{n≤Z} c(y,n) κ(n) (n/q),   |κ(n)|≤1.

For the admitted family P of primes, meanSqK proves uniformly for y∈[Y,Y^K]

    Σ_{q∈P} |S_q(y)|² ≤ C y log(y) |P|.

Here is the exponent calculation. If a fraction f of P exceeds y^a/2 at a fixed y, those primes alone contribute at least f|P|y^(2a)/4. Thus

    f ≤ 4C y^(1−2a) log y.

Every a>1/2 gives decay. With a=1/2+τ the bound is
4C y^(−2τ)log y. At τ=0 this argument gives no decay. This is an upper estimate, not a variance asymptotic.

### Which cross terms survive?

Large q does not make distinct prime powers orthogonal. For every odd prime q, (8/q)=(2/q), and both 8 and 2 have positive Mangoldt weight.

MeanSqAbs expands the square and groups pairs n,n′ by the squarefree part of nn′ outside the progression modulus. It handles the trivial class and one possible exceptional class separately. twistK supplies small correlations for the other admissible classes. It uses a prime-counting estimate in progressions and page_across.

sPsq_le bounds the sum of squared grouped prime weights by C y log y. RR_le controls the even prime powers and the powers of primes dividing the progression modulus. In the application their total weight is O(√y), whose square is O(y). These estimates explain how actual correlations fit within the budget.

### How the bound holds across an entire interval

A bad prime can have its own bad point y_q. BadShare.bs_block allows a different y_q∈[Y,2Y] for every q and still proves

    Σ_{q∈P}|S_q(y_q)|² ≤ 4C Y log(2Y) |P|.

It uses an integrated derivative estimate to control variation inside the block. Only then do bs_markov and bad_share sum across dyadic blocks. Their excluded fraction is bounded by

    (32C/τ) Y^(−τ) / (1−2^(−τ)).

This tends to zero for fixed τ>0. The starting threshold depends on τ. The call producing PairGood uses τ=ε/2.

### From S back to the arithmetic observable

With Z=(Y^K)^400 and the characters matched, BoxOfS uses

    Gχ(y) = −S_q(y) − y·tailLχ(Z).

The finite sum costs at most half the allowed threshold. tailK bounds the remaining contribution by Y^ε, small enough for the other half in the specified range. kappaC supplies the logarithmic derivative estimate. The zero-free-box condition and the count_bad_core bound for its exceptions remain additional analytic inputs.

## 8. How the estimates land on the same window

winPairs uses PairEx and VWinAt to obtain arbitrarily late intervals [Z,Z^(3/2)]. FamilyClassConnected supplies one family with the class condition and ChainTied on its late window points. At a given x on such a window the design supplies an index i. The host estimate holds for every eligible i at that x. windowInequality_of_artinInputs applies it to the same i. This explains the alignment. The deeper theorems supplying those hypotheses still matter to a full proof.

## 9. Primary source map

Paths are relative to src/ at the pinned commit. A filename without a line number denotes the named declaration or file. Use local search for exact current positions.

- Main.lean:4; Supplements/Kernels/MainTheorems.lean:7–9; Formalism/GammaFactorNonvanishing/{CritLine,RhOfRight}.lean — RH entry and reflection.
- Formalism/StatementOC.lean:11–13 — Gζ and Sz.
- Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/{Window,TopWin,ExplicitFormulaErrorOfHostConditions,Analytic}.lean — window quantifiers, cyclic level, Gm and bdG. Landau.lean:115 is the eventual-bound alternative.
- Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/{WindowHypOfRpow,lemmaL,poleData,landauWindow}.lean — actual window contradiction. ChCore.lean:343 — character balance and scalar estimate.
- Formalism/SizeWindowBrackets/GrowthBoundGivesRiemannHypothesis.lean:76–122 and ChainSlopeWindows/LipschitzWeightAndMinimum.lean:507 onward in the same directory — moveCost, size assumptions and proof body.
- Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsRanksRankValFrame.lean — even rank construction. PChain.lean:1603 and SChain.lean:214 are the parallel plain-ceiling locations reported by Claude.
- Development/AutomorphicArithmetic/PrimitiveCosets/{CardPsiA,GmAEq,SigALe,CoreGm,WindowInequalityOfArtinInputs}.lean — kept/omitted characters and aligned estimates.
- Development/AutomorphicArithmetic/CharacterBoxes/{PairGood,BoundedTw,WinPairs,SupplyChi,EveryCharacter,ZeroFreeAllOfTopG,DivinNOfHypV}.lean and Development/AutomorphicArithmetic/ShortNorms/supplyOfAdmOf.lean — twist definitions, family supply and actual bdG assignment.
- Development/AutomorphicArithmetic/MeanSquareBounds/{PrimeSetTwoBounds,StagePow,Stage1Succ,PairShare,PairExists,pairEx}.lean — candidate families and selection.
- In that same MeanSquareBounds directory: meanSqK.lean:51 onward, MeanSqAbs.lean:8 onward, SPsqLe.lean:161, RRLe.lean:9, twistK.lean:148 onward, BadShare.lean:164 onward, BoxOfS.lean:28, CountBad.lean:9.
- Formalism/GL3MeanSquares/SecondEstimateOfIntervalHypothesis.lean:23 — coefficient cN.

Comparison only: the separate 7/8 formalization is documented at
https://github.com/openai/math/blob/main/lean/docs/003.md .
The readable guide at https://www.math.uwaterloo.ca/~mrubinst/quasi_rh_notes/zeta_7_8_guide.pdf exposes the crossing β−11/16 > 3/16. Masullo’s trace-formula manuscript is a separate proposed route, with no established dependency in this reconstruction.

## 10. Next task for Codex in VS Code

Continue from the source pin above. Start at QH.twistK in twistK.lean near line 148. Follow pnt_progressions_relative_weak_holds, page_across, and excBound. Explain why at most one exceptional squarefree class needs separate treatment in the simultaneous correlation estimate. Then trace pairs_r inside meanSq_abs and show how that exceptional class’s contribution fits within C y log y. Give the actual inequalities, identify the variables and quantifiers, and cite the pinned declarations. Keep zero-density counting in count_bad_core separate from this exception.

For each result, record whether it was read in source, derived on paper, or compiled. Update this same Markdown file. If compiling a compact Lean lemma is feasible, record its exact imports, hypotheses, command, result and axiom output. The longer-term task is to reconstruct the upstream arithmetic and growth inequality sufficiently well that a human can check the main argument without reading the whole repository.






I'll check the second reader's claims against the source, then follow the next lead (`twistK` and its exception handling).

I checked the second reader's note against the source and it holds up. I also followed the next lead (`twistK`), and the result is clean: the 1/2 on the character side comes from a mean-square budget, and every input to it is a classical theorem about zeros near Re s = 1, never near 1/2. So the hard part of the proof is not on the character side. It sits in one bridge step, identified below. Nothing was compiled (Lean still isn't available here); everything is from reading the pinned source.

## The picture

Think of one radio per huge prime q, each playing static: the twisted prime sum S_q(y). The source proves the total static power across all the radios averages out to about y·log y per radio. Power is loudness squared. If more than a tiny fraction of radios were louder than y^a, their power alone would blow the budget unless 2a > 1. So almost every radio is quiet at the √y level, and the proof picks a quiet pair q, d.

The open question is how a few quiet radios make the zeta radio quiet. That bridge is the next target.

## Checks on the second reader's note

| Claim | Status | Where |
|---|---|---|
| Distinct prime powers can give the same twist, e.g. (8/q) = (2/q) | Correct. The source groups pairs (n, n′) by `soutPart m₀ (n·n′)`, the squarefree part of n·n′ with primes dividing m₀ removed (8 divides m₀). Pairs like (2, 8) fall into the trivial class, paid for by the sP² and RR² terms. | `meanSq_abs`, MeanSqAbs.lean:8-16; definitions at MeanSquareHypWIff.lean:48, 51, 54 |
| One possible exceptional class `nstar` | Confirmed | MeanSqAbs.lean:12-13 |
| Each q may pick its own y_q in [Y, 2Y] and the bound still holds | Confirmed: Σ‖S(y_q)‖² ≤ 4CY·log(2Y)·\|P\| | `bs_block`, BadShare.lean:163-166 |
| Gχ(y) = −S_q(y) − y·tailL, with the tail ≤ Y^ε | Confirmed | BoxOfS.lean:44-62 |
| Bad fraction f ≤ 4C·y^(1−2a)·log y | Correct algebra from the `MeanSq` definition (PrimeSetTwoBounds.lean:26-27) | Hand-derived |

This also corrects my last addendum. I wrote that the diagonal is just Σ Λ(n)²·min(1, y/n)². It isn't, because identical twists survive averaging. The grouped form above is what the source actually bounds.

## New: what makes the off-diagonal terms small (`twistK`)

`twistK` (MeanSquareBounds/twistK.lean:148-151) says: for any ε, A, B > 0 and Y large enough, there is at most one exceptional nstar such that for every other odd squarefree s with 1 < s ≤ Y^A (coprime to m₀),

|Σ_{q∈P} (q/s)| ≤ Y^(−B)·|P|.

**Why q is chosen so huge.** This replaces my earlier guess. The family P consists of primes q up to U with log U ≥ Y^(ε/6). So every modulus s ≤ Y^A is at most a power of log U. That is the Siegel–Walfisz range, where the prime number theorem in progressions applies with error exp(−c·log U / log s), smaller than any power of Y. This is my reconstruction from the hypotheses `admitted.lo` and `PNTAPRelW`, not something stated in a single line.

`twistK` relies on four classical theorems, each formalized in the repo:

| Input | Plain statement | Proved at |
|---|---|---|
| `PNTAPRelW` | Primes in progressions follow li(X)/φ(M), plus at most one exceptional-zero term | PNTFinal.lean:22 (definition at MeanSquareHypWIff.lean:38) |
| `ZFRDirichlet` | De la Vallée Poussin zero-free region, with at most one real exceptional zero | LandauZeroFreeBounds/NoZeroComplex.lean:32 |
| `ExcBound` | Siegel: an exceptional zero satisfies β ≤ 1 − c·q^(−ε) | SiegelWalfiszAPOfSiegelLower.lean:32 |
| `page_across` | Page: at most one exceptional modulus in a range | MSqPage.lean:37 |

`count_bad_core` (CountBadCore.lean:18) uses `ZeroDensityBox` (proved at CountZAll.lean:13 via mollifier, zero detection and a duality inequality). It says the number of primitive characters of conductor ≤ Q with a zero at Re s > 1 − 1/400, |Im s| ≤ Q is at most C·Q^(1/4).

None of these mentions 1/2, and all of them concern zeros close to Re s = 1. So the character side is not circular. The audit's axiom list (no `sorryAx`) suggests these are all fully proved, but only if the audit was run on this exact commit. I did not check that link.

## Where the remaining weight sits

Bounds of this mean-square kind are known to give square-root cancellation for most members of a family, not for one fixed L-function. So if the proof gets RH for ζ itself, the new content must be in the step that moves the bound from the quiet twists to ζ. In the source that step is the following:

- **The bridge inequality**, `hY` in `ch_core` (ChCore.lean:427): |TT|·(G − 4x^(1/2+ε)) ≤ Σ_{t∈TT} Re Σ_{ψ∈PsiA} ψ(e1 t)·GPsi(ψ, a_t/b), with G = GmA − SigA. That is, the zeta sum minus the auxiliary-character sums is controlled by an average of character-weighted sums over a finite set TT.
- **The hypothesis that pays for the right side**, `ch_core` line 350: for every u ∈ A0, gapA(u) ≤ x^(Cε)·errorBracketSizeWindows(…). This is the same three-term bracket where m ≈ √x balances.
- **What gapA measures** (DedekindLFunctions/SplitInertia.lean:50): gapA(u) = Σ_{t∈TT} Σ_j (ASK(a_t, t, w_{u,j}) − Re MAIN(a_t, w_{u,j})). That is "an arithmetic count minus its main term".

I have not opened ASK, MAIN, or the theorem that supplies the gapA bound (it arrives through `ChainTied` / `FamilyClassConnected`). That is where I'd look next.

## Copyable addendum

```
ADDENDUM 3 — character-side 1/2 fully traced; bridge identified (read in source at e50d098…; nothing compiled)
Paths: MSB = src/Development/AutomorphicArithmetic/MeanSquareBounds ; JCS = src/Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums

1. Second reader's Addendum 2 VERIFIED:
   meanSq_abs (MSB/MeanSqAbs.lean:8-16) groups pairs by soutPart m₀ (n·n') (JCS/MeanSquareHypWIff.lean:48), one exceptional class nstar;
   trivial class paid by Σ_p sP² + RR² (sP :51, RR :54). (8/q)=(2/q) example correct; 2 | m₀ so such pairs land in the trivial class.
   bs_block (MSB/BadShare.lean:163-166): Σ_q ||S(y_q)||² <= 4CY log(2Y)|P| for ANY choice y_q in [Y,2Y].
   box_of_S (MSB/BoxOfS.lean:44-62): Gχ(y) = -S_q(y) - y·tailL; tail <= Y^ε.
   Chebyshev step (hand-derived from MeanSq, PrimeSetTwoBounds.lean:26-27): bad fraction f <= 4C y^(1-2a) log y -> 0 iff a > 1/2.
   Correction to my Addendum 2: the diagonal is NOT simply Σ Λ(n)² min(1,y/n)²; identical twists survive averaging.

2. twistK (MSB/twistK.lean:148-151): ∀ ε A B > 0, eventually in Y, for admitted (U,m₀,a₀): ∃ nstar, ∀ odd squarefree s, 1<s<=Y^A, s coprime m₀, s≠nstar:
     |Σ_{q∈PPset m₀ a₀ U} (q/s)| <= Y^(-B) |P|.
   Reason q is huge (reconstruction): admitted.lo gives log U >= Y^(ε/6), so s <= Y^A <= (log U)^(6A/ε): Siegel–Walfisz range.
   Classical inputs (none mention 1/2; all about zeros near Re s = 1):
     PNTAPRelW  def JCS/MeanSquareHypWIff.lean:38, proved JCS/PNTFinal.lean:22  (PNT in APs with ≤1 exceptional term)
     ZFRDirichlet def src/Formalism/LandauZeroFreeBounds/Statement.lean:15, proved .../NoZeroComplex.lean:32
     ExcBound (Siegel) def .../LogDerivRegionChiOf.lean:50, proved .../SiegelWalfiszAPOfSiegelLower.lean:32
     page_across (Page) JCS/MSqPage.lean:37
   count_bad_core (MSB/CountBadCore.lean:18) <- ZeroDensityBox (def src/Formalism/GL3MeanSquares/ZeroDensityBox.lean:8; proved JCS/CountZAll.lean:13):
     #{primitive χ, cond <= Q, zero with Re s > 1-1/400, |Im s| <= Q} <= C·Q^(1/4).

3. CONCLUSION (character side): 1/2 = "power is loudness squared" against a y·log y mean-square budget; τ>0 needed for log and dyadic union.
   This is family-average square-root cancellation. Family averages are known not to give RH for a single L-function.
   => The decisive new content must be in the transfer from good twists to ζ.

4. THE BRIDGE (next target):
   hY in ch_core (src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChCore.lean:427):
     |TT|·(G - 4x^(1/2+ε)) <= Σ_{t∈TT} Re Σ_{ψ∈PsiA} ψ(e1 t)·GPsi(ψ, a_t/b),   G = GmA - SigA.
   paid for by ch_core hypothesis (ChCore.lean:350): ∀ u∈A0, gapA(u) <= x^(Cε)·errorBracketSizeWindows(...)   [same 3-term bracket where m ~ √x balances]
   gapA(u) = Σ_{t∈TT} Σ_j (ASK(a_t,t,w_{u,j}) - Re MAIN(a_t,w_{u,j}))   (.../DedekindLFunctions/SplitInertia.lean:50)  = arithmetic count minus main term.
   NOT OPENED: ASK, MAIN definitions; CharacterBalanceMoves.one_char (ChBalance.lean); the theorem supplying the gapA bound (via ChainTied / FamilyClassConnected).

5. Lean sketch (UNCOMPILED) of the elementary character-side step:
   theorem bad_fraction {ι} (P B : Finset ι) (S : ι → ℝ) (C y a : ℝ) (hB : B ⊆ P)
       (hms : ∑ q ∈ P, S q ^ 2 ≤ C * y * Real.log y * P.card)
       (hbad : ∀ q ∈ B, y ^ a / 2 < |S q|) (hy : 0 < y) :
       (B.card : ℝ) * (y ^ (2 * a) / 4) ≤ C * y * Real.log y * P.card
   (Source equivalent with varying y_q and dyadic union: bs_markov / bad_share, MSB/BadShare.lean:207, 251.)

NEXT: open ASK and MAIN, then find who proves the gapA bound. Write ASK - MAIN in plain math with every power of x, m, k visible.
```

## Addendum 4 — bridge definitions and immediate bound suppliers

Source checked locally at `e50d09817ad81469f737e8f637561e6ccf86c670` on 2026-11-20. A sparse checkout is in `rh-source/`; `git rev-parse HEAD` returned that exact pin. All declaration checks below are **read in source**, algebraic expansions are **derived on paper**, and nothing is **compiled**: neither `lean` nor `lake` was found on PATH. This is a further dependency trace, not an independent verification of RH or of all upstream hypotheses.

### The finite ASK actually used by gapA

Pinned source: [FirstPrimeNeSecondPrime.lean](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/FirstPrimeNeSecondPrime.lean#L66-L92).

Let `[v]+ = max(v,0)`, `P_t(g) = cconj + g + topPl(t)`, `f = |PhiSet|`, and let `I_d` be the inertia subgroup at `d`. The definitions give exactly

    ASK(D,N,a,t,w)
      = 2 Σ_{p ≤ N, IsInert(D,p)} log p
            Σ_{1 ≤ i ≤ N, i·frob(p) ∉ Phi}
              [a/p^i − w(P_t(i·frob(p)))]+
        + log d Σ_{1 ≤ i ≤ N}
            Σ_{g ∈ i·frob(d)+I_d, g ∉ Phi}
              [a/d^i − w(P_t(g))]+.

Here `IsInert(D,p)` explicitly requires p prime, p different from 2, q1 and d, and `frob(p) ∉ Phi`. This is a weighted prime-power ramp sum, with a separate ramified-prime term. It is not simply an unweighted counting function. `N` truncates both the prime range and exponent range. The hypotheses later ensure `a/w(ρ) ≤ N` on Phi.

The main term in the same namespace is complex, and its real part is

    Re MAIN(ell,a,w)
      = a [log a − 1 − γ + Re ell(chC)
           − (1/f) Σ_{ρ∈PhiSet} log w(ρ)].

`gapA(u)` is the sum of the difference of these two displayed expressions over `t ∈ TT` and `j ∈ Fin m`, using `a = a(t)` and `w = w(u,j)`. This follows directly from `Deduction.CH.gapA`, SplitInertia.lean:50–52.

There is also an infinite-sum, multiplicative-group definition named `ASK` in RunBaseDimensionLeRankAddGenusTerm.lean:105. It must not be silently substituted for this finite definition; identifying their applications needs the intervening comparison results.

### Who supplies the gap bound?

The immediate pointwise supplier is [Deduction.ch_top](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L37-L73). For arbitrary finite index types and data in its statement, assume

    IdentU Dd tr D N ell TT a w eT eP,
    SizeData₂ Dd C Xpp, ErrWindows Dd C Xpp eK K,
    BNBoundsU Dd T2, LargeX Dd.x Dd.ε K C.cHH eK.

Then for **every** `u : U0` it proves

    gapA(tr u) ≤ x^[(C.eDiv+C.eLoss+3)ε]
       [nT·aE·(1+m²/k) + 2n·m²·b·x^ε
                            + m·nT2·k·b·x^(2ε)/n²],

with `x=Dd.x`, `ε=Dd.ε`, `n=|H|`, `nT=|TT|`, `nT2=|T2|`, `aE=Dd.a`, `b=Dd.b`, and `k=Dd.k`. The last bracket is the paper expansion of `errorBracketSizeWindows`; rewriting its denominator uses `n>0` and `x>0`. The exact unexpanded Lean term is

    nT*aE*(1+m^2/k)
      + m*((2*n)*m*b*x^ε + nT2*k*b*x^ε/(n*(n*x^(-ε)))).

The proof explicitly establishes the following chain:

    gapA(tr u) = Dd.ASK u − Dd.Main u
      ≤ ErrX5at Dd C Xpp u
      ≤ x^[(C.eDiv+C.eLoss+3)ε] ErrText(Dd)
      ≤ x^[(C.eDiv+C.eLoss+3)ε] errorBracketSizeWindows(...).

The equality uses `ch_top_main_eq` and the ASK component of `IdentU`. The first inequality uses `each_unit_bound_statement`; the second uses `errX5at_le`; the final comparison uses the two `BNBoundsU` inequalities. Thus the small bracket is a conclusion from substantial geometric and slope hypotheses, rather than a direct consequence of quiet auxiliary twists alone.

### The next layer is now explicit

`SizeData₂` is defined in SChain.lean:17–19 as the conjunction

    HidaSetting, DIV, EComp5, HComp, Count5, Slopes,
    QuotientSlopeBoundsWith, LossBounds, SlopeIneq, HHBound, FParams.

`each_unit_bound_statement` (ChainSlopeWindows/LevelOfCongruence.lean:175–197) consumes all eleven components. Its body invokes `Ga_bound5` and `weighted_mean_lower_bound_le`, then combines them with `LossBounds` by linear arithmetic. In particular, `LossBounds` is a genuinely quantitative input:

    ∀ u, Dd.ASK u − Dd.Ga u ≤ Dd.LoP C
         and Dd.IO u ≤ Dd.LoP C.

`PointwiseBoundVariant` and this definition are at QuotientSlopeBoundsWith.lean:34–35,72–76. `errX5at_le` (ChainSlopeWindows/PChain.lean:613–673) then absorbs the expanded error into `ErrText`, with

    ErrText = nT*aE*(1+m²/k) + m*(B0+Nc),
    CErr = C.eDiv + C.eLoss + 3.

Those definitions are at ErrorFormsWeakWindowsFalse.lean:16–19. The absorption uses `ErrWindows`, `LargeX`, and the scalar `core_ineq`; it is not where the arithmetic gap is originally controlled.

The existing window packaging also checks out at this level: `ChainTied` (TieGlobal.lean:97–114) includes `Ident`, `SizeData₂`, `ErrWindows`, and `BNBounds`, together with the remaining growth, cost and size conditions. Separately, `chain_top_bound` (PChain.lean:28 onward) follows the mean-bound route through `joint_error_bound`, `top_from_weighted_mean` and `uniform_bound_statement`. This confirms two nearby presentations (pointwise and mean); this session has not proved that `ch_top` itself is invoked by the headline dependency path.

**Still to do:** trace the actual constructions supplying the eleven `SizeData₂` components, especially `LossBounds` and `QuotientSlopeBoundsWith`, starting from the `ChainTied` construction in LossesSmallShares.lean. Expand `Ga_bound5` and `weighted_mean_lower_bound_le` before calling this bridge independently understood. The earlier exceptional-squarefree-class calculation in `meanSq_abs` also remains to be checked in full; this addendum does not settle it. No claim of noncircularity follows merely from the earlier observation that several character-side statements concern zeros near 1.

## Addendum 5 — the bridge call and the exceptional class

**Source trace at the same pin.** `core_gm` actually applies `ch_core`, takes an arbitrary $u∈A₀$, uses the cover to find $v$ with $tr(v)=u$, and supplies `Deduction.ch_top … v` as the gap bound. The proof increases the exponent using $C.eDiv+C.eLoss≤eD+eL$ and the nonnegativity of the bracket. It then uses `gmA_eq` and `sigA_le`. This resolves the dependency question in Addendum 4. The per-character inequality `one_char` used at this step is in ChCore.lean:202, called at line 419. [core_gm](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/PrimitiveCosets/CoreGm.lean#L51-L72)

**Geometric loss.** Put $Q=|TT|mb$. For each allowed choice of weights at a sufficiently late family scale, the concrete loss proof obtains

    ASK − Ga ≤ (2 log(4) C + 13 sg) Q ≤ (3 C + 13) Q,
    Σ_{p∈cand} log(p) io(p) ≤ sg Q ≤ Q.

Here the source proves $sg≤1$, $0≤C≤K$, and ultimately uses $3|K|+13$ for both inequalities. In particular this construction can take **eL = 0**. Its constant and starting scale are supplied with the family. The working quantifiers in `LossFS` choose one admissible pair of vectors at each sufficiently large window point and control every index realizing that pair. [LossFS and its use](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L13-L21) · [joint_core](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/DiscriminantSettingSatisfied.lean#L178-L226)

The supply chain is `joint_core → joint_discriminant_bound → joint_discriminant_eventually → losses_of_small_share_weight → stLoss7 → lossF_of_7 → linkCore.L8`. The first declaration combines `loss_bound`, `out_discriminant_bound`, `first_le`, `second_discriminant_bound`, and `size_core`. The family application supplies `ChosenTT`, `ChosenBadp`, `LinkG`, and a small-share weight condition. It uses `askIsF` to identify the finite arithmetic ASK. The source of L7 is different: `model_slopes_five` transports two inequalities from `SlopesN_at`, which `slopesN_at_of` derives from `UnitWeightPartition.lower_bound_simplified` and `claimHigh_valid` under local hypotheses `Places_at`. These are remaining substantive dependencies. [Family loss proof](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/LossRequirementsOfSmallShares.lean#L86-L165) · [Construction of eleven inputs](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L158-L211)

**Which exception survives the simultaneous estimate?** In `twistK` fix an admitted family and set $Z=m₀Y^A$. A bad label $s$ requires a selected exceptional pair $(χ,β)$ for modulus $m₀s≤Z$, with $1-β<c₀/\log Z$, whose values on units congruent to 1 modulo $m₀$ agree with the quadratic symbol of $s$. For two such labels, `page_across` gives agreement of the two characters on integers coprime to both moduli. Restriction to those equal to 1 modulo $m₀$ and `jacobi_separate` then force equality of the squarefree labels. The proof selects that unique label if one exists and zero otherwise. `excBound` also enters the prime-family counting lemma `count_a`. The zero-density exception in `count_bad_core` plays no role in this uniqueness argument. [twistK](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/twistK.lean#L245-L285)

For $r=\max(nstar,2)$, `pairs_r` bounds its ordered-pair weight by $2B²+2BR$. The prime case budgets $sP(r)^2+2sP(r)R$. The composite case uses the two possible orders of the pair of primes $(\minFac(r),r/\minFac(r))$. With $B=C₂\log y$ and $R≤5C₁\sqrt y$, the source bounds the two terms by $4C₂² y\log y$ and $20C₁C₂ y\log y$. The prime-family factor $|P|$ is applied to the whole budget. The separate extraction in [rh-extraction](rh-extraction/README.md) gives a diagonal argument for this step. [Pair estimate](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/MSqPairs.lean#L307-L323) · [Constants](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/meanSqK.lean#L151-L192)

## Addendum 6 — compiled check of the exceptional-class bound

**Compiled.** Lean v4.33.1 (portable Windows build) against Mathlib at 0df444a360eaa60ab8c11dca51a86af692955474, checked out and already built. I ran `lean <file>` for each of the three files in [rh-extraction](rh-extraction/README.md) with `LEAN_PATH` set to Mathlib and its packages. I did not use `lake build`. Every `#print axioms` line reports only `propext, Classical.choice, Quot.sound`, with no `sorryAx`.

| File | Declarations checked |
|---|---|
| ParityEnergy.lean (imports `Std` only) | `parity_energy_identity`, `parity_correlation_le` |
| ScalarBridge.lean | `normalized_bridge`, `geometric_pole_contradiction`, `exclude_right_zero` |
| Squarefree.lean | `class_le_trivial`, `interval_class_le_trivial` |

**Statement as compiled.** For every `N m r` and every `c : ℕ → ℝ` with `0 ≤ c n`,

    Σ_{a,b ∈ Icc 1 N} [rep_m(ab)=r] c(a)c(b)  ≤  Σ_{a,b ∈ Icc 1 N} [rep_m(ab)=1] c(a)c(b)

(`interval_class_le_trivial`). It needs no prime-power support and no cap on single-prime buckets. A fix was made in this pass: `pairMass_eq` (Fin N shifted by one → `Icc 1 N`) had a failing `simp_rw`, which I replaced with two explicit reindexings.

**Comparison with the source (read in source, definitions compared by eye).**
- `representative m n = ∏ p ∈ n.primeFactors.filter (Odd (n.factorization p) ∧ ¬ p ∣ m), p` is the same expression as `soutPart m₀ N` (MeanSquareHypWIff.lean:48-49). They are not linked by a compiled equality, because the extraction does not import the repository.
- The double sum over `Icc 1 N` with `if … = r then c n * c n' else 0` has the same shape as the left side of `pairs_r` (MSqPairs.lean:307-309).
- The source's exceptional label is `max nstar 2` (MeanSqAbs.lean:55), so `r > 1`. The Lean bound holds for any `r`.

**What this does and does not show.** It gives a second route for the exceptional class: its pair mass is at most the trivial-class pair mass, with constant 1. The source instead bounds it by `2B² + 2B·RR` using a cap `sP ≤ B`. The trivial-class budget is the sum of `sP²` plus `RR²`, so this route needs the same inputs already used for the trivial class. It does not replace `pairs_r`, and it says nothing about the zeta bridge, `LossBounds`, or `QuotientSlopeBoundsWith`. Those remain uncompiled.

**Next.** Trace `LossBounds` and `QuotientSlopeBoundsWith` (the open item at the end of Addendum 4). To link `representative` to `soutPart` formally, add the pinned repository as a dependency.

## Addendum 7 — load-bearing test of the eleven `SizeData₂` inputs (Claude, 2026-11-21)

Tags: **READ** = read in source at the pin; **DERIVED** = hand algebra; **COMPILED** = checked by Lean; **INTERPRETATION** = my reading, not stated in source. Paths are under `src/Formalism/`. Abbreviations: `LOC` = SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean, `MBS` = RankGapBounds/MeanBoundSecondForm.lean, `QSB` = SizeWindowBrackets/QuotientSlopeBoundsWith.lean.

### Result in one line

`ASK − Main` is bounded by chaining four inequalities in which two quantities cancel: the ambient lattice slope `μ(cc)` and the place-sum `Ga`. All eleven components are used; four carry the main terms and the rest size the errors.

### The chain (READ; algebra DERIVED and COMPILED as a skeleton)

`each_unit_bound_statement` (LOC:175-197) splits `ASK − Main = (ASK − Ga) + (Ga − Main)`. `LossBounds` (QSB:34) pays the first part. `Ga_bound5` (LOC:113-161) pays the second using the other ten. For one window point `u0` and one family member `u`:

1. **Slope gain** — `QuotientSlopeBoundsWith`, second half (QSB:19-22): `μ(M_u) + Ga + Fo − Ee_u − Lo_u ≤ μ(N_u)`. Twisting the lattice `M_u` at the places raises its slope by `Ga`.
2. **Explicit degree** — `DIV` (MBS:118): `μ(cc) + h_u − Fo ≤ Σ_t [m·ph(a_t) − m·a_t·logOm − a_t·log T_u] + EDiv`, with `ph(y) = y log y − y` (MBS:9) and `logOm = γ + log(π/v) − Re ell(chC)` (MBS:88). Euler's γ enters here.
3. **Count link** — `Count5` lower bound (QSB:27): `Lam5 ≤ log T_u`. `key_identity5` (LOC:105) is exact algebra turning `SDiv − sumA·Lam5 + m·sumA·lg` into `Main + const`, where `Main = Σ_j Σ_t a_t (log a_t − 1 − γ + Re ell(chC) − mean_ρ log w)` (MBS:107). This is the `x log x − (1+γ)x` shape of Gζ's main term.
4. **Pointwise combination** — `s_lower5` (LOC:50): `Ga + μ(cc) − K5 − mean Lo ≤ s`, where `s = mean_u (μ(N_u) − h_u)`.
5. **Averaging slope inequality** — `SlopeIneq` (MBS:151): `s − log|W| − Φ ≤ μ(cc)`, with `Φ = (1−del)⁻¹[4·uF·log(1 + HH/uF) + (η + 4√e)·HH]`.
6. **Cancellations** — `μ(cc)` cancels between 4 and 5, giving `Ga ≤ Main + log|W| + K0 + mean Lo + Φ`. Then `Ga` cancels with `LossBounds`, giving `ASK − Main ≤ LoP + K0 + mean Lo + log|W| + Φ`.

### What each of the eleven does (READ)

| Component | Definition | Job |
|---|---|---|
| `LossBounds` | QSB:34 | Primes: the ramp sum ASK is within `LoP = cLoss·nT·m·b·x^(eLoss·ε)` of the place-sum Ga; also bounds IO |
| `QuotientSlopeBoundsWith` | QSB:19 | Primes: Ga is the slope gain from twisting at places (both directions) |
| `DIV` | MBS:118 | Main term: ambient degree ≤ explicit archimedean sum (γ, log π) |
| `Count5` | QSB:27 | Main-term link (lower bound); error size (other two clauses) |
| `SlopeIneq` | MBS:151 | Links the two sides: mean slope ≤ ambient slope + log of family size + Φ |
| `Slopes` | MBS:139 | Error size: `|μ(M_u)| ≲ cSlope·nT·a·La` → the x/m term |
| `EComp5` | QSB:24 | Error size `m·B0` → the m term; its main part `m·sumA·lg` cancels in the key identity |
| `HComp` | MBS:126 | Error size: heights and log T vary little across the family |
| `HHBound` | MBS:158 | Error size of Φ: `HH ≤ x^cHH·b` |
| `FParams` | MBS:161 | Parameter ranges for Φ (del, η, e) |
| `HidaSetting` | MBS:111 | Signs and positivity |

### Where the first square root sits (READ sizes; DERIVED ratio)

`mkData` (SizeWindowBrackets/Chain2aCoreNoAnalytic.lean:226) sets `a = x·b`, `b = exp(x^ε)`, `B0 = 2|H|·m·b·x^ε`, `Nc = |T2|·k·b·x^ε`, `HH = x^cHH·b`. The "a-sized" errors (Slopes, DIV, HComp) scale like `nT·x·b` and do not grow with m. The per-index errors (EComp5, HComp, QSB) scale like `m·B0 ∝ m²`. The normaliser L scales like `nT·m·b`. Dividing gives x/m against m, which balances at m ≈ √x. So averaging over m indices divides the a-sized lattice error by m, while each index adds its own fixed cost.

### Interpretation (INTERPRETATION)

The bridge computes one lattice degree two ways. Finite places (primes) give the slope gain Ga ≈ ASK; the archimedean data gives Main (γ, log π). The slope inequalities make it one-sided, which matches the earlier observation that only an upper bound on Gζ is used.

### Compiled skeleton (COMPILED)

File `rh-extraction/TransferSkeleton.lean` imports only `Std` (no Mathlib). Command: `lean TransferSkeleton.lean` with Lean 4.33.1 (official Linux release, commit 819816b2e0a3), run by Claude in its own workspace.
- `pointwise_lower` (mirrors `s_lower5`) and `transfer` (mirrors `Ga_bound5` + `each_unit_bound_statement`): axioms `[propext, Classical.choice, Quot.sound]`.
- `slope_needed`, `lower_needed`, `loss_needed`, `div_needed`, `gain_needed`: explicit integer counterexamples showing the conclusion fails when that one hypothesis is dropped. No axioms.
- Not modelled: the weighted-mean step (`sub_wmean_le`) between the two levels, and the size bounds inside the error terms.
- Same toolchain, independent check: `ParityEnergy.lean` from Addendum 6 also compiles with the standard three axioms.

### Next

The real content now sits in the **suppliers** of the four main-term components: QSB (slope gain), DIV (explicit degree), SlopeIneq (averaging), LossBounds (ASK ≈ Ga), plus the size bounds Slopes and EComp5. A parallel GPT prompt asks for each supplier's location and type (arithmetic / classical / automorphic) and for a check that the audit names this commit.

## Addendum 8 — GPT supplier audit of the eleven inputs (2026-11-21; merged by Claude)

Merged verbatim from the GPT handoff (its section "November 21 supplier audit at e50d098"). Claude spot-checked three claims against the pinned source and found them correct: `topDesWin` (Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean:11) is called with eD = 2 and eL = 0 on the headline path; `ChQD_at` / `BoundsAtX` (Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean:38-45) contain |gχ(x)| ≤ x^(1/2+ε) and |L′(1,χ)/L(1,χ)| ≤ C log x for the q, d and product twists; `placesF_min'` (Formalism/LocalToGlobal/GlobalTheory/PlacesMin.lean:101-114) hands off to `places_at_of`. The archive byte comparison (audit SHA-256 and 175,187 identical Lean files) was done by GPT and was not re-run by Claude.

### November 21 supplier audit at e50d098

READ marks a definition, proof body, or published audit entry. DERIVED marks hand algebra, a classification, or an independent comparison of source bytes. COMPILED is reserved for a Lean check run by the investigating reader. This pass is source-level.

| Component | Plain-math meaning | Definition | Supplier on the headline path | Type (DERIVED) | Tag |
|---|---|---|---|---|---|
| HidaSetting | Positivity of sizes, ranks, level primes and weights, mean slope bounded by maximal slope, and ranges for the frame errors. | [MeanBoundSecondForm.lean:111](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L111) | Direct conjunction at [LossesSmallShares.lean:158–168](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L158-L168). Positive ranks, slope comparison and lattice duality come from `lat_at` / `latF` at [QuadraticLogDerivCongr.lean:1323–1351](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L1323-L1351). Node, frame and size inputs enter at [LinkMin.lean:716–721](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L716-L721). | a + c | READ |
| DIV | Upper bound on the dual lattice slope plus word height minus the local term Fo, by an explicit main term and two errors. | [MeanBoundSecondForm.lean:118](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L118) | `DivisionPackageFace.wordFacts` calls `linkDIV_L2R_face` at [RecBridge.lean:633–641](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L633-L641) and [LinkDIVL2R3Col.lean:19](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/Divisibility/LinkDIVL2R3Col.lean#L19). The third word fact is supplied to `linkDIV_at_words` at [RecBridge.lean:689–691](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L689-L691). `data_DIV` at [QuadraticLogDerivCongr.lean:580](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L580) transfers it at [LossesSmallShares.lean:169–183](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L169-L183). | c | READ |
| EComp5 | The sum of the local E contributions over all m lifts differs from m times a common main term by at most cE·m·B₀. | [QuotientSlopeBoundsWith.lean:24](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean#L24) | `secondComplement_of_inputs` splits the two type primes from the remaining primes at [WeightDegreeSizes.lean:677–693](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/WeightDegreeSizes.lean#L677-L693). `complement_two_of_items` at [ClassOfRecordOfChoice.lean:148](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/ClassOfRecordOfChoice.lean#L148) passes this to the division theorem at [RecBridge.lean:334–336](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L334-L336), [694](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/Divisibility/RecBridge.lean#L694). `data_EComp5` sums over lifts at [QuadraticLogDerivCongr.lean:594](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L594) and [LossesSmallShares.lean:184–187](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L184-L187). | c + a | READ |
| HComp | The height corrected by (sum of top weights)·log T varies little between any two words over the same base. | [MeanBoundSecondForm.lean:126](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L126) | `compl3_diff`, `compl3_record` and `rbCompl3` at [Compl3Record.lean:15](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/HookProducts/Compl3Record.lean#L15), [Compl3Record.lean:217](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/HookProducts/Compl3Record.lean#L217) and [Compl3Record.lean:282](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/Divisibility/HookProducts/Compl3Record.lean#L282). The supplier proves the bound with coefficient 20+6/ε. See the actual field assignment at [IndefiniteRealisationChoice.lean:114](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/IndefiniteRealisationChoice.lean#L114), followed by [LossesSmallShares.lean:188–193](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L188-L193). | a at the estimate, on supplied arithmetic data | READ |
| Count5 | Two absolute bounds on log T and a uniform bound on its variation between words. | [QuotientSlopeBoundsWith.lean:27](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean#L27) | `division_level_prime_family` at [LinkMin.lean:425](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L425) combines mass, volume and a multiplicity gap. `family_part_five_of_explicit_constants` at [FamilyPartFiveOfExplicitConstants.lean:483](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/FamilyPartFiveOfExplicitConstants.lean#L483) and `countF_fam` at [JointsL.lean:1152](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/JointsL.lean#L1152) supply the field via [LinkMin.lean:711](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L711), [734](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L734) and [LossesSmallShares.lean:194–195](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L194-L195). | c | READ |
| Slopes | A lower bound on the mean slope of M and an upper bound on its maximal slope. | [MeanBoundSecondForm.lean:139](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L139) | The two open-part estimates are proved by `lower_slope_inequality_family` at [LowerSlopeInequalityFamily.lean:14](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/GL4/LowerSlopeInequalityFamily.lean#L14) and `slope_inequality_family_four` at [PStmtFree.lean:17](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/GL4/PStmtFree.lean#L17). They are selected at [TuSizeOfRealPlaceSecondLayer.lean:21–23](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/TuSizeOfRealPlaceSecondLayer.lean#L21-L23). `slopesM_at_of` at [JointsL.lean:1518](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/JointsL.lean#L1518) and `slopesMF_of_count_fam` at [SlopesMFOfCountFam.lean:25](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/SlopesMFOfCountFam.lean#L25) give the estimates used at [LinkMin.lean:713](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L713) and [LossesSmallShares.lean:196–197](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L196-L197). | c, with a b input at s=1 | READ |
| QuotientSlopeBoundsWith | Compare the mean and maximal slopes of N with those of M after adding local gains and subtracting local errors. | [QuotientSlopeBoundsWith.lean:15–22](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean#L15-L22) | `placesF_min'` at [PlacesMin.lean:23](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/PlacesMin.lean#L23), [101–114](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/PlacesMin.lean#L101-L114) assembles local-place and rank estimates, including `LinkMu`. `slopesN_at_of` at [TopDensityNGeSixteen.lean:1529](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1529) applies `lower_bound_simplified` and `claimHigh_valid` at [WeightedSlopeExcessDecomposition.lean:180](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/WeightedSlopeExcessDecomposition.lean#L180), [191](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/WeightedSlopeExcessDecomposition.lean#L191). `slopesNF_of` at [TopDensityNGeSixteen.lean:1544](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1544) supplies [LinkMin.lean:714–715](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L714-L715) and [LossesSmallShares.lean:198–200](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L198-L200). | c with a and b estimates | READ |
| LossBounds | For each base point, the shortfall of the local gain against the finite prime sum ASK, and the local loss IO, each have the same upper bound. | [QuotientSlopeBoundsWith.lean:34](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean#L34) and [MeanBoundSecondForm.lean:105](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L105) | `joint_discriminant_eventually` at [DiscriminantSettingSatisfied.lean:234](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/DiscriminantSettingSatisfied.lean#L234), from `joint_core` at [DiscriminantSettingSatisfied.lean:178](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/DiscriminantSettingSatisfied.lean#L178). `losses_of_small_share_weight` at [LossRequirementsOfSmallShares.lean:86](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/LossRequirementsOfSmallShares.lean#L86) applies both estimates at [LossRequirementsOfSmallShares.lean:129–160](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/LossRequirementsOfSmallShares.lean#L129-L160). `stLoss7` at [LossRequirementsOfSmallShares.lean:165](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/LossRequirementsOfSmallShares.lean#L165) and `lossF_of_7` at [LossesSmallShares.lean:308](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L308) supply [LinkMin.lean:721](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L721) and [LossesSmallShares.lean:201–206](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L201-L206). | a on the supplied local data, with b/c inputs | READ |
| SlopeIneq | Lower bound on the dual slope from the weighted mean of the word slopes minus heights, after frame and dimension errors. | [MeanBoundSecondForm.lean:151](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L151) | `joint_a_ramified_holds` at [JointDModelAppliesUnitLattice.lean:254](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/JointDModelAppliesUnitLattice.lean#L254) is applied by `frame_at_of` at [TopDensityNGeSixteen.lean:538](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L538), [596](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L596). `frameF_of` at [TopDensityNGeSixteen.lean:606](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L606) gives the family result at [LinkMin.lean:717–719](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L717-L719). `data_SlopeIneq` transfers it at [QuadraticLogDerivCongr.lean:699](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L699) and [LossesSmallShares.lean:207](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L207). | c, using a lattice/frame inequality | READ |
| HHBound | A positive budget HH dominates the difference between the frame mean and minimal dual slope, with HH ≤ x^CH·b. | [MeanBoundSecondForm.lean:158](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L158) | `hh_of_lvl` at [LvlWire.lean:51](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/Divisibility/DivisibilityRemainder/NoColumnCase/LvlWire.lean#L51) applied at [BrestFinalAll.lean:45–54](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BrestFinalAll.lean#L45-L54) supplies the size estimate. `lat_at` proves the dual minimum equals minus the primal maximum at [QuadraticLogDerivCongr.lean:1323–1333](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L1323-L1333). `data_HHBound` combines them at [QuadraticLogDerivCongr.lean:714–728](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L714-L728) and [LossesSmallShares.lean:208–209](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L208-L209). | c | READ |
| FParams | Each frame parameter δ, η, e lies between zero and its corresponding cap. | [MeanBoundSecondForm.lean:161](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/RankGapBounds/MeanBoundSecondForm.lean#L161) | For δ, `closed_linkIRR_of_join_count` at [LinkIrr.lean:22–43](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkIrr.lean#L22-L43) calls `linkIRR_of_join_ex`. For η and e, `frameF_of` at [TopDensityNGeSixteen.lean:606](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L606), [638–646](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L638-L646) produces the bounds used at [LossesSmallShares.lean:96–99](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L96-L99). The conjunction is assembled at [LossesSmallShares.lean:210–211](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L210-L211). | c, followed by a | READ |

**READ — Which construction feeds the table.** On the headline path, `UpperTheory.FinalTheorems.everyCharacter` goes through `every_character_of_literature_of_vWin`, `every_character_of_theta_integrals_local_matching`, and `every_character_of_green_v_win`. The window theorem calls `shape_closed_link_n_of_green`. That theorem uses `GlobalTheory.Top.link_gl`, whose proof calls `FamGLmin.link8`. The latter uses `link7`, then `linkGLOBAL7_min → linkGLOBAL7_items → linkCore`. The family reaches `topDesWin` with eD=2 and eL=0. This corrects the earlier handoff's reference to the parallel entry point `plugWin`. [MainConclusion.lean:7–11](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean#L7-L11) · [EveryCharacterOfLiteratureOfVWin.lean:810](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L810) · [SiegelEisensteinSecondTermHypotheses.lean:69–73](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L69-L73) · [TopPlug.lean:12–18](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean#L12-L18) · [TopShape.lean:33–55](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean#L33-L55) · [LinkGl.lean:25–31](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LinkGl.lean#L25-L31) · [LogXLowerFamilyOfTheorems.lean:60–75](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LogXLowerFamilyOfTheorems.lean#L60-L75) · [LinkMin.lean:693–737](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L693-L737).

**READ — What the eleven supply.** `ch_top` identifies the gap with ASK−Main, applies the per-unit bound to the eleven inputs, then applies the separate error-window, size, and large-x estimates. [SChain.lean:17–19](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/SChain.lean#L17-L19) · [ChTop.lean:37–72](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L37-L72) · [LevelOfCongruence.lean:175–178](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L175-L178).

#### The three inequalities in the concrete family

**READ.** M is the level-zero lattice; N is the lattice called Nu in the model. A base index is u₀ and a word above it is u. Write n for the ambient order, n_T for the number of top indices, T for the word's level prime, and Δ_E for the absolute discriminant of the host field. The model takes b=exp(x^ε), a=xb, L=x^ε, b′=a/exp(x^(ε/3)), L_a=log(a·rdE), f=2n and B₀=fmbx^ε. The field degree is 2f. [QuadraticLogDerivCongr.lean:464–502](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L464-L502) · [DataParams₂.lean:27–39](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/DataParams₂.lean#L27-L39), [226–230](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/DataParams₂.lean#L226-L230) · [Params.lean:28–30](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/Params.lean#L28-L30) · [DataArith.lean:198–200](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/DataArith.lean#L198-L200) · [DataHost.lean:140](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/DataHost.lean#L140) · [CoeNeZeroOfNotMem.lean:235–241](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/CoeNeZeroOfNotMem.lean#L235-L241).

**DERIVED — Slopes.** Put B=exp(x^ε), P=exp(x^(ε/3)) and A=log(xB·Δ_E^(1/(4n))). For every u₀,u the pair is

    −cSlope n_T xB A (1+m/k) ≤ μ_M,
                               μ_max,M ≤ cSlope n_T xB A.

**DERIVED — QuotientSlopeBoundsWith.** With the same notation, put J=Ga(u₀)+Fo(u₀)−Ee(u₀,u) and c₁=cSl1. The two comparisons are

    μ_max,N ≤ μ_max,M + J + 2c₁ n m² B x^ε,
    μ_N ≥ μ_M + J − [c₁ IO(u₀)
                       + c₁ n_T m xB(1/k + 1/P) log T
                       + c₁ x n P + 1].

The term xnP comes from X″=a/[b′/(xn)]=xnP. The m² in the upper bound comes from the product mB₀. Ga, Fo, Ee, IO and T are data of the chosen places and word. Replacing them by monomials would be an extra estimate.

**DERIVED — LossBounds.** The general right side for each inequality is cLoss·n_T·m·B·x^(eLoss ε). On this path eLoss=0, so the two inequalities, pointwise in u₀, become

    ASK(u₀) − Ga(u₀) ≤ cLoss n_T m exp(x^ε),
                IO(u₀) ≤ cLoss n_T m exp(x^ε).

**READ.** In the actual loss proof the reduced unit is n_T m b, and the family coefficient chosen there is 3|K|+13 for the local K of that proof. The coefficient need not be fixed across ε. By contrast eD=2 and eL=0 are fixed on the headline path. [LossRequirementsOfSmallShares.lean:86–101](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/LossRequirementsOfSmallShares.lean#L86-L101), [133–160](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GlobalTheory/LossRequirementsOfSmallShares.lean#L133-L160) · [TopShape.lean:52](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopShape.lean#L52) · [DivinNOfHypV.lean:13–15](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/CharacterBoxes/DivinNOfHypV.lean#L13-L15).

#### 1. Audit and commit provenance

**READ.** The MIT audit log gives no RH-repository commit, tag, tree hash or archive hash. Its exact headline axiom line is

    'riemannHypothesis' depends on axioms: [propext, Classical.choice, Quot.sound]

**READ.** The audit page itself identifies the mirror, the source archive, the toolchain and the exported proof. It gives SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc` for the 239,275,554-byte joined source archive. It names Lean commit `819816b2` and Mathlib tag `v4.33.1` at `0df444a3`. It gives no Deicyde commit. The audit reports compilation and independent kernel checks. [Audit log](https://math.mit.edu/~drew/grh/audit.log) · [Verification and provenance](https://math.mit.edu/~drew/grh/#provenance).

**DERIVED — Independent byte comparison.** In this pass the 14 published parts were joined in numerical order. The joined SHA-256 and byte count match the audit. Every one of the archive's 175,187 Lean sources under `lean/src/` is present and byte-identical in the e50d098 pin. Of all 175,190 original regular files only `lakefile.toml` differs. The pin adds nine files, including `src/Challenge.lean`. This establishes a source-content match for the proof at the requested commit. No Lean compilation or proof-export reproduction was performed in this pass. [Pinned repository](https://github.com/Deicyde/riemann-hypothesis/tree/e50d09817ad81469f737e8f637561e6ccf86c670) · [Source archive instructions at the pin](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/verification/NOTES.md#L7-L20).

#### 4. Circularity and next checks

**READ.** None of the eleven literal definitions states RH, an upper bound for Gζ, or a bound for ζ′/ζ in the open right critical strip. There is genuine analytic input upstream. `ChosenQD` includes |gχ(x)| ≤ x^(1/2+ε) AND |L′(1,χ)/L(1,χ)| ≤ C log x for the q, d and product twists. `dl_at_of` selects the logarithmic derivative clause for the d character and `dl_of_chosen` weakens its upper bound to x^ε. The model identifies this number with the real part of L′(1,χ_d)/L(1,χ_d). [Chosen.lean:38–45](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean#L38-L45), [71](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean#L71) · [FrameCodeOfAdditive.lean:153–181](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalSchurBounds/FrameCodeOfAdditive.lean#L153-L181) · [DataParams₂.lean:65–71](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/DataParams₂.lean#L65-L71), [126–127](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/DataParams₂.lean#L126-L127).

**READ.** `LinkDIV_at` includes a field named `ZeroAbove`. Above a residue-characteristic cutoff, and outside listed exceptional primes, two local quantities (gain and E) vanish. Its variable is a finite place. [GlobalTheoremInputs.lean:77–89](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GlobalTheoremInputs.lean#L77-L89) · [DataParams₂.lean:246–250](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalRingCardinality/DataParams₂.lean#L246-L250).

**DERIVED.** The distinction requiring care is which function is bounded, for which family, and on which set of arguments. A square-root bound for the chosen auxiliary twists is a substantive input. The written clauses do not assume the target Gζ bound. Also, `ASK−Ga` can look like the output: `ch_top` explicitly identifies its target with `ASK−Main`. Getting from Ga to Main requires a separate estimate. This inspection establishes the displayed dependency edges, and leaves any claim of global independence to a transitive proof check.

**READ — Follow-up on the selected twists, retained from the parallel investigation.** For fixed y, `MeanSq` bounds Σ_q |S|² by Cy log(y)|P| for every weight |κ(n)|≤1, with S=Σ_{n≤Z} Λ(n)min(1,y/n)κ(n)(n/q). `stage` uses `meanSqK`, `bad_share` and `box_of_S`; the latter passes on a zero-free box for each selected primitive inducing character. The proof of `meanSqK` uses `RR_le`, `exists_primePowerSum_le_mul_log`, `sPsq_le`, `sum_cN_le` and `twistK`. Read its off-diagonal bound at lines 107–111: it permits an exceptional squarefree index nstar. Treat an appeal to exact pairwise orthogonality as a heuristic until the actual estimates are accounted for. [PrimeSetTwoBounds.lean:13–36](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/PrimeSetTwoBounds.lean#L13-L36) · [SecondEstimateOfIntervalHypothesis.lean:23](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/GL3MeanSquares/SecondEstimateOfIntervalHypothesis.lean#L23) · [StagePow.lean:41](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/StagePow.lean#L41) · [BadShare.lean:251](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/BadShare.lean#L251) · [BoxOfS.lean:28](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/BoxOfS.lean#L28) · [meanSqK.lean:51–64](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/meanSqK.lean#L51-L64), [107–111](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Development/AutomorphicArithmetic/MeanSquareBounds/meanSqK.lean#L107-L111).

**Copyable continuation prompt**

```text
Read the November 21 supplier audit in this file first. Use commit e50d09817ad81469f737e8f637561e6ccf86c670. Claude is separately testing which of the eleven SizeData₂ hypotheses are necessary. Leave that experiment to Claude.

For the quotient-slope branch, start at PlacesMin.lean:101–114. Follow places_at_of and its local length/slope hypotheses until you can derive the term x n exp(x^(ε/3)) from local estimates on paper. Distinguish the scalar cutoff identity from the theorem that actually bounds the error by that cutoff. As a separate branch, if investigating the auxiliary twists, start at meanSqK.lean:107 and follow twistK for the nonexceptional and exceptional indices. Use READ, DERIVED and COMPILED on every finding; give full pinned paths and line numbers. Include the first formula you can independently check and the first remaining input. Update this same Markdown handoff.
```

## Addendum 9 — "the prime tally matches the gain" (`LossBounds`, first half), traced one prime at a time (Claude, 2026-11-21)

Tags as in Addendum 7. Paths under `src/Formalism/`. `SKB` = SizeWindowBrackets/SecondKindBucket.lean.

### The picture

A ledger with one line per prime p. "Owed" is what p contributes to the prime tally. "Paid" is the lattice gain at p. The places above p split the payment, but their weights always add up to exactly log p, so the ledger collapses to one line per prime. At most primes ("served") the payment covers almost everything owed. At a few primes nothing is paid. The claim is that the total unpaid amount is tiny.

### The formula (READ)

For lifts j (m of them), tops t (nT of them) with ramp heights a_t ≤ a(1+θ), and odd exponents i:

    ramp_{j,t}(p) = Σ_{odd i} max(0, a_t/p^i − w_{j,t,i})                       (askAt, SKB:95)
    ASK − Ga = Σ_p 2·log p · [ Σ_{j,t} ramp_{j,t}(p) − (Σ_j gain_j(p) − τ(p)) ] + d-term   (SplitEq, SKB:30; proved splitEq_valid, SizeWindowBrackets/ChainSlopeWindows/AdmissibleSchurLemma.lean:63)

The collapse from places to primes is `UnitRule` (SKB:24): the place weights above p sum to log p. In the concrete family it is trivial: places are indexed by the primes themselves with weight log p (`unitRule_at`, LocalToGlobal/GlobalTheory/PowFourLtCeilThresholdPrime.lean:1982).

### How each class of prime is paid for (READ statements; ratios DERIVED)

- **Served primes** (p ≤ X″): per-prime covering rule (SKB:45, local `SizeData₂`): gain covers the ramps of the covered tops TTp(p), minus a small per-top loss `lo` and per-lift floor `fl`. Unpaid: the ramps of uncovered tops TT∖TTp(p) (`servedLoss`, SKB:50).
- **High primes** (p > X″ = a/w″): a_t/p^i < w″ apart from a tiny θ-overshoot, so ramps nearly vanish (`tHigh`).
- **First- and second-kind primes:** no gain; their whole ramp is lost, but each ramp is at most (4/3)·a/p (`AskUpperBound`, SKB:98; proved `top_term_bound`, AdmissibleSchurLemma.lean:290).
- **Counting tools:** Σ_{p≤Y} log p/p ≤ log Y + log 4 (`prime_log_sum_bound`, :141) and Σ_{p≤Y} log p ≤ log 4·Y (`theta_finite`, :155). These are proved in the repo; their proofs were not inspected.

Bad pairs must be rare. The uncovered (prime, top) pairs satisfy Σ log p/p · #(bad tops at p) ≤ nT·x^(−2+ε) (`badPrimeLogWeightedCount`, `OutD`, SizeWindowBrackets/PrimeClassLossHypothesesSatisfiable.lean:39-47; size `tOutD` :60). Second-kind primes satisfy `lhsW ≤ x^(−9)` (:36, :49, :62). The resulting loss from uncovered pairs is about 4·a·m·nT·x^(−2+ε) = 4·nT·m·b·x^(−1+ε). That is far below the unit nT·m·b (`unitU`, SizeWindowBrackets/WindowSettingSatisfiable.lean:130). All classes combine in `joint_core` (SizeWindowBrackets/ChainSlopeWindows/DiscriminantSettingSatisfied.lean:196) to give ASK − Ga ≤ (3C+13)·nT·m·b.

### What this means (DERIVED)

1. This step is bookkeeping plus elementary prime estimates, **given two local facts**:
   (a) the covering rule at served primes; (b) the rarity of uncovered pairs and of second-kind primes.
2. **[Corrected in Addendum 11]** Only the uncovered-pair part is ≈ x^(−1+ε) of the unit. The whole allowance is a constant multiple, (3C+13)·nT·m·b; the high-prime term alone is at least 2·log 4·C units (`SizePrHighLower`, SizeWindowBrackets/WindowSettingSatisfiable.lean:185). After normalisation that is still only x^O(ε), so this step is still not where √x is decided; eL = 0 means no extra power of x is needed.
3. Fact (a) is `AuxBlock8.Conclusion1` (SharpRestriction/GrowthBounds/SmallOrderPrimes.lean:15), used through `LinkG_at` (SharpRestriction/GlobalTheoremInputs.lean:122) and `linkG_at_core` (SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean:718). Its local gain is `gainP` (LocalToGlobal/GlobalTheory/IsResidueClassZero.lean:224): a sum over good representatives t0 of max(gU − Pr, g0). **[Corrected in Addenda 10–11]** `WeilJacquetShalikaLaw.Conclusion1` is a different statement that shares the name (a valuation bound on lattice columns). The actual numerical supplier is `AuxBlock8.Pf.stmtF`.
4. Fact (b) is supplied by the family (`ChBadp_at`, `ChW_at`; see `loss_setting_family`, LocalToGlobal/GlobalTheory/LossRequirementsOfSmallShares.lean). Not traced.

### Next

Trace fact (a): why the local lattice gain at a served prime covers the ramp tally of its covered tops. If (a) is a local counting fact on a finite group, the whole "primes enter the lattice" half becomes hand-checkable apart from (b).

## Addendum 10 — the covering rule at one prime is local combinatorics on Frobenius cycles (Claude, 2026-11-21)

Tags as in Addendum 7. Paths under `src/Formalism/`. `GB` = SharpRestriction/GrowthBounds. Nothing new was compiled; statements are READ, the interpretation is DERIVED.

### The picture

The finite group H holds a set of "tops", scattered through it like a random sprinkling of density δ₁ = x^(−ε/8). A prime p acts on H by one fixed step h, its Frobenius. Repeating the step walks H around in cycles. A top s "owes" its ramp: over odd step counts e, how far a_s/p^e sits above the fill at the spot s + e·h it lands on. On a **good** cycle, where the sprinkled tops look typical, the lattice "pays" at least what the cycle's tops owe, by a matching argument you can check with a pencil. On a **bad** cycle nothing is paid, and Addendum 9's rarity fact (b) has to show bad cycles are rare.

### The chain (READ)

1. Family-level `LinkG` (SharpRestriction/GlobalTheoremInputs.lean:137) is proved by `linkG_without_kernels` (LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean:224-238). That calls `AuxBlock8.Pf.stmtF` (GB/LogarithmicSums.lean:101), whose bundle contains the covering rule `AuxBlock8.Conclusion1` (GB/SmallOrderPrimes.lean:15).
2. The covering rule follows from `GainBoundAll` (GB/LogarithmicSums/Conclusion1OfGainBoundAll.lean:103-121). That in turn follows (`gain_bound_all_of_star`, GB/LogarithmicSums/NotSingularOfCentral.lean:730) from the per-cycle inequality `StarAt` (Conclusion1OfGainBoundAll.lean:129):

       Σ_{s on cycle t0} (askP(s) − lo) ≤ gU(t0) + dl(t0) − Pr(t0) − ⌈tv(t0)⌉ − Dp − 1.

3. `gU` (GB/IsResidueClassZero.lean:254) is `gam(p)·Σ_s al(s) − Σ_{non-V s} Σ_{odd e} min(al(s)/p^e, capU(s,e)) − dl`, with `gam(p) = p/(p²−1) = Σ_{odd e≥1} p^(−e)` (:89). Since x − min(x, c) = max(0, x − c), gU is the same ramp tally as `askP`, with height lowered to al = a − 2cG and cap lowered by kaJ (DERIVED).
4. `StarAll` is proved by `star_fam` (GB/LogarithmicSums/StarFam.lean:11) → `starAll_of` (GB/LogarithmicSums/PartnerCountOfCentral.lean:842). It splits into small primes (`starAt_D`, :597) and large primes (`starAt_E`). Its local lemmas live in the same file:
   - `gU_lower` (:308): gU + dl ≥ Σ askP + (V-top terms) − Nv·3cG·log_p(2a).
   - `kink` (:136): on a cycle of even length with marked positions, Σ_{odd-position marked y} min(W(y), a(x_y)/q^{d_y}) ≤ Σ_{even-position marked x} Σ_{odd e} min(a(x)/q^e, W(x+e)). Here x_y is the nearest even-position marked bead behind y, at odd distance d_y. This is a pure injection argument.
   - `kinkHH` (:369), `orbit_facts` (:471), `caseD_arith` (:497), `caseE_arith` (:545): transfer to H, then scalar arithmetic.
   - Inputs: `adm1` (GB/SmallOrderPrimes.lean:70) and numeric size facts `NumStar`.
5. `adm1` says that on **good** cycles: the number of tops lies between n·δ₁/(Ce·log x) and 40·n·δ₁; every V-top has a next V-top within Gp steps with at most N1 tops between; and backward V-partners are few. It is proved by `family_uniform_constant_holds` (GB/TopChoiceBounds.lean:4394) from `family_master_orbit_holds` (:4387). "Good" is `IsGoodOrbit` → `GoodOrbitIntervalTileCondition` (SubspaceCounting/GoodOrbitIntervalTileCondition.lean:24): CondA ∧ CondTiles ∧ CondIntervals, with binomial bounds (`binUpper`, `markedBound`, `condProbAt` with density δ).

### What this means (DERIVED)

- The covering rule (fact (a) of Addendum 9) looks **elementary in kind**: matching on cycles plus arithmetic, under typical-pattern conditions on good cycles. The proofs of `starAt_E`/`starAt_D` and the arithmetic lemmas were listed, not read line by line.
- The real content of this half moves to **counting**: tops sprinkled with density δ₁ make most Frobenius cycles good (`master_orbit_lemma_holds`), and bad cycles and second-kind primes are rare enough (fact (b)). Not yet read.
- This half does not set the exponent (Addendum 9). Together with Addenda 9 and 10, the route "primes → lattice gain" is now: bookkeeping + elementary prime sums + local cycle combinatorics + a counting/probability lemma about good cycles.

### Next

Read `master_orbit_lemma_holds` (GB/TopChoiceBounds.lean) to see whether "most cycles are good" is a self-contained counting argument. On the other half, the places theorem (GPT's branch) and the four lattice inequalities remain.

## Addendum 11 — GPT: how one served prime covers its tally (2026-11-21; merged by Claude)

Merged from GPT's file, where it was titled "Addendum 10"; GPT wrote it from the copy that ended at Addendum 9. It agrees with Claude's Addendum 10 and adds the exact split askP + Mn = p/(p²−1)·a, a worked example of the cycle injection, a finite check over 5,460 marked cycles, and the per-prime assembly. Claude re-checked one claim against the pin: `SizePrHighLower` (SizeWindowBrackets/WindowSettingSatisfiable.lean:185) states 2·log 4·C·unitU ≤ tPrHigh, and `xprime_q_two_expand` (ChainSlopeWindows/OneLeThresholdMulPowers.lean:444) gives X′·Q₂ = C·b + …, confirming GPT's correction of the loss size. The finite check was not re-run.

Pinned source at `e50d09817ad81469f737e8f637561e6ccf86c670`, 2026-11-21. READ means a statement or proof body inspected at the pin. DERIVED means a paper calculation or interpretation. No COMPILED claim for this addendum. Earlier addenda record their own checks.

#### The part you can prove on paper

**READ / DERIVED.** Fix a prime $p$, a lift $j$, and a selected position $s$ (a “top”). At odd distance $e$, write $v_e=a_s/p^e$ and let $w_e$ be the level at its partner. Split the contribution into the ramp $(v_e-w_e)_+$ and the capped part $\min(v_e,w_e)$. They add to $v_e$ exactly. Summing the geometric series gives

$$
\operatorname{askP}(s)+M(s)
=\sum_{e=1,3,5,\ldots}a_s p^{-e}
=\frac{p}{p^2-1}a_s,
\qquad M(s)=\sum_{e=1,3,5,\ldots}\min(a_s p^{-e},w_e).
$$

The source calls $M$ `Mn`. This fixes exactly how much is left to pay another charge after the ramp has been accounted for. [Exact split](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/PartnerCountOfCentral.lean#L249) · [Geometric factor](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L89)

**READ / DERIVED.** Take a cycle of even length $N$ and mark a subset $T$ of its positions. “Even” and “odd” refer to the position in this cycle. For each marked odd $y$, walk backwards to the nearest marked even $u$. Write $d$ for the distance. If no marked even position exists, the charge at $y$ is zero. Otherwise $d$ is odd and $y=u+d\pmod N$. Thus $y\mapsto(u,d)$ is injective, even when several positions use the same predecessor. For nonnegative heights $a_u$, caps $W_y$ and $p\ge2$ this proves

$$
\sum_{y\in T_{\rm odd}\, :\,d(y)>0}
  \min\!\left(W_y,\frac{a_{u(y)}}{p^{d(y)}}\right)
\le
\sum_{u\in T_{\rm even}}\ 
\sum_{e=1,3,5,\ldots}
  \min\!\left(\frac{a_u}{p^e},W_{u+e\bmod N}\right).
$$

Every term on the left occurs at its own index on the right. The remaining terms are nonnegative, and each series is bounded by a geometric series. Example on a cycle of length 8 with $T=\{1,3,6,7\}$: the receipts for $7,1,3$ are $(6,1),(6,3),(6,5)$. This includes two positions reached by wrapping around. [Parity convention](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/UnramifiedQuadraticSetting.lean#L54) · [Backward distance](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L207) · [Counting proof](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/PartnerCountOfCentral.lean#L136) · [Injectivity](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/PartnerCountOfCentral.lean#L168)

**DERIVED, with a finite check.** I also enumerated all 5,460 subsets of cycles of lengths 2, 4, 6, 8, 10 and 12. I checked injectivity and the inequality using exact fractions, $p=3$, $a_i=(i+1)(i+2)/3$, $W_i=(i\bmod 4)/2$, and odd distances up to $N$. The finite check includes empty sets and wraparound. The argument above covers arbitrary nonnegative weights and the infinite sum.

#### How much of the covering this explains

| Scope | Result read in the pinned source |
|---|---|
| One good orbit, one lift | `StarAt` requires $\sum_{s\in T(t_0)}(\operatorname{askP}(s)-\mathrm{lo})\le g_U+\mathrm{dl}-\mathrm{Pr}-\lceil t_v\rceil_{\mathbb N}-D_p-1$. Here $T(t_0)$ contains the selected positions on that orbit. $g_U$ is a model gain. The remaining symbols are the named error and cost terms in the source. [Full local inequality](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/Conclusion1OfGainBoundAll.lean#L129) |
| Two prime ranges | For a candidate $p<p_0(k)$, `starAt_D` uses `gU_lower`, nonnegativity of $M$, orbit sizes and explicit scalar bounds. For a candidate $p_0(k)\le p<X'$, `starAt_E` also uses `kinkHH`, the cyclic count above transported to the orbit, with a fill-offset error bounded by $N_v(b'/x+\eta_{\rm Sz})$. [Gain comparison](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/PartnerCountOfCentral.lean#L308) · [Transport and offset](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/PartnerCountOfCentral.lean#L369) · [Smaller primes](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/PartnerCountOfCentral.lean#L597) · [Larger candidate primes](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/PartnerCountOfCentral.lean#L696) |
| One prime | When the accepted representative set $V$ is nonempty, the covered tops partition by representative. The definition of `gainP` gives at least $g_U-\mathrm{Pr}$ on each accepted representative and a nonnegative baseline outside $V$. The sum of the orbit inequalities, the definition of $\tau_p$, and the floor bound pay the stated tally. When $V$ is empty, $\tau_p=0$; the proof also handles primes with full coverage through the baseline or vanishing ramps. [Partition](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/NotSingularOfCentral.lean#L601) · [Empty case](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/NotSingularOfCentral.lean#L636) · [Nonempty case](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/NotSingularOfCentral.lean#L689) · [Net gain definitions](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/IsResidueClassZero.lean#L341) |
| From the tally to the family | Increasing the loss constant by one pays the explicit difference between `askG` and `askP`. The family proof supplies the good-orbit and numerical hypotheses and also uses a bound for the prime-dependent $\mathrm{ep}(p)$ when assembling the floors. [Change of tally](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/GainBoundAllAddOneOfGainBoundAllRequired.lean#L378) · [Family hypotheses](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/StarFam.lean#L29) · [Gain and floor assembly](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums.lean#L57) |
| From numbers to a lattice | `AuxBlock8.Conclusion1` bounds a numerical gain. `linkG_at_core` uses the family’s `ParametersFill` equalities to identify the gain, covered tops and corrections at a place. `WeilJacquetShalikaLaw.Conclusion1` has a different conclusion, a valuation bound on lattice columns; `admissible_off_twist_places` applies it to a period. The matching names led Addendum 9 to the valuation branch. The direct numerical covering supplier is `AuxBlock8.Pf.stmtF`. [Numerical statement](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/SmallOrderPrimes.lean#L15) · [Supplier call](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L232) · [Use at a place](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L761) · [Column statement](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/WeilJacquetShalikaLaw.lean#L97) · [Valuation application](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean#L171) |

**READ / DERIVED.** The finite lemma holds for every marked subset. Applying it inside the full bound also requires a good orbit with enough marked positions relative to its length, weights in range, and numerical error bounds. For example, `orbit_facts` extracts $|\mathrm{orb}|\,\delta_1\le N_v C_{31}\log x$. These hypotheses describe finite configurations and size estimates. No hypothesis of the standalone counting lemma mentions $\zeta$, its zeros, or $G_\zeta$. This check covers this branch only. [Orbit density](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/PartnerCountOfCentral.lean#L471) · [Eventual size estimates](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/LogarithmicSums/StarFam.lean#L19) · [Density supplier](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SharpRestriction/GrowthBounds/TopChoiceBounds.lean#L4394)

#### Correction to the loss size in Addendum 9

**READ / DERIVED.** Write $U=n_Tmb$ and $a=xb$. The upper bound allocated to uncovered pairs is $4am n_T x^{-2+\varepsilon}=4U x^{-1+\varepsilon}$. For the full signed tally difference, the bound in `joint_core` is
$$
\mathrm{ASK}-\mathrm{Ga}
\le (2C\log 4+13\,\mathrm{sg})U
\le (3C+13)U,
\qquad \mathrm{sg}=100Kx^{-1+4\varepsilon}.
$$
There is an explicit source for the constant-sized allowance. The ledger uses $t_{\rm PrHigh}=2(\log 4)mn_T X'Q_2$, and expanding $X'Q_2$ produces a $Cb$ term, giving $2C(\log 4)U$. This concerns the error allowance. The actual signed loss could be smaller. $e_L=0$ therefore means a constant multiple of $U$ suffices with no extra power of $x$. [Uncovered pairs](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/PrimeClassLossHypothesesSatisfiable.lean#L60) · [High-price term](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/WindowSettingSatisfiable.lean#L139) · [Expansion](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/OneLeThresholdMulPowers.lean#L444) · [Total bound](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/DiscriminantSettingSatisfied.lean#L196) · [Final constant](https://github.com/Deicyde/riemann-hypothesis/blob/e50d09817ad81469f737e8f637561e6ccf86c670/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/DiscriminantSettingSatisfied.lean#L220)

#### Next handoff for Claude or VS Code

~~~text
Use commit e50d09817ad81469f737e8f637561e6ccf86c670. Continue with the rarity of bad (prime, top) pairs. Addendum 10 already gives the deterministic covering for one good orbit. The remaining question here is why a single choice of the marked set T works in the weighted sum over primes.

Start in src/Formalism/SharpRestriction/GrowthBounds/TopChoiceBounds.lean at bad_orbit_prob_eq_conditional (:2352), SharpTopsChoiceInequality (:2568), and tops_choice_of_sharp_inequality (:2577). Trace the supplier near :2805–2890. Write out which bad events are counted and how each gets its power of x, including conditioning on a specified position being selected. Explain how the one-orbit probability estimate turns into existence of one T for the prime-weighted sum via src/Formalism/SharpRestriction/AdmissibleParameterJoins/GandSa.lean:23–69. Then verify which selection is used for the actual family’s TT through ChBad_at and chosenBadp_of_old. Keep the different estimate for second-kind primes (ChW_at) separate. Label READ, DERIVED and COMPILED. Return a paper proof for the strongest step verified, its hypotheses, and the first input still unproved independently.
~~~

## Addendum 12 — why one random sprinkling of tops works for every prime at once (Claude, 2026-11-21; GPT's task, GPT out of credits)

Tags as in Addendum 7. Paths under `src/Formalism/SharpRestriction/`. `TCB` = GrowthBounds/TopChoiceBounds.lean. Nothing compiled.

### The picture

Run a lottery once: keep each spot of the group with probability δ = x^(−ε/8). For any one prime and any one spot, the chance that the spot is kept **and** its loop under that prime looks bad is tiny, at most δ·Cb·x^(−2). So the *expected* bad weight, summed over all primes with weights log p/p, is tiny. One draw that is at most 4 times its expectation, and also has about δn spots, happens with probability at least 1/2. So such a draw exists, and it works for all primes at the same time. The proof never needs a separate sprinkling per prime, because it averages the weighted total, not each prime separately.

### The chain (READ)

1. **Per-spot bound** — `bad_orbit_prob_eq_conditional` (TCB:2352): P(t ∈ T and t's loop under h is bad) = δ · condProbAt(i₀), where i₀ is t's position on its loop of length ord(h) and the conditional probability assumes that position is selected. `tops_choice_of_sharp_inequality` (TCB:2577) turns `SharpTopsChoiceInequality` (TCB:2568) into `BadPrimeBound` = `BadProb` (AdmissibleParameterJoins/GandSa.lean:23): that probability is ≤ Cb·x^(−2)·δ for every h with ord(h) ≥ x^(ε/4).
2. **The three bad events on one loop** (`good_orbit_failure_prob_le`; sum must be ≤ Cb·x^(−2) for every loop length n′ | n with n′ ≥ x^(ε/4)):
   - clusters (window condition): L₂·C(L₂,K)·δ^K + n′·C(L₂,K+1)·δ^(K+1);
   - too few marked tiles: n′·(1 − markedBound(δ, r, u))^M₀;
   - too many marks in an interval: n′·binUpper(G′, δ, N₁ − 1).
3. **One T for all primes** — `tops_exist_of` (GandSa.lean:47) uses `UnusedSlot33.Conclusion6` (GlobalSchurBounds/CMFieldLemmas.lean:116): if every per-spot bad probability is ≤ β·δ and δn ≥ 16, then some T has δn/2 ≤ |T| ≤ 2δn **and** Σ_p ω_p·#(bad t ∈ T at p) ≤ 4·β·δ·n·Σ_p ω_p. It is proved from `SecondMomentBadEventsBound` (GlobalSchurBounds/ConclusionR7abs.lean:171, 182). `TopsOK` (GandSa.lean:30) is that conclusion with ω_p = log p/p over `largeOrderResiduePrimes`.
4. **The family's condition** — `ChBad_at` (GlobalSchurBounds/Chosen.lean:34) is exactly TopsOK's third clause. `chosenBadp_of_old` (GlobalSchurBounds/LossesSmallShares.lean:357) converts it, with the size of TT, into the bad-pair form `ChosenBadp` used by the loss proof (Addendum 9).

### Paper proof of the extraction step (DERIVED; matches the statement of Conclusion6)

Let T be a random subset, each spot kept independently with probability δ, and let W(T) = Σ_p ω_p·#{t ∈ T : t bad at p}. By linearity, E[W] = Σ_p ω_p Σ_t P(t ∈ T, bad) ≤ Σ_p ω_p · n · βδ. Markov: P(W > 4E[W]) < 1/4. |T| is a sum of n independent Bernoulli(δ) variables with mean δn and variance ≤ δn. Chebyshev: P(||T| − δn| > δn/2) ≤ 4/(δn) ≤ 1/4 when δn ≥ 16. So with probability > 1/2 both good events hold, and some T satisfies both. (Edge cases such as E[W] = 0 are handled in the source.)

### Where each power of x comes from (READ definitions; ratios DERIVED)

- δ = x^(−ε/8) (`delta1`, SizeWindowBrackets/GrowthBracketBoundOfSizeWindows.lean:102).
- K = ⌈8(hG + 2)/ε⌉ with hG = 2 + 8ε (GrowthBounds/IsResidueClassZero.lean:37-41), so δ^(K+1) ≤ x^(−(4+8ε)) · x^(−ε/8).
- L₂ = 2·max over inert p of ⌈log_p((k·x^A)^4)⌉ (:53) is O(log x), so C(L₂, K+1) is only a power of log x (K depends on ε only).
- With n′ ≤ n ≈ x^(2+8ε), the cluster term is about x^(−2−ε/8) times a power of log x, which is ≤ Cb·x^(−2) eventually. The choice hG = 2 + 8ε matches n ≈ x^(2+8ε). That size of n was read from the PChain construction and is **not re-verified on the headline path**.
- The tiles term uses M₀ = `orbitSmallMultiplicity` ≈ (hG+3)·log x·10^(6r+1) (GrowthBounds/UnramifiedQuadraticSetting.lean:243). The intervals term uses `binomial_tail_le_choose_mul_pow` (binUpper(G, δ, N) ≤ C(G, N)·δ^N). Their numerics were not re-derived.

### Does it deliver the size the loss proof needs? (DERIVED)

`ChBad_at` gives bad weight ≤ 4·Cb·x^(−2)·δn·Σ log p/p. With δn ≤ 2|T|, Σ_{p<X′} log p/p ≤ 2 log X′ = 2x^(ε/3) (`MertensBound`, GrowthBounds/CornerGLContinuity.lean:108), and 16·Cb ≤ x^(2ε/3) eventually (the `ev_le_rpow (2ε/3) (16·Cb)` step in `chosenBadp_of_old`), the bound is ≤ 16·Cb·x^(−2+ε/3)·|T| ≤ |T|·x^(−2+ε). That is the nT·x^(−2+ε) required by `OutD` (Addendum 9). Yes.

### Scope and first unproved inputs

- Covers only large-order primes (ord ≥ x^(ε/4)). Small-order primes are "first kind" (`first_kind_bound`). Second-kind primes (`ChW_at`, `lhsW ≤ x^(−9)`) use a separate estimate. Neither was traced here.
- Not read: the proof of `SecondMomentBadEventsBound`; the numerics inside `good_orbit_failure_prob_le`; the family hook-up through `family_tops_choice_of_mertens` (TCB:4452).
- First input not independently proved: the n-size on the headline path, and the tiles/intervals numerics.

## Addendum 13 — the "can't squeeze the orchard" rule (`SlopeIneq`) is geometry of numbers plus linear algebra, given near-orthogonality (Claude, 2026-11-21)

Tags as in Addendum 7. Paths under `src/Formalism/`. Nothing compiled.

### The picture

Many small grids (one per family member u) all feed into one target grid through linear maps. If those maps spread evenly in every direction (a near-"tight frame"), the small grids cannot be denser on average than the target grid, up to small corrections. "Evenly spread" is checked by asking that any two different maps barely overlap (tiny cross-talk) and that each map alone is close to an isometry. So the averaging rule needs one real input: **the family members are nearly orthogonal to each other**. That input is where the next layer of depth sits.

### The chain (READ)

1. `SlopeIneq` (RankGapBounds/MeanBoundSecondForm.lean:151) is supplied by `frame_at_of` (SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean:538) → `joint_a_ramified_holds` → `ramification_condition_holds` → `flat_lattice_theorem_holds` (SizeWindowBrackets/ChainSlopeWindows/JointDModelAppliesUnitLattice.lean:187-258) → `TheoremFLat` (SizeWindowBrackets/FrameTraceRatioFinEquiv.lean:162) = `theoremF` = `frame_theorem_log_ideal` (HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean:400).
2. **Statement** (`TheoremFLat`): for a CM field K, target lattice cc ⊂ W, lattices N_i ⊂ V_i and maps B_i : V_i → W, if
   - `LatNum`: s·Σ dim ≤ Σ dim_i·(μ(N_i) − h_i), and μ_max(N_i) − h_i ≤ s + u,
   - `FrameDeviationLinear` (:46): Σ_i ‖γ_i·B_i*B_i − Id‖²_HS ≤ e·Σ dim_i, with e ≤ 1/4,
   - `FrameTraceRatioLinear` (:51): tr(Q²) ≤ (1+η)·tr(Q)²/dim W for Q = Σ γ_i B_i B_i* (Q is close to a multiple of the identity),
   - `LatGeom`: geometric compatibility (invertible metrics, ranks),

   then s − log|I| − (1−δ)⁻¹·[4u·log(1 + HH/u) + (η + 4√e)·HH] ≤ μ(cc).
3. **Ingredients of its proof:**
   - `FrameLA1` (HarderNarasimhan/StatementFrameF.lean:11; proved `frame_linear_algebra_first`, HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean:77, 223 lines, pure linear algebra over ℂ): if the maps form a near-tight frame (e, η) and subspaces Nτ_i ⊂ V_i have total codimension ≤ ε·Σ dim, then the part of H missed by the images of the Nτ_i has dimension ≤ (η + 4ε + 4√e)·dim H.
   - `thmF_share` (HarderNarasimhanProofs/TheoremFSharp.lean:11), a reverse-Markov fact: if numbers average at least s and none exceeds s + u, then at most a u/(u+τ) share fall below s − τ.
   - Harder–Narasimhan slope theory for hermitian lattices (`HNSlopes`, `SlopeIneq`, `Duality`, … in HarderNarasimhanProofs/; classical: Stuhler, Grayson, Bost). Not read line by line.
4. **The family's frame input**: `frame_at_of` needs `FrameReal_at` ← `MatReal_at` ← `MatSF` (TopDensityNGeSixteen.lean:658, 691, 740) ← `matSF_of` (:862) from `LinkS`. `LinkS_at` (SharpRestriction/GlobalTheoremInputs.lean:145) says that for different family members u ≠ u′ the cross-kernel has ‖·‖²_HS ≤ (1+η0)·d_u·d_u′/D*, that each diagonal kernel is within e0·d_u of the identity, and that D_all ≤ (1+η1)·D*. On the family, η0, η1 and √e0 are all ≤ exp(−x^(ε/8)) (`MatSF`, :740-744): essentially exact orthogonality.
5. **Who proves the near-orthogonality**: `LinkS` is supplied from LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ (`LinkSFinal.lean:83`, via `linkS_of_thmSPEv`, `CountE.PLev`, `thmSOwn_of_clauses`, and `kExpTied_holds` built from `FoldOK`, `FundExists`, `OOIntAll`, `AbsConv`, `KExpansion`). The names suggest lattice-point counting and theta-series / Fourier-expansion arguments. **Not read.**

### Interpretation (INTERPRETATION)

The entropy term 4u·log(1 + HH/u) looks like the integral of the share bound u/(u+τ) over thresholds τ from 0 to HH: ∫ u/(u+τ) dτ = u·log(1 + HH/u). That matches how a slope can be written as an integral over thresholds of the "share above threshold". Not checked against the proof body.

### What this means (DERIVED)

- The averaging rule is **not** where the depth lies. Given near-orthogonality, it is linear algebra, a counting fact, and classical lattice theory.
- The depth moves to `LinkS`: why different members of the family of lattices are almost exactly orthogonal (errors ≈ exp(−x^(ε/8))). That is the next target, in SiegelLatticeTheory/FlagStabilizerTensors.
- Status of the four lattice inequalities: `SlopeIneq` is reduced to LinkS (this addendum). `QuotientSlopeBoundsWith` (the places theorem), `DIV` (the explicit degree) and `Slopes` (slope sizes) are still open.

---

## Addendum 14 — the fake-zeta test: `LinkS` is symmetry plus giant size, and the places theorem is exact bookkeeping (Claude, 2026-11-21)

Paths below are relative to `src/` at commit e50d098.

### Method: the fake-zeta test (DERIVED)

Two kinds of counterfeit zeta functions are known to have zeros off the critical line:

- **Davenport–Heilbronn, and Epstein zeta functions.** Epstein zetas are built from lattices and theta series. These have the functional equation (mirror symmetry) but no Euler product.
- **Beurling generalized primes.** These have an Euler product, but there is no additive structure on the "integers" they generate.

So a step whose proof uses only symmetry, lattice or theta structure, or only multiplicativity plus a Chebyshev-strength prime count, cannot carry RH strength by itself. The step that does carry it must use real primes acting on additive structure, at a strength beyond the classical estimates. This addendum applies the test to `LinkS` and to the places theorem.

### 14.1 `LinkS`: symmetry, giant size and a word count (READ at statement level)

**The definition** is at `Formalism/SharpRestriction/GlobalTheoremInputs.lean:144–157` (`LinkS_at`, `GamOf`, `LinkS`). It requires:
- cross HS² ≤ (1+η0)·d_u·d_u′/D*;
- diagonal defect ≤ e0·d_u;
- Dall ≤ (1+η1)·D*;
- η0, η1, √e0 ≤ exp(−x^(ε/8)).

**The supplier** is `linkS_of_standing_hypotheses` at `Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean:628`. Outside the window `Win` (line ~594), `LinkS` holds vacuously, with all η = 0.

It has three ingredients:

1. **Theorem S, i.e. symmetry.** `Conclusion1` at `Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean:212` states:
   - the projected kernel `Kpp D u u′` is exactly **0** for u ≠ u′;
   - ‖Kpp(u,u)‖² ≤ d_u·exp(−k f log k);
   - the remainder `Kmat − Kpp` has cross HS² ≤ (1+eta0)·d_u·d_u′/D*.

   `linkS_concl` (StandingHypothesesHoldFamily.lean:186) reads off eta0 = b^(−6).

2. **Giant size.** This is `eF_nonneg_and_le_exp_neg` (:206) together with `size_thresholds` (:48).
   - `scL_eq` gives L = y⁸ = x^ε with y = x^(ε/8), and b = e^L. So **η0 = b^(−6) = e^(−6x^ε)**.
   - The diagonal error is eF = 2C0/Γ + 2·exp(−k f log k) (`FrobeniusProjectedBounds.lean:164`).
   - Here Γ = exp(CGam·m⁵·f·L), and the rank satisfies k ≥ 8·log Γ ≥ 8·CGam·x^ε.

3. **A combinatorial count.** `adm7` at `Formalism/SharpRestriction/CuspSpanNormBounds/FrobeniusProjectedBounds.lean:105` gives |Dall − D*| ≤ exp(−c·n f log n)·D*.
   - D* = (T−1)^f (`Formalism/SizeWindowBrackets/ChainSlopeWindows/ChainLatticeSizesModelEventually.lean:704`) counts words of length f over T−1 letters.

**Verdict (DERIVED).** At the level of statements, this layer has no prime-distribution input:
- exact orthogonality comes from symmetry;
- the tiny errors are bought by size;
- the count is of words.

It would pass for a counterfeit, so it is not the mechanism. *Caveat:* Theorem S's own proof (clauses `ClKppOff`, `ClKppDiag`, `ClOff`, `ClDiag`, fed in at `LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LinkSFinal.lean` ~73–76) and the proof of `adm7` are NOT read yet. Arithmetic input could hide there.

### 14.2 The places theorem (`QuotientSlopeBoundsWith` side): a per-place ledger (READ)

**Statement:** `Places_at` at `Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean:1516`, and `PlacesF` at `:1541`. The consumer is `slopesN_at_of` (`:1529`), which produces `SlopesN_at`.

**Proof chain:** `placesF_min'` (`Formalism/LocalToGlobal/GlobalTheory/PlacesMin.lean:23`) → `places_at_of` (`Formalism/LocalToGlobal/GlobalTheory/PlacesP.lean:297`).

**The ledger** is all of `Formalism/SizeWindowBrackets/ClaimGaFree.lean` (106 lines, namespace `UnitWeightPartition`):
- `Ga` = 2·Σ_w l(w)·(Σ_j gain_j(w) − τ(w)) (:14).
- `HypLow` (:65): new slope μN = μMu + Σ_w 2·l(w)·(sg′(w) − τ(w)) − BeSum. Here BeSum = Σ_w 2·l(w)·(len(w) − d_u·τ(w))/d_u (:32–36).
- `ClaimUnit` (:48): if the place weights above each p sum to log p, then IO = 2·Σ_p log p·iop(p).
- `ClaimLow2` (:87): μM + Ga + Fo − Ee − (4·IOp + LT + RX + 1) ≤ μN.
- `ClaimHigh` (:99): μmaxN ≤ μmaxM + Ga + Fo − Ee.

**Plain reading.** Change a lattice at a place above p by local length ℓ, and its log-volume moves by ℓ·log p, because the index of a sublattice factors over primes. The ledger simply adds up these per-place moves.

**What `places_at_of` actually uses:**
- local length bounds `LocLe` at each place;
- the rank formula rank = d_u·(1 − 1/(T−1))^f, with `deficit_bounds`;
- Σ sz(τ) ≤ b², from `tau_sum_family_of_mertens` (`Formalism/SharpRestriction/GrowthBounds/TopChoiceBounds.lean:4503`).

**The only prime-size fact** is `mertens` at `PlacesP.lean:441`: Σ_{p<y} log p / p ≤ 2·log y. That is Chebyshev strength.

**Size terms carried** in `Places_at`:
- LT ≤ C·|TT|·m·(a/k + b′)·log T;
- RX ≤ C·X″(n).

**Verdict (DERIVED).** This *is* the step where real primes meet the additive lattice, so it passes the "uses both" criterion. But its content is an exact identity (log of index = Σ length·log p) plus a Chebyshev-strength prime bound. It contains no estimate at RH strength, so it is not the mechanism by itself.

### 14.3 Consequence and next target (DERIVED; a hypothesis to test, not a result)

- Every component opened so far falls into one of these kinds:
  - classical estimates (Siegel–Walfisz, Page, Siegel, zero density);
  - exact bookkeeping (transfer, ledger, UnitRule);
  - combinatorics (kink matching, lottery, word counts);
  - symmetry plus size (`LinkS`).

  So RH strength cannot sit in any single opened component. Our working hypothesis is that it comes from the **assembly**, which has three parts:
  - the analytic prime sum is captured as a lattice gain, with ASK − Ga ≤ (3C+13)·nT·m·b (Addenda 9–12);
  - the lattice is near-semistable: no sublattice beats the average slope by more than logW + Φ (Addendum 13 plus 14.1);
  - the average is fixed by `DIV`.
- If so, the exponent 1/2 is decided entirely by the **error budget**:
  - LoP + E + logW + Φ;
  - which includes LT, RX, IOp and (3C+13)·nT·m·b;
  - all normalized by the scale b = e^(x^ε).
- **Next target: a budget audit.** On the headline path (eD=2, eL=0), write each error term as a power of x, identify the largest, and check that the total lands at x^(1/2+O(ε)).
  - Start from `errorBracketSizeWindows` (`Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean:133`): nT·aE·(1 + m²/k) + m·(2n·m·b·x^ε + nT2·k·b·x^ε/(n·n·x^(−ε))).
  - Also use the hypotheses of `ch_core`: m ≤ x^(1/2+ε/2) and x·m ≤ k (`Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChCore.lean:343`).
- **Still open:**
  - `DIV`: Euler's γ occurs in 137 files, so grep doesn't localize it;
  - `Slopes`;
  - the proof of Theorem S;
  - the proof of `adm7`.
- **Caution on names:** at least 15 distinct definitions in different files are all named `KudlaFamilyStatement`, with different content. Go by statements, not names.

---

## Addendum 15 — budget audit, first pass: where the √x is spent, and which lattice rules carry it (Claude, 2026-11-21)

Paths below are relative to `src/` at commit e50d098.

### 15.1 What the lattice must deliver (READ)

- `gapA D N ell TT a w u0` = Σ_{t∈TT} Σ_{j<m} (ASK(a t, t, w_j) − MAIN(a t, w_j)). This is the prime sum minus the main term, summed over nT tops and m pieces each (`Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean:50`).
- `ch_top` (`Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean:37`) proves gapA = ASK u − Main u ≤ x^(CErr·ε)·errorBracketSizeWindows. It does this in three steps:
  - `MeanBoundWith`, which is the eleven inputs ⇒ umean ASK ≤ umean Main + `errorTermWith` (`Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean:56,67`);
  - `ErrorFormsUnderWindows`, which gives errorTermWith ≤ x^(CErr·ε)·`ErrText` (`Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean:54`);
  - ErrText = nT·a·(1 + m²/k) + m·(B0 + Nc) (`:16`), where `BNBoundsU` (`SplitInertia.lean:74`) gives B0 ≤ 2n·m·b·x^ε and Nc ≤ nT2·k·b·x^(2ε)/n². Here n = |H|.
- The bracket itself, `errorBracketSizeWindows`, is at `Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean:133`.

### 15.2 How the bracket becomes x^(1/2) (READ)

- `core` (`ChCore.lean:283`): nT·m·b·(δ2/2)·Y ≤ Err + 2·nT·m·b/x, where Y = G − 4x^(1/2+ε), G = GmA − SigA and δ2 = |T2|/|H| (`Formalism/SizeWindowBrackets/GrowthBoundGivesRiemannHypothesis.lean:41`).
- `ch_core` (`ChCore.lean:343`) concludes GmA ≤ x^(1/2+(C+3)ε) + SigA. Its size conditions are `RestSize` (`Formalism/SizeWindowBrackets/SChain.lean:53`) together with the `SizeWindowsSplit` extras (`:114`):
  - aE ≤ 2xb;
  - nT ≥ x^(−ε/8)·n/2;
  - nT2/n ≥ x^(−ε);
  - x^(1/2−ε) ≤ m ≤ x^(1/2+ε/2);
  - x·m ≤ k ≤ n²·x^(1/2−ε).
- The separate 4x^(1/2+ε) comes from the character side (`one_char`). The proof bounds it very crudely: |M|·A1 ≤ x^(1/4), times x^(1/4+ε). It looks like generous slack, not the binding constraint (DERIVED).

### 15.3 The per-piece budget (DERIVED: divide ErrText by nT·m·b·δ2/2)

| bracket term | per piece | uses | lattice inputs carrying it (by constant name in `errorTermWith`) |
|---|---|---|---|
| nT·a·(1 + m²/k) | ≲ (x/m)·x^(O(ε)) | a ≤ 2xb, k ≥ xm, m ≥ x^(1/2−ε) | Count5 (`cCount`), DIV (`cDiv`), Slopes (`cSlope`) |
| m·B0 | ≲ m·x^(O(ε)) | B0 ≤ 2n·m·b·x^ε, n/nT ≤ 2x^(ε/8), m ≤ x^(1/2+ε/2) | DIV (`cDiv`), EComp5 (`cE`) |
| m·Nc | ≲ (k/(n·nT))·x^(O(ε)) ≲ x^(1/2+O(ε)) | k ≤ n²·x^(1/2−ε) | DIV (`cDiv`) |
| LoP, log\|W\|, MLo5, Φ | absorbed | LoP = (3C+13)·nT·m·b; Φ needs (η̄+4√ē)·x^cHH·b ≤ K·x^ε·nT·a (`ErrWindows`, `:43`) | LossBounds, word count, SlopeIneq + LinkS |

**Plain picture: cutting a log.** Some costs are paid once per top: the counting, degree and slope errors (Count5, DIV, Slopes), each about (size of the numbers)·x^ε. Those get shared across the m pieces, so each piece pays about x/m. Other costs grow as you cut finer (B0 ∝ m). Balancing the two gives m ≈ √x. This is the `sqrt-balance` clip, now traced to its source terms.

**Why `LinkS` needs η0 = b^(−6).** `ErrWindows` requires the frame errors, multiplied by the scale b, to stay below nT·a·x^ε. With b = e^(x^ε), the overlaps therefore have to beat 1/b. That is exactly what Addendum 14.1 found: η0 = b^(−6), and Γ = b^(CGam·m⁵·f).

### 15.4 Consequence (DERIVED)

- The square-root saving is the statement that **the per-top errors of Count5, DIV and Slopes do not grow with the number of pieces m.** Their errors are about a·x^ε per top, while the signal grows like m·a.
- So the three lattice rules still unread (**Count5, DIV, Slopes**) are precisely the ones whose accuracy sets the x/m term. The next reads should be those three, asking one question of each: why is its error independent of m? A rank of k ≥ x·m, which makes room for m pieces, is the obvious suspect.
- Status of "do we understand the lattice":
  - its **job**: yes, as in 15.1–15.3;
  - its **books**: mostly — the transfer, the ledger, LossBounds, covering, the lottery, SlopeIneq given LinkS, and LinkS at statement level;
  - **what it is and why its rules hold**: no — not the construction (number fields, Frobenius, words over T−1 letters), not the proof of Theorem S, and not Count5, DIV or Slopes.

---

## Addendum 16 — the three measuring rules (Count5, DIV, Slopes) and where γ enters the lattice (Claude, 2026-11-21)

Paths below are relative to `src/` at commit e50d098. The question asked of each rule: **why doesn't your error grow with the number of pieces m?**

### 16.1 Statements (READ)

- **`Count5`** (`Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean:27`).
  - Lower bound: log T ≥ Σ_{j<m} (1/f)·Σ_ρ log(w·v/π) + m·lg − cCount·(La + m²·La/k).
  - Upper bound: log T ≤ cCount·m·L.
  - Variation: the spread of log T across u is at most cCount·log k.
- **`DIV`** (`Formalism/RankGapBounds/MeanBoundSecondForm.lean:118`): μCC + h − Fo ≤ Σ_t [m·(ph(a_t) − a_t·logOm) − a_t·log T] + cDiv·nT·a·La + cDiv·m·(B0+Nc)·x^(eDiv·ε).
  - Here ph(y) = y·log y − y (`:9`) and logOm = gam + log(π/v) − LpL (`logOm`, `:88`).
- **`Slopes`** (`:139`): −cSlope·nT·a·La·(1 + m/k) ≤ μM and μmaxM ≤ cSlope·nT·a·La.
- **`EComp5`** (`QuotientSlopeBoundsWith.lean:24`): |Ee − m·sumA·lg| ≤ cE·m·B0.
- For comparison, **`Main`** (`MeanBoundSecondForm.lean:107`) = Σ_j Σ_t a_t·(log a_t − 1 − gam + LpL − (1/f)·Σ_ρ log w).

### 16.2 How m enters (DERIVED)

In all three rules, m reaches the error only through **m/k or m²/k**:

| rule | error | m-dependence |
|---|---|---|
| Count5 | La·(1 + m²/k) | m²/k |
| Slopes | nT·a·La·(1 + m/k) | m/k |
| DIV | nT·a·La + m·(B0+Nc)·x^ε | the first term has no m; the second is the "m-cost" of 15.3 |

The windows force the rank to be large: `ErrWindows0` requires x·m ≤ k (`ErrorFormsWeakWindowsFalse.lean:28`). So m/k ≤ 1/x and m²/k ≤ m/x.

**Plain picture:** the lattice has at least x directions of room for every piece, so the pieces never crowd each other.

There is also an upper squeeze on the rank. `ZWindows` (`Formalism/SizeWindowBrackets/TranslateWordBoundHypotheses.lean:35`) needs m ≤ k, f·k² ≤ nT·a and f·k·(b′+Sc) ≤ nT·a. `RestSize` needs k ≤ n²·x^(1/2−ε).

### 16.3 Suppliers (READ)

- **Slopes:** `ZToSlopes` (`TranslateWordBoundHypotheses.lean:62`). It takes `PropZ`, two-sided bounds on μM and μmaxM by `ZiiR`/`ZiiiR` measured in units of unitZ = nT·a·La (`:18–31`), plus `ZWindows`.
- **Count5:** `Prop5ToCount5` (`:100`). It takes a count X with `BoundedBy'` (error c5·(L + m²L/k)), `Variation5`, and `LevelWindow`, which says T ≈ X·Γ^(−2/(f·k)).
- **DIV:** `DivOfFree` (`Formalism/SizeWindowBrackets/SBrDiv.lean:59`) combines `DivFree` with `Per`. On the headline construction this goes through `MkDivOfFree` (`:397`) with `PerMk` (`:394`) and `PerHost` (`Formalism/SizeWindowBrackets/Chain2aCoreNoAnalytic.lean:512`).
  - `PerHost`: **logOm = γ + log(π/hostV) − Re hostEll(chC)**.
  - `hostV` = 2^(e − 2^(−e))·√(q·d) (`:510`).
  - `hostEll ψ` = **the derivative at s = 1 of the primitive Dirichlet L-function** of the host character (`:368–374`).
- **Not located:** the actual proof of `DivFree` on the headline path. `divisibility_free_at` (`ChainSlopeWindows/PBrDiv.lean:454`) only proves DivFree ↔ DivAt, which is a restatement.

### 16.4 Where γ enters the lattice (READ for the formula; DERIVED for the reading)

Per piece, DIV's main term is a·log a − a − a·logOm. Substituting PerHost gives:

a·log a − (1+γ)·a − a·log(π/hostV) + a·Re L′(1,χ).

The first two terms are the detector's main term x log x − (1+γ)x (StatementOC.lean:11–13), written in a-units. **So DIV is the rule that makes the lattice's total size reproduce the zeta-specific main term.**

The shape (γ, log π, powers of 2, and L′(1,χ) for characters of conductor about 2^e·q·d) is that of a height/period formula of Chowla–Selberg or Colmez type. In such formulas γ and log 2 arise from Γ′/Γ(1) = −γ and Γ′/Γ(1/2) = −γ − 2 log 2. *This is a reading, not verified.*

### 16.5 Answers and next target (DERIVED)

- **Count5 and Slopes:** the error does not grow with m because the rank satisfies k ≥ x·m.
- **DIV:** the statement itself puts the error per top. Why that holds is in the unlocated proof of `DivFree`.
- **Fake-zeta test (Addendum 14):** DIV uses real Dirichlet L-values L′(1,χ) and real primes q, d. It is the first opened rule that ties the lattice's size to genuine arithmetic at full strength. **It is now the top candidate for the mechanism.**
- **Next:** locate and read the proof of `DivFree` for `mkData` (the lattice degree computation), and check whether `PerHost` is proved as a theorem or carried as a defining choice of logOm.

---

## Addendum 17 — where γ really enters: the Chowla–Selberg period of a CM elliptic curve (Claude, 2026-11-21)

Paths below are relative to `src/` at commit e50d098.

### 17.1 Is the γ formula a theorem or a definition? (READ)

**As bookkeeping, it is a definition.** `logOm` is *defined* with γ on the lattice side:
- `Formalism/LocalRingCardinality/DataParams₂.lean:224`: logOm := γ + log(π/host.v) − logDerivativeAtOne.
- The same definition appears at `Formalism/LocalToGlobal/Divisibility/Numbers.lean:68` and as `logOmVal` at `Formalism/LocalToGlobal/KernelLattices/ColumnData.lean:49`.
- Here logDerivativeAtOne = Re L′/L(1, χ_d), where χ_d is the quadratic (Legendre) character mod the prime d (`Numbers.lean:64–66`), and v = rd/2 (`:55`).
- The lattice MAIN term (`DataParams₂.lean:232`) is Σ_t [m·(phF(a_t) − a_t·logOm) − a_t·log T].

γ is also written by definition into the analytic main term: MAIN(ell, a, w) = a·(log a − 1 − γ + ell(chC) − avg log w) (`Formalism/SizeWindowBrackets/FirstPrimeNeSecondPrime.lean:89–91`).

`PerHost` / `PerMk` simply pin the existential logOm to this value.

**As content, the γ is earned by a theorem.**

**The headline degree bound** is `LinkDIV_at` (`Formalism/SharpRestriction/GlobalTheoremInputs.lean:77–89`): μDual + h − Fo ≤ MAIN + C·|TT|·a·La + C·m·(B0+Nc)·x^(Cabs·ε).
- Its supplier on the headline is `linkDIVt_closedK` (`Formalism/LocalToGlobal/Divisibility/RecBridgeSel.lean:369`), taking `BridgeRowsK` (`:329`) with `pkg : DivisionPackageKernel` (`:268`, which extends `DivisionPackageColumns`, `RecBridgeTied.lean:130`).
- It is passed in at `Development/AutomorphicArithmetic/CharacterBoxes/ShapeWin.lean:43` and arrives at `topDesWin`'s hDIV (`DesWin.lean:18`).
- Because the main term carries the factor m while the error does not, this bound must get the γ-term right to relative precision about La/m.

**The Chowla–Selberg period theorem**, `GlobalTheory.T.chowla_selberg_period` (`Development/AutomorphicSpectrum/Proofs/GeometryProofs/ChowlaSelbergPeriodStatement.lean:9`).
- Statement: for a CM field E with host H, a Kronecker character χ mod d, and ρ² = −d, there is a CM curve `Curve0 H ρ` with a period x satisfying
  **x = γ + log(2π/√d) − L′(1,χ)/L(1,χ).**
- Proof: `exists_curve0_hasPeriod` (`ChowlaSelbergPeriod.lean:18`), via `exists_cmEllipticCurve_integers_with_period` and `exists_cmEllipticCurve_withPeriod` (not read).

**The flat degree uses it.** `FlatDegree` (`Development/AutomorphicSpectrum/Statements/GeometryStatements/FlatDegree.lean:12`) states:

N.deg = ((p−q)/2)·Re logOm(E,χ) + q·(2·log √d − log rootDiscr E).

It is proved as `flatDegree` (`Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHolds.lean:60`). Along the way, `flatDegree_logOm_re` (`:41`) gives Re logOm(E,χ) = x − log rootDiscr E + log √d, with x the Chowla–Selberg period.

**Import chain from `Main`** (shortest path, computed from the import lines):

Main → MainTheoremsAll → MainTheoremsCritical → MainTheorems → CharacterBoxes.MainConclusion → EveryCharacterOfLiteratureOfVWin → HodgeBundleWeights.TopCovolSlim2Use → MoriwakiBigness.HilbertSamuelApplications.{TopCovolSlim2Use, AhSlimU, DeepStROfUse, GoodTowerVolumeTheoremBis} → GoodTowerVolumeTheoremAlt → FinalTheoremOfInputsRight(Statement) → GoodTowerVolumeTheorem(Statement) → FlatDegreeHolds(Statement) → ChowlaSelbergPeriod(Statement).

`good_tower_volume_theorem` (`Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerVolumeTheoremStatement.lean:26`) concludes `GoodTowerExistsX ∧ VolumeTheoremX`.

*Caveat:* this shows Chowla–Selberg is compiled into the headline build and feeds a volume theorem (an arithmetic Hilbert–Samuel / Moriwaki-bigness type application). That the `LinkDIV` proof uses `flatDegree` at the term level is likely but NOT yet traced. `ShapeWin`'s own import closure does not contain it; the suppliers are passed in from higher up.

### 17.2 Numerical check (COMPUTED, mpmath, 30 digits, numerical derivative)

The functional equation of L(s,χ_d), for odd χ_d (d ≡ 3 mod 4), gives

γ + log(2π/d) − L′/L(1,χ_d) = L′/L(0,χ_d).

Here γ and log 2 come from Γ′/Γ(1) = −γ and Γ′/Γ(1/2) = −γ − 2·log 2. Checked for d = 3, 7, 11, with |difference| ≤ 3·10⁻¹⁰:

| d | L′/L(0,χ_d) | γ + log(2π/d) − L′/L(1,χ_d) |
|---|---|---|
| 3 | 0.948198826 | 0.948198826 |
| 7 | 0.453546892 | 0.453546892 |
| 11 | 0.101415763 | 0.101415763 |

So the Chowla–Selberg period in 17.1 is **x = L′/L(0,χ_d) + ½·log d** (DERIVED).

**Reading (DERIVED, normalization-dependent):** Colmez's form of Chowla–Selberg for a CM elliptic curve E with CM by Q(√−d) is h_Fal(E) = −½·L′/L(0,χ) − ¼·log d. So x is, up to a normalization constant, **−2·h_Fal(E)**. In other words, the lattice's density constant is the Faltings height (the "size") of a CM elliptic curve.

### 17.3 Consequence (DERIVED)

- γ is not inserted ad hoc on the lattice side. It comes from a classical, exact theorem: Chowla–Selberg, equivalently the Kronecker limit formula. That is the "exchange rate" between lattice size and L-function data.
- Being an exact evaluation, it does not by itself carry RH strength.
- It passes the fake-zeta test: it uses genuine CM elliptic curves and real Dirichlet L-values.
- The open RH-strength content therefore sits in the **volume theorem** that turns this per-unit degree into the bound "total degree ≤ m × main term + per-top error". That is `good_tower_volume_theorem` and the HilbertSamuelApplications chain, plus how it reaches `LinkDIV`.
- `nf_Om` (`Formalism/LocalToGlobal/Divisibility/EigenvalueSumLeClosedOf.lean:682`) uses only the crude bound γ < 2/3 to show |logOm| ≤ La. That is a size bound, not the identity.
- **Next target:** read `good_tower_volume_theorem`'s statement (`VolumeTheoremX`), and trace term-level how `BridgeRowsK.pkg` (the degree bound) is produced from it on the headline.

---

## Addendum 18 — cross-check against the external guide "The proof of the Riemann hypothesis announced by L. Alpöge: a guide to its architecture" (Claude, 2026-11-21)

**Source.** An 11-page PDF by "riemann-rev", dated 2026-11-20, uploaded by Timmy as `proof-guide.pdf`. It is treated as a claim. Every Lean name below that the guide cites was checked to exist at commit e50d098 (READ):

| name | location |
|---|---|
| `key_minor_dvd` | `Formalism/SharpRestriction/GrowthBounds/CoarseMultiplicity/KeyMinorDvd.lean:132` |
| `slopeInequality_of` | `Formalism/LatticeSlopes/LatticeSlopesProofs/SlopeInequality.lean:111` |
| `ch_balance` | `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChBalance.lean:200` |
| `hostThickExists` | `Formalism/FrobeniusOrbits/FrobeniusOrbitsProofs/ThickExists.lean:181` |
| `supplyChi` | `Development/AutomorphicArithmetic/CharacterBoxes/SupplyChi.lean:8` |
| `window1` | `Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Window1.lean:6` |
| `VWinAt` | `Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean:44` |
| `every_character_of_literature_of_vWin` | `.../ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:810` |
| `ChainInt` | `Formalism/ThetaLiftIndependence/Statement.lean:40` |
| `IsChiField` | `ExistsPageN.lean:19` |
| `BoundedCharsPointwise` | `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Analytic.lean:154` |

### 18.1 The guide's one-line summary of the mechanism

> "Arithmetic geometry bounds a smoothed sum over primes *from above*, by a square root, on sparse but long intervals." The guide calls it "Stepanov over ℤ".

In Stepanov's proof of RH for curves over finite fields, an auxiliary function vanishing to high order at the rational points gives an upper bound on the number of points. Here the dictionary is:
- vanishing to order m ↔ divisibility of an m-fold iterated theta lift;
- counting degrees ↔ Bost's slope inequality;
- finite extensions of 𝔽 ↔ the layers of a cyclotomic tower;
- "upper bounds suffice" ↔ the localized Landau theorem.

**The simplest case (guide §4).** Take a theta function on a CM elliptic curve, with period Ω and invariant derivation D. Then D^a ϑ(0)/Ω^a is divisible by p^(a/p + a/p³ + ⋯ − O(log a)) for each prime p inert in K = ℚ(√−d), much as a! is divisible by p^(⌊a/p⌋ + ⌊a/p²⌋ + ⋯).

A non-zero algebraic integer divisible by many primes cannot be small. By the **product formula**, Σ_p (exponent)·log p ≤ log(size at the infinite places):
- the left side is a ramp-weighted prime sum;
- the right side is computed exactly.

The result is an upper bound on the prime sum.

### 18.2 How our addenda map onto the guide

| guide | our finding | status |
|---|---|---|
| §1 Reflection (`rh_of_right`) | early addenda | ✓ same |
| §2 statistic G(y) = Σ Λ(n)(y/n − 1) − y(log y − 1 − γ) | Gζ, StatementOC.lean:11–13 | ✓ same |
| §3 localized Landau: positive families, k-th derivatives localize, one side suffices | lemmaL / landau_window / window–pole argument | ✓ same |
| §3/§5 weights 1 and 1/(3o+1); tops T with proportion 4/(3o+1) in A₀ | Addendum 12, the lottery (one T for all primes) | ✓ consistent |
| §4(a) ASK(a) = Σ Λ(n)(1 − χ₋d(n))(a/n − w_n)₊; the factor 1 − χ₋d is 2 at **odd powers of inert primes** | ASK and Ga (Add. 9, 14.2); `gam p = p/(p²−1) = Σ_odd p^(−e)`; `kink` matching at odd distances (Add. 10–11) | ✓ explains why odd powers: the exponent a/p + a/p³ + ⋯ |
| §4(a) local source: "if ϖ² = p then ϖ divides a 2×2 minor" | `key_minor_dvd` (hypotheses ϖ² = p, M^(p^e) ≡ N′ mod p) | NEW: located, not yet read in full |
| §4(b) Bost: μ(𝓛) ≤ μmax(𝓛′) + log‖φ‖ | SlopeIneq / Slopes / HN (Add. 13, 16) | ✓ same family; `slopeInequality_of` is NEW |
| §4(c) Chowla–Selberg: log Ω = γ + log(2π/√d) − L′/L(1,χ₋d), together with Rallis inner product, Siegel mass formula and Weyl's formula | Add. 17, same formula (`chowla_selberg_period`) | ✓ exact match; Rallis, Siegel mass and Weyl not read |
| §4 outcome: (1/b)(ASK − MAIN) ≤ x^(O(ε))·(x/m + m + √x), with √(xδ₁) ≤ m ≤ 2√(xδ₁), δ₁ = x^(−ε/8) | Add. 15 budget (x/m, m, and k/n² ≈ √x); `sqrt_mul_rpow_neg_eq` | ✓ exact match |
| "The centring of G and g_χ, Euler's constant included, is the archimedean side of a slope inequality" | Add. 16–17 | ✓ same conclusion |
| §5 averaging over A₀ (`ch_balance`), positivity by design, twisting via mean square over pairs (q, d) | quiet radios: `MeanSq`, `bad_share` (Add. 8) | ✓ |
| §5 auxiliary primes q ≡ 3 (mod 8), d ≡ 7 (mod 16), q ∣ d+1 | GPT's (8/q) = (2/q) note | ✓ consistent |
| §5 thick set T₂ via Behrend (no 3-term APs; a Frobenius orbit meets a translate of T₂ at most twice per H steps) | T₂, δ₂ (Add. 15) | ✓; `hostThickExists` NEW |
| §5 bookkeeping 13/8 + 5 + 1 + 3/8 + 1 = 9 → x^(1/2+9ε) | `core_gm` exponent (eD+eL+7)ε with eD = 2, eL = 0 | ✓ same 9 |
| §6 Iwasawa: Ш lengths bounded on a window (Ferrero–Washington, interval lemma `window1`, `VWinAt ψ 401`) | not read (we saw the windows in DesWin/TopWin, not their source) | OPEN |
| §7 Galois representations for regular algebraic polarized cuspidal π on GL_n over CM fields | not read | OPEN |

### 18.3 What the guide does NOT settle

- The guide states that §§4–7 "are read here from the Lean source and from the announcement, not re-derived". So the hard estimate — the divisibility of the chain of theta lifts, paid for by Iwasawa theory — is machine-checked but not independently explained in human terms there either.
- Its machine-check box reports two independent kernels (Lean and NanoDA) and the three standard axioms. That is consistent with what we saw, but not re-run by us.

### 18.4 Revised map of where the mechanism lives (DERIVED)

- The fake-zeta criterion (Add. 14), "real primes meeting additive structure at full strength", is met by the **product formula applied to a highly divisible non-zero algebraic integer**: the m-fold theta lift at CM points.
- Divisibility is the multiplicative side: inert primes divide it about a/p + a/p³ + ⋯ times.
- Size at infinity is the additive and archimedean side: Chowla–Selberg, Rallis, Siegel mass.
- Neither counterfeit (Davenport–Heilbronn or Beurling) has such an object.
- **Next targets, in order:**
  1. `key_minor_dvd` plus `ChainInt`: why the chain is that divisible.
  2. §6 `VWinAt` / `window1`: how much divisibility is lost, and why only on special windows.
  3. Rallis / Siegel mass inputs to the archimedean size.

---

## Addendum 19 — the local divisibility engine: `key_minor_dvd` is Fermat's little theorem plus "everything collapses onto one line mod √p" (Claude, 2026-11-21)

Paths below are relative to `src/` at commit e50d098.

### 19.1 Statement (READ)

`key_minor_dvd` (`Formalism/SharpRestriction/GrowthBounds/CoarseMultiplicity/KeyMinorDvd.lean:132`) is proved in any commutative ring A. Assume:

- **(h1)** w² = p;
- **(h2)** u_b and u′_b are multiples of w for every index b ≠ 0;
- **(h3)** entrywise, M_{ba}^(p^e) = N′_{ba} + p·T for some T. This is a Frobenius congruence.

Then for every column c,

  **w ∣ (u′N′)_c·(uM)₀^(p^e) − (u′N′)₀·(uM)_c^(p^e).**

That is, a 2×2 minor of the lifted data is divisible by w = √p.

The companion `key_pow_dvd` (`:10`) adds an inverse matrix N with N′N = I and the hypothesis w ∣ v₀. It concludes w ∣ Σ_a (uM)_a^(p^e)·(vN)_a, a Frobenius-twisted pairing.

**The proof (about 20 lines)** works modulo w:
1. By (h2), uM ≡ u₀·(row 0 of M). So modulo w the data has rank one: every vector lies on the same line.
2. Since p = w² ≡ 0, (h3) gives (row 0 of M)^(p^e) ≡ row 0 of N′.
3. So both terms of the minor become u′₀·u₀^(p^e)·N′₀₀·N′₀c, and they cancel.

### 19.2 Where the hypotheses come from (READ)

- **(h3), Frobenius congruence.** This is `frobCong` (`Formalism/SharpRestriction/GrowthBounds/FrobeniusPaths/LatticeCountingFormula.lean:29`, for `FrobCong` at `LiftedColumnOrder.lean:16`). It holds in WF p f := `WittVector p (GaloisField p f)`, the unramified extension of ℤ_p of degree f (`ObjPol.lean:309`).
  - The key step is `cc_frob_pow`: the constant coefficient of σⁿ(x) equals (constant coefficient of x)^(pⁿ).
  - This is Fermat's little theorem lifted to Witt vectors: σ(x) ≡ x^p (mod p).
- **(h1).** `UniformizedDVR.SqP : S.w² = p` (`ObjPol.lean:21`): a discrete valuation ring in which p is the square of the uniformizer.
- **(h2).** Weights `dW` (the `hhLetters` pattern) put a factor w on the non-leading coordinates. They also put a factor w on the leading coordinate of the covector at the odd top.
- **Where the keys are used** (`kS_ord`, `kW_ord`, same file): for each segment j of a Frobenius orbit `X.TT` and each "odd" top at distance d from the segment start (`topOdd`, `BinomialRatio/FinalTheorems.lean:10`; `topStart`, `RestRawTail1Of.lean:10`), the key polynomials are
  - kS = Σ_a X(start,a)^(p^d)·X(odd,a), the vector–covector pairing;
  - kW = 2×2 minors (`RestRawTail1Of.lean:14–21`).

  Substituting the lifted data for any g ∈ GL gives order ≥ 1 in w. `key3Ord` and `key3At` package this as `CoarseMultiplicityOrderBound` and `CoarseMultiplicityBoundAtIdentity` (`KeyOne.lean:114`, `RestRawTail1Of.lean:29`). At g = 1 the substitution is w·(X^(p^d)·X + w^(p^d − 1)·…), exactly one factor of w.
- **The local ring really is Witt vectors.** `WittIdent` (`Formalism/SharpRestriction/GrowthBounds/ObjBridge.lean:14`) says that in a `HidaSetting` there is W ≅ WF p n′ compatible with Frobenius. This is classical: the completion of an unramified extension of ℚ_p is W(𝔽_q).
- **Consumers:** `stmtEExt_of_15c` (`Formalism/SharpRestriction/GrowthBounds/CoarseMultiplicity.lean:31`) and `TensorOfPairLift.lean:600` (`Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/`).

### 19.3 Concrete check (COMPUTED)

The script `rh-extraction/key_minor_check.py` works in A = ℤ[w]/(w² − p). An element a + b·w is divisible by w exactly when p ∣ a. It draws random u, u′, M, and builds N′ = M^(p^e) − p·T entrywise.

| p | e | lemma holds | fails when one u_b is not a multiple of w | fails when the Frobenius congruence is broken |
|---|---|---|---|---|
| 2 | 1 | 300/300 | 75/300 | 47/300 |
| 3 | 1 | 300/300 | 133/300 | 107/300 |
| 5 | 1 | 300/300 | 164/300 | 131/300 |
| 3 | 2 | 300/300 | 140/300 | 118/300 |

So the lemma holds, and both hypotheses are load-bearing.

### 19.4 Consequence (DERIVED)

- **The local engine of divisibility is elementary.** It is Fermat/Frobenius (x^p ≡ σ(x) mod p, the point where adding and multiplying meet at a prime) plus "mod √p the data has rank one". It gives one factor √p per (segment, odd top) on each Frobenius orbit of an inert prime.
- **Link to earlier addenda (not traced at term level).** Counting these factors along the orbit, with the p^d weights, is the bookkeeping that produces the exponent a/p + a/p³ + ⋯, i.e. a·`gam p` (Add. 10–11, 18).
- **Therefore the RH-strength content is not in the local divisibility.** It is in three places:
  - **(i)** the identification of the actual iterated theta-lift data with Frobenius-lifted data at every inert prime simultaneously: `WittIdent` in a `HidaSetting`, `paired_lifts_of_identity`, `admitted` D;
  - **(ii)** the exact archimedean size: Chowla–Selberg (Add. 17), plus Rallis inner product, Siegel mass and Weyl;
  - **(iii)** the Iwasawa price of divisibility (guide §6: `VWinAt`, `window1`).
- **Next target:** (i), i.e. why the chain of theta lifts carries this Frobenius structure. Start from `paired_lifts_of_identity` and `admitted` (the `Adm1`/`adm*` list in `AdmissibleBoundsFromSource.lean`).

---

## Addendum 20 — Bost's slope inequality is "divisible means big", plus the full squeeze in repo terms; visual candidates noted (Claude, 2026-11-21)

Paths below are relative to `src/` at commit e50d098.

### 20.1 Statement and proof (READ)

`SlopeInequality` (`Formalism/LatticeSlopes/Statement.lean:75`), proved as `slopeInequality_of` (`Formalism/LatticeSlopes/LatticeSlopesProofs/SlopeInequality.lean:111`).

**Statement.** Take Euclidean lattices L ⊂ E and M ⊂ F, with L ≠ 0. Let φ : L → M be injective with ‖φx‖ ≤ C·‖x‖. Then

  **slope L ≤ μmax M + log C.**

The definitions (`Statement.lean:15–30`) are covol = √det(Gram), deg = −log covol, slope = deg/rk, and μmax = sup of the slopes of nonzero sublattices.

**Proof.** About 80 lines, plus `gram_det_le` and `slopeLeMuMax_of`.
1. Let N = φ(L) ⊂ M, of rank r.
2. A Gram-determinant comparison gives covol N ≤ C^r·covol L, so slope L ≤ slope N + log C.
3. Since slope N ≤ μmax M, the result follows.

It is elementary geometry of numbers. It is also used inside the lattice-slope library: `OrthSum.lean:93`, `ExistsSaturatedSlopeEqMuMax`, `SaturationProperties`.

### 20.2 The one-dimensional case is the product formula (DERIVED, plus a COMPILED receipt)

Take L = ℤv, M = ℤw and φ(v) = c·w with c ∈ ℤ∖{0}.
- slope L = −log‖v‖ and μmax M = −log‖w‖.
- ‖φ‖ = |c|·‖w‖/‖v‖.
- So the inequality reads 0 ≤ log|c|, i.e. **a nonzero integer has size ≥ 1**.

If N ∣ c, then φ/N is still a lattice map. That gives N ≤ |c|, i.e. Σ_p k_p·log p ≤ log|c|: **divisibility at the primes is paid for by size at infinity.**

**Receipt:** `rh-extraction/DivisibleMeansBig.lean` uses core Lean 4.33.1 only, with no Mathlib, and compiles.
- `divisible_means_big` (0 < c, N ∣ c ⇒ N ≤ c) and `prime_powers_le` both depend on the axiom propext only.
- It also checks, by `decide`, that 3^48 ∣ 100! and 3^49 ∤ 100!. That is Legendre: 33 + 11 + 3 + 1 = 48. It then concludes 3^48 ≤ 100!.

### 20.3 The full squeeze, in repo terms (DERIVED)

In general, divisibility of φ by Π p^(k_p) lowers log‖φ‖ by Σ k_p·log p. So

  **Σ_p k_p·log p ≤ log‖φ‖_∞ + μmax(M) − slope(L).**

Each piece of this has been read:
- **Left side, the divisibility.** The per-place gain Ga, via the places ledger (Add. 14.2). Its local source is `key_minor_dvd` (Add. 19). Summed, it reproduces the ramp-weighted prime sum ASK (guide §4(a); Add. 9).
- **log‖φ‖_∞, the archimedean size.** Computed exactly: Chowla–Selberg (Add. 17), plus Rallis, Siegel mass and Weyl (not read). This gives MAIN, with γ.
- **μmax(M) − slope(L).** Kept small by near-semistability, the flat lattice theorem (Add. 13, LinkS Add. 14.1), and the slope-size rules (Add. 16).

So every inequality in the squeeze is elementary or classical. The RH-strength claim is that the m-fold chain achieves divisibility with **multiplicity ~m** (each lift contributes its own a/p + a/p³ + ⋯) while the losses stay per-top. This is the "mimicking multiplicity" of the announcement: the Stepanov step.

**Next target.** The multiplicity assembly, and what it costs:
- `stmtEExt_of_15c`, `paired_lifts_of_identity` and `ExtendedClosedForm` (`Formalism/SharpRestriction/GrowthBounds/CoarseMultiplicity.lean`);
- `TensorOfPairLift.lean:600`;
- the Iwasawa window `VWinAt` (`Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean:44`) and `window1`.

### 20.4 Visual candidates (noted, not built; ranked by tightness to the Lean)

1. **Flatten the parallelogram.** `key_minor_dvd` (KeyMinorDvd.lean:132): mod √p the data falls onto one line, so the 2×2 area is 0 mod √p.
2. **Seats and bills** (a remake of loop-receipts). `kink` (PartnerCountOfCentral.lean:136) and `gam p = p/(p²−1)` (IsResidueClassZero.lean:89).
3. **Odd-layer prime count.** `vonMangoldtClassSum` (Formalism/LocalRingCardinality/DataParams₂.lean:240): Σ over odd i of (a/pⁱ − w)₊. The all-layers "3 divides 100! 48 times" version is a warm-up only, now with a compiled receipt (20.2).
4. **Fermat clock.** `gf_pow` / `frobCong` (Formalism/SharpRestriction/GrowthBounds/FrobeniusPaths/LatticeCountingFormula.lean, just above :29): x^(p^(f·t)) = x in GaloisField p f. Pascal's triangle mod p is one step looser.
5. **Divisible means big (balance scale).** Upgraded to tight by 20.1–20.2: `slopeInequality_of`, whose one-dimensional case is `divisible_means_big`.
6. **Random arrows getting perpendicular.** Dropped as misleading: the repo's near-orthogonality comes from symmetry plus scale (Add. 14.1), not randomness.

---

## Addendum 21 — the multiplicity assembly: base-p digit bookkeeping with a running budget whose slack is divided by m+1 (Claude, 2026-11-21)

Paths below are relative to `src/Formalism/SharpRestriction/GrowthBounds/` unless they say otherwise. Commit e50d098.

### 21.1 Where it sits (READ)

The chain runs:

`stmtEExt_of_15c` (`CoarseMultiplicity.lean:30`) → `ExtendedClosedForm D` (`ColumnSystems.lean:511`, `admitted D → Closed (ExtendedAllConclusions D)`) ← `paired_lifts_of_identity` (WittIdent, RestRawTail1, RestForm) ← `restRawTail1_of` (`CoarseMultiplicity/RestRawTail1Of.lean:63`).

The last of these takes three inputs:
- `CoarseMultiplicityBoundAtIdentity`, the √p keys (Add. 19);
- `LocalBoundAtIdentity` (`RestRawTail1Of.lean:47`), products over segments of X^(p^G − 1);
- `RestAsmRT`. This is supplied by `asmRTCondition_of_adm` (`StandardPolynomials.lean:21`) = `rest_assumptions_of_three_interfaces` together with `restCols` (`StandardPolynomials/ColTop.lean:90`), `restPre` (`ColumnPolynomialCovectorZero.lean:138`) and `restTCore` (`RestTCore.lean:7`).

**Scale.** `StandardPolynomials/` is 60 files and 9,293 lines. `CoarseMultiplicity/` is 56 files and 8,417 lines. **About 17,700 lines: this is the Stepanov "auxiliary polynomial" part of the proof.**

### 21.2 What is proved: an auxiliary polynomial with prescribed vanishing order (READ, statement level)

**The local data.** `Loc` (`ColumnSystems.lean:15`) holds:
- a prime p;
- a Frobenius orbit of length n′;
- marked tops TT, with heights aT and bT;
- a size m, with k = m+1 and matrices in GL_{m+1}.

`locOf` (`ColumnSpanDensity/LocalHypothesisOfGlobal.lean:108`) copies m from the global data. The window conditions there shrink with m+1:
- a ≤ … ≤ a + a/((m+1)·Y);
- (m+1)·Y²·log a ≤ a/b′.

**`CoarseMultiplicityAtIdentity`** (`CoarseMultiplicity/CoarseMultiplicityAtIdentity.lean:78`). For each choice of blocks β_j, one per segment j of the orbit, that are **`Kept`**, and for symbols s_j in the block data, there is a polynomial F, in the right degree space `Pol … hhDegs`, such that:
- **w^(Σ_j blockOrd(β_j))·F is integral** (`InA`), with w = √p;
- F at the identity matches the symmetric family `symFam` modulo w^c;
- the order bound holds for every g ∈ GL.

In other words, F vanishes to order Σ_j blockOrd(β_j) at all the lifted points. **This is the Stepanov step: an auxiliary function with high multiplicity.**

### 21.3 The bookkeeping that sets the multiplicity (READ; `ObjSeg.lean:111–170, 282`)

The segment data are `SegData`: σ, G, distances d_i, bTop, bPlus, a, Y, La, E0. From them, P_i = p^(G − d_i).

A block (`SegBlock`) consists of base-p digits rz, ry, orders o, w, sg, and oPlus.
- **`blockOrd`** = Σ_i (P_i·oEff_i + Σ_{c≠0} rz_{i,c} + ry_{i,0}) + oPlus. This is order counted like place value in base p.
- **`DigitsOK`:** every digit is < P_i, and P_i divides (bTop_i − Σ_c rz_{i,c}) and (aTop_i − Σ_c ry_{i,c}). These are genuine base-p digits.
- **`coarseA` / `coarseC`:** the quotients (bTop_i − Σ rz)/P_i and (aTop_i − Σ ry)/P_i.

**The running budget:** cap(l) = A0 + Σ_{i<l} (coarseA_i − oEff_i), where A0 = ⌊(a − E0)/p^G⌋. Each top earns its coarse quota and spends its claimed order.

**`Kept`** (`:161`) requires:
- o_i ≤ coarseA_i and **o_i ≤ cap_i + La·coarseA_i/(m+1)**;
- for the first σ tops, w_i + sg_i ≤ coarseA_i·(1 + 4/p²) + La·cap_i/(m+1) and sg_i ≤ 2·La·A0/(m+1);
- oPlus ≤ cap + (La/(m+1) + 4/p²)·Σ 2a/P_i + La·bPlus/(m+1).

**Every overdraft allowance carries the factor La/(m+1).**

### 21.4 Plain picture and consequence (DERIVED)

**Picture.** Walk along each segment of a prime's Frobenius loop with a bank account. Each top deposits its quota (its base-p "coarse" digits). Each top withdraws the vanishing order it claims. An overdraft is allowed, but only up to La/(m+1) times the deposit. A longer chain (bigger m) lets you claim almost exactly what you earned. The total claimed, Σ blockOrd, is the multiplicity of the auxiliary polynomial, measured in powers of √p.

**Link to the budget audit (Add. 15).** The per-block slack La/(m+1), summed over the window, is the natural source of the "errors shared among the m lifts" term x/m. This is consistent with the guide §4, but not traced at term level.

**Where RH strength now sits.** The existence part is `StandardPolynomials` (`restCols`, `restPre`, `restTCore`): an F of bounded degree with exactly this multiplicity. That is the analogue of Stepanov's parameter count, "enough free coefficients to force vanishing", and it is the next thing to read. In particular:
- `ColsAt`, `PreAt`, `TCoreAt`, i.e. why the needed polynomial exists;
- the degree bound `hhDegs`, which feeds the archimedean (size) side.

---

## Addendum 22 — black-box map; the auxiliary polynomial is built as an explicit product (no counting argument); what the 2.85M-line DivisorProofs folder is (Claude, 2026-11-21)

Paths below are relative to `src/` at commit e50d098.

### 22.1 Black-box map (READ / COMPUTED)

Full table: `rh-extraction/blackbox-map.md`. Sources are our own line counts and `verification/NOTES.md`.

**Size.** 175,187 files and 17,374,215 lines. The source has no comments, 818,755 theorems and 242,067 definitions, and **every file is in `Main`'s import closure**. Import closure therefore cannot tell us what is used.

**Coverage.** The handoff cites 251 files, about 0.14%. By library:

| library | share of lines | files cited |
|---|---:|---:|
| Development | 70.4% | 49 |
| Formalism | 18.4% | 194 |
| GroundTheory | 6.4% | 3 |
| ReciprocityTheory | 3.2% | 4 |
| CompanionTheory | 1.1% | 0 |

**Largest boxes.**
- `Development/AbelianVarietyTheory/Proofs`: 7.4M lines. Its subfolder DivisorProofs alone is 2.85M lines in **42,424 files in one flat folder**.
- `Development/AutomorphicSpectrum/Proofs`: 1.16M lines.
- `Development/AutomorphicArithmetic/AutomorphicVarieties`: 849k lines, including ModularityArgument at 292k.
- `GroundTheory/HeightsAndTheta/Heights`: 627k lines.
- `Formalism/HermitianCurvature`: 437k lines.
- `Formalism/PeriodIntegrals/UnitaryGroupMassFormula`: 430k lines.

**Limits.** Neither we nor Codex can build the project: it takes 7–10 h on 48 cores and 503 GB of RAM, and the export is 61 GB. A term-level usage map from `riemannHypothesis`, made by textual name resolution, is assigned to Codex (`rh-extraction/codex-prompt-blackbox.md`, Task 1). Codex also has Task 2, Iwasawa/`VWinAt`, and Task 3, Rallis/Siegel mass/Weyl. Its output goes to `rh-extraction/codex-blackbox-report.md`.

### 22.2 The auxiliary polynomial is an explicit product, so the multiplicities simply add (READ)

All paths below are under `Formalism/SharpRestriction/GrowthBounds/StandardPolynomials/`.

**`ColSys`** (`ColsDef.lean:9`) and **`ColsAt`** (`:46`). For every level datum and every word y, the polynomial ψ(y) **factors** as ∏_a Kc_a (`Kprod`). Each factor Kc_a is integral (`KInt`) and has degree ≤ 1 in each chain letter (`digit_le_one`). After twisting by a monomial `pl a`, each factor is `IsFac` with its own order `oC a`.

The bookkeeping identities are:
- `oSum`: Σ_a oC_a = Σ_i P_i·deg(letter 2i) + deg(last letter);
- `plSum`: Σ_a pl_a = Qj·a0 at the start top + Σ_i P_i·(coarseA_i − claimed_i) at the odd tops.

The proof is `restCols` (`ColTop.lean:90`), which is `colsAt_of` together with `column_numerics_holds` (`ColXNum.lean:294`).

**`LvDat.word` / `LvDat.stdPoly`** (`TCoreDef.lean:56`, `:41`). The "standard polynomial" of a segment is a product of powers of fixed building blocks: ∏ Ehatᵢ^(lvᵢ) · Eplus^(jp) · ∏ X(scalZ)^(zᵢ) · X^(zPlus) · G · ∏ ξ_c^(γ_c). `ioBlock_word` (`:67`) gives ioBlock(word) = head · stdPoly.

**`TCoreAt`** (`:84`): stability when the levels are lowered (ju ≤ lv) for 1 ≤ e < n.

**`NumCoreAt`** (`TCNumDef.lean:9`), proved as `restNumCore` (`TCXNum.lean:285`). These are pure inequalities giving room:
- 1 + 2·p^(G′)·e + o_i ≤ coarseA_i;
- for nearby digit choices b′, whose coarse quotients lie within m+1 of each other, the orders move by at most 2·((m+1) + p^(G′)·e).

**Reading (DERIVED).** There is **no pigeonhole or Siegel-lemma step** here. The polynomial is written down as a product of explicit pieces. Each piece's divisibility by √p comes from the key lemmas (Add. 19), and **orders of a product add**, just as v_p(ab) = v_p(a) + v_p(b). The slack again scales with m+1. So the multiplicity is constructive bookkeeping. What carries the depth is that these pieces really are the theta-lift data, which is the next item.

### 22.3 What DivisorProofs is (READ by sampling; DERIVED reading)

The 42,424 file names, counted by keyword:

| keyword | files |
|---|---:|
| Bound | 1,843 |
| Theta | 1,782 |
| Lattice | 1,667 |
| Abelian | 993 |
| CM | 736 |
| Period | 599 |
| Kernel | 575 |
| Weil | 528 |
| Torus | 526 |
| Tate | 485 |
| Height | 477 |
| Galois | 377 |
| Siegel | 357 |
| Hecke | 356 |
| Hodge | 341 |
| Inert | 311 |
| DeRham | 235 |
| Witt | 153 |
| Crystal | 124 |
| Dieudonné | 55 |

**Caution.** "Theta" is overloaded. For example, `ainfGhostThetaFrobIter_values_xi_mu_padic` is about Fontaine's θ on A_inf (p-adic Hodge theory), not about theta functions.

**Genuine theta-jet theory is here.** `GlobalTheory.T.exists_keyDatumBaseChange_thetaJets` (`Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsKeyDatumBaseChangeThetaJetsStatement.lean`) shows that jets (Taylor coefficients) `ThJet` of a theta section of the polarization bundle on an abelian variety are compatible with base change K → C. `FockJetsUnitVacuumEqScaledThetaJets` identifies Fock-model jets (from the Weil representation) with scaled theta jets.

**Reading.** DivisorProofs is the global-to-local bridge. It holds the algebraic theory of theta jets on polarized and CM abelian varieties: their algebraicity and integrality, plus the reduction at inert primes via crystalline, Dieudonné and Witt theory, which supplies the Frobenius structure used by `key_minor_dvd`. That is target (i) of Add. 19. It is classical-to-research-level arithmetic geometry, and **not traced**.

**Next for Claude:** follow `ThJet` from the theta lifts used on the main path into DivisorProofs. Codex Task 1's usage graph should show which part of the 42k files is actually reached.

## Addendum 22b — (Codex) the threshold-avoiding window (`window1`) and its arithmetic input

> **Merge note (Claude, 2026-11-22).** Its author numbered this "Addendum 7"; it has been renumbered. Codex's later report corrects one claim below: `HasMu` is **not** μ = 0 (see Addendum 23.2), and Ferrero–Washington is a separate theorem that is proved in the repo.

Source files are under `src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/` at the pin. They were **read in source**, fetched from the blobless clone in `rh-source/` with `git show`. This directory is not in the sparse checkout. `window1` was **compiled** as described below. Everything else is read only.

**Which window this is.** This is a different window argument from the Landau one in sections 3 and 8. It selects a multiplicative window `[Y, Y²]` that avoids a finite set of bad integers. I have not confirmed it is on the headline path.

### `window1` (Window1.lean)
For `R : ℕ`, `B ≥ 1`, `U > 0` and a finite `T ⊂ ℝ` with `|T| ≤ R`, there is `y` with

    U / (2^(R+2) · B^R) ≤ y,   2y ≤ U,
    ∀ a ∈ T, ∀ u ∈ [y, 2y],  a ≤ u → B·a ≤ u.

So no threshold `a` lies in the "forbidden gap" `[u/B, u)` for any `u` in the window. The proof is induction on `R`. If some `a₀ ∈ T` lies in `(U/(2B), U]`, remove it and recurse with `U' = U/(2B)`. Each step costs a factor `2B`, so the final lower bound is `U/(2B)^R` and the extra `1/4` comes from the base case `y = U/2'`. If no threshold lies there, take `y = U/2`.

### `window` (Window.lean)
Put `X > 1`, `0 < η ≤ Ct`, and a finite `Exc ⊂ ℕ` with `|Exc| ≤ R`. Apply `window1` with `B = Ct/η`, `U = log X` and `T = {log e / Ct : e ∈ Exc}`. Exponentiating gives `Y` with `Y ≥ X^(1/(2^(R+2)(Ct/η)^R))`-type growth (the file's `InRange` records the exact form) and, for every `x ∈ [Y, Y²]`,

    Good η Ct Exc x := ∀ e ∈ Exc, e ≤ x^Ct → e ≤ x^η
    (SecondBound.lean:46).

In words: every exceptional `e` is either bigger than `x^Ct` or already at most `x^η`. Nothing falls in between.

### Where the exceptional set comes from (Exc.lean, SecondBound.lean)
- `ABound l R L₀` (SecondBound.lean:19) says: there are at most `R'≤R` points `s_i` of an ultrametric `ℚ_l`-algebra `K` such that, whenever every `s_i` stays `l^(-B)`-far from `e`, the Sha invariant satisfies `shaInv L₁ l e ≤ R'·(max m j₀ + c + B)`, together with `SecondBound`.
- `exc` (Exc.lean:7): from `ABound l R L₀` and any cutoff `Z`, build `Exc = ⋃_i {e ≤ Z : ‖s_i − e‖ < l^(−⌊log_l Z⌋)}`. `near1` shows each ball holds at most one integer, so `|Exc| ≤ R' ≤ R`. Off `Exc` one gets `FirstBound`: `shaInv L₁ l e ≤ R·(max m j₀ + c + log_l Z)`.
- The bound that feeds this is `FixedIn` (SecondBound.lean:32): for odd `l`, every abelian family `A` with `A.HasMu l`, and every abelian field `L₀`, some `R` gives `ABound l R L₀`. `HasMu` is the μ = 0 hypothesis. I **did not find** where `HasMu` is defined or where the Ferrero–Washington theorem is discharged. It is not among the files in the local sparse checkout, and a filename search for it was too noisy to trust. Locating it is open.
- The `l = 2` case is the separate `TwoIn`/`TwoBase` package.

### Consumer arithmetic (Final.lean)
`final`: for all `Ct, eps, C` with `eps > 0` there is `x₀ ≥ 2` such that for `x ≥ x₀`,

    x^Ct · ptBound C eps x ≤ exp(x^(4·eps/5)),
    ptBound C eps x = C(1+log x) + 2·exp(C·x^(3·eps/4)).

The proof compares `3/4 < 4/5` exponents and absorbs `log x` and constants into the gap `x^(4eps/5 − 3eps/4)`.

### Compiled
`rh-extraction/WindowAvoid.lean` is `window1` copied verbatim (namespace changed, import is `Mathlib` only). Command: `lean WindowAvoid.lean` from `rh-extraction/`, Lean 4.33.1, Mathlib `0df444a3…`, with `LEAN_PATH` as in Addendum 6. Result: compiles, with only `push_neg` deprecation warnings. `#print axioms window1` gives `[propext, Classical.choice, Quot.sound]`.

### Not done
- Locate the definition of `HasMu` and the Ferrero–Washington proof or hypothesis.
- Find the call that passes `Exc` and `FirstBound` into `window`. Codex's note says it found this call, but I did not re-derive it.
- The six inputs of the named volume-side theorem were not identified: several theorems with `volume` in their name exist (`GL5/…`, `GenusMassVolumeResults.lean:14`), and I do not know which one Codex meant.


---

## Addendum 23 — Codex black-box report merged: usage map, the Iwasawa price, the archimedean inputs, and the real source of the degree clause (Claude, 2026-11-22)

**Source.** `rh-extraction/codex-blackbox-report.md` (151 KB, 2026-11-22) and its data files (`usage-graph.json`, `usage-*.csv`, `interface-witnesses.json`, `blackbox-*paths.json`). Tags below say who did the work:
- **[Codex]**: from the report;
- **[verified]**: Claude re-read the cited lines at e50d098;
- **[not re-checked]**: taken from the report as is.

### 23.1 Usage map from `riemannHypothesis` [Codex; COMPILED by analysis scripts, lexical only]

| search from `Main.lean:4` | declarations | files | lines | share of all lines |
|---|---:|---:|---:|---:|
| indexed source | 1,061,434 | 175,188 | 13,272,823 | 76.4% |
| following all candidates | 851,914 | 157,737 | 11,020,207 | 63.4% |
| following single-target references only | 755,832 | 146,587 | 10,058,743 | 57.9% |

- 54% of reference records are ambiguous because names repeat. Those records make up 97.6% of the candidate arrows.
- This is a lexical graph, not the kernel's dependency graph. It is neither an upper nor a lower bound.
- **Reading (DERIVED):** even counting only unambiguous references, about 10 million lines are reached. The proof is not a small core wrapped in unused library code: most of the archive is plausibly on the path.
- The root was re-confirmed. There is a second theorem called `riemannHypothesis` at `CharacterBoxes/MainConclusion.lean:13`, so do not start from it.

### 23.2 The Iwasawa "price of divisibility" (guide §6)

**`VVle E t B`** (`Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean:12–17`) [verified]:
- every Ш-length (Tate–Shafarevich) for 0 < e < t is finite;
- **for every finite set S of primes**, Σ_{ℓ∈S} log ℓ · Σ_{1≤e<t} len Ш(ℓ, e) ≤ B.

**`VWin`** (`:19–49`) [not re-checked]: for every character ψ and every 0 < ε < 1/52 there is a window [Y, Y²] on which the bound holds with **t = ⌊x^401⌋ and B = √exp(x^ε)**. That is B = √b in the scale of Addendum 14.

**Window selection:** `window1` and `window` (Addendum 22b; `WindowAvoid.lean` compiled by Codex, axioms standard).

**Ferrero–Washington is proved, not assumed** [verified]:
- the proposition is at `Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/FerreroWashington.lean:7`. For each prime ℓ and each abelian K with the required root of unity, there is an r such that every ℓⁿ-cyclotomic layer K′ has #(Cl(K′)/ℓ) ≤ ℓ^r;
- the theorem is `UpperTheory.V.FW.ferreroWashington` at `…/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:104`;
- it is used at `…/DenseThresholdCases/HVCore.lean:19`: `of_four_alt` → `Win.thmBab_of_lemmaK … FW.ferreroWashington …`.

**`HasMu`** (`Development/AutomorphicArithmetic/AutomorphicVarieties/StmtFields.lean:22`) [verified] is `l ∣ A.m ∧ ∀ a, A.ker a → a ≡ 1 [MOD l]`. This is a condition on the kernel modulo ℓ, **not** μ = 0, and it corrects 22b.

**Where the price is paid** [Codex; not re-checked]:
- `divinN_at` (`CharacterBoxes/DivinNOfHypV.lean:76–130`) gives etaSum ≤ D0·(|C|+1)·x^ε·(B0+Nc), using √b ≤ b ≤ B0;
- this flows `DIVinN` → `LinkDIVt` (`LinkEta → DIVinN → LinkDIV`, `GlobalTheoremInputs.lean:91–95`) → `topDesWin` (`DesWin.lean:23–31`).

**So the Iwasawa leakage lands inside the m·(B0+Nc)·x^ε term of `LinkDIV`, which is the "m-cost" of the √x budget (Addendum 15).**

### 23.3 The archimedean inputs (guide §4(c)) [Codex; not re-checked]

- **Rallis inner product:** proved from the doubling method plus convergent Siegel–Weil (`rallis_of_dm`), and passed in the published-results bundle at the headline join. Whether it is indispensable to the degree clause is not established.
- **Siegel mass ratio** (`Formalism.HermitianLatticesTheory.SiegelMassRatio`): used in the lower trace bound b^(m/2) ≤ Tr(D,u) (`eventually_le_trace`). It is also used in the family link via `link_gl` → `famGLmin_of_realPlaceSecondLayer` → `siegel_mass_ratio_family`.
- **Weyl dimension:** the log-dimension bound in a covering estimate, via `parameters_scale_rank_gap_bounds` ← `dualWeyl_dim_formula_duality_bound`.
- **Good-tower volume theorem:** it has six inputs (`Top.Given`, integrality, avoidance, `Out.WeilSt`, a positive family, a comparison pair). None of the three formulas above is fed to it directly.
- **Caution:** `WeilSt` here is not Weyl's formula.

### 23.4 The real source of the degree clause (DIV) [Codex; key line verified]

- `linkDIV_at_words` does **not** prove the degree inequality. It takes it from `WordFacts` (`(hW u).2.2`, `Formalism/LocalToGlobal/Divisibility/RecBridge.lean:332`) [verified].
- It comes from the division package: `P.wordFacts` is built from **`wordFacts_of_face`** (`RecBridge.lean:204`) and **`linkDIV_L2R_face`** (`LinkDIVL2R3Col.lean:19`) [both verified to exist].
- `linkDIVt_of_rowsF` (`RecBridge.lean:633–695`) passes `DIVinN` to both `B.pkg` and `B.hh`.

### 23.5 Updated clean map (DERIVED)

- **"Iwasawa leakage" box: opened at statement level.** Ferrero–Washington (proved) gives small Ш-lengths on a special window, and these are absorbed into B0, the m-cost.
- **"Mass formulas" box: opened at call level.** These formulas feed trace and size bounds and a covering estimate, not the tower theorem directly.
- **Next target (Claude):** `wordFacts_of_face` plus `linkDIV_L2R_face`. This is where "lattice degree ≤ MAIN + per-top error" is actually proved, and where Chowla–Selberg/γ (Addendum 17) should be consumed at the term level.

---

## Addendum 24 — the authors' own split: 194 literature theorems plus three new pieces (Claude, 2026-11-22)

All of this was READ at e50d098, in `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean` (814 lines).

**What the file contains.**
- `structure UpperTheory.LiteratureTheorems.OpenLiteratureStatements : Prop` (`:215`) has exactly three fields: `caraianiLocalGlobalDual` (a `Row`), `localLanglandsExists` (`RecTExists`) and `galoisRepOfPolarizedPairLit` (a `Row`).
- The file then has **194 theorems `UpperTheory.LiteratureTheorems.*`** of the form `…_of_literature (O) : <Published proposition> := <proof in the repo>`.

The 194 cover, among others:
- **L-functions and class field theory:** Deligne–Ribet; Siegel–Klingen; Hecke–Tate functional equation; partial zeta functional equation; Hecke L-function entire and nonzero at 1; global Artin reciprocity; ray class fields; Hilbert class field and j; elliptic main theorem of CM; Linnik; Chebotarev.
- **Representation theory and Langlands:** local Langlands for GL_n; Jacquet–Shalika; Bernstein–Zelevinsky; Howe duality; Stone–von Neumann; the Weil representation; Siegel–Weil (several forms); Rallis inner product; doubling method; discrete-series classification.
- **p-adic Hodge theory and arithmetic geometry:** Fontaine B_cris; Bhatt–Scholze; Grothendieck–Messing; Kawamata–Viehweg; Nadel vanishing; arithmetic Hilbert–Samuel; Chow forms; toroidal compactification.
- **Galois cohomology:** Poitou–Tate; Greenberg–Wiles; local and global Euler characteristic; Tate duality.

**The top join** (`:810`):

```
every_character_of_literature_of_vWin (O) (hV : VWin) : EveryCharacter :=
  every_character_of_theta_integrals_local_matching
    (published_results_eigen O) (published_results_first O) (theta_integrals_… O).1 (….2)
    (topCovolSlim2_use_alt_alt <about 15 literature results>)
    (local_langlands_gl_recT_exists_of_literature O) hV
```

**Reading (DERIVED).** Most of the 10–11M reached lines (Addendum 23.1) formalize *published* mathematics that the argument uses as tools. **The new argument is the three non-literature pieces:**

- **(i)** `every_character_of_theta_integrals_local_matching`. This is the main line traced in Addenda 1–22: window and pole, averaging, the √x budget, and the squeeze.
- **(ii)** `topCovolSlim2_use_alt_alt`. This is an arithmetic-volume (covolume) bound assembled from about 15 literature results: Moriwaki bigness, Hilbert–Samuel, Zarhin, Fargues, toroidal compactification, and others.
- **(iii)** `VWin`. This is the leakage window, assembled from Ferrero–Washington plus the counts I, II, III and V and LemmaK (Addendum 23.2).

**Next.**
- Codex task `rh-extraction/codex-prompt-core.md`: run the usage search again, but **stop at the literature theorems**, to measure the size of the new argument and list its hubs.
- Claude: branch (i) at the term level, starting with `wordFacts_of_face` (`RecBridge.lean:204`) and `linkDIV_L2R_face` (`LinkDIVL2R3Col.lean:19`).

---

## Addendum 25 — Codex's "cut at the literature" run: the cut removes only ~14%, so size cannot locate the new idea (Claude, 2026-11-22)

**Source.** Codex ran out of credits before writing `codex-core-report.md`. It did leave data: `core-counts.json`, `core-rules.json`, `core-hubs.csv`, `core-directories.csv`, `core-stopset.csv` and others in `rh-extraction/`. What follows is Claude's reading of that data [Codex data; COMPILED by Codex's scripts; lexical], plus one source check [verified].

### 25.1 The stop set

2,785 declarations:
- 194 literature wrappers;
- 193 published propositions;
- 372 right-hand-side proofs;
- 1,671 declarations in `*.Published.*` namespaces;
- 1,160 proofs of published results.

### 25.2 What is reachable after cutting

| search, single-target edges | declarations | files | lines |
|---|---:|---:|---:|
| headline, no cut (Add. 23.1) | 755,832 | 146,587 | 10,058,743 |
| **headline, cut at literature** | 660,273 | 121,229 | **8,672,900** |
| branch (i), main argument | 568,601 | 100,037 | 7,222,849 |
| branch (ii), covolume | 314,452 | 61,428 | 4,019,276 |
| branch (iii), window | 255,029 | 48,487 | 3,197,398 |

- Shared by all three branches: 2.62M lines. Their union: 8.62M lines.
- The largest strongly connected block (code that refers back to itself) is 152,457 declarations and 2.2M lines. This is a sign that name-matching ties code together in loops.

### 25.3 Reading (DERIVED)

- **Cutting at the 194 literature results removes only about 14% of the reached code.** The new argument's own statements use the same enormous library of objects directly: abelian varieties, theta lifts, automorphic forms, Galois cohomology. So the "rest" is mostly shared infrastructure, not new reasoning.
- **Line counts cannot isolate the new idea.** The only reliable way is the one we have been using: follow *statements*, interface by interface. The handoff's clean map (squeeze, budget, window, averaging) is that statement-level core.
- The `core-hubs.csv` ranking is by size, not importance. Its top chain runs: `every_character_of_theta_integrals_local_matching` → `nonempty_hyps_definite_side_of_closed_bound` → `hypotheses_nonempty_of_unramified_exponents_alt` → `allRows_of_open0_alt` → `large_unramified_exponent_bundles_exist_alt` → `open0_of_unitary_group_hypotheses` → …. It also includes `member_exists_baseLattice_alt`, `main_theorem_published_inputs_third_alt_alt`, `diagonalRow_of_siegelWeil_unitary`, and the tower/covolume chain. These hubs are mostly the *construction of the objects* (rows, base lattices, open orbits), not the decisive inequality.

### 25.4 Soundness of the authors' split [verified]

`Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:7–11` builds the literature bundle as `⟨h, recTExists, h⟩`, where:
- `h := UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` (the Galois "row", guide §7);
- `UpperTheory.Zero.LLC.recTExists` is local Langlands existence.

Both are proved theorems, so the three fields are discharged and not assumed. The same `h` also feeds the window (`vwin_of_row h`).

**Picture:** the whole proof hangs from one proved Galois-representation theorem plus local Langlands.

### 25.5 Next

The "pick out the pieces" deliverable should be a **statement-level core skeleton**: "RH follows from Lemmas 1–N", where each lemma is stated in plain math with its Lean anchor and its status (read / compiled / black box). It is assembled from Addenda 1–24. Claude continues branch (i) at `wordFacts_of_face` / `linkDIV_L2R_face`.

## Addendum 26 — Codex's final core report merged; `LinkN` is a place-by-place cost ledger with a special allowance at the primes 2 and 3 (Claude, 2026-11-22)

**Sources.** Codex wrote `rh-extraction/codex-core-report.md` (1,058 lines) and new data files:
- `core-reach.csv`, `core-hubs.csv`, `core-wrappers.csv`
- `core-supplied-wrappers.json`, `core-uncertain-providers.csv`
- `core-literature-frontiers.csv`, `core-frontier-context.json`, `core-hub-method.json`

Codex did **not** edit this handoff; its sha was still `b7085a74…` before this addendum. Claude re-read every Lean claim below on the pinned clone (`e50d0981…`). Paths are `src/`-relative.

### 26.1 What the final report adds to Addendum 25

- **COMPILED (Codex), headline sizes.** After stopping at the literature, the headline reaches 8,672,900 lines with single-target references and 10,006,103 with all candidates. That removes 13.78% and 9.20% respectively. The stop set has 2,785 declaration IDs.
- **COMPILED (Codex), branch sizes (single-target).** The three branches overlap heavily, so these do not add up:
  - main argument: 7,222,849 lines
  - covolume: 4,019,276 lines
  - window: 3,197,398 lines
  - shared by all three: 2,623,359 lines
- **READ (Codex), which literature each branch uses.**
  - The main argument receives 4 wrappers from the join. Opening their bundles gives 154.
  - The covolume receives 13 wrappers. Opening their bundles gives 43.
  - Three wrappers are shared, giving 194 in total.
  - The window is built at the caller of the join (`VwinOfRow.lean:4–5`) and goes to `HVCore.lean:18` (`of_four_alt`: Ferrero–Washington, then `thmBab_of_lemmaK`, then the bound at 401). This was already in Addenda 23 and 25.
- **READ (Codex), why the cut leaves so much.**
  - (a) Some classical results are proved outright and not marked as literature. Examples: `hsUse_outright` (arithmetic Hilbert–Samuel) and `moriwakiBig_outright` (Moriwaki bigness), at `Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/Outright.lean:9,13`. The join supplies them explicitly at `EveryCharacterOfLiteratureOfVWin.lean:812`.
  - (b) The lexical graph sometimes mistakes a bound variable for a declaration. This creates false cycles, for example `MemPuncturedRingIffPowerSeriesPart.lean:101` pointing to `GlobalTheory.Conv.u` at line 262.
  - So these counts are lexical, not kernel dependencies.
- **READ (Codex) / confirmed, the inputs are supplied.**
  - The literature bundle `O = ⟨h, recTExists, h⟩` (`MainConclusion.lean:7–11`): fields 1 and 3 have the same type, `UpperTheory.One.M.Row`.
  - No unproved literature premise reaches `Main.lean:4` at source level.
  - The upstream static scan (`verification/static-scan.txt`) reports no `axiom`, `sorry` or `admit`.
  - **A kernel-level axiom audit (`#print axioms` on `riemannHypothesis`) has not been done by us.**

### 26.2 Placeholder check on the 194 [COMPILED, Claude]

Codex flagged that `siegel_eisenstein_simple_pole` (`EveryCharacterOfLiteratureOfVWin.lean:505–506`) concludes `GlobalTheory.Published.UnusedSlot72`. That name is defined as exactly `True` (`…/LocalTypeDictionary/DiscreteSpectrumResidualClassification.lean:7`), and the proof is `trivial`.

I then checked whether any of the other 193 are also empty:
- 182 of the 194 result types are a single bare name.
- I searched the whole of `src/` for every `def`/`abbrev X : Prop := True` and matched against those names.
- **Only one match: UnusedSlot72.**

So **193 of the 194 literature entries carry real statements.** Whether each matches the full strength of the famous published theorem it is named after is **not established**.

### 26.3 What `LinkN` says [READ]

**Picture.** The main chain does not end in a structural fact. It ends in a **ledger line**: an extra cost has to fit inside a budget.

`Formalism/SharpRestriction/GlobalTheoremInputs.lean:31–48`:

    vvTerm(ℓ)  = log ℓ · Σ_{1≤e<t} len Ш(ℓ, e)          (0 if ℓ not prime)        :31
    etaSum(j)  = Σ_{w with μ(w) ≠ μ0}  weight(w) · ramIdx(w) · η_j(w)               :36
    LinkN_at:  etaSum(j) ≤ dZ0(j) · ( C·(f·m·b·L² + (log x)²·Nc) + Σ_ℓ vvTerm(ℓ) )  :40–43
    LinkN:     for all large x, every family member with finite odd Ш satisfies LinkN_at for every lift j   :45–47

In plain words:
- **The extra cost** is etaSum: the sum, over the places w where the local type μ is not the base type μ0, of a weight times a ramification index times η.
- **It must fit inside** a size term plus the Iwasawa/Ш leak Σ vvTerm. That leak is the same quantity bounded by `LinkV_at` (:18–20) and by VVle (Addendum 23).
- **Comparison:** the sibling bound `DIVinN_at` (:59–60, Addendum 23) gives etaSum ≤ D0·C·x^ε·(B0+Nc), with no Ш term.
- How LinkN and DIVinN divide the work is **not established**.

### 26.4 How `LinkN` is produced: cut, then bound place by place [READ]

`ThirdPlaceSeries/LinkNFam.lean:35–53` (`linkN_of_twGood_galoisPreconditions`):

1. For each family member, `CutGivesAlt` (:35) cuts the data down to a "good" piece that keeps the norm-choice facts and `Tie4`.
2. `linkN_along_family_of_localBounds` and `conclF_of_family_facts_and_bound_at_two_three` (:51) turn **local bounds** into `LinkN`.
3. `goodPointMultiplicityLeRank_proof` (:53) supplies **multiplicity ≤ rank** at good points. This is the same "rank one" theme as Addenda 19 and 21.

The local bounds are a **place-by-place ledger** (`Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/BoundAtTwoThreeFamily.lean`). Each local count `vcc` at twisted place i (and each π) is bounded by its expected value plus an allowance:

    Bd(i, π, b):  vcc(i, π) ≤ sPi(i, ρ_i, π) + b + VVr(ℓ_i) + vhE(ℓ_i) + epsL(ℓ_i)        :17–19
    midF       =  C·f·m·b·log x + C·x^C·(large₂)²                                          :33–34

| Places | Allowance b | Lean |
|---|---|---|
| large ℓ > ℓ*, outside gset and the exceptions | **0** | `StarE` :21 |
| the exceptions | at most (|TT|+2)(Sc + 3·ηSz + t + 8b/ℓ* + 9) places, each ℓ ≤ 3b | `ExcOK` :25 |
| small primes other than 2 | midF | `StarS` :55 |
| **ℓ = 2, and ℓ = 3 when 3 is not "small"** | midF | **`BoundAtTwoThree` :52** |
| the host primes q and d | midG | `StarG` :78 |

`starF_of` (:58–71) glues `BoundAtTwoThree` and `StarS` into the small-prime clause `StarF`.

**The new work for the main argument is the 2-and-3 clause.** `At23` (:73) asks for it, with finite odd Ш and the killing condition. There are two family versions:
- `BoundAtTwoThreeFamily` (:76);
- its variant `BoundAtTwoThreeFamilyFonAlt` (`ThirdPlaceSeries/BoundAtTwoThreeFamilyFon.lean:25`).

`final_of_alt` (`LinkNFam.lean:75`) takes the FonAlt variant as its hypothesis `hAt`. Inside `linkN_of_twGood_galoisPreconditions`, the 2-and-3 bound is supplied by `UpperTheory.N.at23_family_alt` (`LinkNFam.lean:51`).

**DERIVED, picture.** This is the "debt" ledger written out:
- Every place pays its expected cost.
- Large places pay **nothing** extra, apart from a counted set of exceptions.
- The primes 2 and 3 (and other small primes) get a fixed allowance midF.
- midF has the same shape as the m-term of the race equation (f·m·b·log x).
- So the bad primes are charged to the same budget line the amplifier already pays. The exact term-by-term match is **not established**.

### 26.5 Where Siegel–Weil enters the main argument [READ, with DERIVED reading]

Codex's 40 largest hubs include a Siegel–Weil branch:
- `sLp_sO_hTF_of_siegelWeil` (`AtChoice.lean:24`) and `at_choice_alt` (:16): the per-slot Lp bound, order bound and torsion-free condition.
- `diagonalRow_of_siegelWeil_unitary` (`…/DecoratedLatticeProofs/DiagonalRowOfSiegelWeilUnitaryStatement.lean:45`).
- `corankOnePairsFamilyBounds_of_siegelWeil` (`…/CorankOnePairsFamilyBoundsOfSiegelWeilStatement.lean:45`).

The proof that matters, `rowDiag_of_siegelWeilUnitary` (`…/DiagonalRowOfSiegelWeilUnitary.lean:50–55`), is short. It combines three things:
- degenerate-term and collision bounds at window width 3;
- corank-one pair family bounds, which come from **convergent Siegel–Weil for unitary groups**;
- the result: diagonal-row bounds (`IsScaleWithBoundedGamma` ∧ `RankMu`).

**DERIVED.** Siegel–Weil is the classical identity that turns a theta integral into an Eisenstein series. That is what lets a family average be computed exactly, so this branch is plausibly the "averaging over families" step of the skeleton. This match is **not established** term by term.

### 26.6 Next

1. **The 2-and-3 bound.** Read `at23_family_alt` and `GlobalTheory.T.conclF_of_family_facts_and_bound_at_two_three`. This is the new local estimate the main argument needs, and the most concrete "new piece" found so far below the join.
2. **Kernel axiom audit.** A transitive `#print axioms riemannHypothesis` against a built export is still open.

## Addendum 27 — with RH removed as the target: the general theorem the amplifier proves, how far it extends, and what is ζ-specific (Claude, 2026-11-22)

Paths are `src/`-relative at e50d098. Tags: READ = read in source; DERIVED = hand reasoning.

### 27.1 The theorem actually proved (READ)

`UpperTheory.EveryCharacter` (`Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean:13`) states:

> for every N ≥ 1, every Dirichlet character χ mod N, and every s with Re s > 1/2 (excluding s = 1 when χ is trivial), L(s,χ) ≠ 0.

- **RH** is the N = 1 instance (`Formalism/GammaFactorNonvanishing/CritLine.lean:29`).
- **`critLine`** (same file) adds the reflection: every nontrivial zero of a primitive L(s,χ) lies on Re s = 1/2.

So the headline is **GRH for all Dirichlet L-functions**.

**Corollaries (DERIVED, standard).**
- GRH for the Dedekind zeta function of every abelian number field, since it factors into Dirichlet L-functions.
- The usual GRH consequences for primes in progressions.

**Not covered.** GRH for:
- non-abelian fields;
- Kummer fields, so not Artin's primitive-root conjecture;
- modular forms and elliptic curves.

### 27.2 The quantitative output (READ statements; DERIVED translation)

**Detectors.**
- `Formalism/StatementOC.lean:13` and `…/TotientGaloisClasses/Analytic.lean:11–24`:
  - G₁(y) = Σ_{n≤y} Λ(n)(y/n − 1) − y log y + (1+γ)y;
  - G_χ(y) = Σ_{n≤y} Λ(n)χ(n)(y/n − 1) + y·L′(1,χ)/L(1,χ).
- Equivalently, G_χ(y) = −Σ_ρ y^ρ/(ρ(ρ−1)) + O_χ(log y). This uses the Mellin transform −L′/L(s,χ)/(s(s−1)), with the pole at s = 1 removed.

**Family** (`Level.Gm`, `Level.cyc`, `…/ExplicitFormulaErrorOfHostConditions.lean`). Let ψ be primitive of order o. Then

  M_ψ(y) = G₁(y) + (3o+1)⁻¹ Σ_{j=1}^{o−1} Re G_{ψ^j}(y),

where each ψ^j is replaced by its primitive inducing character.

**Theorem B.** For every ε > 0 there are arbitrarily large Y such that M_ψ(y) ≤ y^{1/2+ε} on all of [Y, Y^{3/2}].
- The windows use power 3/2 (`plugWin`, `EveryCharacter.lean:8`).
- The source exponent is 1/2 + 9ε.

**Positivity (DERIVED).** The Dirichlet coefficient of M_ψ at n is Λ(n)·c(n), with c(n) ≥ 1 − (o−1)/(3o+1) = (2o+2)/(3o+1) > 0. That positivity is what the localized Landau argument needs.

**Strength (DERIVED).** Theorem B is *equivalent* to GRH for the L(s,ψ^j), not stronger: under GRH, |G_χ(y)| ≪_N y^{1/2} for all y. Nothing beyond GRH comes out.

### 27.3 The amplifier as a stand-alone theorem

**(a) Divisible means big (READ).** This is Bost's slope inequality, `Formalism/LatticeSlopes/LatticeSlopesProofs/SlopeInequality.lean:111`, combined with divisibility. For Euclidean lattices L ≠ 0, M and an injective φ: L → M divisible by Π p^{k_p}:

  Σ_p k_p log p ≤ log‖φ‖ + μ_max(M) − μ(L).

In rank one this is the product formula.

**(b) Amplification (DERIVED abstraction; the source normalizes by |TT|·m·b).** Suppose that for every integer m in [x^{1/2−ε}, x^{1/2+ε}] there is a map φ_m with:
- (D) Σ_p k_p log p ≥ m·S;
- (C) log‖φ_m‖ + μ_max − μ ≤ m·Main + C x^ε (x + m² + m√x).

Then m(S − Main) ≤ C x^ε (x + m² + m√x). Taking m = √x gives S − Main ≤ 3C x^{1/2+ε}. All the content lies in constructing φ_m: the divisibility must grow like m, while the per-top costs must not.

**(c) The instance the repo constructs (READ: `Formalism/SizeWindowBrackets/FirstPrimeNeSecondPrime.lean:21–110`; `Formalism/ThickAverageLoss/PartnersToFactorsAt.lean:13–26`).**

*Setting.*
- A finite abelian F/ℚ with Galois group G = (ℤ/2)² × H.
- κ(g) = (−1)^{g₁}, with Φ = ker κ.
- κ cuts out K = ℚ(√−d), with d prime and d ≡ 7 (mod 8). DERIVED from `HostFacts`: 2 splits in K, d ramifies, and complex conjugation lies outside Φ.
- F is unramified outside {2, q, d}.

*Prime side.*
- ASK = 2 Σ log p · (a/p^i − w(class of p^i))₊, over *odd* powers p^i of primes p inert in K, plus a ramified term at d.
- So ASK carries the weight Λ(n)(1 − χ_K(n)).

*Main term.* MAIN = a(log a − 1 − γ + L′/L(1,χ_K) − mean_{ρ∈Φ} log w(ρ)).

*Exact identity (proved: `colour_balance`, `Formalism/SizeWindowBrackets/ChainSlopeWindows/StronglyIrreducible.lean:695`).*

  ASK − MAIN = |Φ|⁻¹ Σ_{g∉Φ} w(πg) Σ_{ψ∈Ĝ} ψ̄(g) G_ψ(a/w(πg)).

So the amplifier bounds a positive combination of detectors over the Dirichlet characters of F.

### 27.4 Can other L-functions satisfy the hypotheses? (DERIVED)

| Function | Verdict | Reason |
|---|---|---|
| Dirichlet L, any modulus (including ζ) | yes | proved |
| Dedekind ζ of abelian fields | yes | a product of Dirichlet L-functions |
| Hecke L with infinite-order characters (e.g. a CM elliptic curve) | unknown | Their prime weights are not class functions on a finite abelian Galois group over ℚ, and 27.3(c) has no version for them. This is the most plausible extension, since the CM inputs are nearby. |
| Non-abelian Dedekind ζ / Artin L | not covered | μ = 0 is known only for abelian fields (Ferrero–Washington). The CM period formula (Colmez) is known for abelian CM fields, some quartic cases, and on average. |
| GL(2) and higher, without CM | not covered | No algebraic integer is known whose valuations count λ_f(p) log p, and the coefficients are not sign-definite. |
| Davenport–Heilbronn, Epstein | fails | No Euler product, so no positive prime weights and no divisibility object. They have off-line zeros. |
| Beurling | fails | No ring of integers and no periods. |

### 27.5 What is general, what is specific to ℚ, what is specific to ζ (DERIVED)

**General.**
- The localized Landau criterion (positive coefficients plus one-sided bounds on long windows give a zero-free half-plane).
- Bost's inequality and the product formula.
- The amplification algebra.
- The per-place ledger.
- Near-orthogonality from symmetry plus scale.

**Specific to ℚ and its abelian arithmetic.**
- Kronecker–Weber: Frobenius classes correspond to Dirichlet characters.
- CM by K = ℚ(√−d), with Frobenius divisibility at inert primes.
- Chowla–Selberg (the source of γ, log 2π and L′/L(1,χ_K) on the arithmetic side).
- Ferrero–Washington.
- Siegel–Walfisz, Page, Siegel, and zero density near Re s = 1 (for the twists).

**Specific to ζ.** Only that ζ is the trivial character:
- It is the positive anchor: G₁ has coefficient 1 in every combination, because the weight 1 − χ_K always contains it.
- Its pole and Laurent constant (−ζ′/ζ = 1/(s−1) − γ + …) give the main term y log y − (1+γ)y. Chowla–Selberg reproduces the same γ on the arithmetic side.

## Addendum 28 — LinkG (d) traced backward (2026-11-22)

- Chain actually reached: linkG_concrete5 → linkG_concrete_noKer → link_of_local_closed → linkG_fam_noKer → linkG_without_kernels (depths 11–15). The real-chain variant `linkG_concrete` (LocalDataSystem hyps) is NOT reached.
- Clause (d) = ParametersFill (gain := gainP etc.; a FIELD of FamP, ParConsts.lean:62) + AuxBlock8.Conclusion1 (SmallOrderPrimes.lean:15, from Pf.stmtF on `admitted`) + lo_le_loG.
- Iteration: none. Accounting: by definition (g0 :246, gU :252, gainP :355, askG :368 in IsResidueClassZero.lean). Transfer: ParametersFill (assumed field), no valuation theorem.
- Only valuation clause on path: admG1 (iii) vKge ≥ Σ gainP + lowFE. Discharged by `zeroCh` (chain map := 0) + `vKge_zero`. Valid because Conclusion₂ doesn't mention Y; means clause (d) carries no valuation content.
- key_minor_dvd IS on chain: (a) → kW_ord → key3Ord → stmtEExt_of_15c → extendedClosedForm → Loc8.p15 → first theorem (κ-share bounds) → Adm8F → linkG_without_kernels; (b) key3Ord → RangeOne.tensor_closed → … → everyCharacter. Feeds κ bound, not gains.
- key_minor_dvd's `hp : p.Prime` is unused in the body; Frobenius enters via `frobCong` (FrobeniusPaths/LatticeCountingFormula.lean:29) supplying hMN in kW_ord.
- Open: which adm inputs stmtF uses for Conclusion1; where gain is used as a twist with the real chain (vKge reached via WeilJacquetShalikaLaw.CmpV → Cp.SelectionServed → Fc.HypsAlt; LinkMu).
- Doc: §8 written (rev 38); §7 "engine" sentence corrected; Remark 7.0a added; status-table row for LinkG (d).

## Addendum 29 — Is the gain earned by the actual map? (2026-11-22)

- LinkMu = NprimeMuR (GlobalTheoremInputs.lean:69/74). Proved by J.linkMu (SumLogPrimeFactorsLe.lean:728) from FAMILY FIELD nprimeDef (ParConsts.lean:71): (D.div.Nu u).L := span(Iu · NuLat u), Iu = Π 𝔭^(−⌊e·sg⌋) (DataDIVDefs.lean:17,22). So LinkMu = Prop 7.1 on a lattice DEFINED as the twist. Bookkeeping.
- RECEIPT = LinkDIV_at clause 1 OneMapIntoCC (DataArith.lean:180): Bk maps the enlarged lattice into RR dual ⇔ Bk(NuLat) ⊆ 𝔭^⌊e·sg⌋ · dual.
  Chain: linkDIV_at_words (RecBridge:327) ← WordFacts cl.1 (:128) ← DivisionPackageFace.wordFacts (:633; called as P.wordFacts — lexical graph MISSES dot-notation) ← ServJointF.val2AllAtRF (ServJointF:84) ← LocalQuadraticParts.adm2 (:206: actual period perCol is 0 or v ≥ ⌊e·sg⌋ on NuLat) ← admissible_level_two (AdmissibleAtGeneratorPlaces:214) / admissible_off_twist_places (:171) ← WJS.Conclusion1 for REAL Y = Fm.Gy (WJS:97) ← kernel_valuation_served (WJS:348) ← CmpV (WJS:156; proved by cmpV_of_cmpLite, ColumnWeightComparison:37, chain tied to actual column via exists_chain) + lattice valuations Σ gainP + low from SysTw + FormalGroupSystem.Pf.stmt_proved via unit_bound_of_sum_over_primes (JointsTw:243) in sum_over_primes_service (SumOverPrimesHypotheses:187).
  All meet at TopShape.lean:33 shape_closed_link_n_of_green (hServ → closed_family_admissible_twist_link_alt → bridge rows → LinkDIV; LinkG separately via closed_linkG_of_duty). cmpV_of_cmpLite on chain depth 20.
- Check 3: admG1(iii) map (Y.Ch) ≠ slope map (D.div.Bk). linkG_at_core:746 discards admG1(iii); NP/yProd (IsResidueClassZero:453) don't depend on Ch. zeroCh = disposable witness; never reaches slope argument.
- Check 2: OneMapIntoCC + height clause (only if Bk≠0) don't force Bk≠0. Nondegeneracy via MatReal_at in frameReal_at_of (TopDensityNGeSixteen:679), MatK built with LinkS (matKF_of :1348). Tie of matrix blocks to Bk on-chain NOT yet checked (visible only in off-chain FamRec.MatRec).
- Check 4: tensor_closed (TensorOfPairLift:597) = second proof of ExtendedClosedForm (p15) → Loc8All.inputs → First Theorem → wClosed (weight condition from mean excess, κ bound). Counting only.
- Verdict: gains ARE earned by the real map on the service branch; LinkG checks the same numbers beat prime sums. Next: trace SysTw and CmpLite suppliers (row-service chain under UpperTheory.Lit), and the MatReal↔Bk tie.
- Doc: §9 written (rev 41); status rows for LinkMu and Receipt.

## Addendum 30 — Zero-map test on the final slope bound (2026-11-22)

- Dependency structure: LinkMu is INDEPENDENT of LinkG (linkMu_of_linkDIV, SumLogPrimeFactorsLe:775, in topDesWin). LinkG + LinkMu → placesF_of (PlacesP:638) → slopesNF_of (TopDensityNGeSixteen:1544) = LOWER pan: μ(N_u) ≥ μ(base) + Ga + Fo − Ee − Lo (QuadraticLogDerivCongr:181). LinkDIV + LinkS + LinkIRR → matKF_of (:1348) → FrameReal_at (:519) → frame_at_of (:538) → FrameF (QLDC:258) = UPPER pan (avg μ(N_u) − h_u ≤ μdual(R)). linkCore (LossesSmallShares:38) compares. zeroCh only touches LinkG's unused admG1(iii).
- MatK_at (:807): Ball_u = Bf_u·Vr_u, Vr orthonormal cols, R-rows of Ball_u = matrix of D.div.Bk u; extra rows = Dall − Drows = delp·Dall (D_eq, DataRows:71); KdG ≈ I (HS ≤ e0·duS), cross KpG ≤ (1+η0)duS duS'/D*. Built from BesselId via blockReal_at_of (:1283; BlockReal_at :1087) + LinkS. Same field D.div.Bk as the receipt (OneMapIntoCC).
- Lemma Z (DERIVED): columns in e dims ⇒ (Σ‖C_u‖²)² ≤ e·Σ‖C_uᴴC_u'‖². Words where Bk = 0 carry rank S0 with S0[(1−de−√e0)² − delp(1+η1)(1+η0)] ≤ delp(1+η1)(1+√e0)² D* ⇒ fraction ≲ delp·sg. Bk ≡ 0 needs delp ≈ 1, contradicting LinkIRR. Numeric check: rh-extraction/zero_map_check.py (max ratio 1.000; delp ≥ 0.93 at errors 0.01).
- Verdict: numerical gains + zero map cannot produce the final bound. Open: whether a datum satisfying all constraints is actually constructed from the L-function (family existence / meaning); BesselId → BlockReal internals.
- Doc §10 (rev 43); status row "Zero-map test".

## Addendum 31 — Outside world caught up; meaning check closed (2026-11-23)

- STATUS (web, Nov 21–23): Lean FRO + Mathlib Initiative issued a joint statement (Nov 21) certifying the statement and proof of classical RH. Multiple independent kernels accept the export (Lean kernel, nanoda, con-leche [formally verified], con-ron, pestka per reports). Nov 22: sandboxed rebuild reproduced the 61,570,595,788-byte export. Nov 23: statement comparison + axiom check passed; full end-to-end `lake comparator` on original export still finishing. Repo moved to leanprover-community/riemann-hypothesis (community cleanup on `main`; `original` branch = our e50d098 content). Open in the world: human understanding (Tao: Langlands/arith geometry, will take time; Rubinstein draft reduces to 13 hypotheses; Robin Zhang provisional reconstruction). Clay still lists RH unsolved (needs publication + 2 yrs).
- Consequence: inner-definition "mismatch" hunting cannot find a correctness flaw — only the final statement (Mathlib's RiemannHypothesis), axioms, and checkers matter, and those are checked. Our doc's value = human-readable extraction.
- Meaning check (READ, e50d098): top is concrete. Level.Gm y = Gz y + Σ wt·Re gChi(ψ.χ, y) (ExplicitFormulaErrorOfHostConditions.lean:38) = detector family of §1; ZeroFreeAbove uses Mathlib DirichletCharacter.LFunction (:11). FormBAt/LandauWinAt (Window.lean:30) = Theorem 3 window Landau. Bridge: level_gm_le_on_family_scales → windowInequality_of_artinInputs → core_gm (CoreGm.lean) using gmA_eq (GmAEq.lean:61: host amplifier quantity GmA = Λ.Gm exactly, under EAtH + HostAddCharCompatible [ell ψ = L'/L(1,χ)]). Family nonempty by construction: FamCore fields Win_unb, Ix_win (FamCore.lean:71–80); ChainTied (TieGlobal.lean:97) is ∃ i0 member. DesignExists supplies the family in topDesWin (DesWin.lean:11).

## Addendum 32 — Codex expert map (2026-11-23)

- File: rh-extraction/expert-map.md (68.6 KB). Sources: Alpöge remark (20-step journal), Rubinstein v2 (Nov 22, 265 pp, H0–H12; sha b49de503…), Zhang (Nov 22, 76 pp; sha 3bd82fa3…), Tao blog, Lean FRO/Mathlib joint statement, Zulip #general thread.
- Nearly everything MATCHes our skeleton (Thm 1/2/3, √x theta chain, Bost slope, rank estimate). OURS ONLY: Add. 29–30 (receipt + near-isometry on the SAME D.div.Bk; zero-map test) — Rubinstein flags this as unresolved (H8, O25).
- Corrections: (a) Thm 3 anchor: zero_free_of_Chebyshev_growth (Landau:538) is the all-large-x version; real consumer level_of_tiedWin (TopWin:68) → FormBAt. (b) Add. 24 count: 195 theorem decls incl. final implication (194 before); only 177 names contain `of_literature`. (c) Add. 18.4 single-integer summary is illustrative only; source uses map/image lattice/mean slope.
- Gaps (priority): 1 projector denominators → height of actual period map (Zhang §5, Rubinstein S8/H1/H9); 2 classical theta kernel ↔ integral map in receipts (CmpLite normalization; lemniscate test); 3 size through linear term with exact volume/level allowances; 4 classical dictionary for rank+valuation on Bk/MatK/BlockReal; 5 good primes per family member (H12); 6 expository models.
- Community main snapshot ef349ac: some names renamed/removed (LandauWinAt, zero_free_of_Chebyshev_growth, GeneralHyps not found); FormBAt survives.
- Doc §11 written.

## Addendum 33 — Common period map: gap 4 closed at formal level (2026-11-23)

- Theorem (DERIVED from READ; Lean file written, compile pending): at each family member with LinkDIV_at + LinkS_at (+ ChosenProviso proviso), for each word u ∃ a≠0, isometry U(u), common isometry V with
  embLL(Bk u φ x) = a · besS u (U (jN φ)) (V (jEE x)),  besS u φ F = ⟪sEE F, s.Pu u (Cu⁻¹ eMu φ)⟫ (RhoDet…:353),
  OneMapIntoCC (receipt) for the same Bk, and hsDiagFull D u = ‖KD u u − 1‖² ≤ e0·duS with KD = Kmat = (c0 c0')^{-1/2} Pu† Pu' (RelevantZeroGramTerms:339,509), c0 = volN·volH/dimPi.
- Proof = BesselId (BuRational + Bessel identity) + LinkS_at diag clause; both inside on-chain inputs (matKF_of :1348).
- File: rh-extraction/CommonPeriodMap.lean (sha 573cd37b…): RHX.besS_eq, RHX.KD_eq, RHX.common_period_map, RHX.common_period_map_family, #print axioms.
- Codex prompt: rh-extraction/codex-prompt-common-period-map.md — compile against homeowmorphism/riemann-hypothesis-original with `lake exe cache get; lake build --no-build`; quote Rubinstein H8/O25 + Zhang L4.2/P4.3 wording.
- Gap 2 narrowed: remaining classical step = identify D.s.Pu with textbook theta-lift period map (c0, KExpansion :345).
- Also: level identity perCol u μ φ F = zeC u μ · Bu u φ (ι_μ F) with zeC root of unity (ZetaProductPairs:136–147, rows_form_without_side_condition) links receipts at level μ_w to Bu; adm1 bundle (LocalQuadraticParts:41) only reached via ambiguous refs.
- Doc §12 written.

## Addendum 34 — 2026-11-23: compile stop, closure route, Nielsen check, one-page proof

- Codex common-period-map-check.md: NOT compiled. C: 81.4 GB < 105 GB cache need; D: is exFAT with 1 MiB clusters (>=367 GB for .olean/.ilean). Partial checkout removed. Axioms unmeasured.
- Codex verdict (DERIVED): lemma PARTIALLY answers H8/O25 — ties Bk to matrix coefficients of Pu (besS, BuRational) and carries OneMapIntoCC (8a) + Gram/diag bound; does NOT derive the projected rank estimate (8c) nor identify the classical chain. Headline topDesWin supplies LinkDIV, LinkS, ChosenProviso on the same Fm (ShapeWin:27, DesWin:11, LinkMin:693/734, TopDensityNGeSixteen:1348).
- Closure route: import closure of Formalism.SharpRestriction.GlobalTheoremInputs at src tree 24df20b = 307 repo modules (~2.3 MB source) + Mathlib. List: rh-extraction/closure-files.txt (sha256 57c04567...). New prompt: rh-extraction/codex-prompt-compile-closure.md (A: build closure from source on C:\rhc + compile; B: classical identification; C: rank section (8c) -> CommonPeriodMap2.lean). Cloud workspace cannot reach Lean/Mathlib hosts.
- Nielsen (PhilArchive NIEIOT-2, PDF blocked to fetch; read via abstract excerpts, verification log, dev.to audit + comments, and source): anyGeometry := fun _ _ _ => True (OverIx.lean:19) is real, 24 files, reachable from Main (Tong audit). Does not affect validity: closed kernel-checked term for Mathlib RiemannHypothesis with standard axioms; an always-true slot only weakens a requirement. divEx_prov (TupPinsOfMuIsW.lean:204) still proves the real content (Y, h1-h4, LamAre), only the geometry conjunct is trivial. Same pattern as zeroCh (Add. 28). Zeng already posted a rebuttal -> not a new contribution for us. Write-up consequence: do not claim a geometric input at that step.
- Doc: new section "The proof on one page" after the byline; §12 Gap 4 corrected to "partly closed; compile pending".

## Addendum 35 — 2026-11-23: Part C answered (one map, three sections); no-credit compile script

- Codex out of credits. Claude did Part C from source (cloud clone, e50d098 tree).
- READ: H8's three sections all concern D.div.Bk u: (8a) OneMapIntoCC and (8b) htMap(Bk u) <= h u, both in LinkDIV_at (GlobalTheoremInputs:77); (8c) Lnk.MatK_at (TopDensityNGeSixteen:807) — matrix of Bk u at place v in normalized coords = top block of Bf u * Vr u, Vr isometry, Bf with KpG/KdG HS bounds; produced by matKF_of (:1348) from LinkS + ChosenProviso + LinkDIV(BesselId via blockReal_at_of :1283). frameReal_at_of (:679) bundles all three into LatGeom (one B); frame_at_of (:538) -> joint_a_ramified_holds (JointARam, FrameTraceRatioFinEquiv:197) -> Frame_at (mean-slope bound). This is Zhang Prop 4.3's shape.
- New file rh-extraction/CommonPeriodMap2.lean (sha256 5ccc4511...): RHX.one_map_three_sections — headline premises on one Fm give eventually (8a) ∧ (8b) ∧ MatK_at with eta0, sqrt e0 <= exp(-x^(eps/8)). Packaging only, no new math. Not compiled.
- Closure for TopDensityNGeSixteen = 705 modules (superset of the 307). closure-files.txt updated (sha256 74664cc7...).
- rh-extraction/compile-closure.ps1 (sha256 18e1e5bd..., ASCII, CRLF): Timmy runs it himself, no AI credits. Sparse partial clone at C:\rhc of 4e8bb36, verifies src tree 24df20b and 705 files, installs elan if missing, lake exe mathlib/cache get (Mathlib only; LAKE_ARTIFACT_CACHE=false), lake build TopDensityNGeSixteen from source, lake env lean on both files, PASS/FAIL + axiom check into compile-log.txt. Untested (cloud cannot reach Lean hosts).
- Still open: Part B (classical identification of s.HH/Cu/Pu, c0), compile verdicts.
- Doc: §12 table "One map, three sections"; one-page section updated.

## Addendum 36 — 2026-11-23: Gap 5 (one pair per window) read from source; Part B first look

- Gap 5 (READ): UpperTheory.Top.winPairs (CharacterBoxes/WinPairs.lean:5) is the formal H12. Inputs VWinAt ψ 401 (ExistsPageN.lean:44) + PairEx (PairGood.lean def; proved QH.pairEx, MeanSquareBounds/pairEx.lean:112 via pair_exists + kappa4, mean-square). Proof: fix k=c^(1/(2+8ε)); M ≥ max(1,y,Y1,k^3,k^400); X ≥ max(X0,M^J); Y=X^(1/J); one pair (q,d) good on [Y,X]; VWin gives W (X^(1/J) ≤ W, W^2 ≤ X); Z=kW; every x in [Z,Z^(3/2)] gets WinDatum with the SAME Y,q,d (x ≤ W^2 ≤ X since W ≥ k^3), e=e(x/k), cohomology bound at x/k ∈ [W,W^2] (k^400 ≤ x/k lifts 401→400). Consumer supplyOfAdmOf (ShortNorms/supplyOfAdmOf.lean:29) fixes CT2,C8,c6,Cb,x1 before the scale; hosts use H0.q=q, H0.d=d of the window. Open: map PairGood vs derived QDq/Boxq (PairRows.lean) to Rubinstein's Estimate B / C letters (needs his text).
- Part B first look (READ): S.Draft.SData (CuspSpanNormBounds/DataS.lean) is abstract: HH, Cu, Pu, volN, volH, Term/aTerm. exists_sStage (ExistsSStageUnconditional.lean:128) builds it with HH = ℂ^Dall, Pu = given P ∘ colEq, volN=volH=1, Term=Unit, aTerm=0; other call sites use P = 0 (line 222) etc. On headline path LinkS diag bound excludes Pu=0 (unfolding_constant_pos_of_diagonal). BesselId pins Pu's matrix coefficients to the arithmetic Bu up to isometries/scalars, so the classical content sits in what₂.Bu (perCol). Next: which S-stage the topDesWin family uses; trace Bu/perCol classically.
- Doc §13 written (Gap 5).

## Addendum 37 — 2026-11-23: Gap 5 B/C mapped; Gap 2 test bench (lemniscate + naive theta)

- Gap 5: Rubinstein v2 §I.6(e) pp.17-18: Estimate B (pair must satisfy: |Gχ(x)| ≤ x^(1/2+ε), χ = χq, χd, χqχd, x in [Y,Y^(3/2)]; Thm III.1.1(d)) ↔ PairGood.bounds at modulus one (Lean stronger: ε/2, on [Y,X], + log-deriv at 1) → QDq (qdq_of_pair, PairRows:299). Estimate C (follows; |Gχ(y)| ≤ y exp(-κ x^(ε/8)) for huge y; Thm III.2.1 using III.1.1(e)) ↔ derived from PairGood.boxes → Boxq (boxq_of_pair, PairRows:170); III.1.1(e) ↔ boxes is likely, unchecked. Compatibility: VWinAt applied to the same (q,d); IsChiField cuts fields by ψ,q,d.
- Gap 2 (COMPUTED, rh-extraction/gap2_lemniscate_check.py, results .txt): reproduced exactly Rubinstein's Hurwitz numbers, Thm Le18 table, 418/501 equality, max excess 4.625 at p=3 n=1945, no violations n ≤ 2001 inert p<200, split 5/13/17/29 never divide, A_(4k+1) ≡ 3^k mod 5, split p<200 dividing: 157,181 (p<2000: 30 primes). Le13: + sign integral to deg 4000 (p=3,7,11); − fails first at p^2. Naive Θ over Z[i]: r1..r5, denominators | 4^k (k ≤ 30), v3(r30)=14 vs 45, log sizes 119.0 vs 160.2; Θ/T0 = σ^2 ℘ cross-checked vs lattice sums (15 digits). NEW: naive kernel v_p(r_k) within 2 of n/(p^2-1) for all n ≤ 300, p = 3,7,11,19 — short by exactly a factor p vs np/(p^2-1). Numerical, not proved.
- Lean side (READ): BHyp (GaussJetBounds/Statement.lean:85) = (B1)-(B4) with letterLog = model L+; HasThetaProductForm (OrbitLabellings/ColDefs.lean) requires Th∘(ep·log) = U·exp(Σ±β∘log), U integral, BHyp each β; bHyps_of_beStd (SatakeParameters/StandardSeriesBConditionsLargePrime.lean:145) proves BHyp for BeStd β (level-one biextension data, biextension_hypotheses_of_level_one), l ≥ 5. Open: dictionary classical kernel → column with BeStd β; Lean needs l ≥ 5 while Rubinstein's worked case is ℓ = 3.
- Doc §13 B/C table; §14 Gap 2 test bench.

## Addendum 38 — 2026-11-23: GPT audit folded in; Adriazola novelty check

- GPT quoted Rubinstein v2 Thm III.1.1 (p.61): (d) eq. III.2 |Gχ(y)| ≤ y^(1/2+ε/2), |L'/L(1,χ)| ≤ 4 log y = PairGood.bounds verbatim; (e) eq. III.3 zero-free Re s > 1-1/400, |Im s| ≤ 8M exp(Y^(ε/5)) exp(Y^(ε/5)(log Y)^2) = PairGood.boxes with height at j=1 (Lean height M eps Y j = 8M exp(Y^(ε/5)) exp(Y^(ε/5) log^2 Y)^j). Remark (4): (e) excludes exceptional real zeros for Estimate C. B/C mapping now confirmed (via GPT quote + exact number match).
- supplyOfAdmOf confirmed to build the host H0 from the window's own pair (hF e he q d ... gives H0 with H0.q = q, H0.d = d), answering Rubinstein pp.214-215 "the construction must actually use such pairs".
- Adriazola repo cloned (commit 6f4e8cb, 23 Nov 11:23 MST), manuscript/ 225pp LaTeX. Findings: §18 gives H12-type window structure conventionally (admissible data with base Y0, Prop dataexist, uniform constant C) → our §13 classical content is his; ours adds the Lean route + B/C match. His §19 frontier lists Bessel dictionaries H-dict/H-rat (abstract Bessel realization ↔ automorphic objects, rationality of period maps) as class (O) open = our Part B / gap 4 classical side; seesaw relation H-see open. No mention of lemniscate or naive kernel in his sources → our gap-2 bench is not duplicated there. His Selmer-on-windows hypothesis is open (O).
- Doc §13 updated (exact III.1.1 match; prior-work credit to Adriazola); §14 prior-work note.

## Addendum 39 — 2026-11-23 16:15: FIRST LEMMA COMPILED; 705-module build failed on Mathlib cache files

- COMPILED: rh-extraction/common-period-map.out (written 15:48 local by Timmy's local Claude Code session, lake env lean in C:\rhc against the source-built closure; CommonPeriodMap.lean sha256 573cd37b... unchanged): RHX.besS_eq, RHX.KD_eq, RHX.common_period_map, RHX.common_period_map_family each "depends on axioms: [propext, Classical.choice, Quot.sound]". No errors.
- compile-closure.ps1 rerun 15:58: Mathlib step "No files to download / Already decompressed 8690", then lake build TopDensityNGeSixteen failed after 8.5 min. Errors are all of one kind: "failed to read file 'C:\rhc\.lake\packages\mathlib\.lake\build\lib\lean\Mathlib\...\<X>.olean.private'" for scattered Mathlib modules (Analysis.Calculus.Taylor, Complex.AbsMax, Calculus.UniformLimitsDeriv, Complex.ExponentialBounds, AffineSpace.Simplex.Centroid, Complex.Periodic, ...). Diagnosis: incomplete/corrupted Mathlib cache unpack (likely concurrent processes or AV locks), not a proof error. Fix: stop all lake/lean processes; in C:\rhc with MATHLIB_CACHE_GET_URL set run `lake exe mathlib/cache get!` (force re-download/unpack); verify Taylor.olean.private exists; rerun script. If it recurs, add C:\rhc to Defender exclusions.
- CommonPeriodMap2.lean not yet compiled (needs the 705 closure).
