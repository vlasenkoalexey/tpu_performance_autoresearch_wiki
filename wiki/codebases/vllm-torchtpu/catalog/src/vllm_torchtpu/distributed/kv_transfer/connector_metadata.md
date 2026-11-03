---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.connector_metadata`/
symbols:
  LoadMeta.uuid: LoadMeta#uuid.
  TPUConnectorMetadata: TPUConnectorMetadata#
  LoadMeta.local_block_ids: LoadMeta#local_block_ids.
  LoadMeta.remote_host: LoadMeta#remote_host.
  ReqId: ReqId.
  LoadMeta: LoadMeta#
  LoadMeta.remote_block_ids: LoadMeta#remote_block_ids.
  TPUConnectorMetadata.reqs_to_send: TPUConnectorMetadata#reqs_to_send.
  SendMeta.uuid: SendMeta#uuid.
  LoadMeta.remote_port: LoadMeta#remote_port.
  TPUConnectorMetadata.reqs_to_load: TPUConnectorMetadata#reqs_to_load.
  SendMeta.local_block_ids: SendMeta#local_block_ids.
  LoadMeta.remote_side_channel_port: LoadMeta#remote_side_channel_port.
  SendMeta: SendMeta#
  SendMeta.expiration_time: SendMeta#expiration_time.
  SendMeta.num_tokens: SendMeta#num_tokens.
  LoadMeta.report_completion: LoadMeta#report_completion.
  LoadMeta.fail_only: LoadMeta#fail_only.
  TPUConnectorMetadata.reqs_to_release: TPUConnectorMetadata#reqs_to_release.
  SendMeta.mamba_state_block_ids: SendMeta#mamba_state_block_ids.
  SendMeta.group_block_ids: SendMeta#group_block_ids.
  SendMeta.next_prompt_token_id: SendMeta#next_prompt_token_id.
  SendMeta.registered_ahead: SendMeta#registered_ahead.
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py)

## Classes
### <a id="LoadMeta"></a>`LoadMeta`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py:56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L56)
- signature: `class LoadMeta:`
- members:
  - <a id="LoadMeta.fail_only"></a>`fail_only` — [`L71`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L71)
  - <a id="LoadMeta.local_block_ids"></a>`local_block_ids` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L58)
  - <a id="LoadMeta.remote_block_ids"></a>`remote_block_ids` — [`L59`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L59)
  - <a id="LoadMeta.remote_host"></a>`remote_host` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L60)
  - <a id="LoadMeta.remote_port"></a>`remote_port` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L61)
  - <a id="LoadMeta.remote_side_channel_port"></a>`remote_side_channel_port` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L62)
  - <a id="LoadMeta.report_completion"></a>`report_completion` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L69)
  - <a id="LoadMeta.uuid"></a>`uuid` — [`L57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L57)
- used by: [`_submit_stage3_loads`](tpu_connector.md#TPURaidenConnectorWorker._submit_stage3_loads), [`_coord_rank0_ipc_loop`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_ipc_loop), [`_coord_rank0_handle_new_load`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_handle_new_load), [`process_send_load`](tpu_connector.md#TPURaidenConnectorWorker.process_send_load), [`_coord_rank0_register_copy`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_register_copy), [`_fail_load`](tpu_connector.md#TPURaidenConnectorScheduler._fail_load), [`_coord_process_send_load`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_process_send_load), [`update_state_after_alloc`](tpu_connector.md#TPURaidenConnectorScheduler.update_state_after_alloc), [`_coord_drain_scatter`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_drain_scatter), [`_coord_rank0_send_notify`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_send_notify), [`update_state_after_alloc`](tpu_connector.md#TPUConnectorScheduler.update_state_after_alloc), [`reqs_to_load`](tpu_connector.md#TPUConnectorScheduler.reqs_to_load), [`_resolve_remote_endpoint`](tpu_connector.md#TPURaidenConnectorWorker._resolve_remote_endpoint), [`_resolve_remote_host_port`](zmq_shm_base.md#ZmqShmKvConnectorBase._resolve_remote_host_port), [`reqs_to_load`](connector_metadata.md#TPUConnectorMetadata.reqs_to_load)

### <a id="SendMeta"></a>`SendMeta`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py:30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L30)
- signature: `class SendMeta:`
- members:
  - <a id="SendMeta.expiration_time"></a>`expiration_time` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L34)
  - <a id="SendMeta.group_block_ids"></a>`group_block_ids` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L45)
  - <a id="SendMeta.local_block_ids"></a>`local_block_ids` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L32)
  - <a id="SendMeta.mamba_state_block_ids"></a>`mamba_state_block_ids` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L41)
  - <a id="SendMeta.next_prompt_token_id"></a>`next_prompt_token_id` — [`L48`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L48)
  - <a id="SendMeta.num_tokens"></a>`num_tokens` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L37)
  - <a id="SendMeta.registered_ahead"></a>`registered_ahead` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L52)
  - <a id="SendMeta.uuid"></a>`uuid` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L31)
