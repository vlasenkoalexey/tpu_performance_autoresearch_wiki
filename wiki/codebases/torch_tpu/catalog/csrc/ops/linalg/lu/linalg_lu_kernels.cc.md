---
title: 'Module: csrc/ops/linalg/lu/linalg_lu_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/linalg/lu/linalg_lu_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLinalgLuSolveOut: AtenLinalgLuSolveOut(f46067ad474d5a57).
  AtenLinalgLuFactorExOut: AtenLinalgLuFactorExOut(8b6913a985ffc187).
  AtenLuUnpackOut: AtenLuUnpackOut(39829d9fc102eca7).
  AtenLinalgLuOut: AtenLinalgLuOut(1fa6cd66a5b14d48).
  ApplyPivotsInPlace: '`$anonymous_namespace_csrc/ops/linalg/lu/linalg_lu_kernels.cc`/ApplyPivotsInPlace(8922c2508dfb613f).'
  ValidateLuSupportedDtype: '`$anonymous_namespace_csrc/ops/linalg/lu/linalg_lu_kernels.cc`/ValidateLuSupportedDtype(fd0458bfc68bb174).'
  LuDecompositionBuilder: '`$anonymous_namespace_csrc/ops/linalg/lu/linalg_lu_kernels.cc`/LuDecompositionBuilder(456e4eb919dc3e8d).'
---
# Module: [`csrc/ops/linalg/lu/linalg_lu_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc)

## Functions
- <a id="ApplyPivotsInPlace"></a>`ApplyPivotsInPlace(at::Tensor& tensor, const at::Tensor& pivots, bool to_rows, bool inverse)` — [`L138`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc#L138) — Applies permutation represented by `pivots` in-place to either rows or
- <a id="AtenLinalgLuFactorExOut"></a>`AtenLinalgLuFactorExOut(const at::Tensor& a, bool pivot, bool check_errors, at::Tensor& lu, at::Tensor& pivots, at::Tensor& info)` — [`L199`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc#L199) — Computes LU factorization of a matrix or batch of matrices `A` using
- <a id="AtenLinalgLuOut"></a>`AtenLinalgLuOut(const at::Tensor& a, bool pivot, at::Tensor& p, at::Tensor& l, at::Tensor& u)` — [`L444`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc#L444) — Computes PLU factorization of a matrix or batch of matrices `A`.
- <a id="AtenLinalgLuSolveOut"></a>`AtenLinalgLuSolveOut(const at::Tensor& lu, const at::Tensor& pivots, const at::Tensor& b, bool left, bool adjoint, at::Tensor& out)` — [`L340`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc#L340) — Solves a system of linear equations given LU factorization of A.
- <a id="AtenLuUnpackOut"></a>`AtenLuUnpackOut(const at::Tensor& lu_data, const at::Tensor& lu_pivots, bool unpack_data, bool unpack_pivots, at::Tensor& p, at::Tensor& l, at::Tensor& u)` — [`L263`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc#L263) — Unpacks LU factorization results into P, L, and U matrices.
- <a id="LuDecompositionBuilder"></a>`LuDecompositionBuilder(mlir::MlirOp input)` — [`L83`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc#L83)
- `LuDecompositionBuilder(mlir::MlirOp input)` — [`L83`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc#L83)
- <a id="ValidateLuSupportedDtype"></a>`ValidateLuSupportedDtype(const at::Tensor& tensor)` — [`L70`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/lu/linalg_lu_kernels.cc#L70)

