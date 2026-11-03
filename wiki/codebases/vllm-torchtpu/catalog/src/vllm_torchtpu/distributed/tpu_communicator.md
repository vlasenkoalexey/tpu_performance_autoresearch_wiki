---
title: 'Module: src/vllm_torchtpu/distributed/tpu_communicator.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/tpu_communicator.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.tpu_communicator`/
symbols:
  TpuDeviceCommunicator: TpuDeviceCommunicator#
  TpuDeviceCommunicator._moe_group: TpuDeviceCommunicator#_moe_group().
  TpuDeviceCommunicator.all2all_manager: TpuDeviceCommunicator#all2all_manager.
  TpuDeviceCommunicator.dispatch_router_logits: TpuDeviceCommunicator#dispatch_router_logits().
  TpuDeviceCommunicator.dispatch: TpuDeviceCommunicator#dispatch().
  TpuDeviceCommunicator.combine: TpuDeviceCommunicator#combine().
  TpuNullAll2AllManager: TpuNullAll2AllManager#
  TpuDeviceCommunicator.__init__: TpuDeviceCommunicator#__init__().
---
# Module: [`src/vllm_torchtpu/distributed/tpu_communicator.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py)

## Classes
### <a id="TpuDeviceCommunicator"></a>`TpuDeviceCommunicator`
- def: [`src/vllm_torchtpu/distributed/tpu_communicator.py:35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py#L35) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- signature: `class TpuDeviceCommunicator(DeviceCommunicatorBase):`
- members:
  - <a id="TpuDeviceCommunicator.combine"></a>`combine(self, hidden_states: torch.Tensor, is_sequence_parallel: bool = False)` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py#L87)
  - <a id="TpuDeviceCommunicator.dispatch"></a>`dispatch(self, hidden_states: torch.Tensor, topk_weights: torch.Tensor, topk_ids: torch.Tensor, is_sequence_parallel: bool = False, extra_tensors=None)` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py#L67)
  - <a id="TpuDeviceCommunicator.dispatch_router_logits"></a>`dispatch_router_logits(self, hidden_states: torch.Tensor, router_logits: torch.Tensor, is_sequence_parallel: bool = False, extra_tensors=None)` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py#L49)
  - <a id="TpuDeviceCommunicator.all2all_manager"></a>`all2all_manager` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py#L43)
- protocol/private: <a id="TpuDeviceCommunicator.__init__"></a>`__init__`[`L36`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py#L36), <a id="TpuDeviceCommunicator._moe_group"></a>`_moe_group`[`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py#L45)
- uses (calls/refs, reference-scoped): [`TpuNullAll2AllManager`](tpu_communicator.md#TpuNullAll2AllManager)
- used by: [`get_device_communicator_cls`](../platforms/tpu_platform.md#TpuPlatform.get_device_communicator_cls)

### <a id="TpuNullAll2AllManager"></a>`TpuNullAll2AllManager`
- def: [`src/vllm_torchtpu/distributed/tpu_communicator.py:31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_communicator.py#L31)
- doc: Probe-only stub; TPU EP dispatch/combine never goes through it.
- signature: `class TpuNullAll2AllManager(All2AllManagerBase):`
- used by: [`all2all_manager`](tpu_communicator.md#TpuDeviceCommunicator.all2all_manager)

