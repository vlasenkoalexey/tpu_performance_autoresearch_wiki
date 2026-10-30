---
title: 'Module: csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc'
type: catalog
provenance: extracted
module: csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PadRealToStatic: PadRealToStatic(9ad86ad167275933).
  BuildPadRealToStaticCustomCall: '`$anonymous_namespace_csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc`/BuildPadRealToStaticCustomCall(501d76eb5b2c0581).'
---
# Module: [`csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc)

## Functions
- <a id="BuildPadRealToStaticCustomCall"></a>`BuildPadRealToStaticCustomCall(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> inputs, llvm::ArrayRef<int64_t> out_dims)` — [`L68`](../../../../../../../../raw/code/torch_tpu/csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc#L68) — Builds the StableHLO PadRealToStatic custom call. — documented in [dynamic-shape-ops](../../../../../concepts/dynamic-shape-ops.md)
- `BuildPadRealToStaticCustomCall(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> inputs, llvm::ArrayRef<int64_t> out_dims)` — [`L68`](../../../../../../../../raw/code/torch_tpu/csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc#L68) — Builds the StableHLO PadRealToStatic custom call.
- <a id="PadRealToStatic"></a>`PadRealToStatic(const at::Tensor& input, at::TensorList runtime_shape, at::IntArrayRef static_shape, c10::List<bool> is_dynamic)` — [`L100`](../../../../../../../../raw/code/torch_tpu/csrc/ops/dynamic/pad_real_to_static/pad_real_to_static.cc#L100) — This op is a torch_tpu custom op for use in torch.compile() mode to pad — documented in [dynamic-shape-ops](../../../../../concepts/dynamic-shape-ops.md)

