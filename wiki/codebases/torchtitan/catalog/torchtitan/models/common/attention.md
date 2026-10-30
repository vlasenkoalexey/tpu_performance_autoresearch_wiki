---
title: 'Module: torchtitan/models/common/attention.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.attention`/
symbols:
  FlexInnerAttention: FlexInnerAttention#
  ScaledDotProductInnerAttention: ScaledDotProductInnerAttention#
  VarlenInnerAttention: VarlenInnerAttention#
  AttentionMasksType: AttentionMasksType.
  BaseAttention: BaseAttention#
  GQAttention: GQAttention#
  FlexInnerAttention.Config: FlexInnerAttention#Config#
  FlexInnerAttention.forward: FlexInnerAttention#forward().
  GQAttention.forward: GQAttention#forward().
  get_causal_mask_mod: get_causal_mask_mod().
  FusedQKVLinear: FusedQKVLinear#
  segment_ids_from_positions: segment_ids_from_positions().
  VarlenInnerAttention.Config: VarlenInnerAttention#Config#
  create_attention_mask: create_attention_mask().
  GQAttention.k_norm: GQAttention#k_norm.
  create_varlen_metadata_for_document: create_varlen_metadata_for_document().
  ScaledDotProductInnerAttention.Config: ScaledDotProductInnerAttention#Config#
  QKVLinear: QKVLinear#
  VarlenInnerAttention.forward: VarlenInnerAttention#forward().
  BaseAttention.Config: BaseAttention#Config#
  FlexInnerAttention.inductor_configs: FlexInnerAttention#inductor_configs.
  GQAttention.rope: GQAttention#rope.
  ScaledDotProductInnerAttention.forward: ScaledDotProductInnerAttention#forward().
  BaseQKVLinear: BaseQKVLinear#
  FusedQKVLinear.forward: FusedQKVLinear#forward().
  VarlenMetadata: VarlenMetadata#
  GQAttention.Config.inner_attention: GQAttention#Config#inner_attention.
  GQAttention.q_norm: GQAttention#q_norm.
  BaseAttention.Config.inner_attention: BaseAttention#Config#inner_attention.
  GQAttention.Config.qk_norm: GQAttention#Config#qk_norm.
  FusedQKVLinear.__init__: FusedQKVLinear#__init__().
  GQAttention.Config.__post_init__: GQAttention#Config#__post_init__().
  InnerAttention: InnerAttention#
  get_sliding_window_mask_mod: get_sliding_window_mask_mod().
  GQAttention.Config.n_heads: GQAttention#Config#n_heads.
  get_efficient_causal_mask_mod_for_packed_document: get_efficient_causal_mask_mod_for_packed_document().
  QKVLinear.Config.wkv: QKVLinear#Config#wkv.
  FusedQKVLinear.Config: FusedQKVLinear#Config#
  FlexInnerAttention._compiled_flex_attn: FlexInnerAttention#_compiled_flex_attn.
  QKVLinear.Config.wq: QKVLinear#Config#wq.
  FusedQKVLinear.Config.wqkv: FusedQKVLinear#Config#wqkv.
  BaseQKVLinear.head_dim: BaseQKVLinear#head_dim.
  QKVLinear.forward: QKVLinear#forward().
  QKVLinear.Config: QKVLinear#Config#
  GQAttention.Config: GQAttention#Config#
  GQAttention.Config.n_kv_heads: GQAttention#Config#n_kv_heads.
  GQAttention.Config.rope: GQAttention#Config#rope.
  GQAttention.inner_attention: GQAttention#inner_attention.
  BaseQKVLinear.Config.head_dim: BaseQKVLinear#Config#head_dim.
  GQAttention.Config.qkv_linear: GQAttention#Config#qkv_linear.
  GQAttention.Config.wo: GQAttention#Config#wo.
  get_document_mask_mod: get_document_mask_mod().
  GQAttention.qkv_linear: GQAttention#qkv_linear.
  FusedQKVLinear.Config.n_heads: FusedQKVLinear#Config#n_heads.
  FusedQKVLinear.Config.n_kv_heads: FusedQKVLinear#Config#n_kv_heads.
  FusedQKVLinear.wqkv: FusedQKVLinear#wqkv.
  GQAttention.enable_gqa: GQAttention#enable_gqa.
  GQAttention.wo: GQAttention#wo.
  BaseQKVLinear.Config: BaseQKVLinear#Config#
  GQAttention.Config.head_dim: GQAttention#Config#head_dim.
  ScaledDotProductInnerAttention.__init__: ScaledDotProductInnerAttention#__init__().
  FusedQKVLinear.heads_per_kv: FusedQKVLinear#heads_per_kv.
  GQAttention.scaling: GQAttention#scaling.
  VarlenInnerAttention.window_size: VarlenInnerAttention#window_size.
  FlexInnerAttention.compiled_flex_attn: FlexInnerAttention#compiled_flex_attn().
  GQAttention.head_dim: GQAttention#head_dim.
  InnerAttention.Config: InnerAttention#Config#
  QKVLinear.local_qkv_head_split: QKVLinear#local_qkv_head_split().
  BaseQKVLinear.forward: BaseQKVLinear#forward().
  QKVLinear.wq: QKVLinear#wq.
  QKVLinear.wk: QKVLinear#wk.
  QKVLinear.wv: QKVLinear#wv.
  VarlenMetadata.cu_seq_q: VarlenMetadata#cu_seq_q.
  GQAttention.Config.dim: GQAttention#Config#dim.
  local_head_split: local_head_split().
  BaseQKVLinear.__init__: BaseQKVLinear#__init__().
  VarlenInnerAttention.Config.window_size: VarlenInnerAttention#Config#window_size.
  FlexInnerAttention.Config.block_size: FlexInnerAttention#Config#block_size.
  ScaledDotProductInnerAttention.sdpa_backends: ScaledDotProductInnerAttention#sdpa_backends.
  BaseAttention.Config.n_heads: BaseAttention#Config#n_heads.
  GQAttention.n_kv_heads: GQAttention#n_kv_heads.
  FlexInnerAttention.__init__: FlexInnerAttention#__init__().
  FlexInnerAttention.Config.kernel_options: FlexInnerAttention#Config#kernel_options.
  QKVLinear.__init__: QKVLinear#__init__().
  GQAttention.__init__: GQAttention#__init__().
  FlexInnerAttention.kernel_options: FlexInnerAttention#kernel_options.
  FlexInnerAttention._get_aux_request: FlexInnerAttention#_get_aux_request().
  FlexInnerAttention._process_aux: FlexInnerAttention#_process_aux().
  get_fixed_block_mask_mod: get_fixed_block_mask_mod().
  BaseAttention.Config.__post_init__: BaseAttention#Config#__post_init__().
  GQAttention.n_heads: GQAttention#n_heads.
  FusedQKVLinear.r_dim: FusedQKVLinear#r_dim.
  FusedQKVLinear._split: FusedQKVLinear#_split().
  VarlenInnerAttention.__init__: VarlenInnerAttention#__init__().
  VarlenMetadata.cu_seq_k: VarlenMetadata#cu_seq_k.
  VarlenMetadata.max_q: VarlenMetadata#max_q.
  VarlenMetadata.max_k: VarlenMetadata#max_k.
  get_fixed_block_mask_mod.blocked_mask_mod: get_fixed_block_mask_mod().blocked_mask_mod().
  get_sliding_window_mask_mod.sliding_window_mod: get_sliding_window_mask_mod().sliding_window_mod().
  FusedQKVLinear._merge_qkv_on_load: FusedQKVLinear#_merge_qkv_on_load().
  varlen_attn: varlen_attn().
  varlen_attn_with_lse: varlen_attn_with_lse().
  get_causal_mask_mod._causal_mask: get_causal_mask_mod()._causal_mask().
  get_document_mask_mod.document_mask: get_document_mask_mod().document_mask().
  get_efficient_causal_mask_mod_for_packed_document.packed_document_mask: get_efficient_causal_mask_mod_for_packed_document().packed_document_mask().
  _compiled_create_block_mask: _compiled_create_block_mask.
  FusedQKVLinear._split_qkv_on_save: FusedQKVLinear#_split_qkv_on_save().
  __all__: __all__.
