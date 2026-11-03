---
title: 'Module: src/vllm_torchtpu/offload/raiden_store.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/offload/raiden_store.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.offload.raiden_store`/
symbols:
  RaidenOffloadingManager.submit_store_job: RaidenOffloadingManager#submit_store_job().
  TPURaidenStoreOffloadingSpec.get_manager: TPURaidenStoreOffloadingSpec#get_manager().
  RaidenOffloadingManager._finalize: RaidenOffloadingManager#_finalize().
  RaidenOffloadingManager.submit_load_job: RaidenOffloadingManager#submit_load_job().
  resolve_storage_config: resolve_storage_config().
  TPURaidenStoreOffloadingSpec.get_worker: TPURaidenStoreOffloadingSpec#get_worker().
  RaidenOffloadingManager._fail_launch: RaidenOffloadingManager#_fail_launch().
  RaidenOffloadingManager._poll_once: RaidenOffloadingManager#_poll_once().
  RaidenOffloadingManager._maybe_retry_save: RaidenOffloadingManager#_maybe_retry_save().
  RaidenOffloadingManager.drain_jobs: RaidenOffloadingManager#drain_jobs().
  RaidenStoreOffloadingWorker._register_loop: RaidenStoreOffloadingWorker#_register_loop().
  worker_storage_rank_coords: worker_storage_rank_coords().
  build_worker_storage_backend_config: build_worker_storage_backend_config().
  logger: logger.
  RaidenOffloadingManager.prepare_load: RaidenOffloadingManager#prepare_load().
  RaidenOffloadingManager._mark_unloadable: RaidenOffloadingManager#_mark_unloadable().
  RaidenOffloadingManager._store: RaidenOffloadingManager#_store.
  RaidenOffloadingManager.lookup: RaidenOffloadingManager#lookup().
  RaidenOffloadingManager._admissions: RaidenOffloadingManager#_admissions.
  AdmissionOp: AdmissionOp#
  resolve_kernel_geometry: resolve_kernel_geometry().
  RaidenStoreOffloadingWorker._backend_configs: RaidenStoreOffloadingWorker#_backend_configs.
  TPURaidenStoreOffloadingSpec.raiden_controller_port: TPURaidenStoreOffloadingSpec#raiden_controller_port.
  _new_storage_backend_config: _new_storage_backend_config().
  RaidenOffloadingManager._block_status: RaidenOffloadingManager#_block_status.
  build_store_storage_backend_config: build_store_storage_backend_config().
  RaidenOffloadingManager.prepare_store: RaidenOffloadingManager#prepare_store().
  StorageRankCoords.__post_init__: StorageRankCoords#__post_init__().
  StorageRankCoords.engine_rank: StorageRankCoords#engine_rank().
  RaidenOffloadingManager._finished: RaidenOffloadingManager#_finished.
  RaidenOffloadingManager._on_eviction: RaidenOffloadingManager#_on_eviction().
  Admission.job_id: Admission#job_id.
  RaidenOffloadingManager._supports_eviction_callback: RaidenOffloadingManager#_supports_eviction_callback.
  Admission.op: Admission#op.
  Admission: Admission#
  Admission.pending: Admission#pending.
  RaidenOffloadingManager._pins_still_held: RaidenOffloadingManager#_pins_still_held().
  derive_offload_namespace: derive_offload_namespace().
  StorageRankCoords.pcp_size: StorageRankCoords#pcp_size.
  TPURaidenStoreOffloadingSpec.key_namespace: TPURaidenStoreOffloadingSpec#key_namespace.
  RaidenOffloadingManager._hash_to_admission: RaidenOffloadingManager#_hash_to_admission.
  resolve_attention_geometry: resolve_attention_geometry().
  AdmissionOp.STORE: AdmissionOp#STORE.
  FinishedJob: FinishedJob#
  FinishedJob.job_id: FinishedJob#job_id.
  RaidenOffloadingManager._sub_hashes: RaidenOffloadingManager#_sub_hashes().
  RaidenOffloadingManager.shutdown: RaidenOffloadingManager#shutdown().
  StorageRankCoords.tp_size: StorageRankCoords#tp_size.
  StorageRankCoords.pp_size: StorageRankCoords#pp_size.
  FinishedJob.op: FinishedJob#op.
  _MANAGED_STORAGE_PROPERTIES: _MANAGED_STORAGE_PROPERTIES.
  StorageRankCoords.storage_size: StorageRankCoords#storage_size().
  TPURaidenStoreOffloadingSpec.block_major_contract: TPURaidenStoreOffloadingSpec#block_major_contract.
  Admission.keys: Admission#keys.
  RaidenOffloadingManager._enable_global: RaidenOffloadingManager#_enable_global.
  RaidenOffloadingManager._newly_inserted_sub_hashes: RaidenOffloadingManager#_newly_inserted_sub_hashes().
  RaidenOffloadingManager.poll_finished_jobs: RaidenOffloadingManager#poll_finished_jobs().
  record_all_ranks_kv_bytes_per_block: record_all_ranks_kv_bytes_per_block().
  RaidenOffloadingManager._inflight_store_keys: RaidenOffloadingManager#_inflight_store_keys.
  TPURaidenStoreOffloadingSpec.raiden_job_name: TPURaidenStoreOffloadingSpec#raiden_job_name.
  RaidenOffloadingManager.touch: RaidenOffloadingManager#touch().
  RaidenStoreOffloadingWorker.shutdown: RaidenStoreOffloadingWorker#shutdown().
  RaidenLoadStoreSpec.keys: RaidenLoadStoreSpec#keys.
  Admission.failed: Admission#failed.
  FinishedJob.success: FinishedJob#success.
  RaidenOffloadingManager._record_unloadable: RaidenOffloadingManager#_record_unloadable().
  RaidenStoreOffloadingWorker._register_thread: RaidenStoreOffloadingWorker#_register_thread.
  TPURaidenStoreOffloadingSpec.is_hybrid_model: TPURaidenStoreOffloadingSpec#is_hybrid_model.
  TPURaidenStoreOffloadingSpec.kernel_physical_blocks_capacity: TPURaidenStoreOffloadingSpec#kernel_physical_blocks_capacity.
  TPURaidenStoreOffloadingSpec.storage_config: TPURaidenStoreOffloadingSpec#storage_config.
  _get_ephemeral_port_range: _get_ephemeral_port_range().
  RaidenLoadStoreSpec: RaidenLoadStoreSpec#
  AdmissionOp.LOAD: AdmissionOp#LOAD.
  Admission.sub_hashes: Admission#sub_hashes.
  Admission.remote_sub_hashes: Admission#remote_sub_hashes.
  Admission.failed_sub_hashes: Admission#failed_sub_hashes.
  RaidenOffloadingManager._sub_hash_to_offload_key: RaidenOffloadingManager#_sub_hash_to_offload_key().
  StorageRankCoords.tp_rank: StorageRankCoords#tp_rank.
  iter_leaf_kv_cache_specs: iter_leaf_kv_cache_specs().
  RaidenOffloadingManager._expand_keys: RaidenOffloadingManager#_expand_keys().
  RaidenOffloadingManager._probe: RaidenOffloadingManager#_probe().
  TPURaidenStoreOffloadingSpec.offload_logical_blocks_capacity: TPURaidenStoreOffloadingSpec#offload_logical_blocks_capacity.
  TPURaidenStoreOffloadingSpec.dp_rank: TPURaidenStoreOffloadingSpec#dp_rank.
  TPURaidenStoreOffloadingSpec._manager: TPURaidenStoreOffloadingSpec#_manager.
  TPURaidenStoreOffloadingSpec._worker: TPURaidenStoreOffloadingSpec#_worker.
  RaidenLoadStoreSpec.__repr__: RaidenLoadStoreSpec#__repr__().
  Admission.req_id: Admission#req_id.
  Admission.retries_left: Admission#retries_left.
  FinishedJob.req_id: FinishedJob#req_id.
  RaidenOffloadingManager: RaidenOffloadingManager#
  RaidenOffloadingManager._device_block_size_factor: RaidenOffloadingManager#_device_block_size_factor.
  RaidenOffloadingManager.on_request_finished: RaidenOffloadingManager#on_request_finished().
  RaidenOffloadingManager.take_events: RaidenOffloadingManager#take_events().
  RaidenStoreOffloadingWorker._rank: RaidenStoreOffloadingWorker#_rank.
  RaidenStorageConfig: RaidenStorageConfig#
  RaidenStorageConfig.capacity_bytes: RaidenStorageConfig#capacity_bytes.
  StorageRankCoords: StorageRankCoords#
  StorageRankCoords.pcp_rank: StorageRankCoords#pcp_rank.
  StorageRankCoords.pp_rank: StorageRankCoords#pp_rank.
  _DRAIN_TIMEOUT_S: _DRAIN_TIMEOUT_S.
  RaidenOffloadingManager._expand_device_blocks: RaidenOffloadingManager#_expand_device_blocks().
  _parse_storage_properties: _parse_storage_properties().
  RaidenOffloadingManager._key_namespace: RaidenOffloadingManager#_key_namespace.
  RaidenOffloadingManager._evicted_keys_queue: RaidenOffloadingManager#_evicted_keys_queue.
  RaidenStoreOffloadingWorker._controller_address: RaidenStoreOffloadingWorker#_controller_address.
  RaidenStorageConfig.root_dir: RaidenStorageConfig#root_dir.
  _storage_setting: _storage_setting().
  TPURaidenStoreOffloadingSpec.tp_size: TPURaidenStoreOffloadingSpec#tp_size.
  TPURaidenStoreOffloadingSpec.pcp_size: TPURaidenStoreOffloadingSpec#pcp_size.
  TPURaidenStoreOffloadingSpec.pp_size: TPURaidenStoreOffloadingSpec#pp_size.
  _SAVE_RETRIES: _SAVE_RETRIES.
  all_ranks_kv_bytes_per_block: all_ranks_kv_bytes_per_block().
  RaidenOffloadingManager._raiden_id: RaidenOffloadingManager#_raiden_id.
  RaidenOffloadingManager.on_store_job_cancelled: RaidenOffloadingManager#on_store_job_cancelled().
  RaidenOffloadingManager.is_job_launched: RaidenOffloadingManager#is_job_launched().
  _resolve_multi_shapes_kv_geometry: _resolve_multi_shapes_kv_geometry().
  RaidenStoreOffloadingWorker._controller_reachable: RaidenStoreOffloadingWorker#_controller_reachable().
  _parse_storage_capacity: _parse_storage_capacity().
  Admission.poisoned: Admission#poisoned.
  Admission.dst_device_block_ids: Admission#dst_device_block_ids.
  RaidenOffloadingManager._eviction_lock: RaidenOffloadingManager#_eviction_lock.
  RaidenOffloadingManager._evicted_sub_hashes: RaidenOffloadingManager#_evicted_sub_hashes.
  RaidenOffloadingManager._unloadable: RaidenOffloadingManager#_unloadable.
  RaidenOffloadingManager._live_req_ids: RaidenOffloadingManager#_live_req_ids.
  RaidenOffloadingManager._remote_slices: RaidenOffloadingManager#_remote_slices.
  is_multi_shapes_geometry: is_multi_shapes_geometry().
  RaidenStoreOffloadingWorker._stop_registration: RaidenStoreOffloadingWorker#_stop_registration.
  _STORAGE_PATH_KEY: _STORAGE_PATH_KEY.
  _STORAGE_CAPACITY_GB_KEY: _STORAGE_CAPACITY_GB_KEY.
  _STORAGE_SKIP_PARALLELISM_CHECK_KEY: _STORAGE_SKIP_PARALLELISM_CHECK_KEY.
  _POSIX_STORAGE_TYPE: _POSIX_STORAGE_TYPE.
  RaidenStorageConfig.storage_type: RaidenStorageConfig#storage_type.
  RaidenStorageConfig.model_name: RaidenStorageConfig#model_name.
  RaidenStorageConfig.properties: RaidenStorageConfig#properties.
  TPURaidenStoreOffloadingSpec: TPURaidenStoreOffloadingSpec#
  TPURaidenStoreOffloadingSpec.world_size: TPURaidenStoreOffloadingSpec#world_size.
  _all_ranks_kv_bytes_per_block._all_ranks_kv_bytes_per_block: _all_ranks_kv_bytes_per_block._all_ranks_kv_bytes_per_block.
  RaidenOffloadingManager.on_new_request: RaidenOffloadingManager#on_new_request().
  RaidenOffloadingManager.on_schedule_end: RaidenOffloadingManager#on_schedule_end().
  RaidenOffloadingManager.has_pending_work: RaidenOffloadingManager#has_pending_work().
  RaidenStoreOffloadingWorker.__init__: RaidenStoreOffloadingWorker#__init__().
  StorageRankCoords.storage_rank: StorageRankCoords#storage_rank().
  RaidenLoadStoreSpec.pinned: RaidenLoadStoreSpec#pinned.
  _DEFAULT_CONTROLLER_PORT: _DEFAULT_CONTROLLER_PORT.
  _IP_LOCAL_PORT_RANGE_PATH: _IP_LOCAL_PORT_RANGE_PATH.
  Admission.consumed_sub_hashes: Admission#consumed_sub_hashes.
  FinishedJob.failed_device_block_ids: FinishedJob#failed_device_block_ids.
  RaidenOffloadingManager._pending_remote_slices: RaidenOffloadingManager#_pending_remote_slices.
  RaidenStoreOffloadingWorker: RaidenStoreOffloadingWorker#
  RaidenStoreOffloadingWorker._init_registration: RaidenStoreOffloadingWorker#_init_registration().
  RaidenStoreOffloadingWorker._host_blocks_to_allocate: RaidenStoreOffloadingWorker#_host_blocks_to_allocate.
  RaidenStoreOffloadingWorker._mgr: RaidenStoreOffloadingWorker#_mgr.
  _STORAGE_TYPE_KEY: _STORAGE_TYPE_KEY.
  _STORAGE_MODEL_NAME_KEY: _STORAGE_MODEL_NAME_KEY.
  _STORAGE_PROPERTIES_KEY: _STORAGE_PROPERTIES_KEY.
  TPURaidenStoreOffloadingSpec.device_block_size_factor: TPURaidenStoreOffloadingSpec#device_block_size_factor.
  TPURaidenStoreOffloadingSpec.store_server_ip: TPURaidenStoreOffloadingSpec#store_server_ip.
  _DEFAULT_EPHEMERAL_PORT_RANGE: _DEFAULT_EPHEMERAL_PORT_RANGE.
  _worker_kv_bytes_per_block: _worker_kv_bytes_per_block().
  has_multi_shapes_kv_caches: has_multi_shapes_kv_caches().
  Admission.saved_sub_hashes: Admission#saved_sub_hashes.
  RaidenOffloadingManager._capacity_keys: RaidenOffloadingManager#_capacity_keys.
  RaidenOffloadingManager._block_id_cls: RaidenOffloadingManager#_block_id_cls.
  RaidenStoreOffloadingWorker._device_tensors: RaidenStoreOffloadingWorker#_device_tensors.
  _parse_storage_flag: _parse_storage_flag().
  _ensure_writable_dir: _ensure_writable_dir().
  TPURaidenStoreOffloadingSpec.vllm_config: TPURaidenStoreOffloadingSpec#vllm_config.
  TPURaidenStoreOffloadingSpec.kv_cache_config: TPURaidenStoreOffloadingSpec#kv_cache_config.
  TPURaidenStoreOffloadingSpec.global_registry_address: TPURaidenStoreOffloadingSpec#global_registry_address.
  TPURaidenStoreOffloadingSpec.kv_pool_group: TPURaidenStoreOffloadingSpec#kv_pool_group.
  RaidenLoadStoreSpec.__init__: RaidenLoadStoreSpec#__init__().
  RaidenOffloadingManager.__init__: RaidenOffloadingManager#__init__().
  RaidenOffloadingManager.reset_cache: RaidenOffloadingManager#reset_cache().
  RaidenStoreOffloadingWorker.submit_store: RaidenStoreOffloadingWorker#submit_store().
  RaidenStoreOffloadingWorker.submit_load: RaidenStoreOffloadingWorker#submit_load().
  RaidenStoreOffloadingWorker.get_finished: RaidenStoreOffloadingWorker#get_finished().
  RaidenStoreOffloadingWorker.wait: RaidenStoreOffloadingWorker#wait().
  TPURaidenStoreOffloadingSpec.__init__: TPURaidenStoreOffloadingSpec#__init__().
