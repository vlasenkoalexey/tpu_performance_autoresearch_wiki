---
title: 'Module: csrc/ops/linalg/linalg_svd_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/linalg/linalg_svd_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLinalgSvdU: AtenLinalgSvdU(1681e6eb192b7594).
  BuildQdwhShlo: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildQdwhShlo(edfc09f64e3669c3).'
  Svd: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/Svd(312f072155cf733f).'
  BuildQdwhLoopBody: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildQdwhLoopBody(45e4a52db0c1b99).'
  BuildSvdShlo: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildSvdShlo(74387a5d64299223).'
  BuildSvdTallAndSquare: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildSvdTallAndSquare(e5e3f331dac45f6e).'
  BuildQdwhConvergenceCheck: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildQdwhConvergenceCheck(ca0aa3fea17ac50c).'
  BuildEighWithDiagonalShift: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildEighWithDiagonalShift(456e4eb919dc3e8d).'
  BuildQdwhIterationQR: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildQdwhIterationQR(ac48754f9fea6edd).'
  BuildCheckRankDeficiency: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildCheckRankDeficiency(201b5272288a245a).'
  BuildQrCorrectedSigns: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildQrCorrectedSigns(9d00322735e95b13).'
  BuildQdwhIterationCholesky: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildQdwhIterationCholesky(ac48754f9fea6edd).'
  UpcastComplexDoubleOutputs: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/UpcastComplexDoubleOutputs(508dc10fa5ed0f43).'
  HandleEmptyInputSvd: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/HandleEmptyInputSvd(d2b18ecb4cf182a0).'
  DowncastFromComplexDouble: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/DowncastFromComplexDouble(cd958efedc17238).'
  BuildGetDiagonal: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildGetDiagonal(a7867b6222e713f9).'
  BuildDiagonalShiftMatrix: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildDiagonalShiftMatrix(33f52a735f987286).'
  BuildRecoverSingularValues: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildRecoverSingularValues(9dd408ac7de815bd).'
  BuildSortEigenPairs: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildSortEigenPairs(a61f55de01622fcd).'
  BuildQdwhInitialScaling: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildQdwhInitialScaling(a7867b6222e713f9).'
  PropagateNanIfNeeded: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/PropagateNanIfNeeded(9dd408ac7de815bd).'
  BuildEighShlo: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildEighShlo(bbde92ba6b04e6b).'
  BuildScaleTensor: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildScaleTensor(9dd408ac7de815bd).'
  BuildNewtonSchulzRefinement: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildNewtonSchulzRefinement(c116150205aa322e).'
  BuildHermitianFactor: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildHermitianFactor(4e058530975e9b5a).'
  BuildAllFinite: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildAllFinite(a7867b6222e713f9).'
  BuildBatchedEye: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildBatchedEye(f5b2f24263856e2).'
  BuildConjugateTransposeShlo: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildConjugateTransposeShlo(a7867b6222e713f9).'
  BuildSvdPreprocess: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildSvdPreprocess(ba522e98b36b08f3).'
  BuildMatrix1Norm: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildMatrix1Norm(a7867b6222e713f9).'
  BuildMatrixInfNorm: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildMatrixInfNorm(a7867b6222e713f9).'
  BuildCorrectRankDeficiency: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildCorrectRankDeficiency(4e058530975e9b5a).'
  UpcastToComplexDouble: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/UpcastToComplexDouble(c5514e0230fe3804).'
  UpcastToDouble: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/UpcastToDouble(c5514e0230fe3804).'
  BuildSvdPostprocess: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildSvdPostprocess(6f685434e2dd1080).'
  BuildSvdUReconstruction: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildSvdUReconstruction(49b374079ee0da3c).'
  GetOutDtype: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/GetOutDtype(afbb217a7cdbf13a).'
  BuildQdwhBranch: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildQdwhBranch(a0ffeeb3c527af3e).'
  BuildMaxReduction: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildMaxReduction(6696ef0d66c99f43).'
  BuildTransposeShlo: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildTransposeShlo(a7867b6222e713f9).'
  BuildMatMulShlo: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildMatMulShlo(9dd408ac7de815bd).'
  ConvertToComplexIfNeeded: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/ConvertToComplexIfNeeded(9dd408ac7de815bd).'
  MakeEmptySlice: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/MakeEmptySlice(32e5625f5d56765e).'
  BuildIsFiniteShlo: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildIsFiniteShlo(a7867b6222e713f9).'
  BuildSafeAlphaInverse: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildSafeAlphaInverse(9dd408ac7de815bd).'
  BuildNanLike: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildNanLike(a7867b6222e713f9).'
  BuildSliceLastDimension: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildSliceLastDimension(1d9fc30246b9c9cd).'
  ConcatBatchAndDims: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/ConcatBatchAndDims(25ad42c1a3d80817).'
  BroadcastScalar: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BroadcastScalar(b250076e9d5d164a).'
  BuildTriangularSolveShlo: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildTriangularSolveShlo(69563b3fafc3cd5e).'
  GetSvdOutDims: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/GetSvdOutDims(b280ae8bf2b0048d).'
  GetScalarAtIndex: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/GetScalarAtIndex(6fb228fd2a36be37).'
  MaybeCastInput: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/MaybeCastInput(305148ce2b3e1423).'
  BuildCustomCallOp: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/BuildCustomCallOp(bcfb2f2fa9ad755b).'
  StablehloTranspose: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/StablehloTranspose#'
  GetEpsilon: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/GetEpsilon(1da28fdfc09cd382).'
  kCastDtypeForIntegerInput: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/kCastDtypeForIntegerInput.'
  SvdOutDims: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdOutDims#'
  SvdPreprocessResult.u_out_null: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdPreprocessResult#u_out_null.'
  SvdPostprocessResult.vh: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdPostprocessResult#vh.'
  ComputeQdwhCoefs: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/ComputeQdwhCoefs(a38f2c597ea5332e).'
  QdwhLoopOptions.use_chol_consts: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#use_chol_consts.'
  DiagonalShiftResult.delta: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/DiagonalShiftResult#delta.'
  SvdPreprocessResult: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdPreprocessResult#'
  SvdOutDims.vh: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdOutDims#vh.'
  SvdOutDims.s: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdOutDims#s.'
  SvdPostprocessResult: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdPostprocessResult#'
  QdwhLoopOptions: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#'
  DiagonalShiftResult: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/DiagonalShiftResult#'
  SvdOutDims.u: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdOutDims#u.'
  QdwhLoopOptions.rank: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#rank.'
  QdwhLoopOptions.a_consts: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#a_consts.'
  SvdPreprocessResult.q_op: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdPreprocessResult#q_op.'
  DiagonalShiftResult.shift_matrix: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/DiagonalShiftResult#shift_matrix.'
  QdwhLoopOptions.c_consts: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#c_consts.'
  QdwhLoopOptions.b_consts: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#b_consts.'
  QdwhCoefs.use_cholesky: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhCoefs#use_cholesky.'
  SvdPreprocessResult.a_svd: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdPreprocessResult#a_svd.'
  SvdPostprocessResult.u: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/SvdPostprocessResult#u.'
  QdwhLoopOptions.element_type: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#element_type.'
  QdwhCoefs: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhCoefs#'
  QdwhLoopOptions.tolerance: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#tolerance.'
  QdwhLoopOptions.batch_shape: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhLoopOptions#batch_shape.'
  QdwhCoefs.a: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhCoefs#a.'
  QdwhCoefs.b: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhCoefs#b.'
  QdwhCoefs.c: '`$anonymous_namespace_csrc/ops/linalg/linalg_svd_kernels.cc`/QdwhCoefs#c.'
