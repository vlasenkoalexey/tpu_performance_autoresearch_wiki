---
title: 'Module: torchtitan/models/deepseek_v3/mtp.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v3/mtp.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v3.mtp`/
symbols:
  MTPDecoder.preprocess_inputs: MTPDecoder#preprocess_inputs().
  MTPTransformerBlock.forward: MTPTransformerBlock#forward().
  MTPDecoder.mtp_layers: MTPDecoder#mtp_layers.
  MTPDecoder.forward: MTPDecoder#forward().
  MTPDecoder.Config.update_from_config: MTPDecoder#Config#update_from_config().
  MTPDecoder: MTPDecoder#
  MTPDecoder.Config.mtp_layers: MTPDecoder#Config#mtp_layers.
  apply_fsdp_to_mtp_decoder: apply_fsdp_to_mtp_decoder().
  MTPLoss.__call__: MTPLoss#__call__().
  MTPDecoder.__init__: MTPDecoder#__init__().
  MTPTransformerBlock.Config: MTPTransformerBlock#Config#
  MTPDecoder.Config: MTPDecoder#Config#
  MTPTransformerBlock.moe: MTPTransformerBlock#moe.
  MTPLoss: MTPLoss#
  MTPLoss.Config: MTPLoss#Config#
  MTPLoss.__init__: MTPLoss#__init__().
  MTPTransformerBlock.Config.enorm: MTPTransformerBlock#Config#enorm.
  MTPTransformerBlock.Config.hnorm: MTPTransformerBlock#Config#hnorm.
  MTPTransformerBlock.Config.eh_proj: MTPTransformerBlock#Config#eh_proj.
  MTPTransformerBlock.Config.mtp_norm: MTPTransformerBlock#Config#mtp_norm.
  MTPTransformerBlock.ffn_norm: MTPTransformerBlock#ffn_norm.
  MTPTransformerBlock.moe_enabled: MTPTransformerBlock#moe_enabled.
  MTPTransformerBlock: MTPTransformerBlock#
  MTPTransformerBlock.attention: MTPTransformerBlock#attention.
  MTPTransformerBlock.attention_norm: MTPTransformerBlock#attention_norm.
  MTPTransformerBlock.enorm: MTPTransformerBlock#enorm.
  MTPTransformerBlock.hnorm: MTPTransformerBlock#hnorm.
  MTPTransformerBlock.eh_proj: MTPTransformerBlock#eh_proj.
  MTPTransformerBlock.mtp_norm: MTPTransformerBlock#mtp_norm.
  MTPTransformerBlock.feed_forward: MTPTransformerBlock#feed_forward.
  roll_mtp_sequence: roll_mtp_sequence().
  MTPLoss.mtp_scale: MTPLoss#mtp_scale.
  MTPTransformerBlock.__init__: MTPTransformerBlock#__init__().
  MTPLoss.Config.mtp_scale: MTPLoss#Config#mtp_scale.
---
# Module: [`torchtitan/models/deepseek_v3/mtp.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py)

