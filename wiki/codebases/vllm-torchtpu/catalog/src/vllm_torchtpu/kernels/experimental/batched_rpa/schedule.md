---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.schedule`/
symbols:
  BaseMetadataComputer.k_loop: BaseMetadataComputer#k_loop().
  _mask_out_steps: _mask_out_steps().
  _compute_waits.body: _compute_waits().body().
  BaseMetadataComputer.fill_dma_kv_new: BaseMetadataComputer#fill_dma_kv_new().
  RpaSchedule.create_shape_dtype: RpaSchedule#create_shape_dtype().
  BaseMetadataComputer.q_loop: BaseMetadataComputer#q_loop().
  BaseMetadataComputer.get_rpa_schedule: BaseMetadataComputer#get_rpa_schedule().
  generate_rpa_metadata: generate_rpa_metadata().
  BaseMetadataComputer.seq_loop: BaseMetadataComputer#seq_loop().
  rpa_metadata_schedule_kernel: rpa_metadata_schedule_kernel().
  RpaSchedule: RpaSchedule#
  SmemWrapper: SmemWrapper#
  FieldOffset: FieldOffset#
  BaseMetadataComputer.flush_carry: BaseMetadataComputer#flush_carry().
  RpaSchedule.dma_kv_cache: RpaSchedule#dma_kv_cache.
  flush_to_hbm: flush_to_hbm().
  BaseMetadataComputer.advance_carry: BaseMetadataComputer#advance_carry().
  BaseMetadataComputer.page_indices_offset: BaseMetadataComputer#page_indices_offset().
  _compute_waits: _compute_waits().
  LoopCarry: LoopCarry#
  BaseMetadataComputer.compute: BaseMetadataComputer#compute().
  BaseMetadataComputer.cfgs: BaseMetadataComputer#cfgs.
  DmaNew: DmaNew#
  DmaNew.set_flags: DmaNew#set_flags().
  RpaSchedule.is_last_k: RpaSchedule#is_last_k.
  _write_schedule_to_hbm: _write_schedule_to_hbm().
  BaseMetadataComputer.wait_page_window: BaseMetadataComputer#wait_page_window().
  RpaSchedule.dma_q: RpaSchedule#dma_q.
  BaseMetadataComputer: BaseMetadataComputer#
  BaseMetadataComputer.page_indices_ref: BaseMetadataComputer#page_indices_ref.
  BaseMetadataComputer.start_page_window: BaseMetadataComputer#start_page_window().
  DmaNew.fetch_val: DmaNew#fetch_val().
  DmaNew.wb_val: DmaNew#wb_val().
  BaseMetadataComputer.page_window_idx: BaseMetadataComputer#page_window_idx().
  DmaNew.fetch_hbm: DmaNew#fetch_hbm.
  DmaNew.fetch_vmem: DmaNew#fetch_vmem.
  DmaNew.wb_hbm: DmaNew#wb_hbm.
  DmaNew.num_fields: DmaNew#num_fields().
  SmemArrayOfStructs.__getitem__: SmemArrayOfStructs#__getitem__().
  RpaSchedule.s_idx: RpaSchedule#s_idx.
  RpaSchedule.k_idx: RpaSchedule#k_idx.
  RpaSchedule.dma_kv_new: RpaSchedule#dma_kv_new.
  BaseMetadataComputer.start_window_copy: BaseMetadataComputer#start_window_copy().
  SmemWrapper._get_pos: SmemWrapper#_get_pos().
  BaseMetadataComputer.enter_window: BaseMetadataComputer#enter_window().
  SmemWrapper.create_shape_dtype: SmemWrapper#create_shape_dtype().
  RpaSchedule.q_idx: RpaSchedule#q_idx.
  RpaSchedule.do_writeback: RpaSchedule#do_writeback.
  SmemArrayOfStructs._get_pos: SmemArrayOfStructs#_get_pos().
  BaseMetadataComputer.__init__: BaseMetadataComputer#__init__().
  DmaNew.wb_vmem: DmaNew#wb_vmem.
  SeqAlongLaneDmaNew: SeqAlongLaneDmaNew#
  SeqAlongLaneDmaNew._flags: SeqAlongLaneDmaNew#_flags.
  HeadAlongSublaneDmaNew._flags: HeadAlongSublaneDmaNew#_flags.
  SmemWrapper.__getitem__: SmemWrapper#__getitem__().
  SmemWrapper.__setitem__: SmemWrapper#__setitem__().
  flush_to_hbm.body: flush_to_hbm().body().
  LoopCarry.count: LoopCarry#count.
  SmemArrayOfStructs: SmemArrayOfStructs#
  RpaSchedule.total_wait_kv_in: RpaSchedule#total_wait_kv_in.
  RpaSchedule.total_wait_kv_out: RpaSchedule#total_wait_kv_out.
  RpaSchedule.total_wait_q_in: RpaSchedule#total_wait_q_in.
  RpaSchedule.total_wait_o_out: RpaSchedule#total_wait_o_out.
  RpaSchedule.total_wait_lse_out: RpaSchedule#total_wait_lse_out.
  RpaSchedule.cfgs: RpaSchedule#cfgs.
  RpaSchedule.get_dma_q: RpaSchedule#get_dma_q().
  HeadAlongSublaneDmaNew: HeadAlongSublaneDmaNew#
  SmemArrayOfStructs.struct_cls: SmemArrayOfStructs#struct_cls.
  RpaSchedule.get_dma_kv_cache: RpaSchedule#get_dma_kv_cache().
  RpaSchedule.in_specs: RpaSchedule#in_specs().
  SmemWrapper.data: SmemWrapper#data.
  LoopCarry.hbm_offset: LoopCarry#hbm_offset.
  BaseMetadataComputer.schedule: BaseMetadataComputer#schedule.
  FieldOffset.__get__: FieldOffset#__get__().
  DmaNew._flags: DmaNew#_flags.
  SeqAlongLaneDmaNew.fetch_hbm: SeqAlongLaneDmaNew#fetch_hbm.
  SeqAlongLaneDmaNew.fetch_vmem: SeqAlongLaneDmaNew#fetch_vmem.
  SeqAlongLaneDmaNew.wb_hbm: SeqAlongLaneDmaNew#wb_hbm.
  SeqAlongLaneDmaNew.wb_vmem: SeqAlongLaneDmaNew#wb_vmem.
  SeqAlongLaneDmaNew.fetch_val: SeqAlongLaneDmaNew#fetch_val().
  SeqAlongLaneDmaNew.wb_val: SeqAlongLaneDmaNew#wb_val().
  SeqAlongLaneDmaNew.set_flags: SeqAlongLaneDmaNew#set_flags().
  HeadAlongSublaneDmaNew.wb_hbm: HeadAlongSublaneDmaNew#wb_hbm.
  HeadAlongSublaneDmaNew.fetch_hbm: HeadAlongSublaneDmaNew#fetch_hbm.
  HeadAlongSublaneDmaNew.fetch_vmem: HeadAlongSublaneDmaNew#fetch_vmem.
  HeadAlongSublaneDmaNew.wb_vmem: HeadAlongSublaneDmaNew#wb_vmem.
  HeadAlongSublaneDmaNew.fetch_val: HeadAlongSublaneDmaNew#fetch_val().
  HeadAlongSublaneDmaNew.wb_val: HeadAlongSublaneDmaNew#wb_val().
  HeadAlongSublaneDmaNew.set_flags: HeadAlongSublaneDmaNew#set_flags().
  SmemWrapper.shape: SmemWrapper#shape.
  RpaSchedule.actual_steps: RpaSchedule#actual_steps.
  RpaSchedule.scratch_shapes: RpaSchedule#scratch_shapes().
  BaseMetadataComputer.extra_refs: BaseMetadataComputer#extra_refs.
  BaseMetadataComputer.page_indices_sem: BaseMetadataComputer#page_indices_sem.
  FieldOffset.offset: FieldOffset#offset.
  SmemArrayOfStructs.struct_size: SmemArrayOfStructs#struct_size.
  SmemArrayOfStructs.create_shape_dtype: SmemArrayOfStructs#create_shape_dtype().
  RpaSchedule.wrapper: RpaSchedule#wrapper().
  RpaSchedule.out_specs: RpaSchedule#out_specs().
  BaseMetadataComputer.schedule_hbm_ref: BaseMetadataComputer#schedule_hbm_ref.
  BaseMetadataComputer.dma_sem: BaseMetadataComputer#dma_sem.
  BaseMetadataComputer.page_indices_hbm_ref: BaseMetadataComputer#page_indices_hbm_ref.
  FieldOffset.__init__: FieldOffset#__init__().
  FieldOffset.__isabstractmethod__: FieldOffset#__isabstractmethod__.
  DmaNew.data: DmaNew#data.
  DmaNew.pos: DmaNew#pos.
  SeqAlongLaneDmaNew.num_fields: SeqAlongLaneDmaNew#num_fields().
  HeadAlongSublaneDmaNew.num_fields: HeadAlongSublaneDmaNew#num_fields().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py)

## Classes
### <a id="BaseMetadataComputer"></a>`BaseMetadataComputer`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:507`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L507)
- doc: Base metadata scheduler computing seq -&gt; q -&gt; k loops.
- signature: `class BaseMetadataComputer:`
- members:
  - <a id="BaseMetadataComputer.advance_carry"></a>`advance_carry(self, carry: LoopCarry)` — [`L721`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L721)
  - <a id="BaseMetadataComputer.compute"></a>`compute(self, cu_q_lens_ref: jax.Ref, q_offsets_ref: jax.Ref, kv_cache_lens_ref: jax.Ref, kv_new_lens_ref: jax.Ref, distribution_ref: jax.Ref)` — [`L834`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L834) — Generates the metadata schedule across all sequences.
  - <a id="BaseMetadataComputer.enter_window"></a>`enter_window()` — [`L810`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L810)
  - <a id="BaseMetadataComputer.fill_dma_kv_new"></a>`fill_dma_kv_new(i, dst_vmem, dma_sz)` — [`L653`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L653) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="BaseMetadataComputer.flush_carry"></a>`flush_carry(self, carry: LoopCarry)` — [`L730`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L730)
  - <a id="BaseMetadataComputer.get_rpa_schedule"></a>`get_rpa_schedule(cls, cfgs: configs.RpaConfigs, multiplier: int = 1)` — [`L511`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L511) — Returns the RpaSchedule shape/dtype struct for this metadata computer.
  - <a id="BaseMetadataComputer.k_loop"></a>`k_loop(self, k_idx, carry: LoopCarry, *, s_idx, q_idx, q_end, q_src, q_sz_task, kv_cache_len, kv_new_len, end_k_idx, p_offset)` — [`L590`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L590) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="BaseMetadataComputer.page_indices_offset"></a>`page_indices_offset(self, s_idx)` — [`L579`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L579) — Offset in `page_indices_ref` where sequence `s_idx`'s row starts.
  - <a id="BaseMetadataComputer.page_window_idx"></a>`page_window_idx(self, s_idx)` — [`L548`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L548) — Window holding sequence `s_idx`'s page_indices row.
  - <a id="BaseMetadataComputer.q_loop"></a>`q_loop(self, q_idx, carry: LoopCarry, *, s_idx, q_start, q_end, q_offset, kv_cache_len, kv_new_len, num_k, p_offset)` — [`L742`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L742)
  - <a id="BaseMetadataComputer.seq_loop"></a>`seq_loop(self, s_idx, carry: LoopCarry, *, cu_q_lens_ref, q_offsets_ref, kv_cache_lens_ref, kv_new_lens_ref, start_seq_idx, end_seq_idx)` — [`L786`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L786)
  - <a id="BaseMetadataComputer.start_page_window"></a>`start_page_window(self, win_idx, pred)` — [`L552`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L552) — Starts the DMA of window `win_idx` into slot `win_idx & 1` when `pred`.
  - <a id="BaseMetadataComputer.start_window_copy"></a>`start_window_copy()` — [`L563`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L563)
  - <a id="BaseMetadataComputer.wait_page_window"></a>`wait_page_window(self, win_idx)` — [`L574`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L574) — Waits for window `win_idx`; only the semaphore and size matter.
  - <a id="BaseMetadataComputer.cfgs"></a>`cfgs` — [`L542`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L542)
  - <a id="BaseMetadataComputer.dma_sem"></a>`dma_sem` — [`L541`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L541)
  - <a id="BaseMetadataComputer.extra_refs"></a>`extra_refs` — [`L543`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L543)
  - <a id="BaseMetadataComputer.page_indices_hbm_ref"></a>`page_indices_hbm_ref` — [`L544`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L544)
  - <a id="BaseMetadataComputer.page_indices_ref"></a>`page_indices_ref` — [`L545`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L545)
  - <a id="BaseMetadataComputer.page_indices_sem"></a>`page_indices_sem` — [`L546`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L546)
  - <a id="BaseMetadataComputer.schedule"></a>`schedule` — [`L539`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L539)
  - <a id="BaseMetadataComputer.schedule_hbm_ref"></a>`schedule_hbm_ref` — [`L540`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L540)
