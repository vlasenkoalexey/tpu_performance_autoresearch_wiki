---
title: 'Module: csrc/ops/linalg/qr/qr_lib.cc'
type: catalog
provenance: extracted
module: csrc/ops/linalg/qr/qr_lib.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildQrShlo: BuildQrShlo(203298a750ae3a11).
  BuildEmptyQrShlo: '`$anonymous_namespace_csrc/ops/linalg/qr/qr_lib.cc`/BuildEmptyQrShlo(6826c7de997292a1).'
  BuildGeqrfShlo: BuildGeqrfShlo(456e4eb919dc3e8d).
  BuildTriuShlo: '`$anonymous_namespace_csrc/ops/linalg/qr/qr_lib.cc`/BuildTriuShlo(c108f29ac8b2284d).'
  BuildPadShlo: '`$anonymous_namespace_csrc/ops/linalg/qr/qr_lib.cc`/BuildPadShlo(a1fcae8f74484247).'
  BuildHouseholderProductCustomCallOp: '`$anonymous_namespace_csrc/ops/linalg/qr/qr_lib.cc`/BuildHouseholderProductCustomCallOp(3fb20af30da297dc).'
  BuildGeqrfCustomCallOp: '`$anonymous_namespace_csrc/ops/linalg/qr/qr_lib.cc`/BuildGeqrfCustomCallOp(30a389985540f2c1).'
  ConcatBatchAndMatrixDims: '`$anonymous_namespace_csrc/ops/linalg/qr/qr_lib.cc`/ConcatBatchAndMatrixDims(86a56f124544068f).'
  BuildCustomCallOp: '`$anonymous_namespace_csrc/ops/linalg/qr/qr_lib.cc`/BuildCustomCallOp(da7e807e8e1a7856).'
---
# Module: [`csrc/ops/linalg/qr/qr_lib.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc)

## Functions
- <a id="BuildCustomCallOp"></a>`BuildCustomCallOp(mlir::MlirBuilder& builder, llvm::StringRef call_target_name, llvm::ArrayRef<mlir::Type> result_types, llvm::ArrayRef<mlir::Value> operands)` — [`L43`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L43)
- `BuildCustomCallOp(mlir::MlirBuilder& builder, llvm::StringRef call_target_name, llvm::ArrayRef<mlir::Type> result_types, llvm::ArrayRef<mlir::Value> operands)` — [`L43`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L43)
- `BuildEmptyQrShlo(mlir::MlirBuilder& builder, mlir::ElementType element_type, int64_t m, int64_t n, bool full_matrices, llvm::ArrayRef<int64_t> batch_dims, c10::string_view mode)` — [`L94`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L94)
- <a id="BuildEmptyQrShlo"></a>`BuildEmptyQrShlo(mlir::MlirBuilder& builder, mlir::ElementType element_type, int64_t m, int64_t n, bool full_matrices, llvm::ArrayRef<int64_t> batch_dims, c10::string_view mode)` — [`L94`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L94)
- <a id="BuildGeqrfCustomCallOp"></a>`BuildGeqrfCustomCallOp(mlir::MlirOp& input, mlir::RankedTensorType out_a_type, mlir::RankedTensorType tau_type)` — [`L63`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L63)
- `BuildGeqrfCustomCallOp(mlir::MlirOp& input, mlir::RankedTensorType out_a_type, mlir::RankedTensorType tau_type)` — [`L63`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L63)
- <a id="BuildGeqrfShlo"></a>`BuildGeqrfShlo(mlir::MlirOp input)` — [`L171`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L171) — Generates StableHLO for "geqrf" using the XLA "Qr" custom call.
- `BuildGeqrfShlo(mlir::MlirOp input)` — [`L171`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L171) — Generates StableHLO for "geqrf" using the XLA "Qr" custom call.
- <a id="BuildHouseholderProductCustomCallOp"></a>`BuildHouseholderProductCustomCallOp(mlir::MlirOp& input, mlir::MlirOp& tau, mlir::RankedTensorType out_type)` — [`L75`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L75)
- <a id="BuildPadShlo"></a>`BuildPadShlo(mlir::MlirOp input, mlir::MlirOp padding_value, llvm::ArrayRef<int64_t> edge_padding_high)` — [`L123`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L123)
- <a id="BuildQrShlo"></a>`BuildQrShlo(mlir::MlirOp input, c10::string_view mode)` — [`L203`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L203) — Generates StableHLO for QR decomposition using the XLA
- `BuildQrShlo(mlir::MlirOp input, c10::string_view mode)` — [`L203`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L203) — Generates StableHLO for QR decomposition using the XLA
- <a id="BuildTriuShlo"></a>`BuildTriuShlo(mlir::MlirOp input, mlir::ElementType element_type, int64_t m, int64_t n)` — [`L133`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L133)
- <a id="ConcatBatchAndMatrixDims"></a>`ConcatBatchAndMatrixDims(llvm::ArrayRef<int64_t> batch_dims, int64_t m, int64_t n)` — [`L86`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L86)
- `ConcatBatchAndMatrixDims(llvm::ArrayRef<int64_t> batch_dims, int64_t m, int64_t n)` — [`L86`](../../../../../../../../raw/code/torch_tpu/csrc/ops/linalg/qr/qr_lib.cc#L86)

