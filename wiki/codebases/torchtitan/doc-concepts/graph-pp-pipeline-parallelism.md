---
title: GraphPP (graph-based pipeline parallelism)
type: doc-concept
provenance: doc
source: torchtitan/experiments/graph_trainer/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# GraphPP (graph-based pipeline parallelism)

## Definition
GraphPP is the `aot_fx_trace` pipeline-parallel path for GraphTrainer. It reuses TorchTitan's eager PP module splitting and PyTorch PP schedules, but traces **one representative microbatch per local stage** with the GraphTrainer tracer and reuses the resulting per-stage graph bundles for every later microbatch. At run time the PP runtime only executes the prebuilt callable for each schedule action.

## In torchtitan (grounded)
- Entry: [`graph_pipeline_llm`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/pipeline.md#graph_pipeline_llm) builds the stages ([`GraphPipelineStage`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/stage.md#GraphPipelineStage)) and accepts the schedules `Interleaved1F1B`, `ZBVZeroBubble`, `DualPipeV`.
- Runtime: [`GraphPipelineRuntime`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/runner.md#GraphPipelineRuntime) maps schedule actions to prebuilt callables; actions are registered via [`register_graph_pp_schedule`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/runner.md#register_graph_pp_schedule).
- Graph building: [`GraphTrainerStageGraphProvider.prepare_graphs`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.md#GraphTrainerStageGraphProvider.prepare_graphs) drives [`_build_stage_graphs`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.md#_build_stage_graphs) after [`_apply_graph_pp_pre_partition_passes`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.md#_apply_graph_pp_pre_partition_passes); the joint graph is cut by [`partition_joint_graph`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/partition.md#partition_joint_graph).
- Per-stage graph kinds: forward/backward; optional FSDP UNSHARD / REDUCE_GRAD graphs ([`split_forward_fsdp_collectives`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.md#split_forward_fsdp_collectives), [`split_backward_fsdp_collectives`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.md#split_backward_fsdp_collectives)); optional dI/dW graphs for split-backward (zero-bubble) schedules ([`split_di_dw_graph`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.md#split_di_dw_graph)); and multiplexed graphs for `OVERLAP_F_B` actions ([`multiplex_fw_bw_graph`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/graph_multiplex.md#multiplex_fw_bw_graph), built by [`_build_graph_pp_overlap_graphs`](../catalog/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.md#_build_graph_pp_overlap_graphs)).
- Regional and full Inductor reuse the standard terminal passes on each extracted callable ([`final_inductor_compile_passes`](../catalog/torchtitan/experiments/graph_trainer/passes.md#final_inductor_compile_passes)).

## Why it matters / when it applies
- **Trace once, replay per microbatch.** Compile cost is paid per stage, not per microbatch, and the extracted callables are the natural unit for later CUDA-graph capture.
- **Subclass boundary.** Extracted graphs run on flat plain-tensor leaves; only values crossing the PP runtime (stage outputs, input grads sent upstream, param grads before assignment to `param.grad`) are rewrapped into DTensors from tracer metadata. Internal values (saved activations, unsharded FSDP params, raw grad leaves, multiplexed intermediates) stay flat.
- **Multiplexed F/B graphs** keep the forward graph's ShapeEnv as the destination and insert backward compute before it, preserving forward collective-size provenance for full Inductor - this is what makes DualPipeV-style overlapped F/B actions compilable.
- Example launch: DeepSeek-V3 debug model with PP=2, 8 microbatches, `Interleaved1F1B`, FSDP=4, EP=2, `--training.disable_cuda_graphs`.
- Limitations (README): no precompile-artifact loading yet; CUDA-graph capture of the steady-state runtime is future work; EP-overlap annotations are not yet composed with GraphPP. The composability table still marks graph-based PP and EP+PP as in progress.
- **TPU relevance.** The partition-per-stage design is the closest analogue in this fork to how the TPU lane would host PP, but the TPU lane's PP story is separate; see [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md).

## Connections
- Code concepts: [graph-trainer](../concepts/graph-trainer.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md)
- Module catalogs: [graph_trainer/graph_pp/pipeline](../catalog/torchtitan/experiments/graph_trainer/graph_pp/pipeline.md), [graph_trainer/graph_pp/runner](../catalog/torchtitan/experiments/graph_trainer/graph_pp/runner.md), [graph_trainer/graph_pp/graph_builder](../catalog/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.md), [graph_trainer/graph_pp/partition](../catalog/torchtitan/experiments/graph_trainer/graph_pp/partition.md)
- Related doc-concepts: [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md), [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md), [simple-fsdp](simple-fsdp.md), [graph-trainer-ep-overlap](graph-trainer-ep-overlap.md)

## Source
Extracted from `torchtitan/experiments/graph_trainer/README.md` (kept in place).
