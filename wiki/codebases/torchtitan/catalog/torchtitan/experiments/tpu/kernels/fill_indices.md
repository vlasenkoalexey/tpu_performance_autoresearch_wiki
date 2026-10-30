---
title: 'Module: torchtitan/experiments/tpu/kernels/fill_indices.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/fill_indices.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.fill_indices`/
symbols:
  fill_indices: fill_indices().
  fill_indices.fill_indices_jax: fill_indices().fill_indices_jax().
  fill_indices.fill_indices_jax.segment_body: fill_indices().fill_indices_jax().segment_body().
  _fill_indices_kernel_cache: _fill_indices_kernel_cache.
  fill_indices.fill_indices_jax.segment_body.atom_body: fill_indices().fill_indices_jax().segment_body().atom_body().
---
# Module: [`torchtitan/experiments/tpu/kernels/fill_indices.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fill_indices.py)

## Functions
- <a id="fill_indices.fill_indices_jax.segment_body.atom_body"></a>`atom_body(j, atom_out)` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fill_indices.py#L70)
- <a id="fill_indices"></a>`fill_indices(tokens_per_expert_group: torch.Tensor, start_index_values: torch.Tensor, write_offsets: torch.Tensor, experts_per_rank: int, num_ranks: int, max_len: int)` — [`L10`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fill_indices.py#L10) — Prepare permutation indices and the number of tokens for each expert. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- <a id="fill_indices.fill_indices_jax"></a>`fill_indices_jax(tpeg, siv, wo)` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fill_indices.py#L41)
- <a id="fill_indices.fill_indices_jax.segment_body"></a>`segment_body(i, current_out)` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fill_indices.py#L65)

## Module values
- <a id="_fill_indices_kernel_cache"></a>`_fill_indices_kernel_cache` — [`L8`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fill_indices.py#L8)

