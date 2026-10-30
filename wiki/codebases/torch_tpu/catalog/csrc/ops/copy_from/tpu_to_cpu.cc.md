---
title: 'Module: csrc/ops/copy_from/tpu_to_cpu.cc'
type: catalog
provenance: extracted
module: csrc/ops/copy_from/tpu_to_cpu.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CopyTpuToCpu: CopyTpuToCpu(65a4a3a9c76762c1).
  TranslateXlaTensorOomError: '`$anonymous_namespace_csrc/ops/copy_from/tpu_to_cpu.cc`/TranslateXlaTensorOomError(973685755ff6bc1f).'
---
# Module: [`csrc/ops/copy_from/tpu_to_cpu.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/tpu_to_cpu.cc)

## Functions
- <a id="CopyTpuToCpu"></a>`CopyTpuToCpu(const at::Tensor& src, const at::Tensor& dest, bool non_blocking)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/tpu_to_cpu.cc#L77) — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="TranslateXlaTensorOomError"></a>`TranslateXlaTensorOomError(absl::Status status, at::ScalarType elem_type, absl::Span<const int64_t> dims)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/tpu_to_cpu.cc#L55) — Translates a low-level XLA OOM error to an error that is easier to understand — documented in [host-device-copy](../../../../concepts/host-device-copy.md)

