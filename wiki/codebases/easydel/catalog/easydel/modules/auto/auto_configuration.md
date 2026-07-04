---
title: 'Module: easydel/modules/auto/auto_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/auto/auto_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.auto.auto_configuration`/
symbols:
  infer_task_from_hf_config: infer_task_from_hf_config().
  AutoEasyDeLConfig.from_pretrained: AutoEasyDeLConfig#from_pretrained().
  get_modules_by_type: get_modules_by_type().
  AutoShardAndGatherFunctions.from_config: AutoShardAndGatherFunctions#from_config().
  TASK_ALIASES.TASK_ALIASES: TASK_ALIASES.TASK_ALIASES.
  AutoShardAndGatherFunctions.from_pretrained: AutoShardAndGatherFunctions#from_pretrained().
  AutoEasyDeLConfig: AutoEasyDeLConfig#
  AutoEasyDeLConfig.bind_model_task: AutoEasyDeLConfig#bind_model_task().
  logger: logger.
  AutoShardAndGatherFunctions: AutoShardAndGatherFunctions#
  normalize_task: normalize_task().
  is_flatten: is_flatten().
  AutoShardAndGatherFunctions.from_params: AutoShardAndGatherFunctions#from_params().
---
# Module: [`easydel/modules/auto/auto_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py)

## Classes
### `AutoEasyDeLConfig`
- def: [`easydel/modules/auto/auto_configuration.py:231`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L231)
- doc: Factory class for automatically loading EasyDeL model configurations.
- signature: `class AutoEasyDeLConfig:`
- members:
  - `bind_model_task(model_task: TaskType, architectures: list[str] | str)` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L249)
  - `from_pretrained(cls, pretrained_model_name_or_path: str, sharding_axis_dims: Sequence[int] = (1, -1, 1, 1, 1), sharding_dcn_axis_dims: Sequence[int] | None = None, sharding_axis_names: Sequence[str] = ("dp", "fsdp", "ep", "tp", "sp"), partition_axis: PartitionAxis | None = None, backend: EasyDeLBackends | None = None, platform: EasyDeLPlatforms | None = None, model_task: TaskType = TaskType.AUTO_BIND, from_torch: bool = False, **kwargs)` — [`L262`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L262) — The from_pretrained function is a helper function that allows you to instantiate a model from the pretrained
- uses (calls/refs, reference-scoped): [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`add_basic_configurations`](../../infra/base_config.md#EasyDeLBaseConfig.add_basic_configurations), [`infer_task_from_hf_config`](auto_configuration.md#infer_task_from_hf_config), [`get_modules_by_type`](auto_configuration.md#get_modules_by_type), [`EasyDeLBackends`](../../infra/etils.md#EasyDeLBackends), [`EasyDeLPlatforms`](../../infra/etils.md#EasyDeLPlatforms), [`from_pretrained`](../../infra/base_config.md#EasyDeLBaseConfig.from_pretrained), [`AUTO_BIND`](../../infra/factory.md#TaskType.AUTO_BIND), [`attach_custom_arguments`](../../infra/base_config.md#EasyDeLBaseConfig.attach_custom_arguments), [`_model_task`](../../infra/base_module.md#EasyDeLBaseModule._model_task), `architectures`
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`from_pretrained`](../../infra/mixins/bridge.md#EasyBridgeMixin.from_pretrained), [`load_state`](../../infra/base_state.md#EasyDeLState.load_state), [`from_pretrained`](auto_configuration.md#AutoShardAndGatherFunctions.from_pretrained), [`sub_configs`](../aya_vision/aya_vision_configuration.md#AyaVisionConfig.sub_configs), [`sub_configs`](../llava/llava_configuration.md#LlavaConfig.sub_configs)

### `AutoShardAndGatherFunctions`
- def: [`easydel/modules/auto/auto_configuration.py:334`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L334)
- doc: A class to automatically generate shard and gather functions for a given model configuration.
- signature: `class AutoShardAndGatherFunctions:`
- members:
  - `from_config(cls, config: EasyDeLBaseConfig, partition_rules: tuple[tuple[str, PartitionSpec]] | None = None, flatten: bool = True, model_task: TaskType = TaskType.CAUSAL_LM, depth_target: list[str] | None = None)` — [`L352`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L352) — Generates shard and gather functions based on a provided `EasyDeLBaseConfig` object.
  - `from_params(params, partition_rules, mesh)` — [`L392`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L392) — Generates shard and gather functions directly from model parameters, partition rules, and a mesh.
  - `from_pretrained(cls, pretrained_model_name_or_path: str, sharding_axis_dims: Sequence[int] = (1, -1, 1, 1, 1), sharding_dcn_axis_dims: Sequence[int] | None = None, sharding_axis_names: Sequence[str] = ("dp", "fsdp", "ep", "tp", "sp"), partition_axis: PartitionAxis | None = None, backend: EasyDeLBackends | None = None, platform: EasyDeLPlatforms | None = None, partition_rules: tuple[tuple[str, PartitionSpec]] | None = None, flatten: bool = True, config_kwargs: Mapping[str, tp.Any] | None = None, model_task: TaskType = TaskType.CAUSAL_LM, from_torch: bool = False, trust_remote_code: bool = False)` — [`L411`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L411) — Generates shard and gather functions based on a pretrained model name or path.
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`flatten_dict`](../../utils/traversals.md#flatten_dict), [`from_pretrained`](auto_configuration.md#AutoEasyDeLConfig.from_pretrained), [`_get_partition_rules`](../../infra/base_module.md#EasyDeLBaseModule._get_partition_rules), [`get_modules_by_type`](auto_configuration.md#get_modules_by_type), [`EasyDeLBackends`](../../infra/etils.md#EasyDeLBackends), [`unflatten_dict`](../../utils/traversals.md#unflatten_dict), [`EasyDeLPlatforms`](../../infra/etils.md#EasyDeLPlatforms), [`mesh`](../../infra/base_config.md#EasyDeLBaseConfig.mesh), [`AutoEasyDeLConfig`](auto_configuration.md#AutoEasyDeLConfig), [`lazy_init`](../../infra/base_module.md#EasyDeLBaseModule.lazy_init), [`graphtree_shape`](../../infra/base_module.md#EasyDeLBaseModule.graphtree_shape), [`is_flatten`](auto_configuration.md#is_flatten)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`_from_torch_pretrained`](../../infra/mixins/bridge.md#EasyBridgeMixin._from_torch_pretrained), [`from_pretrained`](../../infra/mixins/bridge.md#EasyBridgeMixin.from_pretrained)

## Functions
- `get_modules_by_type(model_type: str, task_type: TaskType)` — [`L32`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L32) — The get_modules_by_type function is a helper function that returns the following:
- `infer_task_from_hf_config(model_name_or_path: str)` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L101) — Infer task type from HuggingFace model config without downloading the model.
- `is_flatten(pytree: dict)` — [`L48`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L48) — The is_flatten function checks if the pytree is flattened.
- `normalize_task(t: TaskType | str | None)` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L77) — Normalize task type specification to TaskType enum.

## Module values
- `TASK_ALIASES` — [`L63`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L63)
- `logger` — [`L29`](../../../../../../../raw/code/EasyDeL/easydel/modules/auto/auto_configuration.py#L29)

