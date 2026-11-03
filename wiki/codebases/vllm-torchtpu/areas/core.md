---
title: 'Area: src/vllm_torchtpu/core'
type: area
area: 'src/vllm_torchtpu/core'
description: 'Narrow scheduler extensions for TPU serving: time-budgeted pipeline-parallel prefill chunking, a lazy-push engine stepper for deep pipelines, opt-in admission policies, and scheduler-init patches for disaggregated prefill/decode.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/core`

## Purpose
`src/vllm_torchtpu/core` does not replace vLLM's scheduler. It subclasses or patches it at a few seams so that what the scheduler emits is something a TPU deployment can run efficiently. It enters through engine-core patches (`patch_engine_core_for_pp_chunks`, `patch_engine_core_for_lazy_push`) that the platform installs when the matching features are on, and it hands the rest of the repo nothing but a different `SchedulerOutput`: which requests run, and how many prefill tokens each gets in a step.

The load-bearing idea, documented on [tpu-schedulers](../concepts/tpu-schedulers.md), is that a pipeline-parallel step should be budgeted in time rather than tokens. Stages move in lockstep, so a wave lasts as long as its slowest step, and a deep prefill chunk costs far more than a first chunk of the same size. The pipeline chunk scheduler fits a per-stage cost model at startup and clips each prefill chunk to the remaining step time. The lazy-push stepper keeps a lone request from filling a deep pipeline's batch queue with empty steps.

For TPU inference performance this area mostly matters for pipeline-parallel deployments (bubble size and time to first token) and for P/D disaggregation, where the scheduler must agree with the [KV transfer connector](../concepts/kv-transfer-and-disaggregated-serving.md) about when blocks are ready.

## How the units connect
The whole area is one unit owned by [tpu-schedulers](../concepts/tpu-schedulers.md). In outline: `pp_chunks.py` holds the step cost model and the chunk-clipping arithmetic; `pp_chunk_scheduler.py` profiles each stage at startup, installs that model, and patches the engine core so scheduling uses it (`uses_dynamic_chunks` says whether it is active); `pp_lazy_step.py` replaces vLLM's batch-queue step loop for deep pipelines; `tpu_scheduler.py` (DP-aligned prefill admission), `prefix_aware_scheduler.py` (prefix-warmth-first admission) and `experimental/srpt_prefill_scheduler.py` (shortest-remaining-prefill-first) add the opt-in admission orders. Three small patches cover the rest: `raiden_pd.py` keeps Raiden producer response state on the stock schedulers, `eagle_block_drop.py` optionally keeps the trailing prefix-cache block that vLLM drops under EAGLE/MTP, and `abort_on_preemption.py` makes a KV consumer fail a request instead of preempting it when `kv_load_failure_policy` is `fail`. The runner side of the pipeline hand-off lives in [distributed](distributed.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/core`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/core` | 9 | 202 | 9 | [`patch_engine_core_for_lazy_push`](../catalog/src/vllm_torchtpu/core/pp_lazy_step.md#patch_engine_core_for_lazy_push "src/vllm_torchtpu/core/pp_lazy_step.py:L440"), [`patch_engine_core_for_pp_chunks`](../catalog/src/vllm_torchtpu/core/pp_chunk_scheduler.md#patch_engine_core_for_pp_chunks "src/vllm_torchtpu/core/pp_chunk_scheduler.py:L242"), [`uses_dynamic_chunks`](../catalog/src/vllm_torchtpu/core/pp_chunk_scheduler.md#uses_dynamic_chunks "src/vllm_torchtpu/core/pp_chunk_scheduler.py:L48") | [tpu-schedulers](../concepts/tpu-schedulers.md) |

<!-- area:auto:end -->
