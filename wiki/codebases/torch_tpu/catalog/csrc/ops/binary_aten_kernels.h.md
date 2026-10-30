---
title: 'Module: csrc/ops/binary_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/binary_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BinaryOpOut: BinaryOpOut(96277755e6753971).
  BinaryOp: BinaryOp(e7ff9465b5cca623).
  BinaryOpOptions: BinaryOpOptions#
  TernaryOpOptions.split_mode: TernaryOpOptions#split_mode.
  BinaryOpOptions.split_mode: BinaryOpOptions#split_mode.
  TernaryOpOptions: TernaryOpOptions#
  BinaryOpOptions.force_float_inputs: BinaryOpOptions#force_float_inputs.
  TernaryOpOptions.force_float_inputs: TernaryOpOptions#force_float_inputs.
  TernaryOpOptions.donated_indices: TernaryOpOptions#donated_indices.
  TernaryOpOptions.op_param_cache_keys: TernaryOpOptions#op_param_cache_keys.
  BinaryOpOptions.donated_indices: BinaryOpOptions#donated_indices.
  BinaryOpOptions.op_param_cache_keys: BinaryOpOptions#op_param_cache_keys.
  TernaryOpOptions.result_dtype: TernaryOpOptions#result_dtype.
  BinaryOpOptions.result_dtype: BinaryOpOptions#result_dtype.
  BinaryOpOptions.op_name: BinaryOpOptions#op_name.
  TernaryOpOptions.op_name: TernaryOpOptions#op_name.
  BinaryOpOptions.reverse_operands: BinaryOpOptions#reverse_operands.
  BinaryOpOptions.allow_out_dtype_cast: BinaryOpOptions#allow_out_dtype_cast.
  TernaryOpOptions.allow_out_dtype_cast: TernaryOpOptions#allow_out_dtype_cast.
---
# Module: [`csrc/ops/binary_aten_kernels.h`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h)

## Classes
### <a id="BinaryOpOptions"></a>`BinaryOpOptions`
- def: [`csrc/ops/binary_aten_kernels.h:44`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L44) — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- signature: `struct BinaryOpOptions`
- members:
  - <a id="BinaryOpOptions.allow_out_dtype_cast"></a>`allow_out_dtype_cast` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L69) — Whether the out-variant kernel allows casting the natural result dtype
  - <a id="BinaryOpOptions.donated_indices"></a>`donated_indices` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L53)
  - <a id="BinaryOpOptions.force_float_inputs"></a>`force_float_inputs` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L49)
  - <a id="BinaryOpOptions.op_name"></a>`op_name` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L47) — The op name for dispatching. If omitted, use the op name from the active
  - <a id="BinaryOpOptions.op_param_cache_keys"></a>`op_param_cache_keys` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L51)
  - <a id="BinaryOpOptions.result_dtype"></a>`result_dtype` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L64) — Natural result dtype of the operation.
  - <a id="BinaryOpOptions.reverse_operands"></a>`reverse_operands` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L48)
  - <a id="BinaryOpOptions.split_mode"></a>`split_mode` — [`L52`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L52)
- uses (calls/refs, reference-scoped): [`OpName`](op_names.h.md#OpName), [`OpParamCacheKeys`](../common/cache_key.h.md#OpParamCacheKeys), [`Indices`](../common/dimension_types.h.md#Indices), [`OpSplitMode`](../eager/device_buffer.h.md#OpSplitMode), [`kNone`](../eager/device_buffer.h.md#OpSplitMode.kNone)
- used by: [`BinaryOpOut`](binary_aten_kernels.h.md#BinaryOpOut), [`DispatchBinaryOpOut`](binary_aten_kernels.cc.md#DispatchBinaryOpOut), [`DispatchBinaryOp`](binary_aten_kernels.cc.md#DispatchBinaryOp), [`DispatchBinaryOp`](binary_aten_kernels.cc.md#DispatchBinaryOp), [`DispatchBinaryOpOut`](binary_aten_kernels.cc.md#DispatchBinaryOpOut), [`BinaryOp`](binary_aten_kernels.h.md#BinaryOp)

### <a id="TernaryOpOptions"></a>`TernaryOpOptions`
- def: [`csrc/ops/binary_aten_kernels.h:72`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L72)
- signature: `struct TernaryOpOptions`
- members:
  - <a id="TernaryOpOptions.allow_out_dtype_cast"></a>`allow_out_dtype_cast` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L93) — Whether the out-variant kernel allows casting the natural result dtype
  - <a id="TernaryOpOptions.donated_indices"></a>`donated_indices` — [`L80`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L80)
  - <a id="TernaryOpOptions.force_float_inputs"></a>`force_float_inputs` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L76)
  - <a id="TernaryOpOptions.op_name"></a>`op_name` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L75) — The op name for dispatching. If omitted, use the op name from the active
  - <a id="TernaryOpOptions.op_param_cache_keys"></a>`op_param_cache_keys` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L78)
  - <a id="TernaryOpOptions.result_dtype"></a>`result_dtype` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L89) — Natural result dtype of the operation.
  - <a id="TernaryOpOptions.split_mode"></a>`split_mode` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L79)
- uses (calls/refs, reference-scoped): [`OpName`](op_names.h.md#OpName), [`OpParamCacheKeys`](../common/cache_key.h.md#OpParamCacheKeys), [`Indices`](../common/dimension_types.h.md#Indices), [`OpSplitMode`](../eager/device_buffer.h.md#OpSplitMode), [`kNone`](../eager/device_buffer.h.md#OpSplitMode.kNone)
- used by: [`BinaryOpOut`](binary_aten_kernels.h.md#BinaryOpOut), [`TernaryOpOut`](binary_aten_kernels.cc.md#TernaryOpOut), [`DispatchTernaryOp`](binary_aten_kernels.cc.md#DispatchTernaryOp)

## Functions
- <a id="BinaryOp"></a>`BinaryOp(const at::Tensor& tensor, const OtherType& other, MlirBinaryOpBuilder op_builder, BinaryOpOptions opts)` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L124) — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- <a id="BinaryOpOut"></a>`BinaryOpOut(const at::Tensor& tensor, const OtherType& other, at::Tensor& out, MlirBinaryOpBuilder op_builder, BinaryOpOptions opts)` — [`L135`](../../../../../../raw/code/torch_tpu/csrc/ops/binary_aten_kernels.h#L135) — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)

