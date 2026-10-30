---
title: 'Module: src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.fx_passes.detect_causal_mask`/
symbols:
  _evaluate_node_on_inputs: _evaluate_node_on_inputs().
  _try_eliminate_causal_mask: _try_eliminate_causal_mask().
  apply: apply().
  _is_causal_mask: _is_causal_mask().
  _MAX_FOLD_NUMEL: _MAX_FOLD_NUMEL.
  _MAX_FOLD_DEPTH: _MAX_FOLD_DEPTH.
  _is_foldable: _is_foldable().
  _SDPA_SPECS._SDPA_SPECS: _SDPA_SPECS._SDPA_SPECS.
---
# Module: [`src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py)

## Functions
- <a id="_evaluate_node_on_inputs"></a>`_evaluate_node_on_inputs(node: Any, placeholder_to_input: dict[torch.fx.Node, Any], gm: torch.fx.GraphModule | None, cache: dict[torch.fx.Node, Any], depth: int = 0)` — [`L103`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py#L103) — Evaluates a node producing a mask tensor. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_is_causal_mask"></a>`_is_causal_mask(tensor: Any)` — [`L23`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py#L23) — Returns True if the tensor represents a lower-triangular causal mask. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_is_foldable"></a>`_is_foldable(target: torch._ops.OpOverload)` — [`L96`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py#L96) — Returns True if `target` is a deterministic, non-mutating op. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_try_eliminate_causal_mask"></a>`_try_eliminate_causal_mask(node: torch.fx.Node, bias_idx: int, is_causal_idx: int, is_bwd: bool, graph: torch.fx.Graph, placeholder_to_input: dict[torch.fx.Node, Any], gm: torch.fx.GraphModule | None, cache: dict[torch.fx.Node, Any])` — [`L186`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py#L186) — Inspects attn_bias in node and eliminates it if it is a causal mask. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="apply"></a>`apply(gm_or_graph: torch.fx.GraphModule | torch.fx.Graph, example_inputs: Sequence[Any] | None = None)` — [`L244`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py#L244) — Replaces redundant causal attention masks in SDPA with is_causal=True. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)

## Module values
- <a id="_MAX_FOLD_DEPTH"></a>`_MAX_FOLD_DEPTH` — [`L93`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py#L93) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_MAX_FOLD_NUMEL"></a>`_MAX_FOLD_NUMEL` — [`L92`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py#L92) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_SDPA_SPECS._SDPA_SPECS"></a>`_SDPA_SPECS` — [`L161`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/detect_causal_mask.py#L161) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)

