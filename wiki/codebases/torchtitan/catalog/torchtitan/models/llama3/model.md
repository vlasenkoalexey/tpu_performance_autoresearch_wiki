---
title: 'Module: torchtitan/models/llama3/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/llama3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.llama3.model`/
symbols:
  Llama3Model: Llama3Model#
  Llama3Model.Config: Llama3Model#Config#
  Llama3Model.Config.dim: Llama3Model#Config#dim.
  Llama3TransformerBlock.forward: Llama3TransformerBlock#forward().
  Llama3TransformerBlock.attention: Llama3TransformerBlock#attention.
  Llama3Model.Config.vocab_size: Llama3Model#Config#vocab_size.
  Llama3TransformerBlock: Llama3TransformerBlock#
  Llama3Model.Config.update_from_config: Llama3Model#Config#update_from_config().
  Llama3TransformerBlock.Config: Llama3TransformerBlock#Config#
  Llama3Model.Config.get_nparams_and_flops: Llama3Model#Config#get_nparams_and_flops().
  Llama3TransformerBlock.feed_forward: Llama3TransformerBlock#feed_forward.
  Llama3TransformerBlock.attention_norm: Llama3TransformerBlock#attention_norm.
  Llama3TransformerBlock.ffn_norm: Llama3TransformerBlock#ffn_norm.
  Llama3TransformerBlock.__init__: Llama3TransformerBlock#__init__().
---
# Module: [`torchtitan/models/llama3/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py)

