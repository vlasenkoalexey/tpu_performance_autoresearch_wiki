---
title: 'Module: csrc/ops/distance/dist_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/distance/dist_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenCdistForward: AtenCdistForward(8476e20c59cb563d).
  AtenCdistBackward: AtenCdistBackward(663a91a64c5aeba4).
  AtenPdistBackward: AtenPdistBackward(fdd22b8833e0aaed).
  AtenPdistForward: AtenPdistForward(f7c053eb040d1add).
  ValidateNotBFloatOrHalf: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/ValidateNotBFloatOrHalf(d8359b99282c084c).'
  ValidateIsFloatingPoint: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/ValidateIsFloatingPoint(d8359b99282c084c).'
  BuildPdistForwardHlo: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/BuildPdistForwardHlo(2098a22246401bc7).'
  BuildCdistForwardShlo: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/BuildCdistForwardShlo(db1f076a94caaa6c).'
  BuildPdistBackwardShlo: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/BuildPdistBackwardShlo(d316c0f006f4d14f).'
  BuildCdistBackwardShlo: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/BuildCdistBackwardShlo(39e41d95d03c5e25).'
  BroadcastCdistInput: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/BroadcastCdistInput(5157d2e76159c407).'
  BuildZeroNorm: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/BuildZeroNorm(4175f2d8feeca5f8).'
  IsBFloatOrHalf: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/IsBFloatOrHalf(b580d0b7e29ca914).'
  FeatureDimMapping.second_dim: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/FeatureDimMapping#second_dim.'
  FeatureDimMapping: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/FeatureDimMapping#'
  FeatureDimMapping.first_dim: '`$anonymous_namespace_csrc/ops/distance/dist_aten_kernels.cc`/FeatureDimMapping#first_dim.'
---
# Module: [`csrc/ops/distance/dist_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc)

## Classes
### <a id="FeatureDimMapping"></a>`FeatureDimMapping`
- def: [`csrc/ops/distance/dist_aten_kernels.cc:98`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L98)
- signature: `struct FeatureDimMapping`
- members:
  - <a id="FeatureDimMapping.first_dim"></a>`first_dim` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L99)
  - <a id="FeatureDimMapping.second_dim"></a>`second_dim` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L100)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BroadcastCdistInput`](dist_aten_kernels.cc.md#BroadcastCdistInput)

## Functions
- <a id="AtenCdistBackward"></a>`AtenCdistBackward(const at::Tensor& grad, const at::Tensor& x1, const at::Tensor& x2, double p, const at::Tensor& cdist)` — [`L631`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L631)
- <a id="AtenCdistForward"></a>`AtenCdistForward(const at::Tensor& x1, const at::Tensor& x2, double p, std::optional<int64_t> compute_mode)` — [`L571`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L571)
- <a id="AtenPdistBackward"></a>`AtenPdistBackward(const at::Tensor& grad, const at::Tensor& self, double p, const at::Tensor& pdist)` — [`L725`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L725)
- <a id="AtenPdistForward"></a>`AtenPdistForward(const at::Tensor& self, double p)` — [`L688`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L688)
- <a id="BroadcastCdistInput"></a>`BroadcastCdistInput(mlir::MlirOp op, mlir::RankedTensorType target_bcast_type, const int64_t common_batch_rank, FeatureDimMapping feature_dim_mappings)` — [`L105`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L105) — Helper to broadcast cdist inputs (x1, x2, grad, cdist) to target shape
- <a id="BuildCdistBackwardShlo"></a>`BuildCdistBackwardShlo(mlir::MlirOp grad_op, mlir::MlirOp x1_op, mlir::MlirOp x2_op, double p, mlir::MlirOp cdist_op, const Dimensions common_batch_shape, int64_t r1, int64_t r2, int64_t c)` — [`L416`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L416)
- <a id="BuildCdistForwardShlo"></a>`BuildCdistForwardShlo(mlir::MlirOp x1_op, mlir::MlirOp x2_op, double p, int64_t compute_mode, const Dimensions common_batch_shape, int64_t r1, int64_t r2, int64_t c)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L130) — Computes the p-norm distance of the difference between each pair of row
- <a id="BuildPdistBackwardShlo"></a>`BuildPdistBackwardShlo(mlir::MlirOp grad_op, mlir::MlirOp self_op, double p, mlir::MlirOp pdist_op)` — [`L235`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L235)
- <a id="BuildPdistForwardHlo"></a>`BuildPdistForwardHlo(mlir::MlirOp input_op, double p)` — [`L183`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L183) — Computes the p-norm distance of the difference between each pair of elements
- <a id="BuildZeroNorm"></a>`BuildZeroNorm(mlir::MlirOp input, int64_t reduce_dim, mlir::Type element_type)` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L68) — When p=0, compute the 0-norm (Hamming distance equivalent)
- <a id="IsBFloatOrHalf"></a>`IsBFloatOrHalf(const at::Tensor& tensor)` — [`L548`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L548)
- <a id="ValidateIsFloatingPoint"></a>`ValidateIsFloatingPoint(const at::Tensor& tensor, const std::string_view name)` — [`L553`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L553)
- <a id="ValidateNotBFloatOrHalf"></a>`ValidateNotBFloatOrHalf(const at::Tensor& tensor, const std::string_view name)` — [`L561`](../../../../../../../raw/code/torch_tpu/csrc/ops/distance/dist_aten_kernels.cc#L561)

