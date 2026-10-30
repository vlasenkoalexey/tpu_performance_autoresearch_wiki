---
slug: torch_tpu
commit: 005903d0ef0dde919b832530451e568912c6f464
scip_tool: scip-python
updated: 2026-10-29
okf_version: "0.2"
sources:
  - {resource: ../../../raw/code/torch_tpu, title: torch_tpu @ 005903d0ef}
---

# torch_tpu internals wiki

Generated, grounded wiki. Start from a concept (or an area); drill into cited symbols.
The commit pin above is the single source version for every page in this silo.

**Start here → [Overview](overview.md)** — torch_tpu v0.2.0, Google's native PyTorch backend for Cloud TPU: ATen ops on the `tpu` device are recorded as deferred StableHLO builders, cut into graphs at materialization points, compiled by XLA through PjRt behind a three-tier compilation cache, and reused unchanged by the torch.compile(backend="tpu") path, with Mosaic/Pallas attention and custom kernels and c10d collectives lowered as graph ops.

## Areas
One page per top-level area: what it is for, the units inside it with their entry points, and the small units that have no page of their own.
- [csrc](areas/csrc.md) — C++ core of torch_tpu: ATen kernels lowered to StableHLO, the deferred eager graph, the compilation pipeline and its cache tiers, Mosaic kernels, collectives and the PjRt runtime.
- [src](areas/src.md) — Python package of torch_tpu: device registration and public API, the torch.compile backend and its static/dynamic compilers, FX passes, distributed launchers, Pallas bridge, optimizers, profiler and hardware helpers.

## Concepts (deep)
Grouped by the source area each page's citations point into.

### `csrc/common`
| Concept | Description | Status |
|---|---|---|
| [compilation-cache-key](concepts/compilation-cache-key.md) | What exactly torch_tpu fingerprints to decide whether a graph needs a new TPU compile (graph structure and dtypes, every tensor dimension, per-op parameters, compile options), why scalars are promoted to tensors, and how dynamic-shape keys differ; read it when hunting a recompilation storm or adding an op parameter. | fresh |
| [compilation-cache](concepts/compilation-cache.md) | How torch_tpu's CompilationCache finds or builds a TPU executable (static, bounded-dynamic and unbounded-dynamic tier-1 maps, tier-2 host tmpfs with cross-process file locks, tier-3 local or gs:// store with a racing backup compile) and the env vars and modes that control it; read it when diagnosing recompiles, cold starts, or cache misconfiguration. | fresh |
| [compilation-pipeline](concepts/compilation-pipeline.md) | How torch_tpu turns a graph of deferred ATen ops into a compiled TPU executable (compile-option resolution, O1 vs O2 modes, StableHLO module build, async PjRt compile, futures); read it before tuning compile time vs step time or XLA/libtpu flags. | fresh |
| [context-states-and-execution-modes](concepts/context-states-and-execution-modes.md) | How torch_tpu's EagerMode (DEFER_NEVER, DEFER_AND_FUSE, DEFER_NEVER_AND_LAUNCH_BLOCKING and two internal modes) decides whether a dispatched ATen op is compiled and launched alone, queued for multi-op XLA fusion, or never touches the device, which XLA compile effort and in-place donation policy each mode gets, and how that mode and the other thread-local context states (precision, tracebacks, spmd_safe, compiler options, layout, profile) are stacked, read and kept off worker threads; read it before choosing an execution mode or debugging why an op did not fuse, recompiled, or ignored a context manager. | fresh |
| [dtype-and-precision](concepts/dtype-and-precision.md) | How torch_tpu translates PyTorch dtypes to StableHLO/XLA element types (and which dtypes it rejects), how per-op matmul precision is chosen from the torch.tpu.precision context manager or the patched torch.set_float32_matmul_precision global and baked into the cache key, how compute-dtype upcasts and CUDA-style accumulation types are applied, and what the allow_excess_precision compiler flag changes; read it when a matmul is slower or less accurate than expected, a dtype is rejected, or numerics differ between eager and compiled runs. | fresh |
| [error-handling](concepts/error-handling.md) | How torch_tpu's C++ core reports errors (absl::Status built by StatusBuilder and the TT_ERROR / TT_RET_CHECK / TT_RETURN_IF_ERROR / TT_ASSIGN_OR_* macros), where a Status becomes a Python exception (TtError -> c10::Error at the TT_KERNEL boundary), how XLA compiler errors are rewritten, and how the global sticky error turns asynchronous failures (torch._assert_async) into an error on the next op dispatch or device sync; read it before debugging a torch_tpu exception, adding an error path to a kernel, or reasoning about what error checking costs on the dispatch hot path. | fresh |
| [fused-optimizer-kernels](concepts/fused-optimizer-kernels.md) | How torch_tpu implements PyTorch's fused=True optimizer ATen ops as a single multi-tensor StableHLO program per step - fp32 compute precision, runtime (non-recompiling) hyperparameters, buffer donation, and the found_inf select; read before tuning optimizer-step time or HBM. | fresh |

