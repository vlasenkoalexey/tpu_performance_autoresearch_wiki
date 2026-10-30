---
title: 'Module: torchtitan/components/checkpointer/base.py'
type: catalog
provenance: extracted
module: torchtitan/components/checkpointer/base.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.checkpointer.base`/
symbols:
  BaseCheckpointManager.Config.interval: BaseCheckpointManager#Config#interval.
  BaseCheckpointManager.Config.last_save_model_only: BaseCheckpointManager#Config#last_save_model_only.
  BaseCheckpointManager.Config.enable: BaseCheckpointManager#Config#enable.
  BaseCheckpointManager.load: BaseCheckpointManager#load().
  BaseCheckpointManager.Config.__post_init__: BaseCheckpointManager#Config#__post_init__().
  BaseCheckpointManager._purge_stale_checkpoints: BaseCheckpointManager#_purge_stale_checkpoints().
  MODEL: MODEL.
  BaseCheckpointManager.Config.initial_load_in_hf: BaseCheckpointManager#Config#initial_load_in_hf.
  BaseCheckpointManager.Config.initial_load_path: BaseCheckpointManager#Config#initial_load_path.
  BaseCheckpointManager.sd_adapter: BaseCheckpointManager#sd_adapter.
  BaseCheckpointManager._find_load_step: BaseCheckpointManager#_find_load_step().
  BaseCheckpointManager: BaseCheckpointManager#
  BaseCheckpointManager._storage: BaseCheckpointManager#_storage.
  BaseCheckpointManager.save: BaseCheckpointManager#save().
  BaseCheckpointManager.close: BaseCheckpointManager#close().
  BaseCheckpointManager.states: BaseCheckpointManager#states.
  BaseCheckpointManager._should_purge: BaseCheckpointManager#_should_purge().
  BaseCheckpointManager.enable: BaseCheckpointManager#enable.
  BaseCheckpointManager.folder: BaseCheckpointManager#folder.
  BaseCheckpointManager._create_checkpoint_id: BaseCheckpointManager#_create_checkpoint_id().
  BaseCheckpointManager._should_save: BaseCheckpointManager#_should_save().
  BaseCheckpointManager._states_to_load: BaseCheckpointManager#_states_to_load().
  BaseCheckpointManager.Config.initial_load_model_only: BaseCheckpointManager#Config#initial_load_model_only.
  BaseCheckpointManager.Config.export_dtype: BaseCheckpointManager#Config#export_dtype.
  BaseCheckpointManager.Config.keep_latest_k: BaseCheckpointManager#Config#keep_latest_k.
  OPTIMIZER: OPTIMIZER.
  BaseCheckpointManager.maybe_wait_for_saving: BaseCheckpointManager#maybe_wait_for_saving().
  LR_SCHEDULER: LR_SCHEDULER.
  BaseCheckpointManager.maybe_wait_for_staging: BaseCheckpointManager#maybe_wait_for_staging().
  BaseCheckpointManager.Config: BaseCheckpointManager#Config#
  BaseCheckpointManager.Config.folder: BaseCheckpointManager#Config#folder.
  BaseCheckpointManager.Config.purge_exempt: BaseCheckpointManager#Config#purge_exempt.
  DATALOADER: DATALOADER.
  BaseCheckpointManager.Config.exclude_from_loading: BaseCheckpointManager#Config#exclude_from_loading.
  ModelWrapper.state_dict: ModelWrapper#state_dict().
  ModelWrapper.load_state_dict: ModelWrapper#load_state_dict().
  purge_thread: purge_thread().
  ModelWrapper.cached_state_dict: ModelWrapper#cached_state_dict.
  CheckpointStorage.isdir: CheckpointStorage#isdir().
  BaseCheckpointManager.keep_latest_k: BaseCheckpointManager#keep_latest_k.
  BaseCheckpointManager._wait_for_saving: BaseCheckpointManager#_wait_for_saving().
  BaseCheckpointManager._load_checkpoint: BaseCheckpointManager#_load_checkpoint().
  BaseCheckpointManager._save: BaseCheckpointManager#_save().
  BaseCheckpointManager._maybe_wait_for_staging: BaseCheckpointManager#_maybe_wait_for_staging().
  BaseCheckpointManager._close: BaseCheckpointManager#_close().
  BaseCheckpointManager._is_valid_checkpoint: BaseCheckpointManager#_is_valid_checkpoint().
  BaseCheckpointManager._is_resumable_checkpoint: BaseCheckpointManager#_is_resumable_checkpoint().
  BaseCheckpointManager.Config.create_seed_checkpoint: BaseCheckpointManager#Config#create_seed_checkpoint.
  ModelWrapper._get_state_dict: ModelWrapper#_get_state_dict().
  ModelWrapper: ModelWrapper#
  BaseCheckpointManager.load_only: BaseCheckpointManager#load_only.
  BaseCheckpointManager.Config.last_save_in_hf: BaseCheckpointManager#Config#last_save_in_hf.
  BaseCheckpointManager._parse_step: BaseCheckpointManager#_parse_step().
  CheckpointStorage.isfile: CheckpointStorage#isfile().
  BaseCheckpointManager.exclude_from_loading: BaseCheckpointManager#exclude_from_loading.
  BaseCheckpointManager.initial_load_path: BaseCheckpointManager#initial_load_path.
  BaseCheckpointManager.purge_exempt: BaseCheckpointManager#purge_exempt.
  BaseCheckpointManager.Config.load_step: BaseCheckpointManager#Config#load_step.
  BaseCheckpointManager.Config.load_only: BaseCheckpointManager#Config#load_only.
  BaseCheckpointManager._is_purge_exempt: BaseCheckpointManager#_is_purge_exempt().
  TRAIN_STATE: TRAIN_STATE.
  BaseCheckpointManager.interval: BaseCheckpointManager#interval.
  BaseCheckpointManager.enable_first_step_checkpoint: BaseCheckpointManager#enable_first_step_checkpoint.
  BaseCheckpointManager.initial_load_model_only: BaseCheckpointManager#initial_load_model_only.
  BaseCheckpointManager.initial_load_in_hf: BaseCheckpointManager#initial_load_in_hf.
  BaseCheckpointManager.initial_load_in_hf_quantized: BaseCheckpointManager#initial_load_in_hf_quantized.
  BaseCheckpointManager.Config.initial_load_in_hf_quantized: BaseCheckpointManager#Config#initial_load_in_hf_quantized.
  BaseCheckpointManager.Config.enable_first_step_checkpoint: BaseCheckpointManager#Config#enable_first_step_checkpoint.
  ModelWrapper.model: ModelWrapper#model.
  CheckpointStorage: CheckpointStorage#
  CheckpointStorage.listdir: CheckpointStorage#listdir().
  BaseCheckpointManager.purge_thread: BaseCheckpointManager#purge_thread.
  BaseCheckpointManager.purge_queue: BaseCheckpointManager#purge_queue.
  _shares_storage: _shares_storage().
  BaseCheckpointManager._STEP_DIR_PATTERN: BaseCheckpointManager#_STEP_DIR_PATTERN.
  ModelWrapper.__init__: ModelWrapper#__init__().
  CheckpointStorage.remove: CheckpointStorage#remove().
  BaseCheckpointManager.staging_future: BaseCheckpointManager#staging_future.
  BaseCheckpointManager.save_future: BaseCheckpointManager#save_future.
---
# Module: [`torchtitan/components/checkpointer/base.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py)

