---
title: 'Module: torchtitan/experiments/graph_trainer/simple_fsdp.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/simple_fsdp.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.simple_fsdp`/
symbols:
  data_parallel: data_parallel().
  MixedPrecisionPolicy: MixedPrecisionPolicy#
  ReplicateComputation.replicate_compute: ReplicateComputation#replicate_compute().
  disable_active_parametrization: disable_active_parametrization().
  MixedPrecisionPolicy.param_dtype: MixedPrecisionPolicy#param_dtype.
  ReplicateComputation.forward: ReplicateComputation#forward().
  MixedPrecisionPolicy.reduce_dtype: MixedPrecisionPolicy#reduce_dtype.
  ReplicateComputation: ReplicateComputation#
  ReplicateComputation.reduce_dtype: ReplicateComputation#reduce_dtype.
  _BuildUnshardedTensorFunction.forward: _BuildUnshardedTensorFunction#forward().
  ReplicateComputation.grad_placements: ReplicateComputation#grad_placements.
  ReplicateComputation.param_dtype: ReplicateComputation#param_dtype.
  _register_parametrization: _register_parametrization().
  _active_parametrization: _active_parametrization.
  ReplicateComputation.device_mesh: ReplicateComputation#device_mesh.
  ReplicateComputation.compute_placements: ReplicateComputation#compute_placements.
  ReplicateComputation.__init__: ReplicateComputation#__init__().
  ReplicateComputation.non_dp_mesh_types: ReplicateComputation#non_dp_mesh_types.
  _wrap_class_cache._wrap_class_cache: _wrap_class_cache._wrap_class_cache.
  _prepare_spmd_parameter_for_fsdp: _prepare_spmd_parameter_for_fsdp().
  _distribute_dtensor: _distribute_dtensor().
  _wrap_class_id: _wrap_class_id.
  _BuildUnshardedTensorFunction: _BuildUnshardedTensorFunction#
  ReplicateComputation.param_sharding: ReplicateComputation#param_sharding.
  _BuildUnshardedTensorFunction.backward: _BuildUnshardedTensorFunction#backward().
  ReplicateComputation.mode: ReplicateComputation#mode.
---
# Module: [`torchtitan/experiments/graph_trainer/simple_fsdp.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py)

