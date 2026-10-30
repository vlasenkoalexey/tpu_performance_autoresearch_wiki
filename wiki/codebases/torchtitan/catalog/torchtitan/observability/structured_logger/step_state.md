---
title: 'Module: torchtitan/observability/structured_logger/step_state.py'
type: catalog
provenance: extracted
module: torchtitan/observability/structured_logger/step_state.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.observability.structured_logger.step_state`/
symbols:
  set_step: set_step().
  add_step_tag: add_step_tag().
  get_step: get_step().
  get_relative_step: get_relative_step().
  get_step_tags: get_step_tags().
  clear_step_tags: clear_step_tags().
  _TAGS_GLOBAL._TAGS_GLOBAL: _TAGS_GLOBAL._TAGS_GLOBAL.
  _TAGS_CV._TAGS_CV: _TAGS_CV._TAGS_CV.
  _STEP_GLOBAL._STEP_GLOBAL: _STEP_GLOBAL._STEP_GLOBAL.
  _RELATIVE_STEP_GLOBAL._RELATIVE_STEP_GLOBAL: _RELATIVE_STEP_GLOBAL._RELATIVE_STEP_GLOBAL.
  _STEP_CV._STEP_CV: _STEP_CV._STEP_CV.
  _RELATIVE_STEP_CV._RELATIVE_STEP_CV: _RELATIVE_STEP_CV._RELATIVE_STEP_CV.
  _is_in_async_task: _is_in_async_task().
---
# Module: [`torchtitan/observability/structured_logger/step_state.py`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py)

## Functions
- <a id="_is_in_async_task"></a>`_is_in_async_task()` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L87) — True iff called from inside a running asyncio task.
- <a id="add_step_tag"></a>`add_step_tag(tag: str)` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L153) — Annotate the current step. Tags appear in trace JSONL for filtering. — documented in [observability](../../../../concepts/observability.md)
- <a id="clear_step_tags"></a>`clear_step_tags()` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L178) — Reset step tags. — documented in [observability](../../../../concepts/observability.md)
- <a id="get_relative_step"></a>`get_relative_step()` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L137) — Return the relative step (steps since process start), or None.
- <a id="get_step"></a>`get_step()` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L129) — Return the current step, or None if not set. — documented in [observability](../../../../concepts/observability.md)
- <a id="get_step_tags"></a>`get_step_tags()` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L145) — Return the current step tags (CV if non-empty, else global).
- <a id="set_step"></a>`set_step(step: int, *, relative_step: int | None = None)` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L101) — Set the current training step. All subsequent trace records will — documented in [observability](../../../../concepts/observability.md)

## Module values
- <a id="_RELATIVE_STEP_CV._RELATIVE_STEP_CV"></a>`_RELATIVE_STEP_CV` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L81)
- <a id="_RELATIVE_STEP_GLOBAL._RELATIVE_STEP_GLOBAL"></a>`_RELATIVE_STEP_GLOBAL` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L74)
- <a id="_STEP_CV._STEP_CV"></a>`_STEP_CV` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L80)
- <a id="_STEP_GLOBAL._STEP_GLOBAL"></a>`_STEP_GLOBAL` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L73)
- <a id="_TAGS_CV._TAGS_CV"></a>`_TAGS_CV` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L84) — documented in [observability](../../../../concepts/observability.md)
- <a id="_TAGS_GLOBAL._TAGS_GLOBAL"></a>`_TAGS_GLOBAL` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/step_state.py#L75) — documented in [observability](../../../../concepts/observability.md)

