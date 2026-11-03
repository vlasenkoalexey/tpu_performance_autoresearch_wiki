---
title: 'Module: src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.sparse.dsa_gather`/
symbols:
  main_kernel.outer_pipeline._body: main_kernel().outer_pipeline()._body().
  dsa_gather: dsa_gather().
  main_kernel.outer_pipeline.idx_window: main_kernel().outer_pipeline().idx_window().
  main_kernel: main_kernel().
  main_kernel.outer_pipeline: main_kernel().outer_pipeline().
  main_kernel.outer_pipeline._run_gather: main_kernel().outer_pipeline()._run_gather().
  main_kernel.outer_pipeline.subchunk: main_kernel().outer_pipeline().subchunk().
  main_kernel.process_rope: main_kernel().process_rope().
---
# Module: [`src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py)

## Functions
- <a id="main_kernel.outer_pipeline._body"></a>`_body(nope_sem, nope_out_i32, *refs)` — [`L101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py#L101)
- <a id="main_kernel.outer_pipeline._run_gather"></a>`_run_gather()` — [`L168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py#L168)
- <a id="dsa_gather"></a>`dsa_gather(nope_cache: jax.Array, rope_cache: jax.Array, indices: jax.Array, num_valid_indices: jax.Array | None = None)` — [`L197`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py#L197) — Fused SparseCore gather of the nope and rope caches.
- <a id="main_kernel.outer_pipeline.idx_window"></a>`idx_window(r, s)` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py#L98)
- <a id="main_kernel"></a>`main_kernel(nope_in_hbm_ref: Any, rope_in_hbm_ref: Any, indices_hbm_ref: Any, valid_indices_ref: Any, nope_out_hbm_ref: Any, rope_out_hbm_ref: Any, nope_sem: Any, *, core_axis_name: str, subcore_axis_name: str, num_row_subchunks: int, num_streams: int)` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py#L27)
- <a id="main_kernel.outer_pipeline"></a>`outer_pipeline(idx_ref, valid_ref)` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py#L87)
- <a id="main_kernel.process_rope"></a>`process_rope(gather_ref, out_ref, idx_sub, out_row_base=0)` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py#L71)
- <a id="main_kernel.outer_pipeline.subchunk"></a>`subchunk(r, s)` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/dsa_gather.py#L95)

