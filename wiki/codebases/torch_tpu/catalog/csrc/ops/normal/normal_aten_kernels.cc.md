---
title: 'Module: csrc/ops/normal/normal_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/normal/normal_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNormalTensorTensor: AtenNormalTensorTensor(20707e8cdee30d92).
  AtenNormalTensorFloat: AtenNormalTensorFloat(ffa4f03e34d01f32).
  AtenNormal_: AtenNormal_(bb63f3d140094158).
  AtenNormalTensorTensorOut: AtenNormalTensorTensorOut(1c4d73b0421078cd).
  AtenNormalFloatTensor: AtenNormalFloatTensor(df5f41b5425a0c9b).
  AtenNormalTensorFloatOut: AtenNormalTensorFloatOut(b347e6b6fffab572).
  AtenNormalFloatTensorOut: AtenNormalFloatTensorOut(75424b3b5ed5ce02).
  ValidateNormalStdPreconditions: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/ValidateNormalStdPreconditions(ea500e704f590848).'
  ValidateNormalPreconditions: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/ValidateNormalPreconditions(d8359b99282c084c).'
  BuildNormalComplexShlo: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/BuildNormalComplexShlo(fdfe0d94a3b2b3f0).'
  DispatchNormal2: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/DispatchNormal2(255c927ef422688d).'
  DispatchNormal3: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/DispatchNormal3(f93edacd823b1369).'
  BuildNormalRealShlo: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/BuildNormalRealShlo(c1fdb88a1a11bf81).'
  DispatchNormal1: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/DispatchNormal1(4ae8445f94248148).'
  GetNormalFloatTensorBuilder: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/GetNormalFloatTensorBuilder(6a166556ddf60815).'
  GetNormalTensorFloatBuilder: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/GetNormalTensorFloatBuilder(6a166556ddf60815).'
  GetNormalTensorTensorBuilder: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/GetNormalTensorTensorBuilder(63df4cc3a9cf59b8).'
  BuildStandardNormalShlo: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/BuildStandardNormalShlo(359cb5fedc96080e).'
  GetNormalScalarScalarBuilder: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/GetNormalScalarScalarBuilder(d7d04da8eba784ec).'
  DispatchNormal2Out: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/DispatchNormal2Out(ac9c533e9874a61d).'
  DispatchNormal3Out: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/DispatchNormal3Out(c1d30b3d9f150a91).'
  BuildNormalShlo: '`$anonymous_namespace_csrc/ops/normal/normal_aten_kernels.cc`/BuildNormalShlo(fdfe0d94a3b2b3f0).'
---
# Module: [`csrc/ops/normal/normal_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc)