---
# Module: [`src/vllm_torchtpu/offload/raiden_store.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py)

## Classes
### <a id="Admission"></a>`Admission`
- def: [`src/vllm_torchtpu/offload/raiden_store.py:254`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L254) — documented in [host-offload](../../../../concepts/host-offload.md)
- doc: Exact-batch record of one launched store/load job.
- signature: `class Admission:`
- members:
  - <a id="Admission.consumed_sub_hashes"></a>`consumed_sub_hashes` — [`L288`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L288)
  - <a id="Admission.dst_device_block_ids"></a>`dst_device_block_ids` — [`L280`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L280)
  - <a id="Admission.failed"></a>`failed` — [`L270`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L270)
  - <a id="Admission.failed_sub_hashes"></a>`failed_sub_hashes` — [`L295`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L295)
  - <a id="Admission.job_id"></a>`job_id` — [`L264`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L264) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="Admission.keys"></a>`keys` — [`L266`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L266) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="Admission.op"></a>`op` — [`L265`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L265) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="Admission.pending"></a>`pending` — [`L269`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L269) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="Admission.poisoned"></a>`poisoned` — [`L275`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L275)
  - <a id="Admission.remote_sub_hashes"></a>`remote_sub_hashes` — [`L285`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L285)
  - <a id="Admission.req_id"></a>`req_id` — [`L279`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L279)
  - <a id="Admission.retries_left"></a>`retries_left` — [`L296`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L296)
  - <a id="Admission.saved_sub_hashes"></a>`saved_sub_hashes` — [`L292`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L292)
  - <a id="Admission.sub_hashes"></a>`sub_hashes` — [`L267`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L267)
