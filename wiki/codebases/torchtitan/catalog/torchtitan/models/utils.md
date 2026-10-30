---
title: 'Module: torchtitan/models/utils.py'
type: catalog
provenance: extracted
module: torchtitan/models/utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.utils`/
symbols:
  validate_converter_order: validate_converter_order().
  get_nparams_and_active_nparams: get_nparams_and_active_nparams().
  quadratic_attention_flops_per_token: quadratic_attention_flops_per_token().
  MoEStateDictAdapter: MoEStateDictAdapter#
  MoEStateDictAdapter._concatenate_expert_weights_dtensor: MoEStateDictAdapter#_concatenate_expert_weights_dtensor().
  MoEStateDictAdapter.model_config: MoEStateDictAdapter#model_config.
  MoEStateDictAdapter.__init__: MoEStateDictAdapter#__init__().
  MoEStateDictAdapter._get_local_experts_weights: MoEStateDictAdapter#_get_local_experts_weights().
  MoEStateDictAdapter.local_experts_indices: MoEStateDictAdapter#local_experts_indices.
  MoEStateDictAdapter.grouped_expert_weight_placements: MoEStateDictAdapter#grouped_expert_weight_placements.
  MoEStateDictAdapter.grouped_expert_weight_mesh: MoEStateDictAdapter#grouped_expert_weight_mesh.
  MoEStateDictAdapter.grouped_expert_weight_shape: MoEStateDictAdapter#grouped_expert_weight_shape.
  delta_rule_flops_per_token: delta_rule_flops_per_token().
  MoEStateDictAdapter._caculate_indices_from_placements: MoEStateDictAdapter#_caculate_indices_from_placements().
  MoEStateDictAdapter._split_experts_weights: MoEStateDictAdapter#_split_experts_weights().
  MoEStateDictAdapter._concatenate_expert_weights: MoEStateDictAdapter#_concatenate_expert_weights().
  MoEStateDictAdapter._calculate_strided_shard_shard_indices: MoEStateDictAdapter#_calculate_strided_shard_shard_indices().
---
# Module: [`torchtitan/models/utils.py`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py)

## Classes
### <a id="MoEStateDictAdapter"></a>`MoEStateDictAdapter`  ·  implements/extends StateDictAdapter
- def: [`torchtitan/models/utils.py:49`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L49)
- doc: StateDictAdapter for MoE models.
- signature: `class MoEStateDictAdapter(StateDictAdapter):`
- members:
  - <a id="MoEStateDictAdapter._calculate_strided_shard_shard_indices"></a>`_calculate_strided_shard_shard_indices(self, strided_shard_dim_degree: int, strided_shard_dim_rank: int, shard_dim_degree: int, shard_dim_rank: int, dim_size_to_split: int)` — [`L73`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L73) — Given a [StridedShard(dim=i), Shard(dim=i)] placement, calculate the start index
  - <a id="MoEStateDictAdapter._concatenate_expert_weights"></a>`_concatenate_expert_weights(self, expert_weights_by_layer: dict[str, dict[str, dict[int, torch.Tensor]]], abstract_key: str, layer_num: str, n_experts: int)` — [`L373`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L373) — Concatenated GroupedExperts weight using torch.stack(). Used for offline conversion.
  - <a id="MoEStateDictAdapter._concatenate_expert_weights_dtensor"></a>`_concatenate_expert_weights_dtensor(self, expert_weights_by_layer: dict[str, dict[str, dict[int, torch.Tensor]]], abstract_key: str, layer_num: str)` — [`L301`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L301) — Args:
  - <a id="MoEStateDictAdapter._get_local_experts_weights"></a>`_get_local_experts_weights(self, abstract_key: str, titan_abstract_key: str, layer_id: str, grouped_expert_weight: torch.Tensor)` — [`L193`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L193) — Split GroupedExperts weight into individual expert weights for local processing.
  - <a id="MoEStateDictAdapter._split_experts_weights"></a>`_split_experts_weights(self, weight: torch.Tensor, n_experts: int)` — [`L360`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L360) — Split the weights of the experts into a list of tensors. Used for offline conversion.
  - <a id="MoEStateDictAdapter.grouped_expert_weight_mesh"></a>`grouped_expert_weight_mesh` — [`L70`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L70)
  - <a id="MoEStateDictAdapter.grouped_expert_weight_placements"></a>`grouped_expert_weight_placements` — [`L68`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L68)
  - <a id="MoEStateDictAdapter.grouped_expert_weight_shape"></a>`grouped_expert_weight_shape` — [`L69`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L69)
  - <a id="MoEStateDictAdapter.local_experts_indices"></a>`local_experts_indices` — [`L71`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L71)
  - <a id="MoEStateDictAdapter.model_config"></a>`model_config` — [`L65`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L65)
- protocol/private: <a id="MoEStateDictAdapter.__init__"></a>`__init__`[`L59`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L59), <a id="MoEStateDictAdapter._caculate_indices_from_placements"></a>`_caculate_indices_from_placements`[`L124`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L124)
- uses (calls/refs, reference-scoped): [`Decoder`](common/decoder.md#Decoder), [`StateDictAdapter`](../protocols/state_dict_adapter.md#StateDictAdapter), [`Config`](common/decoder.md#Decoder.Config), [`DeepSeekV3StateDictAdapter`](deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter), [`__init__`](../protocols/state_dict_adapter.md#StateDictAdapter.__init__), [`Qwen3StateDictAdapter`](qwen3/state_dict_adapter.md#Qwen3StateDictAdapter), [`hf_assets_path`](../protocols/state_dict_adapter.md#BaseStateDictAdapter.hf_assets_path), [`GptOssStateDictAdapter`](gpt_oss/state_dict_adapter.md#GptOssStateDictAdapter), [`KimiK3StateDictAdapter`](kimi_k3/state_dict_adapter.md#KimiK3StateDictAdapter)
- used by: [`to_hf`](kimi_k3/state_dict_adapter.md#KimiK3StateDictAdapter.to_hf), [`from_hf`](deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.from_hf), [`StateDictAdapter`](../protocols/state_dict_adapter.md#StateDictAdapter), [`from_hf`](kimi_k3/state_dict_adapter.md#KimiK3StateDictAdapter.from_hf), [`to_hf`](deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.to_hf), [`from_hf`](qwen3/state_dict_adapter.md#Qwen3StateDictAdapter.from_hf), [`to_hf`](qwen3/state_dict_adapter.md#Qwen3StateDictAdapter.to_hf), [`from_hf`](gpt_oss/state_dict_adapter.md#GptOssStateDictAdapter.from_hf), [`DeepSeekV3StateDictAdapter`](deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter), [`Qwen3StateDictAdapter`](qwen3/state_dict_adapter.md#Qwen3StateDictAdapter), [`_map_from_hf_layer_key`](deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter._map_from_hf_layer_key), [`__init__`](deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.__init__), [`_map_to_hf_layer_key`](deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter._map_to_hf_layer_key), [`__init__`](gpt_oss/state_dict_adapter.md#GptOssStateDictAdapter.__init__), [`__init__`](kimi_k3/state_dict_adapter.md#KimiK3StateDictAdapter.__init__), [`__init__`](qwen3/state_dict_adapter.md#Qwen3StateDictAdapter.__init__), [`GptOssStateDictAdapter`](gpt_oss/state_dict_adapter.md#GptOssStateDictAdapter), [`KimiK3StateDictAdapter`](kimi_k3/state_dict_adapter.md#KimiK3StateDictAdapter)

## Functions
- <a id="delta_rule_flops_per_token"></a>`delta_rule_flops_per_token(*, num_heads: int, key_head_dim: int, v_head_dim: int)` — [`L450`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L450) — Training FLOPs per token for a recurrent delta-rule state update.
- <a id="get_nparams_and_active_nparams"></a>`get_nparams_and_active_nparams(model: nn.Module, *, modules_excluded_from_active_params: Iterable[nn.Module | None] = ())` — [`L480`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L480) — Count total and matmul-active parameters for a native decoder.
- <a id="quadratic_attention_flops_per_token"></a>`quadratic_attention_flops_per_token(*, num_heads: int, qk_head_dim: int, v_head_dim: int, seq_len: int, sliding_window_size: int | None = None)` — [`L416`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L416) — Training FLOPs per token for quadratic or windowed attention.
- <a id="validate_converter_order"></a>`validate_converter_order(converters: list)` — [`L27`](../../../../../../raw/code/torchtitan/torchtitan/models/utils.py#L27) — Validate that quantization/QAT converters precede LoRA.

