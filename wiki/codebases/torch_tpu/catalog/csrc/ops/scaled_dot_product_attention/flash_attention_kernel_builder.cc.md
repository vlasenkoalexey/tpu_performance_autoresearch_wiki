---
title: 'Module: csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CreateFlashAttentionBackwardKernel: CreateFlashAttentionBackwardKernel(bd342ce251a39f99).
  CreateFlashAttentionKernelImpl: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/CreateFlashAttentionKernelImpl(1062e9d53ca15ae5).'
  CreateFlashAttnConfig: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/CreateFlashAttnConfig(5b9d425287c3197c).'
  CreateCustomCallOp: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/CreateCustomCallOp(c3b31c846d7956b6).'
  ValidateDtype: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/ValidateDtype(90723f725b74ed91).'
  PadSequenceDim: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/PadSequenceDim(f12dcdc849a72837).'
  CreateTiling: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/CreateTiling(2d1611b60bea7700).'
  SliceSequenceDim: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/SliceSequenceDim(f12dcdc849a72837).'
  kMinHeuristicTileSize: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/kMinHeuristicTileSize.'
  PadBias: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/PadBias(f12dcdc849a72837).'
  ReshapeMask: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/ReshapeMask(50d27f9cf709b647).'
  CreateFlashAttentionKernel: CreateFlashAttentionKernel(a985feff0c6350a6).
  GetKvComputeTileSize: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/GetKvComputeTileSize(8ce0d1b217db7fd1).'
  PackPhiloxSeedAndOffsetTo4xI32: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/PackPhiloxSeedAndOffsetTo4xI32(3bc34110f3947668).'
  PackPhiloxPairTo4xI32: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/PackPhiloxPairTo4xI32(cf97982c188f832c).'
  GetDeviceVmemLimitBytes: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/GetDeviceVmemLimitBytes(da6335ded91d79c2).'
  GetInitialTileSize: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/GetInitialTileSize(8ce0d1b217db7fd1).'
  IsDefined: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/IsDefined(b211e45f30fc6fc1).'
  RoundUpToTileSize: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/RoundUpToTileSize(d0a0e4c270da0eca).'
  kMinHardwareTileSize: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/kMinHardwareTileSize.'
  EstimateTileVmemBytes: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`/EstimateTileVmemBytes(a012dddd2948fd0e).'
---
# Module: [`csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc)

