---
title: 'Module: torchtitan/experiments/tpu/transformers_modeling_backend/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/transformers_modeling_backend/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.transformers_modeling_backend.model`/
symbols:
  TPUHFTransformerModel: TPUHFTransformerModel#
  substitute_tpu_experts: substitute_tpu_experts().
  Config.head_dim: Config#head_dim.
  TPUHFTransformerModel.forward: TPUHFTransformerModel#forward().
  TPUHFTransformerModel._added_lm_head: TPUHFTransformerModel#_added_lm_head.
  TPUHFTransformerModel.init_states: TPUHFTransformerModel#init_states().
  TPUHFTransformerModel._added_norm: TPUHFTransformerModel#_added_norm.
  as_tpu_model_config: as_tpu_model_config().
  TPUHFTransformerModel.lm_head: TPUHFTransformerModel#lm_head().
  TPUHFTransformerModel.Config._mirror_logit_transform_into_fused_loss: TPUHFTransformerModel#Config#_mirror_logit_transform_into_fused_loss().
  TPUHFTransformerModel._fused_loss_blocker: TPUHFTransformerModel#_fused_loss_blocker().
  TPUHFTransformerModel._init_swapped_native_modules: TPUHFTransformerModel#_init_swapped_native_modules().
  TPUHFTransformerModel.Config.build: TPUHFTransformerModel#Config#build().
  TPUHFTransformerModel._assign: TPUHFTransformerModel#_assign().
  TPUHFTransformerModel._context_length: TPUHFTransformerModel#_context_length.
  TPUHFTransformerModel.norm: TPUHFTransformerModel#norm().
  TPUHFTransformerModel._forward_kwargs: TPUHFTransformerModel#_forward_kwargs.
  TPUHFTransformerModel.Config._complete_from_hf_config: TPUHFTransformerModel#Config#_complete_from_hf_config().
  TPUHFTransformerModel.Config: TPUHFTransformerModel#Config#
  TPUHFTransformerModel.tok_embeddings: TPUHFTransformerModel#tok_embeddings().
  TPUHFTransformerModel._part: TPUHFTransformerModel#_part().
  TPUHFTransformerModel.get_attention_masks: TPUHFTransformerModel#get_attention_masks().
  TPUHFTransformerModel.layers: TPUHFTransformerModel#layers().
  TPUHFTransformerModel.rotary_emb: TPUHFTransformerModel#rotary_emb().
  TPUHFTransformerModel._check_position_capacity: TPUHFTransformerModel#_check_position_capacity().
  _use_pallas_grouped_mm: _use_pallas_grouped_mm().
  TPUHFTransformerModel._position_capacity: TPUHFTransformerModel#_position_capacity.
  TPUHFTransformerModel._build_with_supported_attention: TPUHFTransformerModel#_build_with_supported_attention().
  TPUHFTransformerModel._init_untouched_parameters: TPUHFTransformerModel#_init_untouched_parameters().
  TPUHFTransformerModel._reassert_device: TPUHFTransformerModel#_reassert_device().
  _Attrs.__getattr__: _Attrs#__getattr__().
  Config.initializer_range: Config#initializer_range.
  TPUHFTransformerModel.__init__: TPUHFTransformerModel#__init__().
  TPUHFTransformerModel._fused_loss: TPUHFTransformerModel#_fused_loss.
  TPUHFTransformerModel._mirrored_logit_transform: TPUHFTransformerModel#_mirrored_logit_transform.
  TPUHFTransformerModel.named_children: TPUHFTransformerModel#named_children().
  TPUHFTransformerModel._reinit_buffer_device: TPUHFTransformerModel#_reinit_buffer_device().
  Config.fused_loss_logit_transform: Config#fused_loss_logit_transform.
  TPUHFTransformerModel.to_empty: TPUHFTransformerModel#to_empty().
  _Attrs: _Attrs#
  TPUHFTransformerModel._set_attn_everywhere: TPUHFTransformerModel#_set_attn_everywhere().
  _Attrs._d: _Attrs#_d.
  _parse_config_overrides: _parse_config_overrides().
  TPUHFTransformerModel.Config._TEXT_TOWERS: TPUHFTransformerModel#Config#_TEXT_TOWERS.
  TPUHFTransformerModel._LOGIT_TRANSFORMS: TPUHFTransformerModel#_LOGIT_TRANSFORMS.
  _Attrs.__init__: _Attrs#__init__().
  TPUHFTransformerModel.Config.update_from_config: TPUHFTransformerModel#Config#update_from_config().
  TPUHFTransformerModel._build_hf_model: TPUHFTransformerModel#_build_hf_model().
