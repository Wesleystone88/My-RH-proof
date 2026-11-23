# Common-period-map check

**Compiled: no. Axioms: unmeasured for all four declarations.** The published cache exceeds the available space on both local volumes in their current formats. The proof file never reached Lean, so there is no compiler error or `#print axioms` output for it. **READ:** the headline argument supplies all three premises on one family. **DERIVED:** the proposed statement partially answers the experts’ common-map question. Part B was gated on a successful Part A kernel check.

## Commands and results

The cache guide specifies **175,187 archives, 4.94 GB of project downloads, plus a separate Mathlib download**, and about **105 GB of free space** with the storage layout used by the maintainers. It also identifies 175,187 published `.olean`/`.ilean` pairs. Download size and nominal free space were reported before the clone. A HEAD request to the project manifest returned HTTP 200 with `Content-Length: 12996051`. No project cache archives were fetched. [Pinned cache guide](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/verification/CACHE.md)

| Measured before fetching the checkout | Format | Bytes free | Bytes per allocation unit |
|---|---|---:|---:|
| C: | NTFS | 81,430,933,504 | 4,096 |
| D: | exFAT | 274,035,900,416 | 1,048,576 |

Free space came from `[IO.DriveInfo]::GetDrives()`; allocation units came from Windows `GetDiskFreeSpaceW` (sectors per cluster × bytes per sector, respectively 8 × 512 and 2048 × 512). Units were checked during checkout after D: consumed tens of GB for small files. **DERIVED:** the two output files per module already require at least `2 × 175187 × 1048576 = 367393767424` bytes on D:. Retaining one downloaded archive per module brings the lower bound to **551,090,651,136 bytes**. It still excludes the checkout, Mathlib, traces and C output. The original decision to use D: based on its nominal free space was corrected at this point.

```text
git ls-remote --symref https://github.com/homeowmorphism/riemann-hypothesis-original HEAD
ref: refs/heads/main    HEAD
4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e    HEAD

git -c core.autocrlf=false -c core.longpaths=true clone --depth 1 https://github.com/homeowmorphism/riemann-hypothesis-original D:\rh-common-period-check
Cloning into 'D:\rh-common-period-check'...
[last progress before the stop] Updating files: 16% (28708/175208)

git -c safe.directory=D:/rh-common-period-check -C D:/rh-common-period-check rev-parse HEAD HEAD:src
4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e
24df20b62d9976ccd20da819bc20b16f808f0fdd

Get-Content D:\rh-common-period-check\lean-toolchain
leanprover/lean4:v4.33.1

lean.exe --version  [existing pinned binary]
Lean (version 4.33.1, x86_64-w64-windows-gnu, commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6, Release)

lake-manifest.json -> packages[name=mathlib].rev
0df444a360eaa60ab8c11dca51a86af692955474
Get-FileHash D:\rh-common-period-check\lake-manifest.json -Algorithm SHA256
fee57ee9ed399d0a638ca955e5ad40a37a36eeb9b6dfd9f5964114fa7bbe4774

Get-FileHash rh-extraction\CommonPeriodMap.lean -Algorithm SHA256
573cd37bb2621d52be6e4f124eda0b35cb3565db1818d4b57aa2f004d5888410
```

The preserved clone's commit and source-tree IDs above were read from the fetched Git objects. All thirteen upstream files cited below were compared byte-for-byte with `git show HEAD:src/<path>`. The cache guide pins the build artifacts to upstream `e50d09817ad81469f737e8f637561e6ccf86c670` with this same source-tree ID. The workspace input hash matches the prompt. There is no compiled-file hash.

| Requested command | Output and status |
|---|---|
| `lake exe cache get` | Unrun. Disk-space stop condition. |
| `lake build --no-build` | Unrun. Cache unavailable. |
| `lake env lean CommonPeriodMap.lean` | Unrun. No stdout or stderr; no kernel verdict. |

The four requested checks were `RHX.besS_eq`, `RHX.KD_eq`, `RHX.common_period_map` and `RHX.common_period_map_family`. The prompt's expected set `{propext, Classical.choice, Quot.sound}` remains untested for each. No full build was started.

## Edits

No changes to `CommonPeriodMap.lean`, its hypotheses or its conclusions. The interrupted scratch checkout and its partial dependency copy were removed. The temporary elan registration was removed and the pre-existing Lean binary was retained.

## 4. The family in the headline argument

**READ.** In the preserved checkout, the constants in the call to `topDesWin` are `Cabs = 2`, `C0 = 3`, `eD = 2`, `eL = 0`. The parameter `CH` comes with the selected family.

