---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.configs`/
symbols:
  RpaConfigs.serve: RpaConfigs#serve.
  KVLayout: KVLayout#
  KVLayout.SEQ_ALONG_LANE: KVLayout#SEQ_ALONG_LANE.
  RpaConfigs.validate_inputs: RpaConfigs#validate_inputs().
  RpaConfigs.model: RpaConfigs#model.
  RpaConfigs.bkv_sz: RpaConfigs#bkv_sz().
  RpaConfigs.bkv_p_new: RpaConfigs#bkv_p_new().
  RpaConfigs.batch_size: RpaConfigs#batch_size().
  RpaConfigs.aligned_kv_head_dim: RpaConfigs#aligned_kv_head_dim().
  RpaConfigs: RpaConfigs#
  ServingConfigs.kv_layout: ServingConfigs#kv_layout.
  RpaConfigs.max_steps_ub: RpaConfigs#max_steps_ub().
  RpaConfigs.kv_vmem_shape: RpaConfigs#kv_vmem_shape().
  ModelConfigs.num_kv_heads: ModelConfigs#num_kv_heads.
  RpaConfigs.block: RpaConfigs#block.
  RpaConfigs.compute_kv_head_dim: RpaConfigs#compute_kv_head_dim().
  ServingConfigs.page_size: ServingConfigs#page_size.
  RpaConfigs.kv_bytes_per_token: RpaConfigs#kv_bytes_per_token().
  RpaConfigs.aligned_num_q_heads_per_kv_head: RpaConfigs#aligned_num_q_heads_per_kv_head().
  RpaConfigs.kv_hbm_stride: RpaConfigs#kv_hbm_stride().
  RpaConfigs.q_vmem_shape: RpaConfigs#q_vmem_shape().
  ServingConfigs.packing_kv: ServingConfigs#packing_kv().
  KVLayout.HEAD_ALONG_SUBLANE: KVLayout#HEAD_ALONG_SUBLANE.
  RpaConfigs.aligned_num_kv_heads_x2: RpaConfigs#aligned_num_kv_heads_x2().
  RpaConfigs.lse_vmem_shape: RpaConfigs#lse_vmem_shape().
  RpaConfigs.bkv_p: RpaConfigs#bkv_p().
  RpaConfigs.bkv_stride: RpaConfigs#bkv_stride().
  ServingConfigs.dtype_kv: ServingConfigs#dtype_kv.
  RpaConfigs.q_bytes_per_token: RpaConfigs#q_bytes_per_token().
  RpaConfigs.o_bytes_per_token: RpaConfigs#o_bytes_per_token().
  RpaCase: RpaCase#
  RpaConfigs.bq_sz: RpaConfigs#bq_sz().
  RpaConfigs.bkv_p_cache: RpaConfigs#bkv_p_cache().
  ServingConfigs.pages_per_seq: ServingConfigs#pages_per_seq().
  RpaConfigs.kv_token_align: RpaConfigs#kv_token_align().
  RpaConfigs.dma_kv_new_size: RpaConfigs#dma_kv_new_size().
  RpaConfigs.acc_scratch_shape: RpaConfigs#acc_scratch_shape().
  AttentionScope: AttentionScope#
  RpaConfigs.aligned_q_head_dim: RpaConfigs#aligned_q_head_dim().
  RpaConfigs.lm_scratch_shape: RpaConfigs#lm_scratch_shape().
  ModelConfigs.head_dim: ModelConfigs#head_dim.
  ServingConfigs.dtype_out: ServingConfigs#dtype_out.
  RpaConfigs.page_window_seqs: RpaConfigs#page_window_seqs().
  ServingConfigs.page_size_log2: ServingConfigs#page_size_log2().
  RpaConfigs.page_window_entries: RpaConfigs#page_window_entries().
  RpaConfigs.kv_vmem_lanes: RpaConfigs#kv_vmem_lanes().
  BlockSizes.batch_size: BlockSizes#batch_size.
  ServingConfigs.per_token_scale_dtype: ServingConfigs#per_token_scale_dtype.
  ServingConfigs.attention_scope: ServingConfigs#attention_scope.
  ServingConfigs.packing_q: ServingConfigs#packing_q().
  BlockSizes.bq_sz: BlockSizes#bq_sz.
  RpaCase.symbol: RpaCase#symbol().
  RpaConfigs.seq_range: RpaConfigs#seq_range().
  RpaConfigs.page_window_slot_len: RpaConfigs#page_window_slot_len().
  RpaConfigs.mode: RpaConfigs#mode.
  RpaConfigs.fuse_accum: RpaConfigs#fuse_accum().
  RpaCase.get_range: RpaCase#get_range().
  ServingConfigs.__post_init__: ServingConfigs#__post_init__().
  ServingConfigs.scale_channels: ServingConfigs#scale_channels().
  KVLayout.symbol: KVLayout#symbol().
  RpaCase.DECODE: RpaCase#DECODE.
  ServingConfigs.page_size_mask: ServingConfigs#page_size_mask().
  BlockSizes: BlockSizes#
  ModelConfigs.num_q_heads_per_kv_head: ModelConfigs#num_q_heads_per_kv_head().
  ServingConfigs.per_token_scale: ServingConfigs#per_token_scale.
  ServingConfigs.return_lse: ServingConfigs#return_lse.
  RpaConfigs.bq_c_sz: RpaConfigs#bq_c_sz().
  BlockSizes.bkv_sz: BlockSizes#bkv_sz.
  ModelConfigs.sliding_window: ModelConfigs#sliding_window.
  AttentionScope.NEW_TOKENS_ONLY: AttentionScope#NEW_TOKENS_ONLY.
  ServingConfigs.dtype_q: ServingConfigs#dtype_q.
  ServingConfigs.max_decode_bkv_p_new: ServingConfigs#max_decode_bkv_p_new().
  RpaConfigs.max_schedule_size_multiplier: RpaConfigs#max_schedule_size_multiplier().
  ModelConfigs.num_q_heads: ModelConfigs#num_q_heads.
  RpaCase.MIXED: RpaCase#MIXED.
  ServingConfigs.num_seqs: ServingConfigs#num_seqs.
  ServingConfigs.scale_q: ServingConfigs#scale_q.
  ServingConfigs.scale_v: ServingConfigs#scale_v.
  ModelConfigs.soft_cap: ModelConfigs#soft_cap.
  NUM_INPUT_SLOTS: NUM_INPUT_SLOTS.
  NUM_OUTPUT_SLOTS: NUM_OUTPUT_SLOTS.
  ServingConfigs.cp_group_size: ServingConfigs#cp_group_size.
  ServingConfigs.mask_invalid_v: ServingConfigs#mask_invalid_v.
  ModelConfigs: ModelConfigs#
  AttentionScope.FULL: AttentionScope#FULL.
  AttentionScope.CACHE_ONLY: AttentionScope#CACHE_ONLY.
  RpaCase.PREFILL: RpaCase#PREFILL.
  ServingConfigs: ServingConfigs#
  ServingConfigs.scale_k: ServingConfigs#scale_k.
  ServingConfigs.skip_kv_update: ServingConfigs#skip_kv_update.
  BlockSizes.bq_c_sz: BlockSizes#bq_c_sz.
  ModelConfigs.mask_value: ModelConfigs#mask_value.
  ModelConfigs.sm_scale: ModelConfigs#sm_scale.
  ServingConfigs.num_page_indices: ServingConfigs#num_page_indices.
  ServingConfigs.decode_query_size: ServingConfigs#decode_query_size.
  RpaConfigs.vmem_limit_bytes: RpaConfigs#vmem_limit_bytes.
  ServingConfigs.total_q_tokens: ServingConfigs#total_q_tokens.
  ServingConfigs.smem_fraction_limit_for_schedule_generation: ServingConfigs#smem_fraction_limit_for_schedule_generation.
  ServingConfigs.max_schedule_size_multiplier: ServingConfigs#max_schedule_size_multiplier.
  ServingConfigs.page_indices_window_size: ServingConfigs#page_indices_window_size.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py)

## Classes
### <a id="AttentionScope"></a>`AttentionScope`  ·  implements/extends StrEnum
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py:71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L71) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- doc: Which KV positions to attend to.
- signature: `class AttentionScope(enum.StrEnum):`
- members:
  - <a id="AttentionScope.CACHE_ONLY"></a>`CACHE_ONLY` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L80)
  - <a id="AttentionScope.FULL"></a>`FULL` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L79)
  - <a id="AttentionScope.NEW_TOKENS_ONLY"></a>`NEW_TOKENS_ONLY` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L81)
- used by: [`ragged_paged_attention`](wrapper.md#ragged_paged_attention), [`k_loop`](schedule_cp.md#CPMetadataComputer.k_loop), [`validate_inputs`](configs.md#RpaConfigs.validate_inputs), [`fetch_compute_metadata`](kernel.md#fetch_compute_metadata), [`q_loop`](schedule.md#BaseMetadataComputer.q_loop), [`build_dcp_kernels`](../../../layers/adapter/cp_attention.md#build_dcp_kernels), [`_pallas_rpa_kernel_dcp`](../../../layers/adapter/cp_attention.md#_pallas_rpa_kernel_dcp), [`attention_scope`](configs.md#ServingConfigs.attention_scope)

### <a id="BlockSizes"></a>`BlockSizes`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py:28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L28)
- doc: Tuning parameters for the RPA kernel.
- signature: `class BlockSizes:`
- members:
  - <a id="BlockSizes.batch_size"></a>`batch_size` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L41)
  - <a id="BlockSizes.bkv_sz"></a>`bkv_sz` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L40)
  - <a id="BlockSizes.bq_c_sz"></a>`bq_c_sz` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L39)
  - <a id="BlockSizes.bq_sz"></a>`bq_sz` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L38)
- used by: [`ragged_paged_attention`](wrapper.md#ragged_paged_attention), [`validate_inputs`](configs.md#RpaConfigs.validate_inputs), [`calculate_block_sizes`](wrapper.md#calculate_block_sizes), [`bkv_sz`](configs.md#RpaConfigs.bkv_sz), [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`flash_attention_qk_softmax`](flash_attention.md#flash_attention_qk_softmax), [`batch_size`](configs.md#RpaConfigs.batch_size), [`find_best_block_sizes`](wrapper.md#calculate_block_sizes.find_best_block_sizes), [`flash_attention_pv`](flash_attention.md#flash_attention_pv), [`kv_vmem_shape`](configs.md#RpaConfigs.kv_vmem_shape), [`max_steps_ub`](configs.md#RpaConfigs.max_steps_ub), [`block`](configs.md#RpaConfigs.block), [`store_new_kv_lane`](stitch_utils.md#store_new_kv_lane), [`q_vmem_shape`](configs.md#RpaConfigs.q_vmem_shape), [`lse_vmem_shape`](configs.md#RpaConfigs.lse_vmem_shape), [`stitch_new_kv_lane`](stitch_utils.md#stitch_new_kv_lane), [`bkv_p`](configs.md#RpaConfigs.bkv_p), [`bq_sz`](configs.md#RpaConfigs.bq_sz), [`acc_scratch_shape`](configs.md#RpaConfigs.acc_scratch_shape), [`lm_scratch_shape`](configs.md#RpaConfigs.lm_scratch_shape), [`kv_vmem_lanes`](configs.md#RpaConfigs.kv_vmem_lanes), [`_stitch_decode_lane`](stitch_utils.md#_stitch_decode_lane), [`bq_c_sz`](configs.md#RpaConfigs.bq_c_sz)

### <a id="KVLayout"></a>`KVLayout`  ·  implements/extends StrEnum
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py:84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L84) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- doc: Represents the different layouts for KV cache.
- signature: `class KVLayout(enum.StrEnum):`
- members:
  - <a id="KVLayout.symbol"></a>`symbol(self)` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L95)
  - <a id="KVLayout.HEAD_ALONG_SUBLANE"></a>`HEAD_ALONG_SUBLANE` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L91) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="KVLayout.SEQ_ALONG_LANE"></a>`SEQ_ALONG_LANE` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L92) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- used by: [`ragged_paged_attention`](wrapper.md#ragged_paged_attention), [`rpa_body`](kernel.md#rpa_body), [`k_loop`](schedule_cp.md#CPMetadataComputer.k_loop), [`_build_rpa_kernel`](../../../layers/adapter/attention.md#PallasAttentionBackendImpl._build_rpa_kernel), [`validate_inputs`](configs.md#RpaConfigs.validate_inputs), [`initialize_kernel`](../../../layers/adapter/attention.md#PallasAttentionBackendImpl.initialize_kernel), [`fill_dma_kv_new`](schedule_cp.md#CPMetadataComputer.fill_dma_kv_new), [`calculate_block_sizes`](wrapper.md#calculate_block_sizes), [`fill_dma_kv_new`](schedule.md#BaseMetadataComputer.fill_dma_kv_new), [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`create_allocs`](kernel.md#create_allocs), [`flash_attention_qk_softmax`](flash_attention.md#flash_attention_qk_softmax), [`_pallas_rpa_kernel_impl`](../../../layers/adapter/attention.md#_pallas_rpa_kernel_impl), [`aligned_kv_head_dim`](configs.md#RpaConfigs.aligned_kv_head_dim), [`find_best_block_sizes`](wrapper.md#calculate_block_sizes.find_best_block_sizes), [`kv_layout`](configs.md#ServingConfigs.kv_layout), [`flash_attention_pv`](flash_attention.md#flash_attention_pv), [`kv_vmem_shape`](configs.md#RpaConfigs.kv_vmem_shape), [`get_kernel_name`](kernel.md#get_kernel_name), [`pcp_streaming_attention_page_groups_packed_local_from_metadata`](../pcp_streaming_rpa/kernel.md#pcp_streaming_attention_page_groups_packed_local_from_metadata), [`_consume_scheduled_kv_page_multi_head`](../pcp_streaming_rpa/kernel.md#_consume_scheduled_kv_page_multi_head), [`get_rpa_schedule`](schedule.md#BaseMetadataComputer.get_rpa_schedule), [`compute_kv_head_dim`](configs.md#RpaConfigs.compute_kv_head_dim), [`calculate_vmem_usage`](wrapper.md#calculate_block_sizes.calculate_vmem_usage), [`KVLayout`](../pcp_streaming_rpa/kernel.md#KVLayout), [`kv_bytes_per_token`](configs.md#RpaConfigs.kv_bytes_per_token), [`sharded_ragged_paged_attention`](../../../layers/core/attention_interface.md#sharded_ragged_paged_attention), [`build_dcp_kernels`](../../../layers/adapter/cp_attention.md#build_dcp_kernels), [`_kv_store_fence`](kernel.md#rpa_body._kv_store_fence), [`kv_hbm_stride`](configs.md#RpaConfigs.kv_hbm_stride), [`sharded_pcp_ragged_paged_attention`](../pcp_streaming_rpa/wrapper.md#sharded_pcp_ragged_paged_attention), [`get_rpa_schedule`](schedule_cp.md#CPMetadataComputer.get_rpa_schedule), [`aligned_num_kv_heads_x2`](configs.md#RpaConfigs.aligned_num_kv_heads_x2), [`attention`](../../../layers/core/attention_interface.md#attention), [`_pcp_streaming_attention_current_state_page_groups_multi_head_pallas_call`](../pcp_streaming_rpa/kernel.md#_pcp_streaming_attention_current_state_page_groups_multi_head_pallas_call), [`_pcp_streaming_attention_history_output_page_groups_multi_head_pallas_call`](../pcp_streaming_rpa/kernel.md#_pcp_streaming_attention_history_output_page_groups_multi_head_pallas_call), [`_bm_kernel`](../../../layers/adapter/attention.md#PallasAttentionBackendImpl._bm_kernel), [`get_kv_cache_shape`](../../../layers/adapter/attention.md#PallasBatchedRPAAttentionBackend.get_kv_cache_shape), [`KVLayout`](../pcp_streaming_rpa/wrapper.md#KVLayout), [`_validate_pcp_streaming_support`](../../../layers/adapter/attention.md#PallasAttentionBackendImpl._validate_pcp_streaming_support)  (+22 more)

### <a id="ModelConfigs"></a>`ModelConfigs`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py:45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L45)
- doc: Model config that will always stay constant.
- signature: `class ModelConfigs:`
- members:
  - <a id="ModelConfigs.num_q_heads_per_kv_head"></a>`num_q_heads_per_kv_head(self)` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L67)
  - <a id="ModelConfigs.head_dim"></a>`head_dim` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L60)
  - <a id="ModelConfigs.mask_value"></a>`mask_value` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L61)
  - <a id="ModelConfigs.num_kv_heads"></a>`num_kv_heads` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L59) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="ModelConfigs.num_q_heads"></a>`num_q_heads` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L58)
  - <a id="ModelConfigs.sliding_window"></a>`sliding_window` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L64)
  - <a id="ModelConfigs.sm_scale"></a>`sm_scale` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L62)
  - <a id="ModelConfigs.soft_cap"></a>`soft_cap` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L63)
- used by: [`ragged_paged_attention`](wrapper.md#ragged_paged_attention), [`rpa_body`](kernel.md#rpa_body), [`validate_inputs`](configs.md#RpaConfigs.validate_inputs), [`body`](schedule.md#_compute_waits.body), [`model`](configs.md#RpaConfigs.model), [`calculate_block_sizes`](wrapper.md#calculate_block_sizes), [`flash_attention_qk_softmax`](flash_attention.md#flash_attention_qk_softmax), [`aligned_kv_head_dim`](configs.md#RpaConfigs.aligned_kv_head_dim), [`kv_vmem_shape`](configs.md#RpaConfigs.kv_vmem_shape), [`get_kernel_name`](kernel.md#get_kernel_name), [`q_loop`](schedule.md#BaseMetadataComputer.q_loop), [`compute_kv_head_dim`](configs.md#RpaConfigs.compute_kv_head_dim), [`calculate_vmem_usage`](wrapper.md#calculate_block_sizes.calculate_vmem_usage), [`get_scale_factors`](kernel.md#get_scale_factors), [`kv_bytes_per_token`](configs.md#RpaConfigs.kv_bytes_per_token), [`store_new_kv_lane`](stitch_utils.md#store_new_kv_lane), [`aligned_num_q_heads_per_kv_head`](configs.md#RpaConfigs.aligned_num_q_heads_per_kv_head), [`kv_hbm_stride`](configs.md#RpaConfigs.kv_hbm_stride), [`q_vmem_shape`](configs.md#RpaConfigs.q_vmem_shape), [`aligned_num_kv_heads_x2`](configs.md#RpaConfigs.aligned_num_kv_heads_x2), [`generate_mask`](kernel.md#generate_mask), [`lse_vmem_shape`](configs.md#RpaConfigs.lse_vmem_shape), [`bkv_stride`](configs.md#RpaConfigs.bkv_stride), [`_stitch_prefill_lane`](stitch_utils.md#_stitch_prefill_lane), [`o_bytes_per_token`](configs.md#RpaConfigs.o_bytes_per_token), [`q_bytes_per_token`](configs.md#RpaConfigs.q_bytes_per_token), [`acc_scratch_shape`](configs.md#RpaConfigs.acc_scratch_shape), [`aligned_q_head_dim`](configs.md#RpaConfigs.aligned_q_head_dim), [`lm_scratch_shape`](configs.md#RpaConfigs.lm_scratch_shape), [`calculate_compute_buffer_time`](wrapper.md#calculate_block_sizes.calculate_compute_buffer_time)

### <a id="RpaCase"></a>`RpaCase`  ·  implements/extends StrEnum
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py:103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L103) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- doc: Represents the different cases for Ragged Paged Attention.
- signature: `class RpaCase(enum.StrEnum):`
- members:
  - <a id="RpaCase.get_range"></a>`get_range(self, distribution: jax.Array)` — [`L127`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L127)
  - <a id="RpaCase.symbol"></a>`symbol(self)` — [`L118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L118)
  - <a id="RpaCase.DECODE"></a>`DECODE` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L113)
  - <a id="RpaCase.MIXED"></a>`MIXED` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L115)
  - <a id="RpaCase.PREFILL"></a>`PREFILL` — [`L114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L114)
- used by: [`ragged_paged_attention`](wrapper.md#ragged_paged_attention), [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`_attention_schedule_capacity`](../../../runner/tpu_runner.md#TPUModelRunner._attention_schedule_capacity), [`run_rpa_kernel`](wrapper.md#ragged_paged_attention.run_rpa_kernel), [`get_kernel_name`](kernel.md#get_kernel_name), [`bkv_p_cache`](configs.md#RpaConfigs.bkv_p_cache), [`seq_range`](configs.md#RpaConfigs.seq_range), [`fuse_accum`](configs.md#RpaConfigs.fuse_accum), [`mode`](configs.md#RpaConfigs.mode)

### <a id="RpaConfigs"></a>`RpaConfigs`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py:221`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L221) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- signature: `class RpaConfigs:`
- members:
  - <a id="RpaConfigs.acc_scratch_shape"></a>`acc_scratch_shape(self)` — [`L533`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L533)
  - <a id="RpaConfigs.aligned_kv_head_dim"></a>`aligned_kv_head_dim(self)` — [`L369`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L369) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.aligned_num_kv_heads_x2"></a>`aligned_num_kv_heads_x2(self)` — [`L388`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L388)
  - <a id="RpaConfigs.aligned_num_q_heads_per_kv_head"></a>`aligned_num_q_heads_per_kv_head(self)` — [`L395`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L395)
  - <a id="RpaConfigs.aligned_q_head_dim"></a>`aligned_q_head_dim(self)` — [`L352`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L352)
  - <a id="RpaConfigs.batch_size"></a>`batch_size(self)` — [`L243`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L243) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.bkv_p"></a>`bkv_p(self)` — [`L326`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L326)
  - <a id="RpaConfigs.bkv_p_cache"></a>`bkv_p_cache(self)` — [`L330`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L330) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.bkv_p_new"></a>`bkv_p_new(self)` — [`L336`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L336) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.bkv_stride"></a>`bkv_stride(self)` — [`L344`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L344)
  - <a id="RpaConfigs.bkv_sz"></a>`bkv_sz(self)` — [`L239`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L239) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.bq_c_sz"></a>`bq_c_sz(self)` — [`L235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L235)
  - <a id="RpaConfigs.bq_sz"></a>`bq_sz(self)` — [`L231`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L231)
  - <a id="RpaConfigs.compute_kv_head_dim"></a>`compute_kv_head_dim(self)` — [`L358`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L358) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.dma_kv_new_size"></a>`dma_kv_new_size(self)` — [`L500`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L500) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.fuse_accum"></a>`fuse_accum(self)` — [`L407`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L407)
  - <a id="RpaConfigs.kv_bytes_per_token"></a>`kv_bytes_per_token(self)` — [`L411`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L411) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.kv_hbm_stride"></a>`kv_hbm_stride(self)` — [`L400`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L400) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.kv_token_align"></a>`kv_token_align(self)` — [`L459`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L459) — DMA token granularity: the 128-lane tile for SEQ_ALONG_LANE, else 1. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.kv_vmem_lanes"></a>`kv_vmem_lanes(self)` — [`L471`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L471) — Lane-dim size of the KV VMEM buffer; SEQ_ALONG_LANE only.
  - <a id="RpaConfigs.kv_vmem_shape"></a>`kv_vmem_shape(self)` — [`L482`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L482) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.lm_scratch_shape"></a>`lm_scratch_shape(self)` — [`L511`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L511)
  - <a id="RpaConfigs.lse_vmem_shape"></a>`lse_vmem_shape(self)` — [`L520`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L520)
  - <a id="RpaConfigs.max_schedule_size_multiplier"></a>`max_schedule_size_multiplier(self)` — [`L541`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L541)
  - <a id="RpaConfigs.max_steps_ub"></a>`max_steps_ub(self)` — [`L263`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L263) — Get maximum upper bound of kernel steps based on SMEM limit.
  - <a id="RpaConfigs.o_bytes_per_token"></a>`o_bytes_per_token(self)` — [`L434`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L434)
  - <a id="RpaConfigs.page_window_entries"></a>`page_window_entries(self)` — [`L312`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L312)
  - <a id="RpaConfigs.page_window_seqs"></a>`page_window_seqs(self)` — [`L303`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L303) — Sequences per page_indices DMA window: a power of two dividing num_seqs.
  - <a id="RpaConfigs.page_window_slot_len"></a>`page_window_slot_len(self)` — [`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L316) — SMEM entries per window slot: lane-aligned, plus a lane group of slack
  - <a id="RpaConfigs.q_bytes_per_token"></a>`q_bytes_per_token(self)` — [`L421`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L421)
  - <a id="RpaConfigs.q_vmem_shape"></a>`q_vmem_shape(self)` — [`L447`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L447)
  - <a id="RpaConfigs.seq_range"></a>`seq_range(self, distribution: jax.Array | jax.Ref)` — [`L246`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L246) — Sequences this kernel call schedules.
  - <a id="RpaConfigs.validate_inputs"></a>`validate_inputs(self, q: jax.Array, k: jax.Array, v: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array)` — [`L545`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L545) — Validate inputs to the RPA kernel statically. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.block"></a>`block` — [`L222`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L222) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.mode"></a>`mode` — [`L225`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L225)
  - <a id="RpaConfigs.model"></a>`model` — [`L223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L223) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.serve"></a>`serve` — [`L224`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L224) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="RpaConfigs.vmem_limit_bytes"></a>`vmem_limit_bytes` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L226)
