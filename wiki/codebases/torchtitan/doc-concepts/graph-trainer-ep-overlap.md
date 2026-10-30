---
title: GraphTrainer expert-parallel overlap (graph chunking)
type: doc-concept
provenance: doc
source: torchtitan/experiments/graph_trainer/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# GraphTrainer expert-parallel overlap (graph chunking)

## Definition
EP overlap is an experimental GraphTrainer optimization for MoE models with real expert-parallel all-to-alls. Selected regions (whole transformer blocks or just the MoE blocks) are **split into chunks along batch or sequence**, and a scheduling pass interleaves one chunk's token exchange (dispatch/combine all-to-all) with another chunk's compute. It only makes sense with `aot_fx_trace` and `expert_parallel_degree > 1`.

## In torchtitan (grounded)
- Config: [`EpOverlapConfig`](../catalog/torchtitan/experiments/graph_trainer/configs.md#EpOverlapConfig) under [`GraphTrainerCompileConfig.ep_overlap`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.ep_overlap): [`enabled`](../catalog/torchtitan/experiments/graph_trainer/configs.md#EpOverlapConfig.enabled), [`chunk_dim`](../catalog/torchtitan/experiments/graph_trainer/configs.md#EpOverlapConfig.chunk_dim) (`batch` | `seq`), [`strategy`](../catalog/torchtitan/experiments/graph_trainer/configs.md#EpOverlapConfig.strategy) (`graph` default; `eager` wraps module forwards before tracing via [`maybe_apply_ep_overlap_eager_chunking`](../catalog/torchtitan/experiments/graph_trainer/ep_eager_chunk.md#maybe_apply_ep_overlap_eager_chunking)), [`module_fqn`](../catalog/torchtitan/experiments/graph_trainer/configs.md#EpOverlapConfig.module_fqn) (`layers.*` or `layers.*.moe`), [`disable_early_grad_accumulation`](../catalog/torchtitan/experiments/graph_trainer/configs.md#EpOverlapConfig.disable_early_grad_accumulation). Legal combinations are enforced by [`validate_ep_overlap_config`](../catalog/torchtitan/experiments/graph_trainer/configs.md#validate_ep_overlap_config).
- Trace-input contract: before the tracer fakeifies inputs, the `ep_overlap` preparer [`prepare_ep_overlap_trace_inputs`](../catalog/torchtitan/experiments/graph_trainer/ep_chunk_pass.md#prepare_ep_overlap_trace_inputs) (enabled through [`trace_input_preparer_keys`](../catalog/torchtitan/experiments/graph_trainer/configs.md#trace_input_preparer_keys)) marks token-grid dims with Dynamo symbolic-shape metadata.
- Passes: [`populate_chunk_dim_metadata_pass`](../catalog/torchtitan/experiments/graph_trainer/ep_chunk_pass.md#populate_chunk_dim_metadata_pass) and [`ep_overlap_chunk_pass`](../catalog/torchtitan/experiments/graph_trainer/ep_chunk_pass.md#ep_overlap_chunk_pass) consume those symbols to decide which live-ins/live-outs to split; [`isolate_ep_process_group_pass`](../catalog/torchtitan/experiments/graph_trainer/ep_process_group_pass.md#isolate_ep_process_group_pass) moves EP collectives to their own group; [`ep_overlap_schedule_pass`](../catalog/torchtitan/experiments/graph_trainer/ep_overlap_pass.md#ep_overlap_schedule_pass) reorders phases; [`ep_overlap_validate_pass`](../catalog/torchtitan/experiments/graph_trainer/ep_overlap_pass.md#ep_overlap_validate_pass) checks the result.

## Why it matters / when it applies
- MoE step time is often bound by the dispatch/combine all-to-all; the Manifesto cites MoE microbatch overlap as the canonical example of something hooks cannot schedule cleanly but a graph can ("scheduling is just node reordering").
- Supported selections: batch chunking of `layers.*` (whole blocks), batch chunking of `layers.*.moe`, sequence chunking of `layers.*.moe`. Sequence chunking of attention is not supported (attention needs full K/V context).
- Early parameter-gradient accumulation is the performant default; `disable_early_grad_accumulation` restores eager cast/reduction order for strict bitwise tests.
- `enable_fsdp_dense_region_overlap` only composes with graph chunking rooted at `layers.*.moe`; otherwise it is skipped with a warning.
- Validation status: tested DP/EP configurations only; other overlap/sharding combinations should be checked with a loss comparison first. Not yet composed with GraphPP.
- **TPU relevance.** The TPU lane solves the same "hide the all-to-all" problem in its own MoE dispatcher; compare with [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) before porting a chunking idea across.

## Connections
- Code concepts: [graph-trainer](../concepts/graph-trainer.md), [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md), [model-building-blocks](../concepts/model-building-blocks.md), [deepseek-v3-model](../concepts/deepseek-v3-model.md)
- Module catalogs: [graph_trainer/configs](../catalog/torchtitan/experiments/graph_trainer/configs.md), [graph_trainer/ep_chunk_pass](../catalog/torchtitan/experiments/graph_trainer/ep_chunk_pass.md), [graph_trainer/ep_overlap_pass](../catalog/torchtitan/experiments/graph_trainer/ep_overlap_pass.md), [graph_trainer/ep_eager_chunk](../catalog/torchtitan/experiments/graph_trainer/ep_eager_chunk.md)
- Related doc-concepts: [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md), [graph-pp-pipeline-parallelism](graph-pp-pipeline-parallelism.md), [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md)

## Source
Extracted from `torchtitan/experiments/graph_trainer/README.md` (kept in place).
