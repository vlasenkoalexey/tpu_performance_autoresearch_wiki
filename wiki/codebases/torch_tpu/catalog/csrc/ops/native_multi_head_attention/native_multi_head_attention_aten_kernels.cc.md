---
title: 'Module: csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNativeMultiHeadAttention: AtenNativeMultiHeadAttention(96bf64cbe2945560).
  ValidateNativeMultiHeadAttentionInputs: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/ValidateNativeMultiHeadAttentionInputs(1e1385b43c3dd2b2).'
  BuildMhaCore: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/BuildMhaCore(5e1b5f197d6e151d).'
  BuildLinear: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/BuildLinear(7e743fa3a17e6aad).'
  BuildNativeMultiHeadAttentionWithWeightsShlo: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/BuildNativeMultiHeadAttentionWithWeightsShlo(bb91b4a78bcdc37f).'
  BuildDotGeneral: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/BuildDotGeneral(37672a16cbec0528).'
  BuildNativeMultiHeadAttentionNoWeightsShlo: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/BuildNativeMultiHeadAttentionNoWeightsShlo(b9611b652f558cad).'
  MhaCoreTensors.attn_weights_full: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/MhaCoreTensors#attn_weights_full.'
  MhaCoreTensors.out: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/MhaCoreTensors#out.'
  MhaCoreTensors: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/MhaCoreTensors#'
  AttnWeightsReduction.kAverage: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/AttnWeightsReduction#kAverage.'
  AttnWeightsReduction: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/AttnWeightsReduction#'
  AttnWeightsReduction.kNone: '`$anonymous_namespace_csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`/AttnWeightsReduction#kNone.'
---
# Module: [`csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc)

