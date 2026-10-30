---
title: 'Module: csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenCtcLossTensor: AtenCtcLossTensor(a509372b86b9cc55).
  AtenCtcLossBackwardTensor: AtenCtcLossBackwardTensor(1efe5649eef27670).
  AtenCtcLossAutograd.backward: AtenCtcLossAutograd#backward(305625f81d7e100).
  AtenCtcLossTensorAutograd.backward: AtenCtcLossTensorAutograd#backward(305625f81d7e100).
  AtenCtcLossAutograd.forward: AtenCtcLossAutograd#forward(248935cd6a40eb28).
  AtenCtcLossTensorAutograd.forward: AtenCtcLossTensorAutograd#forward(665a6f9fd97d1988).
  AtenCtcLossPublic: AtenCtcLossPublic(49d12d60ad0979b0).
  AtenCtcLossBackward: AtenCtcLossBackward(941eb9bcd0011bfe).
  AtenCtcLoss: AtenCtcLoss(9e46d45cad969b60).
  AtenCtcLossPublicTensor: AtenCtcLossPublicTensor(e8bfdc775484bcb8).
  BuildCtcLossShlo: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/BuildCtcLossShlo(969c7bc0dba9f04).'
  CtcLossPublicInternal: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossPublicInternal(5e6700c0d0b0fddb).'
  CtcLossForwardInternal: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossForwardInternal(d85e3bfd2e8ebbfc).'
  CtcLossBackwardInternal: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossBackwardInternal(7ebc3ce62b3b58b1).'
  BuildCtcLossBackwardShlo: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/BuildCtcLossBackwardShlo(4ad971cb8ef205f7).'
  GetMaxTargetLength: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/GetMaxTargetLength(20d0afaae46a230e).'
  ValidateLogProbsDtype: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/ValidateLogProbsDtype(45982de3b0bc1087).'
  BuildCtcLossPublicShlo: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/BuildCtcLossPublicShlo(c6db7dee9a96e0ac).'
  BuildCtcLossPublicBackwardShlo: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/BuildCtcLossPublicBackwardShlo(2bf86689197d385d).'
  ComputeFinalLoss: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/ComputeFinalLoss(101c10845427f751).'
  InitializeCtcLoss: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/InitializeCtcLoss(36027d5fd4dd3b39).'
  Unpack1DTargetsTo2DShlo: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/Unpack1DTargetsTo2DShlo(665145f2399197cc).'
  ComputeInitialMaskAndAlpha: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/ComputeInitialMaskAndAlpha(bc76e213d7e96b5e).'
  BuildCtcLossPublicInferenceShlo: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/BuildCtcLossPublicInferenceShlo(ccc3a20b48fa79b4).'
  CreateTargetsWithBlanks: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CreateTargetsWithBlanks(ea92d3bab0d552d7).'
  CreateGatherIndices: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CreateGatherIndices(665145f2399197cc).'
  LoopBodyLogic: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/LoopBodyLogic(e4351a09cac1aee2).'
  ZeroInfinity: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/ZeroInfinity#'
  BackwardLoopBodyLogic: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/BackwardLoopBodyLogic(35a52ad4f909ce5d).'
  AtenCtcLossPublicAutograd: AtenCtcLossPublicAutograd(49d12d60ad0979b0).
  ReduceAddDim2: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/ReduceAddDim2(c9a7fac082e0cfdd).'
  AtenCtcLossPublicTensorAutograd: AtenCtcLossPublicTensorAutograd(e8bfdc775484bcb8).
  ZeroInfinity.kYes: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/ZeroInfinity#kYes.'
  CtcLossInitResult.C: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#C.'
  MaskAndAlphaResult.alpha_0: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/MaskAndAlphaResult#alpha_0.'
  GetGatherDimensionNumbers: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/GetGatherDimensionNumbers(9a1e7efebf815e52).'
  CtcLossInitResult.batch_seq: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#batch_seq.'
  LogSumExp: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/LogSumExp(b311a7ecf754858b).'
  ZeroInfinity.kNo: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/ZeroInfinity#kNo.'
  MaskAndAlphaResult: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/MaskAndAlphaResult#'
  CtcLossInitResult.neg_inf_const: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#neg_inf_const.'
  CtcLossInitResult.mask_M: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#mask_M.'
  CtcLossInitResult.gather_indices: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#gather_indices.'
  CtcLossInitResult: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#'
  MaskAndAlphaResult.mask_M: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/MaskAndAlphaResult#mask_M.'
  CtcLossInitResult.alpha_0: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#alpha_0.'
  CtcLossInitResult.type_nl_probs: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#type_nl_probs.'
  CtcLossInitResult.L: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#L.'
  CtcLossInitResult.T: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#T.'
  CtcLossInitResult.N: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#N.'
  CtcLossInitResult.S: '`$anonymous_namespace_csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`/CtcLossInitResult#S.'