- protocol/private: <a id="BaseMetadataComputer.__init__"></a>`__init__`[`L526`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L526)
- uses (calls/refs, reference-scoped): [`serve`](configs.md#RpaConfigs.serve), [`k_loop`](schedule_cp.md#CPMetadataComputer.k_loop), [`KVLayout`](configs.md#KVLayout), [`SEQ_ALONG_LANE`](configs.md#KVLayout.SEQ_ALONG_LANE), [`model`](configs.md#RpaConfigs.model), [`bkv_sz`](configs.md#RpaConfigs.bkv_sz), [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`batch_size`](configs.md#RpaConfigs.batch_size), [`RpaConfigs`](configs.md#RpaConfigs), [`kv_layout`](configs.md#ServingConfigs.kv_layout), [`align_to`](utils.md#align_to), [`max_steps_ub`](configs.md#RpaConfigs.max_steps_ub), [`create_shape_dtype`](schedule.md#RpaSchedule.create_shape_dtype), [`page_size`](configs.md#ServingConfigs.page_size), [`RpaSchedule`](schedule.md#RpaSchedule), [`HEAD_ALONG_SUBLANE`](configs.md#KVLayout.HEAD_ALONG_SUBLANE), [`get_rpa_schedule`](schedule_cp.md#CPMetadataComputer.get_rpa_schedule), [`bkv_p`](configs.md#RpaConfigs.bkv_p), [`dma_kv_cache`](schedule.md#RpaSchedule.dma_kv_cache), [`flush_to_hbm`](schedule.md#flush_to_hbm), [`bkv_p_cache`](configs.md#RpaConfigs.bkv_p_cache), [`bq_sz`](configs.md#RpaConfigs.bq_sz), [`kv_token_align`](configs.md#RpaConfigs.kv_token_align), [`pages_per_seq`](configs.md#ServingConfigs.pages_per_seq), [`LoopCarry`](schedule.md#LoopCarry), [`AttentionScope`](configs.md#AttentionScope), [`page_window_seqs`](configs.md#RpaConfigs.page_window_seqs), [`page_size_log2`](configs.md#ServingConfigs.page_size_log2), [`page_window_entries`](configs.md#RpaConfigs.page_window_entries), [`set_flags`](schedule.md#DmaNew.set_flags), [`attention_scope`](configs.md#ServingConfigs.attention_scope), [`is_last_k`](schedule.md#RpaSchedule.is_last_k), [`page_window_slot_len`](configs.md#RpaConfigs.page_window_slot_len), [`seq_range`](configs.md#RpaConfigs.seq_range), [`dma_q`](schedule.md#RpaSchedule.dma_q), [`dma_kv_new`](schedule.md#RpaSchedule.dma_kv_new), [`fetch_hbm`](schedule.md#DmaNew.fetch_hbm), [`fetch_vmem`](schedule.md#DmaNew.fetch_vmem), [`k_idx`](schedule.md#RpaSchedule.k_idx), [`page_size_mask`](configs.md#ServingConfigs.page_size_mask)  (+14 more)
- used by: [`k_loop`](schedule_cp.md#CPMetadataComputer.k_loop), [`fill_dma_kv_new`](schedule_cp.md#CPMetadataComputer.fill_dma_kv_new), [`run_rpa_kernel`](wrapper.md#ragged_paged_attention.run_rpa_kernel), [`generate_rpa_metadata`](schedule.md#generate_rpa_metadata), [`rpa_kernel`](kernel.md#rpa_kernel), [`rpa_metadata_schedule_kernel`](schedule.md#rpa_metadata_schedule_kernel), [`_run`](kernel.md#rpa_kernel.ragged_paged_attention_pipeline._run), [`__init__`](schedule_cp.md#CPMetadataComputer.__init__), [`rank`](schedule_cp.md#CPMetadataComputer.rank), [`CPMetadataComputer`](schedule_cp.md#CPMetadataComputer)

### <a id="DmaNew"></a>`DmaNew`  ·  implements/extends ABC
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L51)
- signature: `class DmaNew(ABC):`
- members:
  - <a id="DmaNew.fetch_val"></a>`fetch_val(self)` — [`L76`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L76)
  - <a id="DmaNew.num_fields"></a>`num_fields()` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L69)
  - <a id="DmaNew.set_flags"></a>`set_flags(self, fetch_val, wb_val)` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L72)
  - <a id="DmaNew.wb_val"></a>`wb_val(self)` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L80)
  - <a id="DmaNew.data"></a>`data` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L52)
  - <a id="DmaNew.fetch_hbm"></a>`fetch_hbm` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L58)
  - <a id="DmaNew.fetch_vmem"></a>`fetch_vmem` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L59)
  - <a id="DmaNew.pos"></a>`pos` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L53)
  - <a id="DmaNew.wb_hbm"></a>`wb_hbm` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L62)
  - <a id="DmaNew.wb_vmem"></a>`wb_vmem` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L63)
