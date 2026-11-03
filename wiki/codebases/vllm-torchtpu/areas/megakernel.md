---
title: 'Area: src/vllm_torchtpu/megakernel'
type: area
area: 'src/vllm_torchtpu/megakernel'
description: 'A self-contained JAX + Pallas library for a decode megakernel: one Pallas kernel per step that runs every layer and streams weights through VMEM rings, declared from composable modules and planned at build time, with a unified fp8 KV/recurrent-state pool.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/megakernel`

## Purpose
The megakernel replaces one XLA program per op with one Pallas kernel that runs every layer of a decode (or MTP-verify) step, streaming weights from HBM through VMEM rings. That removes per-op launch and HBM round-trips for activations, which dominate small-batch decode. [megakernel](../concepts/megakernel.md) owns the design. A model is declared as composable modules arranged into one repeating layer, and a pure build-time planner turns that declaration plus an `ExecSpec` (batch rows, tokens per sequence, TP/EP ranks, context, tiles) into tile sizes, a static weight-stream schedule and per-rank operand shapes.

[megakernel-pool](../concepts/megakernel-pool.md) covers the cache side. All per-sequence state for a hybrid attention/GDN model lives in one raw fp8 pool per attention layer, with recurrent-state checkpoint slots attached to the next attention layer's pool, and separate gather/scatter Pallas kernels move state in and out per step.

At this commit the package is a library in waiting. Nothing else under `src/` imports it (only its tests do), and the emitter that would build the fused layer-loop `pallas_call` is not in the tree. Treat it as a design reference for decode-side fusion rather than a serving path.

## How the units connect
- [megakernel](../concepts/megakernel.md) (package root): module declarations, `ExecSpec` and tiles, the planner, ops and the profile entry; it consumes the pool backend as callbacks on the model spec.
- [megakernel-pool](../concepts/megakernel-pool.md) (`pool/`): `PoolLayout` (the byte contract), gather/scatter kernels and `make_pool_backend`, which packages them for the root.
- `profiles/` (no page) holds `default_tiles`, the model-agnostic tile rule the root re-exports. It returns the same tiles for every bucket (library defaults, flat-ring all-reduce, and the chip's VMEM/SMEM budgets from `CHIP_BUDGETS`, sized by default for TPU v7x, the only chip the megakernel is validated on). It never queries devices at import time; ring depths may be refined at build time to fit VMEM when `ExecSpec.tiles` is left unset.

<!-- area:auto:begin -->
## Units
3 planned unit(s) in `src/vllm_torchtpu/megakernel`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/megakernel/pool` | 12 | 218 | 2 | [`cache_exec`](../catalog/src/vllm_torchtpu/megakernel/pool/config.md#cache_exec "src/vllm_torchtpu/megakernel/pool/config.py:L110"), [`with_cache`](../catalog/src/vllm_torchtpu/megakernel/pool/config.md#with_cache "src/vllm_torchtpu/megakernel/pool/config.py:L120"), [`pool_gather`](../catalog/src/vllm_torchtpu/megakernel/pool/config.md#CacheExec.pool_gather "src/vllm_torchtpu/megakernel/pool/config.py:L69") | [megakernel-pool](../concepts/megakernel-pool.md) |
| `src/vllm_torchtpu/megakernel` | 11 | 384 | 43 | [`ExecSpec`](../catalog/src/vllm_torchtpu/megakernel/exec_spec.md#ExecSpec "src/vllm_torchtpu/megakernel/exec_spec.py:L187"), [`BF16`](../catalog/src/vllm_torchtpu/megakernel/ops.md#BF16 "src/vllm_torchtpu/megakernel/ops.py:L24"), [`FP8`](../catalog/src/vllm_torchtpu/megakernel/ops.md#FP8 "src/vllm_torchtpu/megakernel/ops.py:L28") | [megakernel](../concepts/megakernel.md) |
| `src/vllm_torchtpu/megakernel/profiles` | 2 | 12 | 3 | [`default_tiles`](../catalog/src/vllm_torchtpu/megakernel/profiles/default.md#default_tiles "src/vllm_torchtpu/megakernel/profiles/default.py:L82") | section below |

## Small units
### `src/vllm_torchtpu/megakernel/profiles`
- modules: `src/vllm_torchtpu/megakernel/profiles/__init__.py`, `src/vllm_torchtpu/megakernel/profiles/default.py`
- entry points: [`default_tiles`](../catalog/src/vllm_torchtpu/megakernel/profiles/default.md#default_tiles "src/vllm_torchtpu/megakernel/profiles/default.py:L82")
- hubs: [`chip_budget`](../catalog/src/vllm_torchtpu/megakernel/profiles/default.md#chip_budget "src/vllm_torchtpu/megakernel/profiles/default.py:L62"), [`ChipBudget`](../catalog/src/vllm_torchtpu/megakernel/profiles/default.md#ChipBudget "src/vllm_torchtpu/megakernel/profiles/default.py:L42")

<!-- area:auto:end -->
