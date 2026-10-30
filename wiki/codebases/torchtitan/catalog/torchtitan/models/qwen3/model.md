---
title: 'Module: torchtitan/models/qwen3/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3.model`/
symbols:
  Qwen3Model: Qwen3Model#
  Qwen3Model.Config: Qwen3Model#Config#
  Qwen3Model.Config.dim: Qwen3Model#Config#dim.
  Qwen3TransformerBlock.forward: Qwen3TransformerBlock#forward().
  Qwen3Model.Config.update_from_config: Qwen3Model#Config#update_from_config().
  Qwen3Model.Config.vocab_size: Qwen3Model#Config#vocab_size.
  Qwen3TransformerBlock: Qwen3TransformerBlock#
  Qwen3TransformerBlock.moe: Qwen3TransformerBlock#moe.
  Qwen3TransformerBlock.Config: Qwen3TransformerBlock#Config#
  Qwen3Model.Config.get_nparams_and_flops: Qwen3Model#Config#get_nparams_and_flops().
  Qwen3TransformerBlock.moe_enabled: Qwen3TransformerBlock#moe_enabled.
  Qwen3TransformerBlock.ffn_norm: Qwen3TransformerBlock#ffn_norm.
  Qwen3TransformerBlock.attention: Qwen3TransformerBlock#attention.
  Qwen3TransformerBlock.feed_forward: Qwen3TransformerBlock#feed_forward.
  Qwen3TransformerBlock.attention_norm: Qwen3TransformerBlock#attention_norm.
  Qwen3TransformerBlock.__init__: Qwen3TransformerBlock#__init__().
---
# Module: [`torchtitan/models/qwen3/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py)

## Classes
### <a id="Qwen3Model"></a>`Qwen3Model`  ·  implements/extends Decoder
- def: [`torchtitan/models/qwen3/model.py:75`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L75) — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- doc: Qwen3Model Module
- signature: `class Qwen3Model(Decoder):`
- uses (calls/refs, reference-scoped): [`Decoder`](../common/decoder.md#Decoder), [`GraphTrainerQwen3Model`](../../experiments/graph_trainer/qwen3/model.md#GraphTrainerQwen3Model)
- used by: [`reg_trainer_qwen3_8b`](../../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`qwen3_debugmodel`](../../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`qwen3_moe_235b_scan`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`Decoder`](../common/decoder.md#Decoder), [`parallelize_qwen3`](parallelize.md#parallelize_qwen3), [`_8b_tpu`](../../experiments/tpu/qwen3/__init__.md#_8b_tpu), [`_debugmodel`](__init__.md#_debugmodel), [`_0_6b`](__init__.md#_0_6b), [`_1_7b`](__init__.md#_1_7b), [`_4b`](__init__.md#_4b), [`_testmodel`](__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/qwen3/__init__.md#_testmodel_moe), [`_30b_a3b`](__init__.md#_30b_a3b), [`_14b`](__init__.md#_14b), [`_235b_a22b`](__init__.md#_235b_a22b), [`_32b`](__init__.md#_32b), [`_8b`](__init__.md#_8b), [`_debugmodel_moe`](__init__.md#_debugmodel_moe), [`qwen3_8b_first_85_pct_layers_nvfp4`](config_registry.md#qwen3_8b_first_85_pct_layers_nvfp4), [`qwen3_debugmodel_first_85_pct_layers_nvfp4`](config_registry.md#qwen3_debugmodel_first_85_pct_layers_nvfp4), [`_qwen3_cp`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_cp), [`qwen3_moe_235b_fsdp_smoke`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_fsdp_smoke), [`qwen3_moe_235b_scan_proxy`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan_proxy), [`_qwen3_dense_model_spec`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_dense_model_spec), [`_debugmodel_non_fused_qkv`](__init__.md#_debugmodel_non_fused_qkv), [`GraphTrainerQwen3Model`](../../experiments/graph_trainer/qwen3/model.md#GraphTrainerQwen3Model), [`qwen3_moe_30b_proxy`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_proxy), [`set_qwen3_sharding_config`](sharding.md#set_qwen3_sharding_config), [`MaxTextQwen3Config`](../../experiments/tpu/qwen3/model.md#MaxTextQwen3Config), [`Config`](../../experiments/graph_trainer/qwen3/model.md#GraphTrainerQwen3Model.Config), [`from_qwen3`](../../experiments/tpu/qwen3/model.md#MaxTextQwen3Config.from_qwen3), [`_30b_a3b_global_aux`](__init__.md#_30b_a3b_global_aux), [`__init__`](state_dict_adapter.md#Qwen3StateDictAdapter.__init__)  (10 test-only)

### <a id="Qwen3Model.Config"></a>`Qwen3Model.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3/model.py:84`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L84) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="Qwen3Model.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L131)
  - <a id="Qwen3Model.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L88)
  - <a id="Qwen3Model.Config.dim"></a>`dim` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L85) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
  - <a id="Qwen3Model.Config.vocab_size"></a>`vocab_size` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L86)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`Decoder`](../common/decoder.md#Decoder), [`update_from_config`](../common/decoder.md#Decoder.Config.update_from_config), [`Config`](../common/decoder.md#Decoder.Config), [`get_nparams_and_active_nparams`](../utils.md#get_nparams_and_active_nparams), [`quadratic_attention_flops_per_token`](../utils.md#quadratic_attention_flops_per_token), [`set_qwen3_sharding_config`](sharding.md#set_qwen3_sharding_config), [`update_moe_aux_loss_configs`](../common/config_utils.md#update_moe_aux_loss_configs), [`moe_load_balance_aux_loss_configs`](../common/config_utils.md#moe_load_balance_aux_loss_configs)
- used by: [`reg_trainer_qwen3_8b`](../../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`qwen3_debugmodel`](../../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`qwen3_moe_235b_scan`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`_8b_tpu`](../../experiments/tpu/qwen3/__init__.md#_8b_tpu), [`_debugmodel`](__init__.md#_debugmodel), [`_0_6b`](__init__.md#_0_6b), [`_1_7b`](__init__.md#_1_7b), [`_4b`](__init__.md#_4b), [`_testmodel`](__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/qwen3/__init__.md#_testmodel_moe), [`_30b_a3b`](__init__.md#_30b_a3b), [`_14b`](__init__.md#_14b), [`_235b_a22b`](__init__.md#_235b_a22b), [`_32b`](__init__.md#_32b), [`_8b`](__init__.md#_8b), [`_debugmodel_moe`](__init__.md#_debugmodel_moe), [`qwen3_8b_first_85_pct_layers_nvfp4`](config_registry.md#qwen3_8b_first_85_pct_layers_nvfp4), [`qwen3_debugmodel_first_85_pct_layers_nvfp4`](config_registry.md#qwen3_debugmodel_first_85_pct_layers_nvfp4), [`_qwen3_cp`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_cp), [`qwen3_moe_235b_fsdp_smoke`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_fsdp_smoke), [`qwen3_moe_235b_scan_proxy`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan_proxy), [`_qwen3_dense_model_spec`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_dense_model_spec), [`_debugmodel_non_fused_qkv`](__init__.md#_debugmodel_non_fused_qkv), [`qwen3_moe_30b_proxy`](../../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_proxy), [`set_qwen3_sharding_config`](sharding.md#set_qwen3_sharding_config), [`MaxTextQwen3Config`](../../experiments/tpu/qwen3/model.md#MaxTextQwen3Config), [`Config`](../../experiments/graph_trainer/qwen3/model.md#GraphTrainerQwen3Model.Config), [`from_qwen3`](../../experiments/tpu/qwen3/model.md#MaxTextQwen3Config.from_qwen3), [`_30b_a3b_global_aux`](__init__.md#_30b_a3b_global_aux), [`__init__`](state_dict_adapter.md#Qwen3StateDictAdapter.__init__)  (10 test-only)

### <a id="Qwen3TransformerBlock"></a>`Qwen3TransformerBlock`  ·  implements/extends TransformerBlock
- def: [`torchtitan/models/qwen3/model.py:26`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L26) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- doc: Qwen3 TransformerBlock Module
- signature: `class Qwen3TransformerBlock(TransformerBlock):`
- members:
  - <a id="Qwen3TransformerBlock.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L57)
  - <a id="Qwen3TransformerBlock.attention"></a>`attention` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L44)
  - <a id="Qwen3TransformerBlock.attention_norm"></a>`attention_norm` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L54)
  - <a id="Qwen3TransformerBlock.feed_forward"></a>`feed_forward` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L52)
  - <a id="Qwen3TransformerBlock.ffn_norm"></a>`ffn_norm` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L55)
  - <a id="Qwen3TransformerBlock.moe"></a>`moe` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L49)
  - <a id="Qwen3TransformerBlock.moe_enabled"></a>`moe_enabled` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L46)