## Classes
### <a id="MTPDecoder"></a>`MTPDecoder`  ·  implements/extends Decoder
- def: [`torchtitan/models/deepseek_v3/mtp.py:170`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L170) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- doc: Decoder variant that owns MTP layers.
- signature: `class MTPDecoder(Decoder):`
- members:
  - <a id="MTPDecoder.forward"></a>`forward(self, tokens: torch.Tensor | tuple[torch.Tensor, ...], positions: torch.Tensor | None = None, attention_masks: AttentionMasksType | None = None, mtp_input_valid_masks: tuple[torch.Tensor, ...] | None = None)` — [`L321`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L321) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="MTPDecoder.preprocess_inputs"></a>`preprocess_inputs(self, input_dict: dict[str, torch.Tensor], *, parallel_dims: ParallelDims, parallelism: ParallelismConfig, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L224`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L224) — Prepare aligned pairs before applying CP sharding and annotations. — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="MTPDecoder.mtp_layers"></a>`mtp_layers` — [`L212`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L212) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- protocol/private: <a id="MTPDecoder.__init__"></a>`__init__`[`L209`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L209)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`ParallelismConfig`](../../config/configs.md#ParallelismConfig), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`Decoder`](../common/decoder.md#Decoder), [`spmd_backend`](../../config/configs.md#ParallelismConfig.spmd_backend), [`get_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_mesh), [`VarlenInnerAttention`](../common/attention.md#VarlenInnerAttention), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`get_attention_masks`](../common/decoder.md#Decoder.get_attention_masks), [`preprocess_inputs`](../kimi_k2_7/model.md#KimiK25Model.preprocess_inputs), [`DeepSeekV3Model`](model.md#DeepSeekV3Model), [`IGNORE_INDEX`](../../components/loss.md#IGNORE_INDEX), [`forward`](../common/decoder.md#Decoder.forward), [`Config`](../common/attention.md#FlexInnerAttention.Config), [`tok_embeddings`](../common/decoder.md#Decoder.tok_embeddings), [`cp_enabled`](../../distributed/parallel_dims.md#ParallelDims.cp_enabled), [`lm_head`](../common/decoder.md#Decoder.lm_head), [`Config`](../common/attention.md#VarlenInnerAttention.Config), [`ModuleList`](../../protocols/module.md#ModuleList), [`decoder_input_sharding`](../common/decoder_sharding.md#decoder_input_sharding), [`norm`](../common/decoder.md#Decoder.norm), [`layers`](../common/decoder.md#Decoder.layers), [`annotate_input_spmd_types`](../../distributed/spmd_types.md#annotate_input_spmd_types), [`prepare_context_parallel_input`](../../distributed/context_parallel/api.md#prepare_context_parallel_input), [`context_parallel_load_balancer`](../../config/configs.md#ParallelismConfig.context_parallel_load_balancer), [`forward`](../kimi_k2_7/model.md#KimiK25Model.forward), [`config`](../common/decoder.md#Decoder.config), [`first_full_attention_backend`](../common/decoder.md#Decoder.Config.first_full_attention_backend), [`mtp_layers`](mtp.md#MTPDecoder.Config.mtp_layers), [`__init__`](../common/decoder.md#Decoder.__init__), [`Config`](mtp.md#MTPDecoder.Config), [`Config`](mtp.md#MTPTransformerBlock.Config), [`_skip_lm_head`](../common/decoder.md#Decoder._skip_lm_head), [`MTPTransformerBlock`](mtp.md#MTPTransformerBlock), [`context_parallel_ptrr_mask_key`](../../config/configs.md#ParallelismConfig.context_parallel_ptrr_mask_key), [`roll_mtp_sequence`](mtp.md#roll_mtp_sequence)
- used by: [`Decoder`](../common/decoder.md#Decoder), [`preprocess_inputs`](../common/decoder.md#Decoder.preprocess_inputs), [`DeepSeekV3Model`](model.md#DeepSeekV3Model), [`forward`](../common/decoder.md#Decoder.forward), [`Config`](model.md#DeepSeekV3Model.Config), [`get_deepseek_v3_nparams_and_flops`](model.md#get_deepseek_v3_nparams_and_flops), [`apply_fsdp_to_mtp_decoder`](mtp.md#apply_fsdp_to_mtp_decoder), [`update_from_config`](model.md#DeepSeekV3Model.Config.update_from_config), [`__init__`](../../experiments/graph_trainer/deepseek_v3/model.md#GraphTrainerDeepSeekV3Model.__init__), [`__init__`](../kimi_k2_7/model.md#KimiK25Model.__init__)

### <a id="MTPDecoder.Config"></a>`MTPDecoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v3/mtp.py:179`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L179)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="MTPDecoder.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L182`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L182)
  - <a id="MTPDecoder.Config.mtp_layers"></a>`mtp_layers` — [`L180`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L180)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`Decoder`](../common/decoder.md#Decoder), [`update_from_config`](../common/decoder.md#Decoder.Config.update_from_config), [`Config`](../common/decoder.md#Decoder.Config)
- used by: [`_16b`](__init__.md#_16b), [`_236b`](__init__.md#_236b), [`_671b`](__init__.md#_671b), [`_debugmodel`](__init__.md#_debugmodel), [`_testmodel`](__init__.md#_testmodel), [`mtp_layers`](mtp.md#MTPDecoder.mtp_layers), [`Config`](model.md#DeepSeekV3Model.Config), [`set_deepseek_v3_sharding_config`](sharding.md#set_deepseek_v3_sharding_config), [`get_deepseek_v3_nparams_and_flops`](model.md#get_deepseek_v3_nparams_and_flops), [`update_from_config`](model.md#DeepSeekV3Model.Config.update_from_config), [`__init__`](mtp.md#MTPDecoder.__init__)

### <a id="MTPLoss"></a>`MTPLoss`  ·  implements/extends CrossEntropyLoss
- def: [`torchtitan/models/deepseek_v3/mtp.py:425`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L425)
- doc: DeepSeek-V3 weighted multi-term cross-entropy objective.
- signature: `class MTPLoss(CrossEntropyLoss):`
- members:
  - <a id="MTPLoss.__call__"></a>`__call__(self, pred: torch.Tensor | tuple[torch.Tensor, ...], labels: torch.Tensor | tuple[torch.Tensor, ...], global_valid_tokens: torch.Tensor | None = None, **loss_inputs: Any)` — [`L436`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L436) — Compute the weighted objective from aligned prediction/label pairs.
  - <a id="MTPLoss.mtp_scale"></a>`mtp_scale` — [`L434`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L434)
- protocol/private: <a id="MTPLoss.__init__"></a>`__init__`[`L432`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L432)
- uses (calls/refs, reference-scoped): [`CompileConfig`](../../config/configs.md#CompileConfig), [`CrossEntropyLoss`](../../components/loss.md#CrossEntropyLoss), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`current_spmd_mesh`](../../distributed/spmd_types.md#current_spmd_mesh), [`__call__`](../../components/loss.md#CrossEntropyLoss.__call__), [`Config`](mtp.md#MTPLoss.Config), [`__init__`](../../components/loss.md#CrossEntropyLoss.__init__), [`mtp_scale`](mtp.md#MTPLoss.Config.mtp_scale)
- used by: [`deepseek_v4_mtp_debugmodel`](../deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`CrossEntropyLoss`](../../components/loss.md#CrossEntropyLoss), [`deepseek_v3_debugmodel_mtp`](config_registry.md#deepseek_v3_debugmodel_mtp)

### <a id="MTPLoss.Config"></a>`MTPLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v3/mtp.py:429`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L429)
- signature: `class Config(CrossEntropyLoss.Config):`
- members:
  - <a id="MTPLoss.Config.mtp_scale"></a>`mtp_scale` — [`L430`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L430)
- uses (calls/refs, reference-scoped): [`CrossEntropyLoss`](../../components/loss.md#CrossEntropyLoss), [`Config`](../../components/loss.md#CrossEntropyLoss.Config)
- used by: [`deepseek_v4_mtp_debugmodel`](../deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`deepseek_v3_debugmodel_mtp`](config_registry.md#deepseek_v3_debugmodel_mtp), [`__init__`](mtp.md#MTPLoss.__init__), [`mtp_scale`](mtp.md#MTPLoss.mtp_scale)

### <a id="MTPTransformerBlock"></a>`MTPTransformerBlock`  ·  implements/extends TransformerBlock
- def: [`torchtitan/models/deepseek_v3/mtp.py:112`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L112)
- doc: Generic MTP block for decoder-only transformer models.
- signature: `class MTPTransformerBlock(TransformerBlock):`
- members:
  - <a id="MTPTransformerBlock.forward"></a>`forward(self, mtp_input_embed: torch.Tensor, prev_embed: torch.Tensor, mtp_input_valid_mask: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None)` — [`L147`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L147) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="MTPTransformerBlock.attention"></a>`attention` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L131)
  - <a id="MTPTransformerBlock.attention_norm"></a>`attention_norm` — [`L132`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L132)
  - <a id="MTPTransformerBlock.eh_proj"></a>`eh_proj` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L136)
  - <a id="MTPTransformerBlock.enorm"></a>`enorm` — [`L134`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L134)
  - <a id="MTPTransformerBlock.feed_forward"></a>`feed_forward` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L145)
  - <a id="MTPTransformerBlock.ffn_norm"></a>`ffn_norm` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L133)
  - <a id="MTPTransformerBlock.hnorm"></a>`hnorm` — [`L135`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L135)
  - <a id="MTPTransformerBlock.moe"></a>`moe` — [`L142`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L142)
  - <a id="MTPTransformerBlock.moe_enabled"></a>`moe_enabled` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L139)
  - <a id="MTPTransformerBlock.mtp_norm"></a>`mtp_norm` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L137)
- protocol/private: <a id="MTPTransformerBlock.__init__"></a>`__init__`[`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L129)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`feed_forward`](../common/decoder.md#TransformerBlock.Config.feed_forward), [`attention`](../common/decoder.md#TransformerBlock.Config.attention), [`attention_norm`](../common/decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](../common/decoder.md#TransformerBlock.Config.ffn_norm), [`moe`](../common/decoder.md#TransformerBlock.Config.moe), [`Config`](mtp.md#MTPTransformerBlock.Config), [`eh_proj`](mtp.md#MTPTransformerBlock.Config.eh_proj), [`enorm`](mtp.md#MTPTransformerBlock.Config.enorm), [`hnorm`](mtp.md#MTPTransformerBlock.Config.hnorm), [`mtp_norm`](mtp.md#MTPTransformerBlock.Config.mtp_norm)
- used by: [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`mtp_layers`](mtp.md#MTPDecoder.mtp_layers)

### <a id="MTPTransformerBlock.Config"></a>`MTPTransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v3/mtp.py:123`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L123)
- signature: `class Config(TransformerBlock.Config):`
- members:
  - <a id="MTPTransformerBlock.Config.eh_proj"></a>`eh_proj` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L126)
  - <a id="MTPTransformerBlock.Config.enorm"></a>`enorm` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L124)
  - <a id="MTPTransformerBlock.Config.hnorm"></a>`hnorm` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L125)
  - <a id="MTPTransformerBlock.Config.mtp_norm"></a>`mtp_norm` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L127)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`Config`](../common/decoder.md#TransformerBlock.Config)
- used by: [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`mtp_layers`](mtp.md#MTPDecoder.mtp_layers), [`eh_proj`](mtp.md#MTPTransformerBlock.eh_proj), [`enorm`](mtp.md#MTPTransformerBlock.enorm), [`hnorm`](mtp.md#MTPTransformerBlock.hnorm), [`mtp_norm`](mtp.md#MTPTransformerBlock.mtp_norm), [`__init__`](mtp.md#MTPTransformerBlock.__init__)

## Functions
- <a id="apply_fsdp_to_mtp_decoder"></a>`apply_fsdp_to_mtp_decoder(model: MTPDecoder, dp_mesh: DeviceMesh, param_dtype: torch.dtype, reduce_dtype: torch.dtype, pp_enabled: bool, cpu_offload: bool = False, reshard_after_forward_policy: str = "default", ep_degree: int = 1, edp_mesh: DeviceMesh | None = None, dp_mesh_dims: DataParallelMeshDims | None = None, edp_mesh_dims: DataParallelMeshDims | None = None, enable_symm_mem: bool = False)` — [`L383`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L383)
- <a id="roll_mtp_sequence"></a>`roll_mtp_sequence(sequence: torch.Tensor, *, shift: int, fill_value: int, positions: torch.Tensor | None = None, return_valid_mask: bool = False)` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/mtp.py#L38) — Left-roll an MTP sequence while preserving packed-document boundaries.

