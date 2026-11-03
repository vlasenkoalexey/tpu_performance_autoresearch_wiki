---
title: Kernel design at the hardware-resource level (VREG, VMEM, SMEM, HBM, MXU, DMA)
type: doc-concept
provenance: doc
source: docs/developers_guide/optimization_best_practices.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Kernel design at the hardware-resource level (VREG, VMEM, SMEM, HBM, MXU, DMA)

## Definition
The optimization guide requires kernel decisions in vllm-torchtpu to be argued in terms
of concrete TPU resources - vector registers, VMEM, SMEM, HBM bandwidth, MXU dtype
throughput and DMA latency - and to "let the compiler work" for sharding. Rules P-5 to
P-13 and P-17 are the points that come up most in review; the background hardware model
is the JAX scaling book and the Pallas TPU docs.

## The rules
| ID | Resource | Rule |
|---|---|---|
| P-5 | Sharding | Shard via jit `in_shardings` / `out_shardings` instead of manual reshard functions; use the global mesh context instead of threading `mesh` everywhere |
| P-6 | Collectives | Cast to bf16 **before** collectives when numerics tolerate it, and verify like any dtype change |
| P-7 | VREG | Quantize per loop iteration to avoid spills; no up-front zero-init accumulators; write to `out_ref` on the last step instead of scratch-then-copy |
| P-8 | HBM traffic | Avoid unnecessary zero-init; fuse to avoid HBM round trips |
| P-9 | MXU | w8a16 beats w16a16 - never silently upcast to 16-bit compute; ride 4-bit weights on the fp8 path (u4 -> fp8, not u4 -> bf16); unpack with shifts/masks, not dtype cast chains |
| P-10 | SMEM | Do not allocate the maximum; leave compiler headroom |
| P-11 | DMA | Small DMAs are latency-bound - fewer hops beat equal total bytes; derive the split crossover from a cost model; never `start(); wait()` back to back - pipeline with buffering |
| P-12 | Layout | Fix interleaved splits by preprocessing weights at load; sublane `jnp.repeat` inside a kernel is not cheap |
| P-13 | Barriers | `jax.named_scope` and a `lax.cond` in the hot loop are hidden optimization barriers (a `lax.cond` in the main kernel loop regresses all workloads); do not allocate never-read memory to keep a signature fixed |
| P-17 | Envelope | Know each kernel's hard envelope (mesh rank, EP-only, dtype packing, JAX version range) and gate callers on it explicitly |

## In vllm-torchtpu (grounded)
- P-5 in practice: kernels that run as SPMD programs go through
  [`sharded_jax_op`](../catalog/src/vllm_torchtpu/distributed/sharded_jax_op.md#sharded_jax_op),
  which takes explicit input/output `PartitionSpec`s (output specs are mandatory because
  a wrong one silently turns a sharded output into a replicated one). Mesh axis names
  come from shared constants such as
  [`EP_AXIS_NAME`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#EP_AXIS_NAME)
  and [`build_ep_mesh`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#build_ep_mesh)
  (R-4.5 of the coding guidance).
- Deliberate barriers are explicit rather than accidental: the torch-side
  [`optimization_barrier`](../catalog/src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.md#optimization_barrier)
  custom op exists for the cases where one is wanted.
- P-17 / R-2.3 envelope predicates live next to the kernel, e.g.
  [`adaptive_fused_moe_supported`](../catalog/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/vllm_adapter.md#adaptive_fused_moe_supported)
  in the adaptive fused-MoE kernel's adapter. Hardware facts are meant to come from
  runtime queries (`pltpu.get_tpu_info()` - used for sublane counts and SparseCore
  info in several kernels) rather than literals.
- P-9's "4-bit weights on the fp8 path" is the design the MoE quant methods follow
  (see [quantization-methods](../concepts/quantization-methods.md) and
  [fused-moe-kernels](../concepts/fused-moe-kernels.md)).

## Why it matters / when it applies
Applies to every change under `src/vllm_torchtpu/kernels/` (R-2.7 makes this section
mandatory reading for that directory). These are the levers an optimization pass on
attention, MoE, GDN or quantized-matmul kernels actually pulls; the evidence for any of
them is a trace and, for fusion/layout claims, the compiled HLO
([perf-evidence-standard](perf-evidence-standard.md)).

## Doc vs code at this commit
- The coding guidance names envelope predicates `is_supported_by_*`; no function with
  that prefix exists under `kernels/` at this commit - the predicates are named per
  kernel (for example `adaptive_fused_moe_supported`, `check_scatter_rows_supported`).
- R-4.4 forbids hard-coded hardware constants, but
  `kernels/quantized_matmul/tuned_block_sizes.py` keeps a literal
  `DEVICE_VMEM_LIMIT = {6: 96 MiB, 7: 48 MiB}` keyed by a TPU version parsed from
  `device_kind`, and
  [`TpuPlatform.fp8_dtype`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.fp8_dtype)
  selects `float8_e5m2` by comparing the device name to `"tpu v6e"`.
- R-4.5 itself flags the literal `P("model")` repeated in `layers/core/` as a known
  anti-pattern still present.

## Connections
- Code concepts: [ragged-paged-attention-kernel](../concepts/ragged-paged-attention-kernel.md),
  [fused-moe-kernels](../concepts/fused-moe-kernels.md),
  [adaptive-fused-moe-kernel](../concepts/adaptive-fused-moe-kernel.md),
  [gated-deltanet-kernels](../concepts/gated-deltanet-kernels.md),
  [sparsecore-ragged-gather-scatter](../concepts/sparsecore-ragged-gather-scatter.md),
  [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [custom-ops](../concepts/custom-ops.md)
- Module catalogs: [distributed/sharded_jax_op](../catalog/src/vllm_torchtpu/distributed/sharded_jax_op.md),
  [distributed/ep_mesh](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md),
  [custom_ops/optimization_barrier_op](../catalog/src/vllm_torchtpu/layers/adapter/custom_ops/optimization_barrier_op.md)
- Related doc-concepts: [tuned-block-size-tables](tuned-block-size-tables.md),
  [perf-evidence-standard](perf-evidence-standard.md),
  [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md),
  [derive-dont-declare](derive-dont-declare.md)

## Source
Extracted from `docs/developers_guide/optimization_best_practices.md` sections 1.2-1.4
and 3 (kept in place).