| Pinned source location | What the term does |
|---|---|
| [`src/Development/AutomorphicArithmetic/CharacterBoxes/ShapeWin.lean:27`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/ShapeWin.lean#L27) | `UpperTheory.Top.shapeWin` obtains `hgl` at line 29, constructs the closed divisibility supplier `linkDIVt_closedK` at line 41, and design existence at lines 44–45. At lines 46–49 it applies `UpperTheory.Top.topDesWin` with that supplier, `GlobalTheory.Top.link_alt` for the Schur estimate, and `hgl.2` for the global step. |
| [`src/Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean:11`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean#L11) | At line 27 `topDesWin` chooses a single `Fm, CH` with witnesses `hCh, hT, hDG`. At lines 28–31 it evaluates the suppliers on this `Fm`, forms `hD := aD hT hDG aE (divinN_of_hypV …)`, and calls `aGL hT hDG hCh` with `⟨aG, aS hT, aI, hD, …⟩`. The second and fourth components of this tuple are `LinkS` and `LinkDIV` by [`src/Formalism/SharpRestriction/GlobalTheoremInputs.lean:158`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalTheoremInputs.lean#L158). |
| [`src/Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean:53`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean#L53) | `ChProviso_at` is the two-sided bound on `duS · GamL² / Dstar`. `ChosenProviso` at line 75 supplies it eventually for every index. See `ChosenE` at line 83 and the seven-condition packaging in [`src/Formalism/SharpRestriction/GlobalSchurBounds/WeightVectorSmallSharesSeven.lean:61`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/WeightVectorSmallSharesSeven.lean#L61)–65. |
| [`src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LinkGl.lean:25`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LinkGl.lean#L25) | `GlobalTheory.Top.link_gl` builds `hGLm` and uses `hGLm.link8` at lines 29–31. [`src/Formalism/SharpRestriction/GlobalSchurBounds/LogXLowerFamilyOfTheorems.lean:60`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/LogXLowerFamilyOfTheorems.lean#L60)–75 traces `FamGLmin.link8` through `link7` to `linkGLOBAL7_min`. In [`src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean:734`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L734) that theorem calls `linkGLOBAL7_items`. |
| [`src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean:693`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/LinkMin.lean#L693) | At lines 702–704 `linkGLOBAL7_items` extracts `cPr` from the chosen conditions and `lS, lD` from the theorem inputs. At lines 716–721 it uses `matKF_of … lS cPr lD` inside `frameRealF_of'' … lD lI lS cPr …`, and sends the resulting frame and `lD` to `linkCore`. Each call explicitly takes the same `Fm`. |
| [`src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean:1348`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1348) | `matKF_of` also assumes `0 < C0`. Lines 1350–1361 synchronize the thresholds, specialize all three witnesses at the same `x,i`, apply `hS hP`, and extract `BesselId (Fm.D x i)` from `lD`. Lines 1379–1381 use both Gram estimates and `blockReal_at_of _ hBes`. Lines 988–991 give the other inputs to `frameRealF_of''`, including `LinkIRR`, full lattice and rank hypotheses. |
| [`src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean:38`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalSchurBounds/LossesSmallShares.lean#L38) | `linkCore` takes a frame and `LinkDIV`. The parallel construction `linkGLOBAL7_pk` (lines 468, 483–485, 506–511) displays the same `matKF_of → frameRealF_of'' → linkCore` calls. The `LinkMin.lean` call above identifies which construction `link_gl` uses. |

**DERIVED.** The three premises of `RHX.common_period_map_family` are simultaneously available on the selected family. Its eventual quantifier is over the real scale `x` and every `i : Fm.Ix x`. Within one record the target isometry `V` serves every word, while `a ≠ 0` and `U` may depend on the word. The theorem gives no cross-scale identification of those witnesses.

## 5. Which part of the experts’ question does the lemma answer?

| Source and short quotation | What the comparison requires |
|---|---|
| Rubinstein v2, H8, p. 206, “One map, three sections.” | In the derivation of (III.330), the same map β_w must satisfy lattice inclusion (8a), height (8b) and an image-rank bound (8c). H8 explicitly assumes the identification when comparing the three sections. [H8, p. 206](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=206) |
| Rubinstein v2, O25, pp. 184–185, comment (e), “was not checked in the source”. | O25(c) takes the pairing after the chain and restriction. O25(e) inserts the target section and restricts to rational vectors. Comment (e) flags the identification of the §III.6 lattice pairing with the §III.8 algebraic pairing. [O25(e), p. 185](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf#page=185) |
| Zhang, Lemma 4.2, p. 43, “the part of the target missed by the restricted maps”. | Bounds on the individual Grams and on the weighted target operator bound the codimension of the span of the images of restricted subspaces. The lemma concerns complex maps and has no valuation hypothesis. [Lemma 4.2](https://www.ihes.fr/~rzhang/files/GRH%20note.pdf#page=43) |
| Zhang, Proposition 4.3, p. 44, “after choosing invertible coordinates”. | At one archimedean place the integral maps are assumed to be projections of the larger complex maps satisfying Lemma 4.2. The proposition uses this compatibility together with integrality, heights, ranks and the slope bounds. [Proposition 4.3](https://www.ihes.fr/~rzhang/files/GRH%20note.pdf#page=44) |

**DERIVED — partially answers.** The integral map is `D.div.Bk u`. Its lattice inclusion is `OneMapIntoCC` in [`src/Formalism/LocalRingCardinality/DataArith.lean:180`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/DataArith.lean#L180). After the field embedding, its values agree on rational inputs with a nonzero multiple of matrix coefficients of `D.s.Pu u`, with the changes of variables specified above. The definition of `besS` gives the coefficient and `BuRational` gives the rational comparison in [`src/Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean:353`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L353) and line 364. The diagonal bound measures the squared Hilbert–Schmidt norm of the normalized Gram minus the identity on `D.s.Cu u`. The exact normalization and adjoint composition are in [`src/Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean:337`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L337)–343 and line 509. This relates two differently typed maps by an explicit coefficient identity.

The proposed conclusion retains the diagonal bound. The stronger `LinkDIV_at` premise already bounds the height of the same nonzero `Bk u` ([`src/Formalism/SharpRestriction/GlobalTheoremInputs.lean:77`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SharpRestriction/GlobalTheoremInputs.lean#L77)–81), and `LinkS_at` includes the off-diagonal and dimension bounds (lines 142–148). The four declarations do not derive a rank bound for projected subspaces, a mean-slope inequality, or an identification of the experts’ explicitly described classical chain, lattices, norms and projection. Those further claims require their own mathematical arguments.
