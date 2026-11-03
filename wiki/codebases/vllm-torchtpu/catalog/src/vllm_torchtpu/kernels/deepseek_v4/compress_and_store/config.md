---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.compress_and_store.config`/
symbols:
  Configs.dims: Configs#dims.
  Configs.make: Configs#make().
  Mode: Mode#
  Configs.tile_sizes: Configs#tile_sizes.
  TileSizes.tile_n: TileSizes#tile_n.
  Configs.kv_block_size: Configs#kv_block_size().
  physical_page_size: physical_page_size().
  LANE: LANE.
  Configs.record_bytes: Configs#record_bytes().
  Configs.records_t_shape: Configs#records_t_shape().
  select_mode: select_mode().
  Dimensions.mode: Dimensions#mode.
  Configs.state_rows_per_token: Configs#state_rows_per_token().
  Configs.window_bytes_shape: Configs#window_bytes_shape().
  state_rows_per_token: state_rows_per_token().
  state_host_page_size: state_host_page_size().
  Configs.window_shape: Configs#window_shape().
  SAL_SUBLANE_GROUPS: SAL_SUBLANE_GROUPS.
  Mode.CSA_INDEXER: Mode#CSA_INDEXER.
  Configs.nope_store_dim: Configs#nope_store_dim().
  Configs.head_tiles: Configs#head_tiles().
  Configs.row_size_bytes: Configs#row_size_bytes().
  _state_page_capacity: _state_page_capacity().
  _MODE_DEFAULTS._MODE_DEFAULTS: _MODE_DEFAULTS._MODE_DEFAULTS.
  Configs.window: Configs#window().
  state_block_size: state_block_size().
  Dimensions.has_rope_cache: Dimensions#has_rope_cache.
  Configs.field_rows: Configs#field_rows().
  Configs._tile_n: Configs#_tile_n().
  Configs.page_buffer_shape: Configs#page_buffer_shape().
  Configs.rope_output_shape: Configs#rope_output_shape().
  SAL_PAGE_SIZE: SAL_PAGE_SIZE.
  Configs.last_dim_size: Configs#last_dim_size().
  Configs.state_width: Configs#state_width().
  Configs.record_rows: Configs#record_rows().
  Configs.physical_page_size: Configs#physical_page_size().
  Configs.rope_page_size: Configs#rope_page_size().
  last_dim_size: last_dim_size().
  row_size_bytes: row_size_bytes().
  Dimensions.head_dim: Dimensions#head_dim.
  Dimensions.seq_along_lane: Dimensions#seq_along_lane.
  Configs.cache_last_dims: Configs#cache_last_dims().
  Configs.state_physical_page_size: Configs#state_physical_page_size().
  Configs.pages_to_buffer_per_token: Configs#pages_to_buffer_per_token().
  Configs.kv_stride: Configs#kv_stride().
  Configs.output_shape: Configs#output_shape().
  Configs.cos_sin_shape: Configs#cos_sin_shape().
  Mode.CSA: Mode#CSA.
  Configs: Configs#
  Configs.tokens_in_second_minor: Configs#tokens_in_second_minor().
  Dimensions.has_rope: Dimensions#has_rope().
  Configs.nope_dim: Configs#nope_dim().
  Configs.rope_cache_shape: Configs#rope_cache_shape().
  Dimensions.rope_head_dim: Dimensions#rope_head_dim.
  Configs.half_rope: Configs#half_rope().
  Configs.state_page_capacity: Configs#state_page_capacity().
  Configs.state_block_size: Configs#state_block_size().
  Configs.hbm_pack: Configs#hbm_pack().
  SLOT_PACK: SLOT_PACK.
  Configs.overlap_factor: Configs#overlap_factor().
  Dimensions.is_quantized: Dimensions#is_quantized().
  Dimensions.size_n: Dimensions#size_n.
  Configs.cache_shape: Configs#cache_shape().
  Configs.state_cache_shape: Configs#state_cache_shape().
  check_seq_along_lane_page_size: check_seq_along_lane_page_size().
  Dimensions.nope_dtype: Dimensions#nope_dtype().
  Mode.HCA: Mode#HCA.
  Dimensions.quant_block: Dimensions#quant_block.
  Dimensions.overlap: Dimensions#overlap.
  Configs.rope_slot: Configs#rope_slot().
  N_FIELDS: N_FIELDS.
  FP32_BYTES: FP32_BYTES.
  Dimensions.rope_dtype: Dimensions#rope_dtype().
  state_width: state_width().
  TileSizes: TileSizes#
  Dimensions: Dimensions#
  Dimensions.compress_ratio: Dimensions#compress_ratio.
  Dimensions.physical_page_size: Dimensions#physical_page_size.
  Dimensions.state_physical_page_size: Dimensions#state_physical_page_size.
  Dimensions.state_block_size: Dimensions#state_block_size.
  Dimensions.rms_eps: Dimensions#rms_eps.
  CSA_COMPRESS_RATIO: CSA_COMPRESS_RATIO.
  Dimensions.cos_sin_dtype: Dimensions#cos_sin_dtype.
  Dimensions.rope_width: Dimensions#rope_width.
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py)

## Classes
### <a id="Configs"></a>`Configs`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py:287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L287) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- doc: Configuration for the kernel.
- signature: `class Configs:`
- members:
  - <a id="Configs.cache_last_dims"></a>`cache_last_dims(self)` — [`L420`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L420)
  - <a id="Configs.cache_shape"></a>`cache_shape(self, num_pages: int)` — [`L554`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L554) — Shape of the global HBM KV cache, as uint8 slabs.
  - <a id="Configs.cos_sin_shape"></a>`cos_sin_shape(self)` — [`L550`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L550) — cos/sin VMEM block: (tile, rope_head_dim).
  - <a id="Configs.field_rows"></a>`field_rows(self)` — [`L457`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L457) — Number of physical HBM rows spanned by one field during gather. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.half_rope"></a>`half_rope(self)` — [`L380`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L380) — cos/sin split point (half the rope dim).
  - <a id="Configs.hbm_pack"></a>`hbm_pack(self)` — [`L410`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L410) — Sub-slots physically packed per slot row, <= SLOT_PACK.
  - <a id="Configs.head_tiles"></a>`head_tiles(self)` — [`L355`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L355) — head_dim split into LANE-wide compute tiles (old: slots_per_part). — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.kv_block_size"></a>`kv_block_size(self)` — [`L473`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L473) — Number of compressed KV tokens per page. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.kv_stride"></a>`kv_stride(self)` — [`L431`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L431) — Token stride in logical slot units.
  - <a id="Configs.last_dim_size"></a>`last_dim_size(self)` — [`L415`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L415) — Size of the last HBM cache dimension in bytes. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.make"></a>`make(cls, mode: Mode, *, size_n, physical_page_size, state_block_size, state_physical_page_size=None, rms_eps=0.000001, tile_n=4, **overrides)` — [`L295`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L295) — Build a config for `mode`; `overrides` replace per-mode defaults. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.nope_dim"></a>`nope_dim(self)` — [`L366`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L366) — Width of the non-rope (nope) part of a head.
  - <a id="Configs.nope_store_dim"></a>`nope_store_dim(self)` — [`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L371) — Dimension of the nope storage (contains rope if no separate rope cache). — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.output_shape"></a>`output_shape(self)` — [`L517`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L517) — Packed output tile / VMEM block: (tile, record_rows) + cache_last_dims.
  - <a id="Configs.overlap_factor"></a>`overlap_factor(self)` — [`L345`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L345) — State copies kept per step: 1, or 2 when windows overlap (prev+curr).
  - <a id="Configs.page_buffer_shape"></a>`page_buffer_shape(self)` — [`L533`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L533) — Page-buffer VMEM block: (tile, pages, state page rows) + cache_last_dims.
  - <a id="Configs.pages_to_buffer_per_token"></a>`pages_to_buffer_per_token(self)` — [`L486`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L486) — Pages that must be resident to cover one token's window (+1 guard). — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.physical_page_size"></a>`physical_page_size(self)` — [`L439`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L439) — Number of physical HBM rows per page of the compressed-KV array.
  - <a id="Configs.record_bytes"></a>`record_bytes(self)` — [`L391`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L391) — Bytes in one packed output record (old: total_bytes_out). — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.record_rows"></a>`record_rows(self)` — [`L399`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L399) — Packed physical rows per output record. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.records_t_shape"></a>`records_t_shape(self)` — [`L521`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L521) — SEQ_ALONG_LANE: VMEM staging of every token's record, as cache lanes. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.rope_cache_shape"></a>`rope_cache_shape(self, num_pages: int)` — [`L566`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L566) — Shape of the global HBM RoPE cache, as uint8 slabs.
  - <a id="Configs.rope_output_shape"></a>`rope_output_shape(self)` — [`L545`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L545) — RoPE output VMEM block: (tile, 4, lane).
  - <a id="Configs.rope_page_size"></a>`rope_page_size(self)` — [`L481`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L481) — Number of physical HBM rows per page in RoPE cache.
  - <a id="Configs.rope_slot"></a>`rope_slot(self)` — [`L385`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L385) — Head-tile holding the rope channels (the last one).
  - <a id="Configs.row_size_bytes"></a>`row_size_bytes(self)` — [`L405`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L405) — Size of one physical HBM row in bytes. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.state_block_size"></a>`state_block_size(self)` — [`L468`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L468) — Number of state tokens per page of the state array.
  - <a id="Configs.state_cache_shape"></a>`state_cache_shape(self, num_pages: int)` — [`L562`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L562) — Shape of the global HBM array hosting the f32 compressor state.
  - <a id="Configs.state_page_capacity"></a>`state_page_capacity(self)` — [`L463`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L463) — Number of token states one page of the state array physically holds.
  - <a id="Configs.state_physical_page_size"></a>`state_physical_page_size(self)` — [`L444`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L444) — Number of physical HBM rows per page of the *state* array.
  - <a id="Configs.state_rows_per_token"></a>`state_rows_per_token(self)` — [`L449`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L449) — Number of physical HBM rows occupied by one token's full state — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.state_width"></a>`state_width(self)` — [`L350`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L350) — Width of one stored field (head_dim, doubled when overlapping).
  - <a id="Configs.tokens_in_second_minor"></a>`tokens_in_second_minor(self)` — [`L425`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L425) — Divisor to map wrapper row offset to new physical row offset. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.window"></a>`window(self)` — [`L360`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L360) — Timesteps compressed together (x overlap_factor when overlapping). — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.window_bytes_shape"></a>`window_bytes_shape(self)` — [`L499`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L499) — uint8 view of the window scratch; each f32 lane -> FP32_BYTES rows.
  - <a id="Configs.window_shape"></a>`window_shape(self)` — [`L495`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L495) — f32 window scratch: (fields, tile, window, head_tiles, lane). — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.dims"></a>`dims` — [`L291`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L291) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Configs.tile_sizes"></a>`tile_sizes` — [`L290`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L290) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- protocol/private: <a id="Configs._tile_n"></a>`_tile_n`[`L492`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L492)
