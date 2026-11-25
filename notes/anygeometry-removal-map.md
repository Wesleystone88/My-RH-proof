# Where `anyGeometry` enters, who reads it, and what removing it would take

**DERIVED.** In the pinned source, `anyGeometry` is used only as an argument that fills the `Γ : GeoP` slot of the parameter record `Prm`, and from there it becomes the `geo` field of the structure `OAt`. I found **no proof that reads that field** to get a property out of it. It is built (`geo := trivial`), moved from stage to stage (`GeoCl.step`), wrapped (`geoCl_of`) and stored again. The *other* field of the same structure, `lam`, **is** read, so the slot `OX` as a whole is not removable, only its `geo` field. On this reading, deleting that field is possible in principle. It has not been tried, because testing it means rebuilding the **5,690** modules that import `OverIx.lean` (5,691 with `OverIx` itself, 3.2% of the project). This note extends [`anygeometry-footprint.md`](anygeometry-footprint.md) and does not redo it.

Source: `homeowmorphism/riemann-hypothesis-original` at `4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e` (src tree = upstream `e50d098`). Reading only: I streamed GitHub's archive of that commit and scanned all **175,188** `.lean` files under `src/`. No Lean was run, nothing was built, and `C:\rhc` was not touched. Labels: **READ** (quoted from a file), **DERIVED** (our reasoning), **GUESS**.

**Limits, up front.** Everything below is textual. A text search has no type information, so "no reader found" means no reader of the kinds listed in §2 was found, not a kernel-checked proof of absence. The checkable version is in §5.

## 1. Every occurrence

**READ.** A whole-identifier scan finds **118 lines in 24 files** (162 matches, since many lines contain it twice), in **30 enclosing declarations** including the definition. This matches the critics' count and Codex's 24 files and 30 declarations. The file list is in the footprint note and the per-declaration table is below.

| Kind | Matches |
|---|---|
| (a) definition: `def anyGeometry : GeoP := fun _ _ _ => True` ([OverIx.lean:19][ox19]) | 1 |
| (b) passed as a `GeoP` argument, inside `geoCl anyGeometry` | 151 |
| (b) passed as a `GeoP` argument, bare | 10 |
| (c) of the 161 arguments, those in a declaration's statement (before `:=`) | 87 |
| (c) of the 161 arguments, those in a proof or definition body | 74 |
| (d) other | 0 |

The ten bare arguments: `OX anyGeometry` (3: [TupPinsOfMuIsW.lean:204, 212][tp204], [PublishedInputsImplyConclusion.lean:41][pic39]), `OAt anyGeometry` (1: [NotLamAreShift.lean:153][nls153]), and the lemma calls `movable_geometric … anyGeometry` (2), `movable_pin … anyGeometry` (1), `slot_mv_extension_with_{origin,list}_geo_cl … anyGeometry` (3).

**READ.** Per declaration (file:line of the declaration, matches in statement / body):

