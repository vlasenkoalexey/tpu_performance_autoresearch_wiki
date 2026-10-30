---
title: 'Module: csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PrepareAttentionLogits: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/PrepareAttentionLogits(9f3608967695e6a6).'
  BuildScaledDotProductAttentionBackward: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/BuildScaledDotProductAttentionBackward(bb1887ec466ef98e).'
  ScaledDotProductFusedAttentionShlo: ScaledDotProductFusedAttentionShlo(fdfb2324774ec1be).
  BuildScaledDotProductFusedAttentionShloOp: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/BuildScaledDotProductFusedAttentionShloOp(2c3b78022d90bcaa).'
  ScaledDotProductFusedAttentionShloBackward: ScaledDotProductFusedAttentionShloBackward(49561097bf25142a).
  ComputeGqaBackwardGradients: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/ComputeGqaBackwardGradients(43eebb6bb076e4fa).'
  ComputeGradP: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/ComputeGradP(6fb228fd2a36be37).'
  ComputeStandardBackwardGradients: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/ComputeStandardBackwardGradients(cf061bd7a8ef4712).'
  ConvertElementTypeIfNeeded: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/ConvertElementTypeIfNeeded(441bf030f6313d62).'
  GetCausalMask: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/GetCausalMask(a7867b6222e713f9).'
  PromoteInputIfRequired: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/PromoteInputIfRequired(f8ed13c24baa4ca3).'
  GetSdpaPromotionType: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/GetSdpaPromotionType(88583d9e0a2e7823).'
  SumReduce: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/SumReduce(9f5448989bc725b3).'
  ComputeAttentionOutput: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/ComputeAttentionOutput(a95f2ec02edca2fa).'
  SdpaPromotionType: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/SdpaPromotionType#'
  CanUseXlaOnlineSoftmax: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/CanUseXlaOnlineSoftmax(a762207125510bfe).'
  IsSdpaSequenceAlignedAndLarge: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/IsSdpaSequenceAlignedAndLarge(a762207125510bfe).'
  BackwardGradients4D: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/BackwardGradients4D#'
  GetNegInf: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/GetNegInf(33062c2767d2523b).'
  BackwardGradients4D.grad_value_4d: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/BackwardGradients4D#grad_value_4d.'
  BackwardGradients4D.grad_key_4d: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/BackwardGradients4D#grad_key_4d.'
  BackwardGradients4D.grad_query_4d: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/BackwardGradients4D#grad_query_4d.'
  AttentionPrepResults: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/AttentionPrepResults#'
  SdpaPromotionType.kSoftmaxOnly: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/SdpaPromotionType#kSoftmaxOnly.'
  SdpaPromotionType.kWholeModule: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/SdpaPromotionType#kWholeModule.'
  AttentionPrepResults.query_4d: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/AttentionPrepResults#query_4d.'
  AttentionPrepResults.value_4d: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/AttentionPrepResults#value_4d.'
  AttentionPrepResults.head_count_ratio: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/AttentionPrepResults#head_count_ratio.'
  AttentionPrepResults.key_4d: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/AttentionPrepResults#key_4d.'
  AttentionPrepResults.shifted_attn_logits: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/AttentionPrepResults#shifted_attn_logits.'
  AttentionPrepResults.is_row_all_masked: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/AttentionPrepResults#is_row_all_masked.'
  SdpaPromotionType.kNone: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/SdpaPromotionType#kNone.'
  AttentionPrepResults.scale_value: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`/AttentionPrepResults#scale_value.'
---
# Module: [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc)

## Classes
### <a id="AttentionPrepResults"></a>`AttentionPrepResults`
- def: [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc:65`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L65)
- signature: `struct AttentionPrepResults`
- members:
  - <a id="AttentionPrepResults.head_count_ratio"></a>`head_count_ratio` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L71)
  - <a id="AttentionPrepResults.is_row_all_masked"></a>`is_row_all_masked` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L72)
  - <a id="AttentionPrepResults.key_4d"></a>`key_4d` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L67)
  - <a id="AttentionPrepResults.query_4d"></a>`query_4d` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L66)
  - <a id="AttentionPrepResults.scale_value"></a>`scale_value` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L70)
  - <a id="AttentionPrepResults.shifted_attn_logits"></a>`shifted_attn_logits` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L69)
  - <a id="AttentionPrepResults.value_4d"></a>`value_4d` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L68)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`PrepareAttentionLogits`](scaled_dot_product_attention_shlo.cc.md#PrepareAttentionLogits), [`ConvertElementTypeIfNeeded`](scaled_dot_product_attention_shlo.cc.md#ConvertElementTypeIfNeeded)

### <a id="BackwardGradients4D"></a>`BackwardGradients4D`
- def: [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc:594`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L594)
- signature: `struct BackwardGradients4D`
- members:
  - <a id="BackwardGradients4D.grad_key_4d"></a>`grad_key_4d` — [`L596`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L596)
  - <a id="BackwardGradients4D.grad_query_4d"></a>`grad_query_4d` — [`L595`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L595)
  - <a id="BackwardGradients4D.grad_value_4d"></a>`grad_value_4d` — [`L597`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L597)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildScaledDotProductAttentionBackward`](scaled_dot_product_attention_shlo.cc.md#BuildScaledDotProductAttentionBackward), [`ComputeGqaBackwardGradients`](scaled_dot_product_attention_shlo.cc.md#ComputeGqaBackwardGradients), [`ComputeStandardBackwardGradients`](scaled_dot_product_attention_shlo.cc.md#ComputeStandardBackwardGradients)

### <a id="SdpaPromotionType"></a>`SdpaPromotionType`
- def: [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc:97`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L97)
- signature: `enum class SdpaPromotionType`
- members:
  - <a id="SdpaPromotionType.kNone"></a>`kNone` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L98)
  - <a id="SdpaPromotionType.kSoftmaxOnly"></a>`kSoftmaxOnly` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L99)
  - <a id="SdpaPromotionType.kWholeModule"></a>`kWholeModule` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L100)
- used by: [`BuildScaledDotProductAttentionBackward`](scaled_dot_product_attention_shlo.cc.md#BuildScaledDotProductAttentionBackward), [`BuildScaledDotProductFusedAttentionShloOp`](scaled_dot_product_attention_shlo.cc.md#BuildScaledDotProductFusedAttentionShloOp), [`PromoteInputIfRequired`](scaled_dot_product_attention_shlo.cc.md#PromoteInputIfRequired), [`GetSdpaPromotionType`](scaled_dot_product_attention_shlo.cc.md#GetSdpaPromotionType)

## Functions
- <a id="BuildScaledDotProductAttentionBackward"></a>`BuildScaledDotProductAttentionBackward(absl::Span<mlir::MlirOp> inputs, mlir::MlirBuilder& builder, int rank, int batch_size, bool is_causal, std::optional<double> scale, int64_t num_head_q, int64_t num_head_kv, int64_t seq_len_q, int64_t seq_len_kv, int64_t head_dim, bool allow_half_precision_reduction_math, mlir::stablehlo::Precision precision)` — [`L742`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L742) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- `BuildScaledDotProductAttentionBackward(absl::Span<mlir::MlirOp> inputs, mlir::MlirBuilder& builder, int rank, int batch_size, bool is_causal, std::optional<double> scale, int64_t num_head_q, int64_t num_head_kv, int64_t seq_len_q, int64_t seq_len_kv, int64_t head_dim, bool allow_half_precision_reduction_math, mlir::stablehlo::Precision precision)` — [`L742`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L742)
- <a id="BuildScaledDotProductFusedAttentionShloOp"></a>`BuildScaledDotProductFusedAttentionShloOp(absl::Span<mlir::MlirOp> inputs, mlir::MlirBuilder& builder, bool is_causal, std::optional<double> scale, bool allow_half_precision_reduction_math, mlir::stablehlo::Precision precision)` — [`L473`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L473) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- `BuildScaledDotProductFusedAttentionShloOp(absl::Span<mlir::MlirOp> inputs, mlir::MlirBuilder& builder, bool is_causal, std::optional<double> scale, bool allow_half_precision_reduction_math, mlir::stablehlo::Precision precision)` — [`L473`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L473)
- <a id="CanUseXlaOnlineSoftmax"></a>`CanUseXlaOnlineSoftmax(mlir::MlirOp query, mlir::MlirOp key)` — [`L176`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L176) — Returns true when XLA's MatchSoftmax rewriter can fuse forward SDPA into the
- `ComputeAttentionOutput(mlir::MLIRContext* context, mlir::MlirOp softmax, mlir::MlirOp value_4d, mlir::MlirOp query_4d, int64_t head_count_ratio, mlir::stablehlo::Precision precision)` — [`L437`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L437)
- <a id="ComputeAttentionOutput"></a>`ComputeAttentionOutput(mlir::MLIRContext* context, mlir::MlirOp softmax, mlir::MlirOp value_4d, mlir::MlirOp query_4d, int64_t head_count_ratio, mlir::stablehlo::Precision precision)` — [`L437`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L437)
- <a id="ComputeGqaBackwardGradients"></a>`ComputeGqaBackwardGradients(mlir::MLIRContext* context, mlir::MlirBuilder& builder, mlir::MlirOp softmax, mlir::MlirOp grad_out_4d, mlir::MlirOp query_4d, mlir::MlirOp key_4d, mlir::MlirOp value_4d, mlir::Type element_type, mlir::Type softmax_calc_type, int64_t head_count_ratio, int64_t batch_size, int64_t num_head_q, int64_t num_head_kv, int64_t seq_len_q, int64_t seq_len_kv, int64_t head_dim, mlir::stablehlo::Precision precision)` — [`L600`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L600)
- `ComputeGqaBackwardGradients(mlir::MLIRContext* context, mlir::MlirBuilder& builder, mlir::MlirOp softmax, mlir::MlirOp grad_out_4d, mlir::MlirOp query_4d, mlir::MlirOp key_4d, mlir::MlirOp value_4d, mlir::Type element_type, mlir::Type softmax_calc_type, int64_t head_count_ratio, int64_t batch_size, int64_t num_head_q, int64_t num_head_kv, int64_t seq_len_q, int64_t seq_len_kv, int64_t head_dim, mlir::stablehlo::Precision precision)` — [`L600`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L600)
- <a id="ComputeGradP"></a>`ComputeGradP(mlir::MlirBuilder& builder, mlir::MlirOp softmax, mlir::MlirOp grad_softmax, mlir::Type softmax_calc_type)` — [`L578`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L578)
- `ComputeStandardBackwardGradients(mlir::MLIRContext* context, mlir::MlirBuilder& builder, mlir::MlirOp softmax, mlir::MlirOp grad_out_4d, mlir::MlirOp query_4d, mlir::MlirOp key_4d, mlir::MlirOp value_4d, mlir::Type element_type, mlir::Type softmax_calc_type, mlir::stablehlo::Precision precision)` — [`L683`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L683)
- <a id="ComputeStandardBackwardGradients"></a>`ComputeStandardBackwardGradients(mlir::MLIRContext* context, mlir::MlirBuilder& builder, mlir::MlirOp softmax, mlir::MlirOp grad_out_4d, mlir::MlirOp query_4d, mlir::MlirOp key_4d, mlir::MlirOp value_4d, mlir::Type element_type, mlir::Type softmax_calc_type, mlir::stablehlo::Precision precision)` — [`L683`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L683)
- <a id="ConvertElementTypeIfNeeded"></a>`ConvertElementTypeIfNeeded(mlir::MlirOp op, mlir::Type target_type)` — [`L195`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L195)
- <a id="GetCausalMask"></a>`GetCausalMask(mlir::MlirOp reference_op)` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L87) — Returns a boolean mask with the shape of `reference_op` that is true where
- <a id="GetNegInf"></a>`GetNegInf(mlir::MlirBuilder& builder, mlir::FloatType element_type)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L74)
- <a id="GetSdpaPromotionType"></a>`GetSdpaPromotionType(mlir::MlirOp query, mlir::MlirOp /*key*/, bool allow_half_precision_reduction_math)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L109) — Determine exactly where type promotion should happen inside the attn module.
- <a id="IsSdpaSequenceAlignedAndLarge"></a>`IsSdpaSequenceAlignedAndLarge(mlir::MlirOp query, mlir::MlirOp key)` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L128) — Returns true if the attention tensor has enough elements (>500k) and sequence
- <a id="PrepareAttentionLogits"></a>`PrepareAttentionLogits(mlir::MlirBuilder& builder, mlir::MLIRContext* context, mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, std::optional<mlir::MlirOp> mask, bool is_causal, std::optional<double> scale, mlir::stablehlo::Precision precision)` — [`L203`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L203) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- `PrepareAttentionLogits(mlir::MlirBuilder& builder, mlir::MLIRContext* context, mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, std::optional<mlir::MlirOp> mask, bool is_causal, std::optional<double> scale, mlir::stablehlo::Precision precision)` — [`L203`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L203)
- <a id="PromoteInputIfRequired"></a>`PromoteInputIfRequired(mlir::MlirBuilder& builder, mlir::MlirOp op, SdpaPromotionType promotion_type)` — [`L426`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L426)
- <a id="ScaledDotProductFusedAttentionShlo"></a>`ScaledDotProductFusedAttentionShlo(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const std::optional<at::Tensor>& attn_bias, bool is_causal, std::optional<double> scale, bool allow_half_precision_reduction_math, OpParamCacheKeys param_keys)` — [`L885`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L885) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="ScaledDotProductFusedAttentionShloBackward"></a>`ScaledDotProductFusedAttentionShloBackward(const at::Tensor& grad_out, const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const at::Tensor& attn_bias, const at::Tensor& sum_exp, std::optional<double> scale, bool is_causal, bool allow_half_precision_reduction_math, OpParamCacheKeys param_keys)` — [`L934`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L934) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="SumReduce"></a>`SumReduce(mlir::MlirBuilder& builder, mlir::MlirOp input, int dimension)` — [`L413`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc#L413)