### `csrc/eager`
| Concept | Description | Status |
|---|---|---|
| [deferred-execution-and-materialization](concepts/deferred-execution-and-materialization.md) | How torch_tpu represents tensor data as DeviceBufferRef -> DeviceBufferList -> DeferredOp graphs, how each eager mode (DeferNever, DeferAndFuse, compile) decides when those graphs are cut, compiled to one StableHLO module and executed on background threads, and which states/flags govern it; read this to reason about graph size, graph breaks, recompiles and host-device stalls. | fresh |
| [device-streams-generators-and-rng](concepts/device-streams-generators-and-rng.md) | How torch_tpu tracks the current (device, stream) per thread and uses streams as independent deferred-op queues (including TensorCore/SparseCore pinning), and how its RNG generators keep a device-resident {seed, offset} Philox state tensor that random ops consume as an input and advance with a deferred op, with separate eager and export-mode generators; read it when random ops recompile, sync the host, break fusion, or diverge between eager and torch.compile, or when using torch.tpu.Stream. | fresh |
| [eager-op-dispatch](concepts/eager-op-dispatch.md) | How a torch_tpu ATen kernel turns at::Tensor inputs into DeviceBufferRefs, records a StableHLO-building deferred op via DispatchOp/DispatchOpOut, and binds the results back onto at::Tensor storage (including scalar promotion and in-place buffer donation); read this before writing or profiling an ATen kernel. | fresh |

### `csrc/ops`
| Concept | Description | Status |
|---|---|---|
| [aten-kernel-authoring](concepts/aten-kernel-authoring.md) | How a torch_tpu ATen kernel is written - what the TT_KERNEL macro wraps around the body (op-name scope, Python context, parameter cache keys, arg checks, error translation), how UnaryOp/BinaryOpOut/TernaryOpOut turn a StableHLO builder lambda into a deferred op, and which of these costs survive into an optimized (-c opt) build. Read before adding or optimizing an op. | fresh |
| [op-names-and-python-context](concepts/op-names-and-python-context.md) | How torch_tpu identifies each op (the OpName enum and its stable string form), how the thread-local OpNameStack and ScopedPythonContextCapturer stacks are pushed by every kernel, how the captured PythonContext travels inside a deferred op and comes back as an MLIR location that xprof shows, and how GetRootOpName uses the same state to prefix errors. Read when mapping xprof ops back to Python, when enabling tracebacks, or when an op name shows up in a cache key or error. | fresh |
| [stablehlo-op-builder](concepts/stablehlo-op-builder.md) | What an op's StableHLO builder lambda is allowed to assume and which helpers it uses - MakeScalarConstant / MakeConstantLike / MakeConstant for constants, BroadcastIfNeeded for NumPy broadcasting, GetTensorTypeOrDie / GetElementTypeOrSelf / GetMlirType for types, MlirOpResults for arity - with the static-vs-bounded-dynamic shape rules and when the builder actually runs (only on a compile-cache miss). Read when writing or debugging an op lowering. | fresh |

### `csrc/distributed`
| Concept | Description | Status |
|---|---|---|
| [process-group-and-collectives](concepts/process-group-and-collectives.md) | How torch.distributed collectives on TPU tensors become StableHLO collective ops inside TorchTPU's deferred eager graphs, how the "tpu_dist" process group builds its device assignment and replica groups, and which knobs decide whether a collective gets its own graph; read before reasoning about collective cost, graph splits around collectives, or multi-slice device ordering. | fresh |

