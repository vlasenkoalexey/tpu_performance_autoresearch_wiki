---
title: 'Module: csrc/ops/copy_from/tpu_to_tpu.cc'
type: catalog
provenance: extracted
module: csrc/ops/copy_from/tpu_to_tpu.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CopyTpuToTpu: CopyTpuToTpu(b2d6689cde60befb).
  SliceFP4: '`$anonymous_namespace_csrc/ops/copy_from/tpu_to_tpu.cc`/SliceFP4(a7867b6222e713f9).'
  PadFP4: '`$anonymous_namespace_csrc/ops/copy_from/tpu_to_tpu.cc`/PadFP4(a7867b6222e713f9).'
---
# Module: [`csrc/ops/copy_from/tpu_to_tpu.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/tpu_to_tpu.cc)

## Functions
- <a id="CopyTpuToTpu"></a>`CopyTpuToTpu(const at::Tensor& src, const at::Tensor& dest)` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/tpu_to_tpu.cc#L87) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="PadFP4"></a>`PadFP4(mlir::MlirOp input)` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/tpu_to_tpu.cc#L67) — Zero-pads the last dimension to double the size (logical N -> physical 2N). — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="SliceFP4"></a>`SliceFP4(mlir::MlirOp input)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/tpu_to_tpu.cc#L49) — Slices the first half of elements to discard the padding. — documented in [host-device-copy](../../../../concepts/host-device-copy.md)

