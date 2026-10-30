---
title: 'Module: csrc/ops/copy_from/cpu_to_tpu.cc'
type: catalog
provenance: extracted
module: csrc/ops/copy_from/cpu_to_tpu.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CopyCpuToTpu: CopyCpuToTpu(65a4a3a9c76762c1).
  CopyCpuToTpuBuffer: CopyCpuToTpuBuffer(74fc63197b9a619f).
---
# Module: [`csrc/ops/copy_from/cpu_to_tpu.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/cpu_to_tpu.cc)

## Functions
- <a id="CopyCpuToTpu"></a>`CopyCpuToTpu(const at::Tensor& src, const at::Tensor& dest, bool non_blocking)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/cpu_to_tpu.cc#L61) — Copies the value out of the source CPU tensor and assigns it to the — documented in [host-device-copy](../../../../concepts/host-device-copy.md)
- <a id="CopyCpuToTpuBuffer"></a>`CopyCpuToTpuBuffer(const at::Tensor& src, bool non_blocking)` — [`L38`](../../../../../../../raw/code/torch_tpu/csrc/ops/copy_from/cpu_to_tpu.cc#L38) — Copies the value out of the source CPU tensor to a materialized — documented in [host-device-copy](../../../../concepts/host-device-copy.md)