### `csrc/experimental/batch_transfer`
| Concept | Description | Status |
|---|---|---|
| [batch-host-device-transfer](concepts/batch-host-device-transfer.md) | How torch_tpu's experimental subsystem moves many same-shape tensors between HBM and host in one raw-PJRT batch (BatchTransferD2H/H2D + TransferFuture), and how it ships a hand-built, compile-once Mosaic kernel (nonzero) into the unbounded-dynamic compilation cache - read this when per-tensor .cpu()/.to() overhead or per-shape recompiles of data-dependent ops dominate. | fresh |

### `csrc/internal/compile`
| Concept | Description | Status |
|---|---|---|
| [compiled-mode](concepts/compiled-mode.md) | How csrc/internal/compile turns a Dynamo FX graph into one PJRT executable by re-using the eager deferred-op graph as the tracer (placeholders -> deferred ops -> TraverseAndCompile -> StableHLO -> XLA), how the compiled step is executed and its outputs rebuilt in C++, how scan / associative_scan become stablehlo.while or chlo.scan, and how RNG state is threaded through; read it before reasoning about torch.compile step time, compile latency, argument donation/dedup, or scan-over-layers on TorchTPU. | fresh |

### `csrc/internal/mosaic`
| Concept | Description | Status |
|---|---|---|
| [mosaic-matmul](concepts/mosaic-matmul.md) | The small shared vocabulary in csrc/internal/mosaic/op_builders that every C++-emitted Mosaic kernel in torch_tpu uses - the f32-accumulating tpu.matmul builder and its precision/transpose options, VMEM/SMEM memref types for block operands, and the parallel/arbitrary grid semantics - and how the flash-attention kernels and KILN emit matmul kernels on top of it. | fresh |

### `csrc/internal/mosaic/kiln/core`
| Concept | Description | Status |
|---|---|---|
| [kiln-kernel-dsl](concepts/kiln-kernel-dsl.md) | What KILN is (a small C++ embedded language in csrc/internal/mosaic/kiln that emits Mosaic TPU dialect through operator overloading on Ref / Tile / Scalar handles), how BuildKernel assembles a grid kernel from Pallas-style specs, and what it does and does not do for kernel performance; read before writing or reviewing a C++ Mosaic kernel in torch_tpu. | fresh |

### `csrc/internal/profiler`
| Concept | Description | Status |
|---|---|---|
| [profiler](concepts/profiler.md) | How torch_tpu captures TPU profiles - the `_profiler_backend` pybind module (start_trace/stop_trace, gRPC profiler server) over tsl::ProfilerSession, the libkineto PrivateUse1 plugin that makes `torch.profiler.profile(activities=[..., TPU])` write an xprof `.xplane.pb` and feed device events back into Kineto, the custom-config option grammar, output-path rules, and the RecordFunction -> TraceMe bridge; read it before capturing or debugging a TPU trace. | fresh |

### `csrc/internal/sync`
| Concept | Description | Status |
|---|---|---|
| [tensor-synchronization](concepts/tensor-synchronization.md) | How the csrc/internal/sync subsystem forces deferred TPU tensors to materialize (wait=False, a graph cut) or to finish executing (wait=True, a barrier), the C++ fast paths behind the Python synchronize() call, the materialization-state probes, and the computation-graph dump helpers; read this before placing sync points in a training step or timing TPU work. | fresh |

### `csrc/mlir`
| Concept | Description | Status |
|---|---|---|
| [mlir-optimization-passes](concepts/mlir-optimization-passes.md) | What csrc/mlir does to each StableHLO module TorchTPU builds before handing it to XLA (canonicalize, opt-in CSE, norm-weight reassociation, StableHLO target-independent optimization, symbol DCE), why CSE is off by default, how the env-var knobs and the pass-dump instrumentation work, and which passes are registered for tooling; read it when a StableHLO dump differs from what the eager/compiled lowering emitted, when debugging a numerics or perf change in normalization layers, or when adding a pass. | fresh |

### `csrc/ops/copy_from`
| Concept | Description | Status |
|---|---|---|
| [host-device-copy](concepts/host-device-copy.md) | How torch_tpu implements every tensor copy between CPU and TPU and within TPU (aten _copy_from, copy_, _copy_from_and_resize, _local_scalar_dense), and which directions force materialization of the deferred graph - read this when .cpu(), .item(), .to(device) or a hidden D2H sync shows up in a profile. | fresh |

