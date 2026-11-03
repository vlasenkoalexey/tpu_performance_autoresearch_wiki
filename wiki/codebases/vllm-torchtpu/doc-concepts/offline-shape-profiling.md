---
title: Offline single-shape profiling (examples/tpu_profiling.py)
type: doc-concept
provenance: doc
source: docs/developers_guide/profiling/offline.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Offline single-shape profiling (examples/tpu_profiling.py)

## Definition
`examples/tpu_profiling.py` drives vLLM's offline `LLM` API with a synthetic batch of
fixed shape, runs warmup iterations untraced, then captures `--num-iters` generate
calls. It is the tool for a clean trace of **one shape** - a single prefill or a single
decode batch - with no scheduler noise, as opposed to the serving-window and phased
modes.

## In vllm-torchtpu (grounded)
- The example script (not part of the indexed package) sets
  `profiler_config = {"profiler": "torch", "torch_profiler_dir": <dir>}` on the engine
  args and brackets the measured iterations with `llm.start_profile()` /
  `llm.stop_profile()`. That lands in the same worker path as server-side capture,
  [`TPUWorker.profile`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.profile),
  so output layout and rank merge are identical
  ([multi-rank-trace-capture](multi-rank-trace-capture.md)).
- `examples/run_profiling_suite.sh` sweeps a matrix of these runs (uncomment the
  experiments wanted).

## Recipes from the doc

| Goal | Shape |
|---|---|
| Prefill trace | `--input-len 1024 --output-len 1 --batch-size 1` |
| Decode trace | `--input-len 1 --output-len 1 --batch-size 256` |

Both with e.g. `--model Qwen/Qwen3-30B-A3B-FP8 --tensor-parallel-size 4
--enable-expert-parallel --profile-result-dir profiles/<name>`; all `EngineArgs` are
accepted.

## Why it matters / when it applies
- Warmup matters: the first iterations pay compilation, so `--num-iters-warmup` keeps
  compile time out of the trace.
- Use it for kernel-level questions on a single operating point (attention block
  sizes at one KV length, MoE kernel at one token count); use
  [server-side capture](server-side-profiling-and-trace-options.md) or the
  [phased profiler](phased-profiler.md) for realistic mixed batches. The repo's
  evidence rules warn that padding and repeat overhead is invisible at small batch, so
  claims about the hot path need large-batch traces too
  ([perf-evidence-standard](perf-evidence-standard.md)).

## Doc vs code at this commit
The script header comment still says "PyTorch/XLA profiler"; capture goes through
TorchTPU's profiler config in the worker.

## Connections
- Code concepts: [tpu-model-runner](../concepts/tpu-model-runner.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [tracing-annotations](../concepts/tracing-annotations.md)
- Module catalogs: [tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md)
- Related doc-concepts: [server-side-profiling-and-trace-options](server-side-profiling-and-trace-options.md),
  [phased-profiler](phased-profiler.md), [multi-rank-trace-capture](multi-rank-trace-capture.md)

## Source
Extracted from `docs/developers_guide/profiling/offline.md` (kept in place).
