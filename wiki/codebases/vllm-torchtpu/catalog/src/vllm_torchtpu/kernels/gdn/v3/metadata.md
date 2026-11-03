---
title: 'Module: src/vllm_torchtpu/kernels/gdn/v3/metadata.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/v3/metadata.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.v3.metadata`/
symbols:
  compute_per_seq_metadata: compute_per_seq_metadata().
  compute_batched_seq_metadata: compute_batched_seq_metadata().
---
# Module: [`src/vllm_torchtpu/kernels/gdn/v3/metadata.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/metadata.py)

## Functions
- <a id="compute_batched_seq_metadata"></a>`compute_batched_seq_metadata(cfg: config.GDNConfig, seq_lens: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, read_offsets: jax.Array, end_seq: jax.Array, ckpt_indices: jax.Array | None = None)` — [`L22`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/metadata.py#L22) — Metadata for computing multiple sequences per tile.
- <a id="compute_per_seq_metadata"></a>`compute_per_seq_metadata(cfg: config.GDNConfig, seq_lens: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, read_offsets: jax.Array, start_seq: jax.Array, end_seq: jax.Array, ckpt_indices: jax.Array | None = None)` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/v3/metadata.py#L66) — Metadata for computing single sequence per tile. — documented in [gated-deltanet-kernels](../../../../../../concepts/gated-deltanet-kernels.md)

