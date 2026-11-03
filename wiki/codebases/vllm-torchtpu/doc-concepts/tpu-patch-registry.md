---
title: TPU patch registry (ordered lifecycle patches)
type: doc-concept
provenance: doc
source: docs/developers_guide/tpu_patch_mechanism.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# TPU patch registry (ordered lifecycle patches)

## Definition
vllm-torchtpu is a plugin, not a fork, so every change it makes to upstream vLLM
behavior (scheduler, KV cache, compile cache key, loaders, model families) is a
monkey-patch. All of them are declared in one ordered `PATCHES` tuple; each entry
names a lazily-imported `module:callable` target and the lifecycle **stages** at
which it is eligible. Lifecycle entry points call `apply(stage, model_config=...)`,
and tuple order is execution order within a stage.

## In vllm-torchtpu (grounded)
- The registry lives in `src/vllm_torchtpu/patch_registry.py`:
  [`Patch`](../catalog/src/vllm_torchtpu/patch_registry.md#Patch) (fields `target`,
  `stages`, `model_config`, `refresh`),
  [`PATCHES`](../catalog/src/vllm_torchtpu/patch_registry.md#PATCHES),
  [`apply`](../catalog/src/vllm_torchtpu/patch_registry.md#apply), the lazy importer
  [`_invoke`](../catalog/src/vllm_torchtpu/patch_registry.md#_invoke), and the fork hook
  [`_reset_after_fork`](../catalog/src/vllm_torchtpu/patch_registry.md#_reset_after_fork).
- The five stages and their entry points (verified at this commit):

| Stage | Entry point | Typical use |
|---|---|---|
| `import` | bottom of `env_override.py` | Import-time prerequisites (currently [`_patch_jax_pallas_fori_lowering`](../catalog/src/vllm_torchtpu/env_override.md#_patch_jax_pallas_fori_lowering)) |
| `platform_activation` | [`TpuPlatform.check_and_update_config`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.check_and_update_config) | Shared patches + model patches with `vllm_config.model_config` |
| `engine_core` | [`_run_engine_core_with_tpu_patches`](../catalog/src/vllm_torchtpu/__init__.md#_run_engine_core_with_tpu_patches) | Scheduler / KV-cache / offload / multimodal patches in the engine-core process |
| `worker_init` | [`TPUWorker.__init__`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.__init__) | Shared patches in every (including spawned) worker |
| `model_load` | [`TPUWorker.load_model`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.load_model) | Model-specific patches with `self.model_config` |

- Stage shorthands: `_ACTIVE = (platform_activation, worker_init)` and `_ENGINE` adds
  `engine_core`. Most perf-relevant patches are `_ACTIVE` (compile cache key and
  piecewise backend patches, MoE admission, custom-op registration) or `_ENGINE`
  (hybrid PCP block sizes, offloading config, prefix-hit and preemption behavior),
  because a patch installed in a worker does not affect the engine-core process that
  builds the scheduler and KV connector.
- Example `_ACTIVE` entry from the doc:
  [`patch_default_loader_ep_weight_filter`](../catalog/src/vllm_torchtpu/model_loader_patches.md#patch_default_loader_ep_weight_filter).
  Model-specific example:
  [`maybe_patch_qwen3_vl`](../catalog/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.md#maybe_patch_qwen3_vl),
  registered at `("platform_activation", "model_load")` with `model_config=True`.
- Refresh example: [`_patch_vllm_hybrid_pcp_block_sizes`](../catalog/src/vllm_torchtpu/__init__.md#_patch_vllm_hybrid_pcp_block_sizes)
  and [`_patch_vllm_merge_multimodal_embeddings`](../catalog/src/vllm_torchtpu/__init__.md#_patch_vllm_merge_multimodal_embeddings)
  use themselves as `refresh` so late `from x import f` bindings in consumers get
  re-pointed at later lifecycle boundaries.

## Contract (from the doc, checked against code)
- **Completion is keyed by target string**, is process-local, and is shared across
  stages. Only a literal `False` return leaves an entry eligible for retry; any other
  return (including `None` for an intentional no-op) marks it complete. So a model
  patch must return `False` when `model_config` is `None` or does not match, to get
  another chance at `model_load`. A completed model patch will not run again for a
  different model in the same process.
- Exceptions propagate and stop that stage's pass; earlier completions stay recorded,
  the failing entry stays retryable, nothing is rolled back - patches must be
  idempotent against double wrapping.
- Spawned processes start with an empty registry; forked children inherit installed
  patches and completion records (the fork hook resets only the `RLock` and
  in-progress tracking). Re-entry into the same stage returns immediately.
- The `import` stage must stay light: its targets must not eagerly import TorchTPU or
  resolve vLLM's platform, and `patch_registry.py` must not grow top-level
  implementation imports.
- The INFO log `Completed TPU patch callbacks at <stage>: ...` counts permanent no-ops
  too, so it does **not** prove a wrapper was installed or a feature exercised.

## Why it matters / when it applies
For perf work, many "why is this config slow / recompiling / using the wrong block
size" questions resolve to whether a given patch ran in the right **process**. Parent
platform activation does not cover spawned workers, and engine-core-side behavior
(scheduler, KV connector, offload sizing) needs `engine_core`. When adding a
performance patch, pick stages by where the patched code executes, place it after its
prerequisites in the tuple, and update the manifest assertions in
`tests/platforms/test_patch_registry.py`.

## Doc vs code at this commit
- The doc lists `platform_activation`'s entry as `TpuPlatform.check_and_update_config`;
  the code also calls `apply("platform_activation", ...)` from the experimental export
  path (`experimental/export/checkpoint.py`), which the doc does not mention.
- `vllm_torchtpu.layers.adapter.rotary_embedding` appears twice in `PATCHES` (near
  the top and again after `vision_attention`); because completion is keyed by target,
  the second entry is a no-op at runtime.
- `maybe_patch_qwen3_next` is registered at the model stages without
  `model_config=True`, unlike the recipe the doc gives for model patches.

## Connections
- Code concepts: [tpu-platform](../concepts/tpu-platform.md),
  [vllm-model-patches](../concepts/vllm-model-patches.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [tpu-schedulers](../concepts/tpu-schedulers.md),
  [host-offload](../concepts/host-offload.md)
- Module catalogs: [patch_registry](../catalog/src/vllm_torchtpu/patch_registry.md),
  [tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md),
  [tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md),
  [vllm_torchtpu/__init__](../catalog/src/vllm_torchtpu/__init__.md)
- Related doc-concepts: [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md),
  [env-var-registry-and-compile-key](env-var-registry-and-compile-key.md),
  [derive-dont-declare](derive-dont-declare.md)

## Source
Extracted from `docs/developers_guide/tpu_patch_mechanism.md` (kept in place).
