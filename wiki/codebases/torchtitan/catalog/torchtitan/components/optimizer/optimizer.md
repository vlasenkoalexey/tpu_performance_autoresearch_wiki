---
title: 'Module: torchtitan/components/optimizer/optimizer.py'
type: catalog
provenance: extracted
module: torchtitan/components/optimizer/optimizer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.optimizer.optimizer`/
symbols:
  default_adamw: default_adamw().
  OptimizersContainer: OptimizersContainer#
  register_moe_load_balancing_hook: register_moe_load_balancing_hook().
  OptimizersContainer.__init__: OptimizersContainer#__init__().
  register_moe_load_balancing_hook._update_expert_bias: register_moe_load_balancing_hook()._update_expert_bias().
  OptimizersContainer.Config.implementation: OptimizersContainer#Config#implementation.
  OptimizersContainer.Config: OptimizersContainer#Config#
  OptimizersContainer.optimizers: OptimizersContainer#optimizers.
  ParamGroupConfig: ParamGroupConfig#
  OptimizersContainer._build_param_groups: OptimizersContainer#_build_param_groups().
  collect_moe_routing_metric_tensors: collect_moe_routing_metric_tensors().
  ParamGroupConfig.pattern: ParamGroupConfig#pattern.
  get_moe_load_balancing_metrics: get_moe_load_balancing_metrics().
  OptimizersContainer.Config.param_groups: OptimizersContainer#Config#param_groups.
  ParamGroupConfig.optimizer_name: ParamGroupConfig#optimizer_name.
  OptimizersContainer.zero_grad: OptimizersContainer#zero_grad().
  OptimizersContainer.state_dict: OptimizersContainer#state_dict().
  OptimizersContainer.load_state_dict: OptimizersContainer#load_state_dict().
  set_moe_routing_metric_tensors: set_moe_routing_metric_tensors().
  OptimizersContainer.step: OptimizersContainer#step().
  ParamGroupConfig.optimizer_kwargs: ParamGroupConfig#optimizer_kwargs.
  _iter_moe_layers: _iter_moe_layers().
  OptimizersContainer._register_bf16_optimizer_state_hook: OptimizersContainer#_register_bf16_optimizer_state_hook().
  configure_moe_routing_metrics: configure_moe_routing_metrics().
  OptimizersContainer._build_impl_kwargs: OptimizersContainer#_build_impl_kwargs().
  register_moe_load_balancing_hook._should_register_moe_balancing_hook: register_moe_load_balancing_hook()._should_register_moe_balancing_hook().
  OptimizersContainer.__iter__: OptimizersContainer#__iter__().
  T: T.
  _moe_routing_metrics_aux_loss: _moe_routing_metrics_aux_loss().
  OptimizersContainer._resolve_optimizer_factory: OptimizersContainer#_resolve_optimizer_factory().
  OptimizersContainer._log_optimizer: OptimizersContainer#_log_optimizer().
  OptimizersContainer._validate_params: OptimizersContainer#_validate_params().
  OptimizersContainer.init_cache_state_dict: OptimizersContainer#init_cache_state_dict().
  _MoELike.load_balance_coeff: _MoELike#load_balance_coeff.
  OptimizersContainer.Config.optimizer_factory_kwargs_by_name: OptimizersContainer#Config#optimizer_factory_kwargs_by_name.
  OptimizersContainer.model_parts: OptimizersContainer#model_parts.
  OptimizersContainer.__len__: OptimizersContainer#__len__().
  _MoELike: _MoELike#
  _MoELike.tokens_per_expert_E: _MoELike#tokens_per_expert_E.
  _local_metric_tensor: _local_metric_tensor().
  _MoELike.expert_bias_E: _MoELike#expert_bias_E.
  OptimizersContainer._post_init: OptimizersContainer#_post_init().
  OptimizersContainer._bf16_state_init_hook: OptimizersContainer#_bf16_state_init_hook().
  OptimizersContainer._bf16_state_load_hook: OptimizersContainer#_bf16_state_load_hook().
  register_moe_load_balancing_hook._is_recomputation_enabled: register_moe_load_balancing_hook()._is_recomputation_enabled().
  _all_reduce_moe_metric_sums: _all_reduce_moe_metric_sums().
  __all__: __all__.
---
# Module: [`torchtitan/components/optimizer/optimizer.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py)

