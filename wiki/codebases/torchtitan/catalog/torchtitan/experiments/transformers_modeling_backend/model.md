---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.model`/
symbols:
  HFTransformerModel.model: HFTransformerModel#model.
  HFTransformerModel: HFTransformerModel#
  HFTransformerModel.preprocess_inputs: HFTransformerModel#preprocess_inputs().
  HFTransformerModel.get_attention_masks: HFTransformerModel#get_attention_masks().
  HFTransformerModel.Config: HFTransformerModel#Config#
  HFTransformerModel.init_states: HFTransformerModel#init_states().
  HFTransformerModel.layers: HFTransformerModel#layers().
  HFTransformerModel.cp_mesh: HFTransformerModel#cp_mesh.
  HFTransformerModel.Config.get_nparams_and_flops: HFTransformerModel#Config#get_nparams_and_flops().
  HFTransformerModel.named_children: HFTransformerModel#named_children().
  Config._tt_to_hf_attribute_map: Config#_tt_to_hf_attribute_map.
  HFTransformerModel.__init__: HFTransformerModel#__init__().
  Config._titan_injected_model_args: Config#_titan_injected_model_args.
  Config.is_moe: Config#is_moe.
  HFTransformerModel.Config.update_from_config: HFTransformerModel#Config#update_from_config().
  HFTransformerModel.Config.__init__: HFTransformerModel#Config#__init__().
  HFTransformerModel.tok_embeddings: HFTransformerModel#tok_embeddings().
  HFTransformerModel.forward: HFTransformerModel#forward().
  Config.head_dim: Config#head_dim.
  HFTransformerModel.lm_head: HFTransformerModel#lm_head().
  HFTransformerModel.Config._configure_hf_attention: HFTransformerModel#Config#_configure_hf_attention().
  HFTransformerModel._patch_hf_llama_like: HFTransformerModel#_patch_hf_llama_like().
  HFTransformerModel.norm: HFTransformerModel#norm().
  HFTransformerModel.rotary_emb: HFTransformerModel#rotary_emb().
  SliceableModuleDict: SliceableModuleDict#
  HFTransformerModel.Config.build: HFTransformerModel#Config#build().
  HFFlexKernel.Config: HFFlexKernel#Config#
  _ATTN_IMPLEMENTATION: _ATTN_IMPLEMENTATION.
  HFTransformerModel.Config._initialize_attributes: HFTransformerModel#Config#_initialize_attributes().
  HFTransformerModel.Config._create_property: HFTransformerModel#Config#_create_property().
  HFTransformerModel._build_dense_attention_mask: HFTransformerModel#_build_dense_attention_mask().
  HFFlexKernel: HFFlexKernel#
  HFFlexKernel.__init__: HFFlexKernel#__init__().
  Config.attn_implementation: Config#attn_implementation.
  _flex_attention_torchtitan: _flex_attention_torchtitan().
  Config.topk_group: Config#topk_group.
  HFTransformerModel._build_hf_model: HFTransformerModel#_build_hf_model().
  HFTransformerModel._maybe_dump_logits: HFTransformerModel#_maybe_dump_logits().
  HFTransformerModel.selective_init: HFTransformerModel#selective_init().
  _REMOTE_CONFIG_DENYLIST: _REMOTE_CONFIG_DENYLIST.
  SliceableModuleDict.__getitem__: SliceableModuleDict#__getitem__().
  HFTransformerModel.Config.__repr__: HFTransformerModel#Config#__repr__().
  Config.initializer_range: Config#initializer_range.
  HFTransformerModel.max_seq_len: HFTransformerModel#max_seq_len.
  HFTransformerModel.set_cp_mesh: HFTransformerModel#set_cp_mesh().
  _TT_TO_HF_MAPPINGS: _TT_TO_HF_MAPPINGS.
  _get_moe_attr_name: _get_moe_attr_name().
  HFTransformerModel._skip_lm_head: HFTransformerModel#_skip_lm_head.
  HFTransformerModel.Config.architectures: HFTransformerModel#Config#architectures.
  HFTransformerModel.Config._replace: HFTransformerModel#Config#_replace().
  _uses_dsa: _uses_dsa().
  HFTransformerModel.Config._create_getter_setter_dynamically: HFTransformerModel#Config#_create_getter_setter_dynamically().
  HFTransformerModel.Config.getter: HFTransformerModel#Config#getter().
  HFTransformerModel.Config.setter: HFTransformerModel#Config#setter().
  Config.n_routed_experts: Config#n_routed_experts.
  Config.max_seq_len: Config#max_seq_len.
  HFTransformerModel._decoder_layer_init_patched: HFTransformerModel#_decoder_layer_init_patched().
  HFTransformerModel._initialize_weights_patched: HFTransformerModel#_initialize_weights_patched().
  HFTransformerModel._init_weights_patched: HFTransformerModel#_init_weights_patched().
  HFTransformerModel.copy_into_dtensor: HFTransformerModel#copy_into_dtensor().
  HFFlexKernel.forward: HFFlexKernel#forward().
  SliceableModuleDict.__iter__: SliceableModuleDict#__iter__().
  SliceableModuleDict.__len__: SliceableModuleDict#__len__().
  SliceableModuleDict.init_states: SliceableModuleDict#init_states().
  _TT_SPECIFIC_ATTRIBUTES: _TT_SPECIFIC_ATTRIBUTES.
  HFTransformerModel.Config.transformers_version: HFTransformerModel#Config#transformers_version.
  HFTransformerModel.Config.output_hidden_states: HFTransformerModel#Config#output_hidden_states.
  HFTransformerModel.Config.return_dict: HFTransformerModel#Config#return_dict.
  HFTransformerModel.Config.dtype: HFTransformerModel#Config#dtype.
  HFTransformerModel.Config.chunk_size_feed_forward: HFTransformerModel#Config#chunk_size_feed_forward.
  HFTransformerModel.Config.is_encoder_decoder: HFTransformerModel#Config#is_encoder_decoder.
  HFTransformerModel.Config.id2label: HFTransformerModel#Config#id2label.
  HFTransformerModel.Config.label2id: HFTransformerModel#Config#label2id.
  HFTransformerModel.Config.problem_type: HFTransformerModel#Config#problem_type.
  Config.allow_global_per_layer_attribute_access: Config#allow_global_per_layer_attribute_access.
  Config.layer_types: Config#layer_types.
  Config.per_layer_config: Config#per_layer_config.
  Config.deterministic: Config#deterministic.
  Config.attention_bias: Config#attention_bias.
  Config.mlp_bias: Config#mlp_bias.
  Config.use_cache: Config#use_cache.
  Config.intermediate_size: Config#intermediate_size.
  Config.num_key_value_heads: Config#num_key_value_heads.
  HFTransformerModel._logit_dump_recs: HFTransformerModel#_logit_dump_recs.
  HFTransformerModel.verify_module_protocol: HFTransformerModel#verify_module_protocol().
  HFTransformerModel.__setattr__: HFTransformerModel#__setattr__().
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py)

## Classes
### <a id="HFFlexKernel"></a>`HFFlexKernel`  ·  implements/extends Module
- def: [`torchtitan/experiments/transformers_modeling_backend/model.py:40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L40)
- doc: Flex-attention kernel wrapped as a titan Module for declarative TP.
- signature: `class HFFlexKernel(Module):`
- members:
  - <a id="HFFlexKernel.forward"></a>`forward(self, query, key, value, *, module, block_mask=None, **kwargs)` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L65)
