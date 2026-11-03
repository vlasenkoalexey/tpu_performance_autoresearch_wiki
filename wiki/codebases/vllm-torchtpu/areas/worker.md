---
title: 'Area: src/vllm_torchtpu/worker'
type: area
area: 'src/vllm_torchtpu/worker'
description: 'TPUWorker, the per-device vLLM worker: binds its rank to one TPU chip, bootstraps distributed state, sizes the KV budget from a profile run, and forwards execute, sample, pipeline, LoRA, profiling and kernel-reload calls to the model runner.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/worker`

## Purpose
There is one worker process per TPU device. The [TPU platform](../concepts/tpu-platform.md) sets `TPUWorker` as vLLM's worker class, and the [executors](executors.md) spawn and drive it. Most of its methods pass straight through to the [model runner](../concepts/tpu-model-runner.md) (`execute_model`, `sample_tokens`, the pipeline `pp_push` / `pp_settle`, draft-token retrieval, LoRA add/remove). The worker itself owns process-level setup.

Three pieces of that setup matter for performance. `init_device` resolves the worker's rank to a physical chip and a slice-global rank (used for trace filenames), configures data-parallel and expert-parallel worlds, and initializes the distributed environment, which decides the device topology every collective runs on. `determine_available_memory` runs the runner's profile forward and computes the KV budget from `gpu_memory_utilization` and post-profile reserves (see [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md)), unless `kv_cache_memory_bytes` overrides it. `compile_or_warm_up_model` triggers the bucket precompile.

The worker also exposes the developer and operations RPCs: profiler start/stop through [tracing](tracing.md), `reload_kernels` for kernel hot-reload (see [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md)), KV-offload prewarm shapes, and weight sync.

## How the units connect
- `tpu_worker.py`: `TPUWorker` (vLLM `WorkerBase`), described above; it builds the runner after binding the device.
- `tpu_rank_binding.py`: maps a worker to its TPU chip (`get_tpu_worker_binding`, `TpuWorkerBinding`, `slice_binding_env`). `LOCAL_RANK` is passed through to torch_tpu as the chip index and is deliberately not permuted. The module explains that putting consecutive PCP ranks on ICI-adjacent chips is a mesh-order problem handled by the PCP mesh builder in [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md), not a device-binding one.
- `runai_repull.py`: `ensure_runai_aux_files` pulls a `gs://` / `s3://` model's non-weight files (config, tokenizer, custom code) on worker hosts of a multi-host slice. vLLM fetches them only on the head host, and workers on other hosts would otherwise lack them.

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/worker`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/worker` | 3 | 82 | 3 | [`get_tpu_worker_binding`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#get_tpu_worker_binding "src/vllm_torchtpu/worker/tpu_rank_binding.py:L212"), [`as_env`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#TpuWorkerBinding.as_env "src/vllm_torchtpu/worker/tpu_rank_binding.py:L95"), [`slice_binding_env`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#slice_binding_env "src/vllm_torchtpu/worker/tpu_rank_binding.py:L121") | section below |

## Small units
### `src/vllm_torchtpu/worker`
- modules: `src/vllm_torchtpu/worker/runai_repull.py`, `src/vllm_torchtpu/worker/tpu_rank_binding.py`, `src/vllm_torchtpu/worker/tpu_worker.py`
- entry points: [`get_tpu_worker_binding`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#get_tpu_worker_binding "src/vllm_torchtpu/worker/tpu_rank_binding.py:L212"), [`as_env`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#TpuWorkerBinding.as_env "src/vllm_torchtpu/worker/tpu_rank_binding.py:L95"), [`slice_binding_env`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#slice_binding_env "src/vllm_torchtpu/worker/tpu_rank_binding.py:L121"), [`local_rank`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#TpuWorkerBinding.local_rank "src/vllm_torchtpu/worker/tpu_rank_binding.py:L84"), [`world_size`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#TpuWorkerBinding.world_size "src/vllm_torchtpu/worker/tpu_rank_binding.py:L85")
- hubs: [`init_device`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.init_device "src/vllm_torchtpu/worker/tpu_worker.py:L194"), [`profile`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.profile "src/vllm_torchtpu/worker/tpu_worker.py:L667"), [`_slice_binding_from_env`](../catalog/src/vllm_torchtpu/worker/tpu_rank_binding.md#_slice_binding_from_env "src/vllm_torchtpu/worker/tpu_rank_binding.py:L142")

<!-- area:auto:end -->
