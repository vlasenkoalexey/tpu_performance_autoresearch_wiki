---
title: 'Module: torchtitan/observability/structured_logger/structured_logging.py'
type: catalog
provenance: extracted
module: torchtitan/observability/structured_logger/structured_logging.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.observability.structured_logger.structured_logging`/
symbols:
  log_trace_span: log_trace_span#
  event_extra: event_extra().
  init_structured_logger: init_structured_logger().
  log_trace_span.__enter__: log_trace_span#__enter__().
  log_trace_scalar: log_trace_scalar().
  log_trace_span.__exit__: log_trace_span#__exit__().
  log_trace_instant: log_trace_instant().
  ExtraFields: ExtraFields#
  _structured_logger._structured_logger: _structured_logger._structured_logger.
  log_trace_span.__call__: log_trace_span#__call__().
  get_structured_logger_subprocess_init_fn: get_structured_logger_subprocess_init_fn().
  TraceEventsOnlyFilter.filter: TraceEventsOnlyFilter#filter().
  LogType: LogType#
  _StructuredRecordForwarder.emit: _StructuredRecordForwarder#emit().
  _structured_logger_disabled: _structured_logger_disabled().
  log_trace_span.base_name: log_trace_span#base_name.
  log_trace_span._task_name: log_trace_span#_task_name.
  _structured_logger_subprocess_init_fn._structured_logger_subprocess_init_fn: _structured_logger_subprocess_init_fn._structured_logger_subprocess_init_fn.
  log_trace_span.start_type_name: log_trace_span#start_type_name.
  log_trace_span.end_type_name: log_trace_span#end_type_name.
  F: F.
  ExtraFields.LOG_TYPE_NAME: ExtraFields#LOG_TYPE_NAME.
  log_trace_span.stacklevel: log_trace_span#stacklevel.
  _is_initialized._is_initialized: _is_initialized._is_initialized.
  _disabled._disabled: _disabled._disabled.
  _ensure_root_forwarder: _ensure_root_forwarder().
  log_trace_span.async_wrapper: log_trace_span#async_wrapper().
  log_trace_span.sync_wrapper: log_trace_span#sync_wrapper().
  LogType.INSTANT: LogType#INSTANT.
  console_logger.console_logger: console_logger.console_logger.
  ExtraFields.LOG_TYPE: ExtraFields#LOG_TYPE.
  ExtraFields.EVENT_NAME: ExtraFields#EVENT_NAME.
  ExtraFields.STEP: ExtraFields#STEP.
  ExtraFields.VALUE: ExtraFields#VALUE.
  ExtraFields.RELATIVE_STEP: ExtraFields#RELATIVE_STEP.
  ExtraFields.TASK_NAME: ExtraFields#TASK_NAME.
  _StructuredRecordForwarder: _StructuredRecordForwarder#
  TraceEventsOnlyFilter: TraceEventsOnlyFilter#
  TraceEventsOnlyFilter._warned: TraceEventsOnlyFilter#_warned.
  log_trace_span.description: log_trace_span#description.
  log_trace_span.start_time: log_trace_span#start_time.
  _DEFAULT_HANDLER_FACTORY: _DEFAULT_HANDLER_FACTORY.
  LogType.EVENT: LogType#EVENT.
  LogType.TEXT: LogType#TEXT.
  ExtraFields.CONTEXT: ExtraFields#CONTEXT.
  TraceEventsOnlyFilter.__init__: TraceEventsOnlyFilter#__init__().
  log_trace_span.__init__: log_trace_span#__init__().
---
# Module: [`torchtitan/observability/structured_logger/structured_logging.py`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py)

## Classes
### <a id="ExtraFields"></a>`ExtraFields`  ·  implements/extends StrEnum
- def: [`torchtitan/observability/structured_logger/structured_logging.py:75`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L75) — documented in [observability](../../../../concepts/observability.md)
- doc: Keys for the `extra` dict passed to logging calls.
- signature: `class ExtraFields(enum.StrEnum):`
- members:
  - <a id="ExtraFields.CONTEXT"></a>`CONTEXT` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L82)
  - <a id="ExtraFields.EVENT_NAME"></a>`EVENT_NAME` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L80)
  - <a id="ExtraFields.LOG_TYPE"></a>`LOG_TYPE` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L78)
  - <a id="ExtraFields.LOG_TYPE_NAME"></a>`LOG_TYPE_NAME` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L79)
  - <a id="ExtraFields.RELATIVE_STEP"></a>`RELATIVE_STEP` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L84)
  - <a id="ExtraFields.STEP"></a>`STEP` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L81)
  - <a id="ExtraFields.TASK_NAME"></a>`TASK_NAME` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L85)
  - <a id="ExtraFields.VALUE"></a>`VALUE` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L83)
- used by: [`_log_dict`](jsonl_handler.md#TraceJsonlFormatter._log_dict), [`event_extra`](structured_logging.md#event_extra), [`filter`](structured_logging.md#TraceEventsOnlyFilter.filter), [`emit`](structured_logging.md#_StructuredRecordForwarder.emit)

### <a id="LogType"></a>`LogType`  ·  implements/extends StrEnum
- def: [`torchtitan/observability/structured_logger/structured_logging.py:62`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L62) — documented in [observability](../../../../concepts/observability.md)
- doc: Record kind in the JSONL stream.
- signature: `class LogType(enum.StrEnum):`
- members:
  - <a id="LogType.EVENT"></a>`EVENT` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L70)
  - <a id="LogType.INSTANT"></a>`INSTANT` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L71)
  - <a id="LogType.TEXT"></a>`TEXT` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L72)
- used by: [`_log_dict`](jsonl_handler.md#TraceJsonlFormatter._log_dict), [`event_extra`](structured_logging.md#event_extra), [`log_trace_scalar`](structured_logging.md#log_trace_scalar), [`log_trace_instant`](structured_logging.md#log_trace_instant), [`_collect_paired_and_instants`](gantt_generator.md#_collect_paired_and_instants)

### <a id="TraceEventsOnlyFilter"></a>`TraceEventsOnlyFilter`  ·  implements/extends Filter
- def: [`torchtitan/observability/structured_logger/structured_logging.py:180`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L180)
- doc: Defensive filter: drop any record on the structured logger that did not
- signature: `class TraceEventsOnlyFilter(logging.Filter):`
- members:
  - <a id="TraceEventsOnlyFilter.filter"></a>`filter(self, record: logging.LogRecord)` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L207) — documented in [observability](../../../../concepts/observability.md)
- protocol/private: <a id="TraceEventsOnlyFilter.__init__"></a>`__init__`[`L203`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L203), <a id="TraceEventsOnlyFilter._warned"></a>`_warned`[`L205`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L205)
- uses (calls/refs, reference-scoped): [`ExtraFields`](structured_logging.md#ExtraFields), [`LOG_TYPE_NAME`](structured_logging.md#ExtraFields.LOG_TYPE_NAME), [`console_logger`](structured_logging.md#console_logger.console_logger)
- used by: [`__init__`](jsonl_handler.md#TraceJsonlHandler.__init__)

### <a id="_StructuredRecordForwarder"></a>`_StructuredRecordForwarder`  ·  implements/extends Handler
- def: [`torchtitan/observability/structured_logger/structured_logging.py:88`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L88)
- doc: Forward structured records from the root logger to trace handlers.
- signature: `class _StructuredRecordForwarder(logging.Handler):`
- members:
  - <a id="_StructuredRecordForwarder.emit"></a>`emit(self, record: logging.LogRecord)` — [`L134`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L134)
- uses (calls/refs, reference-scoped): [`ExtraFields`](structured_logging.md#ExtraFields), [`_structured_logger`](structured_logging.md#_structured_logger._structured_logger), [`LOG_TYPE_NAME`](structured_logging.md#ExtraFields.LOG_TYPE_NAME)
- used by: [`_ensure_root_forwarder`](structured_logging.md#_ensure_root_forwarder)

### <a id="log_trace_span"></a>`log_trace_span`
- def: [`torchtitan/observability/structured_logger/structured_logging.py:364`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L364) — documented in [observability](../../../../concepts/observability.md)
- doc: Time a block of work; emits `_start` and `_end` records.
- signature: `class log_trace_span:`
- members:
  - <a id="log_trace_span.async_wrapper"></a>`async_wrapper(*args, **kwargs)` — [`L499`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L499) — documented in [observability](../../../../concepts/observability.md)
  - <a id="log_trace_span.sync_wrapper"></a>`sync_wrapper(*args, **kwargs)` — [`L506`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L506) — documented in [observability](../../../../concepts/observability.md)
  - <a id="log_trace_span.base_name"></a>`base_name` — [`L406`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L406)
  - <a id="log_trace_span.description"></a>`description` — [`L407`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L407)
  - <a id="log_trace_span.end_type_name"></a>`end_type_name` — [`L412`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L412)
  - <a id="log_trace_span.stacklevel"></a>`stacklevel` — [`L408`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L408)
  - <a id="log_trace_span.start_time"></a>`start_time` — [`L409`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L409)
  - <a id="log_trace_span.start_type_name"></a>`start_type_name` — [`L411`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L411)
- protocol/private: <a id="log_trace_span.__call__"></a>`__call__`[`L478`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L478), <a id="log_trace_span.__enter__"></a>`__enter__`[`L414`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L414), <a id="log_trace_span.__exit__"></a>`__exit__`[`L441`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L441), <a id="log_trace_span.__init__"></a>`__init__`[`L399`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L399), <a id="log_trace_span._task_name"></a>`_task_name`[`L410`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L410)
- uses (calls/refs, reference-scoped): [`event_extra`](structured_logging.md#event_extra), [`_structured_logger`](structured_logging.md#_structured_logger._structured_logger), [`get_step`](step_state.md#get_step), [`_structured_logger_disabled`](structured_logging.md#_structured_logger_disabled), [`F`](structured_logging.md#F)
- used by: [`build`](../../config/configurable.md#Configurable.Config.build), [`transfer_stream`](../../trainer.md#Trainer.transfer_stream), [`train_step`](../../trainer.md#Trainer.train_step), [`_trainer_loop`](../../experiments/rl/controller.md#Controller._trainer_loop), [`train`](../../trainer.md#Trainer.train), [`model_path`](../../experiments/rl/actors/generator.md#VLLMGenerator.model_path), [`trainer_dp_degree`](../../experiments/rl/controller.md#Controller.trainer_dp_degree), [`_engine_loop`](../../experiments/rl/actors/generator.md#VLLMGenerator._engine_loop), [`_build_model`](../../experiments/rl/actors/trainer.md#PolicyTrainer._build_model), [`forward_backward_step`](../../trainer.md#Trainer.forward_backward_step), [`_rollout_loop`](../../experiments/rl/controller.md#Controller._rollout_loop), [`forward_backward`](../../experiments/rl/actors/trainer.md#PolicyTrainer.forward_backward), [`load`](../../components/checkpointer/base.md#BaseCheckpointManager.load), [`optim_step`](../../experiments/rl/actors/trainer.md#PolicyTrainer.optim_step), [`generate`](../../experiments/rl/actors/generator.md#VLLMGenerator.generate), [`forward_backward_step`](../../experiments/graph_trainer/trainer.md#GraphTrainer.forward_backward_step), [`main`](../../train.md#main), [`_pull_model_state_dict`](../../experiments/rl/actors/generator.md#VLLMGenerator._pull_model_state_dict), [`_collect_validation_rollouts`](../../experiments/rl/controller.md#Controller._collect_validation_rollouts), [`take_finalized`](../../experiments/rl/components/work_buffer.md#RolloutGroupWorkBuffer.take_finalized), [`init_distributed`](../../trainer.md#Trainer.init_distributed), [`setup_async`](../../experiments/rl/controller.md#Controller.setup_async), [`_batcher_loop`](../../experiments/rl/controller.md#Controller._batcher_loop), [`_data_input_loop`](../../experiments/rl/controller.md#Controller._data_input_loop), [`_pull_one`](../../experiments/rl/routing/inter_generator_router.md#InterGeneratorRouter._pull_one), [`validate`](../../experiments/rl/controller.md#Controller.validate), [`device`](../../experiments/rl/actors/trainer.md#PolicyTrainer.device), [`_generator_pull_and_release_buffer_slots`](../../experiments/rl/components/weight_sync.md#WeightSyncManager._generator_pull_and_release_buffer_slots), [`pull_model_state_dict`](../../experiments/rl/actors/generator.md#VLLMGenerator.pull_model_state_dict), [`save`](../../components/checkpointer/base.md#BaseCheckpointManager.save), [`step`](../../tools/profiler.md#Profiler.step), [`score_group`](../../experiments/rl/rubrics/rubric.md#Rubric.score_group), [`_trainer_push`](../../experiments/rl/components/weight_sync.md#WeightSyncManager._trainer_push), [`generate`](../../experiments/rl/controller.md#Controller.generate), [`push_model_state_dict`](../../experiments/rl/actors/trainer.md#PolicyTrainer.push_model_state_dict), [`_weight_sum`](../../experiments/rl/rubrics/rubric.md#Rubric._weight_sum), [`_path`](../../experiments/rl/rollout_recorder.md#RolloutSampleRecorder._path), [`pp_has_last_stage`](../../components/validate.md#Validator.pp_has_last_stage), [`debug`](../../tools/utils.md#GarbageCollection.debug), [`save_checkpoint`](../../experiments/rl/actors/trainer.md#PolicyTrainer.save_checkpoint)  (+1 more)

## Functions
- <a id="_ensure_root_forwarder"></a>`_ensure_root_forwarder()` — [`L142`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L142) — documented in [observability](../../../../concepts/observability.md)
- <a id="_structured_logger_disabled"></a>`_structured_logger_disabled()` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L53) — Whether structured logging is disabled. — documented in [observability](../../../../concepts/observability.md)
- <a id="event_extra"></a>`event_extra(event_type: str, event_name: str | None = None, step: int | None = None, relative_step: int | None = None, value: float | int | None = None, task_name: str | None = None, log_type: LogType = LogType.EVENT)` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L159) — Build the extra dict for a structured JSONL event record. — documented in [observability](../../../../concepts/observability.md)
- <a id="get_structured_logger_subprocess_init_fn"></a>`get_structured_logger_subprocess_init_fn()` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L151) — documented in [observability](../../../../concepts/observability.md)
- <a id="init_structured_logger"></a>`init_structured_logger(source: str, output_dir: str, rank: int | None = None, enable: bool = True)` — [`L224`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L224) — Attach handlers to the structured logger. Call once per process. — documented in [observability](../../../../concepts/observability.md)
- <a id="log_trace_instant"></a>`log_trace_instant(event_type: str, *, stacklevel: int = 2)` — [`L339`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L339) — Emit a zero-duration event or marker (e.g. ``"training_start"``). — documented in [observability](../../../../concepts/observability.md)
- <a id="log_trace_scalar"></a>`log_trace_scalar(scalars: dict[str, float | int], *, stacklevel: int = 2)` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L295) — Emit a record per (name, value) pair. Useful when adding more context — documented in [observability](../../../../concepts/observability.md)

## Module values
- <a id="F"></a>`F` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L29)
- <a id="_DEFAULT_HANDLER_FACTORY"></a>`_DEFAULT_HANDLER_FACTORY` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L48)
- <a id="_disabled._disabled"></a>`_disabled` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L46) — documented in [observability](../../../../concepts/observability.md)
- <a id="_is_initialized._is_initialized"></a>`_is_initialized` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L42) — documented in [observability](../../../../concepts/observability.md)
- <a id="_structured_logger._structured_logger"></a>`_structured_logger` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L37) — documented in [observability](../../../../concepts/observability.md)
- <a id="_structured_logger_subprocess_init_fn._structured_logger_subprocess_init_fn"></a>`_structured_logger_subprocess_init_fn` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L43) — documented in [observability](../../../../concepts/observability.md)
- <a id="console_logger.console_logger"></a>`console_logger` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/structured_logging.py#L32)

