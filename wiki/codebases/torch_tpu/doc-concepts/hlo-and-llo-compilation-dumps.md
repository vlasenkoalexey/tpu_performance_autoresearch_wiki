---
title: HLO and LLO compilation dumps (XLA_FLAGS / LIBTPU_INIT_ARGS) and how to read them
type: doc-concept
provenance: doc
source: docs/markdown/background_on_torch_compile_on_tpus_via_xla.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# HLO and LLO compilation dumps (XLA_FLAGS / LIBTPU_INIT_ARGS) and how to read them

## Definition
The viewing-compilation-artifacts doc shows how to make XLA write its intermediate IR to disk and what to look for, using a compiled `relu(x + y)`:

| Artifact | How to enable (before `import torch`) | What to look for |
|---|---|---|
| HLO text | `XLA_FLAGS="--xla_dump_to=/tmp/xla_dump --xla_dump_hlo_as_text"` | `module_XXXX.tt_jit_...before_optimizations.txt` shows the unfused ops (`add`, `broadcast`, `maximum`); `*after_codegen.txt` shows the optimized graph |
| LLO text | `LIBTPU_INIT_ARGS="--xla_jf_dump_to=/tmp/llo_dump --xla_jf_dump_llo_text=true"` (the notebook also appends the flags to `sys.argv`) | files named `<id>-<fusion_name>-01-original.txt`; the real vector instructions (`vadd.f32`, `vmax.f32`), `vld`/`vst` to VMEM, and `dma.hbm_to_vmem` / `dma.done` pairs |

Reading the example: after optimization both ops sit in one `fusion(...)` with `kind=kLoop, calls=%fused_computation` (named `add_maximum_fusion`) - "both operators compile into a single memory-efficient loop". The fusion's `backend_config` carries XLA's cost-model hints (`estimated_cycles`, scoped VMEM configs, window bounds). In LLO, operands are DMA'd HBM -> VMEM once, computed in vector registers, and written back once.

