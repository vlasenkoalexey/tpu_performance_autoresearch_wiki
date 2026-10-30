---
title: 'Module: torchtitan/experiments/rl/observability/metrics/console.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/observability/metrics/console.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.observability.metrics.console`/
symbols:
  log_to_console: log_to_console().
  _COLOR_CYCLE: _COLOR_CYCLE.
  fmt_metric_value: fmt_metric_value().
  _CONSOLE_SEPARATOR: _CONSOLE_SEPARATOR.
  _filter_allow_list: _filter_allow_list().
---
# Module: [`torchtitan/experiments/rl/observability/metrics/console.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/console.py)

## Functions
- <a id="_filter_allow_list"></a>`_filter_allow_list(metrics: dict[str, Any], allow_list: Sequence[str] | None)` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/console.py#L38) — Expand allow_list patterns against metrics keys.
- <a id="fmt_metric_value"></a>`fmt_metric_value(value: Any)` — [`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/console.py#L61) — Format a value for console display.
- <a id="log_to_console"></a>`log_to_console(step: int, metrics: dict[str, Any], *, allow_list: Sequence[str] | None, console_prefix: str = "Train")` — [`L96`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/console.py#L96) — Print one console metric line.

## Module values
- <a id="_COLOR_CYCLE"></a>`_COLOR_CYCLE` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/console.py#L26)
- <a id="_CONSOLE_SEPARATOR"></a>`_CONSOLE_SEPARATOR` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/observability/metrics/console.py#L35)

