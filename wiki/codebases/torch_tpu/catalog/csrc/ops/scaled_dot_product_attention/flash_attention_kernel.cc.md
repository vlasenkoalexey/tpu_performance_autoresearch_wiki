---
title: 'Module: csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc
status: fresh
symbol_base: cxx . . $ mlir/torch_tpu/
symbols:
  buildModule: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/buildModule(758cec2b4e0ef1cf).'
  UpdateSoftmaxState: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/UpdateSoftmaxState(a804dc915ff2b2ce).'
  CreateKernel: CreateKernel(5655a7067ede568e).
  EmitGridStep: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/EmitGridStep(afbb09829c00a733).'
  StoreNormalizedOutput: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/StoreNormalizedOutput(88713208cc8af59b).'
  SetKernelAttributes: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/SetKernelAttributes(4947f803f40af1ea).'
  ApplyDropoutToProbabilities: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/ApplyDropoutToProbabilities(edd4ae9e3b54eb72).'
  SoftmaxState.m: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/SoftmaxState#m.'
  KernelArgs.col_block_idx: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#col_block_idx.'
  SoftmaxState: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/SoftmaxState#'
  SoftmaxState.l: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/SoftmaxState#l.'
  KernelArgs.li_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#li_arg.'
  KernelArgs.o_scratch_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#o_scratch_arg.'
  KernelArgs.row_block_idx: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#row_block_idx.'
  KernelArgs.mi_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#mi_arg.'
  SoftmaxState.acc: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/SoftmaxState#acc.'
  KernelArgs: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#'
  KernelArgs.mask_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#mask_arg.'
  MaximumFOp: MaximumFOp#
  KernelArgs.head_idx: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#head_idx.'
  KernelArgs.q_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#q_arg.'
  KernelArgs.lse_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#lse_arg.'
  KernelArgs.batch_idx: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#batch_idx.'
  KernelArgs.k_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#k_arg.'
  KernelArgs.seed_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#seed_arg.'
  KernelArgs.oi_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#oi_arg.'
  KernelArgs.v_arg: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`/KernelArgs#v_arg.'
  CombiningKind: CombiningKind#
---
# Module: [`csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc)

## Classes
### <a id="CombiningKind"></a>`CombiningKind`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc:80`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L80)
- signature: `using mlir::vector::CombiningKind`

### <a id="KernelArgs"></a>`KernelArgs`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc:178`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L178)
- doc: Kernel arguments that are shared by all sub-blocks of a grid step.
- signature: `struct KernelArgs`
- members:
  - <a id="KernelArgs.batch_idx"></a>`batch_idx` — [`L189`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L189)
  - <a id="KernelArgs.col_block_idx"></a>`col_block_idx` — [`L192`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L192)
  - <a id="KernelArgs.head_idx"></a>`head_idx` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L190)
  - <a id="KernelArgs.k_arg"></a>`k_arg` — [`L181`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L181)
  - <a id="KernelArgs.li_arg"></a>`li_arg` — [`L188`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L188)
  - <a id="KernelArgs.lse_arg"></a>`lse_arg` — [`L185`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L185) — Null when LSE is not returned.
  - <a id="KernelArgs.mask_arg"></a>`mask_arg` — [`L183`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L183) — Null when there is no user provided bias.
  - <a id="KernelArgs.mi_arg"></a>`mi_arg` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L187)
  - <a id="KernelArgs.o_scratch_arg"></a>`o_scratch_arg` — [`L186`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L186)
  - <a id="KernelArgs.oi_arg"></a>`oi_arg` — [`L184`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L184)
  - <a id="KernelArgs.q_arg"></a>`q_arg` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L180)
  - <a id="KernelArgs.row_block_idx"></a>`row_block_idx` — [`L191`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L191)
  - <a id="KernelArgs.seed_arg"></a>`seed_arg` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L179) — Null when dropout is disabled.
  - <a id="KernelArgs.v_arg"></a>`v_arg` — [`L182`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L182)