- protocol/private: <a id="HFFlexKernel.__init__"></a>`__init__`[`L62`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L62)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](model.md#HFFlexKernel.Config)
- used by: [`Module`](../../protocols/module.md#Module), [`_attach_flex_kernel`](hf_sharding.md#_attach_flex_kernel)

### <a id="HFFlexKernel.Config"></a>`HFFlexKernel.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/transformers_modeling_backend/model.py:59`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L59)
- signature: `class Config(Module.Config):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_attach_flex_kernel`](hf_sharding.md#_attach_flex_kernel), [`__init__`](model.md#HFFlexKernel.__init__)

### <a id="HFTransformerModel"></a>`HFTransformerModel`  ·  implements/extends BaseModel
- def: [`torchtitan/experiments/transformers_modeling_backend/model.py:197`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L197)
- signature: `class HFTransformerModel(BaseModel):`
- members:
  - <a id="HFTransformerModel._build_dense_attention_mask"></a>`_build_dense_attention_mask(self, positions: torch.Tensor)` — [`L1309`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1309) — Dense 4D additive attention mask for DSA models under flex.
  - <a id="HFTransformerModel._build_hf_model"></a>`_build_hf_model(self, model_cls, config)` — [`L855`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L855) — Construct the wrapped HF model; a subclass may prepare or retry.
  - <a id="HFTransformerModel._init_weights_patched"></a>`_init_weights_patched(self, module)` — [`L947`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L947) — Patched version of _init_weights to match TorchTitan's initialization for Llama-like models.
  - <a id="HFTransformerModel._maybe_dump_logits"></a>`_maybe_dump_logits(self, dump_dir: str, logits: torch.Tensor)` — [`L1378`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1378) — Append this rank's logits (one entry per forward) for numerical tests.
  - <a id="HFTransformerModel._patch_hf_llama_like"></a>`_patch_hf_llama_like(self, decoder_layer_cls, attention_cls, mlp_cls=None, experts_cls=None, router_cls=None)` — [`L862`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L862) — This patch modifies a Hugging Face Llama-like model's weight initialization to match
  - <a id="HFTransformerModel.copy_into_dtensor"></a>`copy_into_dtensor(tensor, other)` — [`L1426`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1426)
  - <a id="HFTransformerModel.forward"></a>`forward(self, *args, **kwargs)` — [`L1334`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1334)
  - <a id="HFTransformerModel.get_attention_masks"></a>`get_attention_masks(self, positions: torch.Tensor)` — [`L1272`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1272) — Build a flex BlockMask (causal or document-causal).
  - <a id="HFTransformerModel.init_states"></a>`init_states(self, *, buffer_device: torch.device | None = None)` — [`L1397`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1397)
  - <a id="HFTransformerModel.layers"></a>`layers(self)` — [`L1126`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1126) — Returns the model's layers, handling different Hugging Face model structures.
  - <a id="HFTransformerModel.lm_head"></a>`lm_head(self)` — [`L1181`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1181) — Returns the model's output layer, handling different Hugging Face model structures.
  - <a id="HFTransformerModel.named_children"></a>`named_children(self)` — [`L1463`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1463) — Provides a flattened view of the model's main components,
  - <a id="HFTransformerModel.norm"></a>`norm(self)` — [`L1150`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1150) — Returns the model's norm, handling different Hugging Face model structures.
  - <a id="HFTransformerModel.preprocess_inputs"></a>`preprocess_inputs(self, input_dict: dict[str, torch.Tensor], *, parallel_dims: ParallelDims, parallelism: ParallelismConfig, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L1222`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1222) — Build the attention mask (when positions are present), CP-shard, return.
  - <a id="HFTransformerModel.rotary_emb"></a>`rotary_emb(self)` — [`L1200`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1200) — Returns the model's rotary_emb, handling different Hugging Face model structures.
  - <a id="HFTransformerModel.selective_init"></a>`selective_init(module)` — [`L1411`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1411)
  - <a id="HFTransformerModel.set_cp_mesh"></a>`set_cp_mesh(self, mesh)` — [`L859`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L859)
  - <a id="HFTransformerModel.tok_embeddings"></a>`tok_embeddings(self)` — [`L1103`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1103) — Returns the model's embed_tokens, handling different Hugging Face model structures.
  - <a id="HFTransformerModel.verify_module_protocol"></a>`verify_module_protocol(self)` — [`L1388`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1388) — Skip recursive verification for HuggingFace model internals.
  - <a id="HFTransformerModel.cp_mesh"></a>`cp_mesh` — [`L815`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L815)
  - <a id="HFTransformerModel.max_seq_len"></a>`max_seq_len` — [`L814`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L814)
  - <a id="HFTransformerModel.model"></a>`model` — [`L813`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L813)
- protocol/private: <a id="HFTransformerModel.__init__"></a>`__init__`[`L692`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L692), <a id="HFTransformerModel.__setattr__"></a>`__setattr__`[`L1474`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1474), <a id="HFTransformerModel._decoder_layer_init_patched"></a>`_decoder_layer_init_patched`[`L887`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L887), <a id="HFTransformerModel._initialize_weights_patched"></a>`_initialize_weights_patched`[`L908`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L908), <a id="HFTransformerModel._logit_dump_recs"></a>`_logit_dump_recs`[`L1384`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L1384), <a id="HFTransformerModel._skip_lm_head"></a>`_skip_lm_head`[`L199`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L199)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`ParallelismConfig`](../../config/configs.md#ParallelismConfig), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`spmd_backend`](../../config/configs.md#ParallelismConfig.spmd_backend), [`BaseModel`](../../protocols/model.md#BaseModel), [`get_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_mesh), [`get_causal_mask_mod`](../../models/common/attention.md#get_causal_mask_mod), [`TPUHFTransformerModel`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel), [`cp_enabled`](../../distributed/parallel_dims.md#ParallelDims.cp_enabled), [`create_attention_mask`](../../models/common/attention.md#create_attention_mask), [`decoder_input_sharding`](../../models/common/decoder_sharding.md#decoder_input_sharding), [`annotate_input_spmd_types`](../../distributed/spmd_types.md#annotate_input_spmd_types), [`forward`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.forward), [`prepare_context_parallel_input`](../../distributed/context_parallel/api.md#prepare_context_parallel_input), [`is_in_batch_invariant_mode`](../../distributed/utils.md#is_in_batch_invariant_mode), [`context_parallel_load_balancer`](../../config/configs.md#ParallelismConfig.context_parallel_load_balancer), [`Config`](model.md#HFTransformerModel.Config), [`init_states`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.init_states), [`prepare_native_moe_configs`](moe_replacement.md#prepare_native_moe_configs), [`lm_head`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.lm_head), [`get_document_mask_mod`](../../models/common/attention.md#get_document_mask_mod), [`is_moe`](model.md#Config.is_moe), [`norm`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.norm), [`tok_embeddings`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.tok_embeddings), [`SliceableModuleDict`](model.md#SliceableModuleDict), [`get_attention_masks`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.get_attention_masks), [`layers`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.layers), [`rotary_emb`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.rotary_emb), [`context_parallel_ptrr_mask_key`](../../config/configs.md#ParallelismConfig.context_parallel_ptrr_mask_key), [`named_children`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.named_children), [`_get_moe_attr_name`](model.md#_get_moe_attr_name), [`architectures`](model.md#HFTransformerModel.Config.architectures), [`_uses_dsa`](model.md#_uses_dsa), [`max_seq_len`](model.md#Config.max_seq_len), [`_build_hf_model`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._build_hf_model)
- used by: [`BaseModel`](../../protocols/model.md#BaseModel), [`flavors`](__init__.md#flavors), [`TPUHFTransformerModel`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel), [`init_states`](../../protocols/module.md#Module.init_states), [`_TPU_FLAVORS`](../tpu/transformers_modeling_backend/config_registry.md#_TPU_FLAVORS), [`forward`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.forward), [`head_dim`](../tpu/transformers_modeling_backend/model.md#Config.head_dim), [`_added_lm_head`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._added_lm_head), [`preprocess_inputs`](../../protocols/model.md#BaseModel.preprocess_inputs), [`init_states`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.init_states), [`get_nparams_and_flops`](model.md#HFTransformerModel.Config.get_nparams_and_flops), [`_added_norm`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._added_norm), [`as_tpu_model_config`](../tpu/transformers_modeling_backend/model.md#as_tpu_model_config), [`_fused_loss_blocker`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._fused_loss_blocker), [`_init_swapped_native_modules`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._init_swapped_native_modules), [`_assign`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._assign), [`_forward_kwargs`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._forward_kwargs), [`Config`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.Config), [`__init__`](state_dict_adapter.md#HFTransformerStateDictAdapter.__init__), [`_part`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._part), [`get_attention_masks`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.get_attention_masks), [`verify_module_protocol`](../../protocols/model.md#BaseModel.verify_module_protocol), [`_check_position_capacity`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._check_position_capacity), [`_init_untouched_parameters`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._init_untouched_parameters), [`_position_capacity`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._position_capacity), [`_reassert_device`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._reassert_device), [`__init__`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.__init__), [`_mirrored_logit_transform`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._mirrored_logit_transform), [`named_children`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.named_children), [`_reinit_buffer_device`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel._reinit_buffer_device)  (6 test-only)

### <a id="HFTransformerModel.Config"></a>`HFTransformerModel.Config`  ·  implements/extends Config, PreTrainedConfig
- def: [`torchtitan/experiments/transformers_modeling_backend/model.py:202`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L202)
- doc: Configuration that bridges TorchTitan and HuggingFace Transformers.
- signature: `class Config(BaseModel.Config, PretrainedConfig):`
- members:
  - <a id="HFTransformerModel.Config._configure_hf_attention"></a>`_configure_hf_attention(self)` — [`L337`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L337) — Configure HuggingFace attention to route through flex attention.
  - <a id="HFTransformerModel.Config._create_getter_setter_dynamically"></a>`_create_getter_setter_dynamically(self, is_moe: bool)` — [`L363`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L363) — Create properties dynamically based on tt and hf attribute mappings.
  - <a id="HFTransformerModel.Config._initialize_attributes"></a>`_initialize_attributes(self, model_config)` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L293) — Initialize all model attributes from the config.
  - <a id="HFTransformerModel.Config._replace"></a>`_replace(self, **overrides)` — [`L270`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L270) — Override to use ``copy.copy()`` instead of ``dataclasses.replace()``.
  - <a id="HFTransformerModel.Config.build"></a>`build(self, **kwargs)` — [`L258`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L258) — Override build() to use _replace() instead of dataclasses.replace().
  - <a id="HFTransformerModel.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L558`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L558)
  - <a id="HFTransformerModel.Config.getter"></a>`getter(self)` — [`L370`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L370)
  - <a id="HFTransformerModel.Config.setter"></a>`setter(self, value)` — [`L373`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L373)
  - <a id="HFTransformerModel.Config.update_from_config"></a>`update_from_config(self, *, config=None, **kwargs)` — [`L404`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L404)
  - <a id="HFTransformerModel.Config.architectures"></a>`architectures` — [`L214`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L214)
  - <a id="HFTransformerModel.Config.chunk_size_feed_forward"></a>`chunk_size_feed_forward` — [`L218`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L218)
  - <a id="HFTransformerModel.Config.dtype"></a>`dtype` — [`L217`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L217)
  - <a id="HFTransformerModel.Config.id2label"></a>`id2label` — [`L220`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L220)
  - <a id="HFTransformerModel.Config.is_encoder_decoder"></a>`is_encoder_decoder` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L219)
  - <a id="HFTransformerModel.Config.label2id"></a>`label2id` — [`L221`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L221)
  - <a id="HFTransformerModel.Config.output_hidden_states"></a>`output_hidden_states` — [`L215`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L215)
  - <a id="HFTransformerModel.Config.problem_type"></a>`problem_type` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L222)
  - <a id="HFTransformerModel.Config.return_dict"></a>`return_dict` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L216)
  - <a id="HFTransformerModel.Config.transformers_version"></a>`transformers_version` — [`L213`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L213)