---
# Module: [`torchtitan/models/common/attention.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py)

## Classes
### <a id="BaseAttention"></a>`BaseAttention`  ·  implements/extends Module
- def: [`torchtitan/models/common/attention.py:745`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L745) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- signature: `class BaseAttention(Module):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`GQAttention`](attention.md#GQAttention), [`Attention`](../deepseek_v3/model.md#Attention), [`Qwen35Attention`](../qwen3_5/model.md#Qwen35Attention), [`Attention`](../gpt_oss/model.md#Attention), [`Attention`](../deepseek_v4/attention.md#Attention), [`KimiMLAAttention`](../kimi_k3/model.md#KimiMLAAttention)
- used by: [`Module`](../../protocols/module.md#Module), [`GQAttention`](attention.md#GQAttention), [`validate_context_parallel`](../../config/validation.md#validate_context_parallel), [`attention`](decoder.md#TransformerBlock.Config.attention), [`validate_tpu_context_parallel`](../../experiments/tpu/cp_attention.md#validate_tpu_context_parallel), [`Attention`](../deepseek_v3/model.md#Attention), [`_create_flex_attention_mask`](decoder.md#Decoder._create_flex_attention_mask), [`qwen3_debugmodel_allgather_cp2`](../../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel_allgather_cp2), [`transform`](../../config/transform/context_parallel.md#ContextParallelTransform.transform), [`__post_init__`](attention.md#GQAttention.Config.__post_init__), [`first_attention`](decoder.md#Decoder.Config.first_attention), [`revert_tpu_context_parallel`](../../experiments/tpu/cp_attention.md#revert_tpu_context_parallel), [`Qwen35Attention`](../qwen3_5/model.md#Qwen35Attention), [`Config`](../deepseek_v3/model.md#Attention.Config), [`_create_flex_attention_mask_for_document`](decoder.md#Decoder._create_flex_attention_mask_for_document), [`Config`](attention.md#GQAttention.Config), [`Attention`](../gpt_oss/model.md#Attention), [`Config`](../gpt_oss/model.md#Attention.Config), [`Config`](../qwen3_5/model.md#Qwen35Attention.Config), [`Config`](../kimi_k3/model.md#KimiMLAAttention.Config), [`Config`](../deepseek_v4/attention.md#Attention.Config), [`Attention`](../deepseek_v4/attention.md#Attention), [`KimiMLAAttention`](../kimi_k3/model.md#KimiMLAAttention)

### <a id="BaseAttention.Config"></a>`BaseAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:747`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L747)
- signature: `class Config(Module.Config):`
- members:
  - <a id="BaseAttention.Config.inner_attention"></a>`inner_attention` — [`L749`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L749)
  - <a id="BaseAttention.Config.n_heads"></a>`n_heads` — [`L748`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L748)
- protocol/private: <a id="BaseAttention.Config.__post_init__"></a>`__post_init__`[`L751`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L751)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`update_from_config`](decoder.md#Decoder.Config.update_from_config), [`get_attention_masks`](decoder.md#Decoder.get_attention_masks), [`_mla_config`](../kimi_k3/__init__.md#_mla_config), [`get_attention_masks`](../muse_glimmer/model.md#MuseGlimmerModel.get_attention_masks), [`get_nparams_and_flops`](../kimi_k3/model.md#KimiK3Model.Config.get_nparams_and_flops), [`validate_context_parallel`](../../config/validation.md#validate_context_parallel), [`_set_llama3_layer_sharding`](../llama3/sharding.md#_set_llama3_layer_sharding), [`attention`](decoder.md#TransformerBlock.Config.attention), [`validate_tpu_context_parallel`](../../experiments/tpu/cp_attention.md#validate_tpu_context_parallel), [`_create_flex_attention_mask`](decoder.md#Decoder._create_flex_attention_mask), [`qwen3_debugmodel_allgather_cp2`](../../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel_allgather_cp2), [`get_attention_masks`](../qwen3_5/model.md#Qwen35Model.get_attention_masks), [`get_attention_masks`](../kimi_k3/model.md#KimiK3Model.get_attention_masks), [`transform`](../../config/transform/context_parallel.md#ContextParallelTransform.transform), [`first_full_attention_backend`](decoder.md#Decoder.Config.first_full_attention_backend), [`__post_init__`](attention.md#GQAttention.Config.__post_init__), [`first_attention`](decoder.md#Decoder.Config.first_attention), [`revert_tpu_context_parallel`](../../experiments/tpu/cp_attention.md#revert_tpu_context_parallel), [`Config`](../deepseek_v3/model.md#Attention.Config), [`_create_flex_attention_mask_for_document`](decoder.md#Decoder._create_flex_attention_mask_for_document), [`Config`](attention.md#GQAttention.Config), [`Config`](../gpt_oss/model.md#Attention.Config), [`Config`](../qwen3_5/model.md#Qwen35Attention.Config), [`Config`](../kimi_k3/model.md#KimiMLAAttention.Config), [`Config`](../deepseek_v4/attention.md#Attention.Config), [`n_heads`](../kimi_k3/model.md#KimiMLAAttention.n_heads)  (1 test-only)

### <a id="BaseQKVLinear"></a>`BaseQKVLinear`  ·  implements/extends Module
- def: [`torchtitan/models/common/attention.py:755`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L755)
- doc: Base class for Q/K/V projection strategies.
- signature: `class BaseQKVLinear(Module):`
- members:
  - <a id="BaseQKVLinear.forward"></a>`forward(self, x: torch.Tensor)` — [`L770`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L770) — Project input into Q, K, V tensors.
  - <a id="BaseQKVLinear.head_dim"></a>`head_dim` — [`L768`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L768)
- protocol/private: <a id="BaseQKVLinear.__init__"></a>`__init__`[`L766`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L766)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`FusedQKVLinear`](attention.md#FusedQKVLinear), [`QKVLinear`](attention.md#QKVLinear), [`forward`](attention.md#FusedQKVLinear.forward), [`forward`](attention.md#QKVLinear.forward), [`TpuPackedQKVLinear`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear), [`head_dim`](attention.md#BaseQKVLinear.Config.head_dim), [`forward`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.forward), [`Config`](attention.md#BaseQKVLinear.Config)
- used by: [`Module`](../../protocols/module.md#Module), [`FusedQKVLinear`](attention.md#FusedQKVLinear), [`QKVLinear`](attention.md#QKVLinear), [`forward`](dist_gemm.md#AllGatherFusedQKVLinear.forward), [`forward`](attention.md#FusedQKVLinear.forward), [`__init__`](attention.md#FusedQKVLinear.__init__), [`Config`](attention.md#FusedQKVLinear.Config), [`Config`](attention.md#QKVLinear.Config), [`TpuPackedQKVLinear`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear), [`qkv_linear`](attention.md#GQAttention.Config.qkv_linear), [`forward`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.forward), [`__init__`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.__init__), [`local_qkv_head_split`](attention.md#QKVLinear.local_qkv_head_split), [`qkv_linear`](../gpt_oss/model.md#Attention.Config.qkv_linear), [`__init__`](attention.md#QKVLinear.__init__)  (2 test-only)

### <a id="BaseQKVLinear.Config"></a>`BaseQKVLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:763`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L763)
- signature: `class Config(Module.Config):`
- members:
  - <a id="BaseQKVLinear.Config.head_dim"></a>`head_dim` — [`L764`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L764)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_build_muse_glimmer_attention`](../muse_glimmer/__init__.md#_build_muse_glimmer_attention), [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`make_gqa_config`](config_utils.md#make_gqa_config), [`_packed_param_init`](../../experiments/tpu/qkv.md#_packed_param_init), [`kv_rows`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.kv_rows), [`Config`](attention.md#FusedQKVLinear.Config), [`head_dim`](attention.md#BaseQKVLinear.head_dim), [`Config`](attention.md#QKVLinear.Config), [`qkv_linear`](attention.md#GQAttention.Config.qkv_linear), [`q_rows`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.q_rows), [`qkv_linear`](../gpt_oss/model.md#Attention.Config.qkv_linear), [`__init__`](attention.md#BaseQKVLinear.__init__)  (2 test-only)

### <a id="FlexInnerAttention"></a>`FlexInnerAttention`  ·  implements/extends InnerAttention
- def: [`torchtitan/models/common/attention.py:233`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L233) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- doc: Inner attention using `flex_attention` with torch.compile.
- signature: `class FlexInnerAttention(InnerAttention):`
- members:
  - <a id="FlexInnerAttention._get_aux_request"></a>`_get_aux_request(self, *, return_lse: bool)` — [`L276`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L276) — Return the auxiliary outputs needed from this attention call.
  - <a id="FlexInnerAttention._process_aux"></a>`_process_aux(self, aux: Any)` — [`L280`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L280) — Consume auxiliary outputs requested by ``_get_aux_request``.
  - <a id="FlexInnerAttention.compiled_flex_attn"></a>`compiled_flex_attn(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, *, score_mod: _score_mod_signature | None, block_mask: BlockMask | None, scale: float | None, enable_gqa: bool, return_aux: AuxRequest, kernel_options: dict)` — [`L290`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L290) — Run compiled FlexInnerAttention outside SPMD typechecking.
  - <a id="FlexInnerAttention.forward"></a>`forward(self, q_THK: torch.Tensor, k_THK: torch.Tensor, v_THV: torch.Tensor, *, attention_masks: BlockMask, score_mod: _score_mod_signature | None = None, scale: float | None = None, enable_gqa: bool = False, out_transform: (Callable[[torch.Tensor, torch.Tensor], torch.Tensor] | None) = None, **kwargs)` — [`L337`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L337)
  - <a id="FlexInnerAttention.inductor_configs"></a>`inductor_configs` — [`L250`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L250)
  - <a id="FlexInnerAttention.kernel_options"></a>`kernel_options` — [`L274`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L274)
- protocol/private: <a id="FlexInnerAttention.__init__"></a>`__init__`[`L272`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L272), <a id="FlexInnerAttention._compiled_flex_attn"></a>`_compiled_flex_attn`[`L267`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L267)
- uses (calls/refs, reference-scoped): [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`Config`](attention.md#FlexInnerAttention.Config), [`KVAllGatherCPFlexInnerAttention`](cp_attention.md#KVAllGatherCPFlexInnerAttention), [`DSV4FlexInnerAttention`](../deepseek_v4/attention.md#DSV4FlexInnerAttention), [`InnerAttention`](attention.md#InnerAttention), [`forward`](cp_attention.md#KVAllGatherCPFlexInnerAttention.forward), [`forward`](cp_attention.md#UlyssesCPFlexInnerAttention.forward), [`UlyssesCPFlexInnerAttention`](cp_attention.md#UlyssesCPFlexInnerAttention), [`QKClipFlexInnerAttention`](../kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention), [`kernel_options`](attention.md#FlexInnerAttention.Config.kernel_options), [`maybe_regional_inductor`](../../distributed/compile.md#maybe_regional_inductor), [`_process_aux`](../kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention._process_aux), [`forward`](../deepseek_v4/attention.md#CompressedSparseAttention.forward), [`forward`](../deepseek_v4/attention.md#HeavilyCompressedAttention.forward), [`forward`](../deepseek_v4/attention.md#SlidingWindowAttention.forward), [`_get_aux_request`](../kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention._get_aux_request)
- used by: [`model_path`](../../experiments/rl/actors/generator.md#VLLMGenerator.model_path), [`_precompile_aot_fx_trace`](../../experiments/graph_trainer/precompile_main.md#_precompile_aot_fx_trace), [`__post_init__`](../../trainer.md#Trainer.Config.__post_init__), [`preprocess_inputs`](../qwen3_5/model.md#Qwen35Model.preprocess_inputs), [`_build_model`](../../experiments/rl/actors/trainer.md#PolicyTrainer._build_model), [`preprocess_inputs`](../muse_glimmer/model.md#MuseGlimmerModel.preprocess_inputs), [`preprocess_inputs`](../deepseek_v3/mtp.md#MTPDecoder.preprocess_inputs), [`get_attention_masks`](decoder.md#Decoder.get_attention_masks), [`_tp_rank`](../../experiments/rl/actors/generator.md#VLLMGenerator._tp_rank), [`get_attention_config`](config_utils.md#get_attention_config), [`preprocess_inputs`](decoder.md#Decoder.preprocess_inputs), [`preprocess_inputs`](../kimi_k2_7/model.md#KimiK25Model.preprocess_inputs), [`get_attention_masks`](../muse_glimmer/model.md#MuseGlimmerModel.get_attention_masks), [`generate`](../../experiments/rl/generate.md#generate), [`set_determinism`](../../distributed/utils.md#set_determinism), [`get_attention_masks`](../gpt_oss/model.md#GptOssModel.get_attention_masks), [`preprocess_inputs`](../kimi_k3/model.md#KimiK3Model.preprocess_inputs), [`_forward_impl`](../deepseek_v4/attention.md#DSV4FlexInnerAttention._forward_impl), [`final_inductor_compile_passes`](../../experiments/graph_trainer/passes.md#final_inductor_compile_passes), [`KVAllGatherCPFlexInnerAttention`](cp_attention.md#KVAllGatherCPFlexInnerAttention), [`_create_flex_attention_mask`](decoder.md#Decoder._create_flex_attention_mask), [`DSV4FlexInnerAttention`](../deepseek_v4/attention.md#DSV4FlexInnerAttention), [`InnerAttention`](attention.md#InnerAttention), [`forward`](cp_attention.md#KVAllGatherCPFlexInnerAttention.forward), [`forward`](cp_attention.md#UlyssesCPFlexInnerAttention.forward), [`inner_attention`](../deepseek_v3/model.md#Attention.Config.inner_attention), [`inner_attention`](vision_encoder.md#VisionAttention.Config.inner_attention), [`convert`](../../experiments/rl/batch_invariance.md#BatchInvariantFlexConverter.convert), [`inner_attention`](../kimi_k3/model.md#KimiMLAAttention.Config.inner_attention), [`UlyssesCPFlexInnerAttention`](cp_attention.md#UlyssesCPFlexInnerAttention), [`_maybe_regional_inductor_backend`](../../distributed/compile.md#_maybe_regional_inductor_backend), [`Config`](../deepseek_v4/attention.md#DSV4FlexInnerAttention.Config), [`__init__`](cp_attention.md#KVAllGatherCPFlexInnerAttention.__init__), [`Config`](../kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention.Config), [`QKClipFlexInnerAttention`](../kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention), [`Config`](cp_attention.md#KVAllGatherCPFlexInnerAttention.Config), [`Config`](cp_attention.md#UlyssesCPFlexInnerAttention.Config), [`__init__`](../deepseek_v4/attention.md#DSV4FlexInnerAttention.__init__), [`__init__`](../kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention.__init__)  (16 test-only)

### <a id="FlexInnerAttention.Config"></a>`FlexInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:246`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L246)
- signature: `class Config(InnerAttention.Config):`
- members:
  - <a id="FlexInnerAttention.Config.block_size"></a>`block_size` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L247)
  - <a id="FlexInnerAttention.Config.kernel_options"></a>`kernel_options` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L248)
- uses (calls/refs, reference-scoped): [`InnerAttention`](attention.md#InnerAttention), [`Config`](attention.md#InnerAttention.Config)
- used by: [`model_path`](../../experiments/rl/actors/generator.md#VLLMGenerator.model_path), [`_precompile_aot_fx_trace`](../../experiments/graph_trainer/precompile_main.md#_precompile_aot_fx_trace), [`__post_init__`](../../trainer.md#Trainer.Config.__post_init__), [`preprocess_inputs`](../qwen3_5/model.md#Qwen35Model.preprocess_inputs), [`_build_model`](../../experiments/rl/actors/trainer.md#PolicyTrainer._build_model), [`preprocess_inputs`](../muse_glimmer/model.md#MuseGlimmerModel.preprocess_inputs), [`preprocess_inputs`](../deepseek_v3/mtp.md#MTPDecoder.preprocess_inputs), [`get_attention_masks`](decoder.md#Decoder.get_attention_masks), [`_tp_rank`](../../experiments/rl/actors/generator.md#VLLMGenerator._tp_rank), [`get_attention_config`](config_utils.md#get_attention_config), [`preprocess_inputs`](decoder.md#Decoder.preprocess_inputs), [`preprocess_inputs`](../kimi_k2_7/model.md#KimiK25Model.preprocess_inputs), [`get_attention_masks`](../muse_glimmer/model.md#MuseGlimmerModel.get_attention_masks), [`generate`](../../experiments/rl/generate.md#generate), [`get_attention_masks`](../gpt_oss/model.md#GptOssModel.get_attention_masks), [`preprocess_inputs`](../kimi_k3/model.md#KimiK3Model.preprocess_inputs), [`_create_flex_attention_mask`](decoder.md#Decoder._create_flex_attention_mask), [`inner_attention`](../deepseek_v3/model.md#Attention.Config.inner_attention), [`inner_attention`](vision_encoder.md#VisionAttention.Config.inner_attention), [`convert`](../../experiments/rl/batch_invariance.md#BatchInvariantFlexConverter.convert), [`inner_attention`](../kimi_k3/model.md#KimiMLAAttention.Config.inner_attention), [`Config`](../deepseek_v4/attention.md#DSV4FlexInnerAttention.Config), [`Config`](../kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention.Config), [`Config`](cp_attention.md#KVAllGatherCPFlexInnerAttention.Config), [`Config`](cp_attention.md#UlyssesCPFlexInnerAttention.Config), [`__init__`](attention.md#FlexInnerAttention.__init__), [`block_size`](../deepseek_v4/attention.md#DSV4FlexInnerAttention.block_size), [`kernel_options`](attention.md#FlexInnerAttention.kernel_options)  (6 test-only)

### <a id="FusedQKVLinear"></a>`FusedQKVLinear`  ·  implements/extends BaseQKVLinear
- def: [`torchtitan/models/common/attention.py:824`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L824)
- doc: Single fused linear projection, split along R dimension.
- signature: `class FusedQKVLinear(BaseQKVLinear):`
- members:
  - <a id="FusedQKVLinear._merge_qkv_on_load"></a>`_merge_qkv_on_load(module, state_dict, prefix, *args)` — [`L945`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L945) — Merge stock ``wq``/``wk``/``wv`` back into fused ``wqkv`` (weight and bias).
  - <a id="FusedQKVLinear._split_qkv_on_save"></a>`_split_qkv_on_save(module, state_dict, prefix, local_metadata)` — [`L915`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L915) — Split fused ``wqkv`` into stock ``wq``/``wk``/``wv`` (weight and bias).
  - <a id="FusedQKVLinear.forward"></a>`forward(self, x: torch.Tensor)` — [`L866`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L866)
  - <a id="FusedQKVLinear.heads_per_kv"></a>`heads_per_kv` — [`L852`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L852)
  - <a id="FusedQKVLinear.r_dim"></a>`r_dim` — [`L853`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L853)
  - <a id="FusedQKVLinear.wqkv"></a>`wqkv` — [`L851`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L851)
- protocol/private: <a id="FusedQKVLinear.__init__"></a>`__init__`[`L844`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L844), <a id="FusedQKVLinear._split"></a>`_split`[`L885`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L885)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`BaseQKVLinear`](attention.md#BaseQKVLinear), [`forward`](dist_gemm.md#AllGatherFusedQKVLinear.forward), [`Config`](attention.md#FusedQKVLinear.Config), [`wqkv`](attention.md#FusedQKVLinear.Config.wqkv), [`head_dim`](attention.md#BaseQKVLinear.head_dim), [`n_heads`](attention.md#FusedQKVLinear.Config.n_heads), [`n_kv_heads`](attention.md#FusedQKVLinear.Config.n_kv_heads), [`__init__`](attention.md#BaseQKVLinear.__init__), [`AllGatherFusedQKVLinear`](dist_gemm.md#AllGatherFusedQKVLinear)
- used by: [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`make_gqa_config`](config_utils.md#make_gqa_config), [`_bld_qkv`](../../experiments/tpu/bld_layout.md#_BLDGQAttention._bld_qkv), [`set_qkv_linear_sharding`](decoder_sharding.md#set_qkv_linear_sharding), [`_packed_param_init`](../../experiments/tpu/qkv.md#_packed_param_init), [`BaseQKVLinear`](attention.md#BaseQKVLinear), [`convert`](../../experiments/tpu/qkv.md#TpuPackedQKVConverter.convert), [`forward`](dist_gemm.md#AllGatherFusedQKVLinear.forward), [`_QKV_FORWARDS`](../../experiments/tpu/bld_layout.md#_QKV_FORWARDS), [`load_weights_on_driver`](../../experiments/tpu/rl_nc_ray/weight_transfer_utils.md#load_weights_on_driver), [`Config`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.Config), [`get_state_dict_layouts`](../../experiments/rl/models/vllm_wrapper.md#VLLMModelWrapper.get_state_dict_layouts), [`forward`](attention.md#BaseQKVLinear.forward), [`Config`](dist_gemm.md#AllGatherFusedQKVLinear.Config), [`AllGatherFusedQKVLinear`](dist_gemm.md#AllGatherFusedQKVLinear)  (2 test-only)

### <a id="FusedQKVLinear.Config"></a>`FusedQKVLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:839`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L839)
- signature: `class Config(BaseQKVLinear.Config):`
- members:
  - <a id="FusedQKVLinear.Config.n_heads"></a>`n_heads` — [`L840`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L840)
  - <a id="FusedQKVLinear.Config.n_kv_heads"></a>`n_kv_heads` — [`L841`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L841)
  - <a id="FusedQKVLinear.Config.wqkv"></a>`wqkv` — [`L842`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L842)
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config), [`BaseQKVLinear`](attention.md#BaseQKVLinear), [`Config`](attention.md#BaseQKVLinear.Config)
- used by: [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`set_qkv_linear_sharding`](decoder_sharding.md#set_qkv_linear_sharding), [`_packed_param_init`](../../experiments/tpu/qkv.md#_packed_param_init), [`convert`](../../experiments/tpu/qkv.md#TpuPackedQKVConverter.convert), [`kv_rows`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.kv_rows), [`__init__`](attention.md#FusedQKVLinear.__init__), [`wqkv_packed`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.wqkv_packed), [`Config`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.Config), [`__init__`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.__init__), [`wqkv`](attention.md#FusedQKVLinear.wqkv), [`heads_per_kv`](attention.md#FusedQKVLinear.heads_per_kv), [`q_rows`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.q_rows), [`Config`](dist_gemm.md#AllGatherFusedQKVLinear.Config), [`heads_per_kv`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.heads_per_kv), [`n_heads`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.n_heads), [`n_kv_heads`](../../experiments/tpu/qkv.md#TpuPackedQKVLinear.n_kv_heads)  (2 test-only)

### <a id="GQAttention"></a>`GQAttention`  ·  implements/extends BaseAttention
- def: [`torchtitan/models/common/attention.py:999`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L999) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- doc: Grouped-Query Attention with pluggable Q/K/V projection.
- signature: `class GQAttention(BaseAttention):`
- members:
  - <a id="GQAttention.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L1068`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1068)
  - <a id="GQAttention.enable_gqa"></a>`enable_gqa` — [`L1050`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1050)
  - <a id="GQAttention.head_dim"></a>`head_dim` — [`L1045`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1045)
  - <a id="GQAttention.inner_attention"></a>`inner_attention` — [`L1056`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1056)
  - <a id="GQAttention.k_norm"></a>`k_norm` — [`L1060`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1060) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
  - <a id="GQAttention.n_heads"></a>`n_heads` — [`L1041`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1041)
  - <a id="GQAttention.n_kv_heads"></a>`n_kv_heads` — [`L1042`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1042)
  - <a id="GQAttention.q_norm"></a>`q_norm` — [`L1059`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1059)
  - <a id="GQAttention.qkv_linear"></a>`qkv_linear` — [`L1054`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1054)
  - <a id="GQAttention.rope"></a>`rope` — [`L1051`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1051)
  - <a id="GQAttention.scaling"></a>`scaling` — [`L1066`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1066)
  - <a id="GQAttention.wo"></a>`wo` — [`L1055`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1055)
- protocol/private: <a id="GQAttention.__init__"></a>`__init__`[`L1039`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1039)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`RMSNorm`](nn_modules.md#RMSNorm), [`AttentionMasksType`](attention.md#AttentionMasksType), [`BaseAttention`](attention.md#BaseAttention), [`RoPE`](rope.md#RoPE), [`forward`](../muse_glimmer/model.md#Attention.forward), [`forward`](../../experiments/tpu/bld_layout.md#_BLDGQAttention.forward), [`inner_attention`](attention.md#GQAttention.Config.inner_attention), [`qk_norm`](attention.md#GQAttention.Config.qk_norm), [`n_heads`](attention.md#GQAttention.Config.n_heads), [`Attention`](../muse_glimmer/model.md#Attention), [`Config`](attention.md#GQAttention.Config), [`n_kv_heads`](attention.md#GQAttention.Config.n_kv_heads), [`rope`](attention.md#GQAttention.Config.rope), [`qkv_linear`](attention.md#GQAttention.Config.qkv_linear), [`wo`](attention.md#GQAttention.Config.wo), [`remat_should_recompute`](../../protocols/module.md#Module.remat_should_recompute), [`remat_region_name`](../../protocols/module.md#Module.remat_region_name), [`head_dim`](attention.md#GQAttention.Config.head_dim), [`dim`](attention.md#GQAttention.Config.dim), [`_BLDGQAttention`](../../experiments/tpu/bld_layout.md#_BLDGQAttention)  (2 test-only)
- used by: [`make_gqa_config`](config_utils.md#make_gqa_config), [`_set_qwen3_layer_sharding`](../qwen3/sharding.md#_set_qwen3_layer_sharding), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`set_gqa_attention_sharding`](decoder_sharding.md#set_gqa_attention_sharding), [`BaseAttention`](attention.md#BaseAttention), [`apply_bld_layout`](../../experiments/tpu/bld_layout.md#apply_bld_layout), [`forward`](../muse_glimmer/model.md#Attention.forward), [`_bld_qkv`](../../experiments/tpu/bld_layout.md#_BLDGQAttention._bld_qkv), [`forward`](../../experiments/tpu/bld_layout.md#_BLDGQAttention.forward), [`forward`](../../experiments/tpu/muse_glimmer/attention.md#TpuMuseGlimmerAttention.forward), [`_attention_eligible`](../../experiments/tpu/bld_layout.md#_attention_eligible), [`_bld_rope`](../../experiments/tpu/bld_layout.md#_BLDGQAttention._bld_rope), [`Attention`](../muse_glimmer/model.md#Attention), [`Config`](../muse_glimmer/model.md#Attention.Config), [`_BLDGQAttention`](../../experiments/tpu/bld_layout.md#_BLDGQAttention), [`__init__`](../muse_glimmer/model.md#Attention.__init__)  (10 test-only)

### <a id="GQAttention.Config"></a>`GQAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:1013`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1013)
- signature: `class Config(BaseAttention.Config):`
- members:
  - <a id="GQAttention.Config.dim"></a>`dim` — [`L1015`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1015)
  - <a id="GQAttention.Config.head_dim"></a>`head_dim` — [`L1020`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1020)
  - <a id="GQAttention.Config.inner_attention"></a>`inner_attention` — [`L1021`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1021)
  - <a id="GQAttention.Config.n_heads"></a>`n_heads` — [`L1014`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1014)
  - <a id="GQAttention.Config.n_kv_heads"></a>`n_kv_heads` — [`L1019`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1019)
  - <a id="GQAttention.Config.qk_norm"></a>`qk_norm` — [`L1018`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1018)
  - <a id="GQAttention.Config.qkv_linear"></a>`qkv_linear` — [`L1016`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1016)
  - <a id="GQAttention.Config.rope"></a>`rope` — [`L1022`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1022)
  - <a id="GQAttention.Config.wo"></a>`wo` — [`L1017`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1017)
- protocol/private: <a id="GQAttention.Config.__post_init__"></a>`__post_init__`[`L1024`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L1024)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config), [`RMSNorm`](nn_modules.md#RMSNorm), [`Config`](../../protocols/module.md#Module.Config), [`Config`](nn_modules.md#RMSNorm.Config), [`BaseAttention`](attention.md#BaseAttention), [`RoPE`](rope.md#RoPE), [`Config`](rope.md#RoPE.Config), [`Config`](attention.md#BaseAttention.Config), [`BaseQKVLinear`](attention.md#BaseQKVLinear), [`Config`](attention.md#BaseQKVLinear.Config), [`__post_init__`](attention.md#BaseAttention.Config.__post_init__)
- used by: [`_build_muse_glimmer_attention`](../muse_glimmer/__init__.md#_build_muse_glimmer_attention), [`make_gqa_config`](config_utils.md#make_gqa_config), [`_set_muse_glimmer_layer_sharding`](../muse_glimmer/sharding.md#_set_muse_glimmer_layer_sharding), [`_set_qwen3_layer_sharding`](../qwen3/sharding.md#_set_qwen3_layer_sharding), [`get_maxtext_decoder_nparams_and_flops`](../../experiments/tpu/mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`set_gqa_attention_sharding`](decoder_sharding.md#set_gqa_attention_sharding), [`k_norm`](attention.md#GQAttention.k_norm), [`use_tpu_attention`](../../experiments/tpu/muse_glimmer/__init__.md#use_tpu_attention), [`rope`](attention.md#GQAttention.rope), [`Config`](../muse_glimmer/model.md#Attention.Config), [`inner_attention`](attention.md#GQAttention.inner_attention), [`qkv_linear`](attention.md#GQAttention.qkv_linear), [`wo`](attention.md#GQAttention.wo), [`scaling`](attention.md#GQAttention.scaling), [`head_dim`](attention.md#GQAttention.head_dim), [`n_kv_heads`](attention.md#GQAttention.n_kv_heads), [`__init__`](attention.md#GQAttention.__init__), [`n_heads`](attention.md#GQAttention.n_heads)  (7 test-only)

### <a id="InnerAttention"></a>`InnerAttention`  ·  implements/extends Module
- def: [`torchtitan/models/common/attention.py:129`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L129) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- doc: Base class for attention kernels used by outer attention modules.
- signature: `class InnerAttention(Module):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`ScaledDotProductInnerAttention`](attention.md#ScaledDotProductInnerAttention), [`VarlenInnerAttention`](attention.md#VarlenInnerAttention)
- used by: [`Module`](../../protocols/module.md#Module), [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`ScaledDotProductInnerAttention`](attention.md#ScaledDotProductInnerAttention), [`VarlenInnerAttention`](attention.md#VarlenInnerAttention), [`Config`](attention.md#FlexInnerAttention.Config), [`Config`](attention.md#VarlenInnerAttention.Config), [`Config`](attention.md#ScaledDotProductInnerAttention.Config)

### <a id="InnerAttention.Config"></a>`InnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:133`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L133)
- signature: `class Config(Module.Config):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`Config`](attention.md#FlexInnerAttention.Config), [`Config`](attention.md#VarlenInnerAttention.Config), [`Config`](attention.md#ScaledDotProductInnerAttention.Config)

### <a id="QKVLinear"></a>`QKVLinear`  ·  implements/extends BaseQKVLinear
- def: [`torchtitan/models/common/attention.py:781`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L781)
- doc: Three separate linear projections for Q, K, V.
- signature: `class QKVLinear(BaseQKVLinear):`
- members:
  - <a id="QKVLinear.forward"></a>`forward(self, x: torch.Tensor)` — [`L795`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L795)
  - <a id="QKVLinear.local_qkv_head_split"></a>`local_qkv_head_split(x)` — [`L803`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L803)
  - <a id="QKVLinear.wk"></a>`wk` — [`L792`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L792)
  - <a id="QKVLinear.wq"></a>`wq` — [`L791`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L791)
  - <a id="QKVLinear.wv"></a>`wv` — [`L793`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L793)
- protocol/private: <a id="QKVLinear.__init__"></a>`__init__`[`L789`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L789)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`BaseQKVLinear`](attention.md#BaseQKVLinear), [`wkv`](attention.md#QKVLinear.Config.wkv), [`wq`](attention.md#QKVLinear.Config.wq), [`head_dim`](attention.md#BaseQKVLinear.head_dim), [`Config`](attention.md#QKVLinear.Config), [`__init__`](attention.md#BaseQKVLinear.__init__)  (2 test-only)
- used by: [`_build_muse_glimmer_attention`](../muse_glimmer/__init__.md#_build_muse_glimmer_attention), [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`make_gqa_config`](config_utils.md#make_gqa_config), [`_bld_qkv`](../../experiments/tpu/bld_layout.md#_BLDGQAttention._bld_qkv), [`set_qkv_linear_sharding`](decoder_sharding.md#set_qkv_linear_sharding), [`BaseQKVLinear`](attention.md#BaseQKVLinear), [`_QKV_FORWARDS`](../../experiments/tpu/bld_layout.md#_QKV_FORWARDS), [`forward`](attention.md#BaseQKVLinear.forward)  (5 test-only)

### <a id="QKVLinear.Config"></a>`QKVLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:785`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L785)
- signature: `class Config(BaseQKVLinear.Config):`
- members:
  - <a id="QKVLinear.Config.wkv"></a>`wkv` — [`L787`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L787)
  - <a id="QKVLinear.Config.wq"></a>`wq` — [`L786`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L786)
- uses (calls/refs, reference-scoped): [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config), [`BaseQKVLinear`](attention.md#BaseQKVLinear), [`Config`](attention.md#BaseQKVLinear.Config)
- used by: [`_build_muse_glimmer_attention`](../muse_glimmer/__init__.md#_build_muse_glimmer_attention), [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`make_gqa_config`](config_utils.md#make_gqa_config), [`set_qkv_linear_sharding`](decoder_sharding.md#set_qkv_linear_sharding), [`wk`](attention.md#QKVLinear.wk), [`wq`](attention.md#QKVLinear.wq), [`wv`](attention.md#QKVLinear.wv), [`__init__`](attention.md#QKVLinear.__init__)  (5 test-only)

### <a id="ScaledDotProductInnerAttention"></a>`ScaledDotProductInnerAttention`  ·  implements/extends InnerAttention
- def: [`torchtitan/models/common/attention.py:393`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L393) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- doc: Inner attention using `F.scaled_dot_product_attention` with CP support.
- signature: `class ScaledDotProductInnerAttention(InnerAttention):`
- members:
  - <a id="ScaledDotProductInnerAttention.forward"></a>`forward(self, q_BLHK: torch.Tensor, k_BLHK: torch.Tensor, v_BLHV: torch.Tensor, *, attention_masks: AttentionMasksType | None = None, scale: float | None = None, enable_gqa: bool = False, is_causal: bool = True, **kwargs)` — [`L435`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L435)
  - <a id="ScaledDotProductInnerAttention.sdpa_backends"></a>`sdpa_backends` — [`L409`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L409)
- protocol/private: <a id="ScaledDotProductInnerAttention.__init__"></a>`__init__`[`L411`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L411)
- uses (calls/refs, reference-scoped): [`AttentionMasksType`](attention.md#AttentionMasksType), [`KVAllGatherCPScaledDotProductInnerAttention`](../../experiments/tpu/cp_attention.md#KVAllGatherCPScaledDotProductInnerAttention), [`Config`](attention.md#ScaledDotProductInnerAttention.Config), [`forward`](../../experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention.forward), [`get_unflatten_seq_len`](../../experiments/tpu/unflatten_shim.md#get_unflatten_seq_len), [`InnerAttention`](attention.md#InnerAttention), [`UlyssesCPScaledDotProductInnerAttention`](../../experiments/tpu/cp_attention.md#UlyssesCPScaledDotProductInnerAttention), [`SlidingWindowScaledDotProductInnerAttention`](../../experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention), [`GraphTrainerScaledDotProductInnerAttention`](../../experiments/graph_trainer/common_utils.md#GraphTrainerScaledDotProductInnerAttention), [`forward`](../../experiments/graph_trainer/common_utils.md#GraphTrainerScaledDotProductInnerAttention.forward)  (2 test-only)
- used by: [`get_attention_masks`](decoder.md#Decoder.get_attention_masks), [`get_attention_config`](config_utils.md#get_attention_config), [`KVAllGatherCPScaledDotProductInnerAttention`](../../experiments/tpu/cp_attention.md#KVAllGatherCPScaledDotProductInnerAttention), [`forward`](../../experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention.forward), [`InnerAttention`](attention.md#InnerAttention), [`_CP_INNER_ATTENTIONS`](../../experiments/tpu/cp_attention.md#_CP_INNER_ATTENTIONS), [`UlyssesCPScaledDotProductInnerAttention`](../../experiments/tpu/cp_attention.md#UlyssesCPScaledDotProductInnerAttention), [`SlidingWindowScaledDotProductInnerAttention`](../../experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention), [`Config`](../../experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention.Config), [`Config`](../../experiments/tpu/cp_attention.md#KVAllGatherCPScaledDotProductInnerAttention.Config), [`local_forward`](../../experiments/tpu/cp_attention.md#KVAllGatherCPInnerAttention.local_forward), [`Config`](../../experiments/tpu/cp_attention.md#UlyssesCPScaledDotProductInnerAttention.Config), [`_apply_cpu_splash_reference_patch`](../../experiments/tpu/base_distributed_device_test.md#_apply_cpu_splash_reference_patch), [`inner_attention`](../flux/model/layers.md#SelfAttention.Config.inner_attention), [`__init__`](../../experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention.__init__), [`inner_attention`](../flux/model/layers.md#DoubleStreamBlock.Config.inner_attention), [`inner_attention`](../flux/model/layers.md#SingleStreamBlock.Config.inner_attention), [`Config`](../../experiments/graph_trainer/common_utils.md#GraphTrainerScaledDotProductInnerAttention.Config), [`_splash_ref_forward`](../../experiments/tpu/base_distributed_device_test.md#_apply_cpu_splash_reference_patch._splash_ref_forward), [`local_forward`](../../experiments/tpu/cp_attention.md#UlyssesCPInnerAttention.local_forward), [`GraphTrainerScaledDotProductInnerAttention`](../../experiments/graph_trainer/common_utils.md#GraphTrainerScaledDotProductInnerAttention), [`forward`](../../experiments/graph_trainer/common_utils.md#GraphTrainerScaledDotProductInnerAttention.forward)  (14 test-only)

### <a id="ScaledDotProductInnerAttention.Config"></a>`ScaledDotProductInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:406`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L406)
- signature: `class Config(InnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`InnerAttention`](attention.md#InnerAttention), [`Config`](attention.md#InnerAttention.Config)
- used by: [`get_attention_masks`](decoder.md#Decoder.get_attention_masks), [`get_attention_config`](config_utils.md#get_attention_config), [`revert_tpu_context_parallel`](../../experiments/tpu/cp_attention.md#revert_tpu_context_parallel), [`Config`](../../experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention.Config), [`Config`](../../experiments/tpu/cp_attention.md#KVAllGatherCPScaledDotProductInnerAttention.Config), [`Config`](../../experiments/tpu/cp_attention.md#UlyssesCPScaledDotProductInnerAttention.Config), [`__init__`](attention.md#ScaledDotProductInnerAttention.__init__), [`inner_attention`](../flux/model/layers.md#SelfAttention.Config.inner_attention), [`inner_attention`](../flux/model/layers.md#DoubleStreamBlock.Config.inner_attention), [`inner_attention`](../flux/model/layers.md#SingleStreamBlock.Config.inner_attention), [`Config`](../../experiments/graph_trainer/common_utils.md#GraphTrainerScaledDotProductInnerAttention.Config)  (5 test-only)

### <a id="VarlenInnerAttention"></a>`VarlenInnerAttention`  ·  implements/extends InnerAttention
- def: [`torchtitan/models/common/attention.py:137`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L137) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- signature: `class VarlenInnerAttention(InnerAttention):`
- members:
  - <a id="VarlenInnerAttention.forward"></a>`forward(self, q_THK: torch.Tensor, k_THK: torch.Tensor, v_THV: torch.Tensor, *, attention_masks: VarlenMetadata, scale: float | None = None, out_transform: (Callable[[torch.Tensor, torch.Tensor], torch.Tensor] | None) = None, **kwargs)` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L165)
  - <a id="VarlenInnerAttention.window_size"></a>`window_size` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L154)
- protocol/private: <a id="VarlenInnerAttention.__init__"></a>`__init__`[`L152`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L152)
- uses (calls/refs, reference-scoped): [`Config`](attention.md#VarlenInnerAttention.Config), [`is_in_batch_invariant_mode`](../../distributed/utils.md#is_in_batch_invariant_mode), [`KVAllGatherCPVarlenInnerAttention`](../../experiments/tpu/cp_attention.md#KVAllGatherCPVarlenInnerAttention), [`VarlenMetadata`](attention.md#VarlenMetadata), [`InnerAttention`](attention.md#InnerAttention), [`UlyssesCPVarlenInnerAttention`](../../experiments/tpu/cp_attention.md#UlyssesCPVarlenInnerAttention), [`get_cuda_flash_attention_impl`](../../tools/utils.md#get_cuda_flash_attention_impl), [`cu_seq_q`](attention.md#VarlenMetadata.cu_seq_q), [`window_size`](attention.md#VarlenInnerAttention.Config.window_size), [`cu_seq_k`](attention.md#VarlenMetadata.cu_seq_k), [`max_k`](attention.md#VarlenMetadata.max_k), [`max_q`](attention.md#VarlenMetadata.max_q), [`varlen_attn`](attention.md#varlen_attn), [`varlen_attn_with_lse`](attention.md#varlen_attn_with_lse)
- used by: [`_build_muse_glimmer_attention`](../muse_glimmer/__init__.md#_build_muse_glimmer_attention), [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`_precompile_aot_fx_trace`](../../experiments/graph_trainer/precompile_main.md#_precompile_aot_fx_trace), [`preprocess_inputs`](../qwen3_5/model.md#Qwen35Model.preprocess_inputs), [`_build_model`](../../experiments/rl/actors/trainer.md#PolicyTrainer._build_model), [`preprocess_inputs`](../muse_glimmer/model.md#MuseGlimmerModel.preprocess_inputs), [`_validate_cuda_graphs`](../../trainer.md#Trainer.Config._validate_cuda_graphs), [`preprocess_inputs`](../deepseek_v3/mtp.md#MTPDecoder.preprocess_inputs), [`get_attention_masks`](decoder.md#Decoder.get_attention_masks), [`_tp_rank`](../../experiments/rl/actors/generator.md#VLLMGenerator._tp_rank), [`get_attention_config`](config_utils.md#get_attention_config), [`preprocess_inputs`](decoder.md#Decoder.preprocess_inputs), [`preprocess_inputs`](../kimi_k2_7/model.md#KimiK25Model.preprocess_inputs), [`get_attention_masks`](../muse_glimmer/model.md#MuseGlimmerModel.get_attention_masks), [`generate`](../../experiments/rl/generate.md#generate), [`get_attention_masks`](../gpt_oss/model.md#GptOssModel.get_attention_masks), [`forward`](../../experiments/tpu/cp_attention.md#KVAllGatherCPInnerAttention.forward), [`preprocess_inputs`](../kimi_k3/model.md#KimiK3Model.preprocess_inputs), [`forward`](../../experiments/tpu/cp_attention.md#UlyssesCPInnerAttention.forward), [`get_attention_masks`](../qwen3_5/model.md#Qwen35Model.get_attention_masks), [`get_attention_masks`](../kimi_k3/model.md#KimiK3Model.get_attention_masks), [`KVAllGatherCPVarlenInnerAttention`](../../experiments/tpu/cp_attention.md#KVAllGatherCPVarlenInnerAttention), [`InnerAttention`](attention.md#InnerAttention), [`_CP_INNER_ATTENTIONS`](../../experiments/tpu/cp_attention.md#_CP_INNER_ATTENTIONS), [`inner_attention`](../gpt_oss/model.md#Attention.Config.inner_attention), [`patch_varlen_attention`](../../experiments/tpu/rl_nc_ray/padding_packing_utils.md#patch_varlen_attention), [`Config`](../../experiments/tpu/cp_attention.md#KVAllGatherCPVarlenInnerAttention.Config), [`UlyssesCPVarlenInnerAttention`](../../experiments/tpu/cp_attention.md#UlyssesCPVarlenInnerAttention), [`__init__`](../../experiments/tpu/cp_attention.md#KVAllGatherCPInnerAttention.__init__), [`Config`](../../experiments/tpu/cp_attention.md#UlyssesCPVarlenInnerAttention.Config), [`_uses_sliding_window`](../../experiments/tpu/cp_attention.md#KVAllGatherCPInnerAttention._uses_sliding_window)  (2 test-only)

### <a id="VarlenInnerAttention.Config"></a>`VarlenInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/attention.py:139`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L139)
- signature: `class Config(InnerAttention.Config):`
- members:
  - <a id="VarlenInnerAttention.Config.window_size"></a>`window_size` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L140) — ---
- uses (calls/refs, reference-scoped): [`InnerAttention`](attention.md#InnerAttention), [`Config`](attention.md#InnerAttention.Config)
- used by: [`_build_muse_glimmer_attention`](../muse_glimmer/__init__.md#_build_muse_glimmer_attention), [`_make_gptoss_attn_config`](../gpt_oss/__init__.md#_make_gptoss_attn_config), [`_precompile_aot_fx_trace`](../../experiments/graph_trainer/precompile_main.md#_precompile_aot_fx_trace), [`preprocess_inputs`](../qwen3_5/model.md#Qwen35Model.preprocess_inputs), [`_build_model`](../../experiments/rl/actors/trainer.md#PolicyTrainer._build_model), [`preprocess_inputs`](../muse_glimmer/model.md#MuseGlimmerModel.preprocess_inputs), [`_validate_cuda_graphs`](../../trainer.md#Trainer.Config._validate_cuda_graphs), [`preprocess_inputs`](../deepseek_v3/mtp.md#MTPDecoder.preprocess_inputs), [`get_attention_masks`](decoder.md#Decoder.get_attention_masks), [`_tp_rank`](../../experiments/rl/actors/generator.md#VLLMGenerator._tp_rank), [`get_attention_config`](config_utils.md#get_attention_config), [`preprocess_inputs`](decoder.md#Decoder.preprocess_inputs), [`preprocess_inputs`](../kimi_k2_7/model.md#KimiK25Model.preprocess_inputs), [`get_attention_masks`](../muse_glimmer/model.md#MuseGlimmerModel.get_attention_masks), [`generate`](../../experiments/rl/generate.md#generate), [`get_attention_masks`](../gpt_oss/model.md#GptOssModel.get_attention_masks), [`preprocess_inputs`](../kimi_k3/model.md#KimiK3Model.preprocess_inputs), [`get_attention_masks`](../qwen3_5/model.md#Qwen35Model.get_attention_masks), [`get_attention_masks`](../kimi_k3/model.md#KimiK3Model.get_attention_masks), [`inner_attention`](../gpt_oss/model.md#Attention.Config.inner_attention), [`Config`](../../experiments/tpu/cp_attention.md#KVAllGatherCPVarlenInnerAttention.Config), [`window_size`](attention.md#VarlenInnerAttention.window_size), [`Config`](../../experiments/tpu/cp_attention.md#UlyssesCPVarlenInnerAttention.Config), [`__init__`](attention.md#VarlenInnerAttention.__init__)  (3 test-only)

### <a id="VarlenMetadata"></a>`VarlenMetadata`  ·  implements/extends NamedTuple
- def: [`torchtitan/models/common/attention.py:76`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L76)
- doc: Cumulative sequence positions for queries and keys/values.
- signature: `class VarlenMetadata(NamedTuple):`
- members:
  - <a id="VarlenMetadata.cu_seq_k"></a>`cu_seq_k` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L83)
  - <a id="VarlenMetadata.cu_seq_q"></a>`cu_seq_q` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L82)
  - <a id="VarlenMetadata.max_k"></a>`max_k` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L85)
  - <a id="VarlenMetadata.max_q"></a>`max_q` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L84)
- used by: [`AttentionMasksType`](attention.md#AttentionMasksType), [`forward`](../kimi_k3/kda.md#KDA.forward), [`forward`](../qwen3_5/gdn.md#GatedDeltaNet.forward), [`forward`](../../experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaNet.forward), [`create_varlen_metadata_for_document`](attention.md#create_varlen_metadata_for_document), [`forward`](attention.md#VarlenInnerAttention.forward), [`get_attention_masks`](../qwen3_5/model.md#Qwen35Model.get_attention_masks), [`annotate_deltanet_cu_seqlens`](../qwen3_5/sharding.md#annotate_deltanet_cu_seqlens), [`Qwen35AttentionMaskDict`](../qwen3_5/model.md#Qwen35AttentionMaskDict), [`KimiK3AttentionMaskDict`](../kimi_k3/model.md#KimiK3AttentionMaskDict)

## Functions
- <a id="get_causal_mask_mod._causal_mask"></a>`_causal_mask(b: torch.Tensor, h: torch.Tensor, q_idx: torch.Tensor, kv_idx: torch.Tensor)` — [`L502`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L502) — Causal mask that prevents attention to future tokens.
- <a id="get_fixed_block_mask_mod.blocked_mask_mod"></a>`blocked_mask_mod(b: torch.Tensor, h: torch.Tensor, q_idx: torch.Tensor, kv_idx: torch.Tensor)` — [`L589`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L589)
- <a id="create_attention_mask"></a>`create_attention_mask(*args, **kwargs)` — [`L637`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L637) — Create an attention mask using compiled create_block_mask.
- <a id="create_varlen_metadata_for_document"></a>`create_varlen_metadata_for_document(positions: torch.Tensor, *, padding_mask: torch.Tensor | None = None, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L642`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L642) — Creates cumulative sequence length indices needed for variable length attention.
- <a id="get_document_mask_mod.document_mask"></a>`document_mask(b: torch.Tensor, h: torch.Tensor, q_idx: torch.Tensor, kv_idx: torch.Tensor)` — [`L526`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L526)
- <a id="get_causal_mask_mod"></a>`get_causal_mask_mod()` — [`L495`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L495) — Returns a causal mask modifier for flex attention.
- <a id="get_document_mask_mod"></a>`get_document_mask_mod(positions: torch.Tensor)` — [`L511`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L511) — Creates a document mask that prevents attention across document boundaries.
- <a id="get_efficient_causal_mask_mod_for_packed_document"></a>`get_efficient_causal_mask_mod_for_packed_document(positions: torch.Tensor)` — [`L534`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L534) — Creates an efficient document mask to compose with a causal mask.
- <a id="get_fixed_block_mask_mod"></a>`get_fixed_block_mask_mod(fixed_block_size: int)` — [`L577`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L577) — Divide the input sequence into blocks and only allow attention within the same block.
- <a id="get_sliding_window_mask_mod"></a>`get_sliding_window_mask_mod(window_size: int)` — [`L603`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L603) — Creates a sliding window mask that only attends to tokens within a fixed window size.
- <a id="local_head_split"></a>`local_head_split(t: torch.Tensor, head_dim: int, *, dp_shard_dim: int = 0)` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L110)
- <a id="get_efficient_causal_mask_mod_for_packed_document.packed_document_mask"></a>`packed_document_mask(b: torch.Tensor, h: torch.Tensor, q_idx: torch.Tensor, kv_idx: torch.Tensor)` — [`L569`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L569)
- <a id="segment_ids_from_positions"></a>`segment_ids_from_positions(positions: torch.Tensor)` — [`L972`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L972) — Compute SplashAttention `segment_ids` from dataloader `positions`.
- <a id="get_sliding_window_mask_mod.sliding_window_mod"></a>`sliding_window_mod(b: torch.Tensor, h: torch.Tensor, q_idx: torch.Tensor, kv_idx: torch.Tensor)` — [`L622`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L622)
- <a id="varlen_attn"></a>`varlen_attn(*args, **kwargs)` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L96)
- <a id="varlen_attn_with_lse"></a>`varlen_attn_with_lse(*args, **kwargs)` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L106)

## Module values
- <a id="AttentionMasksType"></a>`AttentionMasksType` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L90) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- <a id="__all__"></a>`__all__` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L54)
- <a id="_compiled_create_block_mask"></a>`_compiled_create_block_mask` — [`L634`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/attention.py#L634)