---
# Module: [`torchtitan/experiments/tpu/transformers_modeling_backend/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py)

## Classes
### <a id="TPUHFTransformerModel"></a>`TPUHFTransformerModel`  ·  implements/extends HFTransformerModel
- def: [`torchtitan/experiments/tpu/transformers_modeling_backend/model.py:87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L87)
- doc: HFTransformerModel generalized past the Llama nesting, for the TPU lane.
- signature: `class TPUHFTransformerModel(HFTransformerModel):`
- members:
  - <a id="TPUHFTransformerModel._build_with_supported_attention"></a>`_build_with_supported_attention(cls, model_cls, config)` — [`L499`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L499) — Build the model, backing off to an attention path it accepts.
  - <a id="TPUHFTransformerModel._check_position_capacity"></a>`_check_position_capacity(self, seq_len: int)` — [`L662`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L662) — Refuse a sequence the learned position table cannot address.
  - <a id="TPUHFTransformerModel._fused_loss_blocker"></a>`_fused_loss_blocker(self)` — [`L413`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L413) — Why the fused CE cannot stand in for this model's head, or None.
  - <a id="TPUHFTransformerModel._init_swapped_native_modules"></a>`_init_swapped_native_modules(self)` — [`L861`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L861) — Re-initialize Titan modules swapped into the HF tree after to_empty().
  - <a id="TPUHFTransformerModel._init_untouched_parameters"></a>`_init_untouched_parameters(self)` — [`L834`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L834) — Initialize parameters the model's own init never wrote (still NaN).
  - <a id="TPUHFTransformerModel._reassert_device"></a>`_reassert_device(self)` — [`L901`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L901) — Pull back anything init left on the wrong device.
  - <a id="TPUHFTransformerModel._set_attn_everywhere"></a>`_set_attn_everywhere(config, attn: str)` — [`L482`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L482) — Set the attention implementation on a config and its sub-configs.
  - <a id="TPUHFTransformerModel.forward"></a>`forward(self, *args, **kwargs)` — [`L679`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L679)
  - <a id="TPUHFTransformerModel.get_attention_masks"></a>`get_attention_masks(self, positions: torch.Tensor)` — [`L652`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L652)
  - <a id="TPUHFTransformerModel.init_states"></a>`init_states(self, *, buffer_device: torch.device | None = None)` — [`L793`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L793)
  - <a id="TPUHFTransformerModel.layers"></a>`layers(self)` — [`L566`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L566) — The decoder/encoder block stack.
  - <a id="TPUHFTransformerModel.lm_head"></a>`lm_head(self)` — [`L586`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L586) — The output projection, native to the architecture or attached for it.
  - <a id="TPUHFTransformerModel.named_children"></a>`named_children(self)` — [`L606`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L606) — A flattened view of the parts torchtitan expects.
  - <a id="TPUHFTransformerModel.norm"></a>`norm(self)` — [`L575`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L575) — The final norm, or an Identity for an architecture without one.
  - <a id="TPUHFTransformerModel.rotary_emb"></a>`rotary_emb(self)` — [`L597`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L597) — The rotary embedding module; AttributeError for a learned-position model
  - <a id="TPUHFTransformerModel.to_empty"></a>`to_empty(self, *, device, recurse: bool = True)` — [`L785`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L785) — Materialize parameters, but keep buffer values.
  - <a id="TPUHFTransformerModel.tok_embeddings"></a>`tok_embeddings(self)` — [`L557`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L557) — The token embedding table, wherever this architecture keeps it.
- protocol/private: <a id="TPUHFTransformerModel._LOGIT_TRANSFORMS"></a>`_LOGIT_TRANSFORMS`[`L406`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L406), <a id="TPUHFTransformerModel.__init__"></a>`__init__`[`L336`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L336), <a id="TPUHFTransformerModel._added_lm_head"></a>`_added_lm_head`[`L385`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L385), <a id="TPUHFTransformerModel._added_norm"></a>`_added_norm`[`L364`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L364), <a id="TPUHFTransformerModel._assign"></a>`_assign`[`L550`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L550), <a id="TPUHFTransformerModel._build_hf_model"></a>`_build_hf_model`[`L453`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L453), <a id="TPUHFTransformerModel._context_length"></a>`_context_length`[`L464`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L464), <a id="TPUHFTransformerModel._forward_kwargs"></a>`_forward_kwargs`[`L348`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L348), <a id="TPUHFTransformerModel._fused_loss"></a>`_fused_loss`[`L350`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L350), <a id="TPUHFTransformerModel._mirrored_logit_transform"></a>`_mirrored_logit_transform`[`L358`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L358), <a id="TPUHFTransformerModel._part"></a>`_part`[`L544`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L544), <a id="TPUHFTransformerModel._position_capacity"></a>`_position_capacity`[`L344`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L344), <a id="TPUHFTransformerModel._reinit_buffer_device"></a>`_reinit_buffer_device`[`L895`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L895)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger), [`model`](../../transformers_modeling_backend/model.md#HFTransformerModel.model), [`HFTransformerModel`](../../transformers_modeling_backend/model.md#HFTransformerModel), [`get_attention_masks`](../../transformers_modeling_backend/model.md#HFTransformerModel.get_attention_masks), [`init_states`](../../transformers_modeling_backend/model.md#HFTransformerModel.init_states), [`__init__`](../../transformers_modeling_backend/model.md#HFTransformerModel.__init__), [`disable_active_parametrization`](../../graph_trainer/simple_fsdp.md#disable_active_parametrization), [`find_head`](_structure.md#find_head), [`find_embedding`](_structure.md#find_embedding), [`Config`](model.md#TPUHFTransformerModel.Config), [`find_layers`](_structure.md#find_layers), [`find_norm`](_structure.md#find_norm), [`_ATTN_IMPLEMENTATION`](../../transformers_modeling_backend/model.md#_ATTN_IMPLEMENTATION), [`find_backbone`](_structure.md#find_backbone), [`document_segment_ids`](attention.md#document_segment_ids), [`find_rotary`](_structure.md#find_rotary), [`position_capacity`](_structure.md#position_capacity), [`_skip_lm_head`](../../transformers_modeling_backend/model.md#HFTransformerModel._skip_lm_head), [`accepted_kwargs`](_structure.md#accepted_kwargs), [`head_out_features`](_structure.md#head_out_features), [`set_at`](_structure.md#set_at), [`to_empty_keep_buffers`](_meta_init.md#to_empty_keep_buffers)
- used by: [`HFTransformerModel`](../../transformers_modeling_backend/model.md#HFTransformerModel), [`get_attention_masks`](../../transformers_modeling_backend/model.md#HFTransformerModel.get_attention_masks), [`init_states`](../../transformers_modeling_backend/model.md#HFTransformerModel.init_states), [`layers`](../../transformers_modeling_backend/model.md#HFTransformerModel.layers), [`named_children`](../../transformers_modeling_backend/model.md#HFTransformerModel.named_children), [`as_tpu_model_config`](model.md#as_tpu_model_config), [`forward`](../../transformers_modeling_backend/model.md#HFTransformerModel.forward), [`tok_embeddings`](../../transformers_modeling_backend/model.md#HFTransformerModel.tok_embeddings), [`lm_head`](../../transformers_modeling_backend/model.md#HFTransformerModel.lm_head), [`norm`](../../transformers_modeling_backend/model.md#HFTransformerModel.norm), [`rotary_emb`](../../transformers_modeling_backend/model.md#HFTransformerModel.rotary_emb), [`_build_hf_model`](../../transformers_modeling_backend/model.md#HFTransformerModel._build_hf_model)  (1 test-only)

### <a id="TPUHFTransformerModel.Config"></a>`TPUHFTransformerModel.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/transformers_modeling_backend/model.py:91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L91)
- doc: Adds no fields, so a flavor Config can be re-classed in place; the
- signature: `class Config(HFTransformerModel.Config):`
- members:
  - <a id="TPUHFTransformerModel.Config._complete_from_hf_config"></a>`_complete_from_hf_config(self, hf_model_id: str)` — [`L258`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L258) — Carry over what the base's attribute copy misses from the HF config.
  - <a id="TPUHFTransformerModel.Config._mirror_logit_transform_into_fused_loss"></a>`_mirror_logit_transform_into_fused_loss(self, job_config, hf_model_id: str)` — [`L213`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L213) — Hand the head's logit transform to the fused CE, which re-applies it.
  - <a id="TPUHFTransformerModel.Config.build"></a>`build(self, **kwargs)` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L108)
  - <a id="TPUHFTransformerModel.Config.update_from_config"></a>`update_from_config(self, *, config=None, **kwargs)` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L119)
