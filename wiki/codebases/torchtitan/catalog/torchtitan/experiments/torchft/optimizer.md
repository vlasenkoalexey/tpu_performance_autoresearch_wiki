---
title: 'Module: torchtitan/experiments/torchft/optimizer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/torchft/optimizer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.torchft.optimizer`/
symbols:
  TorchFTOptimizersContainer.__init__: TorchFTOptimizersContainer#__init__().
  TorchFTOptimizersContainer: TorchFTOptimizersContainer#
  TorchFTOptimizersContainer.Config: TorchFTOptimizersContainer#Config#
  TorchFTOptimizersContainer._quorum_manager: TorchFTOptimizersContainer#_quorum_manager.
  TorchFTOptimizersContainer._refresh_cached_state_dict: TorchFTOptimizersContainer#_refresh_cached_state_dict().
  TorchFTOptimizersContainer.load_state_dict: TorchFTOptimizersContainer#load_state_dict().
  TorchFTOptimizersContainer.init_cache_state_dict: TorchFTOptimizersContainer#init_cache_state_dict().
  TorchFTOptimizersContainer.cache_state_dict: TorchFTOptimizersContainer#cache_state_dict.
  TorchFTOptimizersContainer.step: TorchFTOptimizersContainer#step().
  TorchFTOptimizersContainer.zero_grad: TorchFTOptimizersContainer#zero_grad().
  TorchFTOptimizersContainer.state_dict: TorchFTOptimizersContainer#state_dict().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/torchft/optimizer.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py)

## Classes
### <a id="TorchFTOptimizersContainer"></a>`TorchFTOptimizersContainer`  ·  implements/extends OptimizersContainer
- def: [`torchtitan/experiments/torchft/optimizer.py:25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L25)
- signature: `class TorchFTOptimizersContainer(OptimizersContainer):`
- members:
  - <a id="TorchFTOptimizersContainer.init_cache_state_dict"></a>`init_cache_state_dict(self)` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L49)
  - <a id="TorchFTOptimizersContainer.load_state_dict"></a>`load_state_dict(self, state_dict: dict[str, Any])` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L63)
  - <a id="TorchFTOptimizersContainer.state_dict"></a>`state_dict(self)` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L52)
  - <a id="TorchFTOptimizersContainer.step"></a>`step(self, closure: Callable[[], float] | None = None)` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L71)
  - <a id="TorchFTOptimizersContainer.zero_grad"></a>`zero_grad(self, set_to_none: bool = True)` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L83)
  - <a id="TorchFTOptimizersContainer.cache_state_dict"></a>`cache_state_dict` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L43)
- protocol/private: <a id="TorchFTOptimizersContainer.__init__"></a>`__init__`[`L30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L30), <a id="TorchFTOptimizersContainer._quorum_manager"></a>`_quorum_manager`[`L45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L45), <a id="TorchFTOptimizersContainer._refresh_cached_state_dict"></a>`_refresh_cached_state_dict`[`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L55)
- uses (calls/refs, reference-scoped): [`OptimizersContainer`](../../components/optimizer/optimizer.md#OptimizersContainer), [`__init__`](../../components/optimizer/optimizer.md#OptimizersContainer.__init__), [`optimizers`](../../components/optimizer/optimizer.md#OptimizersContainer.optimizers), [`use_async_quorum`](manager.md#TorchFTManager.use_async_quorum), [`TorchFTManager`](manager.md#TorchFTManager), [`get_flat_optim_state_dict`](../../components/optimizer/utils.md#get_flat_optim_state_dict), [`load_state_dict`](../../components/optimizer/optimizer.md#OptimizersContainer.load_state_dict), [`state_dict`](../../components/optimizer/optimizer.md#OptimizersContainer.state_dict), [`zero_grad`](../../components/optimizer/optimizer.md#OptimizersContainer.zero_grad), [`Config`](optimizer.md#TorchFTOptimizersContainer.Config), [`init_optim_state`](../../components/optimizer/utils.md#init_optim_state), [`manager`](manager.md#TorchFTManager.manager)
- used by: [`llama3_torchft_debugmodel`](llama3/config_registry.md#llama3_torchft_debugmodel), [`pp_schedule`](trainer.md#FaultTolerantTrainer.pp_schedule), [`OptimizersContainer`](../../components/optimizer/optimizer.md#OptimizersContainer), [`state_dict`](checkpoint.md#TorchFTCheckpointManager.state_dict), [`load_state_dict`](../../components/optimizer/optimizer.md#OptimizersContainer.load_state_dict), [`state_dict`](../../components/optimizer/optimizer.md#OptimizersContainer.state_dict), [`zero_grad`](../../components/optimizer/optimizer.md#OptimizersContainer.zero_grad), [`step`](../../components/optimizer/optimizer.md#OptimizersContainer.step), [`init_cache_state_dict`](../../components/optimizer/optimizer.md#OptimizersContainer.init_cache_state_dict)  (1 test-only)

### <a id="TorchFTOptimizersContainer.Config"></a>`TorchFTOptimizersContainer.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/torchft/optimizer.py:27`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L27)
- signature: `class Config(OptimizersContainer.Config):`
- uses (calls/refs, reference-scoped): [`OptimizersContainer`](../../components/optimizer/optimizer.md#OptimizersContainer), [`Config`](../../components/optimizer/optimizer.md#OptimizersContainer.Config)
- used by: [`llama3_torchft_debugmodel`](llama3/config_registry.md#llama3_torchft_debugmodel), [`pp_schedule`](trainer.md#FaultTolerantTrainer.pp_schedule), [`__init__`](optimizer.md#TorchFTOptimizersContainer.__init__)  (1 test-only)

## Module values
- <a id="__all__"></a>`__all__` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/optimizer.py#L22)

