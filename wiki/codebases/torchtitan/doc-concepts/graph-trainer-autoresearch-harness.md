---
title: GraphTrainer autoresearch harness
type: doc-concept
provenance: doc
source: torchtitan/experiments/graph_trainer/autoresearch/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# GraphTrainer autoresearch harness

## Definition
An autonomous experiment loop for graph-pass / kernel optimization in GraphTrainer. An LLM agent repeatedly edits **one file** (`torchtitan/experiments/graph_trainer/passes.py`), benchmarks the change, and keeps it only if training-step time improves **and** numerics stay bitwise-identical to the eager reference. It runs until stopped; human and agent communicate only through shared files.

## In torchtitan (grounded)
- The editable surface is the pass-orchestration module: new passes are registered in [`construct_default_graph_passes`](../catalog/torchtitan/experiments/graph_trainer/passes.md#construct_default_graph_passes) or [`compile_time_passes`](../catalog/torchtitan/experiments/graph_trainer/passes.md#compile_time_passes). Read-only context the agent may consult includes [`GraphTrainer`](../catalog/torchtitan/experiments/graph_trainer/trainer.md#GraphTrainer), [`minimal_fx_tracer`](../catalog/torchtitan/experiments/graph_trainer/make_fx_tracer.md#minimal_fx_tracer) and [`apply_compile`](../catalog/torchtitan/experiments/graph_trainer/compile.md#apply_compile).
- Harness files (no code symbols; plain files under `autoresearch/`): `autoresearch.md` (operating manual with `[SETUP]` sections: target, starting graph, scaffolding level, reading scope, numerics-check command), `ideas.md`, `experiment_log.md` (append-only journal), `learnings.md`, `results.tsv` (columns: timestamp, commit, tps, memory_gib, status, mfu_pct, wall_time_s, description), `scripts/run_benchmark.sh` (default: Llama3 8B, FSDP=4 x TP=2, 8192 tokens per DP rank, 20 steps, `aot_fx_trace`).
- The bitwise gate is the same property GraphTrainer's own tests enforce ([`BitwiseDeterministicBase`](../catalog/torchtitan/experiments/graph_trainer/tests/test_bitwise_deterministic.md#BitwiseDeterministicBase)).

## Why it matters / when it applies
- Design properties: **asynchronous** (shared files are the only channel), **auditable** (every experiment logged, commit tree keeps failures), **safe** (numerics is a hard gate; failures revert `passes.py` only, best-so-far stays at HEAD), **compounding** (each keep builds on all prior keeps).
- The manual forbids reading the numerics-test source and inspecting git history, so the agent must rediscover optimizations rather than copy prior commits.
- It is the concrete form of the Manifesto's "a graph is a better substrate for agentic optimization" bet ([graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md)).
- **TPU relevance.** The loop shape (single editable surface, bitwise/parity gate, results TSV, keep-or-revert) mirrors the experiment loop this wiki runs for TPU lanes; the harness itself targets GPUs (H100 benchmark, CUDA graphs, Inductor/Triton passes).

## Connections
- Code concepts: [graph-trainer](../concepts/graph-trainer.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md), [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md)
- Module catalogs: [graph_trainer/passes](../catalog/torchtitan/experiments/graph_trainer/passes.md), [graph_trainer/trainer](../catalog/torchtitan/experiments/graph_trainer/trainer.md)
- Related doc-concepts: [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md), [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md)

## Source
Extracted from `torchtitan/experiments/graph_trainer/autoresearch/README.md` (kept in place).
