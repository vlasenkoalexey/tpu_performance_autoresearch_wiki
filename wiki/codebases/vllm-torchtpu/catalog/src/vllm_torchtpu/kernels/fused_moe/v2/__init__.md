---
title: 'Module: src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.fused_moe.v2`/
symbols:
  WeightFormat: WeightFormat.
  ACT_FNS: ACT_FNS.
  ALIGNMENT_SLOT_FIELD: ALIGNMENT_SLOT_FIELD.
  AXIS: AXIS.
  PACK4: PACK4.
  HIDDEN_LANE_BLOCK: HIDDEN_LANE_BLOCK.
  HIDDEN_MAX_BLOCKS: HIDDEN_MAX_BLOCKS.
  MIN_GENERATION: MIN_GENERATION.
  MAX_NBUF: MAX_NBUF.
  ROWBLK: ROWBLK.
  U32_SUBLANE_TILE: U32_SUBLANE_TILE.
  WIDEN_KCHUNK: WIDEN_KCHUNK.
  chip_generation: chip_generation.
  WEIGHT_FORMS: WEIGHT_FORMS.
  WEIGHT_FORMAT_NAMES: WEIGHT_FORMAT_NAMES.
  weight_form: weight_form.
  weight_format_of_dtype: weight_format_of_dtype.
  routing_block: routing_block.
  ragged_stride_bound: ragged_stride_bound.
  vmem_estimate_bytes: vmem_estimate_bytes.
  fit_weight_slots: fit_weight_slots.
  vmem_limit: vmem_limit.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py)

## Module values
- <a id="ACT_FNS"></a>`ACT_FNS` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L24)
- <a id="ALIGNMENT_SLOT_FIELD"></a>`ALIGNMENT_SLOT_FIELD` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L25)
- <a id="AXIS"></a>`AXIS` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L26)
- <a id="HIDDEN_LANE_BLOCK"></a>`HIDDEN_LANE_BLOCK` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L28)
- <a id="HIDDEN_MAX_BLOCKS"></a>`HIDDEN_MAX_BLOCKS` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L29)
- <a id="MAX_NBUF"></a>`MAX_NBUF` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L33)
- <a id="MIN_GENERATION"></a>`MIN_GENERATION` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L30)
- <a id="PACK4"></a>`PACK4` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L27)
- <a id="ROWBLK"></a>`ROWBLK` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L34)
- <a id="U32_SUBLANE_TILE"></a>`U32_SUBLANE_TILE` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L35)
- <a id="WEIGHT_FORMAT_NAMES"></a>`WEIGHT_FORMAT_NAMES` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L43)
- <a id="WEIGHT_FORMS"></a>`WEIGHT_FORMS` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L42)
- <a id="WIDEN_KCHUNK"></a>`WIDEN_KCHUNK` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L36)
- <a id="WeightFormat"></a>`WeightFormat` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L41) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
- <a id="__all__"></a>`__all__` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L58)
- <a id="chip_generation"></a>`chip_generation` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L37)
- <a id="fit_weight_slots"></a>`fit_weight_slots` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L49)
- <a id="ragged_stride_bound"></a>`ragged_stride_bound` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L47)
- <a id="routing_block"></a>`routing_block` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L46)
- <a id="vmem_estimate_bytes"></a>`vmem_estimate_bytes` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L48)
- <a id="vmem_limit"></a>`vmem_limit` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L50)
- <a id="weight_form"></a>`weight_form` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L44)
- <a id="weight_format_of_dtype"></a>`weight_format_of_dtype` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/__init__.py#L45)

