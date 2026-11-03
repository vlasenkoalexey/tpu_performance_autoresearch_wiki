---
title: Benchmark harness and perf/accuracy regression gates
type: doc-concept
provenance: doc
source: docs/developers_guide/benchmarking.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Benchmark harness and perf/accuracy regression gates

## Definition
`scripts/vllm/benchmarking/run_benchmarks.sh` is the single harness behind local
performance testing and the CI perf lane (`.buildkite/pipeline_perf.yml`). A config file
fixes model, parallelism, ISL/OSL sweep and concurrency levels; the harness starts one
`vllm serve`, optionally runs discarded warmup passes, runs the serving benchmark per
ISL/OSL x concurrency cell, and saves JSON results. `check_regression.py` then gates the
results against checked-in baselines: performance at a 5% tolerance and accuracy with a
statistically calibrated drop allowance.

## In vllm-torchtpu (grounded)
The harness is under `scripts/` and is not part of the indexed `src/vllm_torchtpu`
package, so there are no catalog symbols to cite; it exercises the serving stack end to
end. Key facts verified in the scripts at this commit:
- Every server it launches gets `--attention-backend ${ATTENTION_BACKEND:-CUSTOM}`,
  i.e. the batched-RPA Pallas backend
  ([`PallasBatchedRPAAttentionBackend`](../catalog/src/vllm_torchtpu/layers/adapter/attention.md#PallasBatchedRPAAttentionBackend)).
  A script comment records that falling back to `FLASH_ATTN` with `block_size=16`
  regresses benchmarks by ~12%.
- `KV_CACHE_DTYPE` defaults to `fp8` (the README says "forced"; it is an overridable
  default).
- Configs live in `configs/*.sh` (42 at this commit), baselines in
  `baselines/perf/<config>.baseline.json` and `baselines/eval/<config>.<task>.baseline.json`.
- `EXTRA_SERVE_ARGS` is appended to the `vllm serve` command by every config, which is
  how profiling flags are injected (see
  [server-side-profiling-and-trace-options](server-side-profiling-and-trace-options.md)).

## Canonical serving recipe (480B nightly cell)
The doc's standalone recipe mirrors what the harness runs for
`qwen3-coder-480b-fp8-tp8-ep`:
```bash
vllm serve --model=Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \
  --tensor-parallel-size=8 --data-parallel-size=1 \
  --max-model-len=16384 --max-num-batched-tokens=8192 --max-num-seqs=512 \
  --async-scheduling --no-enable-prefix-caching \
  --gpu-memory-utilization=0.95 --kv-cache-dtype=fp8 \
  --enable-expert-parallel --quantization fp8 --attention-backend CUSTOM
vllm bench serve --backend vllm --dataset-name random \
  --random-input-len 1024 --random-output-len 1024 --random-range-ratio 0.8 \
  --num-prompts 320 --max-concurrency 64 --request-rate inf --ignore-eos --seed 42
```
(also ISL/OSL 1024/8192 and 8192/1024). These flags are the perf-relevant baseline
knobs: async scheduling on, prefix caching off, fp8 KV cache, EP for MoE, 95% HBM
utilization, 8192-token prefill budget.

## Regression gates
- **Perf (`--mode perf`)**, tolerance 0.05: median TPOT, total token throughput, output
  token throughput, completed requests (as a floor vs baseline), and median TTFT only
  where the baseline entry carries it. Beyond prefill-admission capacity
  (DP x max-num-batched-tokens / prompt-len) median TTFT is queue-position noise, so
  nightly baselines are calibrated with `--gate-ttft-max-concurrency 0`.
- **Accuracy (`--mode eval`)**, default tolerance 1.5 pp (per-config `EVAL_TOLERANCE`):
  `lm_eval` tasks `mmlu_llama`, `mmlu_pro` (`--run-lm-eval`) and `humaneval_plus_tpu`,
  `mbpp_plus_tpu` (`--run-code-eval`, nightly). Where stderr is recorded the allowed
  drop is `max(tolerance, 1.645 * hypot(stderr_baseline, stderr_run))` - a one-sided 95%
  test on the difference of two independent runs (a single raw stderr would fail ~24%
  of clean reruns on N=164 benchmarks). `EVAL_SOFT_FAIL=1` downgrades only eval
  regressions to warnings; perf regressions still fail.
- Suppressing reasoning for eval is per chat template: the default sends
  `enable_thinking: false`, which some templates ignore (they key on `thinking`).

## Why it matters / when it applies
- The repo's PR rules require CI perf thresholds to be updated in the same PR that moves
  performance, and per-mode speedups in perf PRs
  ([perf-evidence-standard](perf-evidence-standard.md)); this harness is where those
  numbers and baselines come from.
- Profiled runs are extra runs: `CAPTURE_PROFILE=1` profiles a separate pass after the
  measured one and its `<cell>.profile.json` is ignored by the regression check, so the
  gate never compares profile-on numbers.
- Speculative decoding has its own runner mode:
  [spec-bench-harness](spec-bench-harness.md).

## Doc vs code at this commit
- The included README says "All configs target TPU v7x-8 (TP=8)" and lists 7 configs;
  `configs/` holds 42, including DP16, TP32 and TP4 topologies (for example
  `deepseek-v4-pro-dp16-ep`, `kimi-k3-tp32-ep`, `qwen3.5-35b-fp8-tp4-ep`), and
  baselines exist for many configs the README table omits.

## Connections
- Code concepts: [ragged-paged-attention-kernel](../concepts/ragged-paged-attention-kernel.md),
  [batched-ragged-paged-attention-kernel](../concepts/batched-ragged-paged-attention-kernel.md),
  [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md),
  [tpu-schedulers](../concepts/tpu-schedulers.md),
  [fused-moe-kernels](../concepts/fused-moe-kernels.md),
  [quantization-methods](../concepts/quantization-methods.md)
- Module catalogs: [layers/adapter/attention](../catalog/src/vllm_torchtpu/layers/adapter/attention.md)
- Related doc-concepts: [spec-bench-harness](spec-bench-harness.md),
  [server-side-profiling-and-trace-options](server-side-profiling-and-trace-options.md),
  [phased-profiler](phased-profiler.md), [perf-evidence-standard](perf-evidence-standard.md),
  [ci-test-markers-and-pipelines](ci-test-markers-and-pipelines.md)

## Source
Extracted from `docs/developers_guide/benchmarking.md`, which includes
`scripts/vllm/benchmarking/README.md` and
`scripts/vllm/benchmarking/unified_benchmark_script.md` (kept in place).