## Classes
### <a id="BaseCheckpointManager"></a>`BaseCheckpointManager`  ·  implements/extends ABC, Configurable
- def: [`torchtitan/components/checkpointer/base.py:194`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L194) — documented in [checkpointing](../../../../concepts/checkpointing.md)
- doc: Contract every TorchTitan checkpoint manager implements.
- signature: `class BaseCheckpointManager(Configurable, ABC):`
- members:
  - <a id="BaseCheckpointManager._close"></a>`_close(self)` — [`L412`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L412) — Implement ``close``. Only called when checkpointing is enabled.
  - <a id="BaseCheckpointManager._create_checkpoint_id"></a>`_create_checkpoint_id(self, step: int, folder: str = "")` — [`L373`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L373) — Standardized checkpoint path, e.g. ``checkpoints/step-100``. — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager._find_load_step"></a>`_find_load_step(self, folder: str = "")` — [`L444`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L444) — The highest step in ``folder`` that can actually be loaded. — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager._is_purge_exempt"></a>`_is_purge_exempt(self, step: int)` — [`L423`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L423) — Whether the configured exemption protects ``step`` from deletion.
  - <a id="BaseCheckpointManager._is_resumable_checkpoint"></a>`_is_resumable_checkpoint(self, checkpoint_dir: str)` — [`L441`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L441) — Whether automatic loading may select ``checkpoint_dir``.
  - <a id="BaseCheckpointManager._is_valid_checkpoint"></a>`_is_valid_checkpoint(self, checkpoint_dir: str)` — [`L433`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L433) — Whether ``checkpoint_dir`` holds a completed checkpoint.
  - <a id="BaseCheckpointManager._load_checkpoint"></a>`_load_checkpoint(self, states: dict[str, Any], checkpoint_id: str, *, from_hf: bool, from_quantized: bool)` — [`L379`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L379) — Restore ``states`` from a resolved checkpoint source.
  - <a id="BaseCheckpointManager._maybe_wait_for_staging"></a>`_maybe_wait_for_staging(self)` — [`L408`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L408) — Implement ``maybe_wait_for_staging``. Only called when enabled.
  - <a id="BaseCheckpointManager._parse_step"></a>`_parse_step(self, dirname: str)` — [`L427`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L427) — Parse a canonical ``step-N`` checkpoint directory name.
  - <a id="BaseCheckpointManager._purge_stale_checkpoints"></a>`_purge_stale_checkpoints(self, *, saving_step: int, staging_dir_prefix: str | None = None)` — [`L472`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L472) — Delete abandoned entries and reserve one retained slot for this save. — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager._save"></a>`_save(self, curr_step: int, last_step: bool = False)` — [`L404`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L404) — Implement ``save``. Only called when checkpointing is enabled.
  - <a id="BaseCheckpointManager._should_purge"></a>`_should_purge(self)` — [`L415`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L415) — Whether this rank should purge stale checkpoints.
  - <a id="BaseCheckpointManager._should_save"></a>`_should_save(self, curr_step: int, last_step: bool = False)` — [`L365`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L365) — Whether ``curr_step`` is a checkpointing step.
  - <a id="BaseCheckpointManager._states_to_load"></a>`_states_to_load(self, model_only: bool)` — [`L389`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L389) — Select the live state objects that must be restored. — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager._wait_for_saving"></a>`_wait_for_saving(self)` — [`L358`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L358) — Await ``save_future`` and clear it. Only called when it is set.
  - <a id="BaseCheckpointManager.close"></a>`close(self)` — [`L334`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L334) — Release background threads and other resources. — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.load"></a>`load(self, step: int = -1)` — [`L230`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L230) — Restore state from ``step``, or the latest checkpoint when ``-1``. — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.maybe_wait_for_saving"></a>`maybe_wait_for_saving(self)` — [`L347`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L347) — Block until the last asynchronous save completes.
  - <a id="BaseCheckpointManager.maybe_wait_for_staging"></a>`maybe_wait_for_staging(self)` — [`L328`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L328) — Block until asynchronous staging for the last save completes.
  - <a id="BaseCheckpointManager.save"></a>`save(self, curr_step: int, last_step: bool = False)` — [`L321`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L321) — Persist state for ``curr_step``.
  - <a id="BaseCheckpointManager.enable"></a>`enable` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L203) — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.enable_first_step_checkpoint"></a>`enable_first_step_checkpoint` — [`L206`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L206)
  - <a id="BaseCheckpointManager.exclude_from_loading"></a>`exclude_from_loading` — [`L212`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L212)
  - <a id="BaseCheckpointManager.folder"></a>`folder` — [`L209`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L209) — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.initial_load_in_hf"></a>`initial_load_in_hf` — [`L215`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L215)
  - <a id="BaseCheckpointManager.initial_load_in_hf_quantized"></a>`initial_load_in_hf_quantized` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L216)
  - <a id="BaseCheckpointManager.initial_load_model_only"></a>`initial_load_model_only` — [`L214`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L214)
  - <a id="BaseCheckpointManager.initial_load_path"></a>`initial_load_path` — [`L213`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L213)
  - <a id="BaseCheckpointManager.interval"></a>`interval` — [`L205`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L205)
  - <a id="BaseCheckpointManager.keep_latest_k"></a>`keep_latest_k` — [`L210`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L210)
  - <a id="BaseCheckpointManager.load_only"></a>`load_only` — [`L204`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L204)
  - <a id="BaseCheckpointManager.purge_exempt"></a>`purge_exempt` — [`L218`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L218)
  - <a id="BaseCheckpointManager.purge_queue"></a>`purge_queue` — [`L220`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L220)
  - <a id="BaseCheckpointManager.purge_thread"></a>`purge_thread` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L219)
  - <a id="BaseCheckpointManager.save_future"></a>`save_future` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L208)
  - <a id="BaseCheckpointManager.sd_adapter"></a>`sd_adapter` — [`L217`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L217) — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.staging_future"></a>`staging_future` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L207)
  - <a id="BaseCheckpointManager.states"></a>`states` — [`L211`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L211) — documented in [checkpointing](../../../../concepts/checkpointing.md)
