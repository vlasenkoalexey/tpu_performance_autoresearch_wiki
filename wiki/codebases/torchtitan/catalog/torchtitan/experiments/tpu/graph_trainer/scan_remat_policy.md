---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.scan_remat_policy`/
symbols:
  _aten: _aten.
  scan_body_remat_window: scan_body_remat_window().
  _reached_from_counts: _reached_from_counts().
  _sums_a_routing_map: _sums_a_routing_map().
  count_collectives: count_collectives().
  _is_count_source: _is_count_source().
  _count_values_to_save: _count_values_to_save().
  tag_scan_body_joint_graph: tag_scan_body_joint_graph().
  _COUNT_PASSTHROUGH: _COUNT_PASSTHROUGH.
  _COUNT_SOURCES: _COUNT_SOURCES.
  _SUMS: _SUMS.
  scan_body_remat_window.partition: scan_body_remat_window().partition().
  _is_collective: _is_collective().
  _COUNT_COLLECTIVES: _COUNT_COLLECTIVES.
  _is_bool: _is_bool().
  _depends_on_tangents: _depends_on_tangents().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py)

## Functions
- <a id="_count_values_to_save"></a>`_count_values_to_save(graph: fx.Graph)` — [`L166`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L166) — The count collectives, and every count value downstream of one.
- <a id="_depends_on_tangents"></a>`_depends_on_tangents(graph: fx.Graph)` — [`L190`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L190) — Nodes downstream of a tangent, i.e. the ones only backward can compute.
- <a id="_is_bool"></a>`_is_bool(node: fx.Node)` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L95)
- <a id="_is_collective"></a>`_is_collective(node: fx.Node)` — [`L125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L125)
- <a id="_is_count_source"></a>`_is_count_source(node: fx.Node)` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L119)
- <a id="_reached_from_counts"></a>`_reached_from_counts(graph: fx.Graph)` — [`L132`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L132) — Count sources and everything a count flows to unmixed.
- <a id="_sums_a_routing_map"></a>`_sums_a_routing_map(node: fx.Node)` — [`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L100) — A sum over a boolean (one-hot routing map) tensor, through casts/views.
- <a id="count_collectives"></a>`count_collectives(graph: fx.Graph)` — [`L156`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L156) — The all-reduces in ``graph`` that carry expert counts, in graph order.
- <a id="scan_body_remat_window.partition"></a>`partition(joint_module: fx.GraphModule, joint_inputs, *args, **kwargs)` — [`L243`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L243)
- <a id="scan_body_remat_window"></a>`scan_body_remat_window()` — [`L235`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L235) — Fully rematerialize a scan body, except for its expert counts.
- <a id="tag_scan_body_joint_graph"></a>`tag_scan_body_joint_graph(graph: fx.Graph)` — [`L205`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L205) — Tag a scan body's joint graph to save its expert counts, and only those.

## Module values
- <a id="_COUNT_COLLECTIVES"></a>`_COUNT_COLLECTIVES` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L86)
- <a id="_COUNT_PASSTHROUGH"></a>`_COUNT_PASSTHROUGH` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L66)
- <a id="_COUNT_SOURCES"></a>`_COUNT_SOURCES` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L60)
- <a id="_SUMS"></a>`_SUMS` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L61)
- <a id="__all__"></a>`__all__` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L50)
- <a id="_aten"></a>`_aten` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py#L56)