## Classes
### <a id="Llama3Model"></a>`Llama3Model`  ·  implements/extends Decoder
- def: [`torchtitan/models/llama3/model.py:59`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L59) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- doc: Llama3Model Module
- signature: `class Llama3Model(Decoder):`
- uses (calls/refs, reference-scoped): [`Decoder`](../common/decoder.md#Decoder), [`GraphTrainerLlama3Model`](../../experiments/graph_trainer/llama3/model.md#GraphTrainerLlama3Model)  (1 test-only)
- used by: [`Decoder`](../common/decoder.md#Decoder), [`_1b`](__init__.md#_1b), [`_3b`](__init__.md#_3b), [`_405b`](__init__.md#_405b), [`_70b`](__init__.md#_70b), [`_8b`](__init__.md#_8b), [`_debugmodel`](__init__.md#_debugmodel), [`_testmodel`](../../experiments/tpu/llama3/__init__.md#_testmodel), [`parallelize_llama`](parallelize.md#parallelize_llama), [`llama3_8b_first_85_pct_layers_nvfp4`](config_registry.md#llama3_8b_first_85_pct_layers_nvfp4), [`llama3_debugmodel_first_85_pct_layers_nvfp4`](config_registry.md#llama3_debugmodel_first_85_pct_layers_nvfp4), [`set_llama3_sharding_config`](sharding.md#set_llama3_sharding_config), [`_upstream_flavor`](../../experiments/tpu/llama3/__init__.md#_upstream_flavor), [`GraphTrainerLlama3Model`](../../experiments/graph_trainer/llama3/model.md#GraphTrainerLlama3Model), [`__init__`](state_dict_adapter.md#Llama3StateDictAdapter.__init__), [`logger`](state_dict_adapter.md#logger), [`Config`](../../experiments/graph_trainer/llama3/model.md#GraphTrainerLlama3Model.Config)  (13 test-only)

### <a id="Llama3Model.Config"></a>`Llama3Model.Config`  ·  implements/extends Config
- def: [`torchtitan/models/llama3/model.py:68`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L68) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="Llama3Model.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L88)
  - <a id="Llama3Model.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L72) — documented in [llama3-model](../../../../concepts/llama3-model.md)
  - <a id="Llama3Model.Config.dim"></a>`dim` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L69) — documented in [llama3-model](../../../../concepts/llama3-model.md)
  - <a id="Llama3Model.Config.vocab_size"></a>`vocab_size` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L70) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`Decoder`](../common/decoder.md#Decoder), [`update_from_config`](../common/decoder.md#Decoder.Config.update_from_config), [`Config`](../common/decoder.md#Decoder.Config), [`get_nparams_and_active_nparams`](../utils.md#get_nparams_and_active_nparams), [`quadratic_attention_flops_per_token`](../utils.md#quadratic_attention_flops_per_token), [`set_llama3_sharding_config`](sharding.md#set_llama3_sharding_config)
- used by: [`_1b`](__init__.md#_1b), [`_3b`](__init__.md#_3b), [`_405b`](__init__.md#_405b), [`_70b`](__init__.md#_70b), [`_8b`](__init__.md#_8b), [`_debugmodel`](__init__.md#_debugmodel), [`_testmodel`](../../experiments/tpu/llama3/__init__.md#_testmodel), [`llama3_8b_first_85_pct_layers_nvfp4`](config_registry.md#llama3_8b_first_85_pct_layers_nvfp4), [`llama3_debugmodel_first_85_pct_layers_nvfp4`](config_registry.md#llama3_debugmodel_first_85_pct_layers_nvfp4), [`from_hf`](state_dict_adapter.md#Llama3StateDictAdapter.from_hf), [`to_hf`](state_dict_adapter.md#Llama3StateDictAdapter.to_hf), [`set_llama3_sharding_config`](sharding.md#set_llama3_sharding_config), [`_upstream_flavor`](../../experiments/tpu/llama3/__init__.md#_upstream_flavor), [`__init__`](state_dict_adapter.md#Llama3StateDictAdapter.__init__), [`Config`](../../experiments/graph_trainer/llama3/model.md#GraphTrainerLlama3Model.Config)  (11 test-only)

### <a id="Llama3TransformerBlock"></a>`Llama3TransformerBlock`  ·  implements/extends TransformerBlock
- def: [`torchtitan/models/llama3/model.py:22`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L22) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- doc: Llama3 TransformerBlock Module
- signature: `class Llama3TransformerBlock(TransformerBlock):`
- members:
  - <a id="Llama3TransformerBlock.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L45) — documented in [llama3-model](../../../../concepts/llama3-model.md)
  - <a id="Llama3TransformerBlock.attention"></a>`attention` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L39)
  - <a id="Llama3TransformerBlock.attention_norm"></a>`attention_norm` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L42)
  - <a id="Llama3TransformerBlock.feed_forward"></a>`feed_forward` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L41)
  - <a id="Llama3TransformerBlock.ffn_norm"></a>`ffn_norm` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L43)
- protocol/private: <a id="Llama3TransformerBlock.__init__"></a>`__init__`[`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L37)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`feed_forward`](../common/decoder.md#TransformerBlock.Config.feed_forward), [`attention`](../common/decoder.md#TransformerBlock.Config.attention), [`attention_norm`](../common/decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](../common/decoder.md#TransformerBlock.Config.ffn_norm), [`Config`](model.md#Llama3TransformerBlock.Config)
- used by: [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`_build_llama3_layers`](__init__.md#_build_llama3_layers), [`apply_bld_layout`](../../experiments/tpu/bld_layout.md#apply_bld_layout), [`_set_llama3_layer_sharding`](sharding.md#_set_llama3_layer_sharding), [`_BLOCK_FORWARDS`](../../experiments/tpu/bld_layout.md#_BLOCK_FORWARDS)  (1 test-only)

### <a id="Llama3TransformerBlock.Config"></a>`Llama3TransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/llama3/model.py:34`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/model.py#L34) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- signature: `class Config(TransformerBlock.Config):`
- uses (calls/refs, reference-scoped): [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`Config`](../common/decoder.md#TransformerBlock.Config)
- used by: [`_build_llama3_layers`](__init__.md#_build_llama3_layers), [`_set_llama3_layer_sharding`](sharding.md#_set_llama3_layer_sharding), [`__init__`](model.md#Llama3TransformerBlock.__init__)

