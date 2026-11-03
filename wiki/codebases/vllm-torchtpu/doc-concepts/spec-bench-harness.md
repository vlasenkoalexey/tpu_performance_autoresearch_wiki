---
title: Spec-Bench harness for speculative decoding (batch size x K sweep)
type: doc-concept
provenance: doc
source: docs/developers_guide/benchmarking.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Spec-Bench harness for speculative decoding (batch size x K sweep)

## Definition
`run_benchmarks.sh --mode spec_bench` (or `BENCHMARK_MODE=spec_bench`) measures
speculative decoding on the Spec-Bench dataset by sweeping batch size (`SPEC_BS_LIST`)
against the number of draft tokens `K` (`SPEC_K_LIST`), with `K=0` - a server started
without `--speculative-config` - as the no-speculation baseline. It reports mean E2E
time, speedup vs `K=0`, and acceptance rate per cell.

## In vllm-torchtpu (grounded)
The harness lives under `scripts/vllm/benchmarking/` (not indexed); what it measures is
the [speculative-decoding](../concepts/speculative-decoding.md) subsystem in
`src/vllm_torchtpu/spec_decode/` driven through the model runner. Per cell it:
1. restarts `vllm serve` with `--max-num-seqs <BS>` and `--speculative-config`;
2. runs `SPEC_WARMUP_PROMPTS` warmup prompts (default 20) and `SPEC_REPS` measured passes
   (default 2, `SPEC_NUM_PROMPTS`=100 each) of
   `vllm bench serve --dataset-name spec_bench --max-concurrency <BS>`;
3. writes `bs<BS>/k<K>_rep<N>.json`, aggregated by `summarize_spec_bench.py` into
   `spec_benchmark_summary.{json,md}`.

| Config | Method | Draft | K swept | Topology |
|---|---|---|---|---|
| `qwen3-0.6b-ngram` | ngram | - | 0 1 2 4 | TP=1 (smoke) |
| `llama-3-8b-ngram` | ngram | - | 0 1 2 4 8 | TP=1 |
| `llama-3.3-70b-eagle3` | eagle3 | Llama-3.3-70B-Instruct-Eagle3 | 0-4 | TP=8 |
| `gemma-4-31b-it-mtp` | mtp | gemma-4-31B-it-assistant | 0-5 | TP=8 |
| `qwen3.5-397b-fp8-mtp` | mtp | built-in MTP head | 0-5 | TP=8, EP |
| `qwen3-4b-dflash` | dflash | Qwen3-4B-DFlash-b16 | 0 15 | TP=1 |
| `qwen3-4b-dspark` | dspark | dspark_qwen3_4b_block7 | 0 7 | TP=1 |
| `qwen3.5-35b-fp8-dflash` | dflash | Qwen3.5-35B-A3B-DFlash | 0 15 | DP=2 x TP=4, EP |

Config vars: `SPEC_METHOD` (required when any K > 0), `SPEC_DRAFT_MODEL` /
`SPEC_DRAFT_TP` (defaults to the target TP), `SPEC_BENCH_DATASET` /
`SPEC_BENCH_CATEGORY` (default `summarization`), `SERVED_MODEL_NAME`.

## Why it matters / when it applies
- The harness reports speedup per (BS, K) cell rather than one number, because
  speculation's benefit varies with batch size; a spec-decode change should be judged
  across the grid. Block-drafting methods (dflash, dspark) sweep a single K matching
  their draft block (15 and 7 in the configs above).
- The batch-composition classifier counts draft tokens as decode, so a
  [phased-profiler](phased-profiler.md) trace of a spec-decode server files verify steps
  under the decode phases.
- CI runs the spec-decode e2e tests in dedicated steps (2-chip and 8-chip suites; see
  [ci-test-markers-and-pipelines](ci-test-markers-and-pipelines.md)).

## Connections
- Code concepts: [speculative-decoding](../concepts/speculative-decoding.md),
  [tpu-model-runner](../concepts/tpu-model-runner.md),
  [tpu-schedulers](../concepts/tpu-schedulers.md)
- Related doc-concepts: [benchmark-harness-and-regression-gates](benchmark-harness-and-regression-gates.md),
  [phased-profiler](phased-profiler.md)

## Source
Extracted from `docs/developers_guide/benchmarking.md` (via its include of
`scripts/vllm/benchmarking/README.md`, kept in place).
