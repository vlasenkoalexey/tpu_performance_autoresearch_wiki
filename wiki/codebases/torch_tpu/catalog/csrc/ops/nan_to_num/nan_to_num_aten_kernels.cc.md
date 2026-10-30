---
title: 'Module: csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNanToNumOut: AtenNanToNumOut(560fad51638d0f31).
  BuildNanToNumShlo: '`$anonymous_namespace_csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc`/BuildNanToNumShlo(dbe96a503ca063f5).'
---
# Module: [`csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc)

## Functions
- <a id="AtenNanToNumOut"></a>`AtenNanToNumOut(const at::Tensor& self, std::optional<double> nan, std::optional<double> posinf, std::optional<double> neginf, at::Tensor& out)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc#L115)
- <a id="BuildNanToNumShlo"></a>`BuildNanToNumShlo(mlir::MlirOp input, std::optional<double> nan, std::optional<double> posinf, std::optional<double> neginf)` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/nan_to_num/nan_to_num_aten_kernels.cc#L44) — Lower torch.nan_to_num to StableHLO select and compare chains.

