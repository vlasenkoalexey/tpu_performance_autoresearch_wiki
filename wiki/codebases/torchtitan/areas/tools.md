---
title: 'Area: torchtitan/tools'
type: area
area: 'torchtitan/tools'
description: 'Debug and profiling tools of torchtitan: torch/JAX profiler wiring, memory snapshots, device-info and peak-FLOPS helpers.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/tools`

## Purpose
`torchtitan/tools/` holds the profiler and memory-profiler wrappers, device and peak-FLOPS helpers and misc utilities; see [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md). The TPU lane patches the profiler at import to drive the TorchTPU / JAX (xprof) profilers.

## How the units connect
- [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md) is invoked by [trainer-and-train-loop](../concepts/trainer-and-train-loop.md); its peak-FLOPS helper feeds MFU in [observability](../concepts/observability.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `torchtitan/tools`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/tools` | 4 | 123 | 129 | [`logger`](../catalog/torchtitan/tools/logging.md#logger "torchtitan/tools/logging.py:L12"), [`device_type`](../catalog/torchtitan/tools/utils.md#device_type "torchtitan/tools/utils.py:L219"), [`join`](../catalog/torchtitan/tools/filesystem.md#join "torchtitan/tools/filesystem.py:L101") | [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md) |

<!-- area:auto:end -->
