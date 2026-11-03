---
title: 'Module: src/vllm_torchtpu/kernels/mla/scatter_utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/scatter_utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.scatter_utils`/
symbols:
  scatter_rows: scatter_rows().
  _scatter_kernel: _scatter_kernel().
  split_plan: split_plan().
  Plan.total_tokens: Plan#total_tokens().
  _scatter_kernel.body: _scatter_kernel().body().
  Plan.lanes_per_block: Plan#lanes_per_block.
  Plan.blocks_per_round: Plan#blocks_per_round().
  Plan.cores_per_block: Plan#cores_per_block.
  Plan.lanes_per_core: Plan#lanes_per_core().
  _scatter_kernel.block_index: _scatter_kernel().block_index().
  Plan: Plan#
  Plan.steps_per_core: Plan#steps_per_core.
  Plan.num_cores: Plan#num_cores.
---
# Module: [`src/vllm_torchtpu/kernels/mla/scatter_utils.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py)

## Classes
### <a id="Plan"></a>`Plan`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/mla/scatter_utils.py:29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L29)
- doc: How one step's tokens are spread over the vector subcores.
- signature: `class Plan(NamedTuple):`
- members:
  - <a id="Plan.blocks_per_round"></a>`blocks_per_round(self)` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L47)
  - <a id="Plan.lanes_per_core"></a>`lanes_per_core(self)` — [`L43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L43)
  - <a id="Plan.total_tokens"></a>`total_tokens(self)` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L51) — Tokens the grid covers; the inputs must be padded to this.
  - <a id="Plan.cores_per_block"></a>`cores_per_block` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L38)
  - <a id="Plan.lanes_per_block"></a>`lanes_per_block` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L37)
  - <a id="Plan.num_cores"></a>`num_cores` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L39)
  - <a id="Plan.steps_per_core"></a>`steps_per_core` — [`L40`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L40)
- used by: [`scatter_rows`](scatter_utils.md#scatter_rows), [`_scatter_kernel`](scatter_utils.md#_scatter_kernel), [`split_plan`](scatter_utils.md#split_plan), [`body`](scatter_utils.md#_scatter_kernel.body), [`block_index`](scatter_utils.md#_scatter_kernel.block_index)

## Functions
- <a id="_scatter_kernel"></a>`_scatter_kernel(dst_hbm_ref: Any, src_ref: Any, cache_ref: Any, sem: Any, *, core_axis_name: str, subcore_axis_name: str, plan: Plan, tc_tiled: bool)` — [`L75`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L75)
- <a id="_scatter_kernel.block_index"></a>`block_index(step)` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L99)
- <a id="_scatter_kernel.body"></a>`body(dst_ref, src_buf)` — [`L102`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L102)
- <a id="scatter_rows"></a>`scatter_rows(cache: jax.Array, src: jax.Array, dst_rows: jax.Array, name: str = "scatter_kv_cache")` — [`L145`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L145) — Writes one row of `src` per token into `cache`. — documented in [mla-attention-kernels](../../../../../concepts/mla-attention-kernels.md)
- <a id="split_plan"></a>`split_plan(num_tokens: int, num_lanes: int, num_cores: int)` — [`L56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/scatter_utils.py#L56) — Choose the token -> subcore mapping for a step of ``num_tokens``.