## In torch_tpu (grounded)
- Module names in dump filenames come from TorchTPU: eager materializations are named by [`BuildModuleNameFromPyContext`](../catalog/csrc/ops/op_builder_utils.cc.md#BuildModuleNameFromPyContext) as `tt_jit_<file>_L<line>C<col>_<func>_<op>` (the Python frame that triggered the flush), or plain `tt_jit` when MLIR tracebacks are off. `torch.compile` graphs can be named with `options={"custom_module_name": ...}`, producing `<name>_split<N>_fwd|bwd` via [`_get_module_name`](../catalog/src/torch_tpu/_internal/compile/_backend.md#_get_module_name). HLO ops also carry `metadata={op_name="add/add" stack_frame_id=...}`, derived from the MLIR locations (op name + Python frame) TorchTPU attaches while building StableHLO - see [op-names-and-python-context](../concepts/op-names-and-python-context.md) for the op-name machinery ([`OpName`](../catalog/csrc/ops/op_names.h.md#OpName), [`ScopedOpName`](../catalog/csrc/common/op_name_stack.h.md#ScopedOpName)). This metadata is how a fusion is traced back to ATen ops and source lines.
- `LIBTPU_INIT_ARGS` is registered as [`kLibtpuInitArgsEnvVar`](../catalog/csrc/common/env_vars.h.md#kLibtpuInitArgsEnvVar). `XLA_FLAGS` is honored too, but [`kTorchTpuInternalXlaOptionsEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalXlaOptionsEnvVar) overrides its `debug_options`.
- One layer above HLO, TorchTPU can dump its own StableHLO: for every cache miss with [`CompilationCache.SetDumpOnCacheMissMode`](../catalog/csrc/common/compilation_cache.cc.md#CompilationCache.SetDumpOnCacheMissMode) (Python: [`_DeviceModule._set_dump_on_cache_miss`](../catalog/src/torch_tpu/_internal/device/_device_module.md#_DeviceModule._set_dump_on_cache_miss)), and per MLIR pass with [`kTorchTpuInternalDumpMlirPassesToEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalDumpMlirPassesToEnvVar). For `torch.compile`, the `debug_callback` backend option receives a [`TpuCompileDebug`](../catalog/src/torch_tpu/_internal/compile/debug.md#TpuCompileDebug) with pre/post-autograd FX code and compiled artifacts.

## Why it matters / when it applies
- The fusion check is the first HLO question for any perf hypothesis: an elementwise chain that does not end up in one `kLoop`/`kInput`/`kOutput` fusion is paying extra HBM round-trips ([op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md)).
- Diffing `before_optimizations` across two runs is the cheapest way to see why a graph recompiled or why a flag had no effect (an unchanged HLO means the flag never reached the compiler).
- LLO is where Pallas / custom-kernel work is judged: VMEM allocation sizes, DMA wait placement (`pipeline-emitter-dma-wait`), and whether vector/matrix units dominate the bundle stream.
- Dumps are written for every compiled module, eager ones included; expect many files under DeferAndFuse or Strict eager - grep by the `tt_jit_<file>_L...` name.
- Set the env vars before the TPU runtime initializes - the doc's notebook sets both before `import torch` (which autoloads torch_tpu).

## Also: what the env-var, error-glossary and quant docs add
- **Other files in the HLO dump dir** (env-var doc): `*.after_optimizations.txt` (final HLO), `*.flagfile` (every active XLA flag - check `xla_optimization_level` here) and `*tpu_comp_env.txt` (TPU compilation environment). The error glossary lists `XLA_FLAGS` + `LIBTPU_INIT_ARGS` dumps as debugging level 4 ([tpu-debugging-ladder](tpu-debugging-ladder.md)).
- **Dumping perturbs the cache key.** Both env strings are fingerprinted verbatim into the compile-options key by [`MakeCompileOptionsKey`](../catalog/csrc/common/compilation.cc.md#MakeCompileOptionsKey "csrc/common/compilation.cc:L441"), so a dump run compiles cold and shares no tier-2/tier-3 entries with a non-dump run; capture dumps in a dedicated run, not the timed one.
- **Per-rank directories.** A literal `${RANK}` in `XLA_FLAGS` / `LIBTPU_INIT_ARGS` is replaced with the process rank during `PjrtBackend::InitializeInternal` (`csrc/pjrt/pjrt_state.cc`), e.g. `--xla_dump_to=/tmp/hlo_${RANK}`.
- **Pending graph without compiling.** The not-yet-materialized computation can be printed from Python via [`GetComputationMlir`](../catalog/csrc/internal/sync/sync.cc.md#GetComputationMlir "csrc/internal/sync/sync.cc:L188").
- **Custom-op verification** (quant notebooks): with `torch._logging.set_logs(aot_graphs=True)` plus both dumps on, a JAX-backed custom op shows up as a nested computation in `module_NNNN.tt_jit_custom_kernel.before_optimizations.txt` - the `popcnt` instruction of [one-bit-quantized-sum](one-bit-quantized-sum.md). Those notebooks put the libtpu flags in both `LIBTPU_INIT_ARGS` and `sys.argv` because libtpu "sometimes needs flags, sometimes envvar". Full env-var context: [environment-variables](environment-variables.md).

## Connections
- Code concepts: [compilation-pipeline](../concepts/compilation-pipeline.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md), [compilation-cache](../concepts/compilation-cache.md), [mlir-optimization-passes](../concepts/mlir-optimization-passes.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [profiler](../concepts/profiler.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md)
- Module catalogs: [csrc/ops/op_builder_utils.cc](../catalog/csrc/ops/op_builder_utils.cc.md), [csrc/common/op_name_stack.h](../catalog/csrc/common/op_name_stack.h.md), [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md), [csrc/common/compilation_cache.cc](../catalog/csrc/common/compilation_cache.cc.md), [src/torch_tpu/_internal/compile/debug](../catalog/src/torch_tpu/_internal/compile/debug.md)
- Related doc-concepts: [xla-lowering-stablehlo-hlo-llo.md](xla-lowering-stablehlo-hlo-llo.md), [op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md), [pallas-register-level-fusion.md](pallas-register-level-fusion.md), [xprof-profiling-workflow.md](xprof-profiling-workflow.md), [graph-fingerprint-and-recompilation.md](graph-fingerprint-and-recompilation.md), [environment-variables](environment-variables.md), [tpu-debugging-ladder](tpu-debugging-ladder.md), [one-bit-quantized-sum](one-bit-quantized-sum.md)

## Source
Extracted from `docs/markdown/background_on_torch_compile_on_tpus_via_xla.md` (byte-identical copy: `docs/markdown/4_debugging_and_performance_analysis_4_viewing_compilation_artifacts.md`), sections 1-4; the "Also" section from `docs/markdown/environment_variables.md` (= `docs/markdown/6_reference_4_environment_variables.md`), `docs/markdown/error_glossary.md` (= `docs/markdown/4_debugging_and_performance_analysis_3_getting_better_error_information.md`), `docs/markdown/quant.md` and `docs/markdown/quantized_sum.md` (all kept in place).