| Declaration | Matches |
|---|---|
| `anyGeometry` [OverIx:19][ox19] | def |
| `prmA` [GKeyFin:21][gkf21], `prm1` [MultW:44][mw44], `prm0` [ParMem:137][pm137] | body 1 each |
| `oAt_any` [NotLamAreShift:152][nls153] | stmt 1 |
| `member_bundles_large_ue` ([LinkedBundleConstructionExists.lean:25][lbce]) + its `…Statement` | 4+2, 4+0 |
| `nonempty_hyps_of_classicalTheoremsUE` ([NonemptyHypsOfPublishedUE:30][nhpue]) | 2+2 |
| `open_of_hypothesesUE` ([OpenFirstParametersOfPublishedUE:26][ofpue]) | 0+12 |
| `main` ([LinkOfClosedAtFamily:68][locaf]) | 0+3 |
| `memberE_exBL_of_pair` ([MemberBuiltLinkedGeometric:40][mblg]), `memberE_exBL_prm1` (:62), `…Statement` | 11+3, 5+4, 5+0 |
| `divEx_geoCl` ([PublishedInputsImplyConclusion:39][pic39]), `memberE_closing` (:74), `…Statement` | 1+1, 7+5, 7+0 |
| `divEx_prov` ([TupPinsOfMuIsW:204][tp204]), `divEx_of_ox` (:211) | stmt 1 each |
| `hypsE₂` ([EveryCharacterE:41][ece41]) | 0+3 |
| `exists_baseLattice_of_pair_alt`, `…_of_prime_alt`, `member_exists_baseLattice_alt` ([ExistsBaseLatticeOfPrime:36, 57, 80][eblp]) | 11+3, 5+4, 5+0 |
| `hypotheses_nonempty_of_unramified_exponents_alt` ([HypothesesNonemptyOfUnramifiedExponents:41][hnoue]) | 2+2 |
| `final_of_alt` ([LinkNFam:75][lnf]) | 0+4 |
| `member_bundles_large_unramified_exponents_alt` (+ `…exist_alt`) ([MemberBundlesLargeUnramifiedExponents:34, 69][mblue]) | 4+2, 4+0 |
| `memberE_closing_alt_alt` ([MemberEClosing:17][mec]) | 7+5 |
| `open_orbit_of_unramified_exponents_alt` ([OpenOrbitOfUnramifiedExponents:39][ooue]) | 0+12 |
| `parametersOfDependence` ([Prm1:20][prm1f]) | 0+1 |
| `nonempty_hyps_definite_side_of_closed_bound` ([SiegelEisensteinSecondTermHypotheses:44][sets44]) | 0+3 |

**READ, dead code.** I counted the names over all 175,188 files: `prmA`, `prm0`, `oAt_any` and `oAt_geoOf` each occur **once**, at their own declaration, so none is referenced anywhere (this agrees with Codex). `prm1` occurs 9 times, `divEx_geoCl` 5 times (including `memberE_closing` and `memberE_closing_alt_alt`) and `divEx_prov` twice.

## 2. Who builds the certificate, who reads it

### 2.1 The slot, from definition to use (READ)

- `abbrev GeoP := ∀ D, Core D → DivX D → Prop` ([OverIx.lean:14][ox19]). `geoOf Q` is the real geometry (`∃ c > 0, IsGeoOf (Q D) J c X` and `HasTrueSurf X`, :16-17). `anyGeometry` is `True` for every triple (:19).
- `structure OAt (Γ : GeoP) … : Type 1 where geo : Γ … X ; lam : LamAre t.r.Z X` ([OverIx.lean:44-47][ox44]), and `def OX (Γ) : OComponent₂ := fun … => OAt Γ t O.X` (:49).
- `structure Prm hL where R N S Γ` with `Γ : GeoP` ([ThetaChr.lean:26-30][tc26]); `prmR N S Γ := ⟨RX, N, S, Γ⟩` ([:117][tc26]); `Prm.s p := ⟨p.R, NX hL p.N, SXE p.S, OX p.Γ⟩` ([:34][tc26]). **This is the slot every `geoCl anyGeometry` argument fills.**
- `structure Slots` has four components `Rx, Nx, Sx, Ox` ([NonzeroPlacesOverPrimes.lean:118-122][npop118]). The stage structures `Lv2/Lv3/Lv4/Built` hold a field `ox : 𝒮.Ox …` ([:167][npop118]).
- `DivEx 𝒮 : Prop` asks, for every stage, for a `DivX` `Y` with `Nonempty (DivT …)` and `… → Nonempty (𝒮.Ox … O t)` ([:183][npop118]): it needs only that an `Ox` value **exists**.
- `inductive GeoCl (Γ) : … → Prop` with `base : Γ D J X → GeoCl Γ D J X` and `step N h : GeoCl Γ D J X → GeoCl Γ (setDiv D N h) (coreS N h J) (divTr N h X)`; `geoCl Γ := GeoCl Γ`; `geoCl_of h := GeoCl.base h` ([NotGeoClFalse.lean:21-28][ngcf21]). **DERIVED:** `GeoCl` exists to make a `GeoP` closed under the stage move `setDiv`, so the transfer theorem below works for an arbitrary `Γ`. For `Γ = anyGeometry` the closure adds nothing.

