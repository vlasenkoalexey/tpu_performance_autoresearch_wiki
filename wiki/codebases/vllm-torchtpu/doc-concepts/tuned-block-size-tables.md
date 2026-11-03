---
title: Tuned block-size tables (tuning values are data, not knobs)
type: doc-concept
provenance: doc
source: docs/developers_guide/optimization_best_practices.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Tuned block-size tables (tuning values are data, not knobs)

## Definition
Kernel block sizes in vllm-torchtpu live in **tuned tables inside the kernel
directory** (`kernels/*/tuned_block_sizes.py`), keyed by workload and imported as normal
Python data. A lookup miss logs `warning_once` with the full key; new workloads add
table entries, never env overrides (rule P-16). Every threshold should be computable
from a cost model (DMA latency vs bandwidth, VMEM budget per TPU generation), with a
code pointer to the derivation (P-15). The coding guidance backs this from the other
side: tuning values must never become flags or env vars (R-6.2).

## In vllm-torchtpu (grounded)
Tables present at this commit:

| Kernel | Table module | Lookup |
|---|---|---|
| Ragged paged attention v3 (head dim 64) | `kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.py` | [`get_tuned_block_sizes`](../catalog/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.md#get_tuned_block_sizes), keys from [`get_lookup_keys`](../catalog/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.md#get_lookup_keys) / [`get_simplified_raw_key`](../catalog/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.md#get_simplified_raw_key) |
| Quantized matmul | `kernels/quantized_matmul/tuned_block_sizes.py` | [`get_tuned_block_sizes`](../catalog/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.md#get_tuned_block_sizes), key = (TPU version, n_batch, n_out, n_in, x dtype, w dtype); miss -> `(128, 128, 128)` |
| Megablox grouped matmul | `kernels/megablox/tuned_block_sizes.py` | [`get_tuned_block_sizes`](../catalog/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.md#get_tuned_block_sizes), fallback [`get_default_gmm_block_sizes`](../catalog/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.md#get_default_gmm_block_sizes) |

Related per-kernel parameter tables use other file names:
`kernels/flash_attention/tuned_params.py`, `kernels/mla/v2/tuned_params.py`, and
`kernels/collectives/all_gather_matmul_tuned_block_sizes.py`. All three main lookups log
misses through `warning_once`, as P-16 requires.

## Why it matters / when it applies
- A block-size miss silently falls back to a generic tile, which can cost a large
  fraction of kernel throughput on an untuned shape. The `warning_once` with the full
  key is the signal to look for in server logs when a new model, head dim, TP degree or
  quant dtype underperforms; the fix is a new table entry for that key.
- Keeping tables as importable data (not JSON resolved through `__file__`) keeps them
  packaged and reviewable; keeping them out of env vars avoids a knob every user must
  set correctly ([derive-dont-declare](derive-dont-declare.md)).
- Tables are keyed per TPU generation where it matters (the quantized-matmul key starts
  with the TPU version), so v6e and v7x entries coexist.

## Doc vs code at this commit
- The quantized-matmul table module also carries a hard-coded per-generation VMEM map
  (`DEVICE_VMEM_LIMIT`, 96 MiB for v6, 48 MiB for v7, 96 MiB fallback with a warning),
  which sits in tension with R-4.4's "use `pltpu.get_tpu_info()`, never literals".
- Not every kernel follows the `tuned_block_sizes.py` file name the doc gives
  (`tuned_params.py`, `all_gather_matmul_tuned_block_sizes.py`).

## Connections
- Code concepts: [ragged-paged-attention-kernel](../concepts/ragged-paged-attention-kernel.md),
  [batched-ragged-paged-attention-kernel](../concepts/batched-ragged-paged-attention-kernel.md),
  [fused-moe-kernels](../concepts/fused-moe-kernels.md),
  [quantization-methods](../concepts/quantization-methods.md),
  [mla-attention-kernels](../concepts/mla-attention-kernels.md)
- Module catalogs: [ragged_paged_attention/v3/tuned_block_sizes_hd64](../catalog/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/tuned_block_sizes_hd64.md),
  [quantized_matmul/tuned_block_sizes](../catalog/src/vllm_torchtpu/kernels/quantized_matmul/tuned_block_sizes.md),
  [megablox/tuned_block_sizes](../catalog/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.md)
- Related doc-concepts: [kernel-hardware-resource-rules](kernel-hardware-resource-rules.md),
  [derive-dont-declare](derive-dont-declare.md),
  [perf-evidence-standard](perf-evidence-standard.md)

## Source
Extracted from `docs/developers_guide/optimization_best_practices.md` (P-15, P-16) and
`docs/developers_guide/coding_guidance.md` (R-6.2) (kept in place).
