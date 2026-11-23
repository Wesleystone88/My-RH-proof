# Codex task: map the experts' readings of the RH proof onto our extraction

## Why
The proof is certified (Lean FRO + Mathlib Initiative, Nov 21; several independent kernels; axiom
check passed). Correctness is settled. What nobody has released yet is a complete human-readable
account of HOW it works. Since the kernel accepts it, the mechanism is in the source and is
findable. Our extraction (RH-proof-handoff.md, Addenda 1–31) is one partial account. Experts have
started others. Your job: line them up against each other and against the Lean, so we can see what
is settled, what we have that they don't, and what we are missing.

## Pinned source
- Lean source: Deicyde/riemann-hypothesis @ e50d09817ad81469f737e8f637561e6ccf86c670
  (= `original` branch of leanprover-community/riemann-hypothesis). Give anchors as
  `file:line` at this commit. If a declaration was renamed on `main`, give the `main` name too.
- Our notes: ../RH-proof-handoff.md (read Addenda 24–31 first; they summarize the rest).

## Our structure, for the mapping (short form)
- **Theorem 1 (arithmetic identity).** ASK − Main = |Φ|^-1 Σ_{g∉Φ} w(πg) Σ_ψ ψ̄(g) G_ψ(a/w(πg)),
  G = (ℤ/2)² × H, K = ℚ(√−d), d ≡ 7 mod 8. Lean bridge: `gmA_eq` (GmAEq.lean:61), `core_gm` (CoreGm.lean).
- **Detectors.** Λ.Gm y = Gz y + Σ wt·Re gChi(ψ.χ, y) (ExplicitFormulaErrorOfHostConditions.lean:38);
  ramp detector G_χ(y) = Σ Λχ(n)(y/n − 1) + y·L′/L(1,χ).
- **Theorem 2 (amplified bound).** Averaged chain with seven inputs (G), (Dv), (Ct), (E), (Sl), (SI), (L).
  Gains and main term both linear in m; fixed costs paid once; m ≈ √x.
  Lean inputs: LinkG, LinkMu, LinkDIV, LinkS, LinkIRR, LinkEta, LinkN (GlobalTheoremInputs.lean); `linkCore`.
- **Theorem 3 (window Landau).** FormBAt / LandauWinAt (Window.lean:30); zero_free_of_Chebyshev_growth (Landau.lean:538).
- **Receipts (Addendum 29).** The gains are earned by the real map:
  OneMapIntoCC ← WordFacts ← val2AllAtRF ← LocalQuadraticParts.adm2 ← admissible_level_two ←
  WeilJacquetShalikaLaw.Conclusion1 (real lattice instance) ← CmpV/cmpV_of_cmpLite + SysTw/FormalGroupSystem.
- **Nondegeneracy (Addendum 30).** MatK_at / BlockReal_at tie Bk's matrix to a near-isometry (LinkS, BesselId).
- **Three non-literature pieces (Addendum 24).** (i) every_character_of_theta_integrals_local_matching,
  (ii) topCovolSlim2_use_alt_alt, (iii) VWin. Everything else wraps 194 literature theorems.

## Steps
1. **Collect the expert sources.** At least: Alpöge's remark.pdf (alpo.ge/remark.pdf, sha256
   3fc97784b71ddd44ff8aa0a177e99622a1c61b13cfa843a0989ee4a7a0cfeb8d); Michael Rubinstein's draft
   (reported to reduce the bound to thirteen hypotheses); Robin Zhang's reconstruction note; Terence
   Tao's comments; the Lean FRO / Mathlib joint statement; any Lean Zulip thread that describes the
   proof's structure. For each: URL, date, version or hash. Prefer primary documents over news.
   If a source is unreachable, say so and move on.
2. **Extract each expert skeleton.** Number every hypothesis or step in their own order (e.g.
   Rubinstein H1–H13), paraphrased in one or two lines each, with the page or section.
3. **Map, item by item.** One table per source:
   | Expert item | Our item (theorem / input / addendum) | Lean anchor (decl, file:line) | Verdict |
   Verdict is one of: MATCH · THEIRS ONLY (we lack it) · OURS ONLY (they lack it) · CONFLICT.
   For every CONFLICT, read the Lean and say which reading the source supports.
4. **Locate the new idea.** Which expert items fall inside the three non-literature pieces
   (i)–(iii), and which are published results used as tools? Name the single step each expert
   treats as the main new input, and check whether the Lean agrees.
5. **List the gaps in our extraction.** Concretely: which expert items have no counterpart in
   Addenda 1–31, ordered by how much of the argument they carry.

## Rules
- Labels: READ (inspected in source or document), DERIVED (follows from cited statements),
  COMPILED (checked by Lean this run). Do not mark anything COMPILED unless you ran it.
- Do not modify the repository. Paraphrase sources; quote at most a short phrase, with a link.
- Plain language first in every section: one picture or analogy, then the technical terms.

## Output
Write `rh-extraction/expert-map.md`:
1. A one-paragraph plain-language summary of where the readings agree and where they split.
2. The source list (step 1).
3. The mapping tables (step 3).
4. The "new idea" finding (step 4).
5. The gap list (step 5).
