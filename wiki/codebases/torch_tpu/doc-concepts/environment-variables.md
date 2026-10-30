---
title: TorchTPU environment variables (by subsystem, with readers)
type: doc-concept
provenance: doc
source: docs/markdown/environment_variables.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# TorchTPU environment variables (by subsystem, with readers)

## Definition
TorchTPU is configured through environment variables aimed at three consumers: the XLA compiler
(`XLA_FLAGS`), the TPU runtime / driver (`LIBTPU_INIT_ARGS`) and TorchTPU itself (`TORCH_TPU_*`).
The doc's critical rule: they are **process-global and locked when the backend initializes**
(`import torch` / `torch.device("tpu")`); to try a different value, restart the process. The doc
lists a public subset; the code registry in `csrc/common/env_vars.h` is the complete list,
including the `TORCH_TPU_INTERNAL_*` knobs that matter most for perf work.

## In torch_tpu (grounded)
**Why values are locked.** Every C++ read goes through memoized templates in
`csrc/common/env_vars.h` (`GetEnvOnce` / `GetBooleanEnvOnce` / `GetIntegerEnvOnce`): the first read
caches the value in a function-local static for the life of the process. Each variable must be
registered in [`kEnvVarToStage`](../catalog/csrc/common/env_vars.h.md#kEnvVarToStage) with an API
stage (stable / experimental / internal API / internal implementation, see
[api-lifecycle-stages](api-lifecycle-stages.md)); reading an *experimental* or *deprecated* one emits
a one-time warning, and "internal implementation" vars (set *for* libtpu/GCP) may only be written.
Python reads the same memoized values via `PyGetBooleanEnvOnce` in `csrc/internal/env.cc`;
launcher-side Python sets defaults with
[`get_and_set_str_env_once`](../catalog/src/torch_tpu/_internal/env_utils.md#get_and_set_str_env_once).
Before PJRT init, `PjrtBackend::InitializeInternal` replaces a literal `${RANK}` in `XLA_FLAGS` and
`LIBTPU_INIT_ARGS` with the process rank - handy for per-rank dump directories.

### Eager execution and materialization
| Variable | Default | Effect | Read by |
|---|---|---|---|
| `TORCH_TPU_DEFER_AND_FUSE` (exp.) | off | start in `kDeferAndFuse` (fused eager) instead of `kDeferNever` | [`kTorchTpuDeferAndFuseEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuDeferAndFuseEnvVar), memoized in `GetDefaultEagerMode` (`csrc/eager/eager_mode.cc`) |
| `TORCH_TPU_LAUNCH_BLOCKING` (exp.) | off | `kDeferNeverAndLaunchBlocking` debug eager; wins over DEFER_AND_FUSE; also turns debug checks on | [`kTorchTpuLaunchBlockingEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuLaunchBlockingEnvVar) |
| `TORCH_TPU_INTERNAL_DETECT_REPEATED_OPS` | `safe` | in fused eager, on a detected repeated op sequence materialize with split graph (`safe`) or full graph (`aggressive`); other values disable | [`MustApplyRepeatedOpsHeuristic`](../catalog/csrc/eager/device_buffer_utils.cc.md#MustApplyRepeatedOpsHeuristic), [`GetRepeatedOpsMaterializationMode`](../catalog/csrc/eager/device_buffer_utils.cc.md#GetRepeatedOpsMaterializationMode) |
| `TORCH_TPU_INTERNAL_DISABLE_INPLACE_BUFFER_DONATION` | false | disable input-buffer donation for in-place ops in `kDeferNever` (donation on = less HBM churn) | [`IsInplaceBufferDonationEnabled`](../catalog/csrc/eager/eager_mode.cc.md#IsInplaceBufferDonationEnabled) |
| `TORCH_TPU_INTERNAL_SKINNY_SC_OFFLOAD` | 0 | pin traversals containing exactly one collective ("skinny collective") to the SparseCore | [`ApplySplitMode`](../catalog/csrc/eager/materialize.cc.md#ApplySplitMode) |
| `TORCH_TPU_INTERNAL_SPLIT_RNG_STATE_UPDATE` | 0 | isolate RNG state update into its own compilation unit (better error recovery, may cost perf) | [`DeviceGeneratorImplBase::AdvanceDeviceStateTensor`](../catalog/csrc/eager/device_gen_impl.cc.md#DeviceGeneratorImplBase.AdvanceDeviceStateTensor) |

### Compiler and MLIR pipeline
| Variable | Default | Effect | Read by |
|---|---|---|---|
| `XLA_FLAGS` (exp. stage) | - | XLA debug options (dumps, `xla_allow_excess_precision`, ...); the **whole string is fingerprinted into the compile-options cache key** | [`MakeCompileOptionsKey`](../catalog/csrc/common/compilation.cc.md#MakeCompileOptionsKey "csrc/common/compilation.cc:L441"), [`GetAllowExcessPrecision`](../catalog/csrc/common/excess_precision.cc.md#GetAllowExcessPrecision) |
| `LIBTPU_INIT_ARGS` (stable) | - | libtpu / TPU backend compiler flags (e.g. LLO dumps); also fingerprinted into the cache key; TorchTPU rewrites two flags to avoid distributed hangs | [`MakeCompileOptionsKey`](../catalog/csrc/common/compilation.cc.md#MakeCompileOptionsKey "csrc/common/compilation.cc:L441"), `ConfigureLibtpuInitArgs` in [`InitializeDistributedEnvironment`](../catalog/csrc/common/environment.cc.md#InitializeDistributedEnvironment) |
| `TORCH_TPU_INTERNAL_XLA_OPTIONS` | - | `key=value ...` overrides applied to `xla::CompileOptions.env_option_overrides`, taking precedence over `XLA_FLAGS` | `GetCompilerOptionOverridesFromEnvVar` (`csrc/common/compilation.cc`), [`kTorchTpuInternalXlaOptionsEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalXlaOptionsEnvVar) |
| `TORCH_TPU_INTERNAL_ENABLE_MLIR_CSE` | false | run MLIR CSE in TorchTPU's pass pipeline - **off because CSE made large vLLM prefill graphs ~10% slower** | `AddCleanupPasses` (`csrc/mlir/pipeline.cc`), [`kTorchTpuInternalEnableMlirCseEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalEnableMlirCseEnvVar) |
| `TORCH_TPU_INTERNAL_ENABLE_REASSOCIATE_NORM_WEIGHTS` | true | run the reassociate-norm-weights StableHLO pass | `AddShloPasses` (`csrc/mlir/pipeline.cc`) |
| `TORCH_TPU_INTERNAL_DUMP_MLIR_PASSES_TO` | - | dump per-pass IR (`print` or a directory) | [`ConfigureInstrumentation`](../catalog/csrc/mlir/instrumentation.cc.md#ConfigureInstrumentation) |
| `TORCH_TPU_INTERNAL_STORAGE_AWARE_PLACEHOLDERS` | false | `torch.compile` static compiler makes one placeholder per shared storage (aliasing inputs become views) | Python `compiler.py` via [`kTorchTpuInternalStorageAwarePlaceholdersEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalStorageAwarePlaceholdersEnvVar) |

### Compilation cache
| Variable | Default | Effect | Read by |
|---|---|---|---|
| `TORCH_TPU_TIER2_COMPILATION_CACHE` (exp.) | disabled if `WORLD_SIZE` <= 1, else `default` | **name** (not path) of the host-local cache under `/dev/shm/torch_tpu_cache/<name>`; `disabled` turns it off; forced on when tier 3 is on | [`GetTier2CacheName`](../catalog/csrc/common/tier2_compilation_cache.cc.md#GetTier2CacheName) |
| `TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` (exp.) | unset = off | root of the shared persistent cache (e.g. `gs://...`) | [`GetTier3CacheRootDir`](../catalog/csrc/common/compilation_cache_utils.cc.md#GetTier3CacheRootDir) |
| `TORCH_TPU_INTERNAL_TIER3_COMPILATION_CACHE_LOCAL_BACKUP_TASK` | 1 | start a local compile in parallel with the tier-3 read (first to finish wins); `0` = compile only after a tier-3 miss | [`UsesLocalBackupTaskForTier3Read`](../catalog/csrc/common/tier3_compilation_cache.cc.md#UsesLocalBackupTaskForTier3Read) |

> [!warning] Doc vs code on the tier-2 value
> The doc's quick-reference table lists `/dev/shm/torch_tpu_cache/` or `<local_path>` as values for
> `TORCH_TPU_TIER2_COMPILATION_CACHE`; the code (and the doc's own snippet) treat it as a directory
> **name** placed under `/dev/shm/torch_tpu_cache/`.

### Distributed, collectives, topology
| Variable | Default | Effect | Read by |
|---|---|---|---|
| `RANK`, `LOCAL_RANK`, `WORLD_SIZE`, `MASTER_ADDR`, `MASTER_PORT`, `NNODES`, `NODE_RANK` (stable) | launcher | standard torchrun contract; `WORLD_SIZE` presence triggers distributed init | `PjrtBackend::InitializeInternal` |
| `TORCH_TPU_INTERNAL_MATERIALIZE_COLLECTIVE_TENSORS` | true | force graph splits at collectives; `false` for SPMD workloads with identical per-rank graphs (bigger fused graphs) | [`GetCollectiveSplitMode`](../catalog/csrc/distributed/process_group_tpu.cc.md#GetCollectiveSplitMode) |
| `TORCH_TPU_SPMD_HANDSHAKE_STAGE` (exp.) | `OFF` | `COMPILE_STAGE` / `DISPATCH_STAGE`: ranks handshake to prove identical collective graphs so they compile unsplit | [`GetHandshakeStageEnvVarOnce`](../catalog/csrc/distributed/handshake.cc.md#GetHandshakeStageEnvVarOnce) |
| `TORCH_TPU_INTERNAL_HANDSHAKE_PORT`, `..._HANDSHAKE_TIMEOUT_S` | -, 60 | handshake server port / timeout | `csrc/common/env_vars.h` |
| `TORCH_TPU_TOPOLOGY`, `TORCH_TPU_SLICEBUILDER_ADDRESSES` (exp.) | set by launcher | slice topology (e.g. `2x2x4`) and slice-builder endpoints | [`set_tpu_launch_env`](../catalog/src/torch_tpu/_internal/distributed/distributed.md#set_tpu_launch_env), [`ValidateRequiredDistributedEnvVars`](../catalog/csrc/distributed/slicebuilder/discovery.cc.md#ValidateRequiredDistributedEnvVars "csrc/distributed/slicebuilder/discovery.cc:L32") |
| `TORCH_TPU_BASE_PORT`, `TORCH_TPU_DEVICES_PER_HOST` (exp.) | 8070, 8 | inputs for deriving slice-builder addresses | [`set_tpu_launch_env`](../catalog/src/torch_tpu/_internal/distributed/distributed.md#set_tpu_launch_env) |
| `TPU_VISIBLE_DEVICES` (stable) | `0` single-device | device visibility; TorchTPU copies it into `TPU_VISIBLE_CHIPS` because libtpu prefers the latter | `InitializeSingleDeviceEnvironment` (`csrc/common/environment.cc`) |
| `TPU_PREMAPPED_BUFFER_SIZE` (stable) | 0 (set if absent) | PJRT premapped host buffer size in bytes (host-device transfer staging) | [`GetPremappedBufferSizeFromEnvOnce`](../catalog/csrc/common/discovery.cc.md#GetPremappedBufferSizeFromEnvOnce) |

### Debug, safety, profiling
| Variable | Default | Effect | Read by |
|---|---|---|---|
| `TORCH_SHOW_CPP_STACKTRACES` (exp.) | off (OSS) | append the C++ error trace to errors ([tpu-error-anatomy](tpu-error-anatomy.md)) | [`TorchShowCppStacktraces`](../catalog/csrc/common/status_builder.cc.md#TorchShowCppStacktraces) |
| `TORCH_TPU_ENABLE_DEBUG_CHECKS` (exp.) | on only in debug eager | expensive invariant checks, e.g. `torch.take` bounds (`take(): expected indices to be in range`); extra host-device syncs | [`GetEnableDebugChecks`](../catalog/csrc/common/error_utils.cc.md#GetEnableDebugChecks) |
| `TORCH_TPU_PROFILER_OUTPUT_DIR` (exp.) | - | overrides the XPlane output base dir | [`GetProfilerBaseOutputDir`](../catalog/csrc/internal/profiler/tpu_profiler_plugin.cc.md#GetProfilerBaseOutputDir "csrc/internal/profiler/tpu_profiler_plugin.cc:L332") |
| `TORCH_TPU_XPROF_SESSION_ID` (exp.) | launcher sets `time_ns` | one xprof session id shared by all workers | [`set_tpu_launch_env`](../catalog/src/torch_tpu/_internal/distributed/distributed.md#set_tpu_launch_env) |
| `TORCH_TRACE` (exp.) | - | structured logging for tlparse | [`kTorchTraceEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTraceEnvVar) |
| `TORCH_TPU_ALLOW_LEGACY_DEVICE_APIS` (exp.) | false | legacy `torch.tpu.*` device APIs warn instead of raising | [`kTorchTpuAllowLegacyDeviceApisEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuAllowLegacyDeviceApisEnvVar) |

## Why it matters / when it applies
- **Set before import.** Because of memoization, `os.environ[...] = ...` after `import torch` is
  usually a silent no-op - a common way an "experiment" ends up testing nothing. Put env vars in
  the launch command.
- **Cache-key coupling.** Any change to `XLA_FLAGS` or `LIBTPU_INIT_ARGS` (even reordering) changes
  the compile-options key, so a run with a new flag will not hit tier-2/tier-3 entries compiled
  without it - expect a cold-compile first step.
- **Perf knobs to try first:** `TORCH_TPU_DEFER_AND_FUSE=1` (fused eager);
  `TORCH_TPU_INTERNAL_MATERIALIZE_COLLECTIVE_TENSORS=0` or `TORCH_TPU_SPMD_HANDSHAKE_STAGE` for SPMD
  jobs that split at every collective; tier-2/tier-3 caches for multi-process and restart-heavy
  jobs; keep `TORCH_TPU_INTERNAL_ENABLE_MLIR_CSE` off unless re-measured.
- **Never benchmark with** `TORCH_TPU_LAUNCH_BLOCKING`, `TORCH_TPU_ENABLE_DEBUG_CHECKS` or dump flags.

## Connections
- Code concepts: [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md),
  [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md),
  [compilation-pipeline](../concepts/compilation-pipeline.md),
  [compilation-cache](../concepts/compilation-cache.md),
  [compilation-cache-key](../concepts/compilation-cache-key.md),
  [mlir-optimization-passes](../concepts/mlir-optimization-passes.md),
  [process-group-and-collectives](../concepts/process-group-and-collectives.md),
  [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md),
  [pjrt-client](../concepts/pjrt-client.md), [profiler](../concepts/profiler.md),
  [error-handling](../concepts/error-handling.md)
- Module catalogs: [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md),
  [csrc/common/compilation.cc](../catalog/csrc/common/compilation.cc.md),
  [csrc/eager/eager_mode.cc](../catalog/csrc/eager/eager_mode.cc.md),
  [csrc/common/tier2_compilation_cache.cc](../catalog/csrc/common/tier2_compilation_cache.cc.md),
  [src/torch_tpu/_internal/env_utils](../catalog/src/torch_tpu/_internal/env_utils.md)
- Related doc-concepts: [defer-and-fuse-materialization](defer-and-fuse-materialization.md), [spmd-lockstep-and-collective-fusion](spmd-lockstep-and-collective-fusion.md), [hlo-and-llo-compilation-dumps](hlo-and-llo-compilation-dumps.md),
  [eager-execution-modes](eager-execution-modes.md),
  [multi-tier-compilation-cache](multi-tier-compilation-cache.md),
  [tpu-debugging-ladder](tpu-debugging-ladder.md),
  [excess-precision](excess-precision.md),
  [api-lifecycle-stages](api-lifecycle-stages.md),
  [global-and-local-knobs](global-and-local-knobs.md)

## Source
Extracted from `docs/markdown/environment_variables.md` and its byte-identical duplicate
`docs/markdown/6_reference_4_environment_variables.md` (both kept in place); rows beyond the doc's
public list come from the registry in `csrc/common/env_vars.h`.
