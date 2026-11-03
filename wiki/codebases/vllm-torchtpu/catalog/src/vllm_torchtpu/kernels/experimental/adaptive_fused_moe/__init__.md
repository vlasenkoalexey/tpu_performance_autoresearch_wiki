---
title: 'Module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.adaptive_fused_moe`/
symbols:
  ACT_FNS: ACT_FNS.
  ALIGNMENT_SLOT_FIELD: ALIGNMENT_SLOT_FIELD.
  AXIS: AXIS.
  PACK4: PACK4.
  HIDDEN_LANE_BLOCK: HIDDEN_LANE_BLOCK.
  MIN_GENERATION: MIN_GENERATION.
  NBUF: NBUF.
  ROWBLK: ROWBLK.
  U32_SUBLANE_TILE: U32_SUBLANE_TILE.
  WIDEN_KCHUNK: WIDEN_KCHUNK.
  chip_generation: chip_generation.
  WeightFormat: WeightFormat.
  WEIGHT_FORMS: WEIGHT_FORMS.
  WEIGHT_FORMAT_NAMES: WEIGHT_FORMAT_NAMES.
  weight_form: weight_form.
  weight_format_of_dtype: weight_format_of_dtype.
  routing_block: routing_block.
  ragged_stride_bound: ragged_stride_bound.
  vmem_estimate_bytes: vmem_estimate_bytes.
  vmem_limit: vmem_limit.
  select_weight_buffers: select_weight_buffers.
  WeightBufferPlan: WeightBufferPlan.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py)

## Module values
- <a id="ACT_FNS"></a>`ACT_FNS` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L28)
- <a id="ALIGNMENT_SLOT_FIELD"></a>`ALIGNMENT_SLOT_FIELD` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L29)
- <a id="AXIS"></a>`AXIS` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L30)
- <a id="HIDDEN_LANE_BLOCK"></a>`HIDDEN_LANE_BLOCK` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L32)
- <a id="MIN_GENERATION"></a>`MIN_GENERATION` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L33)
- <a id="NBUF"></a>`NBUF` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L34)
- <a id="PACK4"></a>`PACK4` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L31)
- <a id="ROWBLK"></a>`ROWBLK` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L35)
- <a id="U32_SUBLANE_TILE"></a>`U32_SUBLANE_TILE` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L36)
- <a id="WEIGHT_FORMAT_NAMES"></a>`WEIGHT_FORMAT_NAMES` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L44)
- <a id="WEIGHT_FORMS"></a>`WEIGHT_FORMS` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L43)
- <a id="WIDEN_KCHUNK"></a>`WIDEN_KCHUNK` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L37)
- <a id="WeightBufferPlan"></a>`WeightBufferPlan` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L52)
- <a id="WeightFormat"></a>`WeightFormat` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L42)
- <a id="__all__"></a>`__all__` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L60)
- <a id="chip_generation"></a>`chip_generation` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L38)
- <a id="ragged_stride_bound"></a>`ragged_stride_bound` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L48)
- <a id="routing_block"></a>`routing_block` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L47)
- <a id="select_weight_buffers"></a>`select_weight_buffers` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L51)
- <a id="vmem_estimate_bytes"></a>`vmem_estimate_bytes` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L49)
- <a id="vmem_limit"></a>`vmem_limit` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L50)
- <a id="weight_form"></a>`weight_form` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L45)
- <a id="weight_format_of_dtype"></a>`weight_format_of_dtype` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/__init__.py#L46)

