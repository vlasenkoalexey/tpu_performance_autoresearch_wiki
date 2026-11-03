---
title: Profile cache and the startup free-HBM probe
type: doc-concept
provenance: doc
source: docs/deployment/kubernetes.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Profile cache and the startup free-HBM probe

## Definition
At startup every TPU worker runs a **profile run** - a throwaway forward at the largest token
bucket with no KV cache allocated - and then measures how much HBM is left to size the KV cache
from `--gpu-memory-utilization`. The profiling graph is compiled into its own `profile_cache`
subdirectory of the vLLM cache root. The Kubernetes doc's rule: keep the compile and model caches
persistent, but put `profile_cache` on an in-memory `emptyDir` "so free-HBM probing always runs
fresh on startup".

## In vllm-torchtpu (grounded)
- [`TPUWorker.determine_available_memory`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.determine_available_memory)
  short-circuits if `kv_cache_memory_bytes` is set; otherwise it calls
  [`TPUModelRunner.profile_run`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.profile_run)
  at `max_num_tokens`, computes the budget with
  [`compute_hbm_budget`](../catalog/src/vllm_torchtpu/utils.md#compute_hbm_budget), subtracts
  [`post_profile_hbm_reserves`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.post_profile_hbm_reserves)
  (KV-connector staging, LoRA slot-write, PP hand-off buffers allocated after the probe), takes the
  minimum across EP/DP ranks via [`min_across_ep_dp`](../catalog/src/vllm_torchtpu/utils.md#min_across_ep_dp),
  and logs a `Memory statistics | ... total_hbm_avail_gb=` line (the number to copy into
  `kv_cache_memory_bytes` for manual control).
- `profile_run` compiles the backbone so XLA materializes real activation buffers (e.g. the FP8
  activation slab), but only for **one** bucket (`compile_sizes = [num_tokens]`): every program
  loaded on the TPU keeps a permanent bottom-of-HBM program-region reservation, so one throwaway
  program keeps that region inside budget for the full bucket ladder that
  [`capture_model`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.capture_model)
  compiles next. It then resets Dynamo and restores the real cache dir.
- [`TPUModelRunner._profile_isolated_cache`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner._profile_isolated_cache)
  redirects the compilation `cache_dir` to `<cache_root>/profile_cache/<hash>`, where the hash
  combines vLLM's AOT-compile factors with
  [`compute_tpu_compilation_hash`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#compute_tpu_compilation_hash),
  so the kv=0-specialized graph never collides with the serving cache (kv > 0) or with other
  models / TP sizes / dtypes.

Owning modules: `worker/tpu_worker.py`, `runner/tpu_runner.py`, `utils.py`,
`compilation/tpu_compiler.py`.

## Why it matters / when it applies
The KV-cache size - and so max concurrency and preemption rate - is decided by this one
measurement. If the profile graph is served from a persistent cache, the manifest comment
explains, "a later run loads the kv=0 graph instead of compiling it and the free-HBM probe
measures nothing", so the KV budget is computed from the wrong HBM picture. Hence: persistent
volume (or GCS mount) for `VLLM_CACHE_ROOT`, but an `emptyDir` with `medium: Memory`
(16 GiB limit in the CI manifests) shadowing `.../profile_cache`. The same applies outside
Kubernetes: wipe `profile_cache` between runs when comparing KV capacity.

## Doc vs code at this commit
The code comments disagree with each other about intent. `_profile_isolated_cache` says the
subdirectory exists "so it can be cached across warm restarts", while `profile_run` says cache
writes are disabled so the kv=0 graph "never lands in the persistent serving cache", and the
deployment manifests treat a persisted `profile_cache` as harmful. The deployment rule (keep it
ephemeral) is the safe reading; the isolation itself is what protects the serving cache either way.

## Connections
- Code concepts: [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md),
  [tpu-model-runner](../concepts/tpu-model-runner.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md).
- Module catalogs: [worker/tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md),
  [runner/tpu_runner](../catalog/src/vllm_torchtpu/runner/tpu_runner.md),
  [utils](../catalog/src/vllm_torchtpu/utils.md),
  [compilation/tpu_compiler](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md).
- Related doc-concepts: [compilation-cache-and-warmup](compilation-cache-and-warmup.md),
  [gke-multihost-jobset-deployment](gke-multihost-jobset-deployment.md),
  [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md),
  [multi-lora-inference](multi-lora-inference.md).

## Source
Extracted from `docs/deployment/kubernetes.md` (kept in place), best practice 3, and the
`profile_cache` volume comment in `.buildkite/kubernetes/manifests/workloads/mp-multihost-slice.yaml`.
