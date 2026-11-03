---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.compress_and_store.buffered_ref`/
symbols:
  create_allocs_and_specs: create_allocs_and_specs().
  _BufferedRef.cfgs: _BufferedRef#cfgs.
  OutputRef.copy_out: OutputRef#copy_out().
  OutputRef.wait_out: OutputRef#wait_out().
  _BufferedRef: _BufferedRef#
  CosSinRef.copy_in: CosSinRef#copy_in().
  PageBufferRef.copy_in: PageBufferRef#copy_in().
  OutputRef.copy_in: OutputRef#copy_in().
  OutputRef._write_nope: OutputRef#_write_nope().
  PageBufferRef.wait_in: PageBufferRef#wait_in().
  OutputRef.wait_in: OutputRef#wait_in().
  RoPEOutputRef.copy_in: RoPEOutputRef#copy_in().
  RoPEOutputRef.wait_in: RoPEOutputRef#wait_in().
  RoPEOutputRef.copy_out: RoPEOutputRef#copy_out().
  RoPEOutputRef.wait_out: RoPEOutputRef#wait_out().
  _BufferedRef.create: _BufferedRef#create().
  OutputRef._read_nope: OutputRef#_read_nope().
  OutputRef.write_loop: OutputRef#write_loop().
  OutputRef.wait_loop: OutputRef#wait_loop().
  RoPEOutputRef._read_rope: RoPEOutputRef#_read_rope().
  RoPEOutputRef._write_rope: RoPEOutputRef#_write_rope().
  CosSinRef: CosSinRef#
  PageBufferRef: PageBufferRef#
  OutputRef: OutputRef#
  RoPEOutputRef: RoPEOutputRef#
  OutputRef.loop_body: OutputRef#loop_body().
  CosSinRef.loop_body: CosSinRef#loop_body().
  CosSinRef.wait_in: CosSinRef#wait_in().
  OutputRef._wait_nope: OutputRef#_wait_nope().
  RoPEOutputRef.loop_body: RoPEOutputRef#loop_body().
  RoPEOutputRef._wait_rope: RoPEOutputRef#_wait_rope().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py)

## Classes
### <a id="CosSinRef"></a>`CosSinRef`  ·  implements/extends _BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py:61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L61)
- signature: `class CosSinRef(_BufferedRef):`
- members:
  - <a id="CosSinRef.copy_in"></a>`copy_in(self, src_ref, grid_indices)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L62)
  - <a id="CosSinRef.loop_body"></a>`loop_body(i)` — [`L76`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L76)
  - <a id="CosSinRef.wait_in"></a>`wait_in(self, src_ref, grid_indices)` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L87)
