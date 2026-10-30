---
title: 'Module: csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenCountNonzeroDimIntList: AtenCountNonzeroDimIntList(c65c0bc6367ce7f5).
  BuildCountNonzeroShlo: '`$anonymous_namespace_csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc`/BuildCountNonzeroShlo(6696ef0d66c99f43).'
---
# Module: [`csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc)

## Functions
- <a id="AtenCountNonzeroDimIntList"></a>`AtenCountNonzeroDimIntList(const at::Tensor& self, at::IntArrayRef dim)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc#L56)
- <a id="BuildCountNonzeroShlo"></a>`BuildCountNonzeroShlo(mlir::MlirOp input_op, absl::Span<const int64_t> reduce_dims)` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/ops/count_nonzero/count_nonzero_aten_kernels.cc#L45) — count_nonzero == sum(self != 0), with the count accumulated in int64.

