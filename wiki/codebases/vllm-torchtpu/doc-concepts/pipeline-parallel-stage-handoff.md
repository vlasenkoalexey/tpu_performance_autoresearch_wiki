---
title: Pipeline parallelism on TPU - wave vs ring hand-off and dynamic chunks
type: doc-concept
provenance: doc
source: docs/user_guide/parallelism.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Pipeline parallelism on TPU - wave vs ring hand-off and dynamic chunks

## Definition
Pipeline parallelism (`--pipeline-parallel-size`) partitions layers into stages. The
parallelism guide describes three TPU-specific mechanisms: **dynamic microbatch
chunking** (`TPU_PP_DYNAMIC_CHUNKS=1`, default) that sizes prefill chunks to keep
bubbles small without recompiling static buckets; the **stage hand-off mode**
`TPU_PP_HANDOFF` - `wave` (default: one collective per forward on every stage, so a
round lasts as long as the slowest forward in flight) or `ring` (each forward's output
is sent point to point to the next stage as soon as it is done, which keeps stages busy
when prompts of different lengths are in flight); and `TPU_PP_RING_DEPTH`, the per-stage
send queue whose buffers are reserved before the KV cache is sized.

## In vllm-torchtpu (grounded)
- Hand-off selection: [`ring_handoff`](../catalog/src/vllm_torchtpu/distributed/pp_push.md#ring_handoff)
  reads [`TPU_PP_HANDOFF`](../catalog/src/vllm_torchtpu/envs.md#TPU_PP_HANDOFF);
  executors are patched by [`patch_executor_for_pp_handoff`](../catalog/src/vllm_torchtpu/distributed/pp_push.md#patch_executor_for_pp_handoff)
  into [`patch_executor_for_pp_wave`](../catalog/src/vllm_torchtpu/distributed/pp_push.md#patch_executor_for_pp_wave)
  or [`patch_executor_for_pp_ring`](../catalog/src/vllm_torchtpu/distributed/pp_push.md#patch_executor_for_pp_ring).
  Under the ring the engine keeps [`ring_extra_steps`](../catalog/src/vllm_torchtpu/distributed/pp_push.md#ring_extra_steps)
  = `max(1, stages // 2)` extra steps in flight (the doc's "twelve for eight stages") so
  stage 0 always has a forward queued while the engine core schedules the next step.
- Ring memory: [`TPUModelRunner.pp_handoff_hbm_reserve_bytes`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.pp_handoff_hbm_reserve_bytes)
  sizes the reserve from [`TPU_PP_RING_DEPTH`](../catalog/src/vllm_torchtpu/envs.md#TPU_PP_RING_DEPTH)
  and the token paddings (0 for the wave); depth < 1 is rejected by
  [`validate_pipeline_parallel_config`](../catalog/src/vllm_torchtpu/platforms/pp_validation.md#validate_pipeline_parallel_config).
- Dynamic chunks: [`_configure_pipeline_chunks`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_configure_pipeline_chunks)
  installs [`TpuPipelineChunkScheduler`](../catalog/src/vllm_torchtpu/core/pp_chunk_scheduler.md#TpuPipelineChunkScheduler)
  (cost model from [`profile_and_install_cost_model`](../catalog/src/vllm_torchtpu/core/pp_chunk_scheduler.md#profile_and_install_cost_model),
  slack [`TPU_PP_CHUNK_SLACK`](../catalog/src/vllm_torchtpu/envs.md#TPU_PP_CHUNK_SLACK)) only
  when no custom scheduler is set, `DP_SCHED_ENABLED` is off for DP > 1, and chunked
  prefill is on; otherwise it logs that chunk sizing is off.
- Dual-core stages: [`VLLM_TPU_DEVICE_ORDER`](../catalog/src/vllm_torchtpu/envs.md#VLLM_TPU_DEVICE_ORDER)
  remaps local ranks to devices ([`_patch_multiproc_worker_global_rank_env`](../catalog/src/vllm_torchtpu/__init__.md#_patch_multiproc_worker_global_rank_env)),
  e.g. `0,2,1,3,4,6,5,7` so a two-core stage does not bind both cores of one chip.

## Doc-vs-code disagreements
The guide's example combines PP with TP (`--tensor-parallel-size 4
--pipeline-parallel-size 2` on Llama-3.1-70B) and calls PP "composable with TP". At this
commit [`validate_pipeline_parallel_config`](../catalog/src/vllm_torchtpu/platforms/pp_validation.md#validate_pipeline_parallel_config)
rejects that with `NotImplementedError` ("tensor parallelism inside a stage ... Use
--tensor-parallel-size 1"; a code comment cites stage TP collectives stalling on the
first serving step). The same validator also rejects, for PP > 1: async scheduling;
speculative decoding other than prefill-only MTP (`num_speculative_tokens=1`) on a KV
producer; KV connectors other than the Raiden ones; multi-device stages (PCP, or EP
across DP ranks) unless the installed torch_tpu builds per-stage meshes; and the legacy
Ray executor. In practice PP is used for disaggregated prefill engines (the
supported-models page lists "PP4 / DP4 disaggregated with host offload").

## Why it matters / when it applies
- Wave is simplest and fine for uniform prompts; ring removes the slowest-forward
  barrier for mixed-length prefills but costs HBM (outgoing + up to 7 landing buffers of
  `max_num_batched_tokens x hidden` per device) taken from the KV budget.
- Ring needs libtpu >= 0.0.50 with torch_tpu >= 0.2.0; the startup self-test fails fast
  otherwise.
- Neither handoff knob joins the compile cache key, so wave/ring A/Bs can share a warm
  cache.

## Connections
- Code concepts: [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md), [tpu-schedulers](../concepts/tpu-schedulers.md), [tpu-model-runner](../concepts/tpu-model-runner.md), [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md)
- Module catalogs: [pp_push](../catalog/src/vllm_torchtpu/distributed/pp_push.md), [pp_validation](../catalog/src/vllm_torchtpu/platforms/pp_validation.md), [pp_chunk_scheduler](../catalog/src/vllm_torchtpu/core/pp_chunk_scheduler.md)
- Related doc-concepts: [composable-6d-parallelism](composable-6d-parallelism.md), [context-parallelism-pcp-dcp](context-parallelism-pcp-dcp.md), [raiden-pd-disaggregation](raiden-pd-disaggregation.md), [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md)

## Source
Extracted from `docs/user_guide/parallelism.md` (section 4, kept in place).