- protocol/private: <a id="TPUHFTransformerModel.Config._TEXT_TOWERS"></a>`_TEXT_TOWERS`[`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L97)
- uses (calls/refs, reference-scoped): [`param_init`](../../../protocols/module.md#Module.Config.param_init), [`HFTransformerModel`](../../transformers_modeling_backend/model.md#HFTransformerModel), [`PallasCrossEntropyLoss`](../loss.md#PallasCrossEntropyLoss), [`Config`](../loss.md#PallasCrossEntropyLoss.Config), [`Config`](../../transformers_modeling_backend/model.md#HFTransformerModel.Config), [`_owner`](../../../config/configurable.md#Configurable.Config._owner), [`soft_cap`](../loss.md#PallasCrossEntropyLoss.Config.soft_cap), [`output_multiplier`](../loss.md#PallasCrossEntropyLoss.Config.output_multiplier), [`params_meta_buffers_real`](_meta_init.md#params_meta_buffers_real), [`_REMOTE_CONFIG_DENYLIST`](../../transformers_modeling_backend/model.md#_REMOTE_CONFIG_DENYLIST), [`_replace`](../../transformers_modeling_backend/model.md#HFTransformerModel.Config._replace), [`architectures`](../../transformers_modeling_backend/model.md#HFTransformerModel.Config.architectures)
- used by: [`head_dim`](model.md#Config.head_dim), [`as_tpu_model_config`](model.md#as_tpu_model_config), [`__init__`](model.md#TPUHFTransformerModel.__init__), [`initializer_range`](model.md#Config.initializer_range)

### <a id="_Attrs"></a>`_Attrs`
- def: [`torchtitan/experiments/tpu/transformers_modeling_backend/model.py:58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L58)
- doc: Attribute view over a (nested) config dict, for `_structure` helpers.
- signature: `class _Attrs:`
- protocol/private: <a id="_Attrs.__getattr__"></a>`__getattr__`[`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L64), <a id="_Attrs.__init__"></a>`__init__`[`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L61), <a id="_Attrs._d"></a>`_d`[`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L62)
- used by: [`head_dim`](model.md#Config.head_dim)

## Functions
- <a id="_parse_config_overrides"></a>`_parse_config_overrides(spec: str)` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L69) — Parse a JSON object of HF config overrides, e.g. ``{"attn_pdrop": 0}``.
- <a id="_use_pallas_grouped_mm"></a>`_use_pallas_grouped_mm(moe_config)` — [`L1000`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L1000) — Set use_pallas_grouped_mm on every TpuGroupedExperts in a converted MoE config.
- <a id="as_tpu_model_config"></a>`as_tpu_model_config(model_config: HFTransformerModel.Config, *, fused_loss: bool = False)` — [`L930`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L930) — A copy of a flavor's Config that builds a TPUHFTransformerModel.
- <a id="substitute_tpu_experts"></a>`substitute_tpu_experts(model: nn.Module)` — [`L954`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L954) — Swap the TPU grouped experts and token dispatcher into each probed MoE config. — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)

## Other members
- <a id="Config.fused_loss_logit_transform"></a>`Config.fused_loss_logit_transform` — [`L252`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L252)
- <a id="Config.head_dim"></a>`Config.head_dim` — [`L135`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L135)
- <a id="Config.initializer_range"></a>`Config.initializer_range` — [`L196`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/model.py#L196)

