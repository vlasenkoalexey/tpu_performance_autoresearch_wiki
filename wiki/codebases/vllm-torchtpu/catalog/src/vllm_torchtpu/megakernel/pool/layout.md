---
title: 'Module: src/vllm_torchtpu/megakernel/pool/layout.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/layout.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.layout`/
symbols:
  PoolLayout.validate: PoolLayout#validate().
  LANES: LANES.
  PoolLayout: PoolLayout#
  PoolLayout.min_num_pages: PoolLayout#min_num_pages().
  PoolLayout.kv_page_shape: PoolLayout#kv_page_shape().
  PoolLayout._need: PoolLayout#_need().
  PoolLayout.qkv_per_rank: PoolLayout#qkv_per_rank().
  PoolLayout.slots_per_pool: PoolLayout#slots_per_pool.
  PoolLayout.gpr_conv_rows: PoolLayout#gpr_conv_rows().
  PoolLayout.rec_pages_per_slot: PoolLayout#rec_pages_per_slot.
  PoolLayout.conv_taps: PoolLayout#conv_taps.
  PoolLayout.rec_u32_rows: PoolLayout#rec_u32_rows().
  PoolLayout.conv_page_rows: PoolLayout#conv_page_rows().
  PoolLayout.pages_per_slot: PoolLayout#pages_per_slot().
  PoolLayout.num_pools: PoolLayout#num_pools.
  PoolLayout.KD: PoolLayout#KD.
  PoolLayout.page_base: PoolLayout#page_base().
  PoolLayout.from_cache_decls: PoolLayout#from_cache_decls().
  PoolLayout.page_size: PoolLayout#page_size.
  PoolLayout.VD: PoolLayout#VD.
  PoolLayout.hd: PoolLayout#hd.
  PoolLayout.has_recurrent: PoolLayout#has_recurrent().
  PoolLayout.vh_per_rank: PoolLayout#vh_per_rank().
  PoolLayout.conv_rows: PoolLayout#conv_rows().
  PoolLayout.num_recurrent_layers: PoolLayout#num_recurrent_layers().
  PoolLayout.ssm_u32_rows: PoolLayout#ssm_u32_rows().
  PoolLayout.reserved_pages: PoolLayout#reserved_pages().
  PoolLayout.page_bytes: PoolLayout#page_bytes().
  PoolLayout.gpr_conv_fits: PoolLayout#gpr_conv_fits().
  PoolLayout.kvh: PoolLayout#kvh.
  PoolLayout.page_dtype: PoolLayout#page_dtype.
  PoolLayout.conv_pages_per_slot: PoolLayout#conv_pages_per_slot.
  PoolLayout.conv_page: PoolLayout#conv_page().
  VALIDATED_REC_PAGES_PER_SLOT: VALIDATED_REC_PAGES_PER_SLOT.
  PoolLayout.kh: PoolLayout#kh.
  PoolLayout.vh: PoolLayout#vh.
  PoolLayout.conv_dtype: PoolLayout#conv_dtype.
  VALIDATED_CONV_PAGES_PER_SLOT: VALIDATED_CONV_PAGES_PER_SLOT.
  PoolLayout.rec_dtype: PoolLayout#rec_dtype.
  PoolLayout.recurrent_slots_per_pool: PoolLayout#recurrent_slots_per_pool().
  PoolLayout.page_rows: PoolLayout#page_rows().
  PoolLayout.kh_per_rank: PoolLayout#kh_per_rank().
  VALIDATED_HD: VALIDATED_HD.
  VALIDATED_PAGE_SIZE: VALIDATED_PAGE_SIZE.
  VALIDATED_KVH: VALIDATED_KVH.
  VALIDATED_CONV_TAPS: VALIDATED_CONV_TAPS.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/pool/layout.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py)