### `csrc/ops/dynamic/pad_real_to_static`
| Concept | Description | Status |
|---|---|---|
| [dynamic-shape-ops](concepts/dynamic-shape-ops.md) | How torch_tpu's internal dynamic-shape custom ops let one static-shape XLA program serve many runtime sizes - tensors are allocated at a static upper bound and carry their real size via stablehlo.set_dimension_size or bounded dynamic types; read this when a torch.compile graph with SymInt shapes shows these ops in its HLO or when padded compute waste is suspected. | fresh |

### `csrc/ops/experimental/ragged_all_to_all`
| Concept | Description | Status |
|---|---|---|
| [ragged-collectives-and-sparse-ops](concepts/ragged-collectives-and-sparse-ops.md) | How csrc/ops/experimental lowers MoE-oriented ragged ops (ragged_all_to_all custom call, chlo.ragged_dot), dimension-aware all-gather/reduce-scatter, and the SparseCore embedding family (sparse_dense_matmul + fused SGD/Adagrad/Adam grad, sparse_gather, sparse_map_row) to StableHLO; read before building expert-parallel MoE dispatch or TPU embedding tables on torch_tpu. | fresh |

### `csrc/ops/reductions`
| Concept | Description | Status |
|---|---|---|
| [reductions](concepts/reductions.md) | How torch_tpu lowers ATen reductions (sum.IntList_out, mean.out, var / std .correction and their out variants, var_mean.correction) to StableHLO - dim canonicalization, keepdim handling, the BuildReductionShlo / BuildSumShlo builders that many other ops reuse, accumulation-dtype upcasting for bf16/f16, the two-pass variance formula, and how each kernel's cache key is formed; read it when a reduction shows up in a profile, when checking reduction precision, or when writing a new op that needs a reduce. | fresh |

### `csrc/ops/scaled_dot_product_attention`
| Concept | Description | Status |
|---|---|---|
| [scaled-dot-product-attention](concepts/scaled-dot-product-attention.md) | How torch_tpu routes torch.nn.functional.scaled_dot_product_attention to either a hand-built Mosaic flash-attention kernel (forward + dK/dV + dQ backward) or a StableHLO "optimized MATH" graph, with the tiling, padding, dtype and precision rules that decide performance; read before debugging an attention-bound profile. | fresh |

### `csrc/ops/view_decomposition`
| Concept | Description | Status |
|---|---|---|
| [view-decomposition](concepts/view-decomposition.md) | How torch_tpu turns an arbitrary PyTorch strided view (sizes, strides, storage offset, dtype - including as_strided and view(dtype)) into a short sequence of StableHLO reshape / transpose / broadcast / slice / pad / bitcast / unfold primitives, how it inverts that sequence to write a mutated view back into its base buffer with dynamic_update_slice, how ContiguousToView rebuilds a strided tensor from contiguous data, and what each step costs; read it when a profile shows as_strided / as_strided_inverse ops, unexpected copies around views or in-place slicing, or recompiles keyed on strides. | fresh |

### `csrc/pjrt`
| Concept | Description | Status |
|---|---|---|
| [pjrt-client](concepts/pjrt-client.md) | How TorchTPU creates and configures its single PjRt C-API client and device (lazy, fork-guarded singleton), how launcher env vars become libtpu topology settings at that moment, and the thin execute and host-device transfer wrappers every op goes through; read when debugging TPU initialization, multi-process or multi-slice startup, executable launch, or H2D/D2H copy costs. | fresh |

### `src/torch_tpu/_internal/compile`
| Concept | Description | Status |
|---|---|---|
| [torch-compile-backend](concepts/torch-compile-backend.md) | How torch.compile(backend="tpu") turns a Dynamo FX graph into PJRT executables - option parsing, AOTAutograd, the collective-splitting SplitCompiler, static vs dynamic compilers, async compilation and the AOTAutograd cache hook - and which knobs matter for TPU step time and compile time. | fresh |

### `src/torch_tpu/_internal/compile/dynamic`
| Concept | Description | Status |
|---|---|---|
| [dynamic-shapes-compiler](concepts/dynamic-shapes-compiler.md) | How torch_tpu compiles torch.compile graphs whose inputs carry symbolic sizes - SymInt bounds, 128-aligned shape buckets, the FX rewrite into bounded dynamic ops, and the runtime bucket/layout dispatcher - and what it costs in padding, recompiles and dispatch overhead. | fresh |