- protocol/private: <a id="BaseCheckpointManager._STEP_DIR_PATTERN"></a>`_STEP_DIR_PATTERN`[`L223`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L223), <a id="BaseCheckpointManager._storage"></a>`_storage`[`L221`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L221)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`Configurable`](../../config/configurable.md#Configurable), [`CheckpointManager`](dcp.md#CheckpointManager), [`log_trace_span`](../../observability/structured_logger/structured_logging.md#log_trace_span), [`_save`](dcp.md#CheckpointManager._save), [`_save`](torch_checkpointing.md#TorchCheckpointingManager._save), [`MODEL`](base.md#MODEL), [`BaseStateDictAdapter`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter), [`_load_checkpoint`](dcp.md#CheckpointManager._load_checkpoint), [`GarbageCollection`](../../tools/utils.md#GarbageCollection), [`_is_valid_checkpoint`](torch_checkpointing.md#TorchCheckpointingManager._is_valid_checkpoint), [`join`](../../tools/filesystem.md#join), [`_wait_for_saving`](dcp.md#CheckpointManager._wait_for_saving), [`collect`](../../tools/utils.md#GarbageCollection.collect), [`load`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager.load), [`_close`](torch_checkpointing.md#TorchCheckpointingManager._close), [`_is_valid_checkpoint`](dcp.md#CheckpointManager._is_valid_checkpoint), [`_maybe_wait_for_staging`](dcp.md#CheckpointManager._maybe_wait_for_staging), [`hf_assets_path`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.hf_assets_path), [`_is_resumable_checkpoint`](dcp.md#CheckpointManager._is_resumable_checkpoint), [`_is_resumable_checkpoint`](torch_checkpointing.md#TorchCheckpointingManager._is_resumable_checkpoint), [`_close`](dcp.md#CheckpointManager._close), [`_should_purge`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager._should_purge), [`_states_to_load`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager._states_to_load), [`isdir`](base.md#CheckpointStorage.isdir), [`_load_checkpoint`](torch_checkpointing.md#TorchCheckpointingManager._load_checkpoint), [`_wait_for_saving`](torch_checkpointing.md#TorchCheckpointingManager._wait_for_saving), [`TorchCheckpointingManager`](torch_checkpointing.md#TorchCheckpointingManager), [`_maybe_wait_for_staging`](torch_checkpointing.md#TorchCheckpointingManager._maybe_wait_for_staging), [`CheckpointStorage`](base.md#CheckpointStorage), [`listdir`](base.md#CheckpointStorage.listdir)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`CheckpointManager`](dcp.md#CheckpointManager), [`Config`](dcp.md#CheckpointManager.Config), [`checkpoint`](../../trainer.md#Trainer.Config.checkpoint), [`train_step`](../../trainer.md#Trainer.train_step), [`start_trainer`](../../experiments/tpu/train.md#start_trainer), [`train_step`](../../experiments/torchft/trainer.md#FaultTolerantTrainer.train_step), [`train`](../../experiments/torchft/trainer.md#FaultTolerantTrainer.train), [`train`](../../trainer.md#Trainer.train), [`__init__`](dcp.md#CheckpointManager.__init__), [`purge_thread`](torch_checkpointing.md#TorchCheckpointingManager.purge_thread), [`inference`](../../models/flux/inference/infer.md#inference), [`train_step`](../../models/flux/trainer.md#FluxTrainer.train_step), [`_save`](dcp.md#CheckpointManager._save), [`_save_last_step`](torch_checkpointing.md#TorchCheckpointingManager._save_last_step), [`main`](../../train.md#main), [`close`](../../trainer.md#Trainer.close), [`export_dtype`](torch_checkpointing.md#TorchCheckpointingManager.export_dtype), [`_save`](torch_checkpointing.md#TorchCheckpointingManager._save), [`dcp_save`](dcp.md#CheckpointManager.dcp_save), [`_save_last_step`](dcp.md#CheckpointManager._save_last_step), [`save_future`](dcp.md#CheckpointManager.save_future), [`_ft_save`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager._ft_save), [`enable_ft_dataloader_checkpoints`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager.enable_ft_dataloader_checkpoints), [`_ft_load`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager._ft_load), [`purge_queue`](dcp.md#CheckpointManager.purge_queue), [`purge_queue`](torch_checkpointing.md#TorchCheckpointingManager.purge_queue), [`__init__`](torch_checkpointing.md#TorchCheckpointingManager.__init__), [`checkpointer`](../../trainer.md#Trainer.checkpointer), [`_load_checkpoint`](dcp.md#CheckpointManager._load_checkpoint), [`state_dict`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager.state_dict), [`_is_valid_checkpoint`](torch_checkpointing.md#TorchCheckpointingManager._is_valid_checkpoint), [`export_dtype`](dcp.md#CheckpointManager.export_dtype), [`_manager_config`](torch_checkpointing.md#TorchCheckpointingManager._manager_config), [`load`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager.load), [`_manager`](torch_checkpointing.md#TorchCheckpointingManager._manager), [`_ft_folder`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager._ft_folder), [`__post_init__`](dcp.md#CheckpointManager.Config.__post_init__), [`_close`](torch_checkpointing.md#TorchCheckpointingManager._close), [`_is_valid_checkpoint`](dcp.md#CheckpointManager._is_valid_checkpoint)  (+13 more; 5 test-only)

### <a id="BaseCheckpointManager.Config"></a>`BaseCheckpointManager.Config`  ·  implements/extends Config
- def: [`torchtitan/components/checkpointer/base.py:529`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L529) — documented in [checkpointing](../../../../concepts/checkpointing.md)
- doc: Checkpoint policies shared by concrete TorchTitan checkpoint managers.
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="BaseCheckpointManager.Config.create_seed_checkpoint"></a>`create_seed_checkpoint` — [`L578`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L578) — ---
  - <a id="BaseCheckpointManager.Config.enable"></a>`enable` — [`L532`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L532) — --- — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.Config.enable_first_step_checkpoint"></a>`enable_first_step_checkpoint` — [`L575`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L575) — ---
  - <a id="BaseCheckpointManager.Config.exclude_from_loading"></a>`exclude_from_loading` — [`L572`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L572) — ---
  - <a id="BaseCheckpointManager.Config.export_dtype"></a>`export_dtype` — [`L559`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L559) — --- — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.Config.folder"></a>`folder` — [`L535`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L535) — ---
  - <a id="BaseCheckpointManager.Config.initial_load_in_hf"></a>`initial_load_in_hf` — [`L547`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L547) — --- — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.Config.initial_load_in_hf_quantized"></a>`initial_load_in_hf_quantized` — [`L550`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L550) — ---
  - <a id="BaseCheckpointManager.Config.initial_load_model_only"></a>`initial_load_model_only` — [`L544`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L544) — ---
  - <a id="BaseCheckpointManager.Config.initial_load_path"></a>`initial_load_path` — [`L541`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L541) — --- — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.Config.interval"></a>`interval` — [`L538`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L538) — --- — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.Config.keep_latest_k"></a>`keep_latest_k` — [`L562`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L562) — ---
  - <a id="BaseCheckpointManager.Config.last_save_in_hf"></a>`last_save_in_hf` — [`L556`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L556) — ---
  - <a id="BaseCheckpointManager.Config.last_save_model_only"></a>`last_save_model_only` — [`L553`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L553) — --- — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="BaseCheckpointManager.Config.load_only"></a>`load_only` — [`L581`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L581) — ---
  - <a id="BaseCheckpointManager.Config.load_step"></a>`load_step` — [`L568`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L568) — ---
  - <a id="BaseCheckpointManager.Config.purge_exempt"></a>`purge_exempt` — [`L565`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L565) — ---
- protocol/private: <a id="BaseCheckpointManager.Config.__post_init__"></a>`__post_init__`[`L584`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L584)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config), [`MODEL`](base.md#MODEL), [`is_remote`](../../tools/filesystem.md#is_remote), [`OPTIMIZER`](base.md#OPTIMIZER), [`LR_SCHEDULER`](base.md#LR_SCHEDULER), [`Function`](../../config/function.md#Function), [`Config`](../../config/function.md#Function.Config)
- used by: [`sft_llama3_8b_metamath`](../../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](../../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](../../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../../models/llama3/config_registry.md#llama3_debugmodel), [`_qwen3_moe_30b_fsdp_only_full_ac`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](../../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`flux_dev`](../../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../../models/flux/config_registry.md#flux_schnell), [`__init__`](../../experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`llama3_405b`](../../models/llama3/config_registry.md#llama3_405b), [`_tpu_hf_config`](../../experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`transformers_modeling_backend_sft_full`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`qwen35_debugmodel_moe`](../../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen38_debugmodel_moe`](../../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`Config`](dcp.md#CheckpointManager.Config), [`transfer_stream`](../../trainer.md#Trainer.transfer_stream), [`deepseek_v4_flash`](../../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](../../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](../../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`qwen3_debugmodel`](../../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`qwen35_debugmodel`](../../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`kimi_k2_5`](../../models/kimi_k2_7/config_registry.md#kimi_k2_5)  (+62 more; 44 test-only)

### <a id="CheckpointStorage"></a>`CheckpointStorage`  ·  implements/extends Protocol
- def: [`torchtitan/components/checkpointer/base.py:155`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L155)
- doc: The path operations a checkpoint manager needs from its storage.
- signature: `class CheckpointStorage(Protocol):`
- members:
  - <a id="CheckpointStorage.isdir"></a>`isdir(self, path: str)` — [`L177`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L177) — Whether ``path`` is an existing directory. — documented in [checkpointing](../../../../concepts/checkpointing.md)
  - <a id="CheckpointStorage.isfile"></a>`isfile(self, path: str)` — [`L181`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L181) — Whether ``path`` is an existing entry that is not a directory.
  - <a id="CheckpointStorage.listdir"></a>`listdir(self, path: str)` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L185) — The entry names directly under the directory ``path``.
  - <a id="CheckpointStorage.remove"></a>`remove(self, path: str)` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L189) — Recursively delete the directory ``path``.