### 2.2 Constructors (READ)

| Where | What it builds |
|---|---|
| `divEx_prov` ([TupPinsOfMuIsW.lean:204-209][tp204]) | `⟨⟨trivial, lamAre_heq …⟩⟩ : OAt anyGeometry …`, so `geo := trivial` |
| `oAt_any` ([NotLamAreShift.lean:152-155][nls153]) | the same, `⟨_, ⟨trivial, lamAre_set …⟩⟩`; unreferenced |
| `oAt_geoOf` ([NotLamAreShift.lean:157-164][nls153]) | the variant for the real geometry: `⟨geoOf_set hc hX _, lamAre_set …⟩`; **unreferenced** (one occurrence in the corpus). So no `OAt (geoOf Q)` is ever built by the proof. |
| `divEx_geoCl` ([PublishedInputsImplyConclusion.lean:39-49][pic39]) | `⟨⟨geoCl_of o.geo, o.lam⟩⟩`: takes an `OAt anyGeometry`, **reads `o.geo` and re-wraps it** with `GeoCl.base` (see 2.3) |
| `oAt_setDiv` ([DivisionGeometryScalarsTransferSetDivision.lean:71-107][dgs105]) | `⟨⟨GeoCl.step N h hp.geo, lamAre_copy … hp.lam⟩⟩`: moves an `OAt (geoCl Γ)` along `setDiv` |
| `exists_divT` ([TupPinsOfMuIsW.lean:178-189][tp204]) | the **other** geometry slot: `geo := hG : GeoTiedP …` from `geoOver_stages` (§2.5) |

### 2.3 Readers of the `geo` component (READ, then DERIVED)

I looked for every place a value of type `OAt …` or `GeoCl …` is eliminated: projections `.geo` / `.1` / `.ox`, `cases`/`induction`/`match`/`rcases`/`obtain` on it, `GeoCl.rec`/`casesOn`.

| Site | What it does with the value | Real or pass-through |
|---|---|---|
| `oAt_setDiv` ([DGS:106][dgs105]) | `GeoCl.step … hp.geo`: `hp.geo` goes straight into a constructor | **pass-through** |
| `divEx_geoCl` ([PIC:49][pic39]) | `geoCl_of o.geo`: `o.geo` goes straight into `GeoCl.base` | **pass-through** |
| `{ b with nx := … }` in `goodE_of_builtE` ([PIC:60][pic39]) | structure update that copies the `ox` field | pass-through |
| the four call sites that pass `x.ox` to `divisionGeometryScalars_transfer_setDivision` and store the result: [SlotMvPin:33][smp33], [SlotMvPrmRNel:35][smn35], [PositionStageMovesGeometric:53][psmg53], [LinkOfClosedAtFamily:61][locaf61] | `obtain ⟨o⟩ := … x.ox; exact ⟨…, ⟨o⟩⟩` (shown in full for SlotMvPin; the others have the same line) | **pass-through** |
| `obtain ⟨⟩` of the whole stage record with `ox` named, in [ExistsKerTie:21][ekt21], [ExtraTiedCol:16][etc16], [ZetaUniformOfExtension:70][zue70], [ZeUPrmRNEb:33][zeu33] | binds `ox`; **the name is not used afterwards** in any of the four (checked: no later use within 60 lines, or elsewhere in the file) | unused |
| constructors that store an `ox`: [WitnessesPassAlongSetDivision:34, 67][wpas34], [ExistsConstructedCoreOfAllConstructionStages:83, 125][ecc83], [MemNonzeroPlacesOfResidueChar:150][mnpr150] (`ox := PUnit.unit` for a trivial slot) | `obtain ⟨ox⟩ := …; … ox := ox` | pass-through |

