---
title: 'Module: torchtitan/observability/structured_logger/gantt_generator.py'
type: catalog
provenance: extracted
module: torchtitan/observability/structured_logger/gantt_generator.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.observability.structured_logger.gantt_generator`/
symbols:
  generate_gantt_trace: generate_gantt_trace().
  _collect_paired_and_instants: _collect_paired_and_instants().
  _emit_chrome_events: _emit_chrome_events().
  _assign_tids_per_source: _assign_tids_per_source().
  _resolve_instant_tid: _resolve_instant_tid().
  load_all_records: load_all_records().
---
# Module: [`torchtitan/observability/structured_logger/gantt_generator.py`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/gantt_generator.py)

## Functions
- <a id="_assign_tids_per_source"></a>`_assign_tids_per_source(paired: list[dict])` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/gantt_generator.py#L93) — Assign a Perfetto ``tid`` to every paired span (mutates ``s["tid"]``).
- <a id="_collect_paired_and_instants"></a>`_collect_paired_and_instants(records: list[dict], source_to_pid: dict[str, int])` — [`L238`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/gantt_generator.py#L238) — Pair ``_start`` / ``_end`` via a per-(source, task_name) LIFO stack.
- <a id="_emit_chrome_events"></a>`_emit_chrome_events(*, paired: list[dict], instants: list[dict], source_to_pid: dict[str, int], tid_by_source_and_task: dict[tuple[str, str | None], int])` — [`L401`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/gantt_generator.py#L401) — Build the Chrome Trace event list (one Perfetto process per source).
- <a id="_resolve_instant_tid"></a>`_resolve_instant_tid(*, source: str, task_name: str | None, tid_by_source_and_task: dict[tuple[str, str | None], int])` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/gantt_generator.py#L185) — Pick the Perfetto tid for an instant event (no paired span).
- <a id="generate_gantt_trace"></a>`generate_gantt_trace(log_dir: str, output_path: str)` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/gantt_generator.py#L25) — Merge per-rank JSONL into a Chrome Trace JSON for Perfetto. — documented in [observability](../../../../concepts/observability.md)
- <a id="load_all_records"></a>`load_all_records(log_dir: str)` — [`L211`](../../../../../../../raw/code/torchtitan/torchtitan/observability/structured_logger/gantt_generator.py#L211) — Load all JSONL records from a ``structured_logs/`` directory.

