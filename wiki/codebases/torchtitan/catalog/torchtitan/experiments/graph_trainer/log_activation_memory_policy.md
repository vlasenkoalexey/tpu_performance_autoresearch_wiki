---
title: 'Module: torchtitan/experiments/graph_trainer/log_activation_memory_policy.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/log_activation_memory_policy.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.log_activation_memory_policy`/
symbols:
  log_activation_memory_policy: log_activation_memory_policy().
  _format_bytes: _format_bytes().
  _tensor_nbytes: _tensor_nbytes().
  log_activation_memory_policy._fmt_row: log_activation_memory_policy()._fmt_row().
  _SYMBOLIC_NBYTES: _SYMBOLIC_NBYTES.
  _format_stack_trace: _format_stack_trace().
  _format_shape: _format_shape().
  _tensor_dtype: _tensor_dtype().
  log_activation_memory_policy._sum_concrete_bytes: log_activation_memory_policy()._sum_concrete_bytes().
  _resolve_producing_op: _resolve_producing_op().
  _format_policy: _format_policy().
  _normalize_shape: _normalize_shape().
  _layer_fingerprint: _layer_fingerprint().
  _REPO_ROOT: _REPO_ROOT.
  _PASSTHROUGH_TARGETS: _PASSTHROUGH_TARGETS.
  _parse_stack_frames: _parse_stack_frames().
  _POLICY_SHORT_NAMES: _POLICY_SHORT_NAMES.
  _format_original_aten: _format_original_aten().
  _SYM_VAR_RE: _SYM_VAR_RE.
  _strip_layer_prefix: _strip_layer_prefix().
  log_activation_memory_policy._fmt_target: log_activation_memory_policy()._fmt_target().
---
# Module: [`torchtitan/experiments/graph_trainer/log_activation_memory_policy.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py)

## Functions
- <a id="log_activation_memory_policy._fmt_row"></a>`_fmt_row(idx: int, act: dict, submodule: str)` — [`L287`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L287)
- <a id="log_activation_memory_policy._fmt_target"></a>`_fmt_target(act: dict)` — [`L281`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L281)
- <a id="_format_bytes"></a>`_format_bytes(nbytes: int)` — [`L102`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L102)
- <a id="_format_original_aten"></a>`_format_original_aten(node: torch.fx.Node)` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L185)
- <a id="_format_policy"></a>`_format_policy(node: torch.fx.Node)` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L178)
- <a id="_format_shape"></a>`_format_shape(val: object)` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L52)
- <a id="_format_stack_trace"></a>`_format_stack_trace(stack_trace: str | None)` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L141) — Extract the last torchtitan frame, falling back to the last frame.
- <a id="_layer_fingerprint"></a>`_layer_fingerprint(activations: list[dict])` — [`L205`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L205) — Return a hashable fingerprint for a layer's activation pattern.
- <a id="_normalize_shape"></a>`_normalize_shape(shape: str)` — [`L201`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L201)
- <a id="_parse_stack_frames"></a>`_parse_stack_frames(stack_trace: str)` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L117)
- <a id="_resolve_producing_op"></a>`_resolve_producing_op(node: torch.fx.Node)` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L35) — Walk through getitem/wait_tensor to find the real producing op.
- <a id="_strip_layer_prefix"></a>`_strip_layer_prefix(fqn: str)` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L219) — Strip ``layers.<N>.`` prefix to get the relative submodule path.
- <a id="log_activation_memory_policy._sum_concrete_bytes"></a>`_sum_concrete_bytes(acts: list[dict])` — [`L302`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L302)
- <a id="_tensor_dtype"></a>`_tensor_dtype(val: object)` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L86)
- <a id="_tensor_nbytes"></a>`_tensor_nbytes(val: object)` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L68) — Return byte count, or ``_SYMBOLIC_NBYTES`` for symbolic shapes.
- <a id="log_activation_memory_policy"></a>`log_activation_memory_policy(gm: torch.fx.GraphModule, example_inputs: tuple | None = None)` — [`L232`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L232) — List all activation nodes whose outputs are consumed by backward nodes.

## Module values
- <a id="_PASSTHROUGH_TARGETS"></a>`_PASSTHROUGH_TARGETS` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L27)
- <a id="_POLICY_SHORT_NAMES"></a>`_POLICY_SHORT_NAMES` — [`L170`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L170)
- <a id="_REPO_ROOT"></a>`_REPO_ROOT` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L114)
- <a id="_SYMBOLIC_NBYTES"></a>`_SYMBOLIC_NBYTES` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L65)
- <a id="_SYM_VAR_RE"></a>`_SYM_VAR_RE` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/log_activation_memory_policy.py#L198)

