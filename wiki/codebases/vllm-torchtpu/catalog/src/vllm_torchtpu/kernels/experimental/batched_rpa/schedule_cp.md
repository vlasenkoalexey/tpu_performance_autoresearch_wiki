---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.schedule_cp`/
symbols:
  CPMetadataComputer.k_loop: CPMetadataComputer#k_loop().
  CPMetadataComputer.fill_dma_kv_new: CPMetadataComputer#fill_dma_kv_new().
  CPMetadataComputer.get_rpa_schedule: CPMetadataComputer#get_rpa_schedule().
  CPMetadataComputer.__init__: CPMetadataComputer#__init__().
  CPMetadataComputer.rank: CPMetadataComputer#rank().
  HeadAlongSublaneDmaNewCP.set_flags: HeadAlongSublaneDmaNewCP#set_flags().
  HeadAlongSublaneDmaNewCP._fetch_flags: HeadAlongSublaneDmaNewCP#_fetch_flags.
  HeadAlongSublaneDmaNewCP._wb_flags: HeadAlongSublaneDmaNewCP#_wb_flags.
  HeadAlongSublaneDmaNewCP: HeadAlongSublaneDmaNewCP#
  CPMetadataComputer: CPMetadataComputer#
  HeadAlongSublaneDmaNewCP.wb_hbm: HeadAlongSublaneDmaNewCP#wb_hbm.
  HeadAlongSublaneDmaNewCP.fetch_hbm: HeadAlongSublaneDmaNewCP#fetch_hbm.
  HeadAlongSublaneDmaNewCP.fetch_vmem: HeadAlongSublaneDmaNewCP#fetch_vmem.
  HeadAlongSublaneDmaNewCP.wb_vmem: HeadAlongSublaneDmaNewCP#wb_vmem.
  HeadAlongSublaneDmaNewCP.fetch_val: HeadAlongSublaneDmaNewCP#fetch_val().
  HeadAlongSublaneDmaNewCP.wb_val: HeadAlongSublaneDmaNewCP#wb_val().
  HeadAlongSublaneDmaNewCP.num_fields: HeadAlongSublaneDmaNewCP#num_fields().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py)

## Classes
### <a id="CPMetadataComputer"></a>`CPMetadataComputer`  ·  implements/extends BaseMetadataComputer
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py:58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L58)
- doc: Context Parallel (CP) metadata scheduler: overrides only k_loop and schema.
- signature: `class CPMetadataComputer(schedule.BaseMetadataComputer):`
- members:
  - <a id="CPMetadataComputer.fill_dma_kv_new"></a>`fill_dma_kv_new(i, dst_vmem, dma_sz)` — [`L184`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L184) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="CPMetadataComputer.get_rpa_schedule"></a>`get_rpa_schedule(cls, cfgs: configs.RpaConfigs, multiplier: int = 1)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L62) — Returns the RpaSchedule shape/dtype struct with CP-specific DMA struct.
  - <a id="CPMetadataComputer.k_loop"></a>`k_loop(self, k_idx, carry: schedule.LoopCarry, *, s_idx, q_idx, q_end, q_src, q_sz_task, kv_cache_len, kv_new_len, end_k_idx, p_offset)` — [`L101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L101) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="CPMetadataComputer.rank"></a>`rank(self)` — [`L97`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L97)
- protocol/private: <a id="CPMetadataComputer.__init__"></a>`__init__`[`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L77)
- uses (calls/refs, reference-scoped): [`serve`](configs.md#RpaConfigs.serve), [`KVLayout`](configs.md#KVLayout), [`SEQ_ALONG_LANE`](configs.md#KVLayout.SEQ_ALONG_LANE), [`bkv_sz`](configs.md#RpaConfigs.bkv_sz), [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`batch_size`](configs.md#RpaConfigs.batch_size), [`RpaConfigs`](configs.md#RpaConfigs), [`kv_layout`](configs.md#ServingConfigs.kv_layout), [`align_to`](utils.md#align_to), [`create_shape_dtype`](schedule.md#RpaSchedule.create_shape_dtype), [`page_size`](configs.md#ServingConfigs.page_size), [`RpaSchedule`](schedule.md#RpaSchedule), [`HEAD_ALONG_SUBLANE`](configs.md#KVLayout.HEAD_ALONG_SUBLANE), [`bkv_p`](configs.md#RpaConfigs.bkv_p), [`advance_carry`](schedule.md#BaseMetadataComputer.advance_carry), [`dma_kv_cache`](schedule.md#RpaSchedule.dma_kv_cache), [`bkv_p_cache`](configs.md#RpaConfigs.bkv_p_cache), [`bq_sz`](configs.md#RpaConfigs.bq_sz), [`kv_token_align`](configs.md#RpaConfigs.kv_token_align), [`pages_per_seq`](configs.md#ServingConfigs.pages_per_seq), [`LoopCarry`](schedule.md#LoopCarry), [`AttentionScope`](configs.md#AttentionScope), [`cfgs`](schedule.md#BaseMetadataComputer.cfgs), [`page_size_log2`](configs.md#ServingConfigs.page_size_log2), [`set_flags`](schedule.md#DmaNew.set_flags), [`attention_scope`](configs.md#ServingConfigs.attention_scope), [`is_last_k`](schedule.md#RpaSchedule.is_last_k), [`BaseMetadataComputer`](schedule.md#BaseMetadataComputer), [`dma_q`](schedule.md#RpaSchedule.dma_q), [`page_indices_ref`](schedule.md#BaseMetadataComputer.page_indices_ref), [`dma_kv_new`](schedule.md#RpaSchedule.dma_kv_new), [`fetch_hbm`](schedule.md#DmaNew.fetch_hbm), [`fetch_vmem`](schedule.md#DmaNew.fetch_vmem), [`k_idx`](schedule.md#RpaSchedule.k_idx), [`page_size_mask`](configs.md#ServingConfigs.page_size_mask), [`s_idx`](schedule.md#RpaSchedule.s_idx), [`wb_hbm`](schedule.md#DmaNew.wb_hbm), [`align_span`](utils.md#align_span), [`do_writeback`](schedule.md#RpaSchedule.do_writeback), [`q_idx`](schedule.md#RpaSchedule.q_idx)  (+9 more)
- used by: [`k_loop`](schedule.md#BaseMetadataComputer.k_loop), [`run_rpa_kernel`](wrapper.md#ragged_paged_attention.run_rpa_kernel), [`get_rpa_schedule`](schedule.md#BaseMetadataComputer.get_rpa_schedule), [`BaseMetadataComputer`](schedule.md#BaseMetadataComputer)

### <a id="HeadAlongSublaneDmaNewCP"></a>`HeadAlongSublaneDmaNewCP`  ·  implements/extends DmaNew
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py:27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L27)
- doc: Like HeadAlongSublaneDmaNew but with separate fetch/wb flags for CP.
- signature: `class HeadAlongSublaneDmaNewCP(schedule.DmaNew):`
- members:
  - <a id="HeadAlongSublaneDmaNewCP.fetch_val"></a>`fetch_val(self)` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L46)
  - <a id="HeadAlongSublaneDmaNewCP.num_fields"></a>`num_fields()` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L42)
  - <a id="HeadAlongSublaneDmaNewCP.set_flags"></a>`set_flags(self, fetch_val, wb_val)` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L53)
  - <a id="HeadAlongSublaneDmaNewCP.wb_val"></a>`wb_val(self)` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L50)
  - <a id="HeadAlongSublaneDmaNewCP.fetch_hbm"></a>`fetch_hbm` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L35)
  - <a id="HeadAlongSublaneDmaNewCP.fetch_vmem"></a>`fetch_vmem` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L36)
  - <a id="HeadAlongSublaneDmaNewCP.wb_hbm"></a>`wb_hbm` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L34)
  - <a id="HeadAlongSublaneDmaNewCP.wb_vmem"></a>`wb_vmem` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L37)
- protocol/private: <a id="HeadAlongSublaneDmaNewCP._fetch_flags"></a>`_fetch_flags`[`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L38), <a id="HeadAlongSublaneDmaNewCP._wb_flags"></a>`_wb_flags`[`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/schedule_cp.py#L39)
- uses (calls/refs, reference-scoped): [`FieldOffset`](schedule.md#FieldOffset), [`DmaNew`](schedule.md#DmaNew)
- used by: [`get_rpa_schedule`](schedule_cp.md#CPMetadataComputer.get_rpa_schedule), [`DmaNew`](schedule.md#DmaNew), [`set_flags`](schedule.md#DmaNew.set_flags), [`fetch_val`](schedule.md#DmaNew.fetch_val), [`wb_val`](schedule.md#DmaNew.wb_val), [`num_fields`](schedule.md#DmaNew.num_fields)

