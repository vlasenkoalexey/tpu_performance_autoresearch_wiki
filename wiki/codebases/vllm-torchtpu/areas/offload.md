---
title: 'Area: src/vllm_torchtpu/offload'
type: area
area: 'src/vllm_torchtpu/offload'
description: 'Host-DRAM offload of vLLM prefix-cache KV blocks on TPU: a controller-driven OffloadingConnector backed by a C++ KV store that owns the directory, LRU, pins and DMAs, with TPU workers acting as passive DMA endpoints.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/offload`

## Purpose
Host offload extends vLLM's prefix cache beyond HBM. When the scheduler would drop a computed KV block, the block is copied into a host-DRAM pool, and a later request with the same prefix loads it back instead of recomputing the prefill. This area plugs into vLLM's generic `OffloadingConnector` contract but replaces its per-worker transfer engine with a controller-driven design. One C++ KV store in the scheduler process owns the hash-to-slot directory, the LRU, the pins and the DMAs. Each TPU worker registers its HBM KV buffers once and then only serves DMAs.

[host-offload](../concepts/host-offload.md) owns the mechanism: the translation of vLLM's lookup/prepare/submit calls into store operations, the fencing of stores behind the forward that wrote the blocks, the exactly-once pin accounting, and the optional cross-replica sharing and storage tier. What it hands the rest of the repo is a larger effective prefix cache: higher hit rates and less prefill compute for repeated prompts, paid for with host-link bandwidth and a block layout that makes transfers contiguous.

Its runtime touch points are the [executors](executors.md), which prewarm the H2D transfer kernels per shape at startup, and the [KV cache layout](../concepts/kv-cache-layout-and-hbm-budget.md), whose block-major option exists partly so that one block's bytes across layers are contiguous for transfer.

## How the units connect
All three modules belong to [host-offload](../concepts/host-offload.md): `raiden_connector.py` is the connector vLLM instantiates (scheduler and worker roles), `raiden_store.py` holds the scheduler-side offloading manager that drives the store and does the pin/fence bookkeeping, and `block_major_layout.py` describes the block-major KV layout the transfers rely on (`block_major_layer_indices`, per-rank KV bytes per block). The same store family also backs the Raiden transports in [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/offload`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/offload` | 3 | 228 | 4 | [`record_all_ranks_kv_bytes_per_block`](../catalog/src/vllm_torchtpu/offload/raiden_store.md#record_all_ranks_kv_bytes_per_block "src/vllm_torchtpu/offload/raiden_store.py:L186"), [`block_major_layer_indices`](../catalog/src/vllm_torchtpu/offload/block_major_layout.md#block_major_layer_indices "src/vllm_torchtpu/offload/block_major_layout.py:L94") | [host-offload](../concepts/host-offload.md) |

## Small units
### `src/vllm_torchtpu/offload`
- modules: `src/vllm_torchtpu/offload/block_major_layout.py`, `src/vllm_torchtpu/offload/raiden_connector.py`, `src/vllm_torchtpu/offload/raiden_store.py`
- entry points: [`record_all_ranks_kv_bytes_per_block`](../catalog/src/vllm_torchtpu/offload/raiden_store.md#record_all_ranks_kv_bytes_per_block "src/vllm_torchtpu/offload/raiden_store.py:L186"), [`block_major_layer_indices`](../catalog/src/vllm_torchtpu/offload/block_major_layout.md#block_major_layer_indices "src/vllm_torchtpu/offload/block_major_layout.py:L94")
- hubs: [`submit_store_job`](../catalog/src/vllm_torchtpu/offload/raiden_store.md#RaidenOffloadingManager.submit_store_job "src/vllm_torchtpu/offload/raiden_store.py:L911"), [`get_manager`](../catalog/src/vllm_torchtpu/offload/raiden_store.md#TPURaidenStoreOffloadingSpec.get_manager "src/vllm_torchtpu/offload/raiden_store.py:L2552"), [`_finalize`](../catalog/src/vllm_torchtpu/offload/raiden_store.md#RaidenOffloadingManager._finalize "src/vllm_torchtpu/offload/raiden_store.py:L1129")

<!-- area:auto:end -->