---
# Module: [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc)

## Classes
### <a id="CtcLossInitResult"></a>`CtcLossInitResult`
- def: [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc:372`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L372)
- signature: `struct CtcLossInitResult`
- members:
  - <a id="CtcLossInitResult.C"></a>`C` — [`L383`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L383)
  - <a id="CtcLossInitResult.L"></a>`L` — [`L381`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L381)
  - <a id="CtcLossInitResult.N"></a>`N` — [`L379`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L379)
  - <a id="CtcLossInitResult.S"></a>`S` — [`L380`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L380)
  - <a id="CtcLossInitResult.T"></a>`T` — [`L382`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L382)
  - <a id="CtcLossInitResult.alpha_0"></a>`alpha_0` — [`L373`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L373)
  - <a id="CtcLossInitResult.batch_seq"></a>`batch_seq` — [`L377`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L377)
  - <a id="CtcLossInitResult.gather_indices"></a>`gather_indices` — [`L375`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L375)
  - <a id="CtcLossInitResult.mask_M"></a>`mask_M` — [`L374`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L374)
  - <a id="CtcLossInitResult.neg_inf_const"></a>`neg_inf_const` — [`L376`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L376)
  - <a id="CtcLossInitResult.type_nl_probs"></a>`type_nl_probs` — [`L378`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L378)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildCtcLossShlo`](ctc_loss_aten_kernels.cc.md#BuildCtcLossShlo), [`BuildCtcLossBackwardShlo`](ctc_loss_aten_kernels.cc.md#BuildCtcLossBackwardShlo), [`InitializeCtcLoss`](ctc_loss_aten_kernels.cc.md#InitializeCtcLoss)

### <a id="MaskAndAlphaResult"></a>`MaskAndAlphaResult`
- def: [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc:282`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L282)
- signature: `struct MaskAndAlphaResult`
- members:
  - <a id="MaskAndAlphaResult.alpha_0"></a>`alpha_0` — [`L284`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L284) — Initial DP state probabilities at t=0.
  - <a id="MaskAndAlphaResult.mask_M"></a>`mask_M` — [`L283`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L283) — Transition mask for state u-2.
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`InitializeCtcLoss`](ctc_loss_aten_kernels.cc.md#InitializeCtcLoss), [`ComputeInitialMaskAndAlpha`](ctc_loss_aten_kernels.cc.md#ComputeInitialMaskAndAlpha)

### <a id="ZeroInfinity"></a>`ZeroInfinity`
- def: [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc:80`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L80)
- doc: Whether to zero infinite losses and gradients. If kYes, infinite
- signature: `enum class ZeroInfinity`
- members:
  - <a id="ZeroInfinity.kNo"></a>`kNo` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L80)
  - <a id="ZeroInfinity.kYes"></a>`kYes` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L80)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenCtcLossTensor`](ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenCtcLossBackwardTensor`](ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`BuildCtcLossShlo`](ctc_loss_aten_kernels.cc.md#BuildCtcLossShlo), [`CtcLossForwardInternal`](ctc_loss_aten_kernels.cc.md#CtcLossForwardInternal), [`CtcLossPublicInternal`](ctc_loss_aten_kernels.cc.md#CtcLossPublicInternal), [`CtcLossBackwardInternal`](ctc_loss_aten_kernels.cc.md#CtcLossBackwardInternal), [`BuildCtcLossBackwardShlo`](ctc_loss_aten_kernels.cc.md#BuildCtcLossBackwardShlo), [`BuildCtcLossPublicShlo`](ctc_loss_aten_kernels.cc.md#BuildCtcLossPublicShlo), [`BuildCtcLossPublicBackwardShlo`](ctc_loss_aten_kernels.cc.md#BuildCtcLossPublicBackwardShlo), [`ComputeFinalLoss`](ctc_loss_aten_kernels.cc.md#ComputeFinalLoss), [`BuildCtcLossPublicInferenceShlo`](ctc_loss_aten_kernels.cc.md#BuildCtcLossPublicInferenceShlo)

## Functions
- <a id="AtenCtcLoss"></a>`AtenCtcLoss(const at::Tensor& log_probs, const at::Tensor& targets, at::IntArrayRef input_lengths, at::IntArrayRef target_lengths, int64_t blank, bool zero_infinity)` — [`L1437`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1437)
- <a id="AtenCtcLossBackward"></a>`AtenCtcLossBackward(const at::Tensor& grad_out, const at::Tensor& log_probs, const at::Tensor& targets, at::IntArrayRef input_lengths, at::IntArrayRef target_lengths, const at::Tensor& neg_log_likelihood, const at::Tensor& log_alpha, int64_t blank, bool zero_infinity)` — [`L1768`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1768)
- <a id="AtenCtcLossBackwardTensor"></a>`AtenCtcLossBackwardTensor(const at::Tensor& grad_out, const at::Tensor& log_probs, const at::Tensor& targets, const at::Tensor& input_lengths, const at::Tensor& target_lengths, const at::Tensor& neg_log_likelihood, const at::Tensor& log_alpha, int64_t blank, bool zero_infinity)` — [`L1796`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1796)
- <a id="AtenCtcLossPublic"></a>`AtenCtcLossPublic(const at::Tensor& log_probs, const at::Tensor& targets, at::IntArrayRef input_lengths, at::IntArrayRef target_lengths, int64_t blank, int64_t reduction, bool zero_infinity)` — [`L1742`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1742)
- <a id="AtenCtcLossPublicAutograd"></a>`AtenCtcLossPublicAutograd(const at::Tensor& log_probs, const at::Tensor& targets, at::IntArrayRef input_lengths, at::IntArrayRef target_lengths, int64_t blank, int64_t reduction, bool zero_infinity)` — [`L1700`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1700)
- <a id="AtenCtcLossPublicTensor"></a>`AtenCtcLossPublicTensor(const at::Tensor& log_probs, const at::Tensor& targets, const at::Tensor& input_lengths, const at::Tensor& target_lengths, int64_t blank, int64_t reduction, bool zero_infinity)` — [`L1722`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1722)
- <a id="AtenCtcLossPublicTensorAutograd"></a>`AtenCtcLossPublicTensorAutograd(const at::Tensor& log_probs, const at::Tensor& targets, const at::Tensor& input_lengths, const at::Tensor& target_lengths, int64_t blank, int64_t reduction, bool zero_infinity)` — [`L1711`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1711)
- <a id="AtenCtcLossTensor"></a>`AtenCtcLossTensor(const at::Tensor& log_probs, const at::Tensor& targets, const at::Tensor& input_lengths, const at::Tensor& target_lengths, int64_t blank, bool zero_infinity)` — [`L1461`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1461)
- <a id="BackwardLoopBodyLogic"></a>`BackwardLoopBodyLogic(mlir::RegionBuilder& body, mlir::MlirBuilder& body_builder, mlir::MlirOp t_curr, mlir::MlirOp beta_curr, mlir::MlirOp acc_curr, mlir::MlirOp log_probs, mlir::MlirOp gather_indices, mlir::MlirOp mask_m, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, mlir::MlirOp batch_seq, mlir::MlirOp neg_inf_const, mlir::RankedTensorType type_nl_probs, int64_t n, int64_t c, int64_t l, mlir::Type log_probs_element_type)` — [`L731`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L731) — The core dynamic programming body for the CTC backward algorithm at time t.
- `BackwardLoopBodyLogic(mlir::RegionBuilder& body, mlir::MlirBuilder& body_builder, mlir::MlirOp t_curr, mlir::MlirOp beta_curr, mlir::MlirOp acc_curr, mlir::MlirOp log_probs, mlir::MlirOp gather_indices, mlir::MlirOp mask_m, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, mlir::MlirOp batch_seq, mlir::MlirOp neg_inf_const, mlir::RankedTensorType type_nl_probs, int64_t n, int64_t c, int64_t l, mlir::Type log_probs_element_type)` — [`L731`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L731) — The core dynamic programming body for the CTC backward algorithm at time t.
- <a id="BuildCtcLossBackwardShlo"></a>`BuildCtcLossBackwardShlo(mlir::MlirOp grad_out, mlir::MlirOp log_probs, mlir::MlirOp targets, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, mlir::MlirOp neg_log_likelihood, mlir::MlirOp log_alpha, int64_t blank, ZeroInfinity zero_infinity, mlir::MlirBuilder& builder)` — [`L891`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L891) — Top-level entry point to construct the StableHLO operations for
- <a id="BuildCtcLossPublicBackwardShlo"></a>`BuildCtcLossPublicBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp log_probs, mlir::MlirOp targets, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, mlir::MlirOp loss_unreduced, mlir::MlirOp log_alpha, int64_t blank, ZeroInfinity zero_infinity, int64_t reduction, mlir::MlirBuilder& builder)` — [`L1134`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1134)
- <a id="BuildCtcLossPublicInferenceShlo"></a>`BuildCtcLossPublicInferenceShlo(mlir::MlirOp log_probs, mlir::MlirOp targets, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, int64_t blank, ZeroInfinity zero_infinity, int64_t reduction, mlir::MlirBuilder& builder, std::optional<int64_t> max_target_length = std::nullopt)` — [`L1179`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1179)
- `BuildCtcLossPublicInferenceShlo(mlir::MlirOp log_probs, mlir::MlirOp targets, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, int64_t blank, ZeroInfinity zero_infinity, int64_t reduction, mlir::MlirBuilder& builder, std::optional<int64_t> max_target_length = std::nullopt)` — [`L1179`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1179)
- `BuildCtcLossPublicShlo(mlir::MlirOp log_probs, mlir::MlirOp targets, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, int64_t blank, ZeroInfinity zero_infinity, int64_t reduction, mlir::MlirBuilder& builder, std::optional<int64_t> max_target_length = std::nullopt)` — [`L1085`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1085)
- <a id="BuildCtcLossPublicShlo"></a>`BuildCtcLossPublicShlo(mlir::MlirOp log_probs, mlir::MlirOp targets, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, int64_t blank, ZeroInfinity zero_infinity, int64_t reduction, mlir::MlirBuilder& builder, std::optional<int64_t> max_target_length = std::nullopt)` — [`L1085`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1085)
- <a id="BuildCtcLossShlo"></a>`BuildCtcLossShlo(mlir::MlirOp log_probs, mlir::MlirOp targets, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, int64_t blank, ZeroInfinity zero_infinity, mlir::MlirBuilder& builder, std::optional<int64_t> max_target_length = std::nullopt)` — [`L625`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L625) — Top-level entry point to construct the StableHLO operations for CTC Loss.
- `BuildCtcLossShlo(mlir::MlirOp log_probs, mlir::MlirOp targets, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, int64_t blank, ZeroInfinity zero_infinity, mlir::MlirBuilder& builder, std::optional<int64_t> max_target_length = std::nullopt)` — [`L625`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L625) — Top-level entry point to construct the StableHLO operations for CTC Loss.
- <a id="ComputeFinalLoss"></a>`ComputeFinalLoss(mlir::MlirBuilder& builder, mlir::MlirOp final_log_alpha_acc, mlir::MlirOp input_lengths, mlir::MlirOp target_lengths, mlir::MlirOp batch_seq, mlir::MlirOp neg_inf_const, int64_t N, int64_t L, mlir::Type log_probs_element_type, ZeroInfinity zero_infinity)` — [`L539`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L539) — Computes the total CTC loss after the dynamic programming loop has completed.
- <a id="ComputeInitialMaskAndAlpha"></a>`ComputeInitialMaskAndAlpha(mlir::MlirBuilder& builder, mlir::MlirOp targets, mlir::MlirOp targets_with_blanks, mlir::MlirOp log_probs, mlir::MlirOp batch_seq, int64_t blank, int64_t N, int64_t S, int64_t C, int64_t L, mlir::Type targets_element_type, mlir::Type log_probs_element_type)` — [`L297`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L297) — Computes the initial forward variables (alpha_0) and the transition mask
- <a id="CreateGatherIndices"></a>`CreateGatherIndices(mlir::MlirBuilder& builder, mlir::MlirOp targets_with_blanks, mlir::MlirOp batch_seq, int64_t N, int64_t L, mlir::Type element_type)` — [`L267`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L267) — Constructs the [N, L, 2] tensor of indices used to gather log probabilities.
- <a id="CreateTargetsWithBlanks"></a>`CreateTargetsWithBlanks(mlir::MlirBuilder& builder, mlir::MlirOp targets, int64_t blank, int64_t N, int64_t S, mlir::Type element_type)` — [`L241`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L241) — Expands the targets [N, S] to include blanks for CTC alignment.
- <a id="CtcLossBackwardInternal"></a>`CtcLossBackwardInternal(const at::Tensor& grad_output, const at::Tensor& log_probs_batched, const at::Tensor& targets, const at::Tensor& log_alpha, const at::Tensor& loss_unreduced, const at::Tensor& input_lengths, const at::Tensor& target_lengths, int64_t blank, int64_t reduction, bool zero_infinity, bool is_batched, OpParamCacheKeys param_keys)` — [`L1290`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1290)
- <a id="CtcLossForwardInternal"></a>`CtcLossForwardInternal(const at::Tensor& log_probs, const at::Tensor& targets, const at::Tensor& input_lengths, const at::Tensor& target_lengths, int64_t blank, int64_t reduction, bool zero_infinity, OpParamCacheKeys param_keys, std::optional<int64_t> max_target_length = std::nullopt)` — [`L1192`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1192)
- <a id="CtcLossPublicInternal"></a>`CtcLossPublicInternal(const at::Tensor& log_probs, const at::Tensor& targets, const at::Tensor& input_lengths, const at::Tensor& target_lengths, int64_t blank, int64_t reduction, bool zero_infinity, OpParamCacheKeys param_keys, std::optional<int64_t> max_target_length = std::nullopt)` — [`L1364`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1364)
- `GetGatherDimensionNumbers(mlir::MLIRContext* ctx, llvm::ArrayRef<int64_t> offset_dims, llvm::ArrayRef<int64_t> collapsed_slice_dims, llvm::ArrayRef<int64_t> operand_batching_dims, llvm::ArrayRef<int64_t> start_indices_batching_dims, llvm::ArrayRef<int64_t> start_index_map, int64_t index_vector_dim)` — [`L161`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L161) — Helper to construct GatherDimensionNumbersAttr, configuring how dimensions
- <a id="GetGatherDimensionNumbers"></a>`GetGatherDimensionNumbers(mlir::MLIRContext* ctx, llvm::ArrayRef<int64_t> offset_dims, llvm::ArrayRef<int64_t> collapsed_slice_dims, llvm::ArrayRef<int64_t> operand_batching_dims, llvm::ArrayRef<int64_t> start_indices_batching_dims, llvm::ArrayRef<int64_t> start_index_map, int64_t index_vector_dim)` — [`L161`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L161) — Helper to construct GatherDimensionNumbersAttr, configuring how dimensions
- <a id="GetMaxTargetLength"></a>`GetMaxTargetLength(const at::Tensor& targets, const at::Tensor& target_lengths)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L85) — Returns the maximum target length for CTC loss, either from the 2-D shape
- `GetMaxTargetLength(const at::Tensor& targets, at::IntArrayRef target_lengths)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L112)
- <a id="InitializeCtcLoss"></a>`InitializeCtcLoss(mlir::MlirOp log_probs, mlir::MlirOp targets, int64_t blank, mlir::MlirBuilder& builder)` — [`L386`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L386)
- `LogSumExp(std::vector<mlir::MlirOp> inputs, mlir::MlirOp neg_inf, mlir::MlirOp zero, mlir::MlirOp one)` — [`L131`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L131) — Computes a numerically stable log-sum-exp over a list of MLIR operations.
- <a id="LogSumExp"></a>`LogSumExp(std::vector<mlir::MlirOp> inputs, mlir::MlirOp neg_inf, mlir::MlirOp zero, mlir::MlirOp one)` — [`L131`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L131) — Computes a numerically stable log-sum-exp over a list of MLIR operations.
- <a id="LoopBodyLogic"></a>`LoopBodyLogic(mlir::RegionBuilder& body, mlir::MlirBuilder& body_builder, mlir::MlirOp t_curr, mlir::MlirOp alpha_curr, mlir::MlirOp acc_curr, mlir::MlirOp log_probs, mlir::MlirOp gather_indices, mlir::MlirOp mask_M, mlir::MlirOp neg_inf_const, mlir::RankedTensorType type_nl_probs, int64_t N, int64_t C, int64_t L, mlir::Type log_probs_element_type)` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L445) — The core dynamic programming body for the CTC forward algorithm at time t.
- `LoopBodyLogic(mlir::RegionBuilder& body, mlir::MlirBuilder& body_builder, mlir::MlirOp t_curr, mlir::MlirOp alpha_curr, mlir::MlirOp acc_curr, mlir::MlirOp log_probs, mlir::MlirOp gather_indices, mlir::MlirOp mask_M, mlir::MlirOp neg_inf_const, mlir::RankedTensorType type_nl_probs, int64_t N, int64_t C, int64_t L, mlir::Type log_probs_element_type)` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L445) — The core dynamic programming body for the CTC forward algorithm at time t.
- <a id="ReduceAddDim2"></a>`ReduceAddDim2(mlir::MlirBuilder& builder, mlir::MlirOp input, mlir::Type element_type)` — [`L866`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L866)
- <a id="Unpack1DTargetsTo2DShlo"></a>`Unpack1DTargetsTo2DShlo(mlir::MlirBuilder& builder, mlir::MlirOp targets, mlir::MlirOp target_lengths, int64_t N, int64_t S, mlir::Type element_type)` — [`L174`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L174) — Unpacks a 1-D unpadded targets tensor of shape [sum(target_lengths)] into a
- <a id="ValidateLogProbsDtype"></a>`ValidateLogProbsDtype(const at::Tensor& log_probs)` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L71)

## Other members
- <a id="AtenCtcLossAutograd.backward"></a>`AtenCtcLossAutograd.backward` — [`L1590`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1590)
- <a id="AtenCtcLossAutograd.forward"></a>`AtenCtcLossAutograd.forward` — [`L1547`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1547)
- <a id="AtenCtcLossTensorAutograd.backward"></a>`AtenCtcLossTensorAutograd.backward` — [`L1661`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1661)
- <a id="AtenCtcLossTensorAutograd.forward"></a>`AtenCtcLossTensorAutograd.forward` — [`L1629`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.cc#L1629)