**READ, the `lam` field is different.** [ParameterOfDiscreteSeriesRay.lean (IwasawaDecomposition):107][podsr107] and [(ThirdPlaceSeries):72][podsr72] pass `q.x.ox.lam` as the hypothesis of a `logLam` argument (`(hHost …).1 q.O.X q.x.ox.lam`). That is a **real** reader: `LamAre` is used for its content. This is why the slot `OX` is not removable, only its `geo` field.

**DERIVED.** Real readers of `OAt.geo`: **0**. Pass-through projections: **2** (`hp.geo`, `o.geo`).

### 2.4 Nielsen's claims, directly

- **"No proof does case analysis or induction on `GeoCl`."** **READ:** `GeoCl` occurs 7 times in 2 files and `geoCl` 163 times in 29 files. Every occurrence is a declaration, a constructor (`GeoCl.base` in `geoCl_of`, `GeoCl.step` in `oAt_setDiv`) or an argument. There is no `GeoCl.rec`, `casesOn`, `induction` or `cases` naming it. **DERIVED:** values of type `GeoCl …` only reach a proof through `OAt.geo` (§2.3), whose two projections are the pass-throughs above. **Confirmed**, with the limits stated at the top.
- **"`GeoTiedP.geoTied`, `GeoTiedP.formsTieX`, `geoOf_surf` are never called."** **READ:** `geoTied`, `formsTieX` and `geoOf_surf` each occur **exactly once in all 175,188 files**, at their own declaration ([GeoTiedP.lean:136, 140][gtp124], [NotLamAreShift.lean:29][nls153]). Dot-notation calls would count as occurrences, so none exists. `GeoTiedPL` (the variant) occurs twice: its definition and `GeoTiedPL.geoTiedP` ([GeoTiedP.lean:130, 146][gtp124]), also never used. **Confirmed.**

### 2.5 A second, different geometry slot: `GeoTiedP` (READ)

`DivT.geo : GeoTiedP Y inK` ([TiedColumnData.lean:126-133][tcd126]), and the same field in `ClassS` and `LinkedFamiliesFixedValues`, is **not** `anyGeometry` and is not trivial. `GeoTiedP X inK` is an existential over a Shimura family `F`, place and component equivalences, `TiedX`, `CuspTieX`, `IsoInv`, `LevInTie` ([GeoTiedP.lean:124-128][gtp124]). It is constructed for real by `geoOver_stages` ([TupPinsOfMuIsW.lean:155-167][tp204]; family `famFlJ`, `tiedX_fl`) with the trivial parts `inK := fun _ _ => True` and `Q := fun _ => True`, and `geoTiedP_satisfiable` ([GeoTiedP.lean:179][gtp124]). It is carried across stages by `geoTiedP_divTr` ([DivisionLocalDataPreservedDivisionLatticeChange.lean:122][dldp122]), which does destructure it and rebuild the tied data for the moved stage, used in `divT_setDiv` ([:148-150][dldp122]). **DERIVED:** this is a transport that produces another `GeoTiedP` certificate; no consumer extracts a property (`geoTied`, `formsTieX` are never called). The pin `geo : HEq S.geo q.x.div.geo` in `SPin` ([ThetaChr.lean:59][tc26]) is an equality of proofs of a `Prop`. This slot is outside the `anyGeometry` question but would be the next thing to examine.

## 3. The replacement, per use

| Use | Verdict |
|---|---|
| the definition `anyGeometry`; `geoCl anyGeometry` / `anyGeometry` as the `Γ` argument at all 161 argument sites (§1) | **delete** (never read): the value filling `Γ` only ever feeds `OAt.geo` |
| `OAt.geo` (constructed in `divEx_prov`, `oAt_any`, moved in `oAt_setDiv`, wrapped in `divEx_geoCl`) | **delete** (never read), by §2.3 |
| `GeoCl`, `geoCl`, `geoCl_of`, `NotGeoClFalse.lean` | **delete** once `OAt.geo` is gone: they exist only to type that field |
| `OAt.lam` and the slot `OX` | **keep**: `lam` is read ([podsr107][podsr107], [podsr72][podsr72]) |
| `DivT.geo : GeoTiedP` | **keep / separate question** (§2.5) |

