---
title: 'Module: src/vllm_torchtpu/offload/raiden_connector.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/offload/raiden_connector.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.offload.raiden_connector`/
symbols:
  TPURaidenOffloadingScheduler.build_connector_meta: TPURaidenOffloadingScheduler#build_connector_meta().
  TPURaidenOffloadingConnector.get_transfer_results: TPURaidenOffloadingConnector#get_transfer_results().
  TPURaidenOffloadingScheduler.update_connector_output: TPURaidenOffloadingScheduler#update_connector_output().
  TPURaidenOffloadingConnector.connector_worker: TPURaidenOffloadingConnector#connector_worker.
  TPURaidenOffloadingConnector.build_connector_worker_meta: TPURaidenOffloadingConnector#build_connector_worker_meta().
  TPURaidenOffloadingScheduler._fence_pending: TPURaidenOffloadingScheduler#_fence_pending.
  RaidenOffloadingWorkerMetadata.fenced_jobs: RaidenOffloadingWorkerMetadata#fenced_jobs.
  TPURaidenOffloadingConnector.connector_scheduler: TPURaidenOffloadingConnector#connector_scheduler.
  RaidenOffloadingWorkerMetadata.aggregate: RaidenOffloadingWorkerMetadata#aggregate().
  TPURaidenOffloadingScheduler.__init__: TPURaidenOffloadingScheduler#__init__().
  TPURaidenOffloadingConnector.__init__: TPURaidenOffloadingConnector#__init__().
  TPURaidenOffloadingConnector._completed_jobs: TPURaidenOffloadingConnector#_completed_jobs.
  TPURaidenOffloadingConnector.register_kv_caches: TPURaidenOffloadingConnector#register_kv_caches().
  logger: logger.
  TPURaidenOffloadingScheduler._raiden_manager: TPURaidenOffloadingScheduler#_raiden_manager.
  RaidenOffloadingWorkerMetadata: RaidenOffloadingWorkerMetadata#
  TPURaidenOffloadingConnector._fenced_jobs: TPURaidenOffloadingConnector#_fenced_jobs.
  TPURaidenOffloadingConnector._pending_fences: TPURaidenOffloadingConnector#_pending_fences.
  RaidenOffloadingConnectorMetadata.fence_job_ids: RaidenOffloadingConnectorMetadata#fence_job_ids.
  _ParkedStore.keys: _ParkedStore#keys.
  _ParkedStore.acks: _ParkedStore#acks.
  TPURaidenOffloadingConnector._pool_sync_tensors: TPURaidenOffloadingConnector#_pool_sync_tensors.
  TPURaidenOffloadingConnector.prefer_cross_layer_blocks: TPURaidenOffloadingConnector#prefer_cross_layer_blocks().
  TPURaidenOffloadingConnector.supports_divergent_local_hybrid_hits: TPURaidenOffloadingConnector#supports_divergent_local_hybrid_hits().
  TPURaidenOffloadingConnector.reset_cache: TPURaidenOffloadingConnector#reset_cache().
  TPURaidenOffloadingConnector.take_events: TPURaidenOffloadingConnector#take_events().
  TPURaidenOffloadingConnector.get_finished: TPURaidenOffloadingConnector#get_finished().
  RaidenOffloadingConnectorMetadata: RaidenOffloadingConnectorMetadata#
  RaidenOffloadingConnectorMetadata.finished_store_job_ids: RaidenOffloadingConnectorMetadata#finished_store_job_ids.
  RaidenOffloadingConnectorMetadata.finished_load_jobs: RaidenOffloadingConnectorMetadata#finished_load_jobs.
  RaidenOffloadingConnectorMetadata.failed_load_req_ids: RaidenOffloadingConnectorMetadata#failed_load_req_ids.
  _ParkedStore: _ParkedStore#
  _ParkedStore.device_block_ids: _ParkedStore#device_block_ids.
  TPURaidenOffloadingScheduler: TPURaidenOffloadingScheduler#
  _enqueue_pool_writes: _enqueue_pool_writes().
  _record_fence_event: _record_fence_event().
  _event_is_retired: _event_is_retired().
  TPURaidenOffloadingConnector: TPURaidenOffloadingConnector#
  TPURaidenOffloadingConnector.get_required_kvcache_layout: TPURaidenOffloadingConnector#get_required_kvcache_layout().
