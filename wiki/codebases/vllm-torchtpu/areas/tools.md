---
title: 'Area: src/vllm_torchtpu/tools'
type: area
area: 'src/vllm_torchtpu/tools'
description: 'Offline profiling utility: merges a multi-chip run''s per-rank xplane trace captures into a single XSpace file, renumbering device planes and deduplicating host metadata.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/tools`

## Purpose
This area holds a standalone command-line tool, not part of serving (nothing in the package imports it). A multi-chip profiler capture writes one `.xplane.pb` per worker into a single `plugins/profile/<timestamp>/` directory. The tool combines those files into one XSpace file.

Its own docstring notes that it is not needed for the open-source `xprof --logdir` workflow, which already reads the whole directory as one distributed session. It exists for consumers that accept exactly one trace file, and for attaching a single artifact to a bug report. Merging is more than concatenation. Every rank names its own chip `/device:TPU:0` and ships a full copy of the host metadata plane, so the tool renumbers device planes globally and keeps one metadata plane.

For TPU inference performance work it sits downstream of the profiler path in [tracing](tracing.md): the [trace annotations](../concepts/tracing-annotations.md) label the per-rank traces, and this tool makes them portable as one file.

## How the units connect
- `merge_xplane.py`: `discover_sessions` groups trace files under the given paths into capture sessions (one per profile window), `merge_session` writes one merged XSpace per session and reports a `MergeResult`, and `main` is the CLI.
- `xplane_pb2.py` is the generated protobuf module for the XSpace/XPlane schema the merger reads and writes.

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/tools`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/tools` | 2 | 49 | 0 | (internal) | section below |

## Small units
### `src/vllm_torchtpu/tools`
- modules: `src/vllm_torchtpu/tools/merge_xplane.py`, `src/vllm_torchtpu/tools/xplane_pb2.py`
- entry points: (none - internal unit)
- hubs: [`main`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#main "src/vllm_torchtpu/tools/merge_xplane.py:L529"), [`merge_session`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#merge_session "src/vllm_torchtpu/tools/merge_xplane.py:L396"), [`_make_session`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#_make_session "src/vllm_torchtpu/tools/merge_xplane.py:L199")

<!-- area:auto:end -->