## Classes
### <a id="AttnWeightsReduction"></a>`AttnWeightsReduction`
- def: [`csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc:58`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L58)
- signature: `enum class AttnWeightsReduction`
- members:
  - <a id="AttnWeightsReduction.kAverage"></a>`kAverage` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L58)
  - <a id="AttnWeightsReduction.kNone"></a>`kNone` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L58)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenNativeMultiHeadAttention`](native_multi_head_attention_aten_kernels.cc.md#AtenNativeMultiHeadAttention), [`BuildNativeMultiHeadAttentionWithWeightsShlo`](native_multi_head_attention_aten_kernels.cc.md#BuildNativeMultiHeadAttentionWithWeightsShlo)

### <a id="MhaCoreTensors"></a>`MhaCoreTensors`
- def: [`csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc:254`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L254)
- doc: Common function to compute core MHA intermediate tensors
- signature: `struct MhaCoreTensors`
- members:
  - <a id="MhaCoreTensors.attn_weights_full"></a>`attn_weights_full` — [`L256`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L256)
  - <a id="MhaCoreTensors.out"></a>`out` — [`L255`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L255)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildMhaCore`](native_multi_head_attention_aten_kernels.cc.md#BuildMhaCore), [`BuildNativeMultiHeadAttentionWithWeightsShlo`](native_multi_head_attention_aten_kernels.cc.md#BuildNativeMultiHeadAttentionWithWeightsShlo), [`BuildNativeMultiHeadAttentionNoWeightsShlo`](native_multi_head_attention_aten_kernels.cc.md#BuildNativeMultiHeadAttentionNoWeightsShlo)

## Functions
- <a id="AtenNativeMultiHeadAttention"></a>`AtenNativeMultiHeadAttention(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, int64_t embed_dim, int64_t num_head, const at::Tensor& qkv_weight, const at::Tensor& qkv_bias, const at::Tensor& proj_weight, const at::Tensor& proj_bias, const std::optional<at::Tensor>& mask, bool need_weights, bool average_attn_weights, std::optional<int64_t> mask_type)` — [`L465`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L465)
- <a id="BuildDotGeneral"></a>`BuildDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, absl::Span<const int64_t> lhs_contracting, absl::Span<const int64_t> rhs_contracting, absl::Span<const int64_t> lhs_batching = {}, absl::Span<const int64_t> rhs_batching = {}, mlir::stablehlo::Precision precision = mlir::stablehlo::Precision::DEFAULT)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L166)
- `BuildDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, absl::Span<const int64_t> lhs_contracting, absl::Span<const int64_t> rhs_contracting, absl::Span<const int64_t> lhs_batching = {}, absl::Span<const int64_t> rhs_batching = {}, mlir::stablehlo::Precision precision = mlir::stablehlo::Precision::DEFAULT)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L166)
- <a id="BuildLinear"></a>`BuildLinear(mlir::MlirOp input, mlir::MlirOp weight, mlir::MlirOp bias, mlir::stablehlo::Precision precision)` — [`L221`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L221)
- `BuildLinear(mlir::MlirOp input, mlir::MlirOp weight, mlir::MlirOp bias, mlir::stablehlo::Precision precision)` — [`L221`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L221)
- `BuildMhaCore(mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, mlir::MlirOp qkv_weight, mlir::MlirOp qkv_bias, mlir::MlirOp proj_weight, mlir::MlirOp proj_bias, std::optional<mlir::MlirOp> mask, int64_t embed_dim, int64_t num_head, mlir::stablehlo::Precision precision, std::optional<int64_t> mask_type_param = std::nullopt)` — [`L259`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L259)
- <a id="BuildMhaCore"></a>`BuildMhaCore(mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, mlir::MlirOp qkv_weight, mlir::MlirOp qkv_bias, mlir::MlirOp proj_weight, mlir::MlirOp proj_bias, std::optional<mlir::MlirOp> mask, int64_t embed_dim, int64_t num_head, mlir::stablehlo::Precision precision, std::optional<int64_t> mask_type_param = std::nullopt)` — [`L259`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L259)
- `BuildNativeMultiHeadAttentionNoWeightsShlo(mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, mlir::MlirOp qkv_weight, mlir::MlirOp qkv_bias, mlir::MlirOp proj_weight, mlir::MlirOp proj_bias, std::optional<mlir::MlirOp> mask, int64_t embed_dim, int64_t num_head, mlir::stablehlo::Precision precision, std::optional<int64_t> mask_type_param = std::nullopt)` — [`L450`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L450)
- <a id="BuildNativeMultiHeadAttentionNoWeightsShlo"></a>`BuildNativeMultiHeadAttentionNoWeightsShlo(mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, mlir::MlirOp qkv_weight, mlir::MlirOp qkv_bias, mlir::MlirOp proj_weight, mlir::MlirOp proj_bias, std::optional<mlir::MlirOp> mask, int64_t embed_dim, int64_t num_head, mlir::stablehlo::Precision precision, std::optional<int64_t> mask_type_param = std::nullopt)` — [`L450`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L450)
- <a id="BuildNativeMultiHeadAttentionWithWeightsShlo"></a>`BuildNativeMultiHeadAttentionWithWeightsShlo(mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, mlir::MlirOp qkv_weight, mlir::MlirOp qkv_bias, mlir::MlirOp proj_weight, mlir::MlirOp proj_bias, std::optional<mlir::MlirOp> mask, int64_t embed_dim, int64_t num_head, AttnWeightsReduction weights_reduction, mlir::stablehlo::Precision precision, std::optional<int64_t> mask_type_param = std::nullopt)` — [`L421`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L421)
- `BuildNativeMultiHeadAttentionWithWeightsShlo(mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, mlir::MlirOp qkv_weight, mlir::MlirOp qkv_bias, mlir::MlirOp proj_weight, mlir::MlirOp proj_bias, std::optional<mlir::MlirOp> mask, int64_t embed_dim, int64_t num_head, AttnWeightsReduction weights_reduction, mlir::stablehlo::Precision precision, std::optional<int64_t> mask_type_param = std::nullopt)` — [`L421`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L421)
- <a id="ValidateNativeMultiHeadAttentionInputs"></a>`ValidateNativeMultiHeadAttentionInputs(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, int64_t embed_dim, int64_t num_head, const at::Tensor& qkv_weight, const at::Tensor& qkv_bias, const at::Tensor& proj_weight, const at::Tensor& proj_bias, const std::optional<at::Tensor>& mask)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_multi_head_attention/native_multi_head_attention_aten_kernels.cc#L60)

