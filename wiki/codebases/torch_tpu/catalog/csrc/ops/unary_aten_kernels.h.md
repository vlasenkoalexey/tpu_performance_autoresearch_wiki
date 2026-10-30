---
title: 'Module: csrc/ops/unary_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/unary_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/UnaryOpOptions#
symbols:
  UnaryOpOptions.allow_out_dtype_cast: allow_out_dtype_cast.
  UnaryOpOptions.op_name: op_name.
  UnaryOpOptions: ''
  UnaryOpOptions.out_dims: out_dims.
  UnaryOpOptions.out_dtype: out_dtype.
  UnaryOpOptions.op_param_cache_keys: op_param_cache_keys.
  UnaryOpOptions.computation_dtype: computation_dtype.
---
# Module: [`csrc/ops/unary_aten_kernels.h`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.h)

## Classes
### <a id="UnaryOpOptions"></a>`UnaryOpOptions`
- def: [`csrc/ops/unary_aten_kernels.h:33`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.h#L33) — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- signature: `struct UnaryOpOptions`
- members:
  - <a id="UnaryOpOptions.allow_out_dtype_cast"></a>`allow_out_dtype_cast` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.h#L54) — Whether the out-variant kernel allows casting the natural result dtype
  - <a id="UnaryOpOptions.computation_dtype"></a>`computation_dtype` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.h#L49) — If specified, all inputs will be casted to this dtype before
  - <a id="UnaryOpOptions.op_name"></a>`op_name` — [`L36`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.h#L36) — The op name for dispatching. If omitted, use the op name from the active
  - <a id="UnaryOpOptions.op_param_cache_keys"></a>`op_param_cache_keys` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.h#L39) — Parameters (if any) that were used to construct op_builder and will be used
  - <a id="UnaryOpOptions.out_dims"></a>`out_dims` — [`L46`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.h#L46) — Size of the output tensor. If not specified use self's size.
  - <a id="UnaryOpOptions.out_dtype"></a>`out_dtype` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.h#L44) — Natural result dtype of the operation.
- uses (calls/refs, reference-scoped): [`OpName`](op_names.h.md#OpName), [`OpParamCacheKeys`](../common/cache_key.h.md#OpParamCacheKeys), [`UnaryOpOut`](unary_aten_kernels.cc.md#UnaryOpOut), [`UnaryOp`](unary_aten_kernels.cc.md#UnaryOp), [`UnaryOpInPlace`](unary_aten_kernels.cc.md#UnaryOpInPlace), [`MlirUnaryOpBuilder`](op_builder_utils.h.md#MlirUnaryOpBuilder)
- used by: [`UnaryOpOut`](unary_aten_kernels.cc.md#UnaryOpOut), [`UnaryOp`](unary_aten_kernels.cc.md#UnaryOp), [`UnaryOpInPlace`](unary_aten_kernels.cc.md#UnaryOpInPlace), [`UnaryOpInPlace`](unary_aten_kernels.cc.md#UnaryOpInPlace), [`UnaryOpOut`](unary_aten_kernels.cc.md#UnaryOpOut), [`UnaryOp`](unary_aten_kernels.cc.md#UnaryOp)

