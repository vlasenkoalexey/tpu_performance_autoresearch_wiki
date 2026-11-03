---
title: 'Module: src/vllm_torchtpu/core/raiden_pd.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/core/raiden_pd.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.core.raiden_pd`/
symbols:
  _ProducerCompletion.update_from_output: _ProducerCompletion#update_from_output().
  _ProducerCompletion.pending_responses: _ProducerCompletion#pending_responses.
  _ERROR_BY_OUTCOME: _ERROR_BY_OUTCOME.
  patch_scheduler_init.init: patch_scheduler_init().init().
  _ProducerCompletion.finish_requests: _ProducerCompletion#finish_requests().
  _PendingResponse.outcome: _PendingResponse#outcome.
  logger: logger.
  patch_scheduler_init: patch_scheduler_init().
  _PendingResponse: _PendingResponse#
  _PendingResponse.client_index: _PendingResponse#client_index.
  _PendingResponse.finish_reason: _PendingResponse#finish_reason.
  _PendingResponse.stop_reason: _PendingResponse#stop_reason.
  _PendingResponse.kv_transfer_params: _PendingResponse#kv_transfer_params.
  _ProducerCompletion: _ProducerCompletion#
  _ProducerCompletion.original_update: _ProducerCompletion#original_update.
  _ProducerCompletion.original_finish: _ProducerCompletion#original_finish.
  _ProducerCompletion.__init__: _ProducerCompletion#__init__().
---
# Module: [`src/vllm_torchtpu/core/raiden_pd.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py)

## Classes
### <a id="_PendingResponse"></a>`_PendingResponse`
- def: [`src/vllm_torchtpu/core/raiden_pd.py:45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L45)
- signature: `class _PendingResponse:`
- members:
  - <a id="_PendingResponse.client_index"></a>`client_index` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L46)
  - <a id="_PendingResponse.finish_reason"></a>`finish_reason` — [`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L47)
  - <a id="_PendingResponse.kv_transfer_params"></a>`kv_transfer_params` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L49)
  - <a id="_PendingResponse.outcome"></a>`outcome` — [`L50`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L50)
  - <a id="_PendingResponse.stop_reason"></a>`stop_reason` — [`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L48)
- uses (calls/refs, reference-scoped): [`RaidenSendOutcome`](../distributed/kv_transfer/raiden_pd_completion.md#RaidenSendOutcome)
- used by: [`update_from_output`](raiden_pd.md#_ProducerCompletion.update_from_output), [`pending_responses`](raiden_pd.md#_ProducerCompletion.pending_responses)

### <a id="_ProducerCompletion"></a>`_ProducerCompletion`
- def: [`src/vllm_torchtpu/core/raiden_pd.py:70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L70)
- doc: Keep an opted-in P response open until the existing send barrier.
- signature: `class _ProducerCompletion:`
- members:
  - <a id="_ProducerCompletion.finish_requests"></a>`finish_requests(self, request_ids: str | Iterable[str] | None, finished_status: RequestStatus)` — [`L158`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L158)
  - <a id="_ProducerCompletion.update_from_output"></a>`update_from_output(self, scheduler_output, model_runner_output)` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L80) — documented in [kv-transfer-and-disaggregated-serving](../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="_ProducerCompletion.original_finish"></a>`original_finish` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L75)
  - <a id="_ProducerCompletion.original_update"></a>`original_update` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L74)
  - <a id="_ProducerCompletion.pending_responses"></a>`pending_responses` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L76) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- protocol/private: <a id="_ProducerCompletion.__init__"></a>`__init__`[`L73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L73)
- uses (calls/refs, reference-scoped): [`RaidenSendOutcome`](../distributed/kv_transfer/raiden_pd_completion.md#RaidenSendOutcome), [`RaidenSendResults`](../distributed/kv_transfer/raiden_pd_completion.md#RaidenSendResults), [`_ERROR_BY_OUTCOME`](raiden_pd.md#_ERROR_BY_OUTCOME), [`outcomes`](../distributed/kv_transfer/raiden_pd_completion.md#RaidenSendResults.outcomes), [`merge_raiden_send_outcomes`](../distributed/kv_transfer/raiden_pd_completion.md#merge_raiden_send_outcomes), [`outcome`](raiden_pd.md#_PendingResponse.outcome), [`logger`](raiden_pd.md#logger), [`SUCCESS`](../distributed/kv_transfer/raiden_pd_completion.md#RaidenSendOutcome.SUCCESS), [`_PendingResponse`](raiden_pd.md#_PendingResponse), [`client_index`](raiden_pd.md#_PendingResponse.client_index), [`finish_reason`](raiden_pd.md#_PendingResponse.finish_reason), [`kv_transfer_params`](raiden_pd.md#_PendingResponse.kv_transfer_params), [`stop_reason`](raiden_pd.md#_PendingResponse.stop_reason)
- used by: [`init`](raiden_pd.md#patch_scheduler_init.init)

## Functions
- <a id="patch_scheduler_init.init"></a>`init(self, vllm_config, *args, **kwargs)` — [`L179`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L179) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="patch_scheduler_init"></a>`patch_scheduler_init()` — [`L173`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L173) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)

## Module values
- <a id="_ERROR_BY_OUTCOME"></a>`_ERROR_BY_OUTCOME` — [`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L53) — documented in [kv-transfer-and-disaggregated-serving](../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="logger"></a>`logger` — [`L41`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/raiden_pd.py#L41)

