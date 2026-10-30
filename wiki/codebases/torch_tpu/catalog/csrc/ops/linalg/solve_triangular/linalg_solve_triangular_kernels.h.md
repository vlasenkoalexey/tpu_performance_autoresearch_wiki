---
title: 'Module: csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/SolveTriangularOptions#
symbols:
  SolveTriangularOptions.adjoint: adjoint.
  SolveTriangularOptions.upper: upper.
  SolveTriangularOptions.left: left.
  SolveTriangularOptions: ''
  SolveTriangularOptions.unitriangular: unitriangular.
---
# Module: [`csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h)

## Classes
### <a id="SolveTriangularOptions"></a>`SolveTriangularOptions`
- def: [`csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h:25`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h#L25)
- signature: `struct SolveTriangularOptions`
- members:
  - <a id="SolveTriangularOptions.adjoint"></a>`adjoint` — [`L29`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h#L29)
  - <a id="SolveTriangularOptions.left"></a>`left` — [`L27`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h#L27)
  - <a id="SolveTriangularOptions.unitriangular"></a>`unitriangular` — [`L28`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h#L28)
  - <a id="SolveTriangularOptions.upper"></a>`upper` — [`L26`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/solve_triangular/linalg_solve_triangular_kernels.h#L26)
- uses (calls/refs, reference-scoped): [`AtenLinalgSolveTriangular`](linalg_solve_triangular_kernels.cc.md#AtenLinalgSolveTriangular), [`AtenLinalgSolveTriangularOut`](linalg_solve_triangular_kernels.cc.md#AtenLinalgSolveTriangularOut), [`LinalgSolveTriangularBuilder`](linalg_solve_triangular_kernels.cc.md#LinalgSolveTriangularBuilder), [`NAryMlirOpBuilder`](../../op_builder_utils.h.md#NAryMlirOpBuilder), [`LinalgSolveTriangularBuilder`](linalg_solve_triangular_kernels.cc.md#LinalgSolveTriangularBuilder)
- used by: [`LinalgSolveTriangularBuilder`](linalg_solve_triangular_kernels.cc.md#LinalgSolveTriangularBuilder)

