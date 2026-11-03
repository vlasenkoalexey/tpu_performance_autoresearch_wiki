---
title: 'Module: src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.sample.rejection_sampler`/
symbols:
  RejectionSampler.forward: RejectionSampler#forward().
  RejectionSampler.synthetic_mode: RejectionSampler#synthetic_mode.
  _random_rejection_sample_with_segment: _random_rejection_sample_with_segment().
  RejectionSampler.synthetic_conditional_rates: RejectionSampler#synthetic_conditional_rates.
  logger: logger.
  _greedy_rejection_sample: _greedy_rejection_sample().
  PLACEHOLDER_TOKEN_ID: PLACEHOLDER_TOKEN_ID.
  _greedy_rejection_sample_with_segment: _greedy_rejection_sample_with_segment().
  _greedy_rejection_sample_from_argmax: _greedy_rejection_sample_from_argmax().
  RejectionSampler: RejectionSampler#
  RejectionSampler.__call__: RejectionSampler#__call__().
  TEMPERATURE_EPS: TEMPERATURE_EPS.
  RejectionSampler.__init__: RejectionSampler#__init__().
  _get_segment_info: _get_segment_info().
---
# Module: [`src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py)

## Classes
### <a id="RejectionSampler"></a>`RejectionSampler`
- def: [`src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py:35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L35)
- doc: Torch-based rejection sampler for speculative decoding on TPU.
- signature: `class RejectionSampler:`
- members:
  - <a id="RejectionSampler.forward"></a>`forward(self, draft_token_ids: torch.Tensor, num_draft_tokens: torch.Tensor, target_logits: torch.Tensor | None, bonus_token_ids: torch.Tensor, segment_ids: torch.Tensor, group_indices: torch.Tensor, max_draft_tokens: int, temperatures: torch.Tensor | None = None, top_k: torch.Tensor | None = None, top_p: torch.Tensor | None = None, accept_u: torch.Tensor | None = None, recover_u: torch.Tensor | None = None, do_sampling: bool = False, topk_candidates: int = 0, target_argmax: torch.Tensor | None = None, apply_topk_topp: bool = True, draft_probs: torch.Tensor | None = None)` — [`L97`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L97) — Performs rejection sampling for speculative decoding. — documented in [vllm-layer-adapters](../../../../../../concepts/vllm-layer-adapters.md)
  - <a id="RejectionSampler.synthetic_conditional_rates"></a>`synthetic_conditional_rates` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L43)
  - <a id="RejectionSampler.synthetic_mode"></a>`synthetic_mode` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L55) — documented in [vllm-layer-adapters](../../../../../../concepts/vllm-layer-adapters.md)
- protocol/private: <a id="RejectionSampler.__call__"></a>`__call__`[`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L57), <a id="RejectionSampler.__init__"></a>`__init__`[`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L38)
- uses (calls/refs, reference-scoped): [`_random_rejection_sample_with_segment`](rejection_sampler.md#_random_rejection_sample_with_segment), [`logger`](rejection_sampler.md#logger), [`_greedy_rejection_sample_from_argmax`](rejection_sampler.md#_greedy_rejection_sample_from_argmax), [`_greedy_rejection_sample_with_segment`](rejection_sampler.md#_greedy_rejection_sample_with_segment)
- used by: [`_sample_spec_verify_chunk`](../../../runner/tpu_runner.md#TPUModelRunner._sample_spec_verify_chunk), [`_precompile_rejection_sampler`](../../../runner/tpu_runner.md#TPUModelRunner._precompile_rejection_sampler), [`_num_static_verify_reqs`](../../../runner/tpu_runner.md#TPUModelRunner._num_static_verify_reqs), [`rejection_sampler`](../../../runner/tpu_runner.md#TPUModelRunner.rejection_sampler), [`_precompile_top_token_verify`](../../../runner/tpu_runner.md#TPUModelRunner._precompile_top_token_verify)

## Functions
- <a id="_get_segment_info"></a>`_get_segment_info(num_draft_tokens: torch.Tensor, total_tokens: int)` — [`L244`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L244) — Helper to create segment IDs and per-segment indices.
- <a id="_greedy_rejection_sample"></a>`_greedy_rejection_sample(draft_token_ids: torch.Tensor, target_logits_argmax: torch.Tensor, num_draft_tokens: torch.Tensor, bonus_token_ids: torch.Tensor, segment_ids: torch.Tensor, group_indices: torch.Tensor, max_draft_tokens: int, accept_u: torch.Tensor | None, synthetic_conditional_rates: torch.Tensor | None, synthetic_mode: bool)` — [`L329`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L329)
- <a id="_greedy_rejection_sample_from_argmax"></a>`_greedy_rejection_sample_from_argmax(draft_token_ids: torch.Tensor, target_argmax: torch.Tensor, num_draft_tokens: torch.Tensor, bonus_token_ids: torch.Tensor, segment_ids: torch.Tensor, group_indices: torch.Tensor, max_draft_tokens: int, accept_u: torch.Tensor | None, synthetic_conditional_rates: torch.Tensor | None, synthetic_mode: bool)` — [`L302`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L302) — Greedy validation from the target's argmax tokens, without logits.
- <a id="_greedy_rejection_sample_with_segment"></a>`_greedy_rejection_sample_with_segment(draft_token_ids: torch.Tensor, target_logits: torch.Tensor, num_draft_tokens: torch.Tensor, bonus_token_ids: torch.Tensor, segment_ids: torch.Tensor, group_indices: torch.Tensor, max_draft_tokens: int, accept_u: torch.Tensor | None, synthetic_conditional_rates: torch.Tensor | None, synthetic_mode: bool)` — [`L274`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L274) — Vectorized greedy speculative decoding validation in Torch.
- <a id="_random_rejection_sample_with_segment"></a>`_random_rejection_sample_with_segment(draft_token_ids: torch.Tensor, target_logits: torch.Tensor, num_draft_tokens: torch.Tensor, bonus_token_ids: torch.Tensor, segment_ids: torch.Tensor, group_indices: torch.Tensor, max_draft_tokens: int, temperatures: torch.Tensor, top_k: torch.Tensor, top_p: torch.Tensor, accept_u: torch.Tensor, recover_u: torch.Tensor, synthetic_conditional_rates: torch.Tensor | None, synthetic_mode: bool, topk_candidates: int = 0, apply_topk_topp: bool = True, draft_probs: torch.Tensor | None = None)` — [`L467`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L467) — Vectorized non-greedy speculative decoding validation in Torch.

## Module values
- <a id="PLACEHOLDER_TOKEN_ID"></a>`PLACEHOLDER_TOKEN_ID` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L30)
- <a id="TEMPERATURE_EPS"></a>`TEMPERATURE_EPS` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L32)
- <a id="logger"></a>`logger` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/sample/rejection_sampler.py#L27)

