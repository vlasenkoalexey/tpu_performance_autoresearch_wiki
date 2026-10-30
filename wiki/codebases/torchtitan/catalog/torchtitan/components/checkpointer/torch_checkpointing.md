---
title: 'Module: torchtitan/components/checkpointer/torch_checkpointing.py'
type: catalog
provenance: extracted
module: torchtitan/components/checkpointer/torch_checkpointing.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.checkpointer.torch_checkpointing`/
symbols:
  TorchCheckpointingManager.purge_thread: TorchCheckpointingManager#purge_thread.
  TorchCheckpointingManager._save_last_step: TorchCheckpointingManager#_save_last_step().
  TorchCheckpointingManager.export_dtype: TorchCheckpointingManager#export_dtype.
  TorchCheckpointingManager._save: TorchCheckpointingManager#_save().
  TorchCheckpointingManager.purge_queue: TorchCheckpointingManager#purge_queue.
  TorchCheckpointingManager.__init__: TorchCheckpointingManager#__init__().
  TorchCheckpointingManager._is_valid_checkpoint: TorchCheckpointingManager#_is_valid_checkpoint().
  TorchCheckpointingManager._manager_config: TorchCheckpointingManager#_manager_config.
  TorchCheckpointingManager._manager: TorchCheckpointingManager#_manager.
  TorchCheckpointingManager._close: TorchCheckpointingManager#_close().
  _writer_config: _writer_config().
  _default_backend_config: _default_backend_config().
  TorchCheckpointingManager._is_resumable_checkpoint: TorchCheckpointingManager#_is_resumable_checkpoint().
  TorchCheckpointingManager._should_prewarm: TorchCheckpointingManager#_should_prewarm().
  TorchCheckpointingManager._prewarmed: TorchCheckpointingManager#_prewarmed.
  _item_specs: _item_specs().
  _sync_save_config: _sync_save_config().
  _async_save_config: _async_save_config().
  TorchCheckpointingManager.Config: TorchCheckpointingManager#Config#
  _BackendCheckpointStorage._storage: _BackendCheckpointStorage#_storage.
  TorchCheckpointingManager._load_checkpoint: TorchCheckpointingManager#_load_checkpoint().
  TorchCheckpointingManager._wait_for_saving: TorchCheckpointingManager#_wait_for_saving().
  TorchCheckpointingManager.last_save_in_hf: TorchCheckpointingManager#last_save_in_hf.
  _HF_INDEX_FILE_NAME: _HF_INDEX_FILE_NAME.
  _BackendCheckpointStorage.remove: _BackendCheckpointStorage#remove().
  _init_subprocess_logging: _init_subprocess_logging().
  TorchCheckpointingManager.last_save_model_only: TorchCheckpointingManager#last_save_model_only.
  _DEFAULT_BARRIER_TIMEOUT_SEC: _DEFAULT_BARRIER_TIMEOUT_SEC.
  TorchCheckpointingManager.save_future: TorchCheckpointingManager#save_future.
  _BackendCheckpointStorage.isdir: _BackendCheckpointStorage#isdir().
  _BackendCheckpointStorage.isfile: _BackendCheckpointStorage#isfile().
  _BackendCheckpointStorage.listdir: _BackendCheckpointStorage#listdir().
  TorchCheckpointingManager: TorchCheckpointingManager#
  TorchCheckpointingManager.__del__: TorchCheckpointingManager#__del__().
  TorchCheckpointingManager._maybe_wait_for_staging: TorchCheckpointingManager#_maybe_wait_for_staging().
  DEFAULT_TORCH_CHECKPOINTING_BARRIER_TCPSTORE_PORT: DEFAULT_TORCH_CHECKPOINTING_BARRIER_TCPSTORE_PORT.
  _DEFAULT_BARRIER_INIT_TIMEOUT_SEC: _DEFAULT_BARRIER_INIT_TIMEOUT_SEC.
  CHECKPOINTING_LOGGER_NAME: CHECKPOINTING_LOGGER_NAME.
  _BackendCheckpointStorage: _BackendCheckpointStorage#
  _BackendCheckpointStorage.__init__: _BackendCheckpointStorage#__init__().
---
# Module: [`torchtitan/components/checkpointer/torch_checkpointing.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py)