**DERIVED.** Every use of `anyGeometry` and `GeoCl` is "delete (never read)". The *slot* is removable in principle; "removable" here means by the textual evidence of §2, not machine-checked.

## 4. How big a rebuild would be

**READ, computed from the `import` lines of all 175,188 files.**

| Question | Count |
|---|---|
| modules that transitively import `OverIx.lean` | **5,690** (+1 for `OverIx` itself = 5,691, 3.2% of 175,188) |
| of those, direct importers | 4: `NotGeoClFalse`, `NotLamAreShift`, `ThetaChr`, `TupPinsOfMuIsW` |
| modules that transitively import `EveryCharacterE.lean` | **11** (+1), direct importers: `TemperedProductOfSquareIntegrable`, `EveryCharacterOfLiteratureOfVWin`, `SiegelEisensteinSecondTermHypotheses`; **all 11 are also among the 5,690**, since `EveryCharacterE` itself imports `OverIx` |
| union of the two | 5,690 |
| import closure of `src/Main.lean` | **175,187 of 175,188** modules: `Main` reaches everything except `Challenge.lean`, via the aggregator `Supplements.Kernels.MainTheoremsAll` |
| so: of the 5,690, in `Main`'s import closure | **5,690 (all)** |
| shortest import path `Main → OverIx` | 9 modules, through `MainConclusion → RiemannHypothesisOfEveryCharacter → WeightSetSaturatedOfHypsStatement → NotGeoClFalse → OverIx` |
| for context: modules importing `NotGeoClFalse` | 4,445; importing `GeoTiedP` | 11,383 |

**DERIVED.** Because `Main`'s closure is almost everything, "in `Main`'s closure" does not narrow the count; the 5,690 is the number to compare. It is a count of *imports*, not of what `riemannHypothesis` actually depends on. **GUESS:** at the 4 to 5 modules per minute seen in this project's own builds, 5,691 modules is of the order of a day on a laptop; modules vary a lot in cost.

## 5. A patch sketch, not applied

No `.lean` file was edited. Two tiers.

**Tier 1, the test: drop only the `geo` field of `OAt`.** It leaves `Γ`, `GeoP`, `geoCl` and all 161 argument sites type-correct, because `Γ` becomes an unused parameter. Edits:
1. [OverIx.lean:44-47][ox44]: delete the line `geo : Γ … X`. `OAt Γ t X` is then the single field `lam`.
2. [TupPinsOfMuIsW.lean:209][tp204]: `⟨⟨trivial, lamAre_heq …⟩⟩` becomes `⟨⟨lamAre_heq …⟩⟩`.
3. [NotLamAreShift.lean:155][nls153] (`oAt_any`) and [:164][nls153] (`oAt_geoOf`): drop the first component (`trivial`; `geoOf_set hc hX _`). Both theorems are themselves unreferenced, so they could simply be deleted instead; `geoOf_set` and `isGeoOf_set` are used only in this file, and `geoOf_surf` nowhere.
4. [DivisionGeometryScalarsTransferSetDivision.lean:105-106][dgs105]: `refine ⟨⟨?_, ?_⟩⟩` becomes `⟨⟨?_⟩⟩` and the `GeoCl.step` bullet is deleted.
5. [PublishedInputsImplyConclusion.lean:49][pic39] (`divEx_geoCl`): becomes `exact ⟨⟨o.lam⟩⟩`.

A successful rebuild of `OverIx` and its 5,690 importers would show that no proof reads `OAt.geo`, which is the claim this note could only argue from text.

