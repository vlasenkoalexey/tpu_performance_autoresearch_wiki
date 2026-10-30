---
title: 'Module: torchtitan/experiments/graph_trainer/registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.registry`/
symbols:
  register_memory_policy: register_memory_policy.
  _make_registry_decorator: _make_registry_decorator().
  MEMORY_POLICY_REGISTRY.MEMORY_POLICY_REGISTRY: MEMORY_POLICY_REGISTRY.MEMORY_POLICY_REGISTRY.
  register_trace_input_preparer: register_trace_input_preparer.
  register_trace_call_input_preparer: register_trace_call_input_preparer.
  register_pass_pipeline: register_pass_pipeline.
  register_post_init_hook: register_post_init_hook.
  register_pre_train_step_hook: register_pre_train_step_hook.
  TRACE_INPUT_PREPARERS.TRACE_INPUT_PREPARERS: TRACE_INPUT_PREPARERS.TRACE_INPUT_PREPARERS.
  TRACE_CALL_INPUT_PREPARERS.TRACE_CALL_INPUT_PREPARERS: TRACE_CALL_INPUT_PREPARERS.TRACE_CALL_INPUT_PREPARERS.
  PASS_PIPELINE_REGISTRY.PASS_PIPELINE_REGISTRY: PASS_PIPELINE_REGISTRY.PASS_PIPELINE_REGISTRY.
  _make_registry_decorator.register: _make_registry_decorator().register().
  POST_INIT_HOOKS.POST_INIT_HOOKS: POST_INIT_HOOKS.POST_INIT_HOOKS.
  PRE_TRAIN_STEP_HOOKS.PRE_TRAIN_STEP_HOOKS: PRE_TRAIN_STEP_HOOKS.PRE_TRAIN_STEP_HOOKS.
  _make_registry_decorator.register.decorator: _make_registry_decorator().register().decorator().
---
# Module: [`torchtitan/experiments/graph_trainer/registry.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py)

## Functions
- <a id="_make_registry_decorator"></a>`_make_registry_decorator(registry: dict)` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L24) — Create a decorator that registers a function into the given registry.
- <a id="_make_registry_decorator.register.decorator"></a>`decorator(fn: Callable)` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L28)
- <a id="_make_registry_decorator.register"></a>`register(key: str)` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L27)

## Module values
- <a id="MEMORY_POLICY_REGISTRY.MEMORY_POLICY_REGISTRY"></a>`MEMORY_POLICY_REGISTRY` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L41)
- <a id="PASS_PIPELINE_REGISTRY.PASS_PIPELINE_REGISTRY"></a>`PASS_PIPELINE_REGISTRY` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L42)
- <a id="POST_INIT_HOOKS.POST_INIT_HOOKS"></a>`POST_INIT_HOOKS` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L43)
- <a id="PRE_TRAIN_STEP_HOOKS.PRE_TRAIN_STEP_HOOKS"></a>`PRE_TRAIN_STEP_HOOKS` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L44)
- <a id="TRACE_CALL_INPUT_PREPARERS.TRACE_CALL_INPUT_PREPARERS"></a>`TRACE_CALL_INPUT_PREPARERS` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L46)
- <a id="TRACE_INPUT_PREPARERS.TRACE_INPUT_PREPARERS"></a>`TRACE_INPUT_PREPARERS` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L45)
- <a id="register_memory_policy"></a>`register_memory_policy` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L48)
- <a id="register_pass_pipeline"></a>`register_pass_pipeline` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L49)
- <a id="register_post_init_hook"></a>`register_post_init_hook` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L50)
- <a id="register_pre_train_step_hook"></a>`register_pre_train_step_hook` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L51)
- <a id="register_trace_call_input_preparer"></a>`register_trace_call_input_preparer` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L53)
- <a id="register_trace_input_preparer"></a>`register_trace_input_preparer` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/registry.py#L52)