- used by: [`_register_stage3_request_blocks`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks), [`_stage3_publish_send`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_publish_send), [`_register_stage3_request_row_spans`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_row_spans), [`_register_stage3_request_blocks_dsv4`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks_dsv4), [`process_send_load`](tpu_connector.md#TPURaidenConnectorWorker.process_send_load), [`_coord_rank0_handle_new_send`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_handle_new_send), [`_coord_process_send_load`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_process_send_load), [`request_finished`](tpu_connector.md#TPUConnectorScheduler.request_finished), [`reqs_to_send`](connector_metadata.md#TPUConnectorMetadata.reqs_to_send), [`reqs_to_send`](tpu_connector.md#TPUConnectorScheduler.reqs_to_send)

### <a id="TPUConnectorMetadata"></a>`TPUConnectorMetadata`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py:75`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L75)
- signature: `class TPUConnectorMetadata(KVConnectorMetadata):`
- members:
  - <a id="TPUConnectorMetadata.reqs_to_load"></a>`reqs_to_load` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L77)
  - <a id="TPUConnectorMetadata.reqs_to_release"></a>`reqs_to_release` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L80)
  - <a id="TPUConnectorMetadata.reqs_to_send"></a>`reqs_to_send` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L76)
- uses (calls/refs, reference-scoped): [`LoadMeta`](connector_metadata.md#LoadMeta), [`ReqId`](connector_metadata.md#ReqId), [`SendMeta`](connector_metadata.md#SendMeta)
- used by: [`_submit_stage3_loads`](tpu_connector.md#TPURaidenConnectorWorker._submit_stage3_loads), [`_register_stage3_request_blocks`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks), [`_register_stage3_request_row_spans`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_row_spans), [`_register_stage3_request_blocks_dsv4`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks_dsv4), [`process_send_load`](tpu_connector.md#TPURaidenConnectorWorker.process_send_load), [`_coord_process_send_load`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_process_send_load), [`build_connector_meta`](tpu_connector.md#TPUConnectorScheduler.build_connector_meta), [`build_connector_meta`](tpu_connector.md#TPURaidenConnectorScheduler.build_connector_meta), [`_maybe_delay_stage3_registration_for_test`](tpu_connector.md#TPURaidenConnectorWorker._maybe_delay_stage3_registration_for_test), [`start_load_kv`](tpu_connector.md#TPUConnector.start_load_kv), [`_connector_metadata`](tpu_connector.md#TPUConnector._connector_metadata), [`process_send_load`](zmq_shm_base.md#ZmqShmKvConnectorBase.process_send_load), [`build_connector_meta`](tpu_connector.md#TPUConnector.build_connector_meta), [`process_send_load`](tpu_connector.md#TPUConnectorWorker.process_send_load)

## Module values
- <a id="ReqId"></a>`ReqId` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/connector_metadata.py#L26)

