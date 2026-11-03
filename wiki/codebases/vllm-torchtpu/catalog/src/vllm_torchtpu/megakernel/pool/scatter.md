---
title: 'Module: src/vllm_torchtpu/megakernel/pool/scatter.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/scatter.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.scatter`/
symbols:
  scatter_pool_states: scatter_pool_states().
  scatter_pool_states._kernel: scatter_pool_states()._kernel().
  _PALLAS_NAME: _PALLAS_NAME.
---
# Module: [`src/vllm_torchtpu/megakernel/pool/scatter.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter.py)

## Functions
- <a id="scatter_pool_states._kernel"></a>`_kernel(*refs: Any)` — [`L200`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter.py#L200) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="scatter_pool_states"></a>`scatter_pool_states(layout: PoolLayout, ex: ExecSpec, raw_pools: tuple[jax.Array, ...] | list[jax.Array], pos: jax.Array, page_table: jax.Array, knew: jax.Array, vnew: jax.Array, conv: jax.Array | None = None, rec: jax.Array | None = None, ckpt_indices: jax.Array | None = None, active_seqs: jax.Array | str | None = None, *, interpret: bool | None = None, conv_partial: bool | None = None)` — [`L44`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter.py#L44) — Scatter `knew`/`vnew` and GDN `conv`/`rec` checkpoints into `raw_pools` in-place. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)

## Module values
- <a id="_PALLAS_NAME"></a>`_PALLAS_NAME` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/scatter.py#L38)