## Functions
- <a id="AtenNormalFloatTensor"></a>`AtenNormalFloatTensor(double mean, const at::Tensor& std, std::optional<at::Generator> generator)` — [`L478`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L478)
- <a id="AtenNormalFloatTensorOut"></a>`AtenNormalFloatTensorOut(double mean, const at::Tensor& std, std::optional<at::Generator> generator, at::Tensor& out)` — [`L507`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L507)
- <a id="AtenNormalTensorFloat"></a>`AtenNormalTensorFloat(const at::Tensor& mean, double std, std::optional<at::Generator> generator)` — [`L537`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L537)
- <a id="AtenNormalTensorFloatOut"></a>`AtenNormalTensorFloatOut(const at::Tensor& mean, double std, std::optional<at::Generator> generator, at::Tensor& out)` — [`L566`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L566)
- <a id="AtenNormalTensorTensor"></a>`AtenNormalTensorTensor(const at::Tensor& mean, const at::Tensor& std, std::optional<at::Generator> generator)` — [`L596`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L596)
- <a id="AtenNormalTensorTensorOut"></a>`AtenNormalTensorTensorOut(const at::Tensor& mean, const at::Tensor& std, std::optional<at::Generator> generator, at::Tensor& out)` — [`L623`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L623)
- <a id="AtenNormal_"></a>`AtenNormal_(at::Tensor& self, double mean, double std, std::optional<at::Generator> generator)` — [`L448`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L448)
- `BuildNormalComplexShlo(mlir::MlirOp rng_state, std::optional<mlir::MlirOp> mean_op, std::optional<mlir::MlirOp> std_op, double mean_val, double std_val, llvm::ArrayRef<int64_t> out_dims, mlir::ElementType out_dtype)` — [`L136`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L136) — Generates a complex-valued normal distribution.
- <a id="BuildNormalComplexShlo"></a>`BuildNormalComplexShlo(mlir::MlirOp rng_state, std::optional<mlir::MlirOp> mean_op, std::optional<mlir::MlirOp> std_op, double mean_val, double std_val, llvm::ArrayRef<int64_t> out_dims, mlir::ElementType out_dtype)` — [`L136`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L136) — Generates a complex-valued normal distribution.
- `BuildNormalRealShlo(mlir::MlirOp rng_state, std::optional<mlir::MlirOp> mean_op, std::optional<mlir::MlirOp> std_op, double mean_val, double std_val, llvm::ArrayRef<int64_t> out_dims, mlir::ElementType out_dtype)` — [`L95`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L95) — Scales and shifts the standard normal distribution to match the requested
- <a id="BuildNormalRealShlo"></a>`BuildNormalRealShlo(mlir::MlirOp rng_state, std::optional<mlir::MlirOp> mean_op, std::optional<mlir::MlirOp> std_op, double mean_val, double std_val, llvm::ArrayRef<int64_t> out_dims, mlir::ElementType out_dtype)` — [`L95`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L95) — Scales and shifts the standard normal distribution to match the requested
- `BuildNormalShlo(mlir::MlirOp rng_state, std::optional<mlir::MlirOp> mean_op, std::optional<mlir::MlirOp> std_op, double mean_val, double std_val, llvm::ArrayRef<int64_t> out_dims, mlir::ElementType out_dtype)` — [`L231`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L231) — Unified entry point for building normal distribution graphs. Dispatches to
- <a id="BuildNormalShlo"></a>`BuildNormalShlo(mlir::MlirOp rng_state, std::optional<mlir::MlirOp> mean_op, std::optional<mlir::MlirOp> std_op, double mean_val, double std_val, llvm::ArrayRef<int64_t> out_dims, mlir::ElementType out_dtype)` — [`L231`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L231) — Unified entry point for building normal distribution graphs. Dispatches to
- <a id="BuildStandardNormalShlo"></a>`BuildStandardNormalShlo(mlir::MlirOp rng_state, llvm::ArrayRef<int64_t> shape, mlir::ElementType type)` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L71) — Generates a standard normal distribution N(0, 1) using the Inverse Transform
- `BuildStandardNormalShlo(mlir::MlirOp rng_state, llvm::ArrayRef<int64_t> shape, mlir::ElementType type)` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L71) — Generates a standard normal distribution N(0, 1) using the Inverse Transform
- <a id="DispatchNormal1"></a>`DispatchNormal1(c10::optional<at::Generator> generator, NAryMlirOpBuilder<1, 1> builder, mlir::ElementType mlir_type, llvm::ArrayRef<int64_t> out_dims, OpParamCacheKeys param_keys)` — [`L296`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L296)
- `DispatchNormal1(c10::optional<at::Generator> generator, NAryMlirOpBuilder<1, 1> builder, mlir::ElementType mlir_type, llvm::ArrayRef<int64_t> out_dims, OpParamCacheKeys param_keys)` — [`L296`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L296)
- `DispatchNormal2` — [`L315`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L315)
- <a id="DispatchNormal2"></a>`DispatchNormal2` — [`L315`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L315)
- <a id="DispatchNormal2Out"></a>`DispatchNormal2Out(c10::optional<at::Generator> generator, NAryMlirOpBuilder<2, 1> builder, const at::Tensor& input_tensor, at::Tensor& out, mlir::ElementType mlir_type, llvm::ArrayRef<int64_t> out_dims, OpParamCacheKeys param_keys)` — [`L338`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L338)
- `DispatchNormal2Out(c10::optional<at::Generator> generator, NAryMlirOpBuilder<2, 1> builder, const at::Tensor& input_tensor, at::Tensor& out, mlir::ElementType mlir_type, llvm::ArrayRef<int64_t> out_dims, OpParamCacheKeys param_keys)` — [`L338`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L338)
- `DispatchNormal3` — [`L387`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L387)
- <a id="DispatchNormal3"></a>`DispatchNormal3` — [`L387`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L387)
- `DispatchNormal3Out(c10::optional<at::Generator> generator, NAryMlirOpBuilder<3, 1> builder, const at::Tensor& input_tensor1, const at::Tensor& input_tensor2, at::Tensor& out, mlir::ElementType mlir_type, llvm::ArrayRef<int64_t> out_dims, OpParamCacheKeys param_keys)` — [`L411`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L411)
- <a id="DispatchNormal3Out"></a>`DispatchNormal3Out(c10::optional<at::Generator> generator, NAryMlirOpBuilder<3, 1> builder, const at::Tensor& input_tensor1, const at::Tensor& input_tensor2, at::Tensor& out, mlir::ElementType mlir_type, llvm::ArrayRef<int64_t> out_dims, OpParamCacheKeys param_keys)` — [`L411`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L411)
- <a id="GetNormalFloatTensorBuilder"></a>`GetNormalFloatTensorBuilder(double mean, llvm::ArrayRef<int64_t> out_dims, at::ScalarType out_dtype)` — [`L355`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L355)
- `GetNormalFloatTensorBuilder(double mean, llvm::ArrayRef<int64_t> out_dims, at::ScalarType out_dtype)` — [`L355`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L355)
- `GetNormalScalarScalarBuilder(double mean, double std, llvm::ArrayRef<int64_t> out_dims, at::ScalarType out_dtype)` — [`L281`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L281)
- <a id="GetNormalScalarScalarBuilder"></a>`GetNormalScalarScalarBuilder(double mean, double std, llvm::ArrayRef<int64_t> out_dims, at::ScalarType out_dtype)` — [`L281`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L281)
- <a id="GetNormalTensorFloatBuilder"></a>`GetNormalTensorFloatBuilder(double std, llvm::ArrayRef<int64_t> out_dims, at::ScalarType out_dtype)` — [`L371`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L371)
- `GetNormalTensorFloatBuilder(double std, llvm::ArrayRef<int64_t> out_dims, at::ScalarType out_dtype)` — [`L371`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L371)
- <a id="GetNormalTensorTensorBuilder"></a>`GetNormalTensorTensorBuilder(llvm::ArrayRef<int64_t> out_dims, at::ScalarType out_dtype)` — [`L430`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L430)
- `GetNormalTensorTensorBuilder(llvm::ArrayRef<int64_t> out_dims, at::ScalarType out_dtype)` — [`L430`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L430)
- <a id="ValidateNormalPreconditions"></a>`ValidateNormalPreconditions(const at::Tensor& tensor, std::string_view arg_name)` — [`L243`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L243)
- <a id="ValidateNormalStdPreconditions"></a>`ValidateNormalStdPreconditions(const at::Tensor& std, bool allow_integer = true)` — [`L259`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L259)
- `ValidateNormalStdPreconditions(double std)` — [`L253`](../../../../../../../raw/code/torch_tpu/csrc/ops/normal/normal_aten_kernels.cc#L253)