## Classes
### <a id="PoolLayout"></a>`PoolLayout`
- def: [`src/vllm_torchtpu/megakernel/pool/layout.py:84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L84) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- doc: Unified raw-pool layout: KV page packing plus recurrent checkpoint slots.
- signature: `class PoolLayout:`
- members:
  - <a id="PoolLayout.conv_page"></a>`conv_page(self)` — [`L119`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L119) — Index of the conv page inside a slot (after the recurrent pages).
  - <a id="PoolLayout.conv_page_rows"></a>`conv_page_rows(self)` — [`L185`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L185) — bf16 rows of `LANES` lanes in one conv page (`page_bytes // 256`). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.conv_rows"></a>`conv_rows(self, R: int)` — [`L221`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L221) — bf16 rows of `LANES` lanes of one sequence's per-rank conv window.
  - <a id="PoolLayout.from_cache_decls"></a>`from_cache_decls(cls, decls_or_kv: Sequence[KVCacheDecl | RecurrentCacheDecl | Any | None] | KVCacheDecl | Any, rec_decl: RecurrentCacheDecl | Any | None = None, *, num_pools: int | None = None, slots_per_pool: int | None = None, R: int | None = None)` — [`L335`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L335) — Construct a `PoolLayout` from per-layer `cache_decl()` descriptors.
  - <a id="PoolLayout.gpr_conv_fits"></a>`gpr_conv_fits(self, T: int, R: int)` — [`L201`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L201) — Whether the GPR conv window fits the K half of one conv page.
  - <a id="PoolLayout.gpr_conv_rows"></a>`gpr_conv_rows(self, T: int, R: int)` — [`L189`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L189) — `(rows, 4, page_size)` fp8 page rows of the in-kernel gather (GPR)
  - <a id="PoolLayout.has_recurrent"></a>`has_recurrent(self)` — [`L124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L124)
  - <a id="PoolLayout.kh_per_rank"></a>`kh_per_rank(self, R: int)` — [`L207`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L207)
  - <a id="PoolLayout.kv_page_shape"></a>`kv_page_shape(self)` — [`L165`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L165) — Shape of one pool page: `(2 * kvh, hd // 4, 4, page_size)`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.min_num_pages"></a>`min_num_pages(self, ex: ExecSpec)` — [`L152`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L152) — Pages needed for a disjoint test layout (reserved + KV + slots). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.num_recurrent_layers"></a>`num_recurrent_layers(self)` — [`L128`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L128) — Total recurrent layers across all pools (`num_pools * slots_per_pool`).
  - <a id="PoolLayout.page_base"></a>`page_base(self, slot: Any, sub: Any, ndim: int)` — [`L142`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L142) — First page of checkpoint `slot` for sub-layer `sub` (`ckpt_indices.ndim`).
  - <a id="PoolLayout.page_bytes"></a>`page_bytes(self)` — [`L170`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L170)
  - <a id="PoolLayout.page_rows"></a>`page_rows(self)` — [`L175`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L175) — Rows of one page viewed as `(rows, 4, page_size)` (`2 * kvh * hd // 4`).
  - <a id="PoolLayout.pages_per_slot"></a>`pages_per_slot(self)` — [`L114`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L114) — Pages per recurrent checkpoint slot (recurrent pages + conv pages). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.qkv_per_rank"></a>`qkv_per_rank(self, R: int)` — [`L213`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L213) — Conv channel count `2 * kh * KD + vh * VD` on one of `R` ranks. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.rec_u32_rows"></a>`rec_u32_rows(self)` — [`L180`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L180) — u32 rows of `LANES` lanes across the recurrent pages of one slot. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.recurrent_slots_per_pool"></a>`recurrent_slots_per_pool(self)` — [`L133`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L133) — Leading `ckpt_indices` / `read_offsets` dim (1 for KV-only pools).
  - <a id="PoolLayout.reserved_pages"></a>`reserved_pages(self)` — [`L138`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L138) — Null / dummy pages `[0, reserved_pages)` (at least page 0).
  - <a id="PoolLayout.ssm_u32_rows"></a>`ssm_u32_rows(self, R: int)` — [`L217`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L217) — u32 rows of one sequence's per-rank recurrent state.
  - <a id="PoolLayout.validate"></a>`validate(self, ex: ExecSpec | None = None)` — [`L226`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L226) — Raise `MegakernelConfigError` for layouts the pool kernels can't run. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.vh_per_rank"></a>`vh_per_rank(self, R: int)` — [`L210`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L210)
  - <a id="PoolLayout.KD"></a>`KD` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L103)
  - <a id="PoolLayout.VD"></a>`VD` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L104)
  - <a id="PoolLayout.conv_dtype"></a>`conv_dtype` — [`L109`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L109)
  - <a id="PoolLayout.conv_pages_per_slot"></a>`conv_pages_per_slot` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L110)
  - <a id="PoolLayout.conv_taps"></a>`conv_taps` — [`L108`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L108) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.hd"></a>`hd` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L96)
  - <a id="PoolLayout.kh"></a>`kh` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L101)
  - <a id="PoolLayout.kvh"></a>`kvh` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L97)
  - <a id="PoolLayout.num_pools"></a>`num_pools` — [`L93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L93)
  - <a id="PoolLayout.page_dtype"></a>`page_dtype` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L99)
  - <a id="PoolLayout.page_size"></a>`page_size` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L98)
  - <a id="PoolLayout.rec_dtype"></a>`rec_dtype` — [`L105`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L105)
  - <a id="PoolLayout.rec_pages_per_slot"></a>`rec_pages_per_slot` — [`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L106) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.slots_per_pool"></a>`slots_per_pool` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L94) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
  - <a id="PoolLayout.vh"></a>`vh` — [`L102`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L102)
