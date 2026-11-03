---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.zmq_shm_base`/
symbols:
  ZmqShmKvConnectorBase._coord_rank0_ipc_loop: ZmqShmKvConnectorBase#_coord_rank0_ipc_loop().
  ZmqShmKvConnectorBase._coord_rank0_handle_new_load: ZmqShmKvConnectorBase#_coord_rank0_handle_new_load().
  ZmqShmKvConnectorBase._coord_rank0_pull: ZmqShmKvConnectorBase#_coord_rank0_pull().
  logger: logger.
  ZmqShmKvConnectorBase.node_id: ZmqShmKvConnectorBase#node_id.
  ZmqShmKvConnectorBase._coord_rank0_handle_new_send: ZmqShmKvConnectorBase#_coord_rank0_handle_new_send().
  ZmqShmKvConnectorBase._coord_rank0_register_copy: ZmqShmKvConnectorBase#_coord_rank0_register_copy().
  ZmqShmKvConnectorBase._coord_scatter_shard: ZmqShmKvConnectorBase#_coord_scatter_shard().
  ZmqShmKvConnectorBase._coord_rank0_build_pull_response: ZmqShmKvConnectorBase#_coord_rank0_build_pull_response().
  ZmqShmKvConnectorBase._coord_stage_wait_worker: ZmqShmKvConnectorBase#_coord_stage_wait_worker().
  ZmqShmKvConnectorBase._coord_get_finished: ZmqShmKvConnectorBase#_coord_get_finished().
  ZmqShmKvConnectorBase._coord_stage_shard: ZmqShmKvConnectorBase#_coord_stage_shard().
  ZmqShmKvConnectorBase._build_pool_spec: ZmqShmKvConnectorBase#_build_pool_spec().
  ZmqShmKvConnectorBase._coord_pool_spec: ZmqShmKvConnectorBase#_coord_pool_spec.
  ZmqShmKvConnectorBase._coord_process_send_load: ZmqShmKvConnectorBase#_coord_process_send_load().
  ZmqShmKvConnectorBase._coord_worker_ipc_loop: ZmqShmKvConnectorBase#_coord_worker_ipc_loop().
  ZmqShmKvConnectorBase.transfer_stats: ZmqShmKvConnectorBase#transfer_stats.
  ZmqShmKvConnectorBase._coord_rank0_external_data_loop: ZmqShmKvConnectorBase#_coord_rank0_external_data_loop().
  ZmqShmKvConnectorBase._signal_stage_done: ZmqShmKvConnectorBase#_signal_stage_done().
  ZmqShmKvConnectorBase.tp_rank: ZmqShmKvConnectorBase#tp_rank.
  ZmqShmKvConnectorBase._warmup_coord_once: ZmqShmKvConnectorBase#_warmup_coord_once().
  ZmqShmKvConnectorBase._coord_setup_rank0: ZmqShmKvConnectorBase#_coord_setup_rank0().
  ZmqShmKvConnectorBase._coord_drain_scatter: ZmqShmKvConnectorBase#_coord_drain_scatter().
  ZmqShmKvConnectorBase._coord_pool: ZmqShmKvConnectorBase#_coord_pool.
  ZmqShmKvConnectorBase.register_runner: ZmqShmKvConnectorBase#register_runner().
  ZmqShmKvConnectorBase._coord_stage_waiter_loop: ZmqShmKvConnectorBase#_coord_stage_waiter_loop().
  ZmqShmKvConnectorBase._pull_channel: ZmqShmKvConnectorBase#_pull_channel().
  ZmqShmKvConnectorBase._coord_rank0_expire_loop: ZmqShmKvConnectorBase#_coord_rank0_expire_loop().
  ZmqShmKvConnectorBase._coord_setup_worker: ZmqShmKvConnectorBase#_coord_setup_worker().
  ZmqShmKvConnectorBase._coord_rank0_send_notify: ZmqShmKvConnectorBase#_coord_rank0_send_notify().
  ZmqShmKvConnectorBase.get_kv_connector_stats: ZmqShmKvConnectorBase#get_kv_connector_stats().
  ZmqShmKvConnectorBase._coord_scatter_and_ack: ZmqShmKvConnectorBase#_coord_scatter_and_ack().
  _LatencyTracker.record: _LatencyTracker#record().
  ZmqShmKvConnectorBase._coord_lock: ZmqShmKvConnectorBase#_coord_lock.
  ZmqShmKvConnectorBase._coord_teardown: ZmqShmKvConnectorBase#_coord_teardown().
  ZmqShmKvConnectorBase._coord_worker_stage_inline: ZmqShmKvConnectorBase#_coord_worker_stage_inline().
  ZmqShmKvConnectorBase._coord_rank0_external_notif_loop: ZmqShmKvConnectorBase#_coord_rank0_external_notif_loop().
  _CoordRecvEntry.req_id: _CoordRecvEntry#req_id.
  ZmqShmKvConnectorBase.ranks_per_host: ZmqShmKvConnectorBase#ranks_per_host.
  ZmqShmKvConnectorBase._complete_stage_entry: ZmqShmKvConnectorBase#_complete_stage_entry().
  ZmqShmKvConnectorBase.local_tp_rank: ZmqShmKvConnectorBase#local_tp_rank.
  ZmqShmKvConnectorBase._coord_local_to_global_rank: ZmqShmKvConnectorBase#_coord_local_to_global_rank.
  ZmqShmKvConnectorBase._warmup_kv_ops: ZmqShmKvConnectorBase#_warmup_kv_ops().
  ZmqShmKvConnectorBase._lat: ZmqShmKvConnectorBase#_lat.
  ZmqShmKvConnectorBase._coord_send: ZmqShmKvConnectorBase#_coord_send.
  ZmqShmKvConnectorBase._coord_recv: ZmqShmKvConnectorBase#_coord_recv.
  ZmqShmKvConnectorBase.runner: ZmqShmKvConnectorBase#runner.
  ZmqShmKvConnectorBase._coord_broadcast: ZmqShmKvConnectorBase#_coord_broadcast().
  _CoordRecvEntry.uuid: _CoordRecvEntry#uuid.
  ZmqShmKvConnectorBase._pull_response_header: ZmqShmKvConnectorBase#_pull_response_header().
  ZmqShmKvConnectorBase._resolve_remote_host_port: ZmqShmKvConnectorBase#_resolve_remote_host_port().
  ZmqShmKvConnectorBase.device: ZmqShmKvConnectorBase#device.
  ZmqShmKvConnectorBase.side_channel_port: ZmqShmKvConnectorBase#side_channel_port.
  ZmqShmKvConnectorBase._coord_ipc_drain_outbound: ZmqShmKvConnectorBase#_coord_ipc_drain_outbound().
  ZmqShmKvConnectorBase.is_producer: ZmqShmKvConnectorBase#is_producer.
  ZmqShmKvConnectorBase._coord_channel_executor: ZmqShmKvConnectorBase#_coord_channel_executor.
  ZmqShmKvConnectorBase._is_host_coordinator: ZmqShmKvConnectorBase#_is_host_coordinator.
  ZmqShmKvConnectorBase.kv_transfer_port: ZmqShmKvConnectorBase#kv_transfer_port.
  ZmqShmKvConnectorBase.tp_size: ZmqShmKvConnectorBase#tp_size.
  ZmqShmKvConnectorBase._stop_event: ZmqShmKvConnectorBase#_stop_event.
  ZmqShmKvConnectorBase._kv_transfer_ports: ZmqShmKvConnectorBase#_kv_transfer_ports.
  ZmqShmKvConnectorBase.process_send_load: ZmqShmKvConnectorBase#process_send_load().
  ZmqShmKvConnectorBase._prepare_response: ZmqShmKvConnectorBase#_prepare_response().
  ZmqShmKvConnectorBase._send_ready_responses: ZmqShmKvConnectorBase#_send_ready_responses().
  _CoordSendEntry.staged_events: _CoordSendEntry#staged_events.
  _CoordRecvEntry.slot_idx: _CoordRecvEntry#slot_idx.
  ZmqShmKvConnectorBase._coord_threads: ZmqShmKvConnectorBase#_coord_threads.
  ZmqShmKvConnectorBase._coord_workers_ready: ZmqShmKvConnectorBase#_coord_workers_ready.
  ZmqShmKvConnectorBase._worker_pending_load_cv: ZmqShmKvConnectorBase#_worker_pending_load_cv.
  ZmqShmKvConnectorBase._coord_send_ipc: ZmqShmKvConnectorBase#_coord_send_ipc().
  _CoordSendEntry.req_id: _CoordSendEntry#req_id.
  ZmqShmKvConnectorBase._coord_done_sending: ZmqShmKvConnectorBase#_coord_done_sending.
  ZmqShmKvConnectorBase._coord_done_recving: ZmqShmKvConnectorBase#_coord_done_recving.
  ZmqShmKvConnectorBase.__del__: ZmqShmKvConnectorBase#__del__().
  _CoordSendEntry.expiration_time: _CoordSendEntry#expiration_time.
  _CoordRecvEntry.num_blocks: _CoordRecvEntry#num_blocks.
  _CoordRecvEntry.local_blocks: _CoordRecvEntry#local_blocks.
  _CoordRecvEntry.remote_host: _CoordRecvEntry#remote_host.
  _CoordRecvEntry.pull_ok: _CoordRecvEntry#pull_ok.
  ZmqShmKvConnectorBase.zmq_cxt: ZmqShmKvConnectorBase#zmq_cxt.
  ZmqShmKvConnectorBase._n_channels: ZmqShmKvConnectorBase#_n_channels.
  ZmqShmKvConnectorBase._replace_runner_kv_cache: ZmqShmKvConnectorBase#_replace_runner_kv_cache().
  _secure_dumps: _secure_dumps().
  ZmqShmKvConnectorBase._synchronize_device: ZmqShmKvConnectorBase#_synchronize_device().
  _CoordSendEntry.staged: _CoordSendEntry#staged.
  _CoordRecvEntry.remote_port: _CoordRecvEntry#remote_port.
  ZmqShmKvConnectorBase.dp_rank: ZmqShmKvConnectorBase#dp_rank.
  ZmqShmKvConnectorBase._init_coord_state: ZmqShmKvConnectorBase#_init_coord_state().
  ZmqShmKvConnectorBase._coord_rank_to_identity: ZmqShmKvConnectorBase#_coord_rank_to_identity.
  ZmqShmKvConnectorBase._worker_pending_stage_cv: ZmqShmKvConnectorBase#_worker_pending_stage_cv.
  ZmqShmKvConnectorBase.num_layers: ZmqShmKvConnectorBase#num_layers.
  ZmqShmKvConnectorBase._pool_create: ZmqShmKvConnectorBase#_pool_create().
  ZmqShmKvConnectorBase._pool_attach: ZmqShmKvConnectorBase#_pool_attach().
  ZmqShmKvConnectorBase._coord_attach_shm_with_retry: ZmqShmKvConnectorBase#_coord_attach_shm_with_retry().
  ZmqShmKvConnectorBase._coord_worker_wait_load: ZmqShmKvConnectorBase#_coord_worker_wait_load().
  ZmqShmKvConnectorBase._stage_pending_q: ZmqShmKvConnectorBase#_stage_pending_q.
  ZmqShmKvConnectorBase._wait_stage: ZmqShmKvConnectorBase#_wait_stage().
  _CoordSendEntry.pull_acked: _CoordSendEntry#pull_acked.
  _CoordSendEntry.__post_init__: _CoordSendEntry#__post_init__().
  _CoordRecvEntry.remote_blocks: _CoordRecvEntry#remote_blocks.
  _CoordRecvEntry.copied: _CoordRecvEntry#copied.
  _StageInFlight: _StageInFlight#
  _StageInFlight.uuid: _StageInFlight#uuid.
  ZmqShmKvConnectorBase.vllm_config: ZmqShmKvConnectorBase#vllm_config.
  ZmqShmKvConnectorBase._coord_ipc_sock: ZmqShmKvConnectorBase#_coord_ipc_sock.
  ZmqShmKvConnectorBase._worker_pending_load: ZmqShmKvConnectorBase#_worker_pending_load.
  _secure_loads: _secure_loads().
  ZmqShmKvConnectorBase.host_ip: ZmqShmKvConnectorBase#host_ip.
  ZmqShmKvConnectorBase._coord_stage_waiter_pool: ZmqShmKvConnectorBase#_coord_stage_waiter_pool.
  ZmqShmKvConnectorBase._h2d_into_device_async: ZmqShmKvConnectorBase#_h2d_into_device_async().
  ZmqShmKvConnectorBase._try_fast_scatter: ZmqShmKvConnectorBase#_try_fast_scatter().
  _IPC_AUTH_KEY._IPC_AUTH_KEY: _IPC_AUTH_KEY._IPC_AUTH_KEY.
  ZmqShmKvConnectorBase._kv_scatter_enabled: ZmqShmKvConnectorBase#_kv_scatter_enabled.
  _CoordSendEntry: _CoordSendEntry#
  _CoordSendEntry.slot_idx: _CoordSendEntry#slot_idx.
  _CoordRecvEntry: _CoordRecvEntry#
  _CoordRecvEntry.load_complete: _CoordRecvEntry#load_complete.
  ZmqShmKvConnectorBase._worker_pending_stage: ZmqShmKvConnectorBase#_worker_pending_stage.
  _get_default_ipc_key: _get_default_ipc_key().
  ZmqShmKvConnectorBase._coord_stage_wait_timeout_s: ZmqShmKvConnectorBase#_coord_stage_wait_timeout_s.
  ZmqShmKvConnectorBase._extract_kv_layout: ZmqShmKvConnectorBase#_extract_kv_layout().
  ZmqShmKvConnectorBase._warmup_block_sizes: ZmqShmKvConnectorBase#_warmup_block_sizes().
  ZmqShmKvConnectorBase._maybe_enable_kv_scatter: ZmqShmKvConnectorBase#_maybe_enable_kv_scatter().
  ZmqShmKvConnectorBase._stage_d2h: ZmqShmKvConnectorBase#_stage_d2h().
  ZmqShmKvConnectorBase._stage_d2h_sync: ZmqShmKvConnectorBase#_stage_d2h_sync().
  ZmqShmKvConnectorBase._h2d_into_device: ZmqShmKvConnectorBase#_h2d_into_device().
  _try_remove_ipc_endpoint: _try_remove_ipc_endpoint().
  ZmqShmKvConnectorBase.shape: ZmqShmKvConnectorBase#shape.
  _IPC_LOAD_NOTIFY: _IPC_LOAD_NOTIFY.
  _CoordSendEntry.num_blocks: _CoordSendEntry#num_blocks.
  _CoordSendEntry.stage_complete: _CoordSendEntry#stage_complete.
  _CoordSendEntry.stage_failed: _CoordSendEntry#stage_failed.
  _CoordRecvEntry.remote_side_channel_port: _CoordRecvEntry#remote_side_channel_port.
  _CoordRecvEntry.reported_done: _CoordRecvEntry#reported_done.
  _StageInFlight.slot_idx: _StageInFlight#slot_idx.
  _StageInFlight.enqueue_t0: _StageInFlight#enqueue_t0.
  _StageInFlight.issue_t1: _StageInFlight#issue_t1.
  _LatencyTracker._stats: _LatencyTracker#_stats.
  ZmqShmKvConnectorBase._coord_ipc_out: ZmqShmKvConnectorBase#_coord_ipc_out.
  ZmqShmKvConnectorBase.multi_host: ZmqShmKvConnectorBase#multi_host.
  ZmqShmKvConnectorBase.get_finished: ZmqShmKvConnectorBase#get_finished().
  ZmqShmKvConnectorBase.dtype: ZmqShmKvConnectorBase#dtype.
  _MSG_PULL: _MSG_PULL.
  _MSG_OK: _MSG_OK.
  _MSG_ERR: _MSG_ERR.
  _IPC_HELLO: _IPC_HELLO.
  _IPC_STAGE_NOTIFY: _IPC_STAGE_NOTIFY.
  _IPC_STAGE_DONE: _IPC_STAGE_DONE.
  _IPC_LOAD_SKIP: _IPC_LOAD_SKIP.
  _IPC_COPY_DONE: _IPC_COPY_DONE.
  _IPC_DROP: _IPC_DROP.
  _CoordSendEntry.tp_size: _CoordSendEntry#tp_size.
  _StageInFlight.future: _StageInFlight#future.
  _StageInFlight.tpu_tensors: _StageInFlight#tpu_tensors.
  _StageInFlight.cpu_tensors: _StageInFlight#cpu_tensors.
  _StageInFlight.total_bytes: _StageInFlight#total_bytes.
  _StageInFlight._signaled: _StageInFlight#_signaled.
  _LatencyTracker._log_interval_s: _LatencyTracker#_log_interval_s.
  _LatencyTracker._last_log: _LatencyTracker#_last_log.
  ZmqShmKvConnectorBase: ZmqShmKvConnectorBase#
  ZmqShmKvConnectorBase._coord_executor: ZmqShmKvConnectorBase#_coord_executor.
  ZmqShmKvConnectorBase._blocks_token: ZmqShmKvConnectorBase#_blocks_token().
  ZmqShmKvConnectorBase._coord_notif_sockets: ZmqShmKvConnectorBase#_coord_notif_sockets.
  _LAT_D2H: _LAT_D2H.
  _LAT_WIRE: _LAT_WIRE.
  _LAT_UNPACK: _LAT_UNPACK.
  _LAT_H2D: _LAT_H2D.
  _LAT_INSERT: _LAT_INSERT.
  _LAT_STAGE: _LAT_STAGE.
  _LAT_SCATTER: _LAT_SCATTER.
  _StageInFlight.num_blocks: _StageInFlight#num_blocks.
  _StageInFlight._signal_lock: _StageInFlight#_signal_lock.
  _LatencyTracker: _LatencyTracker#
  _LatencyTracker._who: _LatencyTracker#_who.
  _LatencyTracker._lock: _LatencyTracker#_lock.
  ZmqShmKvConnectorBase.config: ZmqShmKvConnectorBase#config.
  ZmqShmKvConnectorBase._coord_setup: ZmqShmKvConnectorBase#_coord_setup().
  ZmqShmKvConnectorBase._coord_sockets_lock: ZmqShmKvConnectorBase#_coord_sockets_lock.
  _LatencyTracker.__init__: _LatencyTracker#__init__().
  ZmqShmKvConnectorBase.__init__: ZmqShmKvConnectorBase#__init__().
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py)

## Classes
### <a id="ZmqShmKvConnectorBase"></a>`ZmqShmKvConnectorBase`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py:278`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L278)
- doc: Generic shm-staged, ZMQ-coordinated KV connector worker.
- signature: `class ZmqShmKvConnectorBase:`
- members:
  - <a id="ZmqShmKvConnectorBase._build_pool_spec"></a>`_build_pool_spec(self)` — [`L683`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L683) — Build the per-host shm pool spec. Subclasses
  - <a id="ZmqShmKvConnectorBase._complete_stage_entry"></a>`_complete_stage_entry(self, entry: _StageInFlight, failed: bool)` — [`L1320`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1320) — Run completion side-effects exactly once per entry.
  - <a id="ZmqShmKvConnectorBase._coord_attach_shm_with_retry"></a>`_coord_attach_shm_with_retry(self, spec: Any, name: str)` — [`L765`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L765) — Non-rank-0 ranks may race ahead of rank 0. Poll the shm name a
  - <a id="ZmqShmKvConnectorBase._coord_broadcast"></a>`_coord_broadcast(self, tag: bytes, payload)` — [`L897`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L897) — Coordinator -> every known non-zero rank. Enqueues one frame per
  - <a id="ZmqShmKvConnectorBase._coord_ipc_drain_outbound"></a>`_coord_ipc_drain_outbound(self)` — [`L906`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L906) — Pop any pending outbound messages and send them. Called from
  - <a id="ZmqShmKvConnectorBase._coord_rank0_external_data_loop"></a>`_coord_rank0_external_data_loop(self, channel_idx: int)` — [`L2288`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2288) — One data server per TCP channel. channel_idx in [0, n_channels).
  - <a id="ZmqShmKvConnectorBase._coord_rank0_handle_new_send"></a>`_coord_rank0_handle_new_send(self, req_id: ReqId, req_meta: SendMeta)` — [`L1004`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1004) — Allocate a slot, broadcast the assignment to non-zero ranks, and — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="ZmqShmKvConnectorBase._coord_rank0_pull"></a>`_coord_rank0_pull(self, entry: _CoordRecvEntry)` — [`L1511`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1511) — Pull the full KV blob (all ranks' shards) from remote coord for all hosts — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="ZmqShmKvConnectorBase._coord_scatter_shard"></a>`_coord_scatter_shard(self, slot_idx: int, num_blocks: int, local_blocks: list[int])` — [`L1831`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1831) — H2D + scatter this rank's shard from shm into the kv cache. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="ZmqShmKvConnectorBase._coord_send_ipc"></a>`_coord_send_ipc(self, tag: bytes, payload)` — [`L890`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L890) — Worker (non-zero rank) -> coordinator. Enqueues a DEALER frame.
  - <a id="ZmqShmKvConnectorBase._coord_setup"></a>`_coord_setup(self)` — [`L738`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L738) — Allocate the shm pool, bind ZMQ endpoints, spawn threads. Called
  - <a id="ZmqShmKvConnectorBase._coord_stage_shard"></a>`_coord_stage_shard(self, uuid: int, slot_idx: int, num_blocks: int, block_ids: list[int])` — [`L1158`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1158) — Issue an async D2H batch for this rank's shard and enqueue the
  - <a id="ZmqShmKvConnectorBase._coord_stage_wait_worker"></a>`_coord_stage_wait_worker(self, entry: _StageInFlight)` — [`L1275`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1275) — Pool worker: block on the entry's stage future and complete.
  - <a id="ZmqShmKvConnectorBase._coord_stage_waiter_loop"></a>`_coord_stage_waiter_loop(self)` — [`L1216`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1216) — Dispatch each pending stage entry to the waiter pool and enforce
  - <a id="ZmqShmKvConnectorBase._coord_worker_stage_inline"></a>`_coord_worker_stage_inline(self, uuid: int, req_id: ReqId, timeout: float = 10)` — [`L1096`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1096) — Non-zero rank, main-thread path: wait for STAGE_NOTIFY to arrive
  - <a id="ZmqShmKvConnectorBase._coord_worker_wait_load"></a>`_coord_worker_wait_load(self, uuid: int, timeout: float = 1)` — [`L2026`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2026) — Block until LOAD_NOTIFY or LOAD_SKIP for uuid arrives, or timeout
  - <a id="ZmqShmKvConnectorBase._extract_kv_layout"></a>`_extract_kv_layout(self)` — [`L513`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L513) — Default (uniform) layout: every kv cache layer has the same shape
  - <a id="ZmqShmKvConnectorBase._h2d_into_device"></a>`_h2d_into_device(self, src_views: list)` — [`L2739`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2739) — Copy the shm data into HBM synchronously.
  - <a id="ZmqShmKvConnectorBase._h2d_into_device_async"></a>`_h2d_into_device_async(self, src_views: list)` — [`L2743`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2743) — Async _h2d_into_device.
  - <a id="ZmqShmKvConnectorBase._init_coord_state"></a>`_init_coord_state(self)` — [`L349`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L349) — Minimum state needed on both rank-0 and the other ranks. The
  - <a id="ZmqShmKvConnectorBase._maybe_enable_kv_scatter"></a>`_maybe_enable_kv_scatter(self)` — [`L1151`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1151) — Subclass hook: optionally enable the multi-layer fused scatter
  - <a id="ZmqShmKvConnectorBase._pool_attach"></a>`_pool_attach(self, spec: Any, shm_name: str)` — [`L734`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L734) — Non-rank-0: attach to the per-host shm pool.
  - <a id="ZmqShmKvConnectorBase._pool_create"></a>`_pool_create(self, spec: Any, shm_name: str)` — [`L730`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L730) — Rank-0: create the per-host shm pool.
  - <a id="ZmqShmKvConnectorBase._pull_channel"></a>`_pull_channel(h: int, ch: int)` — [`L1550`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1550) — Pull one channel's subset of ranks AND unpack their layer
  - <a id="ZmqShmKvConnectorBase._replace_runner_kv_cache"></a>`_replace_runner_kv_cache(self, layer_idx: int, new_cache: torch.Tensor)` — [`L535`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L535) — Replace a runner KV cache and keep attention layers bound to it.
  - <a id="ZmqShmKvConnectorBase._signal_stage_done"></a>`_signal_stage_done(self, uuid: int, failed: bool = False)` — [`L1334`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1334) — Mark this rank's STAGE_DONE on the rank-0 send entry. On rank 0
  - <a id="ZmqShmKvConnectorBase._stage_d2h"></a>`_stage_d2h(self, slot_idx: int, num_blocks: int, block_ids: list[int])` — [`L2723`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2723) — Issue an async device->host transfer of this rank's shard.
  - <a id="ZmqShmKvConnectorBase._stage_d2h_sync"></a>`_stage_d2h_sync(self, slot_idx: int, num_blocks: int, block_ids: list[int])` — [`L2729`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2729) — Synchronous variant of ``_stage_d2h``.
  - <a id="ZmqShmKvConnectorBase._wait_stage"></a>`_wait_stage(self, future: Any)` — [`L2735`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2735) — Block on a future returned by ``_stage_d2h``.
  - <a id="ZmqShmKvConnectorBase._warmup_block_sizes"></a>`_warmup_block_sizes(self)` — [`L558`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L558) — Block count to pre-compile: the worst-case max_blocks only.
  - <a id="ZmqShmKvConnectorBase._warmup_coord_once"></a>`_warmup_coord_once(self, num_blocks: int)` — [`L603`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L603) — TP>1 coord path: warmup using slot 0 of the shm pool. No traffic
  - <a id="ZmqShmKvConnectorBase._warmup_kv_ops"></a>`_warmup_kv_ops(self)` — [`L565`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L565) — Pre-compile the XLA executables for the KV gather/scatter hot
  - <a id="ZmqShmKvConnectorBase.get_finished"></a>`get_finished(self, finished_req_ids: set[str] | None = None)` — [`L668`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L668)
  - <a id="ZmqShmKvConnectorBase.get_kv_connector_stats"></a>`get_kv_connector_stats(self)` — [`L2758`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2758) — Get the KV transfer stats for the worker. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="ZmqShmKvConnectorBase.process_send_load"></a>`process_send_load(self, metadata: TPUConnectorMetadata)` — [`L647`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L647)
  - <a id="ZmqShmKvConnectorBase.register_runner"></a>`register_runner(self, runner: Any)` — [`L478`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L478)
  - <a id="ZmqShmKvConnectorBase.config"></a>`config` — [`L291`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L291)
  - <a id="ZmqShmKvConnectorBase.device"></a>`device` — [`L295`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L295)
  - <a id="ZmqShmKvConnectorBase.dp_rank"></a>`dp_rank` — [`L298`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L298)
  - <a id="ZmqShmKvConnectorBase.dtype"></a>`dtype` — [`L521`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L521)
  - <a id="ZmqShmKvConnectorBase.host_ip"></a>`host_ip` — [`L310`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L310)
  - <a id="ZmqShmKvConnectorBase.is_producer"></a>`is_producer` — [`L292`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L292)
  - <a id="ZmqShmKvConnectorBase.kv_transfer_port"></a>`kv_transfer_port` — [`L311`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L311)
  - <a id="ZmqShmKvConnectorBase.local_tp_rank"></a>`local_tp_rank` — [`L307`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L307)
  - <a id="ZmqShmKvConnectorBase.multi_host"></a>`multi_host` — [`L296`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L296)
  - <a id="ZmqShmKvConnectorBase.node_id"></a>`node_id` — [`L297`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L297) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="ZmqShmKvConnectorBase.num_layers"></a>`num_layers` — [`L519`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L519)
  - <a id="ZmqShmKvConnectorBase.ranks_per_host"></a>`ranks_per_host` — [`L306`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L306)
  - <a id="ZmqShmKvConnectorBase.runner"></a>`runner` — [`L294`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L294)
  - <a id="ZmqShmKvConnectorBase.shape"></a>`shape` — [`L520`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L520)
  - <a id="ZmqShmKvConnectorBase.side_channel_port"></a>`side_channel_port` — [`L314`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L314)
  - <a id="ZmqShmKvConnectorBase.tp_rank"></a>`tp_rank` — [`L304`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L304)
  - <a id="ZmqShmKvConnectorBase.tp_size"></a>`tp_size` — [`L305`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L305)
  - <a id="ZmqShmKvConnectorBase.transfer_stats"></a>`transfer_stats` — [`L331`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L331) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="ZmqShmKvConnectorBase.vllm_config"></a>`vllm_config` — [`L288`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L288)
  - <a id="ZmqShmKvConnectorBase.zmq_cxt"></a>`zmq_cxt` — [`L323`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L323)
- protocol/private: <a id="ZmqShmKvConnectorBase.__del__"></a>`__del__`[`L471`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L471), <a id="ZmqShmKvConnectorBase.__init__"></a>`__init__`[`L285`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L285), <a id="ZmqShmKvConnectorBase._blocks_token"></a>`_blocks_token`[`L523`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L523), <a id="ZmqShmKvConnectorBase._coord_channel_executor"></a>`_coord_channel_executor`[`L397`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L397), <a id="ZmqShmKvConnectorBase._coord_done_recving"></a>`_coord_done_recving`[`L426`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L426), <a id="ZmqShmKvConnectorBase._coord_done_sending"></a>`_coord_done_sending`[`L417`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L417), <a id="ZmqShmKvConnectorBase._coord_drain_scatter"></a>`_coord_drain_scatter`[`L1806`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1806), <a id="ZmqShmKvConnectorBase._coord_executor"></a>`_coord_executor`[`L394`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L394), <a id="ZmqShmKvConnectorBase._coord_get_finished"></a>`_coord_get_finished`[`L2653`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2653), <a id="ZmqShmKvConnectorBase._coord_ipc_out"></a>`_coord_ipc_out`[`L376`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L376), <a id="ZmqShmKvConnectorBase._coord_ipc_sock"></a>`_coord_ipc_sock`[`L372`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L372), <a id="ZmqShmKvConnectorBase._coord_local_to_global_rank"></a>`_coord_local_to_global_rank`[`L379`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L379), <a id="ZmqShmKvConnectorBase._coord_lock"></a>`_coord_lock`[`L454`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L454), <a id="ZmqShmKvConnectorBase._coord_notif_sockets"></a>`_coord_notif_sockets`[`L844`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L844), <a id="ZmqShmKvConnectorBase._coord_pool"></a>`_coord_pool`[`L287`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L287), <a id="ZmqShmKvConnectorBase._coord_pool_spec"></a>`_coord_pool_spec`[`L741`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L741), <a id="ZmqShmKvConnectorBase._coord_process_send_load"></a>`_coord_process_send_load`[`L955`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L955), <a id="ZmqShmKvConnectorBase._coord_rank0_build_pull_response"></a>`_coord_rank0_build_pull_response`[`L2444`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2444), <a id="ZmqShmKvConnectorBase._coord_rank0_expire_loop"></a>`_coord_rank0_expire_loop`[`L2624`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2624), <a id="ZmqShmKvConnectorBase._coord_rank0_external_notif_loop"></a>`_coord_rank0_external_notif_loop`[`L2573`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2573), <a id="ZmqShmKvConnectorBase._coord_rank0_handle_new_load"></a>`_coord_rank0_handle_new_load`[`L1383`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1383), <a id="ZmqShmKvConnectorBase._coord_rank0_ipc_loop"></a>`_coord_rank0_ipc_loop`[`L2047`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2047), <a id="ZmqShmKvConnectorBase._coord_rank0_register_copy"></a>`_coord_rank0_register_copy`[`L1944`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1944), <a id="ZmqShmKvConnectorBase._coord_rank0_send_notify"></a>`_coord_rank0_send_notify`[`L1977`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1977), <a id="ZmqShmKvConnectorBase._coord_rank_to_identity"></a>`_coord_rank_to_identity`[`L431`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L431), <a id="ZmqShmKvConnectorBase._coord_recv"></a>`_coord_recv`[`L428`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L428), <a id="ZmqShmKvConnectorBase._coord_scatter_and_ack"></a>`_coord_scatter_and_ack`[`L1768`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L1768), <a id="ZmqShmKvConnectorBase._coord_send"></a>`_coord_send`[`L414`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L414), <a id="ZmqShmKvConnectorBase._coord_setup_rank0"></a>`_coord_setup_rank0`[`L781`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L781), <a id="ZmqShmKvConnectorBase._coord_setup_worker"></a>`_coord_setup_worker`[`L848`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L848), <a id="ZmqShmKvConnectorBase._coord_sockets_lock"></a>`_coord_sockets_lock`[`L845`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L845), <a id="ZmqShmKvConnectorBase._coord_stage_wait_timeout_s"></a>`_coord_stage_wait_timeout_s`[`L469`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L469), <a id="ZmqShmKvConnectorBase._coord_stage_waiter_pool"></a>`_coord_stage_waiter_pool`[`L465`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L465), <a id="ZmqShmKvConnectorBase._coord_teardown"></a>`_coord_teardown`[`L932`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L932), <a id="ZmqShmKvConnectorBase._coord_threads"></a>`_coord_threads`[`L286`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L286), <a id="ZmqShmKvConnectorBase._coord_worker_ipc_loop"></a>`_coord_worker_ipc_loop`[`L2190`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2190), <a id="ZmqShmKvConnectorBase._coord_workers_ready"></a>`_coord_workers_ready`[`L438`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L438), <a id="ZmqShmKvConnectorBase._is_host_coordinator"></a>`_is_host_coordinator`[`L308`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L308), <a id="ZmqShmKvConnectorBase._kv_scatter_enabled"></a>`_kv_scatter_enabled`[`L370`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L370), <a id="ZmqShmKvConnectorBase._kv_transfer_ports"></a>`_kv_transfer_ports`[`L360`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L360), <a id="ZmqShmKvConnectorBase._lat"></a>`_lat`[`L326`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L326), <a id="ZmqShmKvConnectorBase._n_channels"></a>`_n_channels`[`L359`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L359), <a id="ZmqShmKvConnectorBase._prepare_response"></a>`_prepare_response`[`L2324`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2324), <a id="ZmqShmKvConnectorBase._pull_response_header"></a>`_pull_response_header`[`L526`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L526), <a id="ZmqShmKvConnectorBase._resolve_remote_host_port"></a>`_resolve_remote_host_port`[`L650`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L650), <a id="ZmqShmKvConnectorBase._send_ready_responses"></a>`_send_ready_responses`[`L2340`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2340), <a id="ZmqShmKvConnectorBase._stage_pending_q"></a>`_stage_pending_q`[`L463`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L463), <a id="ZmqShmKvConnectorBase._stop_event"></a>`_stop_event`[`L324`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L324), <a id="ZmqShmKvConnectorBase._synchronize_device"></a>`_synchronize_device`[`L2747`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2747), <a id="ZmqShmKvConnectorBase._try_fast_scatter"></a>`_try_fast_scatter`[`L2750`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2750), <a id="ZmqShmKvConnectorBase._worker_pending_load"></a>`_worker_pending_load`[`L450`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L450), <a id="ZmqShmKvConnectorBase._worker_pending_load_cv"></a>`_worker_pending_load_cv`[`L451`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L451), <a id="ZmqShmKvConnectorBase._worker_pending_stage"></a>`_worker_pending_stage`[`L446`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L446), <a id="ZmqShmKvConnectorBase._worker_pending_stage_cv"></a>`_worker_pending_stage_cv`[`L447`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L447)
- uses (calls/refs, reference-scoped): [`logger`](zmq_shm_base.md#logger), [`_maybe_enable_kv_scatter`](tpu_connector.md#TPUConnectorWorker._maybe_enable_kv_scatter), [`record`](zmq_shm_base.md#_LatencyTracker.record), [`uuid`](connector_metadata.md#LoadMeta.uuid), [`get_p2p_wait_pull_timeout`](../utils.md#get_p2p_wait_pull_timeout), [`layer_view`](host_kv_shm.md#HostKVShmPool.layer_view), [`req_id`](zmq_shm_base.md#_CoordRecvEntry.req_id), [`TPUConnectorMetadata`](connector_metadata.md#TPUConnectorMetadata), [`local_block_ids`](connector_metadata.md#LoadMeta.local_block_ids), [`create`](host_kv_shm.md#HostKVShmPool.create), [`rank_layer_views`](host_kv_shm.md#HostKVShmPool.rank_layer_views), [`unpack_rank_layers`](host_kv_shm.md#HostKVShmPool.unpack_rank_layers), [`remote_host`](connector_metadata.md#LoadMeta.remote_host), [`LoadMeta`](connector_metadata.md#LoadMeta), [`ReqId`](connector_metadata.md#ReqId), [`remote_block_ids`](connector_metadata.md#LoadMeta.remote_block_ids), [`reqs_to_send`](connector_metadata.md#TPUConnectorMetadata.reqs_to_send), [`remote_port`](connector_metadata.md#LoadMeta.remote_port), [`uuid`](connector_metadata.md#SendMeta.uuid), [`uuid`](zmq_shm_base.md#_CoordRecvEntry.uuid), [`release_slot`](host_kv_shm.md#HostKVShmPool.release_slot), [`reqs_to_load`](connector_metadata.md#TPUConnectorMetadata.reqs_to_load), [`attach`](host_kv_shm.md#HostKVShmPool.attach), [`close`](host_kv_shm.md#HostKVShmPool.close), [`TpuKVConnectorStats`](tpu_connector_stats.md#TpuKVConnectorStats), [`_try_fast_scatter`](tpu_connector.md#TPUConnectorWorker._try_fast_scatter), [`local_block_ids`](connector_metadata.md#SendMeta.local_block_ids), [`num_layers`](host_kv_shm.md#PoolSpec.num_layers), [`remote_side_channel_port`](connector_metadata.md#LoadMeta.remote_side_channel_port), [`slot_idx`](zmq_shm_base.md#_CoordRecvEntry.slot_idx), [`staged_events`](zmq_shm_base.md#_CoordSendEntry.staged_events), [`req_id`](zmq_shm_base.md#_CoordSendEntry.req_id), [`SendMeta`](connector_metadata.md#SendMeta), [`TPU_MULTIHOST_BACKEND`](../../envs.md#TPU_MULTIHOST_BACKEND), [`acquire_slot`](host_kv_shm.md#HostKVShmPool.acquire_slot), [`clone_and_reset`](tpu_connector_stats.md#TpuKVConnectorStats.clone_and_reset), [`expiration_time`](zmq_shm_base.md#_CoordSendEntry.expiration_time), [`local_blocks`](zmq_shm_base.md#_CoordRecvEntry.local_blocks), [`num_blocks`](zmq_shm_base.md#_CoordRecvEntry.num_blocks), [`pull_ok`](zmq_shm_base.md#_CoordRecvEntry.pull_ok)  (+87 more)
- used by: [`_maybe_enable_kv_scatter`](tpu_connector.md#TPUConnectorWorker._maybe_enable_kv_scatter), [`_build_d2h_views`](tpu_connector.md#TPUConnectorWorker._build_d2h_views), [`_try_fast_scatter`](tpu_connector.md#TPUConnectorWorker._try_fast_scatter), [`process_send_load`](tpu_connector.md#TPUConnectorWorker.process_send_load), [`TPUConnectorWorker`](tpu_connector.md#TPUConnectorWorker), [`_h2d_into_device`](tpu_connector.md#TPUConnectorWorker._h2d_into_device), [`_h2d_into_device_async`](tpu_connector.md#TPUConnectorWorker._h2d_into_device_async)

### <a id="_CoordRecvEntry"></a>`_CoordRecvEntry`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py:189`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L189)
- signature: `class _CoordRecvEntry:`
- members:
  - <a id="_CoordRecvEntry.copied"></a>`copied` — [`L203`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L203)
  - <a id="_CoordRecvEntry.load_complete"></a>`load_complete` — [`L200`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L200)
  - <a id="_CoordRecvEntry.local_blocks"></a>`local_blocks` — [`L194`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L194)
  - <a id="_CoordRecvEntry.num_blocks"></a>`num_blocks` — [`L193`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L193)
  - <a id="_CoordRecvEntry.pull_ok"></a>`pull_ok` — [`L205`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L205)
  - <a id="_CoordRecvEntry.remote_blocks"></a>`remote_blocks` — [`L195`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L195)
  - <a id="_CoordRecvEntry.remote_host"></a>`remote_host` — [`L196`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L196)
  - <a id="_CoordRecvEntry.remote_port"></a>`remote_port` — [`L197`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L197)
  - <a id="_CoordRecvEntry.remote_side_channel_port"></a>`remote_side_channel_port` — [`L198`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L198)
  - <a id="_CoordRecvEntry.reported_done"></a>`reported_done` — [`L208`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L208)
  - <a id="_CoordRecvEntry.req_id"></a>`req_id` — [`L190`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L190)
  - <a id="_CoordRecvEntry.slot_idx"></a>`slot_idx` — [`L192`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L192)
  - <a id="_CoordRecvEntry.uuid"></a>`uuid` — [`L191`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L191)
- uses (calls/refs, reference-scoped): [`ReqId`](connector_metadata.md#ReqId)
- used by: [`_coord_rank0_ipc_loop`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_ipc_loop), [`_coord_rank0_handle_new_load`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_handle_new_load), [`_coord_rank0_pull`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_pull), [`_coord_rank0_handle_new_send`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_handle_new_send), [`_coord_rank0_register_copy`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_register_copy), [`_coord_get_finished`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_get_finished), [`_coord_drain_scatter`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_drain_scatter), [`_pull_channel`](zmq_shm_base.md#ZmqShmKvConnectorBase._pull_channel), [`_coord_recv`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_recv)

### <a id="_CoordSendEntry"></a>`_CoordSendEntry`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py:155`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L155)
- signature: `class _CoordSendEntry:`
- members:
  - <a id="_CoordSendEntry.expiration_time"></a>`expiration_time` — [`L159`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L159)
  - <a id="_CoordSendEntry.num_blocks"></a>`num_blocks` — [`L158`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L158)
  - <a id="_CoordSendEntry.pull_acked"></a>`pull_acked` — [`L177`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L177)
  - <a id="_CoordSendEntry.req_id"></a>`req_id` — [`L156`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L156)
  - <a id="_CoordSendEntry.slot_idx"></a>`slot_idx` — [`L157`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L157)
  - <a id="_CoordSendEntry.stage_complete"></a>`stage_complete` — [`L174`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L174)
  - <a id="_CoordSendEntry.stage_failed"></a>`stage_failed` — [`L181`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L181)
  - <a id="_CoordSendEntry.staged"></a>`staged` — [`L166`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L166)
  - <a id="_CoordSendEntry.staged_events"></a>`staged_events` — [`L171`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L171)
  - <a id="_CoordSendEntry.tp_size"></a>`tp_size` — [`L163`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L163)
- protocol/private: <a id="_CoordSendEntry.__post_init__"></a>`__post_init__`[`L183`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L183)
- uses (calls/refs, reference-scoped): [`ReqId`](connector_metadata.md#ReqId)
- used by: [`_coord_rank0_ipc_loop`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_ipc_loop), [`_coord_rank0_handle_new_load`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_handle_new_load), [`_coord_rank0_handle_new_send`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_handle_new_send), [`_coord_rank0_build_pull_response`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_build_pull_response), [`_coord_get_finished`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_get_finished), [`_signal_stage_done`](zmq_shm_base.md#ZmqShmKvConnectorBase._signal_stage_done), [`_coord_rank0_expire_loop`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_expire_loop), [`_coord_rank0_external_notif_loop`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_external_notif_loop), [`_coord_send`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_send), [`_pull_response_header`](zmq_shm_base.md#ZmqShmKvConnectorBase._pull_response_header)

### <a id="_LatencyTracker"></a>`_LatencyTracker`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py:235`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L235)
- doc: Running per-phase latency stats + periodic summary log.
- signature: `class _LatencyTracker:`
- members:
  - <a id="_LatencyTracker.record"></a>`record(self, phase: str, duration_ms: float)` — [`L251`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L251)
- protocol/private: <a id="_LatencyTracker.__init__"></a>`__init__`[`L243`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L243), <a id="_LatencyTracker._last_log"></a>`_last_log`[`L249`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L249), <a id="_LatencyTracker._lock"></a>`_lock`[`L246`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L246), <a id="_LatencyTracker._log_interval_s"></a>`_log_interval_s`[`L245`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L245), <a id="_LatencyTracker._stats"></a>`_stats`[`L248`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L248), <a id="_LatencyTracker._who"></a>`_who`[`L244`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L244)
- uses (calls/refs, reference-scoped): [`logger`](zmq_shm_base.md#logger)
- used by: [`_coord_rank0_pull`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_rank0_pull), [`_coord_scatter_shard`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_scatter_shard), [`_coord_stage_wait_worker`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_stage_wait_worker), [`_lat`](zmq_shm_base.md#ZmqShmKvConnectorBase._lat)

### <a id="_StageInFlight"></a>`_StageInFlight`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py:212`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L212)
- doc: A pending async D2H batch waiting on its PjRt future.
- signature: `class _StageInFlight:`
- members:
  - <a id="_StageInFlight.cpu_tensors"></a>`cpu_tensors` — [`L227`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L227)
  - <a id="_StageInFlight.enqueue_t0"></a>`enqueue_t0` — [`L228`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L228)
  - <a id="_StageInFlight.future"></a>`future` — [`L225`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L225)
  - <a id="_StageInFlight.issue_t1"></a>`issue_t1` — [`L229`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L229)
  - <a id="_StageInFlight.num_blocks"></a>`num_blocks` — [`L224`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L224)
  - <a id="_StageInFlight.slot_idx"></a>`slot_idx` — [`L223`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L223)
  - <a id="_StageInFlight.total_bytes"></a>`total_bytes` — [`L230`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L230)
  - <a id="_StageInFlight.tpu_tensors"></a>`tpu_tensors` — [`L226`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L226)
  - <a id="_StageInFlight.uuid"></a>`uuid` — [`L222`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L222)
- protocol/private: <a id="_StageInFlight._signal_lock"></a>`_signal_lock`[`L231`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L231), <a id="_StageInFlight._signaled"></a>`_signaled`[`L232`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L232)
- used by: [`_coord_stage_wait_worker`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_stage_wait_worker), [`_coord_stage_shard`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_stage_shard), [`_coord_stage_waiter_loop`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_stage_waiter_loop), [`_complete_stage_entry`](zmq_shm_base.md#ZmqShmKvConnectorBase._complete_stage_entry)

## Functions
- <a id="_get_default_ipc_key"></a>`_get_default_ipc_key()` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L83)
- <a id="_secure_dumps"></a>`_secure_dumps(obj: Any)` — [`L102`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L102) — Serialize payload with an HMAC-SHA256 signature to prevent
- <a id="_secure_loads"></a>`_secure_loads(data: bytes)` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L110) — Verify HMAC-SHA256 signature before deserializing payload.
- <a id="_try_remove_ipc_endpoint"></a>`_try_remove_ipc_endpoint(ipc_path: str)` — [`L2779`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L2779) — ZMQ's ipc:// backs onto a filesystem path; a stale file from a

## Module values
- <a id="_IPC_AUTH_KEY._IPC_AUTH_KEY"></a>`_IPC_AUTH_KEY` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L99)
- <a id="_IPC_COPY_DONE"></a>`_IPC_COPY_DONE` — [`L149`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L149)
- <a id="_IPC_DROP"></a>`_IPC_DROP` — [`L150`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L150)
- <a id="_IPC_HELLO"></a>`_IPC_HELLO` — [`L140`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L140)
- <a id="_IPC_LOAD_NOTIFY"></a>`_IPC_LOAD_NOTIFY` — [`L143`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L143)
- <a id="_IPC_LOAD_SKIP"></a>`_IPC_LOAD_SKIP` — [`L146`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L146)
- <a id="_IPC_STAGE_DONE"></a>`_IPC_STAGE_DONE` — [`L142`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L142)
- <a id="_IPC_STAGE_NOTIFY"></a>`_IPC_STAGE_NOTIFY` — [`L141`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L141)
- <a id="_LAT_D2H"></a>`_LAT_D2H` — [`L131`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L131)
- <a id="_LAT_H2D"></a>`_LAT_H2D` — [`L134`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L134)
- <a id="_LAT_INSERT"></a>`_LAT_INSERT` — [`L135`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L135)
- <a id="_LAT_SCATTER"></a>`_LAT_SCATTER` — [`L137`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L137)
- <a id="_LAT_STAGE"></a>`_LAT_STAGE` — [`L136`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L136)
- <a id="_LAT_UNPACK"></a>`_LAT_UNPACK` — [`L133`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L133)
- <a id="_LAT_WIRE"></a>`_LAT_WIRE` — [`L132`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L132)
- <a id="_MSG_ERR"></a>`_MSG_ERR` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L127)
- <a id="_MSG_OK"></a>`_MSG_OK` — [`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L126)
- <a id="_MSG_PULL"></a>`_MSG_PULL` — [`L125`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L125)
- <a id="logger"></a>`logger` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/zmq_shm_base.py#L80)

