---
title: 'Module: torchtitan/experiments/graph_trainer/cpu_offload.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/cpu_offload.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.cpu_offload`/
symbols:
  apply_cpu_offload_pass: apply_cpu_offload_pass().
  tag_all_offloadable_activations: tag_all_offloadable_activations().
  _is_view: _is_view().
  prefetch_reloads: prefetch_reloads().
  aten: aten.
  _can_offload_node: _can_offload_node().
  _has_recompute_consumer: _has_recompute_consumer().
  _get_storage_chain._walk: _get_storage_chain()._walk().
  _tensor_bytes: _tensor_bytes().
  _has_offloadable_tensor: _has_offloadable_tensor().
  _collect_view_replay_info._walk: _collect_view_replay_info()._walk().
  defer_offload_waits: defer_offload_waits().
  _get_storage_chain: _get_storage_chain().
  _OffloadInfo.first_bwd_consumer: _OffloadInfo#first_bwd_consumer.
  _VIEW_OPS: _VIEW_OPS.
  _collect_view_replay_info: _collect_view_replay_info().
  _classify_forward_backward: _classify_forward_backward().
  _get_reload_layer: _get_reload_layer().
  _OffloadInfo.replay_views: _OffloadInfo#replay_views.
  _MIN_OFFLOAD_BYTES: _MIN_OFFLOAD_BYTES.
  _OffloadInfo: _OffloadInfo#
  _OffloadInfo.node: _OffloadInfo#node.
  _OffloadInfo.direct_bwd_users: _OffloadInfo#direct_bwd_users.
  _OffloadInfo.view_bwd_redirects: _OffloadInfo#view_bwd_redirects.
  _AO_OPS: _AO_OPS.
  _find_last_tensor_consumer: _find_last_tensor_consumer().
  _get_aten_target: _get_aten_target().
  _is_collective_or_wait: _is_collective_or_wait().
  _tensor_is_contiguous: _tensor_is_contiguous().
---
# Module: [`torchtitan/experiments/graph_trainer/cpu_offload.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py)

## Classes
### <a id="_OffloadInfo"></a>`_OffloadInfo`  ·  implements/extends NamedTuple
- def: [`torchtitan/experiments/graph_trainer/cpu_offload.py:432`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L432)
- signature: `class _OffloadInfo(NamedTuple):`
- members:
  - <a id="_OffloadInfo.direct_bwd_users"></a>`direct_bwd_users` — [`L434`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L434)
  - <a id="_OffloadInfo.first_bwd_consumer"></a>`first_bwd_consumer` — [`L437`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L437)
  - <a id="_OffloadInfo.node"></a>`node` — [`L433`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L433)
  - <a id="_OffloadInfo.replay_views"></a>`replay_views` — [`L435`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L435)
  - <a id="_OffloadInfo.view_bwd_redirects"></a>`view_bwd_redirects` — [`L436`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L436)
- used by: [`apply_cpu_offload_pass`](cpu_offload.md#apply_cpu_offload_pass)

## Functions
- <a id="_can_offload_node"></a>`_can_offload_node(node: Node)` — [`L196`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L196) — Check if a node's output can be profitably offloaded to CPU.
- <a id="_classify_forward_backward"></a>`_classify_forward_backward(gm: torch.fx.GraphModule)` — [`L273`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L273) — Classify nodes in a make_fx traced joint graph as forward or backward.
- <a id="_collect_view_replay_info"></a>`_collect_view_replay_info(node: Node)` — [`L232`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L232) — Collect view chain nodes and backward consumers reachable through views.
- <a id="_find_last_tensor_consumer"></a>`_find_last_tensor_consumer(node: Node)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L63) — Return a Tensor-producing node for wait_tensor's last_use_of_storage arg.
- <a id="_get_aten_target"></a>`_get_aten_target(node: Node)` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L112) — Get the overloadpacket for an aten op node, for overload-agnostic matching.
- <a id="_get_reload_layer"></a>`_get_reload_layer(reload_node: Node)` — [`L651`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L651) — Get the layer ID of an offloaded activation from the reload node's metadata.
- <a id="_get_storage_chain"></a>`_get_storage_chain(node: Node)` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L125) — Walk the view chain to find all nodes sharing this tensor's storage.
- <a id="_has_offloadable_tensor"></a>`_has_offloadable_tensor(node: Node)` — [`L184`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L184) — Check if a node produces a tensor worth offloading (large, contiguous).
- <a id="_has_recompute_consumer"></a>`_has_recompute_consumer(node: Node)` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L216) — Check if any forward user (or transitive view user) is tagged for recomputation.
- <a id="_is_collective_or_wait"></a>`_is_collective_or_wait(node: Node)` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L156) — Check if a node is a distributed collective or wait op.
- <a id="_is_view"></a>`_is_view(node: Node)` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L120) — Check if a node produces a view (aliased memory, not a new allocation).
- <a id="_tensor_bytes"></a>`_tensor_bytes(val: torch.Tensor)` — [`L172`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L172) — Get tensor size in bytes, handling symbolic FakeTensors gracefully.
- <a id="_tensor_is_contiguous"></a>`_tensor_is_contiguous(val: torch.Tensor)` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L163) — Check contiguity, handling symbolic FakeTensors gracefully.
- <a id="_get_storage_chain._walk"></a>`_walk(n: Node)` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L140)
- <a id="_collect_view_replay_info._walk"></a>`_walk(n: Node, in_chain: bool)` — [`L252`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L252)
- <a id="apply_cpu_offload_pass"></a>`apply_cpu_offload_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None, *, prefetch_lookahead: int = 1, defer_n_layers: int = 1)` — [`L440`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L440) — Insert ao offload/reload/wait_tensor ops for nodes tagged ``MUST_CPU_OFFLOAD``. — documented in [tpu-graph-trainer](../../../../concepts/tpu-graph-trainer.md)
- <a id="defer_offload_waits"></a>`defer_offload_waits(gm: torch.fx.GraphModule, wait_offload_map: dict[Node, Node], n_layers: int = 1)` — [`L663`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L663) — Place each forward wait at a legal, overlap-friendly region.
- <a id="prefetch_reloads"></a>`prefetch_reloads(gm: torch.fx.GraphModule, n_layers: int)` — [`L736`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L736) — Move ao.reload nodes N layers earlier in the backward for prefetching.
- <a id="tag_all_offloadable_activations"></a>`tag_all_offloadable_activations(gm: torch.fx.GraphModule, example_inputs: tuple | None = None, *, cpu_budget_gb: float = 100)` — [`L303`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L303) — Tag saved activations eligible for CPU offloading.

## Module values
- <a id="_AO_OPS"></a>`_AO_OPS` — [`L656`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L656)
- <a id="_MIN_OFFLOAD_BYTES"></a>`_MIN_OFFLOAD_BYTES` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L109)
- <a id="_VIEW_OPS"></a>`_VIEW_OPS` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L87)
- <a id="aten"></a>`aten` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/cpu_offload.py#L55)

