---
title: 'Module: torchtitan/experiments/graph_trainer/ep_process_group_pass.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/ep_process_group_pass.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.ep_process_group_pass`/
symbols:
  isolate_ep_process_group_pass: isolate_ep_process_group_pass().
  _EXTRA_EP_PG_REGISTRY._EXTRA_EP_PG_REGISTRY: _EXTRA_EP_PG_REGISTRY._EXTRA_EP_PG_REGISTRY.
  _shares_process_group_with: _shares_process_group_with().
  _get_or_create_extra_ep_pg: _get_or_create_extra_ep_pg().
  c10d: c10d.
  _is_ep_all_to_all: _is_ep_all_to_all().
  _collective_pg_name: _collective_pg_name().
  _pg_rank_set: _pg_rank_set().
  _same_process_group: _same_process_group().
---
# Module: [`torchtitan/experiments/graph_trainer/ep_process_group_pass.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py)

## Functions
- <a id="_collective_pg_name"></a>`_collective_pg_name(node: fx.Node)` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L38) — Return the process-group name argument for supported c10d collectives.
- <a id="_get_or_create_extra_ep_pg"></a>`_get_or_create_extra_ep_pg(source_pg_name: str)` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L85) — Create or reuse an EP-only PG with the same ranks as ``source_pg_name``.
- <a id="_is_ep_all_to_all"></a>`_is_ep_all_to_all(node: fx.Node)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L29) — Return whether ``node`` is a traced all-to-all using the EP PG slot.
- <a id="_pg_rank_set"></a>`_pg_rank_set(pg_name: str)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L53) — Resolve ``pg_name`` and return its rank set.
- <a id="_same_process_group"></a>`_same_process_group(lhs_pg_name: str, rhs_pg_name: str)` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L61) — Compare process-group object identity after resolving graph PG names.
- <a id="_shares_process_group_with"></a>`_shares_process_group_with(pg_name: str, candidate_pg_names: OrderedSet[str])` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L70) — Return whether ``pg_name`` resolves to any candidate PG object.
- <a id="isolate_ep_process_group_pass"></a>`isolate_ep_process_group_pass(gm: fx.GraphModule, example_inputs: tuple | None = None)` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L116) — Move EP all-to-alls off any non-EP collective PG they share by object.

## Module values
- <a id="_EXTRA_EP_PG_REGISTRY._EXTRA_EP_PG_REGISTRY"></a>`_EXTRA_EP_PG_REGISTRY` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L26)
- <a id="c10d"></a>`c10d` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_process_group_pass.py#L25)

