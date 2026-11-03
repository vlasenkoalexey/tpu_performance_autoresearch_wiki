---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.core_attention.csa_gather`/
symbols:
  csa_gather: csa_gather().
  main_kernel.outer_pipeline: main_kernel().outer_pipeline().
  main_kernel.outer_pipeline._body: main_kernel().outer_pipeline()._body().
  main_kernel.outer_pipeline.idx_window: main_kernel().outer_pipeline().idx_window().
  main_kernel: main_kernel().
  main_kernel.outer_pipeline._run_gather: main_kernel().outer_pipeline()._run_gather().
  main_kernel.outer_pipeline.subchunk: main_kernel().outer_pipeline().subchunk().
  main_kernel.process_rope: main_kernel().process_rope().
  main_kernel.outer_pipeline.rope_out_block: main_kernel().outer_pipeline().rope_out_block().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py)

## Functions
- <a id="main_kernel.outer_pipeline._body"></a>`_body(*refs)` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L100)
- <a id="main_kernel.outer_pipeline._run_gather"></a>`_run_gather()` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L173)
- <a id="csa_gather"></a>`csa_gather(nope_cache: jax.Array, rope_cache: jax.Array, indices: jax.Array, num_valid_indices: jax.Array | None = None, *, top_k: int = 1024)` — [`L202`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L202) — Fused SparseCore gather of the nope and rope caches.
- <a id="main_kernel.outer_pipeline.idx_window"></a>`idx_window(r, s)` — [`L94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L94)
- <a id="main_kernel"></a>`main_kernel(nope_in_hbm_ref: Any, rope_in_hbm_ref: Any, indices_hbm_ref: Any, valid_indices_ref: Any, nope_out_hbm_ref: Any, rope_out_hbm_ref: Any, nope_sem: Any, *, core_axis_name: str, subcore_axis_name: str, num_row_subchunks: int, num_streams: int, top_k: int)` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L28)
- <a id="main_kernel.outer_pipeline"></a>`outer_pipeline(idx_ref, valid_ref)` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L81)
- <a id="main_kernel.process_rope"></a>`process_rope(gather_ref, out_ref, out_row_base=0)` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L64)
- <a id="main_kernel.outer_pipeline.rope_out_block"></a>`rope_out_block(r)` — [`L163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L163)
- <a id="main_kernel.outer_pipeline.subchunk"></a>`subchunk(r, s)` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/csa_gather.py#L91)

