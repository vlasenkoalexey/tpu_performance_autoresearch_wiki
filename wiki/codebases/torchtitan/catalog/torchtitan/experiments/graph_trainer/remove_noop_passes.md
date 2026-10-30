---
title: 'Module: torchtitan/experiments/graph_trainer/remove_noop_passes.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/remove_noop_passes.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.remove_noop_passes`/
symbols:
  remove_parameter_gradient_markers_pass: remove_parameter_gradient_markers_pass().
  canonicalize_graph_pass: canonicalize_graph_pass().
  remove_identity_view_pass: remove_identity_view_pass().
  remove_identity_slice_pass: remove_identity_slice_pass().
  eliminate_dead_code_pass: eliminate_dead_code_pass().
  remove_detach_pass: remove_detach_pass().
  remove_b2b_transpose_pass: remove_b2b_transpose_pass().
  normalize_view_ops_as_reshape: normalize_view_ops_as_reshape().
  _is_impure_for_dce: _is_impure_for_dce().
  _FORCE_PURE_TARGETS: _FORCE_PURE_TARGETS.
  _IDENTITY_VIEW_TARGETS: _IDENTITY_VIEW_TARGETS.
  _same_shape: _same_shape().
---
# Module: [`torchtitan/experiments/graph_trainer/remove_noop_passes.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py)

## Functions
- <a id="_is_impure_for_dce"></a>`_is_impure_for_dce(node: torch.fx.Node)` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L140) — ``is_impure_node`` for DCE that forces :data:`_FORCE_PURE_TARGETS` pure.
- <a id="_same_shape"></a>`_same_shape(shape1: torch.Size, shape2: torch.Size)` — [`L245`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L245)
- <a id="canonicalize_graph_pass"></a>`canonicalize_graph_pass(gm: torch.fx.GraphModule, example_inputs=None)` — [`L437`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L437) — Canonicalize and simplify the graph as a single pass-list entry.
- <a id="eliminate_dead_code_pass"></a>`eliminate_dead_code_pass(gm: torch.fx.GraphModule, example_inputs=None)` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L153) — Remove dead nodes -- no users and no side effects -- from the graph.
- <a id="normalize_view_ops_as_reshape"></a>`normalize_view_ops_as_reshape(gm: torch.fx.GraphModule, example_inputs=None)` — [`L403`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L403) — Retarget ``aten.view`` and ``aten._unsafe_view`` to ``aten.reshape``.
- <a id="remove_b2b_transpose_pass"></a>`remove_b2b_transpose_pass(gm: torch.fx.GraphModule, example_inputs=None)` — [`L296`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L296) — Remove back-to-back ``t(t(x))`` transposes that cancel out.
- <a id="remove_detach_pass"></a>`remove_detach_pass(gm: torch.fx.GraphModule, example_inputs=None)` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L207) — Remove ``aten.detach.default`` nodes from the graph.
- <a id="remove_identity_slice_pass"></a>`remove_identity_slice_pass(gm: torch.fx.GraphModule, example_inputs=None)` — [`L339`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L339) — Remove identity aten.slice.Tensor ops that select the full dimension.
- <a id="remove_identity_view_pass"></a>`remove_identity_view_pass(gm: torch.fx.GraphModule, example_inputs=None)` — [`L251`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L251) — Remove identity ``view``, ``reshape``, and ``_unsafe_view`` nodes.
- <a id="remove_parameter_gradient_markers_pass"></a>`remove_parameter_gradient_markers_pass(gm: torch.fx.GraphModule, example_inputs: tuple)` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L44) — Move gradient identities onto their values and erase marker aliases.

## Module values
- <a id="_FORCE_PURE_TARGETS"></a>`_FORCE_PURE_TARGETS` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L38)
- <a id="_IDENTITY_VIEW_TARGETS"></a>`_IDENTITY_VIEW_TARGETS` — [`L238`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/remove_noop_passes.py#L238)

