---
title: 'Module: csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenTransformerEncoderLayerFwd: AtenTransformerEncoderLayerFwd(591a45f1e988e55f).
  ValidateTransformerEncoderInputs: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/ValidateTransformerEncoderInputs(53d202d7aa2c3a54).'
  ApplyAttentionMaskShlo: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/ApplyAttentionMaskShlo(b8cf56afbce6ef5a).'
  BuildMultiheadAttentionShlo: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/BuildMultiheadAttentionShlo(cefd60eded6f2f06).'
  BuildFeedForwardShlo: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/BuildFeedForwardShlo(54b420f67b7c933).'
  ReshapeMask2DShlo: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/ReshapeMask2DShlo(246b4823ccf7cdee).'
  ReshapeMask3DShlo: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/ReshapeMask3DShlo(fad9fe3a36b8efd1).'
  ReshapeMaskTo4DShlo: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/ReshapeMaskTo4DShlo(fad9fe3a36b8efd1).'
  Activation.kGelu: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/Activation#kGelu.'
  Activation: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/Activation#'
  Activation.kRelu: '`$anonymous_namespace_csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`/Activation#kRelu.'
---
# Module: [`csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc)

## Classes
### <a id="Activation"></a>`Activation`
- def: [`csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc:372`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L372)
- signature: `enum class Activation`
- members:
  - <a id="Activation.kGelu"></a>`kGelu` — [`L372`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L372)
  - <a id="Activation.kRelu"></a>`kRelu` — [`L372`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L372)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenTransformerEncoderLayerFwd`](_transformer_encoder_layer_fwd_aten_kernels.cc.md#AtenTransformerEncoderLayerFwd), [`BuildFeedForwardShlo`](_transformer_encoder_layer_fwd_aten_kernels.cc.md#BuildFeedForwardShlo)

## Functions
- <a id="ApplyAttentionMaskShlo"></a>`ApplyAttentionMaskShlo(mlir::MlirOp attn_logits, mlir::MlirOp mask_op, const std::optional<int64_t> mask_type, const mlir::Type elem_type, const int64_t B_dummy, const int64_t T_dummy, const int64_t nH, mlir::MlirBuilder& builder)` — [`L206`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L206)
- <a id="AtenTransformerEncoderLayerFwd"></a>`AtenTransformerEncoderLayerFwd(const at::Tensor& src, const int64_t embed_dim, const int64_t num_heads, const at::Tensor& qkv_weight, const at::Tensor& qkv_bias, const at::Tensor& proj_weight, const at::Tensor& proj_bias, const bool use_gelu, const bool norm_first, const double eps, const at::Tensor& norm_weight_1, const at::Tensor& norm_bias_1, const at::Tensor& norm_weight_2, const at::Tensor& norm_bias_2, const at::Tensor& ffn_weight_1, const at::Tensor& ffn_bias_1, const at::Tensor& ffn_weight_2, const at::Tensor& ffn_bias_2, const std::optional<at::Tensor>& mask, const std::optional<int64_t> mask_type)` — [`L419`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L419)
- <a id="BuildFeedForwardShlo"></a>`BuildFeedForwardShlo(mlir::MlirOp x_op, mlir::MlirOp ffn_weight_1_op, mlir::MlirOp ffn_bias_1_op, mlir::MlirOp ffn_weight_2_op, mlir::MlirOp ffn_bias_2_op, const Activation activation, const mlir::ElementType out_dtype, mlir::MlirBuilder& builder)` — [`L374`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L374)
- <a id="BuildMultiheadAttentionShlo"></a>`BuildMultiheadAttentionShlo(mlir::MlirOp x_op, mlir::MlirOp qkv_weight_op, mlir::MlirOp qkv_bias_op, mlir::MlirOp proj_weight_op, mlir::MlirOp proj_bias_op, const std::optional<mlir::MlirOp>& mask_op, const std::optional<int64_t> mask_type, const int64_t B, const int64_t T, const int64_t D, const int64_t nH, const int64_t d_k, mlir::MlirBuilder& builder)` — [`L238`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L238)
- <a id="ReshapeMask2DShlo"></a>`ReshapeMask2DShlo(mlir::MlirOp mask_val, const std::optional<int64_t> mask_type)` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L152)
- <a id="ReshapeMask3DShlo"></a>`ReshapeMask3DShlo(mlir::MlirOp mask_val, const std::optional<int64_t> mask_type, const int64_t B_dummy, const int64_t T_dummy, const int64_t nH)` — [`L169`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L169)
- <a id="ReshapeMaskTo4DShlo"></a>`ReshapeMaskTo4DShlo(mlir::MlirOp mask_val, const std::optional<int64_t> mask_type, const int64_t B_dummy, const int64_t T_dummy, const int64_t nH)` — [`L192`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L192)
- <a id="ValidateTransformerEncoderInputs"></a>`ValidateTransformerEncoderInputs(const at::Tensor& src, const int64_t embed_dim, const int64_t num_heads, const at::Tensor& qkv_weight, const at::Tensor& qkv_bias, const at::Tensor& proj_weight, const at::Tensor& proj_bias, const at::Tensor& norm_weight_1, const at::Tensor& norm_bias_1, const at::Tensor& norm_weight_2, const at::Tensor& norm_bias_2, const at::Tensor& ffn_weight_1, const at::Tensor& ffn_bias_1, const at::Tensor& ffn_weight_2, const at::Tensor& ffn_bias_2, const std::optional<at::Tensor>& mask)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc#L60)

