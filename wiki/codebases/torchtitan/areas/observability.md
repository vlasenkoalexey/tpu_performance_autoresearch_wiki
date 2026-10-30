---
title: 'Area: torchtitan/observability'
type: area
area: 'torchtitan/observability'
description: 'Observability in torchtitan: metrics and MFU, structured logging, and silent-data-corruption replay checks.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/observability`

## Purpose
`torchtitan/observability/` covers metrics processing (throughput, MFU, memory), the structured JSONL logger, and silent-data-corruption (SDC) replay; see [observability](../concepts/observability.md). For TPU, MFU uses per-device peak FLOPS (halved on v7, which exposes each TensorCore as a device) and is reported as N/A when quantization is active.

## How the units connect
- [observability](../concepts/observability.md) is driven by [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) on log steps; profiling and memory snapshots are in [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `torchtitan/observability`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/observability` | 6 | 149 | 23 | [`log_trace_span`](../catalog/torchtitan/observability/structured_logger/structured_logging.md#log_trace_span "torchtitan/observability/structured_logger/structured_logging.py:L364"), [`add_step_tag`](../catalog/torchtitan/observability/structured_logger/step_state.md#add_step_tag "torchtitan/observability/structured_logger/step_state.py:L153"), [`SDCReplayer`](../catalog/torchtitan/observability/sdc_replayer.md#SDCReplayer "torchtitan/observability/sdc_replayer.py:L318") | [observability](../concepts/observability.md) |

<!-- area:auto:end -->
