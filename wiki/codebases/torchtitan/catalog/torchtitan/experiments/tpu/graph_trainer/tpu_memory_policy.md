---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tpu_memory_policy`/
symbols:
  select_saves: select_saves().
  select_routing: select_routing().
  ROUTING_REGION: ROUTING_REGION.
  SPLASH_ATTENTION_REGION: SPLASH_ATTENTION_REGION.
  select_routing_decisions: select_routing_decisions().
  SAVE_REGIONS.SAVE_REGIONS: SAVE_REGIONS.SAVE_REGIONS.
  resolve_save_regions: resolve_save_regions().
  _tpu_selective_and_offload_memory_policy_pass: _tpu_selective_and_offload_memory_policy_pass().
  select_splash_attention: select_splash_attention().
  select_route_permutations: select_route_permutations().
  full_remat_with_saves: full_remat_with_saves().
  _tpu_selective_memory_policy_pass: _tpu_selective_memory_policy_pass().
  SaveRegion.name: SaveRegion#name.
  _forward_call_nodes: _forward_call_nodes().
  SaveRegion: SaveRegion#
  is_splash_forward_op_name: is_splash_forward_op_name().
  _in_last_n_layers: _in_last_n_layers().
  _full_and_offload_memory_policy_pass: _full_and_offload_memory_policy_pass().
  SaveRegion.select: SaveRegion#select.
  _in_remat_region: _in_remat_region().
  _is_splash_forward_op: _is_splash_forward_op().
  _log_region: _log_region().
  _saved_bytes: _saved_bytes().
  _is_integer_tensor: _is_integer_tensor().
  _ROUTER_FQN_PATTERN: _ROUTER_FQN_PATTERN.
  _SPLASH_FORWARD_OP_NAME: _SPLASH_FORWARD_OP_NAME.
  _is_splash_output: _is_splash_output().
  _tag_saved: _tag_saved().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py)

## Classes
### <a id="SaveRegion"></a>`SaveRegion`
- def: [`torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py:43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L43)
- doc: One kind of forward value that a TPU selective policy may keep.
- signature: `class SaveRegion:`
- members:
  - <a id="SaveRegion.name"></a>`name` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L51)
  - <a id="SaveRegion.select"></a>`select` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L52)
- used by: [`select_saves`](tpu_memory_policy.md#select_saves), [`ROUTING_REGION`](tpu_memory_policy.md#ROUTING_REGION), [`SPLASH_ATTENTION_REGION`](tpu_memory_policy.md#SPLASH_ATTENTION_REGION), [`SAVE_REGIONS`](tpu_memory_policy.md#SAVE_REGIONS.SAVE_REGIONS), [`resolve_save_regions`](tpu_memory_policy.md#resolve_save_regions)  (1 test-only)

## Functions
- <a id="_forward_call_nodes"></a>`_forward_call_nodes(gm: torch.fx.GraphModule)` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L55)
- <a id="_full_and_offload_memory_policy_pass"></a>`_full_and_offload_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L254) — Full recompute plus CPU offload of saved layer boundaries.
- <a id="_in_last_n_layers"></a>`_in_last_n_layers(nodes: list[torch.fx.Node], name: str, n_layers: int)` — [`L311`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L311) — Keep the ``nodes`` in the ``n_layers`` highest-numbered layers.
- <a id="_in_remat_region"></a>`_in_remat_region(node: torch.fx.Node, region: str)` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L63)
- <a id="_is_integer_tensor"></a>`_is_integer_tensor(value: object, ndim: int)` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L67)
- <a id="_is_splash_forward_op"></a>`_is_splash_forward_op(target: object)` — [`L175`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L175)
- <a id="_is_splash_output"></a>`_is_splash_output(value: object)` — [`L181`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L181) — Whether ``value`` is a (4-D BF16 output, 3-D FP32 LSE) pair.
- <a id="_log_region"></a>`_log_region(name: str, selected: int, candidates: int, nbytes: int)` — [`L304`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L304)
- <a id="_saved_bytes"></a>`_saved_bytes(node: torch.fx.Node)` — [`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L289) — Bytes of a node's outputs, from the fake values FX recorded.
- <a id="_tag_saved"></a>`_tag_saved(node: torch.fx.Node, policy: CheckpointPolicy)` — [`L417`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L417) — Tag ``node`` and the getitems that unpack it, which share its tag.
- <a id="_tpu_selective_and_offload_memory_policy_pass"></a>`_tpu_selective_and_offload_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L424`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L424) — ``tpu_selective`` saves kept in HBM, plus CPU offload of layer boundaries.
- <a id="_tpu_selective_memory_policy_pass"></a>`_tpu_selective_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L405`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L405) — Full recompute, except the configured save regions.
- <a id="full_remat_with_saves"></a>`full_remat_with_saves(gm: torch.fx.GraphModule, config: GraphTrainer.Config, save_nodes: Iterable[torch.fx.Node])` — [`L268`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L268) — Recompute everything except ``save_nodes`` and layer boundaries. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="is_splash_forward_op_name"></a>`is_splash_forward_op_name(name: str)` — [`L170`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L170) — Whether ``name`` (``namespace::op``) is a Splash forward op.
- <a id="resolve_save_regions"></a>`resolve_save_regions(save_regions: Sequence[str], last_n_layers: Mapping[str, int], policy: str = "tpu_selective")` — [`L360`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L360) — Check the save-region settings and return the regions they name.
- <a id="select_route_permutations"></a>`select_route_permutations(gm: torch.fx.GraphModule)` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L75) — Return the nodes of the expert sort that ``local_reorder`` marks.
- <a id="select_routing"></a>`select_routing(gm: torch.fx.GraphModule)` — [`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L129) — Return each MoE layer's top-k expert ids and route permutation.
- <a id="select_routing_decisions"></a>`select_routing_decisions(gm: torch.fx.GraphModule)` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L95) — Return each MoE router's top-k expert ids.
- <a id="select_saves"></a>`select_saves(gm: torch.fx.GraphModule, regions: Sequence[SaveRegion], last_n_layers: Mapping[str, int])` — [`L325`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L325) — Choose which candidate nodes of ``regions`` to save.
- <a id="select_splash_attention"></a>`select_splash_attention(gm: torch.fx.GraphModule)` — [`L205`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L205) — Return the Splash forward nodes, whose output and LSE backward reads.

## Module values
- <a id="ROUTING_REGION"></a>`ROUTING_REGION` — [`L158`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L158)
- <a id="SAVE_REGIONS.SAVE_REGIONS"></a>`SAVE_REGIONS` — [`L244`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L244)
- <a id="SPLASH_ATTENTION_REGION"></a>`SPLASH_ATTENTION_REGION` — [`L239`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L239)
- <a id="_ROUTER_FQN_PATTERN"></a>`_ROUTER_FQN_PATTERN` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L92)
- <a id="_SPLASH_FORWARD_OP_NAME"></a>`_SPLASH_FORWARD_OP_NAME` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py#L165)