- uses (calls/refs, reference-scoped): [`KVLayout`](configs.md#KVLayout), [`SEQ_ALONG_LANE`](configs.md#KVLayout.SEQ_ALONG_LANE), [`kv_layout`](configs.md#ServingConfigs.kv_layout), [`align_to`](utils.md#align_to), [`num_kv_heads`](configs.md#ModelConfigs.num_kv_heads), [`page_size`](configs.md#ServingConfigs.page_size), [`packing_kv`](configs.md#ServingConfigs.packing_kv), [`HEAD_ALONG_SUBLANE`](configs.md#KVLayout.HEAD_ALONG_SUBLANE), [`dtype_kv`](configs.md#ServingConfigs.dtype_kv), [`RpaCase`](configs.md#RpaCase), [`pages_per_seq`](configs.md#ServingConfigs.pages_per_seq), [`AttentionScope`](configs.md#AttentionScope), [`get_dtype_packing`](utils.md#get_dtype_packing), [`dtype_out`](configs.md#ServingConfigs.dtype_out), [`head_dim`](configs.md#ModelConfigs.head_dim), [`attention_scope`](configs.md#ServingConfigs.attention_scope), [`batch_size`](configs.md#BlockSizes.batch_size), [`packing_q`](configs.md#ServingConfigs.packing_q), [`bq_sz`](configs.md#BlockSizes.bq_sz), [`scale_channels`](configs.md#ServingConfigs.scale_channels), [`DECODE`](configs.md#RpaCase.DECODE), [`BlockSizes`](configs.md#BlockSizes), [`num_q_heads_per_kv_head`](configs.md#ModelConfigs.num_q_heads_per_kv_head), [`per_token_scale`](configs.md#ServingConfigs.per_token_scale), [`bkv_sz`](configs.md#BlockSizes.bkv_sz), [`dtype_q`](configs.md#ServingConfigs.dtype_q), [`max_decode_bkv_p_new`](configs.md#ServingConfigs.max_decode_bkv_p_new), [`sliding_window`](configs.md#ModelConfigs.sliding_window), [`MIXED`](configs.md#RpaCase.MIXED), [`num_seqs`](configs.md#ServingConfigs.num_seqs), [`scale_v`](configs.md#ServingConfigs.scale_v), [`cp_group_size`](configs.md#ServingConfigs.cp_group_size), [`ModelConfigs`](configs.md#ModelConfigs), [`ServingConfigs`](configs.md#ServingConfigs), [`FULL`](configs.md#AttentionScope.FULL), [`PREFILL`](configs.md#RpaCase.PREFILL), [`get_dtype_bits`](utils.md#get_dtype_bits), [`scale_k`](configs.md#ServingConfigs.scale_k), [`bq_c_sz`](configs.md#BlockSizes.bq_c_sz), [`has_bank_conflicts`](utils.md#has_bank_conflicts)  (+3 more)
- used by: [`rpa_body`](kernel.md#rpa_body), [`k_loop`](schedule_cp.md#CPMetadataComputer.k_loop), [`k_loop`](schedule.md#BaseMetadataComputer.k_loop), [`_mask_out_steps`](schedule.md#_mask_out_steps), [`body`](schedule.md#_compute_waits.body), [`fill_dma_kv_new`](schedule_cp.md#CPMetadataComputer.fill_dma_kv_new), [`fill_dma_kv_new`](schedule.md#BaseMetadataComputer.fill_dma_kv_new), [`fetch_compute_metadata`](kernel.md#fetch_compute_metadata), [`create_allocs`](kernel.md#create_allocs), [`flash_attention_qk_softmax`](flash_attention.md#flash_attention_qk_softmax), [`flash_attention_pv`](flash_attention.md#flash_attention_pv), [`run_rpa_kernel`](wrapper.md#ragged_paged_attention.run_rpa_kernel), [`create_shape_dtype`](schedule.md#RpaSchedule.create_shape_dtype), [`fetch_stitch_metadata`](kernel.md#fetch_stitch_metadata), [`get_kernel_name`](kernel.md#get_kernel_name), [`q_loop`](schedule.md#BaseMetadataComputer.q_loop), [`get_rpa_schedule`](schedule.md#BaseMetadataComputer.get_rpa_schedule), [`generate_rpa_metadata`](schedule.md#generate_rpa_metadata), [`get_scale_factors`](kernel.md#get_scale_factors), [`rpa_kernel`](kernel.md#rpa_kernel), [`store_new_kv_lane`](stitch_utils.md#store_new_kv_lane), [`_kv_store_fence`](kernel.md#rpa_body._kv_store_fence), [`calculate_and_store_out`](kernel.md#calculate_and_store_out), [`rpa_metadata_schedule_kernel`](schedule.md#rpa_metadata_schedule_kernel), [`seq_loop`](schedule.md#BaseMetadataComputer.seq_loop), [`strided_load_bkv`](kernel.md#strided_load_bkv), [`copy_in`](bref_override.md#KVBufferedRefHeadAlongSublane.copy_in), [`get_rpa_schedule`](schedule_cp.md#CPMetadataComputer.get_rpa_schedule), [`generate_mask`](kernel.md#generate_mask), [`stitch_new_kv_lane`](stitch_utils.md#stitch_new_kv_lane), [`copy_out`](bref_override.md#KVBufferedRefSeqAlongLane.copy_out), [`advance_carry`](schedule.md#BaseMetadataComputer.advance_carry), [`flush_to_hbm`](schedule.md#flush_to_hbm), [`_stitch_prefill_lane`](stitch_utils.md#_stitch_prefill_lane), [`page_indices_offset`](schedule.md#BaseMetadataComputer.page_indices_offset), [`_accum`](kernel.md#calculate_and_store_out._accum), [`_compute_waits`](schedule.md#_compute_waits), [`_run`](kernel.md#rpa_kernel.ragged_paged_attention_pipeline._run), [`compute`](schedule.md#BaseMetadataComputer.compute), [`copy_out`](bref_override.md#KVBufferedRefHeadAlongSublane.copy_out)  (+28 more)

### <a id="ServingConfigs"></a>`ServingConfigs`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py:152`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L152)
- doc: Serving config that can change depending on use cases.
- signature: `class ServingConfigs:`
- members:
  - <a id="ServingConfigs.max_decode_bkv_p_new"></a>`max_decode_bkv_p_new(self)` — [`L187`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L187)
  - <a id="ServingConfigs.packing_kv"></a>`packing_kv(self)` — [`L207`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L207) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="ServingConfigs.packing_q"></a>`packing_q(self)` — [`L203`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L203)
  - <a id="ServingConfigs.page_size_log2"></a>`page_size_log2(self)` — [`L195`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L195)
  - <a id="ServingConfigs.page_size_mask"></a>`page_size_mask(self)` — [`L199`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L199)
  - <a id="ServingConfigs.pages_per_seq"></a>`pages_per_seq(self)` — [`L191`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L191)
  - <a id="ServingConfigs.scale_channels"></a>`scale_channels(self)` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L211)
  - <a id="ServingConfigs.attention_scope"></a>`attention_scope` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L173)
  - <a id="ServingConfigs.cp_group_size"></a>`cp_group_size` — [`L172`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L172)
  - <a id="ServingConfigs.decode_query_size"></a>`decode_query_size` — [`L171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L171)
  - <a id="ServingConfigs.dtype_kv"></a>`dtype_kv` — [`L160`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L160) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="ServingConfigs.dtype_out"></a>`dtype_out` — [`L161`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L161)
  - <a id="ServingConfigs.dtype_q"></a>`dtype_q` — [`L159`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L159)
  - <a id="ServingConfigs.kv_layout"></a>`kv_layout` — [`L167`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L167) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="ServingConfigs.mask_invalid_v"></a>`mask_invalid_v` — [`L176`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L176)
  - <a id="ServingConfigs.max_schedule_size_multiplier"></a>`max_schedule_size_multiplier` — [`L169`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L169)
  - <a id="ServingConfigs.num_page_indices"></a>`num_page_indices` — [`L158`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L158)
  - <a id="ServingConfigs.num_seqs"></a>`num_seqs` — [`L155`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L155)
  - <a id="ServingConfigs.page_indices_window_size"></a>`page_indices_window_size` — [`L170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L170)
  - <a id="ServingConfigs.page_size"></a>`page_size` — [`L156`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L156) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="ServingConfigs.per_token_scale"></a>`per_token_scale` — [`L162`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L162)
  - <a id="ServingConfigs.per_token_scale_dtype"></a>`per_token_scale_dtype` — [`L163`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L163)
  - <a id="ServingConfigs.return_lse"></a>`return_lse` — [`L174`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L174)
  - <a id="ServingConfigs.scale_k"></a>`scale_k` — [`L165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L165)
  - <a id="ServingConfigs.scale_q"></a>`scale_q` — [`L164`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L164)
  - <a id="ServingConfigs.scale_v"></a>`scale_v` — [`L166`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L166)
  - <a id="ServingConfigs.skip_kv_update"></a>`skip_kv_update` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L175)
  - <a id="ServingConfigs.smem_fraction_limit_for_schedule_generation"></a>`smem_fraction_limit_for_schedule_generation` — [`L168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L168)
  - <a id="ServingConfigs.total_q_tokens"></a>`total_q_tokens` — [`L157`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L157)
