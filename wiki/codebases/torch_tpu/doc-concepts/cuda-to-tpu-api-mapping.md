---
title: Translating torch.cuda calls (torch.accelerator first, torch.tpu for TPU-specific features)
type: doc-concept
provenance: doc
source: docs/markdown/api_mapping.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Translating torch.cuda calls (torch.accelerator first, torch.tpu for TPU-specific features)

## Definition
The API-mapping doc gives a CUDA-to-TPU translation table with one governing rule: where PyTorch has a device-agnostic `torch.accelerator` API, use it; use `torch.tpu` (registered once the backend initializes, "a drop-in replacement for `torch.cuda`") only for what has no accelerator equivalent. Device queries, current/set stream, synchronize, initial seed and RNG-state reads map to `torch.accelerator`; `is_initialized`, `get_device_name`, `get_device_properties`, `manual_seed[_all]`, `set_rng_state`, `default_stream` and `get_amp_supported_dtype` stay on `torch.tpu`. AMP uses the standard `torch.amp.autocast("tpu", ...)`.

## In torch_tpu (grounded)
- `torch.tpu` is a lazily built public module (see [`install`](../catalog/src/torch_tpu/_internal/public_api.md#install)) whose attributes resolve to classmethods of the device module, e.g. [`TpuDeviceModule.get_device_properties`](../catalog/src/torch_tpu/_internal/device/_device_module.md#TpuDeviceModule.get_device_properties) (name, total memory, `multi_processor_count`), [`TpuDeviceModule.get_device_name`](../catalog/src/torch_tpu/_internal/device/_device_module.md#TpuDeviceModule.get_device_name), [`_DeviceModule.manual_seed_all`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule.manual_seed_all) and [`_DeviceModule.get_amp_supported_dtype`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule.get_amp_supported_dtype) (returns the fixed [`_AMP_SUPPORTED_DTYPES`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_AMP_SUPPORTED_DTYPES) tuple, which the source itself says was "chosen arbitrarily" and includes bf16, fp16, fp32, fp64, complex and fp8 types).
- **Version gates are enforced, not advisory.** The `torch.tpu` twins of the accelerator APIs (`device_count`, `current_device`, `set_device`, `current_stream`, `set_stream`, `synchronize`; `initial_seed`, `get_rng_state`) are decorated with [`internal_or_experimental`](../catalog/src/torch_tpu/_internal/utils/annotations.md#internal_or_experimental): on PyTorch >= 2.11 (>= 2.13 for the RNG pair) calling them from user code raises a `RuntimeError` naming the `torch.accelerator` replacement, unless `TORCH_TPU_ALLOW_LEGACY_DEVICE_APIS=1`. On older PyTorch they are experimental and usable. Example: [`_DeviceModule.synchronize`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule.synchronize).
- AMP hooks: `torch.amp.autocast("tpu")` reaches the device module's autocast state ([`_DeviceModule._set_autocast_dtype`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule._set_autocast_dtype)); see [dtype-and-precision](../concepts/dtype-and-precision.md).
- Streams map to [`TpuStream`](../catalog/src/torch_tpu/_internal/stream/streams.md#TpuStream) ([device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md)).

## Why it matters / when it applies
- **Porting code that calls `torch.cuda.synchronize()` or `torch.cuda.device_count()` should go to `torch.accelerator`**, not a mechanical `cuda` -> `tpu` rename - on current PyTorch the `torch.tpu` spelling errors out.
- **Streams are usually unnecessary on TPU.** The doc's note: in TorchTPU's deferred execution model, the XLA compiler and PjRt runtime manage ordering and hardware concurrency, so CUDA-style multi-stream overlap code can be dropped rather than translated ([deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [pjrt-client](../concepts/pjrt-client.md)).
- **`synchronize` is a full device barrier** - useful for timing, harmful inside a training step ([tensor-synchronization](../concepts/tensor-synchronization.md), [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md)).
- `get_amp_supported_dtype` listing a dtype does not mean it is fast: bf16 is the MXU-native compute type ([mxu-bf16-arithmetic](mxu-bf16-arithmetic.md)).
- `torch.tpu.manual_seed_all(seed)` is the distributed-seeding call (all cores); see [spmd-lockstep-and-collective-fusion](spmd-lockstep-and-collective-fusion.md).

## Connections
- Code concepts: [device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md), [hardware-introspection](../concepts/hardware-introspection.md), [dtype-and-precision](../concepts/dtype-and-precision.md), [tensor-synchronization](../concepts/tensor-synchronization.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [pjrt-client](../concepts/pjrt-client.md)
- Module catalogs: [src/torch_tpu/_internal/device/_device_module](../catalog/src/torch_tpu/_internal/device/_device_module.md), [src/torch_tpu/_internal/utils/annotations](../catalog/src/torch_tpu/_internal/utils/annotations.md), [src/torch_tpu/_internal/stream/streams](../catalog/src/torch_tpu/_internal/stream/streams.md)
- Related doc-concepts: [public-api-surface-inventory](public-api-surface-inventory.md), [api-lifecycle-stages](api-lifecycle-stages.md), [tpu-device-backend-initialization](tpu-device-backend-initialization.md), [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md), [mxu-bf16-arithmetic](mxu-bf16-arithmetic.md)

## Source
Extracted from `docs/markdown/api_mapping.md` (kept in place).
