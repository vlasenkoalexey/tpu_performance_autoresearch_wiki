---
title: 'Module: csrc/ops/experimental/collectives/collectives_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/collectives/collectives_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AllGatherDim: AllGatherDim(a2e89b9740a36bc0).
  ReduceScatterDim: ReduceScatterDim(67159591f57aaf63).
  ParseReduceOp: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/ParseReduceOp(9b121552c48ec72d).'
  ReduceScatterShape: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/ReduceScatterShape(46e309c7b1931f0b).'
  ValidateArgs: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/ValidateArgs(46e309c7b1931f0b).'
  DispatchCollectiveWithDim: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/DispatchCollectiveWithDim(84626d93efd1db2).'
  MetaReduceScatterDim: MetaReduceScatterDim(67159591f57aaf63).
  GetProcessGroupTpu: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/GetProcessGroupTpu(1208006d6f283132).'
  MetaAllGatherDim: MetaAllGatherDim(a2e89b9740a36bc0).
  AllGatherShape: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/AllGatherShape(46e309c7b1931f0b).'
  CollectiveShape.output_shape: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/CollectiveShape#output_shape.'
  CollectiveShape.dim: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/CollectiveShape#dim.'
  CollectiveShape: '`$anonymous_namespace_csrc/ops/experimental/collectives/collectives_aten_kernels.cc`/CollectiveShape#'
---
# Module: [`csrc/ops/experimental/collectives/collectives_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc)

## Classes
### <a id="CollectiveShape"></a>`CollectiveShape`
- def: [`csrc/ops/experimental/collectives/collectives_aten_kernels.cc:63`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L63)
- doc: The validated collective dimension and the resulting output shape.
- signature: `struct CollectiveShape`
- members:
  - <a id="CollectiveShape.dim"></a>`dim` — [`L65`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L65) — The collective dimension, normalized to [0, input.dim()).
  - <a id="CollectiveShape.output_shape"></a>`output_shape` — [`L66`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L66)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../../common/dimension_types.h.md#Dimensions)
- used by: [`AllGatherDim`](collectives_aten_kernels.cc.md#AllGatherDim), [`ReduceScatterDim`](collectives_aten_kernels.cc.md#ReduceScatterDim), [`ReduceScatterShape`](collectives_aten_kernels.cc.md#ReduceScatterShape), [`ValidateArgs`](collectives_aten_kernels.cc.md#ValidateArgs), [`MetaReduceScatterDim`](collectives_aten_kernels.cc.md#MetaReduceScatterDim), [`MetaAllGatherDim`](collectives_aten_kernels.cc.md#MetaAllGatherDim), [`AllGatherShape`](collectives_aten_kernels.cc.md#AllGatherShape)

## Functions
- <a id="AllGatherDim"></a>`AllGatherDim(const at::Tensor& input, int64_t dim, int64_t group_size, std::string_view group_name)` — [`L173`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L173) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="AllGatherShape"></a>`AllGatherShape(const at::Tensor& input, int64_t dim, int64_t group_size)` — [`L81`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L81)
- <a id="DispatchCollectiveWithDim"></a>`DispatchCollectiveWithDim(const at::Tensor& input, int64_t group_size, Dimensions output_shape, std::string_view group_name, CollectiveBuilder collective_builder, OpParamCacheKeys param_keys)` — [`L148`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L148) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- `GetProcessGroupTpu(std::string_view group_name, int64_t group_size)` — [`L125`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L125) — resolve_process_group() and getBackend() throw on an unknown or destroyed
- <a id="GetProcessGroupTpu"></a>`GetProcessGroupTpu(std::string_view group_name, int64_t group_size)` — [`L125`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L125) — resolve_process_group() and getBackend() throw on an unknown or destroyed — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="MetaAllGatherDim"></a>`MetaAllGatherDim(const at::Tensor& input, int64_t dim, int64_t group_size, std::string_view /*group_name*/)` — [`L221`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L221) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="MetaReduceScatterDim"></a>`MetaReduceScatterDim(const at::Tensor& input, std::string_view reduce_op, int64_t dim, int64_t group_size, std::string_view /*group_name*/)` — [`L228`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L228) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="ParseReduceOp"></a>`ParseReduceOp(std::string_view reduce_op, c10::ScalarType scalar_type)` — [`L103`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L103) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="ReduceScatterDim"></a>`ReduceScatterDim(const at::Tensor& input, std::string_view reduce_op, int64_t dim, int64_t group_size, std::string_view group_name)` — [`L197`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L197) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="ReduceScatterShape"></a>`ReduceScatterShape(const at::Tensor& input, int64_t dim, int64_t group_size)` — [`L90`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L90) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="ValidateArgs"></a>`ValidateArgs(const at::Tensor& input, int64_t dim, int64_t group_size)` — [`L69`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/collectives/collectives_aten_kernels.cc#L69) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)

