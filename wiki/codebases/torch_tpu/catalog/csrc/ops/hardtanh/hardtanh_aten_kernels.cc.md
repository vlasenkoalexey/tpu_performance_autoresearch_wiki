---
title: 'Module: csrc/ops/hardtanh/hardtanh_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/hardtanh/hardtanh_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenHardtanhOut: AtenHardtanhOut(55309b41a6fed6d1).
  AtenHardtanhBackwardGradInput: AtenHardtanhBackwardGradInput(748a141ca95b5f86).
  AtenHardtanhBackward: AtenHardtanhBackward(acccb2b9311a4a8b).
  AtenHardtanh: AtenHardtanh(b235cd7d038bd5e6).
  DispatchHardtanh: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/DispatchHardtanh(d1fbb1fa8262b62f).'
  DispatchHardtanhBackward: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/DispatchHardtanhBackward(db335f548b319f56).'
  ValidateHardtanhInputs: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/ValidateHardtanhInputs(fd0458bfc68bb174).'
  ClampIntegralBounds: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/ClampIntegralBounds(57054466015b62bb).'
  ValidateHardtanhBackwardInputs: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/ValidateHardtanhBackwardInputs(fd0458bfc68bb174).'
  BuildHardtanhBackwardShlo: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/BuildHardtanhBackwardShlo(ac48754f9fea6edd).'
  AtenHardtanhImpl: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/AtenHardtanhImpl(2a3ad93e6f1e2986).'
  AtenHardtanhBackwardImpl: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/AtenHardtanhBackwardImpl(adaf20889e038899).'
  AtenHardtanhOutImpl: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/AtenHardtanhOutImpl(41772c7f02f188a2).'
  AtenHardtanhBackwardOutImpl: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/AtenHardtanhBackwardOutImpl(7a29f5c210eb90b9).'
  AtenHardtanh_: AtenHardtanh_(4e16bfbc19ed80f).
  ClampHardtanhBounds: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/ClampHardtanhBounds(cfae63098654c2ff).'
  HardtanhBounds: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/HardtanhBounds#'
  HardtanhBounds.max_val: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/HardtanhBounds#max_val.'
  BuildHardtanhShlo: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/BuildHardtanhShlo(28dc33d166dda8e).'
  HardtanhBounds.min_val: '`$anonymous_namespace_csrc/ops/hardtanh/hardtanh_aten_kernels.cc`/HardtanhBounds#min_val.'
---
# Module: [`csrc/ops/hardtanh/hardtanh_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc)

## Classes
### <a id="HardtanhBounds"></a>`HardtanhBounds`
- def: [`csrc/ops/hardtanh/hardtanh_aten_kernels.cc:86`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L86)
- doc: Holds the min and max scalar limits for hardtanh after bound clamping.
- signature: `struct HardtanhBounds`
- members:
  - <a id="HardtanhBounds.max_val"></a>`max_val` — [`L88`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L88)
  - <a id="HardtanhBounds.min_val"></a>`min_val` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L87)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`DispatchHardtanh`](hardtanh_aten_kernels.cc.md#DispatchHardtanh), [`ClampIntegralBounds`](hardtanh_aten_kernels.cc.md#ClampIntegralBounds), [`ClampHardtanhBounds`](hardtanh_aten_kernels.cc.md#ClampHardtanhBounds)

## Functions
- <a id="AtenHardtanh"></a>`AtenHardtanh(const at::Tensor& self, const at::Scalar& min_val, const at::Scalar& max_val)` — [`L287`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L287)
- <a id="AtenHardtanhBackward"></a>`AtenHardtanhBackward(const at::Tensor& grad_output, const at::Tensor& self, const at::Scalar& min_val, const at::Scalar& max_val)` — [`L317`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L317)
- <a id="AtenHardtanhBackwardGradInput"></a>`AtenHardtanhBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, const at::Scalar& min_val, const at::Scalar& max_val, at::Tensor& grad_input)` — [`L333`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L333)
- <a id="AtenHardtanhBackwardImpl"></a>`AtenHardtanhBackwardImpl(const at::Tensor& grad_output, const at::Tensor& self, PromotedScalar& promoted_min, PromotedScalar& promoted_max, OpParamCacheKeys param_keys)` — [`L259`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L259)
- <a id="AtenHardtanhBackwardOutImpl"></a>`AtenHardtanhBackwardOutImpl(const at::Tensor& grad_output, const at::Tensor& self, PromotedScalar& promoted_min, PromotedScalar& promoted_max, OpParamCacheKeys param_keys, at::Tensor& grad_input)` — [`L271`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L271)
- <a id="AtenHardtanhImpl"></a>`AtenHardtanhImpl(const at::Tensor& self, PromotedScalar& promoted_min, PromotedScalar& promoted_max, OpParamCacheKeys param_keys)` — [`L194`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L194)
- <a id="AtenHardtanhOut"></a>`AtenHardtanhOut(const at::Tensor& self, const at::Scalar& min_val, const at::Scalar& max_val, at::Tensor& out)` — [`L304`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L304)
- <a id="AtenHardtanhOutImpl"></a>`AtenHardtanhOutImpl(const at::Tensor& self, PromotedScalar& promoted_min, PromotedScalar& promoted_max, OpParamCacheKeys param_keys, at::Tensor& out)` — [`L206`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L206)
- <a id="AtenHardtanh_"></a>`AtenHardtanh_(at::Tensor& self, const at::Scalar& min_val, const at::Scalar& max_val)` — [`L299`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L299)
- <a id="BuildHardtanhBackwardShlo"></a>`BuildHardtanhBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp self, mlir::MlirOp min_val, mlir::MlirOp max_val)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L55)
- <a id="BuildHardtanhShlo"></a>`BuildHardtanhShlo(mlir::MlirOp input, mlir::MlirOp min_val, mlir::MlirOp max_val)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L49)
- <a id="ClampHardtanhBounds"></a>`ClampHardtanhBounds(at::ScalarType scalar_type, at::Scalar min_val, at::Scalar max_val)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L129) — Clamps out-of-range bounds with representable range of integral types.
- <a id="ClampIntegralBounds"></a>`ClampIntegralBounds(at::Scalar min_val, at::Scalar max_val, at::ScalarType scalar_type)` — [`L101`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L101) — Clamps integral scalar limits to the representable range of the target
- <a id="DispatchHardtanh"></a>`DispatchHardtanh(const at::Tensor& self, PromotedScalar& promoted_min, PromotedScalar& promoted_max, OpParamCacheKeys param_keys, DispatchFn&& dispatch_fn)` — [`L153`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L153) — Helper to dispatch the hardtanh computation on the device.
- <a id="DispatchHardtanhBackward"></a>`DispatchHardtanhBackward(const at::Tensor& grad_output, const at::Tensor& self, PromotedScalar& promoted_min, PromotedScalar& promoted_max, OpParamCacheKeys param_keys, DispatchFn&& dispatch_fn)` — [`L228`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L228) — Helper to dispatch the hardtanh_backward computation on the device.
- <a id="ValidateHardtanhBackwardInputs"></a>`ValidateHardtanhBackwardInputs(const at::Tensor& self)` — [`L218`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L218)
- <a id="ValidateHardtanhInputs"></a>`ValidateHardtanhInputs(const at::Tensor& self)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardtanh/hardtanh_aten_kernels.cc#L73)