- protocol/private: <a id="PoolLayout._need"></a>`_need`[`L235`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L235)
- uses (calls/refs, reference-scoped): [`derive_pool_layout`](derive.md#derive_pool_layout), [`cache_exec`](config.md#cache_exec), [`ExecSpec`](../exec_spec.md#ExecSpec), [`LANES`](layout.md#LANES), [`MegakernelConfigError`](../errors.md#MegakernelConfigError), [`BF16`](../ops.md#BF16), [`FP8`](../ops.md#FP8), [`NS`](../exec_spec.md#ExecSpec.NS), [`T`](../exec_spec.md#ExecSpec.T), [`KVCacheDecl`](../decls.md#KVCacheDecl), [`RecurrentCacheDecl`](../decls.md#RecurrentCacheDecl), [`page_size`](config.md#CacheExec.page_size), [`rup`](../ops.md#rup), [`GPR`](config.md#CacheExec.GPR), [`R`](../exec_spec.md#ExecSpec.R), [`ctx`](../exec_spec.md#ExecSpec.ctx), [`FUSED`](config.md#CacheExec.FUSED), [`VALIDATED_REC_PAGES_PER_SLOT`](layout.md#VALIDATED_REC_PAGES_PER_SLOT), [`VALIDATED_CONV_PAGES_PER_SLOT`](layout.md#VALIDATED_CONV_PAGES_PER_SLOT), [`VALIDATED_CONV_TAPS`](layout.md#VALIDATED_CONV_TAPS), [`VALIDATED_HD`](layout.md#VALIDATED_HD), [`VALIDATED_KVH`](layout.md#VALIDATED_KVH), [`VALIDATED_PAGE_SIZE`](layout.md#VALIDATED_PAGE_SIZE)
- used by: [`scatter_pool_states`](scatter.md#scatter_pool_states), [`derive_pool_layout`](derive.md#derive_pool_layout), [`gather_gdn_states`](gather.md#gather_gdn_states), [`pool_to_states`](pack.md#pool_to_states), [`states_to_pool`](pack.md#states_to_pool), [`make_pool_backend`](backend.md#make_pool_backend), [`pb_for`](scatter_ckpt.md#pb_for), [`can_pool_gather`](backend.md#can_pool_gather), [`allocate_test_layout`](pack.md#allocate_test_layout), [`prepare_ckpt`](scatter_ckpt.md#prepare_ckpt), [`check_ckpt_bounds`](backend.md#check_ckpt_bounds), [`conv_to_raw_page`](pack.md#conv_to_raw_page), [`raw_page_to_conv`](pack.md#raw_page_to_conv), [`ssm_to_raw_pages`](pack.md#ssm_to_raw_pages), [`raw_pages_to_ssm`](pack.md#raw_pages_to_ssm), [`page_base_for`](gather.md#gather_gdn_states._kernel.page_base_for), [`layout`](config.md#PoolBackend.layout), [`_DEFAULT_LAYOUT`](pack.md#_DEFAULT_LAYOUT), [`ckpt_pages_per_slot`](config.md#PoolBackend.ckpt_pages_per_slot), [`has_recurrent_pool`](config.md#PoolBackend.has_recurrent_pool), [`num_pools`](config.md#PoolBackend.num_pools), [`recurrent_slots_per_pool`](config.md#PoolBackend.recurrent_slots_per_pool), [`layout`](scatter_ctx.md#ScatterGeom.layout)

## Module values
- <a id="LANES"></a>`LANES` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L62) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="VALIDATED_CONV_PAGES_PER_SLOT"></a>`VALIDATED_CONV_PAGES_PER_SLOT` — [`L79`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L79)
- <a id="VALIDATED_CONV_TAPS"></a>`VALIDATED_CONV_TAPS` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L80)
- <a id="VALIDATED_HD"></a>`VALIDATED_HD` — [`L75`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L75)
- <a id="VALIDATED_KVH"></a>`VALIDATED_KVH` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L77)
- <a id="VALIDATED_PAGE_SIZE"></a>`VALIDATED_PAGE_SIZE` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L76)
- <a id="VALIDATED_REC_PAGES_PER_SLOT"></a>`VALIDATED_REC_PAGES_PER_SLOT` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L78)
- <a id="__all__"></a>`__all__` — [`L358`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/layout.py#L358)

