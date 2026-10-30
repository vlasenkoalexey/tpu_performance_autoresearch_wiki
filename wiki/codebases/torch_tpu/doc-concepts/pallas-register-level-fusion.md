---
title: Register-level fusion with a Pallas custom op (quantize+pack case study)
type: doc-concept
provenance: doc
source: docs/markdown/custom_ops_via_pallas.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Register-level fusion with a Pallas custom op (quantize+pack case study)

## Definition
The advanced Pallas doc frames custom kernels as a performance tool: Pallas gives control over the TPU memory hierarchy (HBM -> VMEM -> registers), so two passes that would round-trip an intermediate through HBM can be merged into one kernel that does a single HBM read and a single HBM write. Its case study, inspired by DeepSeek-V3's Triton `act_quant` kernel, merges blockwise sign-binarization (scale = mean |x|) and 32-to-1 bit-packing into one `quant_and_pack` kernel whose shifts and packing happen "entirely within the TPU registers", replacing the two-pass composition version (`quantize` then `pack32`).

## In torch_tpu (grounded)
- The fused kernel is plain Pallas/JAX (`pl.pallas_call` with two outputs: a `uint32` packed vector and an `f32` scale) and is exposed to PyTorch with [`jax_op`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#jax_op) as `testing_op::quant_and_pack`; after that line "the rest of this code is pure PyTorch". The mechanics of that bridge (schema inference, fake kernel, MLIR fingerprint, registration) are on [pallas-jax-op-bridge](pallas-jax-op-bridge.md).
- Calling the op only records a deferred op; the doc forces execution with `packed.cpu()` / `scale.cpu()`. In code, [`JaxCallable.__call__`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#JaxCallable.__call__ "src/torch_tpu/_internal/pallas/pallas.py:L1198") dispatches through [`DispatchOp`](../catalog/csrc/eager/op_dispatcher.h.md#DispatchOp "csrc/eager/op_dispatcher.h:L312") and the kernel is inlined into the graph by [`CallCustomKernel`](../catalog/csrc/ops/custom_kernels.cc.md#CallCustomKernel); materialization happens at the host copy ([host-device-copy](../concepts/host-device-copy.md)).
- **Inspecting what was generated.** The doc's setup cell is a reusable recipe for seeing the compiled artifacts of a custom op:
  - `LIBTPU_INIT_ARGS="--xla_jf_dump_to=/tmp/llo_dump --xla_jf_dump_llo_text=true"` (also appended to `sys.argv`) dumps the low-level LLO text for the TPU program, which is where register/VMEM behavior of the Pallas body is visible.
  - `XLA_FLAGS="--xla_dump_to=/tmp/xla_dump --xla_dump_hlo_as_text"` dumps the HLO modules (the Pallas body appears as a custom call inside the surrounding module).
  - `torch._logging.set_logs(aot_graphs=True)` prints the AOTAutograd graphs, showing the custom op as a single node.
  Both flags must be set before `import torch`. `LIBTPU_INIT_ARGS` is a stable public env var and `XLA_FLAGS` an experimental one ([public-api-surface-inventory](public-api-surface-inventory.md)).

## Why it matters / when it applies
- **Profile the baseline first.** The doc insists on an unoptimized PyTorch baseline (its `quant.py`) both as the numerical-correctness oracle and as the performance reference; writing a kernel is justified only after profiling shows the HBM round-trip matters ([profiler](../concepts/profiler.md)).
- **When fusion pays.** The win comes from eliminating a materialized intermediate between memory-bound passes (binarized signs written to HBM only to be read back for packing). Compute-bound or already-fused XLA chains gain little; check the HLO dump to see whether XLA already fused the composition before hand-writing a kernel.
- **Correctness check is built in.** The example asserts a known answer (scale 4.0, packed `0x66666666`) - the same parity-against-reference discipline that any custom kernel needs before timing.
- The kernel shown is a single-block (no grid/BlockSpec) toy; real kernels add tiling over the grid, which is outside this doc's scope (it points to the JAX Pallas docs).

## Connections
- Code concepts: [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [compilation-pipeline](../concepts/compilation-pipeline.md), [mlir-optimization-passes](../concepts/mlir-optimization-passes.md), [profiler](../concepts/profiler.md), [host-device-copy](../concepts/host-device-copy.md), [dtype-and-precision](../concepts/dtype-and-precision.md)
- Module catalogs: [src/torch_tpu/_internal/pallas/pallas](../catalog/src/torch_tpu/_internal/pallas/pallas.md), [csrc/ops/custom_kernels.cc](../catalog/csrc/ops/custom_kernels.cc.md)
- Related doc-concepts: [pallas-jax-op-bridge](pallas-jax-op-bridge.md), [extending-via-composition](extending-via-composition.md), [pytorch-extension-ladder](pytorch-extension-ladder.md), [xprof-profiling-workflow](xprof-profiling-workflow.md)

## Source
Extracted from `docs/markdown/custom_ops_via_pallas.md` (kept in place).