### `src/torch_tpu/_internal/compile/fx_passes`
| Concept | Description | Status |
|---|---|---|
| [fx-graph-passes](concepts/fx-graph-passes.md) | The nine FX passes in src/torch_tpu/_internal/compile/fx_passes, in the order the static and split compilers run them - GQA folding and causal-mask elimination for attention, constant embedding, activation-checkpoint barriers, and the split_module repair passes (mutated-placeholder cloning, constant sinking, forced collective outputs, SymInt propagation/reordering) - with what each rewrites, why it matters for TPU step time and HBM, and where it can surprise you; read it when an attention, remat or collective-split result in a TorchTPU HLO dump does not match the FX graph you expected. | fresh |

### `src/torch_tpu/_internal/distributed`
| Concept | Description | Status |
|---|---|---|
| [distributed-launchers-and-spmd](concepts/distributed-launchers-and-spmd.md) | The Python side of TorchTPU distributed - launch-env bootstrap, topology-aware DeviceMesh rank layouts, the spmd_safe opt-in, the ZMQ collective handshake that lets torch.compile keep collectives fused, and the TorchComms adapter; read when deciding how to launch multi-host jobs, lay out a DeviceMesh, or get collectives compiled without graph splits. | fresh |

### `src/torch_tpu/_internal/ops/scaled_mm/kernels`
| Concept | Description | Status |
|---|---|---|
| [python-ops](concepts/python-ops.md) | What the Python ops package adds on top of the C++ ATen backend - the JAX/Pallas splash attention bridge behind torch.tpu.ops.splash_sdpa, and the build-time Pallas kernels exported to StableHLO for block-scaled FP8 matmul (_scaled_mm_v2) - with their block-size/tile knobs and perf tradeoffs. | fresh |

### `src/torch_tpu/_internal/optimizers`
| Concept | Description | Status |
|---|---|---|
| [python-optimizers](concepts/python-optimizers.md) | How torch_tpu's Python optimizer layer works - pytree-registered ParamGroup state, functional step() wrappers over torch.optim kernels, bf16-moment options, and SingleTraceTrainer, which traces forward + backward + optimizer into one make_fx graph and compiles it as a single offload; read before choosing an optimizer or train-step path on TPU. | fresh |

### `src/torch_tpu/_internal/pallas`
| Concept | Description | Status |
|---|---|---|
| [pallas-custom-kernels](concepts/pallas-custom-kernels.md) | How torch_tpu turns a JAX function or Pallas kernel into a torch.library custom op - static-arg inference, schema generation, fake kernel, jax.export to StableHLO, fingerprint-keyed kernel registration, donation and meshes; read it before wrapping a Pallas kernel for a PyTorch model on TPU or when debugging recompiles/retraces of one. | fresh |

### `src/torch_tpu/_internal/utils`
| Concept | Description | Status |
|---|---|---|
| [hardware-introspection](concepts/hardware-introspection.md) | How torch_tpu identifies the attached TPU generation from PCI sysfs and turns it into per-chip / per-device HBM and peak bf16 FLOP/s (the MFU denominator), plus the shared utilities in the same package - API lifecycle decorators (@experimental, @deprecated, forbid_in_torch_compile) and the ActivationTracer / OpTracer debug tracers; read it when computing MFU or memory budgets on TPU, or when an API warns, raises or breaks a compiled graph. | fresh |

