# Batch 1 against Rubinstein v2

**DERIVED.** H1, H2, H3, H6 and H9 give the same statement as Rubinstein's, clause by clause, on the selected family. `CommonPeriodMap2.lean` (our H8) is **different**: it gives the ingredients of Rubinstein's H8, (8a), (8b) and a Zhang-style form of (8c), and it does not state his H8 inequality (III.330). Together with batch 2 (H4 and H5 same), that is **7 files that match, not 8**. The count of 8 in earlier public posts is not supported by this audit.

**READ.** Verdicts follow the batch 2 usage. **Same:** the Lean conclusion has every clause of the paper's statement, with the same inequality shape, and no clause missing, changed or extra, once the objects are identified. The family quantifier "one constant and one threshold for every late index" is the convention of batch 2 and is not counted as a difference. **Weaker:** a clause or an identification is dropped. **Different:** a clause is changed, or the Lean statement says something else about the same objects.

**Update (24 Nov, afternoon):** a new file, `H8.lean`, states (III.330) through `frame_at_of`; see the last section ("H8 (new file)"). My first reading graded it "same". Codex's independent check ([`h8-frame-check.md`](h8-frame-check.md)) grades it **different in scope only**: (III.330) matches term by term, but the Lean statement is a family theorem with an eventual scale threshold and `0 < CH`. The official tally stays 7 same, 2 weaker, 4 different (H8 counted as different).

**Read this first: in H1, H2, H3, H9, H6(i), (8a) and (8b) the premise states the conclusion.** Each of these Lean theorems takes `LinkDIV Fm Cabs CH` as a hypothesis, and `LinkDIV_at` already contains the conclusion verbatim as one of its nine conjuncts. The proof is a projection (`exact (hD x hx i).2.2.2.2.2.2.1` and so on). So "same" means the Lean statement matches the paper's statement. It does **not** mean Lean re-derived Rubinstein's status argument. That argument (for example Theorem III.7.1 for H1) is not reproduced; the source supplies `LinkDIV` elsewhere. Only H6(ii)(iii) and (8c) go through real source theorems (`slopesNF_of`, `matKF_of`).

The nine conjuncts of `LinkDIV_at`, in order ([GlobalTheoremInputs.lean:77–89][gti-linkdiv]): (1) `OneMapIntoCC`; (2) `sFrame … + RR.muMax ≤ x^CH · b`; (3) `ZeroAbove`; (4) `BesselId`; (5) `RRFull`; (6) the height bound `htMap … ≤ h u`; (7) the pairing-size inequality; (8) the level-correction inequality; (9) the height comparison. H9 uses (2); H6(i) and (8a) use (1); (8b) uses (6); H1 uses (7); H2 uses (8); H3 uses (9).

**Identifications used throughout (DERIVED, from definitions read at `4e8bb36`; Rubinstein himself says the rows of the §III.10 dictionary for §III.7 are not verified).**

| Paper | Lean | Evidence |
|---|---|---|
| word w, translate u | binder `u : D.what₂.Word` | the theorems quantify `∀ u` |
| μ_CC | `(Fm.D x i).div.RR.muDual` | [DataArith.lean:98][da-mudual]; same slot as the left side of `Frame_at` ([QuadraticLogDerivCongr.lean:188–193][qldc-frame]) |
| μ_CC^min | `RR.muMinDual`, equal to `−RR.muMax` only inside `Lat_at` | [QuadraticLogDerivCongr.lean:185][qldc-lat] |
| the target R^∨ | `D.cc := D.RR.dualL` | [DataArith.lean:168][da-cc] |
| glued lattice Λ^gl_w, first lattice Λ^0_w | `(D.div.Nu u)`, `((D.fm u).lat 0)` | both appear in `SlopesN_at` ([QuadraticLogDerivCongr.lean:181][qldc-slopesn]) |
| s_u | `sFrame D.div.Nu D.div.h`, the d_w-weighted mean of `μ − h` | [DataArith.lean:131][da-sframe]; matches the paper's "mean over the words with the weights d_w" |
| A = Σ_t a_t, \|T\| | `∑ t, L.aT t`, `D.host.TT.card` | `MAIN` ([DataParams₂.lean:232][dp-main]) |
| Lv(w) | `(D.mem u).A.T` | used in `MAIN` and `LoU` |
| G_top, F_0, E_err(w) | `L.Ga`, `L.Fo`, `L.Ee u` | `Ee u = ∑ j, ∑ w, sz w (E u j w)` ([DataParams₂.lean:222][dp-ee]) |
| I_u | `IOsum L` | [QuadraticLogDerivCongr.lean:163][qldc-iosum] |
| log Ω_E | `L.logOm` | **GUESS.** Same role in `MAIN`; not checked against the §III.7 definition of Ω_E ([DataParams₂.lean:224][dp-logom]). |

