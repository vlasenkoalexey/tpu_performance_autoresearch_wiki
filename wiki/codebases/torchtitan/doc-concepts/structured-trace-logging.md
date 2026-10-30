---
title: Structured per-rank trace logging (JSONL spans, step tags, Gantt traces)
type: doc-concept
provenance: doc
source: torchtitan/observability/structured_logger/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Structured per-rank trace logging (JSONL spans, step tags, Gantt traces)

## Definition
The structured logger emits **per-rank JSONL events** for phase timing and diagnostics - spans,
instants, and scalars stamped with rank, source, caller, timestamp, and step - for querying during
and after a run. It is designed to be LLM-friendly, to cover both SPMD pretraining and multi-actor
RL (no shared process group), to stay invisible to user code, never block training, and support
pluggable backends via handler factories.

## In torchtitan (grounded)
- Setup: [`init_structured_logger`](../catalog/torchtitan/observability/structured_logger/structured_logging.md#init_structured_logger "torchtitan/observability/structured_logger/structured_logging.py:L224")
  (once per process; `enable=False` or
  [`DebugConfig.enable_structured_logging`](../catalog/torchtitan/config/configs.md#DebugConfig.enable_structured_logging)
  `=False` turns all calls into no-ops).
- Event API: [`log_trace_span`](../catalog/torchtitan/observability/structured_logger/structured_logging.md#log_trace_span "torchtitan/observability/structured_logger/structured_logging.py:L364")
  (context manager/decorator emitting `_start` / `_end` / `_error`),
  [`log_trace_instant`](../catalog/torchtitan/observability/structured_logger/structured_logging.md#log_trace_instant "torchtitan/observability/structured_logger/structured_logging.py:L339"),
  [`log_trace_scalar`](../catalog/torchtitan/observability/structured_logger/structured_logging.md#log_trace_scalar "torchtitan/observability/structured_logger/structured_logging.py:L295");
  payloads are built by [`event_extra`](../catalog/torchtitan/observability/structured_logger/structured_logging.md#event_extra "torchtitan/observability/structured_logger/structured_logging.py:L159").
- Step state: [`set_step`](../catalog/torchtitan/observability/structured_logger/step_state.md#set_step "torchtitan/observability/structured_logger/step_state.py:L101")
  (also clears tags), [`add_step_tag`](../catalog/torchtitan/observability/structured_logger/step_state.md#add_step_tag "torchtitan/observability/structured_logger/step_state.py:L153"),
  [`clear_step_tags`](../catalog/torchtitan/observability/structured_logger/step_state.md#clear_step_tags "torchtitan/observability/structured_logger/step_state.py:L178").
- Pipeline: records go to a dedicated non-propagating logger, are filtered by
  [`TraceEventsOnlyFilter`](../catalog/torchtitan/observability/structured_logger/structured_logging.md#TraceEventsOnlyFilter),
  and written by [`TraceJsonlHandler`](../catalog/torchtitan/observability/structured_logger/jsonl_handler.md#TraceJsonlHandler)
  / [`TraceJsonlFormatter`](../catalog/torchtitan/observability/structured_logger/jsonl_handler.md#TraceJsonlFormatter)
  to `{output_dir}/structured_logs/*.jsonl`; the default factory is
  [`register_jsonl_handler`](../catalog/torchtitan/observability/structured_logger/jsonl_handler.md#register_jsonl_handler).
- Analysis: [`generate_gantt_trace`](../catalog/torchtitan/observability/structured_logger/gantt_generator.md#generate_gantt_trace "torchtitan/observability/structured_logger/gantt_generator.py:L25")
  pairs `_start`/`_end` across all ranks' JSONL and writes a Chrome Trace JSON for Perfetto.

## Why it matters / when it applies
- **Step tags separate outlier steps.** Tag steps that do extra work (`"gc"`, `"eval"`, checkpoint)
  so step-time analysis can filter them - the same hygiene an autoresearch loop needs when computing
  median step time.
- **Cross-rank skew at a glance.** The Gantt trace shows every rank's `fwd_bwd` / optimizer spans on
  one timeline (one process row per source file, async tasks slot-packed), which surfaces stragglers
  and load imbalance without a full device profiler. It is host-side timing only - it complements,
  not replaces, an xprof/device trace for TPU kernel-level attribution.
- **Custom backends** are selected with the `TITAN_STRUCT_LOGGER_HANDLERS` env var (comma-separated
  factory paths; when set, only those run). A factory receives the `structured_logger`, `rank`, and
  `source` and attaches a handler, e.g. a DB sink with a formatter subclass that enriches records.
- **Never blocks training**, so spans are safe to leave on in production runs.

## Connections
- Code concepts: [observability](../concepts/observability.md),
  [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md),
  [rl-training](../concepts/rl-training.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md).
- Module catalogs: [torchtitan/observability/structured_logger/structured_logging](../catalog/torchtitan/observability/structured_logger/structured_logging.md),
  [torchtitan/observability/structured_logger/jsonl_handler](../catalog/torchtitan/observability/structured_logger/jsonl_handler.md),
  [torchtitan/observability/structured_logger/step_state](../catalog/torchtitan/observability/structured_logger/step_state.md),
  [torchtitan/observability/structured_logger/gantt_generator](../catalog/torchtitan/observability/structured_logger/gantt_generator.md).
- Related doc-concepts: [tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md), [sdc-replay-detection](sdc-replay-detection.md).

## Source
Extracted from `torchtitan/observability/structured_logger/README.md` (kept in place).
