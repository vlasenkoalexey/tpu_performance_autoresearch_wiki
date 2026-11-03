---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.raiden_pd_completion`/
symbols:
  RaidenSendOutcome: RaidenSendOutcome#
  _OUTCOME_PRIORITY: _OUTCOME_PRIORITY.
  RaidenSendResults: RaidenSendResults#
  RaidenSendResults.outcomes: RaidenSendResults#outcomes.
  merge_raiden_send_outcomes: merge_raiden_send_outcomes().
  send_completion_enabled: send_completion_enabled().
  RaidenSendResults.aggregate: RaidenSendResults#aggregate().
  RaidenSendOutcome.SUCCESS: RaidenSendOutcome#SUCCESS.
  RaidenSendOutcome.SEND_FAILURE: RaidenSendOutcome#SEND_FAILURE.
  RaidenSendOutcome.UNCLAIMED_TIMEOUT: RaidenSendOutcome#UNCLAIMED_TIMEOUT.
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py)

## Classes
### <a id="RaidenSendOutcome"></a>`RaidenSendOutcome`  ·  implements/extends StrEnum
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py:70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L70) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- signature: `class RaidenSendOutcome(StrEnum):`
- members:
  - <a id="RaidenSendOutcome.SEND_FAILURE"></a>`SEND_FAILURE` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L72)
  - <a id="RaidenSendOutcome.SUCCESS"></a>`SUCCESS` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L71)
  - <a id="RaidenSendOutcome.UNCLAIMED_TIMEOUT"></a>`UNCLAIMED_TIMEOUT` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L73)
- used by: [`update_from_output`](../../core/raiden_pd.md#_ProducerCompletion.update_from_output), [`_stage3_ready_producer_send_terminals`](tpu_connector.md#TPURaidenConnectorWorker._stage3_ready_producer_send_terminals), [`_OUTCOME_PRIORITY`](raiden_pd_completion.md#_OUTCOME_PRIORITY), [`_ERROR_BY_OUTCOME`](../../core/raiden_pd.md#_ERROR_BY_OUTCOME), [`outcomes`](raiden_pd_completion.md#RaidenSendResults.outcomes), [`merge_raiden_send_outcomes`](raiden_pd_completion.md#merge_raiden_send_outcomes), [`outcome`](../../core/raiden_pd.md#_PendingResponse.outcome)

### <a id="RaidenSendResults"></a>`RaidenSendResults`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py:93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L93) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- signature: `class RaidenSendResults(KVConnectorWorkerMetadata):`
- members:
  - <a id="RaidenSendResults.aggregate"></a>`aggregate(self, other: KVConnectorWorkerMetadata)` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L98)
  - <a id="RaidenSendResults.outcomes"></a>`outcomes` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L96)
- uses (calls/refs, reference-scoped): [`RaidenSendOutcome`](raiden_pd_completion.md#RaidenSendOutcome), [`merge_raiden_send_outcomes`](raiden_pd_completion.md#merge_raiden_send_outcomes)
- used by: [`update_from_output`](../../core/raiden_pd.md#_ProducerCompletion.update_from_output), [`_stage3_ready_producer_send_terminals`](tpu_connector.md#TPURaidenConnectorWorker._stage3_ready_producer_send_terminals), [`build_connector_worker_meta`](tpu_connector.md#TPURaidenConnector.build_connector_worker_meta), [`_pd_send_results`](tpu_connector.md#TPURaidenConnectorWorker._pd_send_results), [`take_pd_send_results`](tpu_connector.md#TPURaidenConnectorWorker.take_pd_send_results)

## Functions
- <a id="merge_raiden_send_outcomes"></a>`merge_raiden_send_outcomes(current: RaidenSendOutcome | None, candidate: RaidenSendOutcome)` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L83)
- <a id="send_completion_enabled"></a>`send_completion_enabled(vllm_config: VllmConfig)` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L28) — Validate and return whether opt-in Raiden P send completion is enabled. — documented in [tpu-schedulers](../../../../../concepts/tpu-schedulers.md)

## Module values
- <a id="_OUTCOME_PRIORITY"></a>`_OUTCOME_PRIORITY` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden_pd_completion.py#L76)