- protocol/private: <a id="ServingConfigs.__post_init__"></a>`__post_init__`[`L178`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L178)
- uses (calls/refs, reference-scoped): [`KVLayout`](configs.md#KVLayout), [`SEQ_ALONG_LANE`](configs.md#KVLayout.SEQ_ALONG_LANE), [`HEAD_ALONG_SUBLANE`](configs.md#KVLayout.HEAD_ALONG_SUBLANE), [`AttentionScope`](configs.md#AttentionScope), [`get_dtype_packing`](utils.md#get_dtype_packing), [`FULL`](configs.md#AttentionScope.FULL)
- used by: [`serve`](configs.md#RpaConfigs.serve), [`ragged_paged_attention`](wrapper.md#ragged_paged_attention), [`rpa_body`](kernel.md#rpa_body), [`k_loop`](schedule_cp.md#CPMetadataComputer.k_loop), [`k_loop`](schedule.md#BaseMetadataComputer.k_loop), [`validate_inputs`](configs.md#RpaConfigs.validate_inputs), [`body`](schedule.md#_compute_waits.body), [`fill_dma_kv_new`](schedule_cp.md#CPMetadataComputer.fill_dma_kv_new), [`calculate_block_sizes`](wrapper.md#calculate_block_sizes), [`fill_dma_kv_new`](schedule.md#BaseMetadataComputer.fill_dma_kv_new), [`fetch_compute_metadata`](kernel.md#fetch_compute_metadata), [`bkv_p_new`](configs.md#RpaConfigs.bkv_p_new), [`create_allocs`](kernel.md#create_allocs), [`flash_attention_qk_softmax`](flash_attention.md#flash_attention_qk_softmax), [`aligned_kv_head_dim`](configs.md#RpaConfigs.aligned_kv_head_dim), [`find_best_block_sizes`](wrapper.md#calculate_block_sizes.find_best_block_sizes), [`flash_attention_pv`](flash_attention.md#flash_attention_pv), [`kv_vmem_shape`](configs.md#RpaConfigs.kv_vmem_shape), [`max_steps_ub`](configs.md#RpaConfigs.max_steps_ub), [`fetch_stitch_metadata`](kernel.md#fetch_stitch_metadata), [`get_kernel_name`](kernel.md#get_kernel_name), [`q_loop`](schedule.md#BaseMetadataComputer.q_loop), [`get_rpa_schedule`](schedule.md#BaseMetadataComputer.get_rpa_schedule), [`compute_kv_head_dim`](configs.md#RpaConfigs.compute_kv_head_dim), [`calculate_vmem_usage`](wrapper.md#calculate_block_sizes.calculate_vmem_usage), [`get_scale_factors`](kernel.md#get_scale_factors), [`kv_bytes_per_token`](configs.md#RpaConfigs.kv_bytes_per_token), [`rpa_kernel`](kernel.md#rpa_kernel), [`store_new_kv_lane`](stitch_utils.md#store_new_kv_lane), [`_kv_store_fence`](kernel.md#rpa_body._kv_store_fence), [`aligned_num_q_heads_per_kv_head`](configs.md#RpaConfigs.aligned_num_q_heads_per_kv_head), [`kv_hbm_stride`](configs.md#RpaConfigs.kv_hbm_stride), [`q_vmem_shape`](configs.md#RpaConfigs.q_vmem_shape), [`calculate_and_store_out`](kernel.md#calculate_and_store_out), [`strided_load_bkv`](kernel.md#strided_load_bkv), [`copy_in`](bref_override.md#KVBufferedRefHeadAlongSublane.copy_in), [`get_rpa_schedule`](schedule_cp.md#CPMetadataComputer.get_rpa_schedule), [`aligned_num_kv_heads_x2`](configs.md#RpaConfigs.aligned_num_kv_heads_x2), [`lse_vmem_shape`](configs.md#RpaConfigs.lse_vmem_shape), [`bkv_p`](configs.md#RpaConfigs.bkv_p)  (+14 more)

## Module values
- <a id="NUM_INPUT_SLOTS"></a>`NUM_INPUT_SLOTS` — [`L143`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L143)
- <a id="NUM_OUTPUT_SLOTS"></a>`NUM_OUTPUT_SLOTS` — [`L148`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/configs.py#L148)