- uses (calls/refs, reference-scoped): [`AdmissionOp`](raiden_store.md#AdmissionOp)
- used by: [`submit_store_job`](raiden_store.md#RaidenOffloadingManager.submit_store_job), [`_finalize`](raiden_store.md#RaidenOffloadingManager._finalize), [`submit_load_job`](raiden_store.md#RaidenOffloadingManager.submit_load_job), [`_fail_launch`](raiden_store.md#RaidenOffloadingManager._fail_launch), [`_poll_once`](raiden_store.md#RaidenOffloadingManager._poll_once), [`_maybe_retry_save`](raiden_store.md#RaidenOffloadingManager._maybe_retry_save), [`drain_jobs`](raiden_store.md#RaidenOffloadingManager.drain_jobs), [`_mark_unloadable`](raiden_store.md#RaidenOffloadingManager._mark_unloadable), [`_admissions`](raiden_store.md#RaidenOffloadingManager._admissions), [`_pins_still_held`](raiden_store.md#RaidenOffloadingManager._pins_still_held), [`_hash_to_admission`](raiden_store.md#RaidenOffloadingManager._hash_to_admission)

### <a id="AdmissionOp"></a>`AdmissionOp`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/offload/raiden_store.py:248`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L248) — documented in [host-offload](../../../../concepts/host-offload.md)
- signature: `class AdmissionOp(enum.Enum):`
- members:
  - <a id="AdmissionOp.LOAD"></a>`LOAD` — [`L250`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L250)
  - <a id="AdmissionOp.STORE"></a>`STORE` — [`L249`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L249)
- used by: [`submit_store_job`](raiden_store.md#RaidenOffloadingManager.submit_store_job), [`_finalize`](raiden_store.md#RaidenOffloadingManager._finalize), [`submit_load_job`](raiden_store.md#RaidenOffloadingManager.submit_load_job), [`build_connector_meta`](raiden_connector.md#TPURaidenOffloadingScheduler.build_connector_meta), [`_fail_launch`](raiden_store.md#RaidenOffloadingManager._fail_launch), [`_poll_once`](raiden_store.md#RaidenOffloadingManager._poll_once), [`_maybe_retry_save`](raiden_store.md#RaidenOffloadingManager._maybe_retry_save), [`op`](raiden_store.md#Admission.op), [`op`](raiden_store.md#FinishedJob.op)

### <a id="FinishedJob"></a>`FinishedJob`
- def: [`src/vllm_torchtpu/offload/raiden_store.py:300`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L300) — documented in [host-offload](../../../../concepts/host-offload.md)
- signature: `class FinishedJob:`
- members:
  - <a id="FinishedJob.failed_device_block_ids"></a>`failed_device_block_ids` — [`L305`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L305)
  - <a id="FinishedJob.job_id"></a>`job_id` — [`L301`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L301) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="FinishedJob.op"></a>`op` — [`L302`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L302) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="FinishedJob.req_id"></a>`req_id` — [`L304`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L304)
  - <a id="FinishedJob.success"></a>`success` — [`L303`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L303)
- uses (calls/refs, reference-scoped): [`AdmissionOp`](raiden_store.md#AdmissionOp)
- used by: [`submit_store_job`](raiden_store.md#RaidenOffloadingManager.submit_store_job), [`_finalize`](raiden_store.md#RaidenOffloadingManager._finalize), [`submit_load_job`](raiden_store.md#RaidenOffloadingManager.submit_load_job), [`build_connector_meta`](raiden_connector.md#TPURaidenOffloadingScheduler.build_connector_meta), [`drain_jobs`](raiden_store.md#RaidenOffloadingManager.drain_jobs), [`_finished`](raiden_store.md#RaidenOffloadingManager._finished), [`poll_finished_jobs`](raiden_store.md#RaidenOffloadingManager.poll_finished_jobs)

### <a id="RaidenLoadStoreSpec"></a>`RaidenLoadStoreSpec`
- def: [`src/vllm_torchtpu/offload/raiden_store.py:226`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L226)
- doc: Offload-side specification describing the ordered keys for a job.
- signature: `class RaidenLoadStoreSpec(LoadStoreSpec):`
- members:
  - <a id="RaidenLoadStoreSpec.keys"></a>`keys` — [`L238`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L238)
  - <a id="RaidenLoadStoreSpec.pinned"></a>`pinned` — [`L239`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L239)
- protocol/private: <a id="RaidenLoadStoreSpec.__init__"></a>`__init__`[`L237`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L237), <a id="RaidenLoadStoreSpec.__repr__"></a>`__repr__`[`L241`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L241)
- used by: [`build_connector_meta`](raiden_connector.md#TPURaidenOffloadingScheduler.build_connector_meta), [`prepare_load`](raiden_store.md#RaidenOffloadingManager.prepare_load), [`prepare_store`](raiden_store.md#RaidenOffloadingManager.prepare_store)

### <a id="RaidenOffloadingManager"></a>`RaidenOffloadingManager`
- def: [`src/vllm_torchtpu/offload/raiden_store.py:308`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L308)
- doc: Scheduler-side OffloadingManager backed by raiden's KVCacheStore.
- signature: `class RaidenOffloadingManager(OffloadingManager):`
- members:
  - <a id="RaidenOffloadingManager._mark_unloadable"></a>`_mark_unloadable(self, admission: Admission)` — [`L1167`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1167) — Stop offering this load's failed keys to the request that owns it. — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager._maybe_retry_save"></a>`_maybe_retry_save(self, admission: Admission)` — [`L1297`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1297) — Re-issue the failed subset of a store job's save, at most — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager._newly_inserted_sub_hashes"></a>`_newly_inserted_sub_hashes(self, sub_hashes: list[bytes], device_ids: list[int])` — [`L537`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L537) — Return the sub-hashes this admission itself inserted — the ones a — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager._on_eviction"></a>`_on_eviction(self, evicted_hashes: list[bytes])` — [`L843`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L843) — Callback invoked by Raiden C++ store upon host LRU cache eviction.
  - <a id="RaidenOffloadingManager._pins_still_held"></a>`_pins_still_held(self, admission: Admission)` — [`L523`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L523) — The job's sub-hashes whose pin nothing has spent yet. — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager._probe"></a>`_probe(self, sub_hashes: list[bytes], *, enable_global: bool = False)` — [`L508`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L508) — Read the directory without laying claim to what it reports.
  - <a id="RaidenOffloadingManager._record_unloadable"></a>`_record_unloadable(self, req_id: str | None, keys: list[OffloadKey], failed_keys: set[OffloadKey])` — [`L1196`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1196) — Record a failed load's keys as unloadable for `req_id`.
  - <a id="RaidenOffloadingManager._sub_hash_to_offload_key"></a>`_sub_hash_to_offload_key(self, sub_hash: bytes)` — [`L824`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L824) — Helper to reverse a Raiden C++ sub_hash to (OffloadKey, sub_idx).
  - <a id="RaidenOffloadingManager.drain_jobs"></a>`drain_jobs(self, job_ids: set[int])` — [`L1347`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1347) — Drain in-flight DMA transfers to safely reclaim HBM blocks before reuse. — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager.has_pending_work"></a>`has_pending_work(self)` — [`L898`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L898)
  - <a id="RaidenOffloadingManager.is_job_launched"></a>`is_job_launched(self, job_id: int)` — [`L1123`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1123) — Whether a job has been admitted+launched and is not yet terminal.
  - <a id="RaidenOffloadingManager.lookup"></a>`lookup(self, key: OffloadKey, req_context: ReqContext)` — [`L612`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L612)
  - <a id="RaidenOffloadingManager.on_new_request"></a>`on_new_request(self, req_context: ReqContext)` — [`L604`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L604)
  - <a id="RaidenOffloadingManager.on_request_finished"></a>`on_request_finished(self, req_context: ReqContext)` — [`L608`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L608)
  - <a id="RaidenOffloadingManager.on_schedule_end"></a>`on_schedule_end(self, context: ScheduleEndContext)` — [`L876`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L876)
  - <a id="RaidenOffloadingManager.on_store_job_cancelled"></a>`on_store_job_cancelled(self, keys: list[OffloadKey])` — [`L1119`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1119) — A fence-pending (never admitted) store job was cancelled.
  - <a id="RaidenOffloadingManager.poll_finished_jobs"></a>`poll_finished_jobs(self)` — [`L1340`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1340) — Poll raiden completion and return newly terminal jobs. — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager.prepare_load"></a>`prepare_load(self, keys, req_context: ReqContext)` — [`L696`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L696) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager.prepare_store"></a>`prepare_store(self, keys, req_context: ReqContext)` — [`L783`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L783)
  - <a id="RaidenOffloadingManager.reset_cache"></a>`reset_cache(self)` — [`L886`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L886)
  - <a id="RaidenOffloadingManager.shutdown"></a>`shutdown(self)` — [`L901`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L901)
  - <a id="RaidenOffloadingManager.submit_load_job"></a>`submit_load_job(self, job_id: int, keys: list[OffloadKey], device_block_ids: list[int], req_id: str, pinned: bool = True)` — [`L1005`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1005) — Launch a load job; entries were pinned in prepare_load. — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager.submit_store_job"></a>`submit_store_job(self, job_id: int, keys: list[OffloadKey], device_block_ids: list[int])` — [`L911`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L911) — Admit and launch a store job after all worker ranks acknowledge — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenOffloadingManager.take_events"></a>`take_events(self)` — [`L860`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L860)
  - <a id="RaidenOffloadingManager.touch"></a>`touch(self, keys, req_context: ReqContext)` — [`L672`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L672)
- protocol/private: <a id="RaidenOffloadingManager.__init__"></a>`__init__`[`L316`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L316), <a id="RaidenOffloadingManager._admissions"></a>`_admissions`[`L482`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L482), <a id="RaidenOffloadingManager._block_id_cls"></a>`_block_id_cls`[`L433`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L433), <a id="RaidenOffloadingManager._block_status"></a>`_block_status`[`L432`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L432), <a id="RaidenOffloadingManager._capacity_keys"></a>`_capacity_keys`[`L345`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L345), <a id="RaidenOffloadingManager._device_block_size_factor"></a>`_device_block_size_factor`[`L346`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L346), <a id="RaidenOffloadingManager._enable_global"></a>`_enable_global`[`L350`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L350), <a id="RaidenOffloadingManager._evicted_keys_queue"></a>`_evicted_keys_queue`[`L439`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L439), <a id="RaidenOffloadingManager._evicted_sub_hashes"></a>`_evicted_sub_hashes`[`L438`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L438), <a id="RaidenOffloadingManager._eviction_lock"></a>`_eviction_lock`[`L437`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L437), <a id="RaidenOffloadingManager._expand_device_blocks"></a>`_expand_device_blocks`[`L502`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L502), <a id="RaidenOffloadingManager._expand_keys"></a>`_expand_keys`[`L496`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L496), <a id="RaidenOffloadingManager._fail_launch"></a>`_fail_launch`[`L1055`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1055), <a id="RaidenOffloadingManager._finalize"></a>`_finalize`[`L1129`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1129), <a id="RaidenOffloadingManager._finished"></a>`_finished`[`L484`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L484), <a id="RaidenOffloadingManager._hash_to_admission"></a>`_hash_to_admission`[`L483`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L483), <a id="RaidenOffloadingManager._inflight_store_keys"></a>`_inflight_store_keys`[`L458`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L458), <a id="RaidenOffloadingManager._key_namespace"></a>`_key_namespace`[`L347`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L347), <a id="RaidenOffloadingManager._live_req_ids"></a>`_live_req_ids`[`L467`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L467), <a id="RaidenOffloadingManager._pending_remote_slices"></a>`_pending_remote_slices`[`L480`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L480), <a id="RaidenOffloadingManager._poll_once"></a>`_poll_once`[`L1231`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1231), <a id="RaidenOffloadingManager._raiden_id"></a>`_raiden_id`[`L434`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L434), <a id="RaidenOffloadingManager._remote_slices"></a>`_remote_slices`[`L471`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L471), <a id="RaidenOffloadingManager._store"></a>`_store`[`L431`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L431), <a id="RaidenOffloadingManager._sub_hashes"></a>`_sub_hashes`[`L488`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L488), <a id="RaidenOffloadingManager._supports_eviction_callback"></a>`_supports_eviction_callback`[`L443`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L443), <a id="RaidenOffloadingManager._unloadable"></a>`_unloadable`[`L463`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L463)
- uses (calls/refs, reference-scoped): [`logger`](raiden_store.md#logger), [`AdmissionOp`](raiden_store.md#AdmissionOp), [`job_id`](raiden_store.md#Admission.job_id), [`op`](raiden_store.md#Admission.op), [`Admission`](raiden_store.md#Admission), [`pending`](raiden_store.md#Admission.pending), [`FinishedJob`](raiden_store.md#FinishedJob), [`STORE`](raiden_store.md#AdmissionOp.STORE), [`job_id`](raiden_store.md#FinishedJob.job_id), [`op`](raiden_store.md#FinishedJob.op), [`keys`](raiden_store.md#Admission.keys), [`failed`](raiden_store.md#Admission.failed), [`success`](raiden_store.md#FinishedJob.success), [`RaidenLoadStoreSpec`](raiden_store.md#RaidenLoadStoreSpec), [`LOAD`](raiden_store.md#AdmissionOp.LOAD), [`failed_sub_hashes`](raiden_store.md#Admission.failed_sub_hashes), [`remote_sub_hashes`](raiden_store.md#Admission.remote_sub_hashes), [`sub_hashes`](raiden_store.md#Admission.sub_hashes), [`req_id`](raiden_store.md#Admission.req_id), [`req_id`](raiden_store.md#FinishedJob.req_id), [`retries_left`](raiden_store.md#Admission.retries_left), [`_DRAIN_TIMEOUT_S`](raiden_store.md#_DRAIN_TIMEOUT_S), [`_SAVE_RETRIES`](raiden_store.md#_SAVE_RETRIES), [`dst_device_block_ids`](raiden_store.md#Admission.dst_device_block_ids), [`poisoned`](raiden_store.md#Admission.poisoned), [`consumed_sub_hashes`](raiden_store.md#Admission.consumed_sub_hashes), [`failed_device_block_ids`](raiden_store.md#FinishedJob.failed_device_block_ids), [`saved_sub_hashes`](raiden_store.md#Admission.saved_sub_hashes)
- used by: [`get_manager`](raiden_store.md#TPURaidenStoreOffloadingSpec.get_manager), [`build_connector_meta`](raiden_connector.md#TPURaidenOffloadingScheduler.build_connector_meta), [`update_connector_output`](raiden_connector.md#TPURaidenOffloadingScheduler.update_connector_output), [`_manager`](raiden_store.md#TPURaidenStoreOffloadingSpec._manager), [`__init__`](raiden_connector.md#TPURaidenOffloadingScheduler.__init__), [`_raiden_manager`](raiden_connector.md#TPURaidenOffloadingScheduler._raiden_manager)

### <a id="RaidenStorageConfig"></a>`RaidenStorageConfig`
- def: [`src/vllm_torchtpu/offload/raiden_store.py:1971`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1971)
- doc: Resolved settings for the storage tier behind the host DRAM pool.
- signature: `class RaidenStorageConfig:`
- members:
  - <a id="RaidenStorageConfig.capacity_bytes"></a>`capacity_bytes` — [`L1986`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1986)
  - <a id="RaidenStorageConfig.model_name"></a>`model_name` — [`L1983`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1983)
  - <a id="RaidenStorageConfig.properties"></a>`properties` — [`L1992`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1992)
  - <a id="RaidenStorageConfig.root_dir"></a>`root_dir` — [`L1982`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1982)
  - <a id="RaidenStorageConfig.storage_type"></a>`storage_type` — [`L1981`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1981)
- used by: [`get_manager`](raiden_store.md#TPURaidenStoreOffloadingSpec.get_manager), [`resolve_storage_config`](raiden_store.md#resolve_storage_config), [`get_worker`](raiden_store.md#TPURaidenStoreOffloadingSpec.get_worker), [`build_worker_storage_backend_config`](raiden_store.md#build_worker_storage_backend_config), [`_new_storage_backend_config`](raiden_store.md#_new_storage_backend_config), [`build_store_storage_backend_config`](raiden_store.md#build_store_storage_backend_config)

### <a id="RaidenStoreOffloadingWorker"></a>`RaidenStoreOffloadingWorker`
- def: [`src/vllm_torchtpu/offload/raiden_store.py:1656`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1656)
- doc: Worker-side endpoint that registers local TPU HBM device buffers with
- signature: `class RaidenStoreOffloadingWorker(OffloadingWorker):`
- members:
  - <a id="RaidenStoreOffloadingWorker._controller_reachable"></a>`_controller_reachable(self)` — [`L1825`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1825) — TCP-probe the controller endpoint (a listening server is a
  - <a id="RaidenStoreOffloadingWorker._register_loop"></a>`_register_loop(self)` — [`L1841`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1841) — Background registration: wait for the controller server to come up — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="RaidenStoreOffloadingWorker.get_finished"></a>`get_finished(self)` — [`L1924`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1924)
  - <a id="RaidenStoreOffloadingWorker.shutdown"></a>`shutdown(self)` — [`L1931`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1931)
  - <a id="RaidenStoreOffloadingWorker.submit_load"></a>`submit_load(self, job_id, src_spec, dst_spec)` — [`L1918`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1918)
  - <a id="RaidenStoreOffloadingWorker.submit_store"></a>`submit_store(self, job_id, src_spec, dst_spec)` — [`L1912`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1912)
  - <a id="RaidenStoreOffloadingWorker.wait"></a>`wait(self, job_ids: set[int])` — [`L1927`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1927)
- protocol/private: <a id="RaidenStoreOffloadingWorker.__init__"></a>`__init__`[`L1676`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1676), <a id="RaidenStoreOffloadingWorker._backend_configs"></a>`_backend_configs`[`L1696`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1696), <a id="RaidenStoreOffloadingWorker._controller_address"></a>`_controller_address`[`L1814`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1814), <a id="RaidenStoreOffloadingWorker._device_tensors"></a>`_device_tensors`[`L1812`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1812), <a id="RaidenStoreOffloadingWorker._host_blocks_to_allocate"></a>`_host_blocks_to_allocate`[`L1813`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1813), <a id="RaidenStoreOffloadingWorker._init_registration"></a>`_init_registration`[`L1803`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1803), <a id="RaidenStoreOffloadingWorker._mgr"></a>`_mgr`[`L1816`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1816), <a id="RaidenStoreOffloadingWorker._rank"></a>`_rank`[`L1815`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1815), <a id="RaidenStoreOffloadingWorker._register_thread"></a>`_register_thread`[`L1818`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1818), <a id="RaidenStoreOffloadingWorker._stop_registration"></a>`_stop_registration`[`L1817`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1817)
- uses (calls/refs, reference-scoped): [`logger`](raiden_store.md#logger), [`resolve_kernel_geometry`](raiden_store.md#resolve_kernel_geometry), [`BlockMajorContract`](block_major_layout.md#BlockMajorContract), [`bundle_row_bytes`](block_major_layout.md#BlockMajorContract.bundle_row_bytes), [`fragment_count`](block_major_layout.md#BlockMajorContract.fragment_count), [`fragment_row_bytes`](block_major_layout.md#BlockMajorContract.fragment_row_bytes), [`is_multi_shapes_geometry`](raiden_store.md#is_multi_shapes_geometry)
- used by: [`get_worker`](raiden_store.md#TPURaidenStoreOffloadingSpec.get_worker), [`_worker`](raiden_store.md#TPURaidenStoreOffloadingSpec._worker)

### <a id="StorageRankCoords"></a>`StorageRankCoords`
- def: [`src/vllm_torchtpu/offload/raiden_store.py:2197`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2197)
- doc: Where one rank's shards sit in the storage layout.
- signature: `class StorageRankCoords:`
- members:
  - <a id="StorageRankCoords.engine_rank"></a>`engine_rank(self)` — [`L2226`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2226) — This rank's index among its engine's workers, in [0, world_size).
  - <a id="StorageRankCoords.storage_rank"></a>`storage_rank(self)` — [`L2244`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2244) — Which of a block's shard files this rank writes: its engine rank.
  - <a id="StorageRankCoords.storage_size"></a>`storage_size(self)` — [`L2249`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2249) — How many shard files a block has. — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="StorageRankCoords.pcp_rank"></a>`pcp_rank` — [`L2208`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2208)
  - <a id="StorageRankCoords.pcp_size"></a>`pcp_size` — [`L2209`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2209) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="StorageRankCoords.pp_rank"></a>`pp_rank` — [`L2210`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2210)
  - <a id="StorageRankCoords.pp_size"></a>`pp_size` — [`L2211`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2211) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="StorageRankCoords.tp_rank"></a>`tp_rank` — [`L2206`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2206)
  - <a id="StorageRankCoords.tp_size"></a>`tp_size` — [`L2207`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2207) — documented in [host-offload](../../../../concepts/host-offload.md)
- protocol/private: <a id="StorageRankCoords.__post_init__"></a>`__post_init__`[`L2213`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2213)
- used by: [`get_manager`](raiden_store.md#TPURaidenStoreOffloadingSpec.get_manager), [`get_worker`](raiden_store.md#TPURaidenStoreOffloadingSpec.get_worker), [`build_worker_storage_backend_config`](raiden_store.md#build_worker_storage_backend_config), [`worker_storage_rank_coords`](raiden_store.md#worker_storage_rank_coords), [`build_store_storage_backend_config`](raiden_store.md#build_store_storage_backend_config)

### <a id="TPURaidenStoreOffloadingSpec"></a>`TPURaidenStoreOffloadingSpec`
- def: [`src/vllm_torchtpu/offload/raiden_store.py:2335`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2335)
- doc: Configuration specification wiring the Raiden offloading manager and
- signature: `class TPURaidenStoreOffloadingSpec(OffloadingSpec):`
- members:
  - <a id="TPURaidenStoreOffloadingSpec.get_manager"></a>`get_manager(self)` — [`L2552`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2552) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="TPURaidenStoreOffloadingSpec.get_worker"></a>`get_worker(self, kv_caches: CanonicalKVCaches)` — [`L2605`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2605) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="TPURaidenStoreOffloadingSpec.block_major_contract"></a>`block_major_contract` — [`L2399`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2399)
  - <a id="TPURaidenStoreOffloadingSpec.device_block_size_factor"></a>`device_block_size_factor` — [`L2394`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2394)
  - <a id="TPURaidenStoreOffloadingSpec.dp_rank"></a>`dp_rank` — [`L2517`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2517)
  - <a id="TPURaidenStoreOffloadingSpec.global_registry_address"></a>`global_registry_address` — [`L2464`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2464)
  - <a id="TPURaidenStoreOffloadingSpec.is_hybrid_model"></a>`is_hybrid_model` — [`L2372`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2372)
  - <a id="TPURaidenStoreOffloadingSpec.kernel_physical_blocks_capacity"></a>`kernel_physical_blocks_capacity` — [`L2457`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2457)
  - <a id="TPURaidenStoreOffloadingSpec.key_namespace"></a>`key_namespace` — [`L2477`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2477) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="TPURaidenStoreOffloadingSpec.kv_cache_config"></a>`kv_cache_config` — [`L2352`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2352)
  - <a id="TPURaidenStoreOffloadingSpec.kv_pool_group"></a>`kv_pool_group` — [`L2473`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2473)
  - <a id="TPURaidenStoreOffloadingSpec.offload_logical_blocks_capacity"></a>`offload_logical_blocks_capacity` — [`L2450`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2450)
  - <a id="TPURaidenStoreOffloadingSpec.pcp_size"></a>`pcp_size` — [`L2503`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2503)
  - <a id="TPURaidenStoreOffloadingSpec.pp_size"></a>`pp_size` — [`L2504`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2504)
  - <a id="TPURaidenStoreOffloadingSpec.raiden_controller_port"></a>`raiden_controller_port` — [`L2521`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2521) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="TPURaidenStoreOffloadingSpec.raiden_job_name"></a>`raiden_job_name` — [`L2541`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2541) — documented in [host-offload](../../../../concepts/host-offload.md)
  - <a id="TPURaidenStoreOffloadingSpec.storage_config"></a>`storage_config` — [`L2505`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2505)
  - <a id="TPURaidenStoreOffloadingSpec.store_server_ip"></a>`store_server_ip` — [`L2467`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2467)
  - <a id="TPURaidenStoreOffloadingSpec.tp_size"></a>`tp_size` — [`L2502`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2502)
  - <a id="TPURaidenStoreOffloadingSpec.vllm_config"></a>`vllm_config` — [`L2351`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2351)
  - <a id="TPURaidenStoreOffloadingSpec.world_size"></a>`world_size` — [`L2366`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2366)
- protocol/private: <a id="TPURaidenStoreOffloadingSpec.__init__"></a>`__init__`[`L2344`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2344), <a id="TPURaidenStoreOffloadingSpec._manager"></a>`_manager`[`L2549`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2549), <a id="TPURaidenStoreOffloadingSpec._worker"></a>`_worker`[`L2550`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2550)
- uses (calls/refs, reference-scoped): [`resolve_storage_config`](raiden_store.md#resolve_storage_config), [`resolve_block_major_contract`](block_major_layout.md#resolve_block_major_contract), [`build_worker_storage_backend_config`](raiden_store.md#build_worker_storage_backend_config), [`worker_storage_rank_coords`](raiden_store.md#worker_storage_rank_coords), [`logger`](raiden_store.md#logger), [`resolve_kernel_geometry`](raiden_store.md#resolve_kernel_geometry), [`build_store_storage_backend_config`](raiden_store.md#build_store_storage_backend_config), [`engine_rank`](raiden_store.md#StorageRankCoords.engine_rank), [`derive_offload_namespace`](raiden_store.md#derive_offload_namespace), [`pcp_size`](raiden_store.md#StorageRankCoords.pcp_size), [`pp_size`](raiden_store.md#StorageRankCoords.pp_size), [`tp_size`](raiden_store.md#StorageRankCoords.tp_size), [`storage_size`](raiden_store.md#StorageRankCoords.storage_size), [`_get_ephemeral_port_range`](raiden_store.md#_get_ephemeral_port_range), [`tp_rank`](raiden_store.md#StorageRankCoords.tp_rank), [`RaidenOffloadingManager`](raiden_store.md#RaidenOffloadingManager), [`StorageRankCoords`](raiden_store.md#StorageRankCoords), [`capacity_bytes`](raiden_store.md#RaidenStorageConfig.capacity_bytes), [`pcp_rank`](raiden_store.md#StorageRankCoords.pcp_rank), [`pp_rank`](raiden_store.md#StorageRankCoords.pp_rank), [`root_dir`](raiden_store.md#RaidenStorageConfig.root_dir), [`all_ranks_kv_bytes_per_block`](raiden_store.md#all_ranks_kv_bytes_per_block), [`model_name`](raiden_store.md#RaidenStorageConfig.model_name), [`properties`](raiden_store.md#RaidenStorageConfig.properties), [`storage_type`](raiden_store.md#RaidenStorageConfig.storage_type), [`RaidenStoreOffloadingWorker`](raiden_store.md#RaidenStoreOffloadingWorker), [`_DEFAULT_CONTROLLER_PORT`](raiden_store.md#_DEFAULT_CONTROLLER_PORT), [`_IP_LOCAL_PORT_RANGE_PATH`](raiden_store.md#_IP_LOCAL_PORT_RANGE_PATH), [`RAIDEN_SHM_KEY`](../envs.md#RAIDEN_SHM_KEY)
- used by: [`__init__`](raiden_connector.md#TPURaidenOffloadingConnector.__init__), [`__init__`](raiden_connector.md#TPURaidenOffloadingScheduler.__init__)

## Functions
- <a id="_ensure_writable_dir"></a>`_ensure_writable_dir(path: str)` — [`L2084`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2084) — Create `path` if needed and check that this process can write to it,
- <a id="_get_ephemeral_port_range"></a>`_get_ephemeral_port_range(path: str = _IP_LOCAL_PORT_RANGE_PATH)` — [`L144`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L144) — Read the host kernel's ephemeral port range (low, high) from procfs.
- <a id="_new_storage_backend_config"></a>`_new_storage_backend_config(impl: Any, storage: RaidenStorageConfig)` — [`L2275`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2275)
- <a id="_parse_storage_capacity"></a>`_parse_storage_capacity(value: str)` — [`L2002`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2002) — GiB as a string -> bytes. "" means unset and reads as 0.
- <a id="_parse_storage_flag"></a>`_parse_storage_flag(value: Any, *, default: bool, what: str)` — [`L2019`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2019) — A yes/no setting from extra config: a boolean, or one of the strings
- <a id="_parse_storage_properties"></a>`_parse_storage_properties(value: Any, source: str)` — [`L2037`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2037) — Pass-through backend properties from one source: a mapping, or a
- <a id="_resolve_multi_shapes_kv_geometry"></a>`_resolve_multi_shapes_kv_geometry(kv_cache_config: KVCacheConfig)` — [`L1486`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1486)
- <a id="_storage_setting"></a>`_storage_setting(extra_config: Mapping[str, Any], key: str, env_value: str)` — [`L1995`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1995) — One storage setting: a non-empty extra-config value, else the env value.
- <a id="_worker_kv_bytes_per_block"></a>`_worker_kv_bytes_per_block(kv_cache_config: Any)` — [`L165`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L165) — One worker's bytes per block, as vLLM's ``build_offloading_config``
- <a id="all_ranks_kv_bytes_per_block"></a>`all_ranks_kv_bytes_per_block()` — [`L201`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L201)
- <a id="build_store_storage_backend_config"></a>`build_store_storage_backend_config(impl: Any, storage: RaidenStorageConfig, coords: StorageRankCoords)` — [`L2294`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2294) — The scheduler-side store's config for the storage tier.
- <a id="build_worker_storage_backend_config"></a>`build_worker_storage_backend_config(impl: Any, storage: RaidenStorageConfig, coords: StorageRankCoords)` — [`L2314`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2314) — One worker's config for the storage tier: which shard file of each
- <a id="derive_offload_namespace"></a>`derive_offload_namespace(vllm_config: VllmConfig, *, kernel_block_size: int, per_block_shape: tuple[int, ...] | set[tuple[int, ...]], kv_dtype: object, device_block_size: int, world_size: int, num_kv_cache_groups: int, num_kv_cache_tensors: int, cp_geometry: tuple[int, ...] = (), block_major_contract: BlockMajorContract | None = None, offloaded_group_ids: tuple[int, ...] | None = None)` — [`L1395`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1395) — Derive a deterministic compatibility namespace prefixed to every store and
- <a id="has_multi_shapes_kv_caches"></a>`has_multi_shapes_kv_caches(vllm_config: VllmConfig)` — [`L216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L216) — Whether this model's KV cache consists of multiple tensors
- <a id="is_multi_shapes_geometry"></a>`is_multi_shapes_geometry(per_block_shape: object)` — [`L1477`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1477) — True when `resolve_kernel_geometry` resolved a multi-shape KV layout.
- <a id="iter_leaf_kv_cache_specs"></a>`iter_leaf_kv_cache_specs(kv_cache_spec)` — [`L205`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L205) — Yield the per-layer specs behind a KV cache group spec.
- <a id="record_all_ranks_kv_bytes_per_block"></a>`record_all_ranks_kv_bytes_per_block(kv_cache_configs: Sequence[Any])` — [`L186`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L186) — Sum the per-worker bytes per block over all workers and remember it. — documented in [host-offload](../../../../concepts/host-offload.md)
- <a id="resolve_attention_geometry"></a>`resolve_attention_geometry(vllm_config: VllmConfig, kv_cache_config: KVCacheConfig)` — [`L1521`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1521) — Resolves the attention KV cache geometry from `VllmConfig` and `KVCacheConfig`. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="resolve_kernel_geometry"></a>`resolve_kernel_geometry(vllm_config: VllmConfig, kv_cache_config: KVCacheConfig)` — [`L1626`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1626) — Resolve physical TPU kernel geometry: — documented in [host-offload](../../../../concepts/host-offload.md)
- <a id="resolve_storage_config"></a>`resolve_storage_config(extra_config: Mapping[str, Any], *, model_name: str, pp_size: int)` — [`L2101`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2101) — Read and check the storage-tier settings. None means the tier is off. — documented in [host-offload](../../../../concepts/host-offload.md)
- <a id="worker_storage_rank_coords"></a>`worker_storage_rank_coords()` — [`L2254`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L2254) — This worker's storage coordinates, read from its TP, PCP, and PP groups. — documented in [host-offload](../../../../concepts/host-offload.md)

## Module values
- <a id="_DEFAULT_CONTROLLER_PORT"></a>`_DEFAULT_CONTROLLER_PORT` — [`L139`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L139)
- <a id="_DEFAULT_EPHEMERAL_PORT_RANGE"></a>`_DEFAULT_EPHEMERAL_PORT_RANGE` — [`L141`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L141)
- <a id="_DRAIN_TIMEOUT_S"></a>`_DRAIN_TIMEOUT_S` — [`L127`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L127)
- <a id="_IP_LOCAL_PORT_RANGE_PATH"></a>`_IP_LOCAL_PORT_RANGE_PATH` — [`L140`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L140)
- <a id="_MANAGED_STORAGE_PROPERTIES"></a>`_MANAGED_STORAGE_PROPERTIES` — [`L1957`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1957)
- <a id="_POSIX_STORAGE_TYPE"></a>`_POSIX_STORAGE_TYPE` — [`L1953`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1953)
- <a id="_SAVE_RETRIES"></a>`_SAVE_RETRIES` — [`L133`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L133)
- <a id="_STORAGE_CAPACITY_GB_KEY"></a>`_STORAGE_CAPACITY_GB_KEY` — [`L1944`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1944)
- <a id="_STORAGE_MODEL_NAME_KEY"></a>`_STORAGE_MODEL_NAME_KEY` — [`L1945`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1945)
- <a id="_STORAGE_PATH_KEY"></a>`_STORAGE_PATH_KEY` — [`L1942`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1942)
- <a id="_STORAGE_PROPERTIES_KEY"></a>`_STORAGE_PROPERTIES_KEY` — [`L1946`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1946)
- <a id="_STORAGE_SKIP_PARALLELISM_CHECK_KEY"></a>`_STORAGE_SKIP_PARALLELISM_CHECK_KEY` — [`L1948`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1948)
- <a id="_STORAGE_TYPE_KEY"></a>`_STORAGE_TYPE_KEY` — [`L1943`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L1943)
- <a id="_all_ranks_kv_bytes_per_block._all_ranks_kv_bytes_per_block"></a>`_all_ranks_kv_bytes_per_block` — [`L162`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L162)
- <a id="logger"></a>`logger` — [`L123`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/offload/raiden_store.py#L123)