- protocol/private: <a id="DmaNew._flags"></a>`_flags`[`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L65)
- uses (calls/refs, reference-scoped): [`FieldOffset`](schedule.md#FieldOffset), [`SeqAlongLaneDmaNew`](schedule.md#SeqAlongLaneDmaNew), [`set_flags`](schedule_cp.md#HeadAlongSublaneDmaNewCP.set_flags), [`HeadAlongSublaneDmaNew`](schedule.md#HeadAlongSublaneDmaNew), [`HeadAlongSublaneDmaNewCP`](schedule_cp.md#HeadAlongSublaneDmaNewCP), [`fetch_val`](schedule_cp.md#HeadAlongSublaneDmaNewCP.fetch_val), [`fetch_val`](schedule.md#HeadAlongSublaneDmaNew.fetch_val), [`fetch_val`](schedule.md#SeqAlongLaneDmaNew.fetch_val), [`set_flags`](schedule.md#HeadAlongSublaneDmaNew.set_flags), [`set_flags`](schedule.md#SeqAlongLaneDmaNew.set_flags), [`wb_val`](schedule_cp.md#HeadAlongSublaneDmaNewCP.wb_val), [`wb_val`](schedule.md#HeadAlongSublaneDmaNew.wb_val), [`wb_val`](schedule.md#SeqAlongLaneDmaNew.wb_val), [`num_fields`](schedule_cp.md#HeadAlongSublaneDmaNewCP.num_fields), [`num_fields`](schedule.md#HeadAlongSublaneDmaNew.num_fields), [`num_fields`](schedule.md#SeqAlongLaneDmaNew.num_fields)
- used by: [`_mask_out_steps`](schedule.md#_mask_out_steps), [`body`](schedule.md#_compute_waits.body), [`fill_dma_kv_new`](schedule_cp.md#CPMetadataComputer.fill_dma_kv_new), [`fill_dma_kv_new`](schedule.md#BaseMetadataComputer.fill_dma_kv_new), [`create_shape_dtype`](schedule.md#RpaSchedule.create_shape_dtype), [`SeqAlongLaneDmaNew`](schedule.md#SeqAlongLaneDmaNew), [`HeadAlongSublaneDmaNew`](schedule.md#HeadAlongSublaneDmaNew), [`HeadAlongSublaneDmaNewCP`](schedule_cp.md#HeadAlongSublaneDmaNewCP), [`struct_cls`](schedule.md#SmemArrayOfStructs.struct_cls)

### <a id="FieldOffset"></a>`FieldOffset`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L30)
- doc: A Python descriptor that generates the `.at[pos + offset]` lazy lookup.
- signature: `class FieldOffset:`
- members:
  - <a id="FieldOffset.offset"></a>`offset` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L43)
- protocol/private: <a id="FieldOffset.__get__"></a>`__get__`[`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L46), <a id="FieldOffset.__init__"></a>`__init__`[`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L39), <a id="FieldOffset.__isabstractmethod__"></a>`__isabstractmethod__`[`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L44)
- used by: [`fetch_hbm`](schedule.md#DmaNew.fetch_hbm), [`fetch_vmem`](schedule.md#DmaNew.fetch_vmem), [`wb_hbm`](schedule.md#DmaNew.wb_hbm), [`_flags`](schedule.md#HeadAlongSublaneDmaNew._flags), [`_flags`](schedule.md#SeqAlongLaneDmaNew._flags), [`wb_vmem`](schedule.md#DmaNew.wb_vmem), [`_fetch_flags`](schedule_cp.md#HeadAlongSublaneDmaNewCP._fetch_flags), [`_wb_flags`](schedule_cp.md#HeadAlongSublaneDmaNewCP._wb_flags), [`_flags`](schedule.md#DmaNew._flags), [`fetch_hbm`](schedule_cp.md#HeadAlongSublaneDmaNewCP.fetch_hbm), [`fetch_hbm`](schedule.md#HeadAlongSublaneDmaNew.fetch_hbm), [`fetch_hbm`](schedule.md#SeqAlongLaneDmaNew.fetch_hbm), [`fetch_vmem`](schedule_cp.md#HeadAlongSublaneDmaNewCP.fetch_vmem), [`fetch_vmem`](schedule.md#HeadAlongSublaneDmaNew.fetch_vmem), [`fetch_vmem`](schedule.md#SeqAlongLaneDmaNew.fetch_vmem), [`wb_hbm`](schedule_cp.md#HeadAlongSublaneDmaNewCP.wb_hbm), [`wb_hbm`](schedule.md#HeadAlongSublaneDmaNew.wb_hbm), [`wb_hbm`](schedule.md#SeqAlongLaneDmaNew.wb_hbm), [`wb_vmem`](schedule_cp.md#HeadAlongSublaneDmaNewCP.wb_vmem), [`wb_vmem`](schedule.md#HeadAlongSublaneDmaNew.wb_vmem), [`wb_vmem`](schedule.md#SeqAlongLaneDmaNew.wb_vmem)

### <a id="HeadAlongSublaneDmaNew"></a>`HeadAlongSublaneDmaNew`  ·  implements/extends DmaNew
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:112`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L112)
- signature: `class HeadAlongSublaneDmaNew(DmaNew):`
- members:
  - <a id="HeadAlongSublaneDmaNew.fetch_val"></a>`fetch_val(self)` — [`L126`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L126)
  - <a id="HeadAlongSublaneDmaNew.num_fields"></a>`num_fields()` — [`L122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L122)
  - <a id="HeadAlongSublaneDmaNew.set_flags"></a>`set_flags(self, fetch_val, wb_val)` — [`L133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L133)
  - <a id="HeadAlongSublaneDmaNew.wb_val"></a>`wb_val(self)` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L130)
  - <a id="HeadAlongSublaneDmaNew.fetch_hbm"></a>`fetch_hbm` — [`L116`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L116)
  - <a id="HeadAlongSublaneDmaNew.fetch_vmem"></a>`fetch_vmem` — [`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L117)
  - <a id="HeadAlongSublaneDmaNew.wb_hbm"></a>`wb_hbm` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L115)
  - <a id="HeadAlongSublaneDmaNew.wb_vmem"></a>`wb_vmem` — [`L118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L118)
- protocol/private: <a id="HeadAlongSublaneDmaNew._flags"></a>`_flags`[`L119`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L119)
- uses (calls/refs, reference-scoped): [`FieldOffset`](schedule.md#FieldOffset), [`DmaNew`](schedule.md#DmaNew)
- used by: [`get_rpa_schedule`](schedule.md#BaseMetadataComputer.get_rpa_schedule), [`DmaNew`](schedule.md#DmaNew), [`set_flags`](schedule.md#DmaNew.set_flags), [`fetch_val`](schedule.md#DmaNew.fetch_val), [`wb_val`](schedule.md#DmaNew.wb_val), [`num_fields`](schedule.md#DmaNew.num_fields)

### <a id="LoopCarry"></a>`LoopCarry`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:502`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L502)
- signature: `class LoopCarry:`
- members:
  - <a id="LoopCarry.count"></a>`count` — [`L504`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L504)
  - <a id="LoopCarry.hbm_offset"></a>`hbm_offset` — [`L503`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L503)
