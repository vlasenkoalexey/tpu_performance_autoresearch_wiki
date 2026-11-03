---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.kv_save_nan_check`/
symbols:
  KVSaveNanCheck.record: KVSaveNanCheck#record().
  KVSaveNanCheck.bad_request_ids: KVSaveNanCheck#bad_request_ids().
  wait_for_save_with_nan_check: wait_for_save_with_nan_check().
  begin_kv_save_nan_check: begin_kv_save_nan_check().
  KVSaveNanCheck: KVSaveNanCheck#
  KVSaveNanCheck._chunks: KVSaveNanCheck#_chunks.
  _leaf_connectors: _leaf_connectors().
  KVSaveNanCheck.is_ready: KVSaveNanCheck#is_ready().
  SupportsKVSaveNanCheck.wait_for_save: SupportsKVSaveNanCheck#wait_for_save().
  KVSaveNanCheck._bad_req_ids: KVSaveNanCheck#_bad_req_ids.
  _Chunk: _Chunk#
  _Chunk.req_ids: _Chunk#req_ids.
  _Chunk.ready_event: _Chunk#ready_event.
  SupportsKVSaveNanCheck: SupportsKVSaveNanCheck#
  SupportsKVSaveNanCheck.needs_kv_save_nan_check: SupportsKVSaveNanCheck#needs_kv_save_nan_check().
  _Chunk.request_indices: _Chunk#request_indices.
  _Chunk.flags_cpu: _Chunk#flags_cpu.
  _token_nan_flags: _token_nan_flags().
  _Chunk.flags_device: _Chunk#flags_device.
  KVSaveNanCheck.__init__: KVSaveNanCheck#__init__().
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py)

## Classes
### <a id="KVSaveNanCheck"></a>`KVSaveNanCheck`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py:63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L63) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- doc: Snapshot all real target forward chunks without synchronizing the issuer.
- signature: `class KVSaveNanCheck:`
- members:
  - <a id="KVSaveNanCheck.bad_request_ids"></a>`bad_request_ids(self)` — [`L107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L107) — Read the snapshot on the store thread, preserving event errors.
  - <a id="KVSaveNanCheck.is_ready"></a>`is_ready(self)` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L104)
  - <a id="KVSaveNanCheck.record"></a>`record(self, hidden_states: torch.Tensor | IntermediateTensors, req_ids: tuple[str, ...], query_start_loc: np.ndarray, plan: SequenceLayoutPlan)` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L76) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- protocol/private: <a id="KVSaveNanCheck.__init__"></a>`__init__`[`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L72), <a id="KVSaveNanCheck._bad_req_ids"></a>`_bad_req_ids`[`L74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L74), <a id="KVSaveNanCheck._chunks"></a>`_chunks`[`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L73)
- uses (calls/refs, reference-scoped): [`SequenceLayoutPlan`](../../layers/core/sequence_layout.md#SequenceLayoutPlan), [`token_slice`](../../layers/core/sequence_layout.md#SequenceLayoutPlan.token_slice), [`global_padded_num_tokens`](../../layers/core/sequence_layout.md#SequenceLayoutPlan.global_padded_num_tokens), [`_packed_to_request_major_token_indices`](../../layers/core/sequence_layout.md#SequenceLayoutPlan._packed_to_request_major_token_indices), [`_Chunk`](kv_save_nan_check.md#_Chunk), [`ready_event`](kv_save_nan_check.md#_Chunk.ready_event), [`req_ids`](kv_save_nan_check.md#_Chunk.req_ids), [`_token_nan_flags`](kv_save_nan_check.md#_token_nan_flags), [`flags_cpu`](kv_save_nan_check.md#_Chunk.flags_cpu), [`request_indices`](kv_save_nan_check.md#_Chunk.request_indices)
- used by: [`execute_model`](../../runner/tpu_runner.md#TPUModelRunner.execute_model), [`wait_for_save_with_nan_check`](kv_save_nan_check.md#wait_for_save_with_nan_check), [`begin_kv_save_nan_check`](kv_save_nan_check.md#begin_kv_save_nan_check), [`maybe_wait_for_kv_save`](../../runner/tpu_runner.md#TPUModelRunner.maybe_wait_for_kv_save), [`_pp_pending_kv_save_nan_check`](../../runner/tpu_runner.md#TPUModelRunner._pp_pending_kv_save_nan_check), [`kv_save_nan_check`](../../runner/tpu_runner.md#ExecuteModelState.kv_save_nan_check), [`wait_for_save`](kv_save_nan_check.md#SupportsKVSaveNanCheck.wait_for_save)

### <a id="SupportsKVSaveNanCheck"></a>`SupportsKVSaveNanCheck`  ·  implements/extends Protocol
- def: [`src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py:124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L124)
- doc: Opt-in store interface; ordinary KV connectors keep their original API.
- signature: `class SupportsKVSaveNanCheck(Protocol):`
- members:
  - <a id="SupportsKVSaveNanCheck.needs_kv_save_nan_check"></a>`needs_kv_save_nan_check(self)` — [`L134`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L134)
  - <a id="SupportsKVSaveNanCheck.wait_for_save"></a>`wait_for_save(self, nan_check: KVSaveNanCheck | None = None)` — [`L136`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L136)
- uses (calls/refs, reference-scoped): [`KVSaveNanCheck`](kv_save_nan_check.md#KVSaveNanCheck)
- used by: [`wait_for_save_with_nan_check`](kv_save_nan_check.md#wait_for_save_with_nan_check), [`begin_kv_save_nan_check`](kv_save_nan_check.md#begin_kv_save_nan_check)

### <a id="_Chunk"></a>`_Chunk`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py:33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L33)
- signature: `class _Chunk:`
- members:
  - <a id="_Chunk.flags_cpu"></a>`flags_cpu` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L36)
  - <a id="_Chunk.flags_device"></a>`flags_device` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L37)
  - <a id="_Chunk.ready_event"></a>`ready_event` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L38)
  - <a id="_Chunk.req_ids"></a>`req_ids` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L34)
  - <a id="_Chunk.request_indices"></a>`request_indices` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L35)
- used by: [`record`](kv_save_nan_check.md#KVSaveNanCheck.record), [`bad_request_ids`](kv_save_nan_check.md#KVSaveNanCheck.bad_request_ids), [`_chunks`](kv_save_nan_check.md#KVSaveNanCheck._chunks), [`is_ready`](kv_save_nan_check.md#KVSaveNanCheck.is_ready)

## Functions
- <a id="_leaf_connectors"></a>`_leaf_connectors(connector: KVConnectorBase_V1)` — [`L139`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L139)
- <a id="_token_nan_flags"></a>`_token_nan_flags(hidden_states: torch.Tensor | IntermediateTensors)` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L41)
- <a id="begin_kv_save_nan_check"></a>`begin_kv_save_nan_check(connector: KVConnectorBase_V1)` — [`L147`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L147) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="wait_for_save_with_nan_check"></a>`wait_for_save_with_nan_check(connector: KVConnectorBase_V1, nan_check: KVSaveNanCheck)` — [`L156`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_save_nan_check.py#L156) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)

