---
title: 'Module: torchtitan/experiments/torchft/checkpoint.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/torchft/checkpoint.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.torchft.checkpoint`/TorchFTCheckpointManager#
symbols:
  TorchFTCheckpointManager.__init__: __init__().
  TorchFTCheckpointManager._ft_save: _ft_save().
  TorchFTCheckpointManager.enable_ft_dataloader_checkpoints: enable_ft_dataloader_checkpoints.
  TorchFTCheckpointManager._ft_load: _ft_load().
  TorchFTCheckpointManager.state_dict: state_dict().
  TorchFTCheckpointManager.ft_manager: ft_manager.
  TorchFTCheckpointManager: ''
  TorchFTCheckpointManager._save: _save().
  TorchFTCheckpointManager.load: load().
  TorchFTCheckpointManager._ft_folder: _ft_folder().
  TorchFTCheckpointManager.Config: Config#
  TorchFTCheckpointManager._wait_for_saving: _wait_for_saving().
  TorchFTCheckpointManager._states_to_load: _states_to_load().
  TorchFTCheckpointManager._should_purge: _should_purge().
  TorchFTCheckpointManager.ft_states: ft_states.
  TorchFTCheckpointManager.ft_replica_id: ft_replica_id.
  TorchFTCheckpointManager.Config.enable_ft_dataloader_checkpoints: Config#enable_ft_dataloader_checkpoints.
  TorchFTCheckpointManager.load_state_dict: load_state_dict().
  TorchFTCheckpointManager.enable_staging: enable_staging.
---
# Module: [`torchtitan/experiments/torchft/checkpoint.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py)