## Classes
### <a id="OptimizersContainer"></a>`OptimizersContainer`  ·  implements/extends Configurable, Generic
- def: [`torchtitan/components/optimizer/optimizer.py:84`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L84) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- doc: A container for multiple optimizers, supporting mixed optimizer types.
- signature: `class OptimizersContainer(Optimizer, Stateful, Configurable, Generic[T]):`
- members:
  - <a id="OptimizersContainer._build_impl_kwargs"></a>`_build_impl_kwargs(config: Config)` — [`L158`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L158) — Build implementation-related kwargs (fused/foreach) from config. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer._build_param_groups"></a>`_build_param_groups(model: nn.Module, param_group_configs: list[ParamGroupConfig], impl_kwargs: dict[str, Any])` — [`L173`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L173) — Build PyTorch param groups from model parameters, partitioned by optimizer. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer._log_optimizer"></a>`_log_optimizer(self, optimizer: Optimizer, part_idx: int, patterns: list[str])` — [`L250`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L250) — Log one optimizer's param-group assignments (patterns are logging-only). — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer._register_bf16_optimizer_state_hook"></a>`_register_bf16_optimizer_state_hook(self)` — [`L337`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L337) — Create and restore Adam optimizer states in bfloat16. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer._validate_params"></a>`_validate_params(self, all_params: list[nn.Parameter])` — [`L273`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L273) — Verify every trainable param is assigned to exactly one optimizer.
  - <a id="OptimizersContainer.init_cache_state_dict"></a>`init_cache_state_dict(self)` — [`L391`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L391) — Initialize cached state dict for TorchFT. No-op for base class.
  - <a id="OptimizersContainer.load_state_dict"></a>`load_state_dict(self, state_dict: dict[str, Any])` — [`L325`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L325) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer.state_dict"></a>`state_dict(self)` — [`L311`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L311) — Return a flat, FQN-keyed optimizer state dict for all optimizers. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer.step"></a>`step(self, closure: Callable[[], float] | None = None)` — [`L294`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L294) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer.zero_grad"></a>`zero_grad(self, set_to_none: bool = True)` — [`L307`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L307) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer.model_parts"></a>`model_parts` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L144)
  - <a id="OptimizersContainer.optimizers"></a>`optimizers` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L143) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- protocol/private: <a id="OptimizersContainer.__init__"></a>`__init__`[`L223`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L223), <a id="OptimizersContainer.__iter__"></a>`__iter__`[`L287`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L287), <a id="OptimizersContainer.__len__"></a>`__len__`[`L290`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L290), <a id="OptimizersContainer._bf16_state_init_hook"></a>`_bf16_state_init_hook`[`L350`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L350), <a id="OptimizersContainer._bf16_state_load_hook"></a>`_bf16_state_load_hook`[`L377`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L377), <a id="OptimizersContainer._post_init"></a>`_post_init`[`L332`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L332), <a id="OptimizersContainer._resolve_optimizer_factory"></a>`_resolve_optimizer_factory`[`L147`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L147)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`Configurable`](../../config/configurable.md#Configurable), [`implementation`](optimizer.md#OptimizersContainer.Config.implementation), [`Config`](optimizer.md#OptimizersContainer.Config), [`ParamGroupConfig`](optimizer.md#ParamGroupConfig), [`build_dist_muon`](../../distributed/flex_shard/dist_muon.md#build_dist_muon), [`get_flat_optim_state_dict`](utils.md#get_flat_optim_state_dict), [`pattern`](optimizer.md#ParamGroupConfig.pattern), [`TorchFTOptimizersContainer`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer), [`param_groups`](optimizer.md#OptimizersContainer.Config.param_groups), [`optimizer_name`](optimizer.md#ParamGroupConfig.optimizer_name), [`optimizer_kwargs`](optimizer.md#ParamGroupConfig.optimizer_kwargs), [`init_optim_state`](utils.md#init_optim_state), [`load_state_dict`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.load_state_dict), [`canonical_fqn`](../checkpointer/utils.md#canonical_fqn), [`init_cache_state_dict`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.init_cache_state_dict), [`step`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.step), [`zero_grad`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.zero_grad), [`load_flat_optim_state_dict`](utils.md#load_flat_optim_state_dict), [`T`](optimizer.md#T), [`optimizer_factory_kwargs_by_name`](optimizer.md#OptimizersContainer.Config.optimizer_factory_kwargs_by_name), [`state_dict`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.state_dict)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`default_adamw`](optimizer.md#default_adamw), [`train_step`](../../trainer.md#Trainer.train_step), [`optimizer`](../../trainer.md#Trainer.Config.optimizer), [`train_step`](../../experiments/torchft/trainer.md#FaultTolerantTrainer.train_step), [`_dist_muon_optimizer`](../../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`__init__`](../checkpointer/dcp.md#CheckpointManager.__init__), [`_fwd_bwd_adamw_step`](../../experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._fwd_bwd_adamw_step), [`train_step`](../../models/flux/trainer.md#FluxTrainer.train_step), [`__init__`](../../experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer.__init__), [`register_moe_load_balancing_hook`](optimizer.md#register_moe_load_balancing_hook), [`qwen3_debugmodel_moe_param_groups`](../../models/qwen3/config_registry.md#qwen3_debugmodel_moe_param_groups), [`optimizers`](../../trainer.md#Trainer.optimizers), [`optimizer`](../../experiments/rl/actors/trainer.md#PolicyTrainer.Config.optimizer), [`__init__`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager.__init__), [`enable_ft_dataloader_checkpoints`](../../experiments/torchft/checkpoint.md#TorchFTCheckpointManager.enable_ft_dataloader_checkpoints), [`__init__`](../checkpointer/torch_checkpointing.md#TorchCheckpointingManager.__init__), [`_align_dist_muon_expert_compute_layouts`](../../models/kimi_k2_7/config_registry.md#_align_dist_muon_expert_compute_layouts), [`__init__`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.__init__), [`register_qk_clip_hook`](../../models/kimi_k2_7/qk_clip.md#register_qk_clip_hook), [`TorchFTOptimizersContainer`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer), [`register_aux_loss_zero_hook`](../../models/common/aux_loss.md#register_aux_loss_zero_hook), [`_register_optimizer_hooks`](../../models/kimi_k2_7/__init__.md#_register_optimizer_hooks), [`Config`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.Config), [`_refresh_cached_state_dict`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer._refresh_cached_state_dict), [`load_state_dict`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.load_state_dict), [`init_cache_state_dict`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.init_cache_state_dict), [`__init__`](lr_scheduler.md#LRSchedulersContainer.__init__), [`step`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.step), [`zero_grad`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.zero_grad), [`optimizers`](../metrics.md#MetricsProcessor.optimizers)  (5 test-only)

### <a id="OptimizersContainer.Config"></a>`OptimizersContainer.Config`  ·  implements/extends Config
- def: [`torchtitan/components/optimizer/optimizer.py:108`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L108) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="OptimizersContainer.Config.implementation"></a>`implementation` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L114) — --- — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="OptimizersContainer.Config.optimizer_factory_kwargs_by_name"></a>`optimizer_factory_kwargs_by_name` — [`L132`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L132) — ---
  - <a id="OptimizersContainer.Config.param_groups"></a>`param_groups` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L109) — --- — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config), [`ParamGroupConfig`](optimizer.md#ParamGroupConfig)
- used by: [`start_trainer`](../../experiments/tpu/conformer/train_minimal.md#start_trainer), [`_qwen3_moe_30b_fsdp_only_full_ac`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`qwen3_moe_30b`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`default_adamw`](optimizer.md#default_adamw), [`optimizer`](../../trainer.md#Trainer.Config.optimizer), [`_dist_muon_optimizer`](../../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`muse_glimmer_30b_full_logits`](../../experiments/tpu/muse_glimmer/config_registry.md#muse_glimmer_30b_full_logits), [`_on_scan_lane`](../../experiments/tpu/llama3/config_registry.md#_on_scan_lane), [`__init__`](optimizer.md#OptimizersContainer.__init__), [`start_trainer`](../../experiments/tpu/train_minimal.md#start_trainer), [`qwen3_debugmodel_moe_param_groups`](../../models/qwen3/config_registry.md#qwen3_debugmodel_moe_param_groups), [`model`](../../experiments/tpu/train_minimal.md#TrainerMinimal.model), [`optimizer`](../../experiments/rl/actors/trainer.md#PolicyTrainer.Config.optimizer), [`_align_dist_muon_expert_compute_layouts`](../../models/kimi_k2_7/config_registry.md#_align_dist_muon_expert_compute_layouts), [`Config`](../../experiments/torchft/optimizer.md#TorchFTOptimizersContainer.Config), [`_build_impl_kwargs`](optimizer.md#OptimizersContainer._build_impl_kwargs)  (8 test-only)

### <a id="ParamGroupConfig"></a>`ParamGroupConfig`
- def: [`torchtitan/components/optimizer/optimizer.py:46`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L46) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- doc: Configuration for a parameter group with its own optimizer.
- signature: `class ParamGroupConfig:`
- members:
  - <a id="ParamGroupConfig.optimizer_kwargs"></a>`optimizer_kwargs` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L70) — --- — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="ParamGroupConfig.optimizer_name"></a>`optimizer_name` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L67) — --- — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
  - <a id="ParamGroupConfig.pattern"></a>`pattern` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L63) — --- — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- used by: [`default_adamw`](optimizer.md#default_adamw), [`_dist_muon_optimizer`](../../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`qwen3_debugmodel_moe_param_groups`](../../models/qwen3/config_registry.md#qwen3_debugmodel_moe_param_groups), [`_build_param_groups`](optimizer.md#OptimizersContainer._build_param_groups), [`param_groups`](optimizer.md#OptimizersContainer.Config.param_groups)  (4 test-only)

### <a id="_MoELike"></a>`_MoELike`  ·  implements/extends Protocol
- def: [`torchtitan/components/optimizer/optimizer.py:78`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L78)
- signature: `class _MoELike(Protocol):`
- members:
  - <a id="_MoELike.expert_bias_E"></a>`expert_bias_E` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L81)
  - <a id="_MoELike.load_balance_coeff"></a>`load_balance_coeff` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L79)
  - <a id="_MoELike.tokens_per_expert_E"></a>`tokens_per_expert_E` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L80)