## Classes
### <a id="MixedPrecisionPolicy"></a>`MixedPrecisionPolicy`
- def: [`torchtitan/experiments/graph_trainer/simple_fsdp.py:51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L51)
- signature: `class MixedPrecisionPolicy:`
- members:
  - <a id="MixedPrecisionPolicy.param_dtype"></a>`param_dtype` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L52)
  - <a id="MixedPrecisionPolicy.reduce_dtype"></a>`reduce_dtype` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L53)
- used by: [`parallelize_conformer`](../tpu/conformer/infra/parallelize.md#parallelize_conformer), [`parallelize_flux`](../../models/flux/parallelize.md#parallelize_flux), [`apply_simple_fsdp`](common_utils.md#apply_simple_fsdp), [`data_parallel`](simple_fsdp.md#data_parallel), [`parallelize_encoders`](../../models/flux/parallelize.md#parallelize_encoders), [`parallelize_llama`](../tpu/llama3/infra/parallelize.md#parallelize_llama), [`parallelize_hf_transformers_tpu`](../tpu/transformers_modeling_backend/parallelize.md#parallelize_hf_transformers_tpu), [`reduce_dtype`](simple_fsdp.md#ReplicateComputation.reduce_dtype), [`grad_placements`](simple_fsdp.md#ReplicateComputation.grad_placements), [`param_dtype`](simple_fsdp.md#ReplicateComputation.param_dtype), [`__init__`](simple_fsdp.md#ReplicateComputation.__init__)  (6 test-only)

### <a id="ReplicateComputation"></a>`ReplicateComputation`  ·  implements/extends Module
- def: [`torchtitan/experiments/graph_trainer/simple_fsdp.py:281`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L281) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- signature: `class ReplicateComputation(Module):`
- members:
  - <a id="ReplicateComputation.forward"></a>`forward(self, x: DTensor)` — [`L377`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L377)
  - <a id="ReplicateComputation.replicate_compute"></a>`replicate_compute(self, x: DTensor)` — [`L309`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L309)
  - <a id="ReplicateComputation.compute_placements"></a>`compute_placements` — [`L294`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L294)
  - <a id="ReplicateComputation.device_mesh"></a>`device_mesh` — [`L291`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L291)
  - <a id="ReplicateComputation.grad_placements"></a>`grad_placements` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L295)
  - <a id="ReplicateComputation.mode"></a>`mode` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L293)
  - <a id="ReplicateComputation.non_dp_mesh_types"></a>`non_dp_mesh_types` — [`L307`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L307)
  - <a id="ReplicateComputation.param_dtype"></a>`param_dtype` — [`L299`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L299)
  - <a id="ReplicateComputation.param_sharding"></a>`param_sharding` — [`L292`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L292)
  - <a id="ReplicateComputation.reduce_dtype"></a>`reduce_dtype` — [`L300`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L300)
- protocol/private: <a id="ReplicateComputation.__init__"></a>`__init__`[`L282`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L282)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`MixedPrecisionPolicy`](simple_fsdp.md#MixedPrecisionPolicy), [`_UnshardedFSDPTensor`](../../components/quantization/_fsdp_tensor.md#_UnshardedFSDPTensor), [`param_dtype`](simple_fsdp.md#MixedPrecisionPolicy.param_dtype), [`replicate_compute`](../tpu/graph_trainer/simple_fsdp.md#TpuReplicateComputation.replicate_compute), [`_ShardedFSDPTensor`](../../components/quantization/_fsdp_tensor.md#_ShardedFSDPTensor), [`reduce_dtype`](simple_fsdp.md#MixedPrecisionPolicy.reduce_dtype), [`TpuReplicateComputation`](../tpu/graph_trainer/simple_fsdp.md#TpuReplicateComputation), [`_active_parametrization`](simple_fsdp.md#_active_parametrization), [`_BuildUnshardedTensorFunction`](simple_fsdp.md#_BuildUnshardedTensorFunction)
- used by: [`Module`](../../protocols/module.md#Module), [`data_parallel`](simple_fsdp.md#data_parallel), [`install_tpu_replicate_computation`](../tpu/graph_trainer/simple_fsdp.md#install_tpu_replicate_computation), [`replicate_compute`](../tpu/graph_trainer/simple_fsdp.md#TpuReplicateComputation.replicate_compute), [`TpuReplicateComputation`](../tpu/graph_trainer/simple_fsdp.md#TpuReplicateComputation)

### <a id="_BuildUnshardedTensorFunction"></a>`_BuildUnshardedTensorFunction`
- def: [`torchtitan/experiments/graph_trainer/simple_fsdp.py:241`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L241)
- doc: Own the gradient edge for an unsharded tensor built outside FSDP2.
- signature: `class _BuildUnshardedTensorFunction(torch.autograd.Function):`
- members:
  - <a id="_BuildUnshardedTensorFunction.backward"></a>`backward(ctx, grad_weight: torch.Tensor)` — [`L276`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L276)
  - <a id="_BuildUnshardedTensorFunction.forward"></a>`forward(ctx, weight: torch.Tensor, wrapper: _ShardedFSDPTensor)` — [`L256`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L256)
- uses (calls/refs, reference-scoped): [`_UnshardedFSDPTensor`](../../components/quantization/_fsdp_tensor.md#_UnshardedFSDPTensor), [`_ShardedFSDPTensor`](../../components/quantization/_fsdp_tensor.md#_ShardedFSDPTensor), [`_build_operands`](../../components/quantization/_fsdp_tensor.md#_ShardedFSDPTensor._build_operands)
- used by: [`forward`](simple_fsdp.md#ReplicateComputation.forward)

## Functions
- <a id="_distribute_dtensor"></a>`_distribute_dtensor(tensor: DTensor, device_mesh: DeviceMesh, dp_placements: Sequence[Placement])` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L115) — Below are experimental enhancements to distribute a DTensor.
- <a id="_prepare_spmd_parameter_for_fsdp"></a>`_prepare_spmd_parameter_for_fsdp(tensor: torch.Tensor, param_name: str, non_dp_mesh: DeviceMesh | None)` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L76) — Prepare an SPMD-annotated parameter for SimpleFSDP.
- <a id="_register_parametrization"></a>`_register_parametrization(module: nn.Module, param_names: list[str], parametrization_init: Callable[[str], nn.Module])` — [`L201`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L201) — It works with state_dict without incurring parametrization calls because
- <a id="data_parallel"></a>`data_parallel(model: nn.Module, device_mesh: DeviceMesh, mode: str = "replicate", mp_policy: MixedPrecisionPolicy | None = None, shard_dim: int | dict[str, int] = 0, non_dp_mesh: DeviceMesh | None = None, ignored_params: set[nn.Parameter] | None = None)` — [`L414`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L414) — Shard ``model`` and install the data-parallel parametrization. — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- <a id="disable_active_parametrization"></a>`disable_active_parametrization()` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L41)

## Module values
- <a id="_active_parametrization"></a>`_active_parametrization` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L37)
- <a id="_wrap_class_cache._wrap_class_cache"></a>`_wrap_class_cache` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L198)
- <a id="_wrap_class_id"></a>`_wrap_class_id` — [`L197`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/simple_fsdp.py#L197)

