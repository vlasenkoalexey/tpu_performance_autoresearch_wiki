---
title: 'Module: src/vllm_torchtpu/kernels/mla/v2/tuned_params.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/v2/tuned_params.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.v2.tuned_params`/
symbols:
  TuningKey: TuningKey#
  TunableParams: TunableParams#
  TunableParams.num_kv_pages_per_block: TunableParams#num_kv_pages_per_block.
  TunableParams.num_queries_per_block: TunableParams#num_queries_per_block.
  TunableParams.vmem_limit_bytes: TunableParams#vmem_limit_bytes.
  TuningKey.case: TuningKey#case.
  TuningKey.max_num_tokens: TuningKey#max_num_tokens.
  TuningKey.actual_num_q_heads: TuningKey#actual_num_q_heads.
  TuningKey.actual_lkv_dim: TuningKey#actual_lkv_dim.
  TuningKey.actual_r_dim: TuningKey#actual_r_dim.
  TuningKey.page_size_per_kv_packing: TuningKey#page_size_per_kv_packing.
  TuningKey.kv_packing: TuningKey#kv_packing.
  TuningKey.max_num_seqs: TuningKey#max_num_seqs.
  TuningKey.pages_per_seq: TuningKey#pages_per_seq.
  tuned_params_mapping.tuned_params_mapping: tuned_params_mapping.tuned_params_mapping.
  TunableParams.decode_batch_size: TunableParams#decode_batch_size.
  TunableParams.q_split: TunableParams#q_split.
  TuningKey.kv_dtype: TuningKey#kv_dtype.
  get_tuned_params: get_tuned_params().
  TuningKey.q_dtype: TuningKey#q_dtype.
  TuningKey.s_dtype: TuningKey#s_dtype.
  TuningKey.soft_cap: TuningKey#soft_cap.
  TuningKey.chunk_prefill_size: TuningKey#chunk_prefill_size.
  TuningKey.sliding_window: TuningKey#sliding_window.
  TuningKey.p_same_dtype_as_v: TuningKey#p_same_dtype_as_v.
  logger: logger.
---
# Module: [`src/vllm_torchtpu/kernels/mla/v2/tuned_params.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py)

## Classes
### <a id="TunableParams"></a>`TunableParams`
- def: [`src/vllm_torchtpu/kernels/mla/v2/tuned_params.py:69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L69) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- signature: `class TunableParams:`
- members:
  - <a id="TunableParams.decode_batch_size"></a>`decode_batch_size` — [`L76`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L76) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TunableParams.num_kv_pages_per_block"></a>`num_kv_pages_per_block` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L72) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TunableParams.num_queries_per_block"></a>`num_queries_per_block` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L73) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TunableParams.q_split"></a>`q_split` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L80) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TunableParams.vmem_limit_bytes"></a>`vmem_limit_bytes` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L74) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- used by: [`tuned_params_mapping`](tuned_params.md#tuned_params_mapping.tuned_params_mapping), [`_mla_ragged_paged_attention`](../../../layers/core/attention_interface.md#mla_attention._mla_ragged_paged_attention), [`get_tuned_params`](tuned_params.md#get_tuned_params)

### <a id="TuningKey"></a>`TuningKey`
- def: [`src/vllm_torchtpu/kernels/mla/v2/tuned_params.py:23`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L23) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- signature: `class TuningKey:`
- members:
  - <a id="TuningKey.actual_lkv_dim"></a>`actual_lkv_dim` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L31) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.actual_num_q_heads"></a>`actual_num_q_heads` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L29) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.actual_r_dim"></a>`actual_r_dim` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L33) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.case"></a>`case` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L26) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.chunk_prefill_size"></a>`chunk_prefill_size` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L61)
  - <a id="TuningKey.kv_dtype"></a>`kv_dtype` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L34) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.kv_packing"></a>`kv_packing` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L41) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.max_num_seqs"></a>`max_num_seqs` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L46) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.max_num_tokens"></a>`max_num_tokens` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L27) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.p_same_dtype_as_v"></a>`p_same_dtype_as_v` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L65)
  - <a id="TuningKey.page_size_per_kv_packing"></a>`page_size_per_kv_packing` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L38) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.pages_per_seq"></a>`pages_per_seq` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L49) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
  - <a id="TuningKey.q_dtype"></a>`q_dtype` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L37)
  - <a id="TuningKey.s_dtype"></a>`s_dtype` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L52)
  - <a id="TuningKey.sliding_window"></a>`sliding_window` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L62)
  - <a id="TuningKey.soft_cap"></a>`soft_cap` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L55)
- used by: [`tuned_params_mapping`](tuned_params.md#tuned_params_mapping.tuned_params_mapping), [`_mla_ragged_paged_attention`](../../../layers/core/attention_interface.md#mla_attention._mla_ragged_paged_attention), [`get_tuned_params`](tuned_params.md#get_tuned_params)

## Functions
- <a id="get_tuned_params"></a>`get_tuned_params(tuning_key: TuningKey)` — [`L1348`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L1348) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)

## Module values
- <a id="logger"></a>`logger` — [`L19`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L19)
- <a id="tuned_params_mapping.tuned_params_mapping"></a>`tuned_params_mapping` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/tuned_params.py#L83) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)