**Tier 2, the cleanup, if Tier 1 builds:** remove the `Γ : GeoP` field from `Prm` and `prmR`/`parametersOfExtension`, the `(Γ : GeoP)` parameter from the statements that carry it (`movable_geometric`, `movable_pin`, `slot_mv_extension_with_{origin,list}_geo_cl`, `divisionGeometryScalars_transfer_setDivision`, `goodE_of_builtE`), delete `NotGeoClFalse.lean` and `anyGeometry`, and drop the third argument at the 151 `geoCl anyGeometry` sites in the 24 files of §1.

## 6. What this does not establish

- Tier 1 has not been built. The reader search is textual; a reader that destructures an `OAt` with anonymous constructor notation under a name other than `ox`, or that uses a projection under another field name, would not appear in §2.3 and would be caught only by the kernel-side check.
- **The checkable version, for later (needs `OverIx` and the 5,690 built, so not done without asking):** extend `results/anygeometry-check/DependsOn.lean` to walk every constant of the project's proof terms for `Expr.proj` nodes and applications of `OAt.geo`, `OAt.rec`/`casesOn` and `GeoCl.rec`/`casesOn`. Zero hits would settle §2.3 in the kernel's terms.
- Whether removing `geo` would let the *whole* proof still build is exactly Tier 1, not shown here.
- I did not read the full proofs of the 24 files. The four `x.ox` pass-through sites were read in full for `SlotMvPin` and identified by the identical call line in the other three.

*Written by Claude Code (reading task, 24 Nov 2026) from `prompts/claude-code-prompt-2026-11-24c.md`, which Claude in chat wrote.*

[ox19]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L14-L19
[ox44]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L44-L49
[ngcf21]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotGeoClFalse.lean#L21-L28
[tc26]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ThetaChr.lean#L26-L34
[npop118]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NonzeroPlacesOverPrimes.lean#L118-L122
[tp204]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L204-L209
[pic39]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PublishedInputsImplyConclusion.lean#L39-L49
[nls153]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotLamAreShift.lean#L152-L164
[dgs105]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/DivisionGeometryScalarsTransferSetDivision.lean#L105-L107
[gtp124]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/LatticeGeometry/GeoTiedP.lean#L124-L146
[tcd126]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TiedColumnData.lean#L126-L133
[dldp122]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/DivisionLocalDataPreservedDivisionLatticeChange.lean#L122-L150
[smp33]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SlotMvPin.lean#L33-L34
[smn35]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SlotMvPrmRNel.lean#L35
[psmg53]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PositionStageMovesGeometric.lean#L53
[locaf61]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LinkOfClosedAtFamily.lean#L61
[ekt21]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsKerTie.lean#L21
[etc16]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExtraTiedCol.lean#L16
[zue70]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ZetaUniformOfExtension.lean#L70
[zeu33]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ZeUPrmRNEb.lean#L33
[wpas34]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/WitnessesPassAlongSetDivision.lean#L34-L67
[ecc83]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsConstructedCoreOfAllConstructionStages.lean#L83-L125
[mnpr150]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/MemNonzeroPlacesOfResidueChar.lean#L150
[podsr107]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ParameterOfDiscreteSeriesRay.lean#L107
[podsr72]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ParameterOfDiscreteSeriesRay.lean#L72
[gkf21]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/GKeyFin.lean#L21-L22
[mw44]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/MultW.lean#L44-L45
[pm137]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ParMem.lean#L137
[lbce]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LinkedBundleConstructionExists.lean#L25
[nhpue]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/NonemptyHypsOfPublishedUE.lean#L30
[ofpue]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/OpenFirstParametersOfPublishedUE.lean#L26
[locaf]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LinkOfClosedAtFamily.lean#L68
[mblg]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/MemberBuiltLinkedGeometric.lean#L40
[ece41]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/EveryCharacterE.lean#L41
[eblp]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L36
[hnoue]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L41
[lnf]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L75
[mblue]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean#L34
[mec]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberEClosing.lean#L17
[ooue]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean#L39
[prm1f]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Prm1.lean#L20
[sets44]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L44