- uses (calls/refs, reference-scoped): [`Mode`](config.md#Mode), [`tile_n`](config.md#TileSizes.tile_n), [`LANE`](config.md#LANE), [`mode`](config.md#Dimensions.mode), [`state_rows_per_token`](config.md#state_rows_per_token), [`CSA_INDEXER`](config.md#Mode.CSA_INDEXER), [`SAL_SUBLANE_GROUPS`](config.md#SAL_SUBLANE_GROUPS), [`_MODE_DEFAULTS`](config.md#_MODE_DEFAULTS._MODE_DEFAULTS), [`has_rope_cache`](config.md#Dimensions.has_rope_cache), [`SAL_PAGE_SIZE`](config.md#SAL_PAGE_SIZE), [`last_dim_size`](config.md#last_dim_size), [`row_size_bytes`](config.md#row_size_bytes), [`head_dim`](config.md#Dimensions.head_dim), [`seq_along_lane`](config.md#Dimensions.seq_along_lane), [`rope_head_dim`](config.md#Dimensions.rope_head_dim), [`SLOT_PACK`](config.md#SLOT_PACK), [`is_quantized`](config.md#Dimensions.is_quantized), [`size_n`](config.md#Dimensions.size_n), [`HCA`](config.md#Mode.HCA), [`overlap`](config.md#Dimensions.overlap), [`FP32_BYTES`](config.md#FP32_BYTES), [`N_FIELDS`](config.md#N_FIELDS), [`Dimensions`](config.md#Dimensions), [`TileSizes`](config.md#TileSizes), [`compress_ratio`](config.md#Dimensions.compress_ratio), [`physical_page_size`](config.md#Dimensions.physical_page_size), [`rms_eps`](config.md#Dimensions.rms_eps), [`state_block_size`](config.md#Dimensions.state_block_size), [`state_physical_page_size`](config.md#Dimensions.state_physical_page_size), [`state_width`](config.md#state_width)
- used by: [`inner_kernel`](kernel.md#inner_kernel), [`compress_norm_rope_store`](kernel.md#compress_norm_rope_store), [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`kernel_fn`](kernel.md#kernel_fn), [`cfgs`](buffered_ref.md#_BufferedRef.cfgs), [`derive_metadata`](compressor_v1.md#derive_metadata), [`copy_out`](buffered_ref.md#OutputRef.copy_out), [`wait_out`](buffered_ref.md#OutputRef.wait_out), [`copy_in`](buffered_ref.md#CosSinRef.copy_in), [`_write_nope`](buffered_ref.md#OutputRef._write_nope), [`copy_in`](buffered_ref.md#OutputRef.copy_in), [`copy_in`](buffered_ref.md#PageBufferRef.copy_in), [`copy_in`](buffered_ref.md#RoPEOutputRef.copy_in), [`copy_out`](buffered_ref.md#RoPEOutputRef.copy_out), [`wait_in`](buffered_ref.md#OutputRef.wait_in), [`wait_in`](buffered_ref.md#PageBufferRef.wait_in), [`wait_in`](buffered_ref.md#RoPEOutputRef.wait_in), [`wait_out`](buffered_ref.md#RoPEOutputRef.wait_out), [`create`](buffered_ref.md#_BufferedRef.create), [`_read_nope`](buffered_ref.md#OutputRef._read_nope), [`_read_rope`](buffered_ref.md#RoPEOutputRef._read_rope), [`_write_rope`](buffered_ref.md#RoPEOutputRef._write_rope), [`wait_loop`](buffered_ref.md#OutputRef.wait_loop), [`write_loop`](buffered_ref.md#OutputRef.write_loop)

### <a id="Dimensions"></a>`Dimensions`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py:247`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L247)
- doc: True inputs only. Anything derivable is a property below.
- signature: `class Dimensions:`
- members:
  - <a id="Dimensions.has_rope"></a>`has_rope(self)` — [`L273`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L273) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Dimensions.is_quantized"></a>`is_quantized(self)` — [`L269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L269)
  - <a id="Dimensions.nope_dtype"></a>`nope_dtype(self)` — [`L277`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L277)
  - <a id="Dimensions.rope_dtype"></a>`rope_dtype(self)` — [`L281`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L281)
  - <a id="Dimensions.compress_ratio"></a>`compress_ratio` — [`L254`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L254)
  - <a id="Dimensions.cos_sin_dtype"></a>`cos_sin_dtype` — [`L265`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L265)
  - <a id="Dimensions.has_rope_cache"></a>`has_rope_cache` — [`L260`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L260) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Dimensions.head_dim"></a>`head_dim` — [`L252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L252)
  - <a id="Dimensions.mode"></a>`mode` — [`L250`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L250) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Dimensions.overlap"></a>`overlap` — [`L259`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L259)
  - <a id="Dimensions.physical_page_size"></a>`physical_page_size` — [`L255`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L255)
  - <a id="Dimensions.quant_block"></a>`quant_block` — [`L258`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L258)
  - <a id="Dimensions.rms_eps"></a>`rms_eps` — [`L261`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L261)
  - <a id="Dimensions.rope_head_dim"></a>`rope_head_dim` — [`L253`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L253)
  - <a id="Dimensions.rope_width"></a>`rope_width` — [`L266`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L266)
  - <a id="Dimensions.seq_along_lane"></a>`seq_along_lane` — [`L263`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L263) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Dimensions.size_n"></a>`size_n` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L251)
  - <a id="Dimensions.state_block_size"></a>`state_block_size` — [`L257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L257)
  - <a id="Dimensions.state_physical_page_size"></a>`state_physical_page_size` — [`L256`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L256)
- uses (calls/refs, reference-scoped): [`Mode`](config.md#Mode)
- used by: [`inner_kernel`](kernel.md#inner_kernel), [`dims`](config.md#Configs.dims), [`compress_norm_rope_store`](kernel.md#compress_norm_rope_store), [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`make`](config.md#Configs.make), [`kernel_fn`](kernel.md#kernel_fn), [`derive_metadata`](compressor_v1.md#derive_metadata), [`copy_out`](buffered_ref.md#OutputRef.copy_out), [`wait_out`](buffered_ref.md#OutputRef.wait_out), [`kv_block_size`](config.md#Configs.kv_block_size), [`record_bytes`](config.md#Configs.record_bytes), [`records_t_shape`](config.md#Configs.records_t_shape), [`state_rows_per_token`](config.md#Configs.state_rows_per_token), [`nope_store_dim`](config.md#Configs.nope_store_dim), [`copy_in`](buffered_ref.md#CosSinRef.copy_in), [`head_tiles`](config.md#Configs.head_tiles), [`row_size_bytes`](config.md#Configs.row_size_bytes), [`window`](config.md#Configs.window), [`field_rows`](config.md#Configs.field_rows), [`rope_output_shape`](config.md#Configs.rope_output_shape), [`last_dim_size`](config.md#Configs.last_dim_size), [`physical_page_size`](config.md#Configs.physical_page_size), [`state_width`](config.md#Configs.state_width), [`state_physical_page_size`](config.md#Configs.state_physical_page_size), [`cos_sin_shape`](config.md#Configs.cos_sin_shape), [`nope_dim`](config.md#Configs.nope_dim), [`rope_cache_shape`](config.md#Configs.rope_cache_shape), [`half_rope`](config.md#Configs.half_rope), [`state_block_size`](config.md#Configs.state_block_size), [`overlap_factor`](config.md#Configs.overlap_factor)

### <a id="Mode"></a>`Mode`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py:66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L66) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- signature: `class Mode(enum.Enum):`
- members:
  - <a id="Mode.CSA"></a>`CSA` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L68) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Mode.CSA_INDEXER"></a>`CSA_INDEXER` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L69) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="Mode.HCA"></a>`HCA` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L67)
- used by: [`inner_kernel`](kernel.md#inner_kernel), [`compress_norm_rope_store`](kernel.md#compress_norm_rope_store), [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`make`](config.md#Configs.make), [`copy_out`](buffered_ref.md#OutputRef.copy_out), [`wait_out`](buffered_ref.md#OutputRef.wait_out), [`physical_page_size`](config.md#physical_page_size), [`mode`](config.md#Dimensions.mode), [`select_mode`](config.md#select_mode), [`state_rows_per_token`](config.md#state_rows_per_token), [`state_host_page_size`](config.md#state_host_page_size), [`_MODE_DEFAULTS`](config.md#_MODE_DEFAULTS._MODE_DEFAULTS), [`_state_page_capacity`](config.md#_state_page_capacity), [`state_block_size`](config.md#state_block_size), [`last_dim_size`](config.md#last_dim_size), [`row_size_bytes`](config.md#row_size_bytes), [`_select_mode`](kernel.md#_select_mode)

### <a id="TileSizes"></a>`TileSizes`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py:239`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L239)
- doc: Tile sizes for the kernel.
- signature: `class TileSizes:`
- members:
  - <a id="TileSizes.tile_n"></a>`tile_n` — [`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L242) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- used by: [`inner_kernel`](kernel.md#inner_kernel), [`compress_norm_rope_store`](kernel.md#compress_norm_rope_store), [`create_allocs_and_specs`](buffered_ref.md#create_allocs_and_specs), [`make`](config.md#Configs.make), [`kernel_fn`](kernel.md#kernel_fn), [`copy_out`](buffered_ref.md#OutputRef.copy_out), [`tile_sizes`](config.md#Configs.tile_sizes), [`wait_out`](buffered_ref.md#OutputRef.wait_out), [`copy_in`](buffered_ref.md#CosSinRef.copy_in), [`_tile_n`](config.md#Configs._tile_n), [`copy_in`](buffered_ref.md#OutputRef.copy_in), [`copy_in`](buffered_ref.md#PageBufferRef.copy_in), [`copy_in`](buffered_ref.md#RoPEOutputRef.copy_in), [`copy_out`](buffered_ref.md#RoPEOutputRef.copy_out), [`wait_in`](buffered_ref.md#OutputRef.wait_in), [`wait_in`](buffered_ref.md#PageBufferRef.wait_in), [`wait_in`](buffered_ref.md#RoPEOutputRef.wait_in), [`wait_out`](buffered_ref.md#RoPEOutputRef.wait_out)

## Functions
- <a id="_state_page_capacity"></a>`_state_page_capacity(mode: Mode, kv_cache_block_size: int, compress_ratio: int | None = None, head_dim: int | None = None, indexer_seq_along_lane: bool = False)` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L185) — Token states one page of `mode`'s host array physically holds. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="check_seq_along_lane_page_size"></a>`check_seq_along_lane_page_size(storage_block_size: int)` — [`L107`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L107) — Raises unless `storage_block_size` is exactly `SAL_PAGE_SIZE`. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="last_dim_size"></a>`last_dim_size(mode: Mode)` — [`L163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L163) — Size of the last HBM cache dimension in bytes.
- <a id="physical_page_size"></a>`physical_page_size(mode: Mode, kv_cache_block_size: int, compress_ratio: int, seq_along_lane: bool = False)` — [`L118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L118) — Rows per page of the uint8 cache array allocated for `mode`. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="row_size_bytes"></a>`row_size_bytes(mode: Mode)` — [`L168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L168) — Size of one physical HBM row in bytes.
- <a id="select_mode"></a>`select_mode(head_dim: int, overlap: bool)` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L100) — Picks the storage mode from the compressor's head_dim / overlap flag. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="state_block_size"></a>`state_block_size(mode: Mode, kv_cache_block_size: int, compress_ratio: int | None = None, head_dim: int | None = None, indexer_seq_along_lane: bool = False)` — [`L204`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L204) — Token states vLLM should page `mode`'s state cache at. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="state_host_page_size"></a>`state_host_page_size(mode: Mode, kv_cache_block_size: int, compress_ratio: int, seq_along_lane: bool = False)` — [`L151`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L151) — Rows per page of the array that *hosts* ``mode``'s f32 compressor state. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="state_rows_per_token"></a>`state_rows_per_token(mode: Mode, head_dim: int, overlap: bool)` — [`L179`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L179) — Physical HBM rows one token's full state (kv + score) occupies. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="state_width"></a>`state_width(head_dim: int, overlap: bool)` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L173) — Width of one stored field: head_dim, doubled when windows overlap.

## Module values
- <a id="CSA_COMPRESS_RATIO"></a>`CSA_COMPRESS_RATIO` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L59)
- <a id="FP32_BYTES"></a>`FP32_BYTES` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L58)
- <a id="LANE"></a>`LANE` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L55) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="N_FIELDS"></a>`N_FIELDS` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L57)
- <a id="SAL_PAGE_SIZE"></a>`SAL_PAGE_SIZE` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L62) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="SAL_SUBLANE_GROUPS"></a>`SAL_SUBLANE_GROUPS` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L63) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="SLOT_PACK"></a>`SLOT_PACK` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L56)
- <a id="_MODE_DEFAULTS._MODE_DEFAULTS"></a>`_MODE_DEFAULTS` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store/config.py#L72) — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)