## Classes
### <a id="TorchFTCheckpointManager"></a>`TorchFTCheckpointManager`  ·  implements/extends CheckpointManager
- def: [`torchtitan/experiments/torchft/checkpoint.py:45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L45)
- doc: CheckpointManager with TorchFT fault tolerance support.
- signature: `class TorchFTCheckpointManager(CheckpointManager):`
- members:
  - <a id="TorchFTCheckpointManager.load"></a>`load(self, step: int = -1)` — [`L171`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L171)
  - <a id="TorchFTCheckpointManager.load_state_dict"></a>`load_state_dict(state_dict)` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L127)
  - <a id="TorchFTCheckpointManager.state_dict"></a>`state_dict()` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L118)
  - <a id="TorchFTCheckpointManager.enable_ft_dataloader_checkpoints"></a>`enable_ft_dataloader_checkpoints` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L101)
  - <a id="TorchFTCheckpointManager.enable_staging"></a>`enable_staging` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L139)
  - <a id="TorchFTCheckpointManager.ft_manager"></a>`ft_manager` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L98)
  - <a id="TorchFTCheckpointManager.ft_replica_id"></a>`ft_replica_id` — [`L135`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L135)
  - <a id="TorchFTCheckpointManager.ft_states"></a>`ft_states` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L140)
- protocol/private: <a id="TorchFTCheckpointManager.__init__"></a>`__init__`[`L73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L73), <a id="TorchFTCheckpointManager._ft_folder"></a>`_ft_folder`[`L203`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L203), <a id="TorchFTCheckpointManager._ft_load"></a>`_ft_load`[`L219`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L219), <a id="TorchFTCheckpointManager._ft_save"></a>`_ft_save`[`L206`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L206), <a id="TorchFTCheckpointManager._save"></a>`_save`[`L146`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L146), <a id="TorchFTCheckpointManager._should_purge"></a>`_should_purge`[`L195`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L195), <a id="TorchFTCheckpointManager._states_to_load"></a>`_states_to_load`[`L176`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L176), <a id="TorchFTCheckpointManager._wait_for_saving"></a>`_wait_for_saving`[`L182`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L182)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`CheckpointManager`](../../components/checkpointer/dcp.md#CheckpointManager), [`LRSchedulersContainer`](../../components/optimizer/lr_scheduler.md#LRSchedulersContainer), [`__init__`](../../components/checkpointer/dcp.md#CheckpointManager.__init__), [`OptimizersContainer`](../../components/optimizer/optimizer.md#OptimizersContainer), [`_save`](../../components/checkpointer/dcp.md#CheckpointManager._save), [`load`](../../components/checkpointer/base.md#BaseCheckpointManager.load), [`dcp_save`](../../components/checkpointer/dcp.md#CheckpointManager.dcp_save), [`save_future`](../../components/checkpointer/dcp.md#CheckpointManager.save_future), [`MODEL`](../../components/checkpointer/base.md#MODEL), [`BaseDataLoader`](../../components/data/loader.md#BaseDataLoader), [`BaseStateDictAdapter`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter), [`_find_load_step`](../../components/checkpointer/base.md#BaseCheckpointManager._find_load_step), [`pg`](../../components/checkpointer/dcp.md#CheckpointManager.pg), [`AsyncMode`](../../components/checkpointer/dcp.md#AsyncMode), [`_load_checkpoint`](../../components/checkpointer/dcp.md#CheckpointManager._load_checkpoint), [`states`](../../components/checkpointer/base.md#BaseCheckpointManager.states), [`_should_purge`](../../components/checkpointer/base.md#BaseCheckpointManager._should_purge), [`GarbageCollection`](../../tools/utils.md#GarbageCollection), [`async_mode`](../../components/checkpointer/dcp.md#CheckpointManager.async_mode), [`TorchFTManager`](manager.md#TorchFTManager), [`join`](../../tools/filesystem.md#join), [`_create_checkpoint_id`](../../components/checkpointer/base.md#BaseCheckpointManager._create_checkpoint_id), [`enable`](../../components/checkpointer/base.md#BaseCheckpointManager.enable), [`folder`](../../components/checkpointer/base.md#BaseCheckpointManager.folder), [`collect`](../../tools/utils.md#GarbageCollection.collect), [`_states_to_load`](../../components/checkpointer/base.md#BaseCheckpointManager._states_to_load), [`TorchFTOptimizersContainer`](optimizer.md#TorchFTOptimizersContainer), [`Config`](checkpoint.md#TorchFTCheckpointManager.Config), [`OPTIMIZER`](../../components/checkpointer/base.md#OPTIMIZER), [`maybe_wait_for_saving`](../../components/checkpointer/base.md#BaseCheckpointManager.maybe_wait_for_saving), [`LR_SCHEDULER`](../../components/checkpointer/base.md#LR_SCHEDULER), [`DATALOADER`](../../components/checkpointer/base.md#DATALOADER), [`replica_id`](manager.md#TorchFTManager.replica_id), [`enabled`](manager.md#TorchFTManager.enabled), [`ASYNC_WITH_PINNED_MEM`](../../components/checkpointer/dcp.md#AsyncMode.ASYNC_WITH_PINNED_MEM), [`manager`](manager.md#TorchFTManager.manager), [`ASYNC`](../../components/checkpointer/dcp.md#AsyncMode.ASYNC), [`enable_ft_dataloader_checkpoints`](checkpoint.md#TorchFTCheckpointManager.Config.enable_ft_dataloader_checkpoints), [`init_cache_state_dict`](../../components/optimizer/optimizer.md#OptimizersContainer.init_cache_state_dict)  (+1 more)
- used by: [`CheckpointManager`](../../components/checkpointer/dcp.md#CheckpointManager), [`llama3_torchft_debugmodel`](llama3/config_registry.md#llama3_torchft_debugmodel), [`_save`](../../components/checkpointer/dcp.md#CheckpointManager._save), [`load`](../../components/checkpointer/base.md#BaseCheckpointManager.load), [`_should_purge`](../../components/checkpointer/base.md#BaseCheckpointManager._should_purge), [`_wait_for_saving`](../../components/checkpointer/dcp.md#CheckpointManager._wait_for_saving), [`_states_to_load`](../../components/checkpointer/base.md#BaseCheckpointManager._states_to_load)  (5 test-only)

### <a id="TorchFTCheckpointManager.Config"></a>`TorchFTCheckpointManager.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/torchft/checkpoint.py:60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L60)
- signature: `class Config(CheckpointManager.Config):`
- members:
  - <a id="TorchFTCheckpointManager.Config.enable_ft_dataloader_checkpoints"></a>`enable_ft_dataloader_checkpoints` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/checkpoint.py#L61) — ---
- uses (calls/refs, reference-scoped): [`CheckpointManager`](../../components/checkpointer/dcp.md#CheckpointManager), [`Config`](../../components/checkpointer/dcp.md#CheckpointManager.Config)
- used by: [`llama3_torchft_debugmodel`](llama3/config_registry.md#llama3_torchft_debugmodel), [`__init__`](checkpoint.md#TorchFTCheckpointManager.__init__), [`enable_ft_dataloader_checkpoints`](checkpoint.md#TorchFTCheckpointManager.enable_ft_dataloader_checkpoints)  (3 test-only)