## H1 — same

**READ.** (III.324), p. 204: for every word w, $\mu_{CC}+h_w-F_0\le S-A\log \mathrm{Lv}(w)+c_1|T|\,a\,L_a+c_1\,m\,(B_0+N_c)\,x^{C_{abs}\varepsilon}$, where $S=\sum_{t\in T}m\,(a_t\log a_t-a_t-a_t\log\Omega_E)$. For $C_{abs}=2$ it is (III.76), proved from Theorem III.7.1's inputs; in the source $C_{abs}$ is a free parameter $\ge0$. [Rubinstein v2, p. 204](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=204)

| Paper clause | What `RHX.h1_pairing_size` gives (DERIVED) |
|---|---|
| $\mu_{CC}+h_w-F_0\le\dots$ | `RR.muDual + h u − Fo ≤ …` ([H1.lean:20][h1-20]) |
| $S-A\log\mathrm{Lv}(w)$ | `L.MAIN u`, which is $\sum_t\big(m(\mathrm{phF}(a_t)-a_t\log\Omega)-a_t\log\mathrm{Lv}\big)$ with `phF y = y log y − y` ([DataParams₂.lean:49, 232][dp-main]). This equals the paper's $S-A\log\mathrm{Lv}(w)$ once log Ω is identified. |
| $c_1|T|aL_a$ | `C * TT.card * sc.a * La` ([H1.lean:22][h1-20]) |
| $c_1m(B_0+N_c)x^{C_{abs}\varepsilon}$ | `C * m * (B0 + Nc) * x ^ (Cabs * eps)` ([H1.lean:23–24][h1-20]) |

**DERIVED.** Same inequality, with one constant C for both error terms, as the paper's single $c_1$. $C_{abs}$ is a theorem parameter, as in the source. The conclusion does not say $C\ge0$; since $|T|$, $a$, $L_a$, $m$, $B_0+N_c$ are nonnegative at late indices, a negative C would only strengthen it, so nothing is lost. **Premise note:** the conclusion is conjunct (7) of `LinkDIV_at` verbatim ([GlobalTheoremInputs.lean:82–84][gti-linkdiv]); the proof is a projection ([H1.lean:25–26][h1-20]). The one unchecked item is the **GUESS** log Ω_E ↔ `logOm`.

## H2 — same

**READ.** p. 204: "For every word and every lift j, $|E_{err,j}(w)-A\,\ell_g|\le c_2B_0$. Hence $|E_{err}(w)-mA\ell_g|\le c_2mB_0$", with $\ell_g=\log(g_0g_1)$. The status says it is "assumed here, from the Lean development". [Rubinstein v2, p. 204](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=204)

| Paper clause | What `RHX.h2_level_corrections` gives (DERIVED) |
|---|---|
| $\forall$ word, $\forall$ lift j: $\lvert E_{err,j}(w)-A\ell_g\rvert\le c_2B_0$ | `∀ u, ∀ j ∈ lifts, \|∑ w ∈ supp, sz w (E u j w) − (∑ t, aT t) * log (g 0 * g 1)\| ≤ C * B0` ([H2.lean:19–22][h2-19]) |
| "Hence" $\lvert E_{err}(w)-mA\ell_g\rvert\le c_2mB_0$ | **Not stated.** It follows by summing over the m lifts, since `Ee u = ∑ j, ∑ w, sz w (E u j w)` ([DataParams₂.lean:222][dp-ee]). It is DERIVED, not asserted by the theorem. |