- protocol/private: <a id="HFTransformerModel.Config.__init__"></a>`__init__`[`L224`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L224), <a id="HFTransformerModel.Config.__repr__"></a>`__repr__`[`L395`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L395), <a id="HFTransformerModel.Config._create_property"></a>`_create_property`[`L369`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L369)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`param_init`](../../protocols/module.md#Module.Config.param_init), [`sharding_config`](../../protocols/module.md#Module.Config.sharding_config), [`BaseModel`](../../protocols/model.md#BaseModel), [`HFTransformerModel`](model.md#HFTransformerModel), [`Config`](../../protocols/model.md#BaseModel.Config), [`quadratic_attention_flops_per_token`](../../models/utils.md#quadratic_attention_flops_per_token), [`layers`](model.md#HFTransformerModel.layers), [`_owner`](../../config/configurable.md#Configurable.Config._owner), [`_tt_to_hf_attribute_map`](model.md#Config._tt_to_hf_attribute_map), [`_titan_injected_model_args`](model.md#Config._titan_injected_model_args), [`head_dim`](model.md#Config.head_dim), [`TitanMoeModelConfig`](__init__.md#TitanMoeModelConfig), [`_ATTN_IMPLEMENTATION`](model.md#_ATTN_IMPLEMENTATION), [`attn_implementation`](model.md#Config.attn_implementation), [`_flex_attention_torchtitan`](model.md#_flex_attention_torchtitan), [`_REMOTE_CONFIG_DENYLIST`](model.md#_REMOTE_CONFIG_DENYLIST), [`_get_moe_attr_name`](model.md#_get_moe_attr_name)
- used by: [`flavors`](__init__.md#flavors), [`_TPU_FLAVORS`](../tpu/transformers_modeling_backend/config_registry.md#_TPU_FLAVORS), [`head_dim`](../tpu/transformers_modeling_backend/model.md#Config.head_dim), [`_tt_to_hf_attribute_map`](model.md#Config._tt_to_hf_attribute_map), [`as_tpu_model_config`](../tpu/transformers_modeling_backend/model.md#as_tpu_model_config), [`__init__`](model.md#HFTransformerModel.__init__), [`_titan_injected_model_args`](model.md#Config._titan_injected_model_args), [`is_moe`](model.md#Config.is_moe), [`build`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.Config.build), [`_complete_from_hf_config`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.Config._complete_from_hf_config), [`Config`](../tpu/transformers_modeling_backend/model.md#TPUHFTransformerModel.Config), [`__init__`](state_dict_adapter.md#HFTransformerStateDictAdapter.__init__)  (1 test-only)

### <a id="SliceableModuleDict"></a>`SliceableModuleDict`  ·  implements/extends ModuleDict
- def: [`torchtitan/experiments/transformers_modeling_backend/model.py:92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L92)
- doc: A ModuleDict that supports slicing like ModuleList.
- signature: `class SliceableModuleDict(ModuleDict):`
- members:
  - <a id="SliceableModuleDict.init_states"></a>`init_states(self, **_kwargs)` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L120) — No-op: HFTransformerModel handles initialization via HF mechanisms.
- protocol/private: <a id="SliceableModuleDict.__getitem__"></a>`__getitem__`[`L98`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L98), <a id="SliceableModuleDict.__iter__"></a>`__iter__`[`L109`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L109), <a id="SliceableModuleDict.__len__"></a>`__len__`[`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L117)
- uses (calls/refs, reference-scoped): [`ModuleDict`](../../protocols/module.md#ModuleDict)
- used by: [`ModuleDict`](../../protocols/module.md#ModuleDict), [`cp_mesh`](model.md#HFTransformerModel.cp_mesh)  (1 test-only)

## Functions
- <a id="_flex_attention_torchtitan"></a>`_flex_attention_torchtitan(module, query, key, value, attention_mask, **kwargs)` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L73) — HF ``AttentionInterface`` shim for flex attention.
- <a id="_get_moe_attr_name"></a>`_get_moe_attr_name(layer: nn.Module)` — [`L158`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L158) — Return the attribute name holding the MoE block on a decoder layer.
- <a id="_uses_dsa"></a>`_uses_dsa(config)` — [`L180`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L180) — True if the model uses DeepSeek-style sparse attention (DSA).

## Module values
- <a id="_ATTN_IMPLEMENTATION"></a>`_ATTN_IMPLEMENTATION` — [`L177`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L177)
- <a id="_REMOTE_CONFIG_DENYLIST"></a>`_REMOTE_CONFIG_DENYLIST` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L155)
- <a id="_TT_SPECIFIC_ATTRIBUTES"></a>`_TT_SPECIFIC_ATTRIBUTES` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L143)
- <a id="_TT_TO_HF_MAPPINGS"></a>`_TT_TO_HF_MAPPINGS` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L126)

