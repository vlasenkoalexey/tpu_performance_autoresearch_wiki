---
title: 'Module: csrc/ops/reductions/reductions.h'
type: catalog
provenance: extracted
module: csrc/ops/reductions/reductions.h
status: fresh
symbol_base: cxx . . $ torch_tpu/ReductionMode#
symbols:
  ReductionMode: ''
  ReductionMode.kDropDims: kDropDims.
  ReductionMode.kKeepDims: kKeepDims.
---
# Module: [`csrc/ops/reductions/reductions.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reductions.h)

## Classes
### <a id="ReductionMode"></a>`ReductionMode`
- def: [`csrc/ops/reductions/reductions.h:29`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reductions.h#L29) — documented in [reductions](../../../../concepts/reductions.md)
- signature: `enum class ReductionMode`
- members:
  - <a id="ReductionMode.kDropDims"></a>`kDropDims` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reductions.h#L29) — documented in [reductions](../../../../concepts/reductions.md)
  - <a id="ReductionMode.kKeepDims"></a>`kKeepDims` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reductions.h#L29) — documented in [reductions](../../../../concepts/reductions.md)
- uses (calls/refs, reference-scoped): [`BuildReductionShlo`](reductions.cc.md#BuildReductionShlo), [`BuildKeepDimsShlo`](reductions.cc.md#BuildKeepDimsShlo)
- used by: [`AtenVarMeanCorrection`](var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenForeachNormScalar`](../foreach_aten_kernels.cc.md#AtenForeachNormScalar), [`AtenStd`](std_aten_kernels.cc.md#AtenStd), [`AtenVar`](var_aten_kernels.cc.md#AtenVar), [`AtenStdOut`](std_aten_kernels.cc.md#AtenStdOut), [`AtenVarOut`](var_aten_kernels.cc.md#AtenVarOut), [`CreateFlashAttentionBackwardKernel`](../scaled_dot_product_attention/flash_attention_kernel_builder.cc.md#CreateFlashAttentionBackwardKernel), [`AtenAminmaxOut`](../a_min_max/a_min_max_aten_kernels.cc.md#AtenAminmaxOut), [`AtenMeanOut`](mean_aten_kernels.cc.md#AtenMeanOut), [`AtenNativeNormScalarOptDimDtype`](../native_norm/native_norm_aten_kernels.cc.md#AtenNativeNormScalarOptDimDtype), [`AtenNativeNormScalar`](../native_norm/native_norm_aten_kernels.cc.md#AtenNativeNormScalar), [`AtenThnnFusedLstmCellBackwardImpl`](../thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc.md#AtenThnnFusedLstmCellBackwardImpl), [`BuildSumShlo`](sum.cc.md#BuildSumShlo), [`AtenThnnFusedGruCellBackward`](../thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc.md#AtenThnnFusedGruCellBackward), [`AtenCountNonzeroDimIntList`](../count_nonzero/count_nonzero_aten_kernels.cc.md#AtenCountNonzeroDimIntList), [`AtenSumIntListOut`](sum_aten_kernels.cc.md#AtenSumIntListOut), [`ArgMinMax`](../min_max/min_max_aten_kernels.cc.md#ArgMinMax), [`UnaryMinMax`](../min_max/min_max_aten_kernels.cc.md#UnaryMinMax), [`AMinMax`](../a_min_max/a_min_max_aten_kernels.cc.md#AMinMax), [`BuildNllLossForwardOutShlo`](../nll_loss/nll_loss.cc.md#BuildNllLossForwardOutShlo), [`BuildQdwhShlo`](../linalg/linalg_svd_kernels.cc.md#BuildQdwhShlo), [`PNormOut`](../norm/norm_aten_kernels.cc.md#PNormOut), [`BuildCrossEntropyClassIndicesShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyClassIndicesShlo), [`BuildCrossEntropyProbTargetShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyProbTargetShlo), [`AtenMinMaxDim`](../min_max/min_max_aten_kernels.cc.md#AtenMinMaxDim), [`ApplySumReduction`](reduction_utils.cc.md#ApplySumReduction), [`PNorm`](../native_norm/native_norm_aten_kernels.cc.md#PNorm), [`GetSizesAfterReduction`](reduction_utils.cc.md#GetSizesAfterReduction), [`DispatchUnaryMinMax`](../min_max/min_max_aten_kernels.cc.md#DispatchUnaryMinMax), [`BuildMinMaxShlo`](../min_max/min_max.cc.md#BuildMinMaxShlo), [`CreateStdBuilder`](std_aten_kernels.cc.md#CreateStdBuilder), [`BuildPNormShlo`](../linalg/vector_norm/pnorm.cc.md#BuildPNormShlo), [`BuildCrossEntropyClassIndicesBackwardShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyClassIndicesBackwardShlo), [`PNormOut`](../linalg/vector_norm/aten_vector_norm_kernels.cc.md#PNormOut), [`BuildCrossEntropyProbTargetBackwardShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyProbTargetBackwardShlo), [`BuildMultinomialShlo`](../multinomial/multinomial.cc.md#BuildMultinomialShlo), [`AtenProdHelper`](../prod/prod_aten_kernels.cc.md#AtenProdHelper), [`CreateVarBuilder`](var_aten_kernels.cc.md#CreateVarBuilder), [`BuildWeightNormShlo`](../weight_norm/weight_norm_aten_kernels.cc.md#BuildWeightNormShlo), [`BuildRenormRow`](../embedding/embedding.cc.md#BuildRenormRow)  (+31 more)