- protocol/private: <a id="Qwen3TransformerBlock.__init__"></a>`__init__`[`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L41)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`feed_forward`](../common/decoder.md#TransformerBlock.Config.feed_forward), [`attention`](../common/decoder.md#TransformerBlock.Config.attention), [`attention_norm`](../common/decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](../common/decoder.md#TransformerBlock.Config.ffn_norm), [`moe`](../common/decoder.md#TransformerBlock.Config.moe), [`Config`](model.md#Qwen3TransformerBlock.Config)
- used by: [`_set_qwen3_layer_sharding`](sharding.md#_set_qwen3_layer_sharding), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`_build_qwen3_moe_layers`](__init__.md#_build_qwen3_moe_layers), [`_build_qwen3_layers`](__init__.md#_build_qwen3_layers), [`apply_bld_layout`](../../experiments/tpu/bld_layout.md#apply_bld_layout), [`_BLOCK_FORWARDS`](../../experiments/tpu/bld_layout.md#_BLOCK_FORWARDS)  (1 test-only)

### <a id="Qwen3TransformerBlock.Config"></a>`Qwen3TransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3/model.py:38`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/model.py#L38)
- signature: `class Config(TransformerBlock.Config):`
- uses (calls/refs, reference-scoped): [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`Config`](../common/decoder.md#TransformerBlock.Config)
- used by: [`_set_qwen3_layer_sharding`](sharding.md#_set_qwen3_layer_sharding), [`_build_qwen3_moe_layers`](__init__.md#_build_qwen3_moe_layers), [`_build_qwen3_layers`](__init__.md#_build_qwen3_layers), [`__init__`](model.md#Qwen3TransformerBlock.__init__)