---
# Module: [`csrc/ops/linalg/linalg_svd_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc)

## Classes
### <a id="DiagonalShiftResult"></a>`DiagonalShiftResult`
- def: [`csrc/ops/linalg/linalg_svd_kernels.cc:1237`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1237)
- signature: `struct DiagonalShiftResult`
- members:
  - <a id="DiagonalShiftResult.delta"></a>`delta` — [`L1239`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1239)
  - <a id="DiagonalShiftResult.shift_matrix"></a>`shift_matrix` — [`L1238`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1238)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildEighWithDiagonalShift`](linalg_svd_kernels.cc.md#BuildEighWithDiagonalShift), [`BuildDiagonalShiftMatrix`](linalg_svd_kernels.cc.md#BuildDiagonalShiftMatrix)

### <a id="QdwhCoefs"></a>`QdwhCoefs`
- def: [`csrc/ops/linalg/linalg_svd_kernels.cc:211`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L211)
- doc: Coefficients for the QDWH (QR-based Dynamically Weighted Halley) iteration.
- signature: `struct QdwhCoefs`
- members:
  - <a id="QdwhCoefs.a"></a>`a` — [`L213`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L213) — Coefficient 'a' used in the Halley iteration formula.
  - <a id="QdwhCoefs.b"></a>`b` — [`L215`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L215) — Coefficient 'b' used to compute the scaling factor e = b / c.
  - <a id="QdwhCoefs.c"></a>`c` — [`L217`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L217) — Coefficient 'c' used in the denominator of the Halley iteration.
  - <a id="QdwhCoefs.use_cholesky"></a>`use_cholesky` — [`L224`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L224) — Indicates whether to use Cholesky decomposition (1) or QR decomposition (0)
- used by: [`BuildQdwhShlo`](linalg_svd_kernels.cc.md#BuildQdwhShlo)

### <a id="QdwhLoopOptions"></a>`QdwhLoopOptions`
- def: [`csrc/ops/linalg/linalg_svd_kernels.cc:646`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L646)
- doc: Config options and precomputed constants for the QDWH loop body.
- signature: `struct QdwhLoopOptions`
- members:
  - <a id="QdwhLoopOptions.a_consts"></a>`a_consts` — [`L656`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L656) — Precomputed 'a' coefficients.
  - <a id="QdwhLoopOptions.b_consts"></a>`b_consts` — [`L658`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L658) — Precomputed 'b' coefficients.
  - <a id="QdwhLoopOptions.batch_shape"></a>`batch_shape` — [`L652`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L652) — The shape of the batch dimensions of the input tensor.
  - <a id="QdwhLoopOptions.c_consts"></a>`c_consts` — [`L660`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L660) — Precomputed 'c' coefficients.
  - <a id="QdwhLoopOptions.element_type"></a>`element_type` — [`L648`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L648) — The element type of the matrix being processed.
  - <a id="QdwhLoopOptions.rank"></a>`rank` — [`L654`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L654) — The rank of the input tensor.
  - <a id="QdwhLoopOptions.tolerance"></a>`tolerance` — [`L650`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L650) — Tolerance value used to determine convergence of the iteration.
  - <a id="QdwhLoopOptions.use_chol_consts"></a>`use_chol_consts` — [`L662`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L662) — Precomputed boolean flags indicating whether to use Cholesky iteration.
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildQdwhShlo`](linalg_svd_kernels.cc.md#BuildQdwhShlo), [`BuildQdwhLoopBody`](linalg_svd_kernels.cc.md#BuildQdwhLoopBody), [`BuildQdwhConvergenceCheck`](linalg_svd_kernels.cc.md#BuildQdwhConvergenceCheck)

### <a id="StablehloTranspose"></a>`StablehloTranspose`
- def: [`csrc/ops/linalg/linalg_svd_kernels.cc:82`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L82)
- doc: Disambiguate the `Transpose` enum from the free `Transpose` op builder
- signature: `using StablehloTranspose = enum mlir::stablehlo::Transpose`
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`BuildQdwhIterationCholesky`](linalg_svd_kernels.cc.md#BuildQdwhIterationCholesky), [`BuildTriangularSolveShlo`](linalg_svd_kernels.cc.md#BuildTriangularSolveShlo)

### <a id="SvdOutDims"></a>`SvdOutDims`
- def: [`csrc/ops/linalg/linalg_svd_kernels.cc:1472`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1472)
- signature: `struct SvdOutDims`
- members:
  - <a id="SvdOutDims.s"></a>`s` — [`L1474`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1474)
  - <a id="SvdOutDims.u"></a>`u` — [`L1473`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1473)
  - <a id="SvdOutDims.vh"></a>`vh` — [`L1475`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1475)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`AtenLinalgSvdU`](linalg_svd_kernels.cc.md#AtenLinalgSvdU), [`Svd`](linalg_svd_kernels.cc.md#Svd), [`UpcastComplexDoubleOutputs`](linalg_svd_kernels.cc.md#UpcastComplexDoubleOutputs)

### <a id="SvdPostprocessResult"></a>`SvdPostprocessResult`
- def: [`csrc/ops/linalg/linalg_svd_kernels.cc:1020`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1020)
- signature: `struct SvdPostprocessResult`
- members:
  - <a id="SvdPostprocessResult.u"></a>`u` — [`L1021`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1021)
  - <a id="SvdPostprocessResult.vh"></a>`vh` — [`L1022`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1022)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildSvdShlo`](linalg_svd_kernels.cc.md#BuildSvdShlo), [`BuildSvdPostprocess`](linalg_svd_kernels.cc.md#BuildSvdPostprocess)

### <a id="SvdPreprocessResult"></a>`SvdPreprocessResult`
- def: [`csrc/ops/linalg/linalg_svd_kernels.cc:956`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L956)
- signature: `struct SvdPreprocessResult`
- members:
  - <a id="SvdPreprocessResult.a_svd"></a>`a_svd` — [`L957`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L957)
  - <a id="SvdPreprocessResult.q_op"></a>`q_op` — [`L958`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L958)
  - <a id="SvdPreprocessResult.u_out_null"></a>`u_out_null` — [`L959`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L959)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildSvdShlo`](linalg_svd_kernels.cc.md#BuildSvdShlo), [`BuildSvdPreprocess`](linalg_svd_kernels.cc.md#BuildSvdPreprocess)

## Functions
- <a id="AtenLinalgSvdU"></a>`AtenLinalgSvdU(const at::Tensor& self, bool full_matrices, bool compute_uv, std::optional<c10::string_view> driver, at::Tensor& u, at::Tensor& s, at::Tensor& vh)` — [`L1634`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1634) — Computes the singular value decomposition (SVD) of a matrix or batch of
- <a id="BroadcastScalar"></a>`BroadcastScalar(mlir::MlirOp scalar, llvm::ArrayRef<int64_t> target_shape)` — [`L329`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L329)
- <a id="BuildAllFinite"></a>`BuildAllFinite(mlir::MlirOp input)` — [`L1374`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1374) — Returns a boolean tensor of shape (batch_shape) indicating if all elements
- <a id="BuildBatchedEye"></a>`BuildBatchedEye(mlir::MlirBuilder& builder, mlir::ElementType element_type, int64_t n, llvm::ArrayRef<int64_t> batch_shape)` — [`L362`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L362) — Helper to construct Eye(N) and broadcast to (batch_dims..., N, N)
- <a id="BuildCheckRankDeficiency"></a>`BuildCheckRankDeficiency(mlir::MlirOp s_sorted, absl::Span<const int64_t> batch_shape, mlir::ElementType element_type)` — [`L1153`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1153) — Checks if the matrix is rank-deficient using the formula:
- <a id="BuildConjugateTransposeShlo"></a>`BuildConjugateTransposeShlo(mlir::MlirOp op)` — [`L107`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L107)
- <a id="BuildCorrectRankDeficiency"></a>`BuildCorrectRankDeficiency(mlir::MlirOp u_svd, mlir::MlirOp s_sorted, const mlir::ElementType element_type)` — [`L1196`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1196)
- <a id="BuildCustomCallOp"></a>`BuildCustomCallOp(mlir::MlirBuilder& builder, llvm::StringRef call_target_name, llvm::ArrayRef<mlir::Type> result_types, llvm::ArrayRef<mlir::Value> operands, llvm::StringRef backend_config = "")` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L130)
- `BuildCustomCallOp(mlir::MlirBuilder& builder, llvm::StringRef call_target_name, llvm::ArrayRef<mlir::Type> result_types, llvm::ArrayRef<mlir::Value> operands, llvm::StringRef backend_config = "")` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L130)
- <a id="BuildDiagonalShiftMatrix"></a>`BuildDiagonalShiftMatrix(mlir::MlirOp h_norm, mlir::ElementType element_type, llvm::ArrayRef<int64_t> shape)` — [`L1244`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1244) — Constructs a batched diagonal shift matrix delta * I of shape `shape`,
- `BuildEighShlo(mlir::MlirOp input)` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L157)
- <a id="BuildEighShlo"></a>`BuildEighShlo(mlir::MlirOp input)` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L157)
- `BuildEighWithDiagonalShift(mlir::MlirOp h)` — [`L1292`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1292) — Regularizes H with a diagonal shift: H_reg = H + delta * I, to prevent NaNs
- <a id="BuildEighWithDiagonalShift"></a>`BuildEighWithDiagonalShift(mlir::MlirOp h)` — [`L1292`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1292) — Regularizes H with a diagonal shift: H_reg = H + delta * I, to prevent NaNs
- <a id="BuildGetDiagonal"></a>`BuildGetDiagonal(mlir::MlirOp op)` — [`L1051`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1051) — Extracts the diagonal elements of a (..., N, N) tensor to (..., N).
- <a id="BuildHermitianFactor"></a>`BuildHermitianFactor(mlir::MlirOp u_refined, mlir::MlirOp input, mlir::ElementType element_type)` — [`L609`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L609)
- <a id="BuildIsFiniteShlo"></a>`BuildIsFiniteShlo(mlir::MlirOp input)` — [`L1357`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1357) — Returns an element-wise boolean mask indicating which elements of the input
- <a id="BuildMatMulShlo"></a>`BuildMatMulShlo(mlir::MlirOp lhs, mlir::MlirOp rhs)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L112)
- <a id="BuildMatrix1Norm"></a>`BuildMatrix1Norm(mlir::MlirOp x)` — [`L307`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L307) — Computes the maximum absolute column sum (1-norm) of a matrix, preserving
- <a id="BuildMatrixInfNorm"></a>`BuildMatrixInfNorm(mlir::MlirOp x)` — [`L319`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L319) — Computes the maximum absolute row sum (inf-norm) of a matrix, preserving
- <a id="BuildMaxReduction"></a>`BuildMaxReduction(mlir::MlirOp input, absl::Span<const int64_t> dims)` — [`L293`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L293) — Computes the maximum reduction along specified dimensions.
- <a id="BuildNanLike"></a>`BuildNanLike(mlir::MlirOp op)` — [`L1384`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1384) — Returns a tensor of the same shape and type as the input, but filled with NaN
- <a id="BuildNewtonSchulzRefinement"></a>`BuildNewtonSchulzRefinement(mlir::MlirOp u, mlir::ElementType element_type)` — [`L590`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L590) — Applies Newton-Schulz refinement to the polar factor U:
- <a id="BuildQdwhBranch"></a>`BuildQdwhBranch(mlir::MlirBuilder& parent_builder, mlir::Region& branch_region, mlir::MlirOp parent_u, mlir::MlirOp parent_e, mlir::MlirOp parent_a_minus_e, mlir::MlirOp parent_c, IterationFn iteration_fn)` — [`L628`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L628)
- <a id="BuildQdwhConvergenceCheck"></a>`BuildQdwhConvergenceCheck(mlir::MlirBuilder& builder, mlir::MlirOp parent_u_next, mlir::MlirOp parent_u_current, mlir::MlirOp parent_active_mask, mlir::MlirOp use_cholesky, const QdwhLoopOptions& options)` — [`L667`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L667) — Checks convergence by comparing the norm of the difference between successive
- <a id="BuildQdwhInitialScaling"></a>`BuildQdwhInitialScaling(mlir::MlirOp input)` — [`L562`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L562) — Calculates the scaling factor:
- <a id="BuildQdwhIterationCholesky"></a>`BuildQdwhIterationCholesky(mlir::MlirOp u, mlir::MlirOp e, mlir::MlirOp a_minus_e, mlir::MlirOp c)` — [`L458`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L458) — Performs a single QDWH iteration step using Cholesky decomposition.
- <a id="BuildQdwhIterationQR"></a>`BuildQdwhIterationQR(mlir::MlirOp u, mlir::MlirOp e, mlir::MlirOp a_minus_e, mlir::MlirOp c)` — [`L384`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L384) — Performs a single QDWH iteration step using QR decomposition.
- `BuildQdwhLoopBody(mlir::RegionBuilder& region_builder, mlir::MlirOp i_op, mlir::MlirOp u_op, mlir::MlirOp active_mask, const QdwhLoopOptions& options)` — [`L744`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L744) — Builds the body of the QDWH convergence loop.
- <a id="BuildQdwhLoopBody"></a>`BuildQdwhLoopBody(mlir::RegionBuilder& region_builder, mlir::MlirOp i_op, mlir::MlirOp u_op, mlir::MlirOp active_mask, const QdwhLoopOptions& options)` — [`L744`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L744) — Builds the body of the QDWH convergence loop.
- `BuildQdwhShlo(mlir::MlirOp input, int64_t max_iterations, std::optional<double> epsilon = std::nullopt)` — [`L793`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L793)
- <a id="BuildQdwhShlo"></a>`BuildQdwhShlo(mlir::MlirOp input, int64_t max_iterations, std::optional<double> epsilon = std::nullopt)` — [`L793`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L793)
- <a id="BuildQrCorrectedSigns"></a>`BuildQrCorrectedSigns(mlir::MlirOp u_svd_rb, const mlir::Type& real_mlir_type)` — [`L1091`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1091) — Computes QR decomposition and returns Q with corrected column signs.
- <a id="BuildRecoverSingularValues"></a>`BuildRecoverSingularValues(mlir::MlirOp s_reg, mlir::MlirOp delta)` — [`L1275`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1275) — Recovers unshifted singular values by subtracting delta from the regularized
- <a id="BuildSafeAlphaInverse"></a>`BuildSafeAlphaInverse(mlir::MlirOp one_norm, mlir::MlirOp alpha_inverse)` — [`L547`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L547) — If the input norm is zero, returns 1.0. Otherwise, returns alpha_inverse.
- <a id="BuildScaleTensor"></a>`BuildScaleTensor(mlir::MlirOp tensor, mlir::MlirOp scale)` — [`L334`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L334)
- <a id="BuildSliceLastDimension"></a>`BuildSliceLastDimension(mlir::MlirOp op, int64_t start, int64_t end)` — [`L1131`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1131) — Slices the input tensor along its last dimension from start to end.
- <a id="BuildSortEigenPairs"></a>`BuildSortEigenPairs(mlir::MlirOp s, mlir::MlirOp v, mlir::ElementType element_type)` — [`L934`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L934)
- `BuildSortEigenPairs(mlir::MlirOp s, mlir::MlirOp v, mlir::ElementType element_type)` — [`L934`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L934)
- <a id="BuildSvdPostprocess"></a>`BuildSvdPostprocess(mlir::MlirOp u_svd, mlir::MlirOp v_sorted, bool transpose_input)` — [`L1026`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1026) — Postprocesses SVD outputs by swapping U and V if the input was transposed.
- <a id="BuildSvdPreprocess"></a>`BuildSvdPreprocess(mlir::MlirOp a, bool full_matrices)` — [`L965`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L965) — If complete QR is requested (full_matrices=true and m > n), performs complete
- <a id="BuildSvdShlo"></a>`BuildSvdShlo(mlir::MlirOp input, bool full_matrices, bool compute_uv)` — [`L1414`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1414)
- `BuildSvdShlo(mlir::MlirOp input, bool full_matrices, bool compute_uv)` — [`L1414`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1414)
- <a id="BuildSvdTallAndSquare"></a>`BuildSvdTallAndSquare(mlir::MlirOp input, bool compute_uv)` — [`L1312`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1312)
- `BuildSvdTallAndSquare(mlir::MlirOp input, bool compute_uv)` — [`L1312`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1312)
- <a id="BuildSvdUReconstruction"></a>`BuildSvdUReconstruction(mlir::MlirOp u_svd, std::optional<mlir::MlirOp> q_op, std::optional<mlir::MlirOp> u_out_null)` — [`L1002`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1002) — Reconstructs the final U matrix from the SVD of the preprocessed matrix.
- <a id="BuildTransposeShlo"></a>`BuildTransposeShlo(mlir::MlirOp op)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L91)
- `BuildTriangularSolveShlo(mlir::MlirOp a, mlir::MlirOp b, bool left_side, bool lower, StablehloTranspose transpose_a, bool unit_diagonal)` — [`L346`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L346) — Helper to construct stablehlo::TriangularSolveOp.
- <a id="BuildTriangularSolveShlo"></a>`BuildTriangularSolveShlo(mlir::MlirOp a, mlir::MlirOp b, bool left_side, bool lower, StablehloTranspose transpose_a, bool unit_diagonal)` — [`L346`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L346) — Helper to construct stablehlo::TriangularSolveOp.
- <a id="ComputeQdwhCoefs"></a>`ComputeQdwhCoefs(double epsilon, int64_t max_iterations)` — [`L231`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L231) — Precomputes the QDWH coefficients. This matches JAX's behavior which also
- <a id="ConcatBatchAndDims"></a>`ConcatBatchAndDims(const T& batch_dims, Dims... dims)` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L85)
- <a id="ConvertToComplexIfNeeded"></a>`ConvertToComplexIfNeeded(mlir::MlirOp scalar, mlir::MlirOp target)` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L187)
- <a id="DowncastFromComplexDouble"></a>`DowncastFromComplexDouble(const at::Tensor& self)` — [`L1495`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1495)
- <a id="GetEpsilon"></a>`GetEpsilon(mlir::ElementType type)` — [`L531`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L531) — Returns the epsilon for a given floating-point element type.
- <a id="GetOutDtype"></a>`GetOutDtype(const at::Tensor& self)` — [`L907`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L907)
- <a id="GetScalarAtIndex"></a>`GetScalarAtIndex(mlir::MlirBuilder& builder, mlir::MlirOp consts, mlir::MlirOp index, mlir::Type mlir_type)` — [`L278`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L278) — Extracts a scalar (0-rank) tensor from a 1D tensor of coefficients at a
- <a id="GetSvdOutDims"></a>`GetSvdOutDims(const at::Tensor& self, bool full_matrices, bool compute_uv)` — [`L1478`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1478)
- <a id="HandleEmptyInputSvd"></a>`HandleEmptyInputSvd(const at::Tensor& self, bool full_matrices, bool compute_uv, at::Tensor& u, at::Tensor& s, at::Tensor& vh)` — [`L1606`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1606)
- <a id="MakeEmptySlice"></a>`MakeEmptySlice(mlir::MlirOp op, int64_t dimension)` — [`L923`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L923) — Returns a slice of the input tensor with size 0 along the specified
- <a id="MaybeCastInput"></a>`MaybeCastInput(mlir::MlirOp self_op, bool input_is_integer)` — [`L912`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L912)
- <a id="PropagateNanIfNeeded"></a>`PropagateNanIfNeeded(mlir::MlirOp output, mlir::MlirOp is_finite)` — [`L1402`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1402) — Conditionally replaces the output tensor with NaNs if the corresponding batch
- <a id="Svd"></a>`Svd(const at::Tensor& self, bool full_matrices, bool compute_uv, OpParamCacheKeys param_keys)` — [`L1571`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1571)
- `Svd(const at::Tensor& self, bool full_matrices, bool compute_uv, OpParamCacheKeys param_keys)` — [`L1571`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1571)
- `UpcastComplexDoubleOutputs(const DeviceBufferRefArray<3>& c64_results, const SvdOutDims& expected_dims, int64_t device_index)` — [`L1554`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1554)
- <a id="UpcastComplexDoubleOutputs"></a>`UpcastComplexDoubleOutputs(const DeviceBufferRefArray<3>& c64_results, const SvdOutDims& expected_dims, int64_t device_index)` — [`L1554`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1554)
- <a id="UpcastToComplexDouble"></a>`UpcastToComplexDouble(const at::Tensor& tensor, const Dimensions& target_dims)` — [`L1520`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1520)
- <a id="UpcastToDouble"></a>`UpcastToDouble(const at::Tensor& tensor, const Dimensions& target_dims)` — [`L1541`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L1541)

## Module values
- <a id="kCastDtypeForIntegerInput"></a>`kCastDtypeForIntegerInput` — [`L905`](../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/linalg_svd_kernels.cc#L905)

