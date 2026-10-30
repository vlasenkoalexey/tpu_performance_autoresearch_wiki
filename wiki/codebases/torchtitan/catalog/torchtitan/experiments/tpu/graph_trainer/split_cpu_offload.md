---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.split_cpu_offload`/
symbols:
  thread_host_offload_donors: thread_host_offload_donors().
  is_ao_transfer: is_ao_transfer().
  _ao_transfer_partition: _ao_transfer_partition().
  place_ao_transfer_pairs: place_ao_transfer_pairs().
  HostDonorSpec: HostDonorSpec#
  _first_downstream_partition: _first_downstream_partition().
  HostDonorSpec.shape: HostDonorSpec#shape.
  HostDonorSpec.stride: HostDonorSpec#stride.
  HostDonorSpec.dtype: HostDonorSpec#dtype.
  initialize_pinned_host_buffer: initialize_pinned_host_buffer().
  _preceding_partition: _preceding_partition().
  _as_tuple: _as_tuple().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py)

## Classes
### <a id="HostDonorSpec"></a>`HostDonorSpec`
- def: [`torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py:20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L20)
- signature: `class HostDonorSpec:`
- members:
  - <a id="HostDonorSpec.dtype"></a>`dtype` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L23)
  - <a id="HostDonorSpec.shape"></a>`shape` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L21)
  - <a id="HostDonorSpec.stride"></a>`stride` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L22)
- used by: [`_initialize_host_donors`](graph_split.md#SplitForwardBackwardModule._initialize_host_donors), [`thread_host_offload_donors`](split_cpu_offload.md#thread_host_offload_donors), [`host_donor_specs`](graph_split.md#SplitForwardBackwardModule.host_donor_specs), [`__init__`](graph_split.md#SplitForwardBackwardModule.__init__)

## Functions
- <a id="_ao_transfer_partition"></a>`_ao_transfer_partition(producer: torch.fx.Node, wait: torch.fx.Node, partition_map: dict[torch.fx.Node, int], backward_prefetch_executables: int)` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L74) — Choose one executable for an asynchronous AO copy/completion pair.
- <a id="_as_tuple"></a>`_as_tuple(value: Any)` — [`L200`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L200)
- <a id="_first_downstream_partition"></a>`_first_downstream_partition(node: torch.fx.Node, partition_map: dict[torch.fx.Node, int])` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L45)
- <a id="_preceding_partition"></a>`_preceding_partition(partition: int, partition_map: dict[torch.fx.Node, int], distance: int)` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L64)
- <a id="initialize_pinned_host_buffer"></a>`initialize_pinned_host_buffer(source: torch.Tensor)` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L26) — Create one pinned-host tensor through the normal AO D2H operation.
- <a id="is_ao_transfer"></a>`is_ao_transfer(node: torch.fx.Node, op_name: str | None = None)` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L32) — Return whether ``node`` is an activation-offload placement op.
- <a id="place_ao_transfer_pairs"></a>`place_ao_transfer_pairs(gm: torch.fx.GraphModule, partition_map: dict[torch.fx.Node, int], *, backward_prefetch_executables: int = 0)` — [`L105`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L105) — Place ``(offload, wait)`` and ``(reload, wait)`` pairs in child executables.
- <a id="thread_host_offload_donors"></a>`thread_host_offload_donors(forward: torch.fx.GraphModule)` — [`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py#L208) — Add graph inputs for persistent host-offload buffers.