- used by: [`k_loop`](schedule_cp.md#CPMetadataComputer.k_loop), [`k_loop`](schedule.md#BaseMetadataComputer.k_loop), [`q_loop`](schedule.md#BaseMetadataComputer.q_loop), [`rpa_metadata_schedule_kernel`](schedule.md#rpa_metadata_schedule_kernel), [`seq_loop`](schedule.md#BaseMetadataComputer.seq_loop), [`flush_carry`](schedule.md#BaseMetadataComputer.flush_carry), [`advance_carry`](schedule.md#BaseMetadataComputer.advance_carry), [`compute`](schedule.md#BaseMetadataComputer.compute)

### <a id="RpaSchedule"></a>`RpaSchedule`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:202`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L202)
- doc: Container for metadata arrays with integrated shape/spec logic.
- signature: `class RpaSchedule:`
- members:
  - <a id="RpaSchedule.create_shape_dtype"></a>`create_shape_dtype(cls, cfgs: configs.RpaConfigs, dma_kv_new_struct_cls: type[DmaNew] = SeqAlongLaneDmaNew, multiplier: int = 1)` — [`L223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L223)
  - <a id="RpaSchedule.get_dma_kv_cache"></a>`get_dma_kv_cache(self, step: jax.typing.ArrayLike, batch_idx: jax.typing.ArrayLike, page_idx: jax.typing.ArrayLike)` — [`L267`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L267)
  - <a id="RpaSchedule.get_dma_q"></a>`get_dma_q(self, step: jax.typing.ArrayLike, batch_idx: jax.typing.ArrayLike)` — [`L279`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L279)
  - <a id="RpaSchedule.in_specs"></a>`in_specs(self)` — [`L295`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L295) — Returns a Pytree of input BlockSpecs.
  - <a id="RpaSchedule.out_specs"></a>`out_specs(self)` — [`L310`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L310) — Returns a Pytree of output BlockSpecs.
  - <a id="RpaSchedule.scratch_shapes"></a>`scratch_shapes(self)` — [`L287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L287) — Returns a Pytree of SMEM scratch memory.
  - <a id="RpaSchedule.wrapper"></a>`wrapper(x)` — [`L298`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L298)
  - <a id="RpaSchedule.actual_steps"></a>`actual_steps` — [`L218`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L218)
  - <a id="RpaSchedule.cfgs"></a>`cfgs` — [`L220`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L220)
  - <a id="RpaSchedule.dma_kv_cache"></a>`dma_kv_cache` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L211)
  - <a id="RpaSchedule.dma_kv_new"></a>`dma_kv_new` — [`L212`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L212)
  - <a id="RpaSchedule.dma_q"></a>`dma_q` — [`L210`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L210)
  - <a id="RpaSchedule.do_writeback"></a>`do_writeback` — [`L209`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L209)
  - <a id="RpaSchedule.is_last_k"></a>`is_last_k` — [`L208`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L208)
  - <a id="RpaSchedule.k_idx"></a>`k_idx` — [`L207`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L207)
  - <a id="RpaSchedule.q_idx"></a>`q_idx` — [`L206`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L206)
  - <a id="RpaSchedule.s_idx"></a>`s_idx` — [`L205`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L205)
  - <a id="RpaSchedule.total_wait_kv_in"></a>`total_wait_kv_in` — [`L213`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L213)
  - <a id="RpaSchedule.total_wait_kv_out"></a>`total_wait_kv_out` — [`L214`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L214)
  - <a id="RpaSchedule.total_wait_lse_out"></a>`total_wait_lse_out` — [`L217`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L217)
  - <a id="RpaSchedule.total_wait_o_out"></a>`total_wait_o_out` — [`L216`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L216)
  - <a id="RpaSchedule.total_wait_q_in"></a>`total_wait_q_in` — [`L215`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L215)
