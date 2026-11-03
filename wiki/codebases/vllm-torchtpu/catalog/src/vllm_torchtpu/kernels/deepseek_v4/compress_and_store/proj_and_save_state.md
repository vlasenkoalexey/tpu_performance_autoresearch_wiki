---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.compress_and_store.proj_and_save_state`/
symbols:
  proj_and_save_state: proj_and_save_state().
  kernel: kernel().
  kernel.inner_kernel.process: kernel().inner_kernel().process().
  Configs.num_m: Configs#num_m().
  Configs.tile_sizes: Configs#tile_sizes.
  Configs.num_k: Configs#num_k().
  Configs.num_n: Configs#num_n().
  kernel.inner_kernel: kernel().inner_kernel().
  kernel.inner_kernel._add_ape: kernel().inner_kernel()._add_ape().
  Configs.dims: Configs#dims.
  TileSizes.tile_n: TileSizes#tile_n.
  kernel._dma_copy_out: kernel()._dma_copy_out().
  TileSizes.tile_m: TileSizes#tile_m.
  TileSizes.tile_k: TileSizes#tile_k.
  Dimensions.size_m: Dimensions#size_m.
  Dimensions.compress_ratio: Dimensions#compress_ratio.
  kernel.inner_kernel.matmul: kernel().inner_kernel().matmul().
  kernel.inner_kernel.matmul_ape_write_out: kernel().inner_kernel().matmul_ape_write_out().
  kernel.inner_kernel.matmul_write_out: kernel().inner_kernel().matmul_write_out().
  kernel.inner_kernel.matmul_ape_only: kernel().inner_kernel().matmul_ape_only().
  TileSizes: TileSizes#
  Dimensions: Dimensions#
  Dimensions.size_k: Dimensions#size_k.
  Dimensions.size_n: Dimensions#size_n.
  Configs: Configs#
  Configs.token_page_size: Configs#token_page_size.
  load_from_acc_ref: load_from_acc_ref().
  store_to_acc_ref: store_to_acc_ref().
  kernel.inner_kernel._matmul: kernel().inner_kernel()._matmul().
  _select_tile_k: _select_tile_k().
  kernel.inner_kernel.process._wait_for_buffer: kernel().inner_kernel().process()._wait_for_buffer().
  kernel.inner_kernel.process._wait_for_buffer._do_wait: kernel().inner_kernel().process()._wait_for_buffer()._do_wait().
  kernel._wait_epilogue: kernel()._wait_epilogue().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py)

## Classes
### <a id="Configs"></a>`Configs`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py:49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L49)
- doc: Configuration parameters for the projection and save state kernel.
- signature: `class Configs:`
- members:
  - <a id="Configs.num_k"></a>`num_k(self)` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L61)
  - <a id="Configs.num_m"></a>`num_m(self)` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L57)
  - <a id="Configs.num_n"></a>`num_n(self)` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L65)
  - <a id="Configs.dims"></a>`dims` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L53)
  - <a id="Configs.tile_sizes"></a>`tile_sizes` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L52)
  - <a id="Configs.token_page_size"></a>`token_page_size` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L54)
- uses (calls/refs, reference-scoped): [`tile_n`](proj_and_save_state.md#TileSizes.tile_n), [`tile_k`](proj_and_save_state.md#TileSizes.tile_k), [`tile_m`](proj_and_save_state.md#TileSizes.tile_m), [`size_m`](proj_and_save_state.md#Dimensions.size_m), [`Dimensions`](proj_and_save_state.md#Dimensions), [`TileSizes`](proj_and_save_state.md#TileSizes), [`size_k`](proj_and_save_state.md#Dimensions.size_k), [`size_n`](proj_and_save_state.md#Dimensions.size_n)
- used by: [`proj_and_save_state`](proj_and_save_state.md#proj_and_save_state), [`kernel`](proj_and_save_state.md#kernel), [`_add_ape`](proj_and_save_state.md#kernel.inner_kernel._add_ape), [`inner_kernel`](proj_and_save_state.md#kernel.inner_kernel), [`_dma_copy_out`](proj_and_save_state.md#kernel._dma_copy_out)

### <a id="Dimensions"></a>`Dimensions`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py:37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L37)
- doc: Dimensions of the input and output tensors.
- signature: `class Dimensions:`
- members:
  - <a id="Dimensions.compress_ratio"></a>`compress_ratio` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L45)
  - <a id="Dimensions.size_k"></a>`size_k` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L41)
  - <a id="Dimensions.size_m"></a>`size_m` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L40)
  - <a id="Dimensions.size_n"></a>`size_n` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L42)
- used by: [`proj_and_save_state`](proj_and_save_state.md#proj_and_save_state), [`num_m`](proj_and_save_state.md#Configs.num_m), [`num_k`](proj_and_save_state.md#Configs.num_k), [`num_n`](proj_and_save_state.md#Configs.num_n), [`_add_ape`](proj_and_save_state.md#kernel.inner_kernel._add_ape), [`inner_kernel`](proj_and_save_state.md#kernel.inner_kernel), [`dims`](proj_and_save_state.md#Configs.dims)

### <a id="TileSizes"></a>`TileSizes`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py:28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L28)
- doc: Tile sizes for Pallas kernel.
- signature: `class TileSizes:`
- members:
  - <a id="TileSizes.tile_k"></a>`tile_k` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L32)
  - <a id="TileSizes.tile_m"></a>`tile_m` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L31)
  - <a id="TileSizes.tile_n"></a>`tile_n` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L33)
- used by: [`proj_and_save_state`](proj_and_save_state.md#proj_and_save_state), [`kernel`](proj_and_save_state.md#kernel), [`num_m`](proj_and_save_state.md#Configs.num_m), [`tile_sizes`](proj_and_save_state.md#Configs.tile_sizes), [`num_k`](proj_and_save_state.md#Configs.num_k), [`num_n`](proj_and_save_state.md#Configs.num_n)

## Functions
- <a id="kernel.inner_kernel._add_ape"></a>`_add_ape()` — [`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L192)
- <a id="kernel._dma_copy_out"></a>`_dma_copy_out(n_idx_val, m_idx_val, buf_idx_val)` — [`L133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L133) — Copys one tile from accumulator to the KV cache.
- <a id="kernel.inner_kernel.process._wait_for_buffer._do_wait"></a>`_do_wait()` — [`L221`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L221)
- <a id="kernel.inner_kernel._matmul"></a>`_matmul()` — [`L181`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L181)
- <a id="_select_tile_k"></a>`_select_tile_k(size_k: int, cap: int = 3584, align: int = 128)` — [`L326`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L326) — Largest 128-aligned k tile that *divides* ``size_k``.
- <a id="kernel._wait_epilogue"></a>`_wait_epilogue(b=b, count=count)` — [`L322`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L322)
- <a id="kernel.inner_kernel.process._wait_for_buffer"></a>`_wait_for_buffer()` — [`L217`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L217)
- <a id="kernel.inner_kernel"></a>`inner_kernel(tiled_wgate_ref, tiled_hidden_states_ref, tiled_positions_ref)` — [`L166`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L166)
- <a id="kernel"></a>`kernel(slot_mapping, positions, hidden_states, wkv_wgate, ape, cache, _, acc_ref, sem_ref, write_counts_ref, *, cfgs: Configs)` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L104) — Inner kernel executing matmul, APE addition, and paged writes. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="load_from_acc_ref"></a>`load_from_acc_ref(ref, dtype=None)` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L69) — Loads data from VMEM accumulator with strided access, handling
- <a id="kernel.inner_kernel.matmul"></a>`matmul()` — [`L259`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L259)
- <a id="kernel.inner_kernel.matmul_ape_only"></a>`matmul_ape_only()` — [`L274`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L274)
- <a id="kernel.inner_kernel.matmul_ape_write_out"></a>`matmul_ape_write_out()` — [`L264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L264)
- <a id="kernel.inner_kernel.matmul_write_out"></a>`matmul_write_out()` — [`L269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L269)
- <a id="kernel.inner_kernel.process"></a>`process(copy_dma: bool, add_ape: bool)` — [`L214`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L214)
- <a id="proj_and_save_state"></a>`proj_and_save_state(hidden_states: jax.Array, wkv_wgate: jax.Array, ape: jax.Array, positions: jax.Array, slot_mapping: jax.Array, cache: jax.Array, compress_ratio: int, interpret: bool = False)` — [`L342`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L342) — Projects hidden states and saves them to the KV cache in HBM. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="store_to_acc_ref"></a>`store_to_acc_ref(ref, val, dtype=None)` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/proj_and_save_state.py#L88) — Stores data to VMEM accumulator with strided access, handling