- used by: [`_update_expert_bias`](optimizer.md#register_moe_load_balancing_hook._update_expert_bias), [`_iter_moe_layers`](optimizer.md#_iter_moe_layers), [`_should_register_moe_balancing_hook`](optimizer.md#register_moe_load_balancing_hook._should_register_moe_balancing_hook)

## Functions
- <a id="_all_reduce_moe_metric_sums"></a>`_all_reduce_moe_metric_sums(values: torch.Tensor, aux_loss: Any)` — [`L730`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L730)
- <a id="register_moe_load_balancing_hook._is_recomputation_enabled"></a>`_is_recomputation_enabled(module)` — [`L481`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L481)
- <a id="_iter_moe_layers"></a>`_iter_moe_layers(model_parts: list[nn.Module])` — [`L425`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L425) — Yield ``(transformer_block, moe)`` for every MoE layer in the model. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="_local_metric_tensor"></a>`_local_metric_tensor(value: torch.Tensor)` — [`L588`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L588)
- <a id="_moe_routing_metrics_aux_loss"></a>`_moe_routing_metrics_aux_loss(moe: nn.Module)` — [`L558`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L558) — Return the MoE's router aux loss if it produces routing metrics. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="register_moe_load_balancing_hook._should_register_moe_balancing_hook"></a>`_should_register_moe_balancing_hook(model_parts: list[nn.Module])` — [`L465`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L465) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="register_moe_load_balancing_hook._update_expert_bias"></a>`_update_expert_bias(model_parts: list[nn.Module], parallel_dims: ParallelDims)` — [`L484`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L484) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="collect_moe_routing_metric_tensors"></a>`collect_moe_routing_metric_tensors(model_parts: list[nn.Module])` — [`L594`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L594) — Collect the fixed-shape local tensors produced by the latest forward. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="configure_moe_routing_metrics"></a>`configure_moe_routing_metrics(model_parts: list[nn.Module], enabled: bool)` — [`L570`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L570) — Enable graph-safe routing metric capture on supported MoE layers. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="default_adamw"></a>`default_adamw(lr: float = 0.0008, **kwargs: Any)` — [`L396`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L396) — Create an OptimizersContainer.Config with a catch-all AdamW param group. — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="get_moe_load_balancing_metrics"></a>`get_moe_load_balancing_metrics(model_parts: list[nn.Module])` — [`L654`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L654) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="register_moe_load_balancing_hook"></a>`register_moe_load_balancing_hook(optimizers: OptimizersContainer, model_parts: list[nn.Module], parallel_dims: ParallelDims)` — [`L449`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L449) — Register an optimizer step pre-hook for MoE auxiliary-loss-free load balancing. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="set_moe_routing_metric_tensors"></a>`set_moe_routing_metric_tensors(model_parts: list[nn.Module], metric_tensors: list[torch.Tensor])` — [`L625`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L625) — Restore graph outputs as runtime sidecars consumed by metric logging. — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)

## Module values
- <a id="T"></a>`T` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L75) — documented in [optimizers-and-lr-schedulers](../../../../concepts/optimizers-and-lr-schedulers.md)
- <a id="__all__"></a>`__all__` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/components/optimizer/optimizer.py#L33)