## Other members
- <a id="Config._titan_injected_model_args"></a>`Config._titan_injected_model_args` — [`L253`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L253)
- <a id="Config._tt_to_hf_attribute_map"></a>`Config._tt_to_hf_attribute_map` — [`L379`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L379)
- <a id="Config.allow_global_per_layer_attribute_access"></a>`Config.allow_global_per_layer_attribute_access` — [`L485`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L485)
- <a id="Config.attention_bias"></a>`Config.attention_bias` — [`L505`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L505)
- <a id="Config.attn_implementation"></a>`Config.attn_implementation` — [`L355`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L355)
- <a id="Config.deterministic"></a>`Config.deterministic` — [`L501`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L501)
- <a id="Config.head_dim"></a>`Config.head_dim` — [`L539`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L539)
- <a id="Config.initializer_range"></a>`Config.initializer_range` — [`L508`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L508)
- <a id="Config.intermediate_size"></a>`Config.intermediate_size` — [`L525`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L525)
- <a id="Config.is_moe"></a>`Config.is_moe` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L248)
- <a id="Config.layer_types"></a>`Config.layer_types` — [`L490`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L490)
- <a id="Config.max_seq_len"></a>`Config.max_seq_len` — [`L496`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L496)
- <a id="Config.mlp_bias"></a>`Config.mlp_bias` — [`L506`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L506)
- <a id="Config.n_routed_experts"></a>`Config.n_routed_experts` — [`L479`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L479)
- <a id="Config.num_key_value_heads"></a>`Config.num_key_value_heads` — [`L535`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L535)
- <a id="Config.per_layer_config"></a>`Config.per_layer_config` — [`L491`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L491)
- <a id="Config.topk_group"></a>`Config.topk_group` — [`L554`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L554)
- <a id="Config.use_cache"></a>`Config.use_cache` — [`L507`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/model.py#L507)