## Doc-derived concepts
Concepts extracted from the project's own docs (README / `docs/`), grounded to the symbol catalog. The source docs stay in place.
- [api-lifecycle-stages](doc-concepts/api-lifecycle-stages.md)
- [aten-and-c10d-ops-as-ir](doc-concepts/aten-and-c10d-ops-as-ir.md)
- [ci-test-tag-filters](doc-concepts/ci-test-tag-filters.md)
- [cuda-to-tpu-api-mapping](doc-concepts/cuda-to-tpu-api-mapping.md)
- [custom-autograd-function](doc-concepts/custom-autograd-function.md)
- [defer-and-fuse-materialization](doc-concepts/defer-and-fuse-materialization.md)
- [eager-execution-modes](doc-concepts/eager-execution-modes.md)
- [environment-variables](doc-concepts/environment-variables.md)
- [excess-precision](doc-concepts/excess-precision.md)
- [extending-via-composition](doc-concepts/extending-via-composition.md)
- [gke-single-device-workload-topology](doc-concepts/gke-single-device-workload-topology.md)
- [global-and-local-knobs](doc-concepts/global-and-local-knobs.md)
- [graph-breaks-on-tpu](doc-concepts/graph-breaks-on-tpu.md)
- [graph-fingerprint-and-recompilation](doc-concepts/graph-fingerprint-and-recompilation.md)
- [hlo-and-llo-compilation-dumps](doc-concepts/hlo-and-llo-compilation-dumps.md)
- [host-sync-avoidance-in-training-loops](doc-concepts/host-sync-avoidance-in-training-loops.md)
- [matmul-precision-modes](doc-concepts/matmul-precision-modes.md)
- [multi-tier-compilation-cache](doc-concepts/multi-tier-compilation-cache.md)
- [mxu-bf16-arithmetic](doc-concepts/mxu-bf16-arithmetic.md)
- [one-bit-quantized-sum](doc-concepts/one-bit-quantized-sum.md)
- [op-fusion-and-hbm-traffic](doc-concepts/op-fusion-and-hbm-traffic.md)
- [optimized-wheel-build](doc-concepts/optimized-wheel-build.md)
- [pallas-jax-op-bridge](doc-concepts/pallas-jax-op-bridge.md)
- [pallas-register-level-fusion](doc-concepts/pallas-register-level-fusion.md)
- [public-api-paths-and-module-structure](doc-concepts/public-api-paths-and-module-structure.md)
- [public-api-surface-inventory](doc-concepts/public-api-surface-inventory.md)
- [python-version-support-policy](doc-concepts/python-version-support-policy.md)
- [pytorch-extension-ladder](doc-concepts/pytorch-extension-ladder.md)
- [sdpa-backend-selection-when-porting](doc-concepts/sdpa-backend-selection-when-porting.md)
- [single-trace-trainer](doc-concepts/single-trace-trainer.md)
- [spmd-lockstep-and-collective-fusion](doc-concepts/spmd-lockstep-and-collective-fusion.md)
- [torch-compile-static-shapes-and-bounded-dynamism](doc-concepts/torch-compile-static-shapes-and-bounded-dynamism.md)
- [torch-tpu-architecture-and-lowering-stack](doc-concepts/torch-tpu-architecture-and-lowering-stack.md)
- [torchrun-launch-and-tpu-dist-ddp](doc-concepts/torchrun-launch-and-tpu-dist-ddp.md)
- [torchtpu-user-guide-map](doc-concepts/torchtpu-user-guide-map.md)
- [tpu-common-failure-patterns](doc-concepts/tpu-common-failure-patterns.md)
- [tpu-cpu-numerical-parity](doc-concepts/tpu-cpu-numerical-parity.md)
- [tpu-debugging-ladder](doc-concepts/tpu-debugging-ladder.md)
- [tpu-device-backend-initialization](doc-concepts/tpu-device-backend-initialization.md)
- [tpu-error-anatomy](doc-concepts/tpu-error-anatomy.md)
- [trace-red-flags](doc-concepts/trace-red-flags.md)
- [xla-lowering-stablehlo-hlo-llo](doc-concepts/xla-lowering-stablehlo-hlo-llo.md)
- [xprof-profiling-workflow](doc-concepts/xprof-profiling-workflow.md)

## Coverage
Two tiers: **concept pages** explain mechanisms deeply (selective); the **symbol
index** represents the rest so the whole repo is navigable. Coverage is a
set-difference over the SCIP symbol table, not a graph walk — every documentable
symbol is enumerated and represented.

- documentable symbols: **20186** across 716 modules
- deep (concept pages): **1177** (5.8%)
- index-only: **19009**
- represented total: **20186** (100.0%)
- classes represented: **1902/1902**

[`catalog/index.md`](catalog/index.md) maps every module; `catalog/symbols/*.tsv` and `catalog/edges/*.tsv` are the greppable symbol index; per-module pages under `catalog/` are a rendering of it (tier `full`).

## Provenance
`extracted` = from SCIP / source. `inferred` = LLM judgment, treat as such.
Design-intent dynamics are labeled; none are runtime-measured (no L4 pass run).
Callers/callees are reference-scoped (SCIP has no call role), labeled "calls/refs".