**DERIVED.** The primary inequality is the same. The "Hence" clause is a consequence in the paper and is absent as a separate conclusion; I count it as same because it is a one-line sum. **Premise note:** conclusion is conjunct (8) of `LinkDIV_at` verbatim ([GlobalTheoremInputs.lean:85–86][gti-linkdiv]); projection proof ([H2.lean:23–24][h2-19]). The paper's description of the source form ("the part away from $g_0,g_1$ is at most a multiple of $B_0$") is a different statement from this conjunct; it is not part of H2 as Rubinstein states it.

## H3 — same

**READ.** (III.325), p. 204: for all words $w,w'$, $\big|(h_w+A\log\mathrm{Lv}(w))-(h_{w'}+A\log\mathrm{Lv}(w'))\big|\le c_3(|T|aL_a+mB_0)$. Status (p. 205): assumed from the Lean development; "we did not read its proof". [Rubinstein v2, p. 204](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=204) · [p. 205](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=205)

**DERIVED.** `RHX.h3_height_comparison` has the same two-word inequality: `|(h u + (∑ aT) * log A.T) − (h u' + (∑ aT) * log A.T')| ≤ C * (TT.card * a * La + m * B0)` ([H3.lean:19–25][h3-19]). Every term matches term for term. **Premise note:** conjunct (9) of `LinkDIV_at` verbatim ([GlobalTheoremInputs.lean:87–89][gti-linkdiv]); projection proof ([H3.lean:26–27][h3-19]). Same.

## H6 — same

**READ.** (III.328), p. 205: for every word, (i) $\beta_w(\Lambda^{gl}_w)\subset\mathcal R^\vee$; (ii) $\mu(\Lambda^{gl}_w)\ge\mu(\Lambda^0_w)+G_{top}+F_0-E_{err}(w)-\mathrm{Lo}_w$ with $\mathrm{Lo}_w=c_6I_u+c_6|T|\,m\,(a/k+b')\log\mathrm{Lv}(w)+c_6X''+1$; (iii) $\mu_{\max}(\Lambda^{gl}_w)\le\mu_{\max}(\Lambda^0_w)+G_{top}+F_0-E_{err}(w)+c_6mB_0$. Status: (i) is Theorem L4(i); (ii) is (III.118); (iii) is Lemma M10; "none is proved outright". [Rubinstein v2, p. 205](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=205)

| Paper clause | What `RHX.h6_glued_lattice` gives (DERIVED) |
|---|---|
| (i) $\beta_w(\Lambda^{gl})\subset\mathcal R^\vee$ | `OneMapIntoCC`: `(Nu u).L.map (Bk u) ≤ D.cc`, with `cc = RR.dualL` ([DataArith.lean:168, 180][da-cc]) |
| (ii) lower slope bound with $\mathrm{Lo}_w$ | second conjunct of `SlopesN_at`: `((fm u).lat 0).mu + Ga + Fo − Ee u − LoU L C u ≤ (Nu u).mu`; `LoU = C·IOsum + C·TT.card·m·(a/k+b')·log A.T + C·X'' + 1` ([QuadraticLogDerivCongr.lean:177–183][qldc-slopesn]). Same four terms. |
| (iii) upper max-slope bound | first conjunct: `(Nu u).muMax ≤ ((fm u).lat 0).muMax + Ga + Fo − Ee u + C·m·B0`. Same. |
| $c_6\ge0$, one threshold | `0 ≤ C` is in the conclusion; the larger of the two thresholds serves all three ([H6.lean:20–26][h6-18]) |

**DERIVED.** All three clauses, same shape, same constants, at the same word. **Premise note:** clause (i) is conjunct (1) of `LinkDIV_at` verbatim. Clauses (ii) and (iii) are **not** a premise restated: they come from the source theorem `slopesNF_of` ([TopDensityNGeSixteen.lean:1544][td-slopesnf]), which takes `PlacesF Fm` ([:1541][td-slopesnf]), a family of place-level hypotheses (`HypLow`, `HypLow2`, `HypHigh`, `Places_at`, [:1516–1527][td-places]), and is proved through `slopesN_at_of` ([:1529][td-places]) and the partition lemmas. So (ii)(iii) rest on a real source proof from `PlacesF`. Whether `PlacesF` itself holds for the headline family is not part of this file.

## H8 (`CommonPeriodMap2.lean`) — different

**READ.** (H8), (III.330), p. 206: there are real numbers $\eta_u,e_u\ge0$ with $(\eta_u+4\sqrt{e_u})x^{C_H}\le6$ such that for every $R>0$ with $s_u-\mu^{\min}_{CC}\le R$,
$$\mu_{CC}\ \ge\ s_u-\log|W_u|-\frac1{1-\delta_p}\Big(4\,sp_u\log\big(1+\tfrac{R}{sp_u}\big)+(\eta_u+4\sqrt{e_u})R\Big).$$
Its status: it follows from Proposition M4 and three statements for **one map** $\beta_w$: (8a) $\beta_w(\Lambda_w)\subset Q$, which is H6(i); (8b) $\mathrm{ht}(\beta_w)\le h_w$ whenever $\beta_w\ne0$; (8c) the rank bound of Proposition M4 with $\eta_*=5x^{-C_H}+4\alpha_{ram}+4\sqrt{e_0}$, the conclusion (III.236) of Corollary T2. Rubinstein adds that the three maps come from different sections and that their identification is "a further assumption" that "was not checked in the source". [Rubinstein v2, p. 206](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=206)

| Paper clause | What `RHX.one_map_three_sections` gives (DERIVED) |
|---|---|
| (III.330) itself, the inequality with $\eta_u,e_u$ | **Missing.** The theorem does not state it. In the source it is `Frame_at` ([QuadraticLogDerivCongr.lean:188–193][qldc-frame]) and, over the family with $(\eta+4\sqrt e)x^{C_H}\le6$, `FrameF CH` ([:258][qldc-framef]). |
| (8a) | `OneMapIntoCC`, same as H6(i) ([CommonPeriodMap2.lean:46][cpm2-41]). Same. |
| (8b) $\mathrm{ht}(\beta_w)\le h_w$ if $\beta_w\ne0$ | `∀ u, Bk u ≠ 0 → htMap … (Bk u) ≤ h u` ([CommonPeriodMap2.lean:47–49][cpm2-41]). Same. |
| (8c) the rank bound with $\eta_*$ | **Changed.** `MatK_at D η0 e0` ([TopDensityNGeSixteen.lean:807–819][td-matk]): the matrix of the same `Bk u` at one place equals the top block of `Bf u * Vr u`, with `Vr u` an isometry and Hilbert–Schmidt bounds on the off-diagonal (`KpG`, $\le(1+\eta_0)\,d_ud_{u'}/D_*$) and diagonal (`KdG − 1`, $\le e_0d_u$) Gram operators. This is Zhang's Lemma 4.2 / Prop. 4.3 form, as the file header says, not the rank bound of Proposition M4. |
| extra | $-1\le\eta_0\le\exp(-x^{\varepsilon/8})$, $0\le e_0$, $\sqrt{e_0}\le\exp(-x^{\varepsilon/8})$, with $\eta_0,e_0$ chosen per index. These bounds are not in H8. |

**DERIVED.** The theorem proves that one map `Bk u` carries the inclusion, the height bound and a Gram block form at once. That is the **one map** question Rubinstein raised, but only in the source's own vocabulary, where all three are stated for the single object `D.div.Bk u`. So "the three maps are one map" holds **by construction of the source's records**. It does not show that the §III.6 pairing, the §III.7 map Φ and the §III.8 pairing equal `Bk`; that is the classical dictionary, and it stays open.
H8's own inequality is reached in the source by two further theorems: `frameReal_at_of` ([:679][td-framereal]) turns the block form into `FrameReal_at`, and `frame_at_of` ([:538][td-frameat]) then gives `Frame_at D (5·sg + 3√de) eB`. With `sg = x^{-CH}` and the constants of that proof, $\eta_u=5x^{-C_H}+3\sqrt{\alpha_{ram}}$ and $e_u=2e_0$, which are the values Rubinstein quotes from (III.239). `frame_at_of` needs more than our three premises: `ChProviso_at`, `ChCode_at`, `D.NuFull` and `Lat_at`. Our file does not state or use it. **Premise note:** (8a) and (8b) are conjuncts (1) and (6) of `LinkDIV_at` verbatim ([GlobalTheoremInputs.lean:78, 80–81][gti-linkdiv]); (8c) comes from the source theorem `matKF_of` ([:1348][td-matkf]) with premises `LinkS`, `ChosenProviso` and `LinkDIV`, a real proof. The file's own header already says "It adds no new mathematics".

## H9 — same (in the source's form)

**READ.** p. 206: "$s_u-\mu^{\min}_{CC}\le x^{C_H}b$. Assumed here, from the Lean development. (The source states it as $s_u+\mu_{\max}(\mathcal R)\le x^{C_H}b$, with $\mu_{\min}(\mathcal R^\vee)=-\mu_{\max}(\mathcal R)$.)" [Rubinstein v2, p. 206](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=206)

**DERIVED.** `RHX.h9_target_slope` states `sFrame Nu h + RR.muMax ≤ x ^ CH * b` ([H9.lean:20–22][h9-18]), which is exactly the form Rubinstein says the source uses. To read it as his $s_u-\mu^{\min}_{CC}\le x^{C_H}b$ one needs $\mu_{\min}(\mathcal R^\vee)=-\mu_{\max}(\mathcal R)$. In Lean that identity is the second clause of `Lat_at` (`RR.muMinDual = −RR.muMax`, [QuadraticLogDerivCongr.lean:185–186][qldc-lat]), **not** a conclusion of H9. So the match is exact to the source's form and to Rubinstein's form only through that identity, which he states himself. The threshold is `∃ x0` with no constant, as in the paper, where $C_H$ is one of the fixed constants. **Premise note:** conjunct (2) of `LinkDIV_at` verbatim ([GlobalTheoremInputs.lean:78][gti-linkdiv]); projection proof ([H9.lean:23–24][h9-18]).

## Summary

| Hypothesis | Verdict | Reason |
|---|---|---|
| H1 | **same** | Same inequality (III.324), one constant for both terms; conclusion is conjunct (7) of `LinkDIV_at`. log Ω_E ↔ `logOm` is a GUESS. |
| H2 | **same** | Same per-lift inequality; the paper's "Hence" sum form follows by one summation and is not stated separately. |
| H3 | **same** | Same two-word inequality term for term; conjunct (9). |
| H6 | **same** | Clauses (i)–(iii) all present with the same $\mathrm{Lo}$ and $c_6mB_0$; (i) is conjunct (1), (ii)(iii) come from `slopesNF_of` given `PlacesF`. |
| H8 (`CommonPeriodMap2`) | **different** | Gives (8a), (8b) and a Zhang-form block (8c); does not state (III.330), changes (8c), adds $\eta_0,e_0$ bounds. One map is by construction, not a dictionary result. |
| H9 | **same** | The source's own form of H9, as Rubinstein notes; equals his form via `Lat_at`'s identity, which is not in the theorem. |

**What this audit did not check.** No Lean was run; every compile result is in the `.out` files. I read the Lean files, the `LinkDIV_at` definition and the definitions behind the table above at `4e8bb36`, and Rubinstein's pp. 203–207 (text and page images). I did not read §III.7's definition of Ω_E, the definitions of `Places_at`'s hypotheses in full, or any proof body beyond the statements quoted. "Same" is a statement-level comparison under the identifications in the table; Rubinstein warns that the rows of the §III.10 dictionary for §III.7 are not verified.

## H8 (new file)

**READ.** `results/rubinstein-hypotheses/H8.lean` ([H8.lean:46–51][h8n]), theorem `RHX.h8_frame`, compiled on 24 Nov 2026 (`H8.out`: `propext`, `Classical.choice`, `Quot.sound`). Its conclusion is `Lnk.FrameF Fm CH`, the source's family-level statement of (III.330) ([QuadraticLogDerivCongr.lean:258–260][qldc-framef]; `Frame_at`, [:188–193][qldc-frame]). It is proved by the source's `frameF_of` ([TopDensityNGeSixteen.lean:606][td-framef]), whose proof calls `frame_at_of` ([:538, :645][td-frameat]). **No premise contains `Frame_at`, `FrameReal_at` or `FrameF`:** the `FrameRealF` it needs is built by `frameRealF_of''` ([:988][td-framef]) from `MatKF`, which comes from `matKF_of` ([:1348][td-matkf]) given `LinkS`, `ChosenProviso`, `LinkDIV`; `LatF` comes from `latF` with `rrRankF_of`. This is the route of the source's own `linkGLOBAL7_items` ([LinkMin.lean:706–717][lm-items]).

| Paper clause (III.330), p. 206 | What `RHX.h8_frame` gives (DERIVED) |
|---|---|
| there are $\eta_u,e_u\ge0$ | `∃ η e, 0 ≤ η ∧ η ≤ etaB ∧ 0 ≤ e ∧ e ≤ eB` inside `Frame_at` |
| $(\eta_u+4\sqrt{e_u})x^{C_H}\le6$ | `FrameF` states $(etaB+4\sqrt{eB})\,x^{C_H}\le6$ with $\eta\le etaB$, $e\le eB$; the paper's bound follows by monotonicity of $\sqrt{\ }$ since $x^{C_H}\ge0$ |
| for every $R>0$ with $s_u-\mu^{\min}_{CC}\le R$ | `∀ HH, sFrame … − RR.muMinDual ≤ HH → 0 < HH →` |
| $\mu_{CC}\ge s_u-\log|W_u|-\frac1{1-\delta_p}\big(4\,sp_u\log(1+\tfrac R{sp_u})+(\eta_u+4\sqrt{e_u})R\big)$ | `sFrame − log (card Word) − (1 − delp)⁻¹ * (4 * uFrame * log (1 + HH / uFrame) + (η + 4 * √e) * HH) ≤ RR.muDual`. Same shape, term for term. |
| constants $\eta_u=5x^{-C_H}+3\sqrt{\alpha_{ram}}$, $e_u=2e_0$ (III.239) | In the proof, `frame_at_of` returns `Frame_at D (5·sg + 3√de) eB` with `sg = x^{-C_H}`, and its witnesses are `η = 5·sg + 3√de`, `e = 2·e0`. The **statement** of `FrameF` exposes only the bounds, so the file states only that. |
| "$x$ large", translate $u$ | `∃ x0, ∀ x ≥ x0, … ∀ i`, the family-eventual convention of batches 1 and 2 |

**Premises, and what they do.** `LinkDIV`, `LinkS`, `LinkIRR`, `ChosenProviso`, `ChosenCode` (from `GlobalTheoremInputs` and `Chosen`), plus `hNF : NuFullF`, `hRk : J.MuRank`, `hTu : TuSize`, `Lnk.RamRankF`, which the source builds from `hT2`, `hT5` in `LinkMin.lean` (outside the 705-module closure, so taken as premises). None of them states the conclusion; the work is done by `matKF_of`, `frameRealF_of''`, `latF` and `frame_at_of`. **GUESS:** these premises correspond in role to the named statements of Rubinstein's status paragraph ((S), (I), (III.234), …); I did not check that correspondence.

**Differences from the paper (all strengthen).** (1) `etaB` and `eB` are chosen per scale $x$ and serve every index $i$; the paper's $\eta_u,e_u$ are per translate. (2) `FrameF` also asserts $eB\le1/4$; the paper lists $e_u\le\tfrac14$ among the source's "three further conditions" that "are not part of (H8)". (3) The identification of $sp_u$ with `uFrame` was not checked against (III.315) when I wrote this; it is settled below.

**First-reading verdict: same.** The conclusion has every clause of (III.330) with the same inequality, and no clause is missing or changed. The two extras only strengthen it; batch 2 also counted H4 and H5 as same although they add a nonnegative constant. A stricter reading that counts any extra clause as a difference would call it different; I judge that the extras do not change what is asserted.

**Independent check (Codex, [`h8-frame-check.md`](h8-frame-check.md)).** Codex wrote its sections 1 to 4 before reading this section. It grades `RHX.h8_frame` **different as a whole statement** (family form, eventual scale threshold, and the restriction `0 < CH`; the paper states H8 for one fixed scale and translate, and the Lean wrapper is a conditional family theorem) but the **same inequality term by term**: no term of (III.330) is lost on the shared domain. It adds that `FrameF` supplies a bare existential error coefficient that can be redistributed, so "all strengthen" above was too quick. **Settled:** both notation questions are now yes: $sp_u$ is `uFrame` (the spread in (III.315); only the subtracted mean is rank weighted), $s_u$ is `sFrame` (the rank-weighted mean of $\mu - h$), and $\mu_{CC}$, $\mu_{CC}^{\min}$ are `muDual`, `muMinDual` (the dual of $R$). **Still not settled:** the correspondence between each premise and a named statement in Rubinstein's status paragraph (the GUESS above); Codex did not establish it either. Codex also corrects the premise provenance in the `H8.lean` header comment (builders occur in several files, `muRank_min` needs the chosen proviso, `TuSize` is assumed at `LinkMin.lean:701`, `ramRankF_min` is a projection and cast at line 718); the comment is fixed and the statement is unchanged.

**Official grade for H8: different in scope only; (III.330) matches term by term.** The official tally stays **same** H1, H2, H3, H4, H5, H6, H9 (7); **weaker** H0, H12 (2); **different** H7, H8, H10, H11 (4). H8 is counted as different on both files: `CommonPeriodMap2.lean` states the ingredients, not (III.330), and `H8.lean` is different in scope only. Of the seven "same", H1, H2, H3, H9 and H6(i) are projections of `LinkDIV` as described at the top; H6(ii)(iii) go through real source theorems, and so does `H8.lean`'s conclusion.

*Written by Claude Code (reading task, 24 Nov 2026). The Lean statements of H1, H6 and batch 2 were drafted by Codex; H2, H3 and H9 by Claude (Opus, chat).*

[gti-linkdiv]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalTheoremInputs.lean#L77-L89
[da-mudual]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataArith.lean#L98
[da-cc]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataArith.lean#L168-L180
[da-sframe]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataArith.lean#L131
[dp-main]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataParams%E2%82%82.lean#L232-L235
[dp-ee]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataParams%E2%82%82.lean#L222
[dp-logom]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataParams%E2%82%82.lean#L224
[qldc-iosum]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L163
[qldc-slopesn]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L177-L183
[qldc-lat]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L185-L186
[qldc-frame]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L188-L193
[qldc-framef]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean#L258-L260
[td-matk]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L807-L819
[td-matkf]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1348
[td-framereal]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L679
[td-frameat]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L538
[td-places]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1516-L1529
[td-slopesnf]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1541-L1544
[h1-20]: ../results/rubinstein-hypotheses/H1.lean#L17
[h2-19]: ../results/rubinstein-hypotheses/H2.lean#L17
[h3-19]: ../results/rubinstein-hypotheses/H3.lean#L17
[h6-18]: ../results/rubinstein-hypotheses/H6.lean#L18
[h9-18]: ../results/rubinstein-hypotheses/H9.lean#L18
[cpm2-41]: ../results/common-period-map/CommonPeriodMap2.lean#L41
[h8n]: ../results/rubinstein-hypotheses/H8.lean#L46-L51
[td-framef]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L606-L648
[lm-items]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L706-L717
