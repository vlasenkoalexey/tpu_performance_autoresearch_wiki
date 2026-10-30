---
title: 'Module: torchtitan/observability/structured_logger/jsonl_handler.py'
type: catalog
provenance: extracted
module: torchtitan/observability/structured_logger/jsonl_handler.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.observability.structured_logger.jsonl_handler`/
symbols:
  TraceJsonlFormatter._log_dict: TraceJsonlFormatter#_log_dict().
  TraceJsonlHandler.__init__: TraceJsonlHandler#__init__().
  register_jsonl_handler: register_jsonl_handler().
  TraceJsonlFormatter._thread_local: TraceJsonlFormatter#_thread_local.
  TraceJsonlFormatter._refresh_event_delta: TraceJsonlFormatter#_refresh_event_delta().
  TraceJsonlFormatter.format: TraceJsonlFormatter#format().
  TraceJsonlFormatter.rank: TraceJsonlFormatter#rank.
  MAX_MESSAGE_SIZE.MAX_MESSAGE_SIZE: MAX_MESSAGE_SIZE.MAX_MESSAGE_SIZE.
  TraceJsonlFormatter: TraceJsonlFormatter#
  TraceJsonlFormatter.source: TraceJsonlFormatter#source.
  TraceJsonlFormatter._local_rank: TraceJsonlFormatter#_local_rank.
  TraceJsonlFormatter._host_name: TraceJsonlFormatter#_host_name.
  TraceJsonlFormatter._seq_counter: TraceJsonlFormatter#_seq_counter.
  TraceJsonlHandler: TraceJsonlHandler#
  console_logger.console_logger: console_logger.console_logger.
  TraceJsonlFormatter.__init__: TraceJsonlFormatter#__init__().
---
# Module: [`torchtitan/observability/structured_logger/jsonl_handler.py`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py)

## Classes
### <a id="TraceJsonlFormatter"></a>`TraceJsonlFormatter`  ·  implements/extends Formatter
- def: [`torchtitan/observability/structured_logger/jsonl_handler.py:41`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L41)
- doc: Format trace records as one JSON line per record.
- signature: `class TraceJsonlFormatter(logging.Formatter):`
- members:
  - <a id="TraceJsonlFormatter._log_dict"></a>`_log_dict(self, record: logging.LogRecord)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L74) — Build the flat dict emitted as one JSONL line. — documented in [observability](../../../../concepts/observability.md)
  - <a id="TraceJsonlFormatter.format"></a>`format(self, record: logging.LogRecord)` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L71)
  - <a id="TraceJsonlFormatter.rank"></a>`rank` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L61)
  - <a id="TraceJsonlFormatter.source"></a>`source` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L62)
- protocol/private: <a id="TraceJsonlFormatter.__init__"></a>`__init__`[`L59`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L59), <a id="TraceJsonlFormatter._host_name"></a>`_host_name`[`L64`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L64), <a id="TraceJsonlFormatter._local_rank"></a>`_local_rank`[`L63`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L63), <a id="TraceJsonlFormatter._refresh_event_delta"></a>`_refresh_event_delta`[`L160`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L160), <a id="TraceJsonlFormatter._seq_counter"></a>`_seq_counter`[`L65`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L65), <a id="TraceJsonlFormatter._thread_local"></a>`_thread_local`[`L69`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L69)
- uses (calls/refs, reference-scoped): [`ExtraFields`](structured_logging.md#ExtraFields), [`get_step`](step_state.md#get_step), [`LogType`](structured_logging.md#LogType), [`get_relative_step`](step_state.md#get_relative_step), [`get_step_tags`](step_state.md#get_step_tags), [`LOG_TYPE_NAME`](structured_logging.md#ExtraFields.LOG_TYPE_NAME), [`EVENT_NAME`](structured_logging.md#ExtraFields.EVENT_NAME), [`LOG_TYPE`](structured_logging.md#ExtraFields.LOG_TYPE), [`MAX_MESSAGE_SIZE`](jsonl_handler.md#MAX_MESSAGE_SIZE.MAX_MESSAGE_SIZE), [`RELATIVE_STEP`](structured_logging.md#ExtraFields.RELATIVE_STEP), [`STEP`](structured_logging.md#ExtraFields.STEP), [`TASK_NAME`](structured_logging.md#ExtraFields.TASK_NAME), [`VALUE`](structured_logging.md#ExtraFields.VALUE), [`CONTEXT`](structured_logging.md#ExtraFields.CONTEXT), [`TEXT`](structured_logging.md#LogType.TEXT)
- used by: [`__init__`](jsonl_handler.md#TraceJsonlHandler.__init__)

### <a id="TraceJsonlHandler"></a>`TraceJsonlHandler`  ·  implements/extends FileHandler
- def: [`torchtitan/observability/structured_logger/jsonl_handler.py:168`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L168)
- doc: Per-rank JSONL file handler.
- signature: `class TraceJsonlHandler(logging.FileHandler):`
- protocol/private: <a id="TraceJsonlHandler.__init__"></a>`__init__`[`L176`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L176)
- uses (calls/refs, reference-scoped): [`TraceEventsOnlyFilter`](structured_logging.md#TraceEventsOnlyFilter), [`TraceJsonlFormatter`](jsonl_handler.md#TraceJsonlFormatter)
- used by: [`register_jsonl_handler`](jsonl_handler.md#register_jsonl_handler)

## Functions
- <a id="register_jsonl_handler"></a>`register_jsonl_handler(*, structured_logger: logging.Logger, rank: int, source: str, output_dir: str, **kw: Any)` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L189) — Default factory: attach a ``TraceJsonlHandler`` to the structured logger.

## Module values
- <a id="MAX_MESSAGE_SIZE.MAX_MESSAGE_SIZE"></a>`MAX_MESSAGE_SIZE` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L38)
- <a id="console_logger.console_logger"></a>`console_logger` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/jsonl_handler.py#L36)