- used by: [`load`](base.md#BaseCheckpointManager.load), [`_purge_stale_checkpoints`](base.md#BaseCheckpointManager._purge_stale_checkpoints), [`_find_load_step`](base.md#BaseCheckpointManager._find_load_step), [`_storage`](base.md#BaseCheckpointManager._storage), [`_should_purge`](base.md#BaseCheckpointManager._should_purge), [`_is_valid_checkpoint`](torch_checkpointing.md#TorchCheckpointingManager._is_valid_checkpoint), [`_is_valid_checkpoint`](dcp.md#CheckpointManager._is_valid_checkpoint), [`_is_resumable_checkpoint`](dcp.md#CheckpointManager._is_resumable_checkpoint), [`_is_resumable_checkpoint`](torch_checkpointing.md#TorchCheckpointingManager._is_resumable_checkpoint)

### <a id="ModelWrapper"></a>`ModelWrapper`
- def: [`torchtitan/components/checkpointer/base.py:93`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L93)
- doc: A wrapper for `nn.Module` (or a list of modules) that provides a unified `Stateful`
- signature: `class ModelWrapper(Stateful):`
- members:
  - <a id="ModelWrapper.load_state_dict"></a>`load_state_dict(self, state_dict: dict[str, Any])` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L145)
  - <a id="ModelWrapper.state_dict"></a>`state_dict(self)` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L130)
  - <a id="ModelWrapper.cached_state_dict"></a>`cached_state_dict` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L124)
  - <a id="ModelWrapper.model"></a>`model` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L123)
