---
title: 'Module: torchtitan/experiments/torchft/manager.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/torchft/manager.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.torchft.manager`/
symbols:
  maybe_semi_sync_training: maybe_semi_sync_training().
  TorchFTManager.use_async_quorum: TorchFTManager#use_async_quorum.
  TorchFTManager._manager: TorchFTManager#_manager.
  TorchFTManager: TorchFTManager#
  TorchFTManager.get_dp_info: TorchFTManager#get_dp_info().
  TorchFTManager.maybe_set_all_reduce_hook: TorchFTManager#maybe_set_all_reduce_hook().
  TorchFTManager.loss_sync_pg: TorchFTManager#loss_sync_pg().
  TorchFTManager.replica_id: TorchFTManager#replica_id.
  TorchFTManager.Config: TorchFTManager#Config#
  TorchFTManager.replicate_pg: TorchFTManager#replicate_pg.
  TorchFTManager.enabled: TorchFTManager#enabled().
  has_torchft: has_torchft.
  TorchFTManager.Config.process_group: TorchFTManager#Config#process_group.
  TorchFTManager.__init__: TorchFTManager#__init__().
  TorchFTManager.manager: TorchFTManager#manager().
  TorchFTManager.Config.enable: TorchFTManager#Config#enable.
  TorchFTManager.group_size: TorchFTManager#group_size.
  TorchFTManager.all_reduce_hook: TorchFTManager#all_reduce_hook().
  TorchFTManager.apply_set_all_reduce_hook: TorchFTManager#apply_set_all_reduce_hook().
  TorchFTManager.Config.replica_id: TorchFTManager#Config#replica_id.
  TorchFTManager.Config.semi_sync_method: TorchFTManager#Config#semi_sync_method.
  TorchFTManager.Config.process_group_timeout_ms: TorchFTManager#Config#process_group_timeout_ms.
  TorchFTManager.Config.group_size: TorchFTManager#Config#group_size.
  TorchFTManager.Config.min_replica_size: TorchFTManager#Config#min_replica_size.
---
# Module: [`torchtitan/experiments/torchft/manager.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py)

## Classes
### <a id="TorchFTManager"></a>`TorchFTManager`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/torchft/manager.py:36`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L36)
- signature: `class TorchFTManager(Configurable):`
- members:
  - <a id="TorchFTManager.all_reduce_hook"></a>`all_reduce_hook(output)` — [`L146`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L146)
  - <a id="TorchFTManager.apply_set_all_reduce_hook"></a>`apply_set_all_reduce_hook(m)` — [`L149`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L149)
  - <a id="TorchFTManager.enabled"></a>`enabled(self)` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L129)
  - <a id="TorchFTManager.get_dp_info"></a>`get_dp_info(self, dp_degree: int, dp_rank: int)` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L137)
  - <a id="TorchFTManager.loss_sync_pg"></a>`loss_sync_pg(self)` — [`L157`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L157)
  - <a id="TorchFTManager.manager"></a>`manager(self)` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L133)
  - <a id="TorchFTManager.maybe_set_all_reduce_hook"></a>`maybe_set_all_reduce_hook(self, model_parts: list[torch.nn.Module])` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L143)
  - <a id="TorchFTManager.group_size"></a>`group_size` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L121)
  - <a id="TorchFTManager.replica_id"></a>`replica_id` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L122)
  - <a id="TorchFTManager.replicate_pg"></a>`replicate_pg` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L125)
  - <a id="TorchFTManager.use_async_quorum"></a>`use_async_quorum` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L111)
- protocol/private: <a id="TorchFTManager.__init__"></a>`__init__`[`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L79), <a id="TorchFTManager._manager"></a>`_manager`[`L84`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L84)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](manager.md#TorchFTManager.Config), [`has_torchft`](manager.md#has_torchft), [`process_group`](manager.md#TorchFTManager.Config.process_group), [`enable`](manager.md#TorchFTManager.Config.enable), [`replica_id`](manager.md#TorchFTManager.Config.replica_id), [`semi_sync_method`](manager.md#TorchFTManager.Config.semi_sync_method), [`process_group_timeout_ms`](manager.md#TorchFTManager.Config.process_group_timeout_ms), [`group_size`](manager.md#TorchFTManager.Config.group_size), [`min_replica_size`](manager.md#TorchFTManager.Config.min_replica_size)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`__init__`](trainer.md#FaultTolerantTrainer.__init__), [`pp_schedule`](trainer.md#FaultTolerantTrainer.pp_schedule), [`train_step`](trainer.md#FaultTolerantTrainer.train_step), [`train`](trainer.md#FaultTolerantTrainer.train), [`maybe_semi_sync_training`](manager.md#maybe_semi_sync_training), [`__init__`](checkpoint.md#TorchFTCheckpointManager.__init__), [`FaultTolerance`](config/job_config.md#FaultTolerance), [`ft_manager`](checkpoint.md#TorchFTCheckpointManager.ft_manager), [`__init__`](optimizer.md#TorchFTOptimizersContainer.__init__), [`ft_manager`](trainer.md#FaultTolerantTrainer.ft_manager), [`_quorum_manager`](optimizer.md#TorchFTOptimizersContainer._quorum_manager), [`ft_replica_id`](checkpoint.md#TorchFTCheckpointManager.ft_replica_id)

### <a id="TorchFTManager.Config"></a>`TorchFTManager.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/torchft/manager.py:38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L38)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="TorchFTManager.Config.enable"></a>`enable` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L39) — ---
  - <a id="TorchFTManager.Config.group_size"></a>`group_size` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L62) — ---
  - <a id="TorchFTManager.Config.min_replica_size"></a>`min_replica_size` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L69) — ---
  - <a id="TorchFTManager.Config.process_group"></a>`process_group` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L48) — ---
  - <a id="TorchFTManager.Config.process_group_timeout_ms"></a>`process_group_timeout_ms` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L53) — ---
  - <a id="TorchFTManager.Config.replica_id"></a>`replica_id` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L59) — ---
  - <a id="TorchFTManager.Config.semi_sync_method"></a>`semi_sync_method` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L72) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config)
- used by: [`llama3_torchft_debugmodel`](llama3/config_registry.md#llama3_torchft_debugmodel), [`__init__`](trainer.md#FaultTolerantTrainer.__init__), [`maybe_semi_sync_training`](manager.md#maybe_semi_sync_training), [`use_async_quorum`](manager.md#TorchFTManager.use_async_quorum), [`FaultTolerance`](config/job_config.md#FaultTolerance), [`_manager`](manager.md#TorchFTManager._manager), [`replica_id`](manager.md#TorchFTManager.replica_id), [`__init__`](manager.md#TorchFTManager.__init__), [`group_size`](manager.md#TorchFTManager.group_size)

## Functions
- <a id="maybe_semi_sync_training"></a>`maybe_semi_sync_training(ft_config: TorchFTManager.Config, ft_manager: TorchFTManager, model: torch.nn.Module, n_layers: int, optimizer: torch.optim.Optimizer, fragment_fn: Callable[..., list[nn.Module]] | None = None)` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L167) — If TorchFT is enabled and the config is set, use semi_sync_method

## Module values
- <a id="has_torchft"></a>`has_torchft` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/manager.py#L31)