## Classes
### <a id="TorchCheckpointingManager"></a>`TorchCheckpointingManager`  ·  implements/extends BaseCheckpointManager
- def: [`torchtitan/components/checkpointer/torch_checkpointing.py:209`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L209)
- doc: TorchTitan checkpoint manager backed by `torch_checkpointing`.
- signature: `class TorchCheckpointingManager(BaseCheckpointManager):`
- members:
  - <a id="TorchCheckpointingManager._is_resumable_checkpoint"></a>`_is_resumable_checkpoint(self, checkpoint_dir: str)` — [`L400`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L400) — Whether automatic loading may select ``checkpoint_dir``.
  - <a id="TorchCheckpointingManager.export_dtype"></a>`export_dtype` — [`L277`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L277)
  - <a id="TorchCheckpointingManager.last_save_in_hf"></a>`last_save_in_hf` — [`L276`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L276)
  - <a id="TorchCheckpointingManager.last_save_model_only"></a>`last_save_model_only` — [`L275`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L275)
  - <a id="TorchCheckpointingManager.purge_queue"></a>`purge_queue` — [`L308`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L308)
  - <a id="TorchCheckpointingManager.purge_thread"></a>`purge_thread` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L241) — documented in [training-components](../../../../concepts/training-components.md)
  - <a id="TorchCheckpointingManager.save_future"></a>`save_future` — [`L240`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L240)
- protocol/private: <a id="TorchCheckpointingManager.__del__"></a>`__del__`[`L321`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L321), <a id="TorchCheckpointingManager.__init__"></a>`__init__`[`L224`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L224), <a id="TorchCheckpointingManager._close"></a>`_close`[`L443`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L443), <a id="TorchCheckpointingManager._is_valid_checkpoint"></a>`_is_valid_checkpoint`[`L411`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L411), <a id="TorchCheckpointingManager._load_checkpoint"></a>`_load_checkpoint`[`L327`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L327), <a id="TorchCheckpointingManager._manager"></a>`_manager`[`L305`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L305), <a id="TorchCheckpointingManager._manager_config"></a>`_manager_config`[`L292`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L292), <a id="TorchCheckpointingManager._maybe_wait_for_staging"></a>`_maybe_wait_for_staging`[`L429`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L429), <a id="TorchCheckpointingManager._prewarmed"></a>`_prewarmed`[`L297`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L297), <a id="TorchCheckpointingManager._save"></a>`_save`[`L365`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L365), <a id="TorchCheckpointingManager._save_last_step"></a>`_save_last_step`[`L456`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L456), <a id="TorchCheckpointingManager._should_prewarm"></a>`_should_prewarm`[`L542`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L542), <a id="TorchCheckpointingManager._wait_for_saving"></a>`_wait_for_saving`[`L436`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L436)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`build`](../../config/configurable.md#Configurable.Config.build), [`LRSchedulersContainer`](../optimizer/lr_scheduler.md#LRSchedulersContainer), [`TORCH_DTYPE_MAP`](../../config/__init__.md#TORCH_DTYPE_MAP), [`interval`](base.md#BaseCheckpointManager.Config.interval), [`last_save_model_only`](base.md#BaseCheckpointManager.Config.last_save_model_only), [`enable`](base.md#BaseCheckpointManager.Config.enable), [`OptimizersContainer`](../optimizer/optimizer.md#OptimizersContainer), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`_purge_stale_checkpoints`](base.md#BaseCheckpointManager._purge_stale_checkpoints), [`MODEL`](base.md#MODEL), [`fqn_to_index_mapping`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`initial_load_in_hf`](base.md#BaseCheckpointManager.Config.initial_load_in_hf), [`BaseDataLoader`](../data/loader.md#BaseDataLoader), [`BaseStateDictAdapter`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter), [`initial_load_path`](base.md#BaseCheckpointManager.Config.initial_load_path), [`sd_adapter`](base.md#BaseCheckpointManager.sd_adapter), [`BaseCheckpointManager`](base.md#BaseCheckpointManager), [`_storage`](base.md#BaseCheckpointManager._storage), [`close`](base.md#BaseCheckpointManager.close), [`states`](base.md#BaseCheckpointManager.states), [`GarbageCollection`](../../tools/utils.md#GarbageCollection), [`add_step_tag`](../../observability/structured_logger/step_state.md#add_step_tag), [`join`](../../tools/filesystem.md#join), [`_create_checkpoint_id`](base.md#BaseCheckpointManager._create_checkpoint_id), [`enable`](base.md#BaseCheckpointManager.enable), [`folder`](base.md#BaseCheckpointManager.folder), [`collect`](../../tools/utils.md#GarbageCollection.collect), [`_should_save`](base.md#BaseCheckpointManager._should_save), [`export_dtype`](base.md#BaseCheckpointManager.Config.export_dtype), [`initial_load_model_only`](base.md#BaseCheckpointManager.Config.initial_load_model_only), [`keep_latest_k`](base.md#BaseCheckpointManager.Config.keep_latest_k), [`is_remote`](../../tools/filesystem.md#is_remote), [`OPTIMIZER`](base.md#OPTIMIZER), [`maybe_wait_for_saving`](base.md#BaseCheckpointManager.maybe_wait_for_saving), [`_default_backend_config`](torch_checkpointing.md#_default_backend_config), [`LR_SCHEDULER`](base.md#LR_SCHEDULER), [`folder`](base.md#BaseCheckpointManager.Config.folder), [`purge_exempt`](base.md#BaseCheckpointManager.Config.purge_exempt), [`DATALOADER`](base.md#DATALOADER)  (+25 more)
- used by: [`BaseCheckpointManager`](base.md#BaseCheckpointManager), [`_close`](base.md#BaseCheckpointManager._close), [`_is_resumable_checkpoint`](base.md#BaseCheckpointManager._is_resumable_checkpoint), [`_is_valid_checkpoint`](base.md#BaseCheckpointManager._is_valid_checkpoint), [`_load_checkpoint`](base.md#BaseCheckpointManager._load_checkpoint), [`_maybe_wait_for_staging`](base.md#BaseCheckpointManager._maybe_wait_for_staging), [`_save`](base.md#BaseCheckpointManager._save), [`_wait_for_saving`](base.md#BaseCheckpointManager._wait_for_saving)

### <a id="TorchCheckpointingManager.Config"></a>`TorchCheckpointingManager.Config`  ·  implements/extends Config
- def: [`torchtitan/components/checkpointer/torch_checkpointing.py:221`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L221) — documented in [checkpointing](../../../../concepts/checkpointing.md)
- signature: `class Config(BaseCheckpointManager.Config):`
- uses (calls/refs, reference-scoped): [`BaseCheckpointManager`](base.md#BaseCheckpointManager), [`Config`](base.md#BaseCheckpointManager.Config)
- used by: [`__init__`](torch_checkpointing.md#TorchCheckpointingManager.__init__)

### <a id="_BackendCheckpointStorage"></a>`_BackendCheckpointStorage`
- def: [`torchtitan/components/checkpointer/torch_checkpointing.py:76`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L76)
- doc: `CheckpointStorage` backed by a `torch_checkpointing` `Storage`.
- signature: `class _BackendCheckpointStorage:`
- members:
  - <a id="_BackendCheckpointStorage.isdir"></a>`isdir(self, path: str)` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L97)
  - <a id="_BackendCheckpointStorage.isfile"></a>`isfile(self, path: str)` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L100)
  - <a id="_BackendCheckpointStorage.listdir"></a>`listdir(self, path: str)` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L104)
  - <a id="_BackendCheckpointStorage.remove"></a>`remove(self, path: str)` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L107)