- protocol/private: <a id="ModelWrapper.__init__"></a>`__init__`[`L122`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L122), <a id="ModelWrapper._get_state_dict"></a>`_get_state_dict`[`L126`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L126)
- uses (calls/refs, reference-scoped): [`_shares_storage`](base.md#_shares_storage)
- used by: [`__init__`](dcp.md#CheckpointManager.__init__), [`purge_thread`](torch_checkpointing.md#TorchCheckpointingManager.purge_thread)

## Functions
- <a id="_shares_storage"></a>`_shares_storage(a: torch.Tensor, b: torch.Tensor)` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L78) — Whether ``a`` and ``b`` are backed by the same storage.
- <a id="purge_thread"></a>`purge_thread(purge_queue: queue.Queue[str | None], remove_path: Callable[[str], None])` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L40) — Thread to purge the old checkpoints.

## Module values
- <a id="DATALOADER"></a>`DATALOADER` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L36)
- <a id="LR_SCHEDULER"></a>`LR_SCHEDULER` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L35)
- <a id="MODEL"></a>`MODEL` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L33) — documented in [checkpointing](../../../../concepts/checkpointing.md)
- <a id="OPTIMIZER"></a>`OPTIMIZER` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L34)
- <a id="TRAIN_STATE"></a>`TRAIN_STATE` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/components/checkpointer/base.py#L37)

