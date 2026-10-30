---
title: 'Module: src/torch_tpu/_internal/utils/tracer_utils.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/utils/tracer_utils.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.utils.tracer_utils`/
symbols:
  _pformat_value: _pformat_value().
  pformat_replay: pformat_replay().
  _helper_render_delta: _helper_render_delta().
  pformat_activation_tracer: pformat_activation_tracer().
  _helper_pformat_module_header: _helper_pformat_module_header().
  _pformat_value._pformat_arg: _pformat_value()._pformat_arg().
  link_events: link_events().
  _TensorOrTensors: _TensorOrTensors.
  _pformat_value._pformat_output: _pformat_value()._pformat_output().
  _pformat_value._pformat_outputs: _pformat_value()._pformat_outputs().
  pformat_op_tracer: pformat_op_tracer().
  replay_log: replay_log().
---
# Module: [`src/torch_tpu/_internal/utils/tracer_utils.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py)

## Functions
- <a id="_helper_pformat_module_header"></a>`_helper_pformat_module_header(lines: list[str], event: dict[str, Any], start_time: float, pre_event: dict[str, Any])` — [`L252`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L252) — Pretty-formats a single module. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_helper_render_delta"></a>`_helper_render_delta(lines: list[str], output: _TensorOrTensors, cpu_output: _TensorOrTensors)` — [`L293`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L293) — Renders the delta between the CPU and TPU outputs. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_pformat_value._pformat_arg"></a>`_pformat_arg(key, item)` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L62) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_pformat_value._pformat_output"></a>`_pformat_output(item)` — [`L69`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L69)
- <a id="_pformat_value._pformat_outputs"></a>`_pformat_outputs(idx, item)` — [`L76`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L76)
- <a id="_pformat_value"></a>`_pformat_value(prefix: str, args: tuple[Any, ...] | None = None, kwargs: dict[str, Any] | None = None, output: Any | None = None)` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L39) — Pretty-formats the collected data from ActivationTracer. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="link_events"></a>`link_events(pre_log: Sequence[utils.Event], log: Sequence[utils.Event])` — [`L102`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L102) — Adds 'pre_event' and 'post_event' keys to link events.
- <a id="pformat_activation_tracer"></a>`pformat_activation_tracer(tracer)` — [`L138`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L138) — Pretty-formats the collected data from ActivationTracer. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="pformat_op_tracer"></a>`pformat_op_tracer(tracer: utils.OpTracer)` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L27) — Pretty-formats the collected data from OpTracer.
- <a id="pformat_replay"></a>`pformat_replay(log: Sequence[utils.Event], pre_log: Sequence[utils.Event], replayed_log: Sequence[utils.Event | Exception])` — [`L321`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L321) — Pretty-formats diff of ActivationTracer forward_log and its replay. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="replay_log"></a>`replay_log(log: Sequence[utils.Event], device: str)` — [`L202`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L202) — Reruns the modules and inputs from the forward log.

## Module values
- <a id="_TensorOrTensors"></a>`_TensorOrTensors` — [`L288`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/tracer_utils.py#L288)