- uses (calls/refs, reference-scoped): [`dims`](config.md#Configs.dims), [`cfgs`](buffered_ref.md#_BufferedRef.cfgs), [`tile_sizes`](config.md#Configs.tile_sizes), [`tile_n`](config.md#TileSizes.tile_n), [`_BufferedRef`](buffered_ref.md#_BufferedRef), [`compress_ratio`](config.md#Dimensions.compress_ratio)
- used by: [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`_BufferedRef`](buffered_ref.md#_BufferedRef)

### <a id="OutputRef"></a>`OutputRef`  ·  implements/extends _BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py:150`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L150)
- signature: `class OutputRef(_BufferedRef):`
- members:
  - <a id="OutputRef.copy_in"></a>`copy_in(self, src_ref, grid_indices)` — [`L153`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L153)
  - <a id="OutputRef.copy_out"></a>`copy_out(self, dest_ref, grid_indices)` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L211) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="OutputRef.loop_body"></a>`loop_body(n)` — [`L171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L171)
  - <a id="OutputRef.wait_in"></a>`wait_in(self, src_ref, grid_indices)` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L185)
  - <a id="OutputRef.wait_loop"></a>`wait_loop(o)` — [`L307`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L307)
  - <a id="OutputRef.wait_out"></a>`wait_out(self, dest_ref, grid_indices)` — [`L265`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L265) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="OutputRef.write_loop"></a>`write_loop(o)` — [`L260`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L260)
- protocol/private: <a id="OutputRef._read_nope"></a>`_read_nope`[`L177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L177), <a id="OutputRef._wait_nope"></a>`_wait_nope`[`L204`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L204), <a id="OutputRef._write_nope"></a>`_write_nope`[`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L236)
- uses (calls/refs, reference-scoped): [`dims`](config.md#Configs.dims), [`Mode`](config.md#Mode), [`cfgs`](buffered_ref.md#_BufferedRef.cfgs), [`tile_sizes`](config.md#Configs.tile_sizes), [`tile_n`](config.md#TileSizes.tile_n), [`kv_block_size`](config.md#Configs.kv_block_size), [`mode`](config.md#Dimensions.mode), [`_BufferedRef`](buffered_ref.md#_BufferedRef), [`CSA_INDEXER`](config.md#Mode.CSA_INDEXER), [`physical_page_size`](config.md#Configs.physical_page_size), [`record_rows`](config.md#Configs.record_rows), [`seq_along_lane`](config.md#Dimensions.seq_along_lane), [`tokens_in_second_minor`](config.md#Configs.tokens_in_second_minor)
- used by: [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`_BufferedRef`](buffered_ref.md#_BufferedRef)

### <a id="PageBufferRef"></a>`PageBufferRef`  ·  implements/extends _BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py:98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L98)
- signature: `class PageBufferRef(_BufferedRef):`
- members:
  - <a id="PageBufferRef.copy_in"></a>`copy_in(self, src_ref, grid_indices)` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L102)
  - <a id="PageBufferRef.wait_in"></a>`wait_in(self, src_ref, grid_indices)` — [`L132`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L132)
- uses (calls/refs, reference-scoped): [`cfgs`](buffered_ref.md#_BufferedRef.cfgs), [`tile_sizes`](config.md#Configs.tile_sizes), [`tile_n`](config.md#TileSizes.tile_n), [`_BufferedRef`](buffered_ref.md#_BufferedRef), [`pages_to_buffer_per_token`](config.md#Configs.pages_to_buffer_per_token)
- used by: [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`_BufferedRef`](buffered_ref.md#_BufferedRef)

### <a id="RoPEOutputRef"></a>`RoPEOutputRef`  ·  implements/extends _BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py:317`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L317)
- signature: `class RoPEOutputRef(_BufferedRef):`
- members:
  - <a id="RoPEOutputRef.copy_in"></a>`copy_in(self, src_ref, grid_indices)` — [`L322`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L322)
  - <a id="RoPEOutputRef.copy_out"></a>`copy_out(self, dest_ref, grid_indices)` — [`L379`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L379)
  - <a id="RoPEOutputRef.loop_body"></a>`loop_body(n)` — [`L335`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L335)
  - <a id="RoPEOutputRef.wait_in"></a>`wait_in(self, src_ref, grid_indices)` — [`L352`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L352)
  - <a id="RoPEOutputRef.wait_out"></a>`wait_out(self, dest_ref, grid_indices)` — [`L408`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L408)
- protocol/private: <a id="RoPEOutputRef._read_rope"></a>`_read_rope`[`L342`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L342), <a id="RoPEOutputRef._wait_rope"></a>`_wait_rope`[`L372`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L372), <a id="RoPEOutputRef._write_rope"></a>`_write_rope`[`L400`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L400)
- uses (calls/refs, reference-scoped): [`cfgs`](buffered_ref.md#_BufferedRef.cfgs), [`tile_sizes`](config.md#Configs.tile_sizes), [`tile_n`](config.md#TileSizes.tile_n), [`_BufferedRef`](buffered_ref.md#_BufferedRef), [`rope_page_size`](config.md#Configs.rope_page_size)
- used by: [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`_BufferedRef`](buffered_ref.md#_BufferedRef)

### <a id="_BufferedRef"></a>`_BufferedRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py:29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L29)
- signature: `class _BufferedRef(pltpu.BufferedRef):`
- members:
  - <a id="_BufferedRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: jax.typing.DTypeLike, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool, cfgs: config.Configs)` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L33)
  - <a id="_BufferedRef.cfgs"></a>`cfgs` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L30) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- uses (calls/refs, reference-scoped): [`Configs`](config.md#Configs), [`CosSinRef`](buffered_ref.md#CosSinRef), [`OutputRef`](buffered_ref.md#OutputRef), [`PageBufferRef`](buffered_ref.md#PageBufferRef), [`RoPEOutputRef`](buffered_ref.md#RoPEOutputRef)
- used by: [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`copy_out`](buffered_ref.md#OutputRef.copy_out), [`wait_out`](buffered_ref.md#OutputRef.wait_out), [`copy_in`](buffered_ref.md#CosSinRef.copy_in), [`_write_nope`](buffered_ref.md#OutputRef._write_nope), [`copy_in`](buffered_ref.md#OutputRef.copy_in), [`copy_in`](buffered_ref.md#PageBufferRef.copy_in), [`copy_in`](buffered_ref.md#RoPEOutputRef.copy_in), [`copy_out`](buffered_ref.md#RoPEOutputRef.copy_out), [`wait_in`](buffered_ref.md#OutputRef.wait_in), [`wait_in`](buffered_ref.md#PageBufferRef.wait_in), [`wait_in`](buffered_ref.md#RoPEOutputRef.wait_in), [`wait_out`](buffered_ref.md#RoPEOutputRef.wait_out), [`_read_nope`](buffered_ref.md#OutputRef._read_nope), [`_read_rope`](buffered_ref.md#RoPEOutputRef._read_rope), [`_write_rope`](buffered_ref.md#RoPEOutputRef._write_rope), [`wait_loop`](buffered_ref.md#OutputRef.wait_loop), [`write_loop`](buffered_ref.md#OutputRef.write_loop), [`CosSinRef`](buffered_ref.md#CosSinRef), [`OutputRef`](buffered_ref.md#OutputRef), [`PageBufferRef`](buffered_ref.md#PageBufferRef), [`RoPEOutputRef`](buffered_ref.md#RoPEOutputRef)

## Functions
- <a id="create_allocs_and_specs"></a>`create_allocs_and_specs(cfgs: config.Configs, *, cache_ref, rope_cache_ref, state_cache_ref, cos_sin_cache_ref, positions_ref, token_pages_ref, kv_slot_mapping_ref, is_first_mask_ref, is_first_mask_rope_ref)` — [`L437`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/buffered_ref.py#L437) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)

