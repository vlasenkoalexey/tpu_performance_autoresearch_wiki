---
title: 'Module: csrc/ops/bucketize/bucketize_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/bucketize/bucketize_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenBucketizeTensorOut: AtenBucketizeTensorOut(27df2ff2a7bf9870).
  AtenBucketizeScalar: AtenBucketizeScalar(d3a0c11dc47412cf).
  AtenBucketizeTensor: AtenBucketizeTensor(1ef88acd173c51e0).
  ValidateInputAndBoundaries: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/ValidateInputAndBoundaries(b2d6689cde60befb).'
  BuildCompareAllShlo: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/BuildCompareAllShlo(cda59f9cff76327).'
  DispatchBucketize: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/DispatchBucketize(6e24ade59359c789).'
  BucketizeOut: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/BucketizeOut(6ade60f18d90fdcb).'
  BroadcastArgs: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/BroadcastArgs(c495b14f13d2cb2f).'
  Bucketize: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/Bucketize(12b10f73b1fcc766).'
  BuildBucketizeShlo: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/BuildBucketizeShlo(cda59f9cff76327).'
  BroadcastResult.boundaries_bcast_op: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/BroadcastResult#boundaries_bcast_op.'
  BroadcastResult: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/BroadcastResult#'
  BroadcastResult.self_bcast_op: '`$anonymous_namespace_csrc/ops/bucketize/bucketize_aten_kernels.cc`/BroadcastResult#self_bcast_op.'
---
# Module: [`csrc/ops/bucketize/bucketize_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc)

## Classes
### <a id="BroadcastResult"></a>`BroadcastResult`
- def: [`csrc/ops/bucketize/bucketize_aten_kernels.cc:77`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L77)
- signature: `struct BroadcastResult`
- members:
  - <a id="BroadcastResult.boundaries_bcast_op"></a>`boundaries_bcast_op` — [`L79`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L79)
  - <a id="BroadcastResult.self_bcast_op"></a>`self_bcast_op` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L78)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildCompareAllShlo`](bucketize_aten_kernels.cc.md#BuildCompareAllShlo), [`BroadcastArgs`](bucketize_aten_kernels.cc.md#BroadcastArgs)

## Functions
- <a id="AtenBucketizeScalar"></a>`AtenBucketizeScalar(const at::Scalar& self, const at::Tensor& boundaries, bool out_int32, bool right)` — [`L212`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L212)
- <a id="AtenBucketizeTensor"></a>`AtenBucketizeTensor(const at::Tensor& self, const at::Tensor& boundaries, bool out_int32, bool right)` — [`L227`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L227)
- <a id="AtenBucketizeTensorOut"></a>`AtenBucketizeTensorOut(const at::Tensor& self, const at::Tensor& boundaries, bool out_int32, bool right, at::Tensor& out)` — [`L239`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L239)
- <a id="BroadcastArgs"></a>`BroadcastArgs(mlir::MlirOp self_op, mlir::MlirOp boundaries_op)` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L82)
- <a id="Bucketize"></a>`Bucketize(const at::Tensor& self, const at::Tensor& boundaries, bool out_int32, bool right, OpParamCacheKeys param_keys)` — [`L178`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L178)
- <a id="BucketizeOut"></a>`BucketizeOut(const at::Tensor& self, const at::Tensor& boundaries, bool out_int32, bool right, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L193`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L193)
- <a id="BuildBucketizeShlo"></a>`BuildBucketizeShlo(mlir::MlirOp self_op, mlir::MlirOp boundaries_op, mlir::ElementType out_dtype, bool right)` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L135)
- <a id="BuildCompareAllShlo"></a>`BuildCompareAllShlo(mlir::MlirOp self_op, mlir::MlirOp boundaries_op, mlir::ElementType out_dtype, bool right)` — [`L94`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L94)
- <a id="DispatchBucketize"></a>`DispatchBucketize(const at::Tensor& self, const at::Tensor& boundaries, bool out_int32, bool right, OpParamCacheKeys param_keys, OpDispatcherFn&& dispatch_fn)` — [`L146`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L146)
- <a id="ValidateInputAndBoundaries"></a>`ValidateInputAndBoundaries(const at::Tensor& self, const at::Tensor& boundaries)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/bucketize/bucketize_aten_kernels.cc#L52)

