---
title: Offline inference example and the online/offline serving entry points
type: doc-concept
provenance: doc
source: docs/api_and_code_examples/offline_inference.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Offline inference example and the online/offline serving entry points

## Definition
The quickstart gives two ways to drive the TPU platform: **online** OpenAI-compatible serving
with `vllm serve` (single chip TP=1, or an 8-device host with TP=8 + expert parallelism) and
**offline** batch generation with `vllm.LLM`. `examples/offline_inference.py` is the offline
reference: it registers the full vLLM `EngineArgs` CLI, so "tensor, expert, and pipeline
parallelism can be selected from the command line", and runs a fixed set of ~40 short prompts
(or `--prompt ...`) through either `LLM.chat` (when the tokenizer has a chat template, or
`--chat-template-kwargs` is passed) or `LLM.generate`, greedy by default.

## In vllm-torchtpu (grounded)
The example contains no TPU-specific code; everything TPU happens behind `vllm.LLM` once the
plugin is loaded (see [plugin-packaging-and-registration](plugin-packaging-and-registration.md)):
[`TPUWorker`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker) sizes the KV cache
([`determine_available_memory`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.determine_available_memory)),
and [`TPUModelRunner`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner)
precompiles the token-bucket ladder in
[`capture_model`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.capture_model)
before the first prompt runs.

Two perf-relevant hooks in the script:
- **Built-in profiling window.** If `--profiler-config.torch_profiler_dir` is set, the script
  calls `llm.start_profile()` / `llm.stop_profile()` around the generate/chat call only, which
  reach [`TPUWorker.profile`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.profile).
  Startup compile and warmup are therefore outside the trace; the captured window is steady-state
  generation for the given prompt set. `examples/offline_lora_inference.py` has the same hook.
- **Compile cost on first start.** The quickstart warns that the first startup compiles graphs
  for the configured token shapes; the knobs that bound that ladder (`--max-model-len`,
  `--max-num-batched-tokens`, `compile_sizes`) also bound startup time.

Owning modules: `worker/tpu_worker.py`, `runner/tpu_runner.py`.

## Why it matters / when it applies
This is the cheapest end-to-end harness for a single-process TPU experiment: no HTTP server, any
engine flag from the CLI, and a profiler window that excludes compilation. For throughput claims,
use the serving benchmark harness instead - the example's prompt set is tiny and fixed, and
greedy sampling with few tokens is decode-dominated.

## Doc vs code at this commit
- The quickstart's TP=8 serving command for Qwen3-Coder-30B-A3B-FP8 omits the
  `--attention-backend CUSTOM`, `--quantization fp8`, `--max-num-seqs` and
  `--gpu-memory-utilization` values the CI config for the same model uses (the benchmark
  harness notes that leaving out CUSTOM falls back to FLASH_ATTN with block size 16, ~12% slower).
  Treat it as a smoke test, not a performance recipe.
- The quickstart's persistence tip points at `VLLM_XLA_CACHE_PATH`, which no module under
  `src/vllm_torchtpu` reads at this commit (see
  [compilation-cache-and-warmup](compilation-cache-and-warmup.md)).

## Connections
- Code concepts: [tpu-model-runner](../concepts/tpu-model-runner.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md),
  [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [tracing-annotations](../concepts/tracing-annotations.md).
- Module catalogs: [worker/tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md),
  [runner/tpu_runner](../catalog/src/vllm_torchtpu/runner/tpu_runner.md).
- Related doc-concepts: [server-side-profiling-and-trace-options](server-side-profiling-and-trace-options.md),
  [benchmark-harness-and-regression-gates](benchmark-harness-and-regression-gates.md),
  [compilation-cache-and-warmup](compilation-cache-and-warmup.md),
  [multi-lora-inference](multi-lora-inference.md),
  [multimodal-encoder-inference](multimodal-encoder-inference.md),
  [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md).

## Source
Extracted from `docs/api_and_code_examples/offline_inference.md` (which embeds
`examples/offline_inference.py`) and `docs/getting_started/quickstart.md` (kept in place).
