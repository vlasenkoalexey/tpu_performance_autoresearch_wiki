---
title: 'Module: src/torch_tpu/_internal/distributed/process_group_utils.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/process_group_utils.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.process_group_utils`/
symbols:
  get_num_collectives_per_pg: get_num_collectives_per_pg().
  ProcessGroupId.ranks: ProcessGroupId#ranks.
  _extract_process_group_id_from_node: _extract_process_group_id_from_node().
  ProcessGroupId: ProcessGroupId#
  ProcessGroupId.__eq__: ProcessGroupId#__eq__().
  ProcessGroupId.__hash__: ProcessGroupId#__hash__().
  ProcessGroupId.__iter__: ProcessGroupId#__iter__().
  ProcessGroupId.__len__: ProcessGroupId#__len__().
  ProcessGroupId.__getitem__: ProcessGroupId#__getitem__().
  _get_collective_op: _get_collective_op().
  ProcessGroupId.__init__: ProcessGroupId#__init__().
  ProcessGroupId.world_size: ProcessGroupId#world_size.
---
# Module: [`src/torch_tpu/_internal/distributed/process_group_utils.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py)

## Classes
### <a id="ProcessGroupId"></a>`ProcessGroupId`
- def: [`src/torch_tpu/_internal/distributed/process_group_utils.py:25`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L25)
- doc: Identifier for a process group consisting of sorted, unique ranks.
- signature: `class ProcessGroupId:`
- members:
  - <a id="ProcessGroupId.ranks"></a>`ranks` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L62)
  - <a id="ProcessGroupId.world_size"></a>`world_size` — [`L63`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L63)
- protocol/private: <a id="ProcessGroupId.__eq__"></a>`__eq__`[`L68`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L68), <a id="ProcessGroupId.__getitem__"></a>`__getitem__`[`L79`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L79), <a id="ProcessGroupId.__hash__"></a>`__hash__`[`L65`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L65), <a id="ProcessGroupId.__init__"></a>`__init__`[`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L35), <a id="ProcessGroupId.__iter__"></a>`__iter__`[`L73`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L73), <a id="ProcessGroupId.__len__"></a>`__len__`[`L76`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L76)
- used by: [`get_num_collectives_per_pg`](process_group_utils.md#get_num_collectives_per_pg), [`_extract_process_group_id_from_node`](process_group_utils.md#_extract_process_group_id_from_node)

## Functions
- <a id="_extract_process_group_id_from_node"></a>`_extract_process_group_id_from_node(node: torch.fx.Node)` — [`L106`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L106) — Extracts the ProcessGroupId from a collective FX node.
- <a id="_get_collective_op"></a>`_get_collective_op(node: torch.fx.Node)` — [`L83`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L83) — Returns the collective OpOverloadPacket if node is a collective call, else None.
- <a id="get_num_collectives_per_pg"></a>`get_num_collectives_per_pg(graph_module: torch.fx.GraphModule)` — [`L178`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/process_group_utils.py#L178) — Returns the number of collective operations per process group in the given graph_module.

