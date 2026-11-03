---
title: 'Module: src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.sample.top_k_top_p`/
symbols:
  apply_top_k_top_p: apply_top_k_top_p().
  _float32_bsearch: _float32_bsearch().
  topk_mask: topk_mask().
  topp_mask: topp_mask().
  apply_top_k_top_p_candidates: apply_top_k_top_p_candidates().
  CANDIDATE_BLOCK: CANDIDATE_BLOCK.
  MASKED_LOGIT_VALUE: MASKED_LOGIT_VALUE.
  _monotonic_int32_to_float32: _monotonic_int32_to_float32().
  _float32_bsearch.int32_predicate: _float32_bsearch().int32_predicate().
  _monotonic_int32_to_float32_bit_pattern: _monotonic_int32_to_float32_bit_pattern().
  _int32_bsearch: _int32_bsearch().
  topk_mask.predicate: topk_mask().predicate().
  topp_mask.predicate: topp_mask().predicate().
---
# Module: [`src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py)

## Functions
- <a id="_float32_bsearch"></a>`_float32_bsearch(batch_shape: Sequence[int], predicate: Callable[[torch.Tensor], torch.Tensor], device: torch.device)` — [`L119`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L119) — Binary search on finite float32 numbers.
- <a id="_int32_bsearch"></a>`_int32_bsearch(batch_shape: Sequence[int], predicate: Callable[[torch.Tensor], torch.Tensor], device: torch.device)` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L33) — Batched binary search over int32 values.
- <a id="_monotonic_int32_to_float32"></a>`_monotonic_int32_to_float32(x: torch.Tensor)` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L103) — Converts an int32 to a float32 with consistent ordering.
- <a id="_monotonic_int32_to_float32_bit_pattern"></a>`_monotonic_int32_to_float32_bit_pattern(x: torch.Tensor)` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L73) — Converts an int32 to a float32 bit pattern with consistent ordering.
- <a id="apply_top_k_top_p"></a>`apply_top_k_top_p(logits: torch.Tensor, top_k: torch.Tensor, top_p: torch.Tensor, topk_candidates: int = 0)` — [`L248`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L248)
- <a id="apply_top_k_top_p_candidates"></a>`apply_top_k_top_p_candidates(logits: torch.Tensor, top_k: torch.Tensor, top_p: torch.Tensor, num_blocks: int)` — [`L265`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L265) — Applies top-k then top-p using only the blocks with the largest maxima.
- <a id="_float32_bsearch.int32_predicate"></a>`int32_predicate(x: torch.Tensor)` — [`L142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L142)
- <a id="topk_mask.predicate"></a>`predicate(threshold: torch.Tensor)` — [`L191`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L191)
- <a id="topp_mask.predicate"></a>`predicate(threshold: torch.Tensor)` — [`L235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L235)
- <a id="topk_mask"></a>`topk_mask(logits: torch.Tensor, k: torch.Tensor, replace_val: float = MASKED_LOGIT_VALUE)` — [`L165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L165) — Sets everything to replace_val, except the top k values per batch element.
- <a id="topp_mask"></a>`topp_mask(logits: torch.Tensor, p: torch.Tensor, replace_val: float = MASKED_LOGIT_VALUE)` — [`L203`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L203) — Applies top-p masking to logits.

## Module values
- <a id="CANDIDATE_BLOCK"></a>`CANDIDATE_BLOCK` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L30)
- <a id="MASKED_LOGIT_VALUE"></a>`MASKED_LOGIT_VALUE` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/top_k_top_p.py#L24)

