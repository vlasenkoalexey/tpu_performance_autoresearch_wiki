---
title: 'Area: src/vllm_torchtpu/tracing'
type: area
area: 'src/vllm_torchtpu/tracing'
description: 'Shared profiler vocabulary: TraceAnnotation regions that cost nothing unless a profiler is recording and label each step with batch metadata, plus resolution of vLLM start_profile requests into TorchTPU trace directories and options.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/tracing`

## Purpose
Every other subsystem uses this area to make a profiler trace readable. Its entry points are called from the runner, the worker, structured decoding, the KV-transfer connector, the pipeline-parallel ring and wave code, and the vLLM-Omni profiler (21 outside callers). It hands back two things: named `record_function` regions in the trace, and the trace directory and options the TorchTPU profiler is started with.

[tracing-annotations](../concepts/tracing-annotations.md) owns the mechanism. Its design idea is "free when off, self-describing when on". Annotations check whether a profiler session is recording at every entry, so normal serving pays one function call per region. A captured trace carries enough per-step metadata (padded token count, request count, request ids, min/avg/max KV length, and the inference phase with the phased profiler) to tie a device-time slice back to the batch that produced it.

For TPU inference performance this is the first tool in an investigation: it separates prefill from decode mix, shows padding waste and pipeline bubbles, and identifies KV-transfer stalls in an xprof trace. Multi-rank traces it produces can be merged into one file with the utility in [tools](tools.md).

## How the units connect
One unit, owned by [tracing-annotations](../concepts/tracing-annotations.md): `annotation.py` (`TraceAnnotation`, the context manager/decorator), `utils.py` (`extract_request_ids_for_tracing` and the KV-length helpers that turn a batch into compact labels), and `options.py` (`resolve_profile_dir_and_opts`, mapping a `start_profile` request to a directory, tracer levels and TPU trace options). The [TPU worker](worker.md) calls the options half when it starts a profile session.

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/tracing`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/tracing` | 4 | 22 | 21 | [`TraceAnnotation`](../catalog/src/vllm_torchtpu/tracing/annotation.md#TraceAnnotation "src/vllm_torchtpu/tracing/annotation.py:L27"), [`resolve_profile_dir_and_opts`](../catalog/src/vllm_torchtpu/tracing/options.md#resolve_profile_dir_and_opts "src/vllm_torchtpu/tracing/options.py:L101"), [`extract_request_ids_for_tracing`](../catalog/src/vllm_torchtpu/tracing/utils.md#extract_request_ids_for_tracing "src/vllm_torchtpu/tracing/utils.py:L29") | [tracing-annotations](../concepts/tracing-annotations.md) |

<!-- area:auto:end -->
