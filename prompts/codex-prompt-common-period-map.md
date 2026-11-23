# Codex task: machine-check the common-period-map lemma against the real project

## What to check
`rh-extraction/CommonPeriodMap.lean` (sha256 573cd37bb2621d52be6e4f124eda0b35cb3565db1818d4b57aa2f004d5888410)
states four results about the published proof, all built from the source's own definitions:

- `RHX.besS_eq`: the Bessel period `D.besS u` is the matrix coefficient of the period map `D.s.Pu u`.
- `RHX.KD_eq`: the operator in `hsDiagFull` / `LinkS_at` is `S.Kmat D.s u u`, the normalized Gram of `D.s.Pu`.
- `RHX.common_period_map`: from `LinkDIV_at` and `LinkS_at` at one family member, the divisibility receipt
  (`OneMapIntoCC`), the Bessel identity (embLL ∘ Bk = a · besS(U·, V·)) and the near-isometry bound hold
  for the same map `D.div.Bk u`.
- `RHX.common_period_map_family`: the same, eventually, for every member of a family with `LinkDIV`,
  `LinkS` and `ChosenProviso` (the inputs `matKF_of` uses on the headline path).

The goal is a Lean kernel verdict on this file against the actual project, plus `#print axioms`.

## Steps
1. Use the preserved original source with its prebuilt cache:
   `https://github.com/homeowmorphism/riemann-hypothesis-original` (Lean 4.33.1, frozen at upstream
   `ab0b7522`, same `src/` as Deicyde e50d098). Read `verification/CACHE.md` first and report the
   download size and free disk space before fetching. Then, in a fresh clone:
   ```
   lake exe cache get
   lake build --no-build
   ```
   If the cache is too large for this machine, stop and report the numbers; do not start a full build.
2. Copy `CommonPeriodMap.lean` into the clone root and run
   `lake env lean CommonPeriodMap.lean`. Record the full output, including the four `#print axioms`
   lines. Expected: no errors; each theorem depends only on `propext`, `Classical.choice`, `Quot.sound`.
3. If it fails to compile, fix only `CommonPeriodMap.lean` (names, namespaces, coercions), keeping every
   statement's meaning. Do not weaken a conclusion or add a hypothesis without saying so. Record each change.
4. Check the hypotheses are the real ones: confirm from source that on the headline path `LinkDIV`, `LinkS`
   and `ChosenProviso` are supplied for the family used by `linkCore` / `frameRealF_of''` /
   `matKF_of` (TopDensityNGeSixteen.lean:1348; LossesSmallShares.lean). Give file:line anchors.
5. Confirm what the experts flagged. Quote briefly (one short phrase each, with page) how Rubinstein v2
   states H8 and the object hypothesis O25, and how Zhang states Lemma 4.2 / Prop. 4.3, on whether the
   valuation (divisibility) estimate and the rank (near-orthogonality) estimate concern the same period
   maps. Say plainly whether `common_period_map` answers that question, partially answers it, or is
   about something else.

## Rules
- Do not modify the repository's own files. Labels: COMPILED only for what Lean accepted in this run.
- Report the exact Lean and Mathlib versions, the clone's commit hash, and the sha256 of the final
  `CommonPeriodMap.lean` you compiled.

## Output
Write `rh-extraction/common-period-map-check.md`: verdict first (compiled yes/no, axioms), then commands
and outputs, then any edits, then steps 4 and 5.

---

# Part B (after Part A passes): gap 2, what the period map is classically

Our end goal is a short human-readable account of the whole proof. Part A shows the divisibility
estimate and the rank estimate are both about one map, `D.s.Pu u`. Part B asks what that map is.

1. **Where it is built.** Find where the family members' datum `D : D7`, and its field
   `s : S.Draft.SData …`, are constructed on the headline path (start from `DesignExists` /
   `topDesWin`, DesWin.lean:11, and `ExistsFamPOfKits.lean`). Give the declaration that supplies
   `s.Pu`, `s.HH`, `s.Cu`, `s.volN`, `s.volH`, and file:line.
2. **What it is.** In plain words, then precisely: what space is `s.HH` (which automorphic forms, which
   group, which level), what is `s.Cu u`, and what does `s.Pu u` do (theta lift? orthogonal projection?
   period integral?). Is `c0 u = volN·volH/dimPi` the constant from the Rallis inner product formula?
3. **How LinkS is proved.** Trace the proof of `LinkS` (the near-identity Gram bound) on the headline
   path. Does it use `KExpansion` (RelevantZeroGramTerms.lean:345, a relative-trace expansion
   `Kmat = Σ aTerm`)? Which term is the identity, and what bounds the rest?
4. **Classical match.** Compare with Rubinstein v2 (S1–S4, O19–O21, O25, H8) and Zhang §§4.1–4.4:
   does their classical period map equal `s.Pu u` with the normalization `c0`? Mark MATCH /
   MISMATCH / UNDETERMINED for each item, and say exactly what would settle an UNDETERMINED one.

Same rules and labels as Part A. Write Part B to `rh-extraction/period-map-classical.md`.
