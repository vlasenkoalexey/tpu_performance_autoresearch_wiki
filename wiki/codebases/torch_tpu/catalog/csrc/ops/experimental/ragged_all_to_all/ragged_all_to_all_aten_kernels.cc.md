---
title: 'Module: csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenRaggedAllToAllOut: AtenRaggedAllToAllOut(692eec7d28e47db4).
  AtenRaggedAllToAll: AtenRaggedAllToAll(7bdfd59d164db4b).
  RaggedAllToAllCommon: '`$anonymous_namespace_csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc`/RaggedAllToAllCommon(c6a85fe02cb91214).'
  GetProcessGroupTpu: '`$anonymous_namespace_csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc`/GetProcessGroupTpu(c006cdc0ea42ff26).'
  AtenRaggedAllToAllAutograd.forward: AtenRaggedAllToAllAutograd#forward(c2d35f69308fe5fc).
  AtenRaggedAllToAllAutograd.backward: AtenRaggedAllToAllAutograd#backward(305625f81d7e100).
---
# Module: [`csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc)

## Functions
- <a id="AtenRaggedAllToAll"></a>`AtenRaggedAllToAll(const at::Tensor& operand, const at::Tensor& output, const at::Tensor& input_offsets, const at::Tensor& send_sizes, const at::Tensor& output_offsets, const at::Tensor& recv_sizes, std::string_view process_group_name)` — [`L135`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc#L135) — RaggedAllToAll collective operation. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="AtenRaggedAllToAllOut"></a>`AtenRaggedAllToAllOut(const at::Tensor& operand, const at::Tensor& output, const at::Tensor& input_offsets, const at::Tensor& send_sizes, const at::Tensor& output_offsets, const at::Tensor& recv_sizes, std::string_view process_group_name, at::Tensor& out)` — [`L155`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc#L155) — RaggedAllToAll collective operation (out variant). — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="GetProcessGroupTpu"></a>`GetProcessGroupTpu(std::string_view process_group_name)` — [`L65`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc#L65) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="RaggedAllToAllCommon"></a>`RaggedAllToAllCommon(const at::Tensor& operand, const at::Tensor& output, const at::Tensor& input_offsets, const at::Tensor& send_sizes, const at::Tensor& output_offsets, const at::Tensor& recv_sizes, std::string_view process_group_name, OpParamCacheKeys& param_keys)` — [`L86`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc#L86) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)

## Other members
- <a id="AtenRaggedAllToAllAutograd.backward"></a>`AtenRaggedAllToAllAutograd.backward` — [`L260`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc#L260)
- <a id="AtenRaggedAllToAllAutograd.forward"></a>`AtenRaggedAllToAllAutograd.forward` — [`L174`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.cc#L174) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)

