---
title: 'Module: src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.fx_passes.fold_gqa`/
symbols:
  apply: apply().
  _extract_repeat_kv_source: _extract_repeat_kv_source().
  _detect_repeat_kv_backward_reduction: _detect_repeat_kv_backward_reduction().
  _RESHAPE_TARGETS: _RESHAPE_TARGETS.
  _SDPA_FORWARD_TARGETS: _SDPA_FORWARD_TARGETS.
  _SDPA_BACKWARD_TARGETS: _SDPA_BACKWARD_TARGETS.
  _EXPAND_TARGETS: _EXPAND_TARGETS.
  _UNSQUEEZE_TARGETS: _UNSQUEEZE_TARGETS.
  _SUM_TARGETS: _SUM_TARGETS.
  _SQUEEZE_TARGETS: _SQUEEZE_TARGETS.
  _erase_unused_chain: _erase_unused_chain().
---
# Module: [`src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py)

## Functions
- <a id="_detect_repeat_kv_backward_reduction"></a>`_detect_repeat_kv_backward_reduction(grad_consumer: fx.Node, expected_group_size: int | None = None)` — [`L151`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L151) — Detects autograd backward reduction of repeat_kv. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_erase_unused_chain"></a>`_erase_unused_chain(node: fx.Node, graph: fx.Graph)` — [`L242`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L242) — Erases node and any of its inputs that become dead. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_extract_repeat_kv_source"></a>`_extract_repeat_kv_source(node: fx.Node)` — [`L76`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L76) — Extracts (orig_tensor_node, group_size) if node is a repeat_kv expansion. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="apply"></a>`apply(gm_or_graph: torch.fx.GraphModule | torch.fx.Graph)` — [`L253`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L253) — Folds repeat_kv head expansion into SDPA forward and backward passes. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)

## Module values
- <a id="_EXPAND_TARGETS"></a>`_EXPAND_TARGETS` — [`L54`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L54) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_RESHAPE_TARGETS"></a>`_RESHAPE_TARGETS` — [`L48`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L48) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_SDPA_BACKWARD_TARGETS"></a>`_SDPA_BACKWARD_TARGETS` — [`L43`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L43) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_SDPA_FORWARD_TARGETS"></a>`_SDPA_FORWARD_TARGETS` — [`L37`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L37) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_SQUEEZE_TARGETS"></a>`_SQUEEZE_TARGETS` — [`L69`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L69) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_SUM_TARGETS"></a>`_SUM_TARGETS` — [`L64`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L64) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_UNSQUEEZE_TARGETS"></a>`_UNSQUEEZE_TARGETS` — [`L59`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/fold_gqa.py#L59) — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)