- protocol/private: <a id="_BackendCheckpointStorage.__init__"></a>`__init__`[`L94`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L94), <a id="_BackendCheckpointStorage._storage"></a>`_storage`[`L95`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L95)
- used by: [`purge_queue`](torch_checkpointing.md#TorchCheckpointingManager.purge_queue), [`_manager_config`](torch_checkpointing.md#TorchCheckpointingManager._manager_config)

## Functions
- <a id="_async_save_config"></a>`_async_save_config()` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L165)
- <a id="_default_backend_config"></a>`_default_backend_config(save_config: CheckpointSaverConfig, *, storage_config: StorageConfig | None = None, items: dict[str, ItemSpec] | None = None, subprocess_init_fn: Callable[..., None] | None = None, subprocess_init_args: tuple[Any, ...] = (), pre_finalize_callback: Callable[[str, EventLogger], None] | None = None)` — [`L180`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L180)
- <a id="_init_subprocess_logging"></a>`_init_subprocess_logging(structured_logger_init_fn: Callable[[], None], init_fn: Callable[..., None] | None, init_args: tuple[Any, ...])` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L111) — Re-establish structured logging inside the async save subprocess.
- <a id="_item_specs"></a>`_item_specs()` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L133)
- <a id="_sync_save_config"></a>`_sync_save_config(*, use_barrier: bool = True)` — [`L173`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L173)
- <a id="_writer_config"></a>`_writer_config(*, use_barrier: bool)` — [`L149`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L149)

## Module values
- <a id="CHECKPOINTING_LOGGER_NAME"></a>`CHECKPOINTING_LOGGER_NAME` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L73)
- <a id="DEFAULT_TORCH_CHECKPOINTING_BARRIER_TCPSTORE_PORT"></a>`DEFAULT_TORCH_CHECKPOINTING_BARRIER_TCPSTORE_PORT` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L64)
- <a id="_DEFAULT_BARRIER_INIT_TIMEOUT_SEC"></a>`_DEFAULT_BARRIER_INIT_TIMEOUT_SEC` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L65)
- <a id="_DEFAULT_BARRIER_TIMEOUT_SEC"></a>`_DEFAULT_BARRIER_TIMEOUT_SEC` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L66)
- <a id="_HF_INDEX_FILE_NAME"></a>`_HF_INDEX_FILE_NAME` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/torch_checkpointing.py#L70)

