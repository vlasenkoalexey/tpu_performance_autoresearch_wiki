---
title: 'Module: src/vllm_torchtpu/runner/min_tokens.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/min_tokens.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.min_tokens`/
symbols:
  MinTokensTracker.batch_state: MinTokensTracker#batch_state().
  MinTokensState: MinTokensState.
  plain_rows: plain_rows().
  build_stop_table: build_stop_table().
  verify_rows: verify_rows().
  verify_logits_rows: verify_logits_rows().
  apply_stop_table: apply_stop_table().
  MinTokensTracker.requests: MinTokensTracker#requests.
  StateRows: StateRows.
  MinTokensTracker.add: MinTokensTracker#add().
  _in_chunk: _in_chunk().
  STOP_IDS_WIDTH: STOP_IDS_WIDTH.
  mask_stop_tokens: mask_stop_tokens().
  restore_all_masked_rows: restore_all_masked_rows().
  MinTokensTracker.discard: MinTokensTracker#discard().
  MinTokensTracker.any_in: MinTokensTracker#any_in().
  MinTokensRequest.min_tokens: MinTokensRequest#min_tokens.
  MinTokensTracker.__init__: MinTokensTracker#__init__().
  MinTokensTracker.__bool__: MinTokensTracker#__bool__().
  MinTokensRequest: MinTokensRequest#
  MinTokensRequest.stop_ids: MinTokensRequest#stop_ids.
  MinTokensRequest.structured: MinTokensRequest#structured.
  MinTokensTracker: MinTokensTracker#
  _mask_stop_tokens: _mask_stop_tokens().
  _restore_all_masked_rows: _restore_all_masked_rows().
---
# Module: [`src/vllm_torchtpu/runner/min_tokens.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py)

## Classes
### <a id="MinTokensRequest"></a>`MinTokensRequest`
- def: [`src/vllm_torchtpu/runner/min_tokens.py:62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L62)
- signature: `class MinTokensRequest:`
- members:
  - <a id="MinTokensRequest.min_tokens"></a>`min_tokens` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L63)
  - <a id="MinTokensRequest.stop_ids"></a>`stop_ids` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L64)
  - <a id="MinTokensRequest.structured"></a>`structured` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L65)
- used by: [`_settle_draft_placeholders_for_min_tokens`](tpu_runner.md#TPUModelRunner._settle_draft_placeholders_for_min_tokens), [`batch_state`](min_tokens.md#MinTokensTracker.batch_state), [`add`](min_tokens.md#MinTokensTracker.add), [`__init__`](min_tokens.md#MinTokensTracker.__init__)

### <a id="MinTokensTracker"></a>`MinTokensTracker`
- def: [`src/vllm_torchtpu/runner/min_tokens.py:73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L73)
- doc: The requests that asked for min_tokens and may still be below it, by
- signature: `class MinTokensTracker:`
- members:
  - <a id="MinTokensTracker.add"></a>`add(self, req_id: str, params: SamplingParams | None)` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L83)
  - <a id="MinTokensTracker.any_in"></a>`any_in(self, req_id_to_index: Mapping[str, int])` — [`L98`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L98) — Whether a tracked request is in the batch. Requests that reached
  - <a id="MinTokensTracker.batch_state"></a>`batch_state(self, req_id_to_index: Mapping[str, int], num_output_tokens: Callable[[str], int | None])` — [`L103`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L103) — The batch rows still below min_tokens. ``num_output_tokens`` must
  - <a id="MinTokensTracker.discard"></a>`discard(self, req_ids: Iterable[str])` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L94)
  - <a id="MinTokensTracker.requests"></a>`requests` — [`L78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L78)
- protocol/private: <a id="MinTokensTracker.__bool__"></a>`__bool__`[`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L80), <a id="MinTokensTracker.__init__"></a>`__init__`[`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L77)
- uses (calls/refs, reference-scoped): [`MinTokensState`](min_tokens.md#MinTokensState), [`min_tokens`](min_tokens.md#MinTokensRequest.min_tokens), [`MinTokensRequest`](min_tokens.md#MinTokensRequest), [`stop_ids`](min_tokens.md#MinTokensRequest.stop_ids), [`structured`](min_tokens.md#MinTokensRequest.structured)
- used by: [`_update_states`](tpu_runner.md#TPUModelRunner._update_states), [`_settle_draft_placeholders_for_min_tokens`](tpu_runner.md#TPUModelRunner._settle_draft_placeholders_for_min_tokens), [`_min_tokens_batch_state`](tpu_runner.md#TPUModelRunner._min_tokens_batch_state), [`_greedy_top_tokens_this_step`](tpu_runner.md#TPUModelRunner._greedy_top_tokens_this_step), [`_min_tokens`](tpu_runner.md#TPUModelRunner._min_tokens)

## Functions
- <a id="_in_chunk"></a>`_in_chunk(state: MinTokensState, start: int, end: int)` — [`L178`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L178)
- <a id="_mask_stop_tokens"></a>`_mask_stop_tokens(logits: torch.Tensor, stop_ids: torch.Tensor)` — [`L236`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L236) — Sets ``logits[r, stop_ids[r]]`` to -inf. A row of -1 writes its own
- <a id="_restore_all_masked_rows"></a>`_restore_all_masked_rows(logits: torch.Tensor, masked: torch.Tensor, restore: torch.Tensor)` — [`L258`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L258) — Rows with ``restore`` that are all -inf after masking go back to
- <a id="apply_stop_table"></a>`apply_stop_table(logits: torch.Tensor, stop_ids: np.ndarray, restore: np.ndarray)` — [`L216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L216) — Masks ``logits`` with a ``build_stop_table`` result.
- <a id="build_stop_table"></a>`build_stop_table(state: MinTokensState, rows: StateRows, num_rows: int)` — [`L138`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L138) — Host-side mask inputs for one logits tensor of ``num_rows`` rows, from
- <a id="mask_stop_tokens"></a>`mask_stop_tokens(logits: torch.Tensor, stop_ids: torch.Tensor)` — [`L232`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L232)
- <a id="plain_rows"></a>`plain_rows(state: MinTokensState, start: int, end: int)` — [`L182`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L182) — Rows of a chunk with one logits row per request.
- <a id="restore_all_masked_rows"></a>`restore_all_masked_rows(logits: torch.Tensor, masked: torch.Tensor, restore: torch.Tensor)` — [`L252`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L252)
- <a id="verify_logits_rows"></a>`verify_logits_rows(state: MinTokensState, start: int, draft_lengths: Sequence[int])` — [`L203`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L203) — Rows of a verify chunk's logits, before the target / bonus gathers:
- <a id="verify_rows"></a>`verify_rows(state: MinTokensState, start: int, draft_lengths: Sequence[int])` — [`L187`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L187) — (target rows, bonus rows) of a verify chunk: request ``start + k`` owns

## Module values
- <a id="MinTokensState"></a>`MinTokensState` — [`L70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L70)
- <a id="STOP_IDS_WIDTH"></a>`STOP_IDS_WIDTH` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L58)
- <a id="StateRows"></a>`StateRows` — [`L135`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/min_tokens.py#L135)