- used by: [`buildModule`](flash_attention_kernel.cc.md#buildModule), [`UpdateSoftmaxState`](flash_attention_kernel.cc.md#UpdateSoftmaxState), [`EmitGridStep`](flash_attention_kernel.cc.md#EmitGridStep), [`StoreNormalizedOutput`](flash_attention_kernel.cc.md#StoreNormalizedOutput), [`ApplyDropoutToProbabilities`](flash_attention_kernel.cc.md#ApplyDropoutToProbabilities)

### <a id="MaximumFOp"></a>`MaximumFOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc:72`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L72)
- signature: `using mlir::arith::MaximumFOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="SoftmaxState"></a>`SoftmaxState`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc:171`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L171)
- doc: The running online-softmax state for a band of query rows.
- signature: `struct SoftmaxState`
- members:
  - <a id="SoftmaxState.acc"></a>`acc` — [`L174`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L174) — [rows, vo_head_dim] f32 unnormalized output.
  - <a id="SoftmaxState.l"></a>`l` — [`L173`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L173) — [rows, 128] f32 running sum.
  - <a id="SoftmaxState.m"></a>`m` — [`L172`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L172) — [rows, 128] f32 running max (log2 domain).
- used by: [`buildModule`](flash_attention_kernel.cc.md#buildModule), [`UpdateSoftmaxState`](flash_attention_kernel.cc.md#UpdateSoftmaxState), [`EmitGridStep`](flash_attention_kernel.cc.md#EmitGridStep), [`StoreNormalizedOutput`](flash_attention_kernel.cc.md#StoreNormalizedOutput), [`ApplyDropoutToProbabilities`](flash_attention_kernel.cc.md#ApplyDropoutToProbabilities)

## Functions
- <a id="ApplyDropoutToProbabilities"></a>`ApplyDropoutToProbabilities(ImplicitLocOpBuilder& b, const FlashAttnConfig& config, const Tiling& tiling, const KernelArgs& args, int64_t row_offset, int64_t col_offset, Value p)` — [`L202`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L202) — Applies PyTorch's inverted dropout to the softmax probabilities `p`: kept
- <a id="CreateKernel"></a>`CreateKernel(MLIRContext* context, const FlashAttnConfig& config, const Tiling& tiling)` — [`L557`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L557) — Creates the flash attention kernel for the given configuration. — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="EmitGridStep"></a>`EmitGridStep(ImplicitLocOpBuilder& b, const FlashAttnConfig& config, const Tiling& tiling, const KernelArgs& args, bool is_single_kv_step, bool has_padding, bool intersects_causal_diag)` — [`L345`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L345) — Emits the compute for one grid step. — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="SetKernelAttributes"></a>`SetKernelAttributes(llvm::ArrayRef<const int64_t> qk_dimensions, const FlashAttnConfig& config, const Tiling& tiling, func::FuncOp fn, OpBuilder& builder)` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L84) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- `SetKernelAttributes(llvm::ArrayRef<const int64_t> qk_dimensions, const FlashAttnConfig& config, const Tiling& tiling, func::FuncOp fn, OpBuilder& builder)` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L84)
- <a id="StoreNormalizedOutput"></a>`StoreNormalizedOutput(ImplicitLocOpBuilder& b, const FlashAttnConfig& config, const KernelArgs& args, const SoftmaxState& state, int64_t row_offset)` — [`L298`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L298) — Normalizes the accumulated output for the query rows starting at
- <a id="UpdateSoftmaxState"></a>`UpdateSoftmaxState(ImplicitLocOpBuilder& b, const FlashAttnConfig& config, const Tiling& tiling, const KernelArgs& args, Value q, int64_t row_offset, int64_t rows, int64_t col_offset, int64_t kc, bool apply_masking, const std::optional<SoftmaxState>& prev)` — [`L224`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L224) — Folds the [rows, kc] logits sub-block at (row_offset, col_offset) of the — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- `buildModule(ImplicitLocOpBuilder& module_builder, const FlashAttnConfig& config, const Tiling& tiling)` — [`L401`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L401) — q [batch_size, num_heads, q_seq_len, d_model]
- <a id="buildModule"></a>`buildModule(ImplicitLocOpBuilder& module_builder, const FlashAttnConfig& config, const Tiling& tiling)` — [`L401`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_kernel.cc#L401) — q [batch_size, num_heads, q_seq_len, d_model] — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)

