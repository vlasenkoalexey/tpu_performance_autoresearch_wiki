---
title: 'Module: csrc/ops/linalg/linalg_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/linalg/linalg_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLinalgSolveExOut: AtenLinalgSolveExOut(85527aa8bfe9141).
  AtenLinalgInvExInverse: AtenLinalgInvExInverse(8ed1043a3f738d71).
---
# Module: [`csrc/ops/linalg/linalg_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_kernels.cc)

## Functions
- <a id="AtenLinalgInvExInverse"></a>`AtenLinalgInvExInverse(const at::Tensor& a, bool check_errors, at::Tensor& inverse, at::Tensor& info)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_kernels.cc#L100) — Computes inverse of a matrix or batch of matrices `A`.
- <a id="AtenLinalgSolveExOut"></a>`AtenLinalgSolveExOut(const at::Tensor& a, const at::Tensor& b, bool left, bool check_errors, at::Tensor& result, at::Tensor& lu, at::Tensor& pivots, at::Tensor& info)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_kernels.cc#L42) — Solves a system of linear equations and returns solution,

