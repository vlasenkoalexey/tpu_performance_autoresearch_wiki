---
title: 'Module: csrc/experimental/precompiled_kernels/mosaic_custom_call.cc'
type: catalog
provenance: extracted
module: csrc/experimental/precompiled_kernels/mosaic_custom_call.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildMosaicCustomCall: BuildMosaicCustomCall(c91ff417e8f6c324).
  SerializeMosaic: '`$anonymous_namespace_csrc/experimental/precompiled_kernels/mosaic_custom_call.cc`/SerializeMosaic(80803442a742f742).'
---
# Module: [`csrc/experimental/precompiled_kernels/mosaic_custom_call.cc`](../../../../../../../raw/code/torch_tpu/csrc/experimental/precompiled_kernels/mosaic_custom_call.cc)

## Functions
- <a id="BuildMosaicCustomCall"></a>`BuildMosaicCustomCall(mlir::ModuleOp kernel, absl::Span<const xla::Shape> parameters, const xla::Shape& result, absl::Span<const int64_t> operand_to_metadata, int aliased_parameter)` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/experimental/precompiled_kernels/mosaic_custom_call.cc#L64) — Serializes the module in place and wraps it in one scheduled custom call. — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)
- <a id="SerializeMosaic"></a>`SerializeMosaic(mlir::ModuleOp module)` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/experimental/precompiled_kernels/mosaic_custom_call.cc#L46) — documented in [batch-host-device-transfer](../../../../concepts/batch-host-device-transfer.md)