- uses (calls/refs, reference-scoped): [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`batch_size`](configs.md#RpaConfigs.batch_size), [`RpaConfigs`](configs.md#RpaConfigs), [`max_steps_ub`](configs.md#RpaConfigs.max_steps_ub), [`SmemWrapper`](schedule.md#SmemWrapper), [`bkv_p_cache`](configs.md#RpaConfigs.bkv_p_cache), [`dma_kv_new_size`](configs.md#RpaConfigs.dma_kv_new_size), [`DmaNew`](schedule.md#DmaNew), [`create_shape_dtype`](schedule.md#SmemWrapper.create_shape_dtype), [`SeqAlongLaneDmaNew`](schedule.md#SeqAlongLaneDmaNew), [`SmemArrayOfStructs`](schedule.md#SmemArrayOfStructs), [`create_shape_dtype`](schedule.md#SmemArrayOfStructs.create_shape_dtype)
- used by: [`rpa_body`](kernel.md#rpa_body), [`k_loop`](schedule_cp.md#CPMetadataComputer.k_loop), [`k_loop`](schedule.md#BaseMetadataComputer.k_loop), [`_mask_out_steps`](schedule.md#_mask_out_steps), [`body`](schedule.md#_compute_waits.body), [`fill_dma_kv_new`](schedule_cp.md#CPMetadataComputer.fill_dma_kv_new), [`fill_dma_kv_new`](schedule.md#BaseMetadataComputer.fill_dma_kv_new), [`fetch_compute_metadata`](kernel.md#fetch_compute_metadata), [`fetch_stitch_metadata`](kernel.md#fetch_stitch_metadata), [`get_rpa_schedule`](schedule.md#BaseMetadataComputer.get_rpa_schedule), [`generate_rpa_metadata`](schedule.md#generate_rpa_metadata), [`rpa_kernel`](kernel.md#rpa_kernel), [`calculate_and_store_out`](kernel.md#calculate_and_store_out), [`rpa_metadata_schedule_kernel`](schedule.md#rpa_metadata_schedule_kernel), [`get_rpa_schedule`](schedule_cp.md#CPMetadataComputer.get_rpa_schedule), [`flush_to_hbm`](schedule.md#flush_to_hbm), [`_compute_waits`](schedule.md#_compute_waits), [`_run`](kernel.md#rpa_kernel.ragged_paged_attention_pipeline._run), [`ragged_paged_attention_pipeline`](kernel.md#rpa_kernel.ragged_paged_attention_pipeline), [`_write_schedule_to_hbm`](schedule.md#_write_schedule_to_hbm), [`__init__`](schedule_cp.md#CPMetadataComputer.__init__), [`__init__`](schedule.md#BaseMetadataComputer.__init__)

### <a id="SeqAlongLaneDmaNew"></a>`SeqAlongLaneDmaNew`  ·  implements/extends DmaNew
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L85)
- signature: `class SeqAlongLaneDmaNew(DmaNew):`
- members:
  - <a id="SeqAlongLaneDmaNew.fetch_val"></a>`fetch_val(self)` — [`L97`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L97)
  - <a id="SeqAlongLaneDmaNew.num_fields"></a>`num_fields()` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L93)
  - <a id="SeqAlongLaneDmaNew.set_flags"></a>`set_flags(self, fetch_val, wb_val)` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L106)
  - <a id="SeqAlongLaneDmaNew.wb_val"></a>`wb_val(self)` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L102)
  - <a id="SeqAlongLaneDmaNew.fetch_hbm"></a>`fetch_hbm` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L86)
  - <a id="SeqAlongLaneDmaNew.fetch_vmem"></a>`fetch_vmem` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L87)
  - <a id="SeqAlongLaneDmaNew.wb_hbm"></a>`wb_hbm` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L88)
  - <a id="SeqAlongLaneDmaNew.wb_vmem"></a>`wb_vmem` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L89)