---
# Module: [`src/vllm_torchtpu/offload/raiden_connector.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py)

## Classes
### <a id="RaidenOffloadingConnectorMetadata"></a>`RaidenOffloadingConnectorMetadata`
- def: [`src/vllm_torchtpu/offload/raiden_connector.py:145`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L145)
- doc: Scheduler -&gt; worker metadata.
- signature: `class RaidenOffloadingConnectorMetadata(OffloadingConnectorMetadata):`
- members:
  - <a id="RaidenOffloadingConnectorMetadata.failed_load_req_ids"></a>`failed_load_req_ids` — [`L161`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L161)
  - <a id="RaidenOffloadingConnectorMetadata.fence_job_ids"></a>`fence_job_ids` — [`L153`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L153)
  - <a id="RaidenOffloadingConnectorMetadata.finished_load_jobs"></a>`finished_load_jobs` — [`L157`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L157)
  - <a id="RaidenOffloadingConnectorMetadata.finished_store_job_ids"></a>`finished_store_job_ids` — [`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L155)
- used by: [`build_connector_meta`](raiden_connector.md#TPURaidenOffloadingScheduler.build_connector_meta), [`get_transfer_results`](raiden_connector.md#TPURaidenOffloadingConnector.get_transfer_results)

### <a id="RaidenOffloadingWorkerMetadata"></a>`RaidenOffloadingWorkerMetadata`
- def: [`src/vllm_torchtpu/offload/raiden_connector.py:165`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L165)
- doc: Worker -&gt; scheduler metadata: contains completed-job echoes and
- signature: `class RaidenOffloadingWorkerMetadata(OffloadingWorkerMetadata):`
- members:
  - <a id="RaidenOffloadingWorkerMetadata.aggregate"></a>`aggregate(self, other)` — [`L171`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L171)
  - <a id="RaidenOffloadingWorkerMetadata.fenced_jobs"></a>`fenced_jobs` — [`L169`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L169)
- used by: [`update_connector_output`](raiden_connector.md#TPURaidenOffloadingScheduler.update_connector_output), [`build_connector_worker_meta`](raiden_connector.md#TPURaidenOffloadingConnector.build_connector_worker_meta)

### <a id="TPURaidenOffloadingConnector"></a>`TPURaidenOffloadingConnector`
- def: [`src/vllm_torchtpu/offload/raiden_connector.py:324`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L324)
- doc: Top-level facade connector for the store-backed (V2) raiden KV offload path.
- signature: `class TPURaidenOffloadingConnector(OffloadingConnector):`
- members:
  - <a id="TPURaidenOffloadingConnector.build_connector_worker_meta"></a>`build_connector_worker_meta(self)` — [`L555`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L555)
  - <a id="TPURaidenOffloadingConnector.get_finished"></a>`get_finished(self, finished_req_ids: set[str])` — [`L498`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L498)
  - <a id="TPURaidenOffloadingConnector.get_required_kvcache_layout"></a>`get_required_kvcache_layout(cls, vllm_config: VllmConfig)` — [`L328`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L328) — No layout preference, unlike the `OffloadingConnector` this extends.
  - <a id="TPURaidenOffloadingConnector.get_transfer_results"></a>`get_transfer_results(self, finished_req_ids: set[str])` — [`L511`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L511) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="TPURaidenOffloadingConnector.prefer_cross_layer_blocks"></a>`prefer_cross_layer_blocks(self)` — [`L338`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L338)
  - <a id="TPURaidenOffloadingConnector.register_kv_caches"></a>`register_kv_caches(self, kv_caches: Mapping[str, torch.Tensor | list[torch.Tensor]])` — [`L434`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L434) — Register the TPU UBP as zero-copy canonical offload tensors.
  - <a id="TPURaidenOffloadingConnector.reset_cache"></a>`reset_cache(self)` — [`L418`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L418)
  - <a id="TPURaidenOffloadingConnector.supports_divergent_local_hybrid_hits"></a>`supports_divergent_local_hybrid_hits(self)` — [`L345`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L345) — Complete a deeper full-attention local hit, behind the Stage-3 flag. — documented in [kv-transfer-and-disaggregated-serving](../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenOffloadingConnector.take_events"></a>`take_events(self)` — [`L428`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L428)
  - <a id="TPURaidenOffloadingConnector.connector_scheduler"></a>`connector_scheduler` — [`L394`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L394)
  - <a id="TPURaidenOffloadingConnector.connector_worker"></a>`connector_worker` — [`L395`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L395)
- protocol/private: <a id="TPURaidenOffloadingConnector.__init__"></a>`__init__`[`L363`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L363), <a id="TPURaidenOffloadingConnector._completed_jobs"></a>`_completed_jobs`[`L409`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L409), <a id="TPURaidenOffloadingConnector._fenced_jobs"></a>`_fenced_jobs`[`L408`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L408), <a id="TPURaidenOffloadingConnector._pending_fences"></a>`_pending_fences`[`L415`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L415), <a id="TPURaidenOffloadingConnector._pool_sync_tensors"></a>`_pool_sync_tensors`[`L412`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L412)
- uses (calls/refs, reference-scoped): [`_prefix_aware_load_enabled`](../distributed/kv_transfer/tpu_connector.md#_prefix_aware_load_enabled), [`VLLM_TPU_BLOCK_MAJOR_KV`](../envs.md#VLLM_TPU_BLOCK_MAJOR_KV), [`fenced_jobs`](raiden_connector.md#RaidenOffloadingWorkerMetadata.fenced_jobs), [`logger`](raiden_connector.md#logger), [`RaidenOffloadingWorkerMetadata`](raiden_connector.md#RaidenOffloadingWorkerMetadata), [`TPURaidenStoreOffloadingSpec`](raiden_store.md#TPURaidenStoreOffloadingSpec), [`fence_job_ids`](raiden_connector.md#RaidenOffloadingConnectorMetadata.fence_job_ids), [`RaidenOffloadingConnectorMetadata`](raiden_connector.md#RaidenOffloadingConnectorMetadata), [`TPURaidenOffloadingScheduler`](raiden_connector.md#TPURaidenOffloadingScheduler), [`failed_load_req_ids`](raiden_connector.md#RaidenOffloadingConnectorMetadata.failed_load_req_ids), [`finished_load_jobs`](raiden_connector.md#RaidenOffloadingConnectorMetadata.finished_load_jobs), [`finished_store_job_ids`](raiden_connector.md#RaidenOffloadingConnectorMetadata.finished_store_job_ids), [`RAIDEN_DISABLE_SINGLETON_WORKER`](../envs.md#RAIDEN_DISABLE_SINGLETON_WORKER), [`_enqueue_pool_writes`](raiden_connector.md#_enqueue_pool_writes), [`_event_is_retired`](raiden_connector.md#_event_is_retired), [`_record_fence_event`](raiden_connector.md#_record_fence_event)

### <a id="TPURaidenOffloadingScheduler"></a>`TPURaidenOffloadingScheduler`
- def: [`src/vllm_torchtpu/offload/raiden_connector.py:198`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L198)
- doc: Scheduler for the store-backed offload path.
- signature: `class TPURaidenOffloadingScheduler(OffloadingConnectorScheduler):`
- members:
  - <a id="TPURaidenOffloadingScheduler.build_connector_meta"></a>`build_connector_meta(self, scheduler_output: SchedulerOutput)` — [`L216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L216) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="TPURaidenOffloadingScheduler.update_connector_output"></a>`update_connector_output(self, connector_output: KVConnectorOutput)` — [`L306`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L306) — documented in [host-offload](../../../../concepts/host-offload.md)