## Functions
- <a id="CreateCustomCallOp"></a>`CreateCustomCallOp(mlir::OpBuilder& builder, mlir::Location loc, mlir::OwningOpRef<mlir::ModuleOp> module, mlir::ValueRange inputs, mlir::TypeRange output_types)` — [`L205`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L205)
- `CreateCustomCallOp(mlir::OpBuilder& builder, mlir::Location loc, mlir::OwningOpRef<mlir::ModuleOp> module, mlir::ValueRange inputs, mlir::TypeRange output_types)` — [`L205`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L205)
- <a id="CreateFlashAttentionBackwardKernel"></a>`CreateFlashAttentionBackwardKernel(const at::Tensor& grad_out, const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const at::Tensor& out, const at::Tensor& logsumexp, std::optional<at::Tensor> attn_bias, std::optional<double> scale, bool is_causal, double dropout_p, const std::optional<at::Tensor>& philox_seed, const std::optional<at::Tensor>& philox_offset)` — [`L698`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L698) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="CreateFlashAttentionKernel"></a>`CreateFlashAttentionKernel(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const std::optional<at::Tensor>& attn_bias, bool is_causal, std::optional<double> scale, double dropout_p, std::optional<bool> return_lse)` — [`L685`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L685)
- <a id="CreateFlashAttentionKernelImpl"></a>`CreateFlashAttentionKernelImpl(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const std::optional<at::Tensor>& attn_bias, bool is_causal, std::optional<double> scale, double dropout_p, bool return_lse)` — [`L468`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L468) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- `CreateFlashAttnConfig(mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, const std::optional<mlir::MlirOp>& attn_bias, bool is_causal, std::optional<double> scale, double dropout_p, bool return_lse, const mlir::torch_tpu::Tiling& tiling, mlir::stablehlo::Precision precision)` — [`L370`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L370)
- <a id="CreateFlashAttnConfig"></a>`CreateFlashAttnConfig(mlir::MlirOp query, mlir::MlirOp key, mlir::MlirOp value, const std::optional<mlir::MlirOp>& attn_bias, bool is_causal, std::optional<double> scale, double dropout_p, bool return_lse, const mlir::torch_tpu::Tiling& tiling, mlir::stablehlo::Precision precision)` — [`L370`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L370) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="CreateTiling"></a>`CreateTiling(int64_t q_seq_len, int64_t k_seq_len, int64_t head_dim, bool is_f32, bool has_mask, bool is_backward, bool has_dropout = false, std::optional<int64_t> vmem_limit_override = std::nullopt)` — [`L173`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L173)
- `CreateTiling(mlir::MlirOp query, mlir::MlirOp key, bool has_mask, bool is_backward = false, bool has_dropout = false)` — [`L329`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L329)
- <a id="EstimateTileVmemBytes"></a>`EstimateTileVmemBytes(int64_t qt, int64_t kt, int64_t head_dim, bool is_f32, bool has_mask, bool is_backward, bool has_dropout = false)` — [`L137`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L137)
- <a id="GetDeviceVmemLimitBytes"></a>`GetDeviceVmemLimitBytes()` — [`L92`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L92)
- <a id="GetInitialTileSize"></a>`GetInitialTileSize(int64_t seq_len)` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L127)
- <a id="GetKvComputeTileSize"></a>`GetKvComputeTileSize(int64_t kt)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L155) — Heuristic to determine the KV compute sub-tile size.
- <a id="IsDefined"></a>`IsDefined(const std::optional<at::Tensor>& tensor)` — [`L267`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L267)
- <a id="PackPhiloxPairTo4xI32"></a>`PackPhiloxPairTo4xI32(mlir::MlirOp pair_i64)` — [`L344`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L344) — Unpacks a 2-element i64 tensor `[seed, offset]` into a 4-element i32 tensor
- <a id="PackPhiloxSeedAndOffsetTo4xI32"></a>`PackPhiloxSeedAndOffsetTo4xI32(mlir::MlirOp philox_seed, mlir::MlirOp philox_offset)` — [`L361`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L361) — Packs `philox_seed` and `philox_offset` into a 4-element i32 tensor. The
- <a id="PadBias"></a>`PadBias(mlir::MlirOp bias, int64_t padded_q_len, int64_t padded_kv_len)` — [`L317`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L317) — Pad the mask if the sequence lengths are not the same as the padded sequence
- <a id="PadSequenceDim"></a>`PadSequenceDim(mlir::MlirOp input, int64_t seq_dim, int64_t target_len)` — [`L279`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L279) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="ReshapeMask"></a>`ReshapeMask(mlir::MlirOp mask_mlir, int batch_size)` — [`L453`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L453)
- <a id="RoundUpToTileSize"></a>`RoundUpToTileSize(int64_t seq_len, int64_t tile_size)` — [`L123`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L123)
- <a id="SliceSequenceDim"></a>`SliceSequenceDim(mlir::MlirOp input, int64_t seq_dim, int64_t target_len)` — [`L297`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L297)
- <a id="ValidateDtype"></a>`ValidateDtype(at::ScalarType dtype)` — [`L271`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L271) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)

## Module values
- <a id="kMinHardwareTileSize"></a>`kMinHardwareTileSize` — [`L119`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L119) — Minimum hardware tile size (hardware lane width).
- <a id="kMinHeuristicTileSize"></a>`kMinHeuristicTileSize` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc#L121) — Minimum tile size for the > 256 heuristic.

