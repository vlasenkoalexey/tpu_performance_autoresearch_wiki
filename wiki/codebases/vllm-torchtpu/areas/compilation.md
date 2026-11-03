---
title: 'Area: src/vllm_torchtpu/compilation'
type: area
area: 'src/vllm_torchtpu/compilation'
description: 'The TorchTPU compile backend vLLM calls once per (subgraph, token bucket): it lowers the captured FX graph to one PjRt executable per bucket, keys and persists the AOT cache, and keeps trace-time shape decisions correct per bucket.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/compilation`

## Purpose
This area is the TPU side of vLLM's `VLLM_COMPILE` contract. The [TPU platform](../concepts/tpu-platform.md) names its compiler adaptor as vLLM's compile backend and hands it a ladder of token buckets; vLLM then calls the adaptor's `compile` / `load` once for every (subgraph, bucket) pair. What leaves the area is one TorchTPU PjRt executable per bucket plus a bundled on-disk artifact, which is what turns a warm restart from tens of minutes of compilation into a cache load. For inference performance it decides two things: how long startup and precompile take, and whether serving ever pays a surprise recompile.

Everything here is a single unit owned by [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md), which documents the compile/load path, the compilation hash that keys every cache (it folds in Pallas kernel sources, TPU env vars, library versions and the KV block count that Dynamo cannot see), per-bucket re-tracing for models that branch on the token count, and peer replay of compiled buckets across ranks. Read that page rather than this one for the mechanism.

The area's inputs come from the [model runner](../concepts/tpu-model-runner.md), whose precompile walks the bucket ladder, and from the worker's kernel-reload RPC; its outputs are consumed by the runner's per-step forward, which should only ever hit already-compiled buckets.

## How the units connect
- `tpu_compiler.py` is the core: the compiler adaptor's `compile` / `load` and `compute_tpu_compilation_hash`, the key every cached artifact sits under.
- `shape_variants.py` sits beside the adaptor: it reads the shape guards a trace discharged, lets a graph build only the buckets those guards accept, and hands executables built by later re-traces back to the live graph (`retrace`, `defer`, `aot_cache_tag`), so each bucket still has exactly one executable.
- `kernel_reload.py` is a developer path for `TPU_KERNEL_ITER_MODE=1`: reloadable Pallas custom ops dispatch through an indirection that `reload_kernels` swaps after re-importing the kernel modules, so a kernel edit costs one kernel compile instead of a server restart. The hash in `tpu_compiler.py` leaves those modules out in this mode so the backbone executables stay cached.

All three are described on [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/compilation`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/compilation` | 3 | 101 | 11 | [`compute_tpu_compilation_hash`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#compute_tpu_compilation_hash "src/vllm_torchtpu/compilation/tpu_compiler.py:L417"), [`aot_cache_tag`](../catalog/src/vllm_torchtpu/compilation/shape_variants.md#aot_cache_tag "src/vllm_torchtpu/compilation/shape_variants.py:L307"), [`defer`](../catalog/src/vllm_torchtpu/compilation/shape_variants.md#defer "src/vllm_torchtpu/compilation/shape_variants.py:L428") | [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md) |

## Small units
### `src/vllm_torchtpu/compilation`
- modules: `src/vllm_torchtpu/compilation/kernel_reload.py`, `src/vllm_torchtpu/compilation/shape_variants.py`, `src/vllm_torchtpu/compilation/tpu_compiler.py`
- entry points: [`compute_tpu_compilation_hash`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#compute_tpu_compilation_hash "src/vllm_torchtpu/compilation/tpu_compiler.py:L417"), [`aot_cache_tag`](../catalog/src/vllm_torchtpu/compilation/shape_variants.md#aot_cache_tag "src/vllm_torchtpu/compilation/shape_variants.py:L307"), [`defer`](../catalog/src/vllm_torchtpu/compilation/shape_variants.md#defer "src/vllm_torchtpu/compilation/shape_variants.py:L428"), [`reload_kernels`](../catalog/src/vllm_torchtpu/compilation/kernel_reload.md#reload_kernels "src/vllm_torchtpu/compilation/kernel_reload.py:L139"), [`retrace`](../catalog/src/vllm_torchtpu/compilation/shape_variants.md#retrace "src/vllm_torchtpu/compilation/shape_variants.py:L321")
- hubs: [`compile`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#TpuCompilerAdaptor.compile "src/vllm_torchtpu/compilation/tpu_compiler.py:L791"), [`load`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#TpuCompilerAdaptor.load "src/vllm_torchtpu/compilation/tpu_compiler.py:L913")

<!-- area:auto:end -->
