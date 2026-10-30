---
title: The public API surface inventory (generated public_apis list, perf-relevant map)
type: doc-concept
provenance: doc
source: docs/markdown/public_apis.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# The public API surface inventory (generated public_apis list, perf-relevant map)

## Definition
`docs/markdown/public_apis.md` is the authoritative, machine-generated list of every TorchTPU Python API and environment variable a program may use, grouped by lifecycle stage (stable, experimental, deprecated, internal). Its framing is blunt: "Using any other TorchTPU API is undefined behavior and unsupported." PyTorch APIs that TorchTPU merely implements for TPU (e.g. `torch.accelerator.*`) are listed as stable but documented by PyTorch. The stage semantics themselves are on [api-lifecycle-stages](api-lifecycle-stages.md); this page is about what the inventory contains and where the perf levers sit.

## In torch_tpu (grounded)
- **Generation.** The lists between `BEGIN GENERATED` / `END GENERATED` markers are produced by the API scanner from the namespace table that [`install`](../catalog/src/torch_tpu/_internal/public_api.md#install) turns into `torch.tpu.*` modules ([`ModuleSpec`](../catalog/src/torch_tpu/_internal/public_api.md#ModuleSpec) entries) plus each symbol's stage annotation ([`experimental`](../catalog/src/torch_tpu/_internal/utils/annotations.md#experimental "src/torch_tpu/_internal/utils/annotations.py:L339"), [`deprecated`](../catalog/src/torch_tpu/_internal/utils/annotations.md#deprecated "src/torch_tpu/_internal/utils/annotations.py:L380"), [`internal_or_experimental`](../catalog/src/torch_tpu/_internal/utils/annotations.md#internal_or_experimental)). Module layout rules are on [public-api-paths-and-module-structure](public-api-paths-and-module-structure.md).
- **Stable is small.** Only the `torch.accelerator` device/memory/stream/RNG APIs, the `torch.tpu.ops.max_pool{1,2,3}d[_backward]` ops, and upstream env vars (`LIBTPU_INIT_ARGS`, `RANK`/`LOCAL_RANK`/`WORLD_SIZE`, `MASTER_ADDR`/`MASTER_PORT`, `NNODES`/`NODE_RANK`, `TPU_VISIBLE_DEVICES`, `TPU_PREMAPPED_BUFFER_SIZE`, `TORCH_DEVICE_BACKEND_AUTOLOAD`, `TMPDIR`) are stable.
- **Internal device APIs raise.** `torch.tpu.synchronize`, `device_count`, `current_stream`, `set_device`, `get_rng_state`, ... are listed as *internal* once the running PyTorch has the `torch.accelerator` equivalent (2.11+, or 2.13+ for `torch.accelerator.random`). They are decorated with `internal_or_experimental`, and calling one from user code raises a `RuntimeError` naming the replacement; `TORCH_TPU_ALLOW_LEGACY_DEVICE_APIS=1` downgrades that to a one-time warning ([`_DeviceModule.synchronize`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule.synchronize) is one example). See [cuda-to-tpu-api-mapping](cuda-to-tpu-api-mapping.md).
- **Deprecated in 0.2.0:** `torch.tpu.topology_aware_mesh` (use `torch.tpu.distributed.topology_aware_mesh`, [`topology_aware_mesh`](../catalog/src/torch_tpu/_internal/distributed/device_mesh.md#topology_aware_mesh "src/torch_tpu/_internal/distributed/device_mesh.py:L224")).

## Why it matters / when it applies
Nearly every TPU-specific performance lever is **experimental** - it works, warns once, and may change between releases, so experiment pages should pin the torch_tpu version. The perf-relevant experimental surface, by area:

| Area | Public APIs / env vars | Code concept |
|---|---|---|
| Eager deferral | `torch.tpu.EagerMode` (`DEFER_AND_FUSE`, `DEFER_NEVER`, `DEFER_NEVER_AND_LAUNCH_BLOCKING`), `eager_mode` / `set_eager_mode` ([`_DeviceModuleMeta.eager_mode`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModuleMeta.eager_mode)); `TORCH_TPU_DEFER_AND_FUSE`, `TORCH_TPU_LAUNCH_BLOCKING` | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md) |
| Precision | `torch.tpu.precision`, `Precision.{DEFAULT,HIGH,HIGHEST}`, `allow_excess_precision` ([`_DeviceModuleMeta.allow_excess_precision`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModuleMeta.allow_excess_precision)), `get_amp_supported_dtype` | [dtype-and-precision](../concepts/dtype-and-precision.md) |
| Compilation | `torch.tpu.compiler.custom_compiler_options` ([`custom_compiler_options`](../catalog/src/torch_tpu/_internal/compiler_options/__init__.md#custom_compiler_options)); `TORCH_TPU_TIER2_COMPILATION_CACHE`, `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`, `XLA_FLAGS` | [compilation-pipeline](../concepts/compilation-pipeline.md), [compilation-cache](../concepts/compilation-cache.md) |
| Kernels / ops | `torch.tpu.ops.splash_sdpa` ([`splash_sdpa`](../catalog/src/torch_tpu/_internal/ops/splash_attention.md#splash_sdpa)), `ragged_dot`, `ragged_all_to_all`, `all_gather_dim`, `reduce_scatter_dim`, `optimization_barrier`, sparse-dense matmul family; `torch.tpu.pallas.jax_op`, `get_pallas_mesh` | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md), [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md) |
| Optimizers | `torch.tpu.optimizers.{AdamW,Muon,Sgd,Optimizer,SingleTraceTrainer}` ([`SingleTraceTrainer`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#SingleTraceTrainer)) | [python-optimizers](../concepts/python-optimizers.md) |
| Distributed | `torch.tpu.distributed.{set_tpu_launch_env, spmd_safe, topology_aware_mesh, window_num_stripes, window_stripe_chunk_mb}`; `TORCH_TPU_TOPOLOGY`, `TORCH_TPU_SLICEBUILDER_ADDRESSES`, `TORCH_TPU_BASE_PORT`, `TORCH_TPU_DEVICES_PER_HOST`, `TORCH_TPU_SPMD_HANDSHAKE_STAGE`, `TORCHCOMM_RANK`/`SIZE` | [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md) |
| Profiling / debug | `torch.tpu.profiler.TpuProfilerConfig` ([`TpuProfilerConfig`](../catalog/src/torch_tpu/_internal/profiler/profiler_config.md#TpuProfilerConfig)), `torch.tpu.Event` timing; `TORCH_TPU_PROFILER_OUTPUT_DIR`, `TORCH_TPU_XPROF_SESSION_ID`, `TORCH_TPU_ENABLE_DEBUG_CHECKS`, `TORCH_TRACE`, `TORCH_SHOW_CPP_STACKTRACES` | [profiler](../concepts/profiler.md), [error-handling](../concepts/error-handling.md) |

- A knob not on this page (e.g. a `TORCH_TPU_INTERNAL_*` variable or a `torch.ops.tpu._*` op) is unsupported by definition; a speedup that depends on one is fragile.
- Experimental and deprecated APIs warn once per process; that warning in a perf log is a stage notice, not an error.

## Connections
- Code concepts: [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [dtype-and-precision](../concepts/dtype-and-precision.md), [compilation-cache](../concepts/compilation-cache.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [python-optimizers](../concepts/python-optimizers.md), [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md), [profiler](../concepts/profiler.md), [device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md), [hardware-introspection](../concepts/hardware-introspection.md)
- Module catalogs: [src/torch_tpu/_internal/public_api](../catalog/src/torch_tpu/_internal/public_api.md), [src/torch_tpu/_internal/utils/annotations](../catalog/src/torch_tpu/_internal/utils/annotations.md), [src/torch_tpu/_internal/device/_device_module](../catalog/src/torch_tpu/_internal/device/_device_module.md)
- Related doc-concepts: [api-lifecycle-stages](api-lifecycle-stages.md), [public-api-paths-and-module-structure](public-api-paths-and-module-structure.md), [global-and-local-knobs](global-and-local-knobs.md), [cuda-to-tpu-api-mapping](cuda-to-tpu-api-mapping.md), [eager-execution-modes](eager-execution-modes.md), [multi-tier-compilation-cache](multi-tier-compilation-cache.md), [pallas-jax-op-bridge](pallas-jax-op-bridge.md), [spmd-lockstep-and-collective-fusion](spmd-lockstep-and-collective-fusion.md), [single-trace-trainer](single-trace-trainer.md)

## Source
Extracted from `docs/markdown/public_apis.md` (kept in place).