- protocol/private: <a id="TPURaidenOffloadingScheduler.__init__"></a>`__init__`[`L205`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L205), <a id="TPURaidenOffloadingScheduler._fence_pending"></a>`_fence_pending`[`L214`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L214), <a id="TPURaidenOffloadingScheduler._raiden_manager"></a>`_raiden_manager`[`L213`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L213)
- uses (calls/refs, reference-scoped): [`submit_store_job`](raiden_store.md#RaidenOffloadingManager.submit_store_job), [`submit_load_job`](raiden_store.md#RaidenOffloadingManager.submit_load_job), [`drain_jobs`](raiden_store.md#RaidenOffloadingManager.drain_jobs), [`AdmissionOp`](raiden_store.md#AdmissionOp), [`STORE`](raiden_store.md#AdmissionOp.STORE), [`job_id`](raiden_store.md#FinishedJob.job_id), [`op`](raiden_store.md#FinishedJob.op), [`poll_finished_jobs`](raiden_store.md#RaidenOffloadingManager.poll_finished_jobs), [`keys`](raiden_store.md#RaidenLoadStoreSpec.keys), [`success`](raiden_store.md#FinishedJob.success), [`RaidenLoadStoreSpec`](raiden_store.md#RaidenLoadStoreSpec), [`fenced_jobs`](raiden_connector.md#RaidenOffloadingWorkerMetadata.fenced_jobs), [`RaidenOffloadingManager`](raiden_store.md#RaidenOffloadingManager), [`req_id`](raiden_store.md#FinishedJob.req_id), [`logger`](raiden_connector.md#logger), [`RaidenOffloadingWorkerMetadata`](raiden_connector.md#RaidenOffloadingWorkerMetadata), [`is_job_launched`](raiden_store.md#RaidenOffloadingManager.is_job_launched), [`on_store_job_cancelled`](raiden_store.md#RaidenOffloadingManager.on_store_job_cancelled), [`TPURaidenStoreOffloadingSpec`](raiden_store.md#TPURaidenStoreOffloadingSpec), [`acks`](raiden_connector.md#_ParkedStore.acks), [`fence_job_ids`](raiden_connector.md#RaidenOffloadingConnectorMetadata.fence_job_ids), [`keys`](raiden_connector.md#_ParkedStore.keys), [`RaidenOffloadingConnectorMetadata`](raiden_connector.md#RaidenOffloadingConnectorMetadata), [`_ParkedStore`](raiden_connector.md#_ParkedStore), [`device_block_ids`](raiden_connector.md#_ParkedStore.device_block_ids), [`failed_load_req_ids`](raiden_connector.md#RaidenOffloadingConnectorMetadata.failed_load_req_ids), [`finished_load_jobs`](raiden_connector.md#RaidenOffloadingConnectorMetadata.finished_load_jobs), [`finished_store_job_ids`](raiden_connector.md#RaidenOffloadingConnectorMetadata.finished_store_job_ids), [`pinned`](raiden_store.md#RaidenLoadStoreSpec.pinned)
- used by: [`connector_worker`](raiden_connector.md#TPURaidenOffloadingConnector.connector_worker), [`connector_scheduler`](raiden_connector.md#TPURaidenOffloadingConnector.connector_scheduler)

### <a id="_ParkedStore"></a>`_ParkedStore`
- def: [`src/vllm_torchtpu/offload/raiden_connector.py:190`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L190)
- doc: A store job parked until every worker rank acknowledges the device fence.
- signature: `class _ParkedStore:`
- members:
  - <a id="_ParkedStore.acks"></a>`acks` — [`L195`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L195)
  - <a id="_ParkedStore.device_block_ids"></a>`device_block_ids` — [`L194`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L194)
  - <a id="_ParkedStore.keys"></a>`keys` — [`L193`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L193)
- used by: [`build_connector_meta`](raiden_connector.md#TPURaidenOffloadingScheduler.build_connector_meta), [`update_connector_output`](raiden_connector.md#TPURaidenOffloadingScheduler.update_connector_output), [`_fence_pending`](raiden_connector.md#TPURaidenOffloadingScheduler._fence_pending)

## Functions
- <a id="_enqueue_pool_writes"></a>`_enqueue_pool_writes(pool_tensors: list[torch.Tensor])` — [`L106`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L106) — Asynchronously dispatches graph execution for KV pool buffers without blocking.
- <a id="_event_is_retired"></a>`_event_is_retired(event: torch.Event)` — [`L131`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L131) — Non-blockingly verifies fence event completion and surfaces deferred errors.
- <a id="_record_fence_event"></a>`_record_fence_event()` — [`L119`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L119) — Records a TPU stream event to track completion of enqueued device operations.

## Module values
- <a id="logger"></a>`logger` — [`L103`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_connector.py#L103)