- protocol/private: <a id="SeqAlongLaneDmaNew._flags"></a>`_flags`[`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L90)
- uses (calls/refs, reference-scoped): [`FieldOffset`](schedule.md#FieldOffset), [`DmaNew`](schedule.md#DmaNew)
- used by: [`create_shape_dtype`](schedule.md#RpaSchedule.create_shape_dtype), [`get_rpa_schedule`](schedule.md#BaseMetadataComputer.get_rpa_schedule), [`get_rpa_schedule`](schedule_cp.md#CPMetadataComputer.get_rpa_schedule), [`DmaNew`](schedule.md#DmaNew), [`set_flags`](schedule.md#DmaNew.set_flags), [`fetch_val`](schedule.md#DmaNew.fetch_val), [`wb_val`](schedule.md#DmaNew.wb_val), [`num_fields`](schedule.md#DmaNew.num_fields)

### <a id="SmemArrayOfStructs"></a>`SmemArrayOfStructs`  ·  implements/extends SmemWrapper
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L168)
- doc: Maps physical 1-D data into logical Array of Structs.
- signature: `class SmemArrayOfStructs(SmemWrapper):`
- members:
  - <a id="SmemArrayOfStructs.create_shape_dtype"></a>`create_shape_dtype(cls, shape, struct_cls, struct_size)` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L175)
  - <a id="SmemArrayOfStructs.struct_cls"></a>`struct_cls` — [`L171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L171)
  - <a id="SmemArrayOfStructs.struct_size"></a>`struct_size` — [`L172`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L172)
