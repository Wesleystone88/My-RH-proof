import Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen

/-!
# Rubinstein H8: the mean-slope inequality (III.330), through `frame_at_of`

Rubinstein v2, H8 (p. 206): there are `η_u, e_u ≥ 0` with `(η_u + 4√e_u) x^{C_H} ≤ 6` such that for every
`R > 0` with `s_u − μ_CC^min ≤ R`,
`μ_CC ≥ s_u − log|W_u| − (1/(1−δ_p)) (4 sp_u log(1 + R/sp_u) + (η_u + 4√e_u) R)`.

READ. The source states this as `Frame_at` (QuadraticLogDerivCongr.lean:188–193) and, over a family with the
constant bound, `FrameF Fm CH` (QuadraticLogDerivCongr.lean:258–260). The conclusion below is `FrameF Fm CH`.

NOT PICKED OUT. No premise below contains `Frame_at`, `FrameReal_at`, `FrameF` or `FrameRealF`. The
conclusion comes through the source's family-level theorem `frameF_of` (TopDensityNGeSixteen.lean:606),
whose proof calls `frame_at_of` (:538, called at :645) with the witnesses `η = 5·x^{−C_H} + 3·√de`, and the
`FrameRealF` it needs is built by `frameRealF_of''` (:988) from `MatKF`, which comes from `matKF_of`
(:1348) applied to `LinkS`, `ChosenProviso` and `LinkDIV`. `LatF` comes from `latF`
(QuadraticLogDerivCongr.lean:1338) with `rrRankF_of` (:1424). This is the route of the source's own
`linkGLOBAL7_items` (LinkMin.lean:706–717).

DERIVED. In the statement, `FrameF` fixes `etaB, eB` with `(etaB + 4√eB)·x^{C_H} ≤ 6` and `Frame_at` gives
`η ≤ etaB`, `e ≤ eB`. The proof of `frameF_of` chooses `etaB = 5·x^{−C_H} + 3·√de`; inside `frame_at_of`
the values are `η = 5·sg + 3·√de` and `e = 2·e0` (with `sg = x^{−C_H}`). Those are Rubinstein's constants, but
the statement of `FrameF` exposes only the bounds, so this file states only what `FrameF` states.

Premises, and where the headline route supplies them (READ, source at `4e8bb36`; paths under
`src/Formalism/` unless noted):
* `lD : LinkDIV`, `lS : LinkS`, `lI : LinkIRR`: conjuncts of `GlobalTheoremInputs`
  (SharpRestriction/GlobalTheoremInputs.lean:158–160); in `linkGLOBAL7_items` they come from `hIn`
  (SharpRestriction/GlobalSchurBounds/LinkMin.lean:704).
* `cPr : ChosenProviso`, `cCo : ChosenCode`: fields of `Chosen` (GlobalSchurBounds/Chosen.lean:75, 77),
  from `hCh : ChosenE` (Chosen.lean:83; LinkMin.lean:703).
* `hTu : TuSize Fm`: `linkGLOBAL7_items` ASSUMES it as a hypothesis (LinkMin.lean:701-702); it has no
  local proof there. Outside `LinkMin`, the selected-family row `row_hTu_cTmin_alt`
  (ThetaPairLifts/ThirdPlaceSeries/RowHTuCTmin.lean:11, 19) invokes `tuSize_min`
  (SharpRestriction/ParamsHeightRankConstant.lean:180).
* `hNF : NuFullF`: `nuCommensF_min` (LinkMin.lean:652, call at :707) then `nuFullF_of` (call at :708;
  built in TopDensityNGeSixteen.lean:1651). A derivation from the level data `hE : J.LvlF`.
* `hRk : J.MuRank`: `muRank_min` (LinkMin.lean:665, call at :709). It needs the chosen proviso `cPr` in
  addition to `hNF`, `hE`, `tSet` and `C0 > 0`. A derivation.
* `hRam : RamRankF`: the inline call is LinkMin.lean:718 (`ramRankF_min`, defined at :659). It is a valid
  proof by projection and cast of the rank identity carried by `hE`; the estimate controlling the
  ramified share is proved separately by `ramShare_at_of`.
  `hE` and `tSet` come from `lvlF_of` (LinkMin.lean:638, call at :706) and `settingF_of` (call at :705)
  applied to `hTu`, `hT2`, `hT5`. These builders live in several files; `LinkMin.lean` is outside the
  705-module closure, so this file takes their results as premises instead of rebuilding them.
  (Correction of an earlier version of this comment, following notes/h8-frame-check.md section 4.)
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h8_frame {eps : ℝ} (Fm : FamP eps) {Cabs CH C0 : ℝ} (hCH : 0 < CH) (hC0 : 1 ≤ C0)
    (lD : LinkDIV Fm Cabs CH) (lS : LinkS Fm C0) (lI : LinkIRR Fm)
    (cPr : ChosenProviso Fm C0) (cCo : ChosenCode Fm C0 CH)
    (hNF : NuFullF Fm) (hRk : J.MuRank Fm) (hTu : TuSize Fm) (hRam : Lnk.RamRankF Fm) :
    Lnk.FrameF Fm CH :=
  Lnk.frameF_of Fm CH C0 hCH hC0
    (Lnk.frameRealF_of'' Fm Cabs CH C0 hCH.le lD lI lS cPr hNF hRk hTu hRam
      (Lnk.matKF_of Fm Cabs CH C0 (by linarith) lS cPr lD))
    (Lnk.latF Fm lD hNF hRk (Lnk.rrRankF_of Fm Cabs CH C0 (by linarith) lS cPr lI lD))
    cPr cCo hNF

end RHX

end

#print axioms RHX.h8_frame