- protocol/private: <a id="SmemArrayOfStructs.__getitem__"></a>`__getitem__`[`L195`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L195), <a id="SmemArrayOfStructs._get_pos"></a>`_get_pos`[`L186`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L186)
- uses (calls/refs, reference-scoped): [`SmemWrapper`](schedule.md#SmemWrapper), [`DmaNew`](schedule.md#DmaNew), [`data`](schedule.md#SmemWrapper.data), [`shape`](schedule.md#SmemWrapper.shape)
- used by: [`create_shape_dtype`](schedule.md#RpaSchedule.create_shape_dtype), [`SmemWrapper`](schedule.md#SmemWrapper), [`dma_kv_new`](schedule.md#RpaSchedule.dma_kv_new), [`_get_pos`](schedule.md#SmemWrapper._get_pos), [`create_shape_dtype`](schedule.md#SmemWrapper.create_shape_dtype)

### <a id="SmemWrapper"></a>`SmemWrapper`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py:139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L139)
- doc: Maps physical 1-D data into logical N-D representation.
- signature: `class SmemWrapper:`
- members:
  - <a id="SmemWrapper.create_shape_dtype"></a>`create_shape_dtype(cls, shape)` — [`L146`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L146)
  - <a id="SmemWrapper.data"></a>`data` — [`L142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L142)
  - <a id="SmemWrapper.shape"></a>`shape` — [`L143`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L143)
- protocol/private: <a id="SmemWrapper.__getitem__"></a>`__getitem__`[`L159`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L159), <a id="SmemWrapper.__setitem__"></a>`__setitem__`[`L162`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L162), <a id="SmemWrapper._get_pos"></a>`_get_pos`[`L149`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L149)
- uses (calls/refs, reference-scoped): [`_get_pos`](schedule.md#SmemArrayOfStructs._get_pos), [`SmemArrayOfStructs`](schedule.md#SmemArrayOfStructs), [`create_shape_dtype`](schedule.md#SmemArrayOfStructs.create_shape_dtype)
- used by: [`flash_attention_qk_softmax`](flash_attention.md#flash_attention_qk_softmax), [`flash_attention_pv`](flash_attention.md#flash_attention_pv), [`create_shape_dtype`](schedule.md#RpaSchedule.create_shape_dtype), [`dma_kv_cache`](schedule.md#RpaSchedule.dma_kv_cache), [`is_last_k`](schedule.md#RpaSchedule.is_last_k), [`dma_q`](schedule.md#RpaSchedule.dma_q), [`__getitem__`](schedule.md#SmemArrayOfStructs.__getitem__), [`k_idx`](schedule.md#RpaSchedule.k_idx), [`s_idx`](schedule.md#RpaSchedule.s_idx), [`do_writeback`](schedule.md#RpaSchedule.do_writeback), [`q_idx`](schedule.md#RpaSchedule.q_idx), [`_get_pos`](schedule.md#SmemArrayOfStructs._get_pos), [`SmemArrayOfStructs`](schedule.md#SmemArrayOfStructs), [`total_wait_kv_in`](schedule.md#RpaSchedule.total_wait_kv_in), [`total_wait_kv_out`](schedule.md#RpaSchedule.total_wait_kv_out), [`total_wait_lse_out`](schedule.md#RpaSchedule.total_wait_lse_out), [`total_wait_o_out`](schedule.md#RpaSchedule.total_wait_o_out), [`total_wait_q_in`](schedule.md#RpaSchedule.total_wait_q_in)

## Functions
- <a id="_compute_waits"></a>`_compute_waits(schedule: RpaSchedule, start_step: jax.typing.ArrayLike, end_step: jax.typing.ArrayLike, *, cfgs: configs.RpaConfigs)` — [`L392`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L392) — Computes total wait row/lane counts for a range of steps.
- <a id="_mask_out_steps"></a>`_mask_out_steps(step: jax.typing.ArrayLike, schedule_smem: RpaSchedule, b_idx: jax.typing.ArrayLike)` — [`L319`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L319) — Mask out unvisited metadata schedule entries at (step, b_idx). — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="_write_schedule_to_hbm"></a>`_write_schedule_to_hbm(schedule_smem: RpaSchedule, schedule_hbm: RpaSchedule, hbm_offset: jax.typing.ArrayLike, num_steps: jax.typing.ArrayLike, dma_sem: jax.Ref, *, cfgs: configs.RpaConfigs)` — [`L354`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L354) — Writes `num_steps` of metadata from `schedule_smem` to
- <a id="_compute_waits.body"></a>`body(step, _)` — [`L411`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L411) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="flush_to_hbm.body"></a>`body(idx)` — [`L483`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L483)
- <a id="flush_to_hbm"></a>`flush_to_hbm(count: jax.typing.ArrayLike, schedule: RpaSchedule, schedule_hbm_ref: RpaSchedule, hbm_offset: jax.typing.ArrayLike, dma_sem: jax.Ref, *, cfgs: configs.RpaConfigs)` — [`L470`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L470)
- <a id="generate_rpa_metadata"></a>`generate_rpa_metadata(cu_q_lens: jax.Array, q_offsets: jax.Array, kv_cache_lens: jax.Array, kv_new_lens: jax.Array, distribution: jax.Array, page_indices: jax.Array, cfgs: configs.RpaConfigs, *, computer_cls: type[BaseMetadataComputer] = BaseMetadataComputer, extra_scalars: Sequence[jax.Array] = (), interpret=False)` — [`L952`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L952) — Generates RPA metadata schedule using the specified computer_cls. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="rpa_metadata_schedule_kernel"></a>`rpa_metadata_schedule_kernel(cu_q_lens_ref: jax.Ref, q_offsets_ref: jax.Ref, kv_cache_lens_ref: jax.Ref, kv_new_lens_ref: jax.Ref, distribution_ref: jax.Ref, extra_scalars_ref: Sequence[jax.Ref], page_indices_hbm_ref: jax.Ref, schedule_hbm_ref: RpaSchedule, schedule_ref: RpaSchedule, dma_sem: jax.Ref, page_indices_ref: jax.Ref, page_indices_sem: jax.Ref, *, cfgs: configs.RpaConfigs, computer_cls: type[BaseMetadataComputer] = BaseMetadataComputer)` — [`L862`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule.py#L862) — Generates the HBM-to-VMEM DMA schedule.

