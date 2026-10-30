---
title: 'Module: torchtitan/models/kimi_k2_7/vision_encoder.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k2_7/vision_encoder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k2_7.vision_encoder`/
symbols:
  MoonViTEncoder.forward: MoonViTEncoder#forward().
  MoonViTEncoder.compute_position_embeddings: MoonViTEncoder#compute_position_embeddings().
  VisionProjector.forward: VisionProjector#forward().
  KimiK25VisionEncoder.Config: KimiK25VisionEncoder#Config#
  MoonViTEncoder: MoonViTEncoder#
  MoonViTEncoder.Config.final_norm: MoonViTEncoder#Config#final_norm.
  MoonViTEncoder.layers: MoonViTEncoder#layers.
  VisionRotaryEmbedding2D.Config: VisionRotaryEmbedding2D#Config#
  MoonViTEncoder.Config.rotary_pos_emb: MoonViTEncoder#Config#rotary_pos_emb.
  MoonViTEncoder.pos_embed: MoonViTEncoder#pos_embed.
  KimiK25VisionEncoder: KimiK25VisionEncoder#
  VisionProjector.Config: VisionProjector#Config#
  MoonViTEncoder.Config: MoonViTEncoder#Config#
  MoonViTEncoder.Config.patch_embed_proj: MoonViTEncoder#Config#patch_embed_proj.
  MoonViTEncoder.Config.block: MoonViTEncoder#Config#block.
  VisionRotaryEmbedding2D: VisionRotaryEmbedding2D#
  VisionRotaryEmbedding2D.inv_freq: VisionRotaryEmbedding2D#inv_freq.
  VisionRotaryEmbedding2D.forward: VisionRotaryEmbedding2D#forward().
  VisionRotaryEmbedding2D._compute_inv_freq: VisionRotaryEmbedding2D#_compute_inv_freq().
  VisionProjector.Config.pre_norm: VisionProjector#Config#pre_norm.
  VisionProjector.Config.linear_1: VisionProjector#Config#linear_1.
  VisionProjector.Config.linear_2: VisionProjector#Config#linear_2.
  MoonViTEncoder.rotary_pos_emb: MoonViTEncoder#rotary_pos_emb.
  _compute_learned_pos_embeds: _compute_learned_pos_embeds().
  _compute_2d_rope_cache: _compute_2d_rope_cache().
  VisionRotaryEmbedding2D.theta: VisionRotaryEmbedding2D#theta.
  VisionProjector.Config.act_fn: VisionProjector#Config#act_fn.
  VisionProjector.pre_norm: VisionProjector#pre_norm.
  VisionProjector.linear_1: VisionProjector#linear_1.
  VisionProjector.linear_2: VisionProjector#linear_2.
  VisionProjector.act_fn: VisionProjector#act_fn.
  MoonViTEncoder.Config.projector: MoonViTEncoder#Config#projector.
  MoonViTEncoder.patch_embed: MoonViTEncoder#patch_embed.
  MoonViTEncoder.final_norm: MoonViTEncoder#final_norm.
  MoonViTEncoder.projector: MoonViTEncoder#projector.
  KimiK25VisionEncoder.Config.final_norm: KimiK25VisionEncoder#Config#final_norm.
  VisionProjector: VisionProjector#
  VisionRotaryEmbedding2D.Config.head_dim: VisionRotaryEmbedding2D#Config#head_dim.
  VisionRotaryEmbedding2D.__init__: VisionRotaryEmbedding2D#__init__().
  VisionRotaryEmbedding2D.head_dim: VisionRotaryEmbedding2D#head_dim.
  MoonViTEncoder.merge_kernel_size: MoonViTEncoder#merge_kernel_size.
  MoonViTEncoder._cached_freq_table: MoonViTEncoder#_cached_freq_table.
  VisionProjector.vt_hidden_size: VisionProjector#vt_hidden_size.
  VisionProjector.merged_dim: VisionProjector#merged_dim.
  MoonViTEncoder.interpolation_mode: MoonViTEncoder#interpolation_mode.
  KimiK25VisionEncoder.Config.num_heads: KimiK25VisionEncoder#Config#num_heads.
  VisionRotaryEmbedding2D._init_self_buffers: VisionRotaryEmbedding2D#_init_self_buffers().
  VisionProjector.__init__: VisionProjector#__init__().
  MoonViTEncoder.__init__: MoonViTEncoder#__init__().
  VisionRotaryEmbedding2D.Config.theta: VisionRotaryEmbedding2D#Config#theta.
  VisionProjector.Config.vt_hidden_size: VisionProjector#Config#vt_hidden_size.
  VisionProjector.Config.merged_dim: VisionProjector#Config#merged_dim.
  MoonViTEncoder.Config.dim: MoonViTEncoder#Config#dim.
  MoonViTEncoder.Config.num_layers: MoonViTEncoder#Config#num_layers.
  MoonViTEncoder.Config.init_pos_emb_height: MoonViTEncoder#Config#init_pos_emb_height.
  MoonViTEncoder.Config.init_pos_emb_width: MoonViTEncoder#Config#init_pos_emb_width.
  MoonViTEncoder.Config.interpolation_mode: MoonViTEncoder#Config#interpolation_mode.
  KimiK25VisionEncoder.Config.patch_size: KimiK25VisionEncoder#Config#patch_size.
  KimiK25VisionEncoder.Config.in_channels: KimiK25VisionEncoder#Config#in_channels.
  _get_temporal_pos_embed: _get_temporal_pos_embed().
  _tpool_patch_merger: _tpool_patch_merger().
  MoonViTEncoder.Config.merge_kernel_size: MoonViTEncoder#Config#merge_kernel_size.
  KimiK25VisionEncoder.Config.dim: KimiK25VisionEncoder#Config#dim.
  KimiK25VisionEncoder.Config.num_layers: KimiK25VisionEncoder#Config#num_layers.
  KimiK25VisionEncoder.Config.merge_kernel_size: KimiK25VisionEncoder#Config#merge_kernel_size.
  KimiK25VisionEncoder.Config.text_hidden_size: KimiK25VisionEncoder#Config#text_hidden_size.
  KimiK25VisionEncoder.Config.init_pos_emb_height: KimiK25VisionEncoder#Config#init_pos_emb_height.
  KimiK25VisionEncoder.Config.init_pos_emb_width: KimiK25VisionEncoder#Config#init_pos_emb_width.
  KimiK25VisionEncoder.Config.projector: KimiK25VisionEncoder#Config#projector.
  MoonViTEncoder.config: MoonViTEncoder#config.
  KimiK25VisionEncoder.Config.interpolation_mode: KimiK25VisionEncoder#Config#interpolation_mode.
---
# Module: [`torchtitan/models/kimi_k2_7/vision_encoder.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py)

## Classes
### <a id="KimiK25VisionEncoder"></a>`KimiK25VisionEncoder`  ·  implements/extends MoonViTEncoder
- def: [`torchtitan/models/kimi_k2_7/vision_encoder.py:472`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L472) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- doc: MoonViT3d vision tower + multimodal projector for Kimi K2.5.
- signature: `class KimiK25VisionEncoder(MoonViTEncoder):`
- uses (calls/refs, reference-scoped): [`MoonViTEncoder`](vision_encoder.md#MoonViTEncoder)
- used by: [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`_moonlight_16b_a3b_config`](__init__.md#_moonlight_16b_a3b_config), [`vision_encoder`](model.md#KimiK25Model.Config.vision_encoder), [`MoonViTEncoder`](vision_encoder.md#MoonViTEncoder)

### <a id="KimiK25VisionEncoder.Config"></a>`KimiK25VisionEncoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k2_7/vision_encoder.py:476`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L476) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- signature: `class Config(MoonViTEncoder.Config):`
- members:
  - <a id="KimiK25VisionEncoder.Config.dim"></a>`dim` — [`L477`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L477)
  - <a id="KimiK25VisionEncoder.Config.final_norm"></a>`final_norm` — [`L490`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L490)
  - <a id="KimiK25VisionEncoder.Config.in_channels"></a>`in_channels` — [`L482`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L482)
  - <a id="KimiK25VisionEncoder.Config.init_pos_emb_height"></a>`init_pos_emb_height` — [`L486`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L486)
  - <a id="KimiK25VisionEncoder.Config.init_pos_emb_width"></a>`init_pos_emb_width` — [`L487`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L487)
  - <a id="KimiK25VisionEncoder.Config.interpolation_mode"></a>`interpolation_mode` — [`L488`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L488)
  - <a id="KimiK25VisionEncoder.Config.merge_kernel_size"></a>`merge_kernel_size` — [`L483`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L483)
  - <a id="KimiK25VisionEncoder.Config.num_heads"></a>`num_heads` — [`L479`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L479)
  - <a id="KimiK25VisionEncoder.Config.num_layers"></a>`num_layers` — [`L478`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L478)
  - <a id="KimiK25VisionEncoder.Config.patch_size"></a>`patch_size` — [`L481`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L481)
  - <a id="KimiK25VisionEncoder.Config.projector"></a>`projector` — [`L491`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L491)
  - <a id="KimiK25VisionEncoder.Config.text_hidden_size"></a>`text_hidden_size` — [`L484`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L484)
- uses (calls/refs, reference-scoped): [`LayerNorm`](../common/nn_modules.md#LayerNorm), [`Config`](../common/nn_modules.md#LayerNorm.Config), [`MoonViTEncoder`](vision_encoder.md#MoonViTEncoder), [`Config`](vision_encoder.md#MoonViTEncoder.Config), [`Config`](vision_encoder.md#VisionProjector.Config), [`VisionProjector`](vision_encoder.md#VisionProjector)
- used by: [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`_moonlight_16b_a3b_config`](__init__.md#_moonlight_16b_a3b_config), [`vision_encoder`](model.md#KimiK25Model.Config.vision_encoder), [`update_from_config`](model.md#KimiK25Model.Config.update_from_config), [`patch_size`](state_dict_adapter.md#KimiK25StateDictAdapter.patch_size), [`in_channels`](state_dict_adapter.md#KimiK25StateDictAdapter.in_channels)

### <a id="MoonViTEncoder"></a>`MoonViTEncoder`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k2_7/vision_encoder.py:328`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L328) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- doc: MoonViT3d vision tower + multimodal projector.
- signature: `class MoonViTEncoder(Module):`
- members:
  - <a id="MoonViTEncoder.compute_position_embeddings"></a>`compute_position_embeddings(self, grids: list[list[int]])` — [`L370`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L370) — Compute both position embeddings for packed visual patches.
  - <a id="MoonViTEncoder.forward"></a>`forward(self, pixel_values: torch.Tensor, *, grid_thw: torch.Tensor)` — [`L404`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L404) — Encode packed image or video patches. — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
  - <a id="MoonViTEncoder.config"></a>`config` — [`L351`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L351)
  - <a id="MoonViTEncoder.final_norm"></a>`final_norm` — [`L367`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L367)
  - <a id="MoonViTEncoder.interpolation_mode"></a>`interpolation_mode` — [`L353`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L353)
  - <a id="MoonViTEncoder.layers"></a>`layers` — [`L364`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L364)
  - <a id="MoonViTEncoder.merge_kernel_size"></a>`merge_kernel_size` — [`L352`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L352)
  - <a id="MoonViTEncoder.patch_embed"></a>`patch_embed` — [`L355`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L355)
  - <a id="MoonViTEncoder.pos_embed"></a>`pos_embed` — [`L357`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L357)
  - <a id="MoonViTEncoder.projector"></a>`projector` — [`L368`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L368)
  - <a id="MoonViTEncoder.rotary_pos_emb"></a>`rotary_pos_emb` — [`L362`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L362) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- protocol/private: <a id="MoonViTEncoder.__init__"></a>`__init__`[`L349`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L349), <a id="MoonViTEncoder._cached_freq_table"></a>`_cached_freq_table`[`L363`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L363)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`ComplexRoPE`](../common/rope.md#ComplexRoPE), [`ModuleDict`](../../protocols/module.md#ModuleDict), [`create_block_diagonal_mask`](../common/vision_encoder.md#create_block_diagonal_mask), [`final_norm`](vision_encoder.md#MoonViTEncoder.Config.final_norm), [`KimiK3VisionEncoder`](../kimi_k3/vision_encoder.md#KimiK3VisionEncoder), [`apply_rotary_emb`](../common/rope.md#ComplexRoPE.apply_rotary_emb), [`rotary_pos_emb`](vision_encoder.md#MoonViTEncoder.Config.rotary_pos_emb), [`KimiK25VisionEncoder`](vision_encoder.md#KimiK25VisionEncoder), [`Config`](vision_encoder.md#MoonViTEncoder.Config), [`block`](vision_encoder.md#MoonViTEncoder.Config.block), [`patch_embed_proj`](vision_encoder.md#MoonViTEncoder.Config.patch_embed_proj), [`_compute_2d_rope_cache`](vision_encoder.md#_compute_2d_rope_cache), [`_compute_learned_pos_embeds`](vision_encoder.md#_compute_learned_pos_embeds), [`projector`](vision_encoder.md#MoonViTEncoder.Config.projector), [`dim`](vision_encoder.md#MoonViTEncoder.Config.dim), [`init_pos_emb_height`](vision_encoder.md#MoonViTEncoder.Config.init_pos_emb_height), [`init_pos_emb_width`](vision_encoder.md#MoonViTEncoder.Config.init_pos_emb_width), [`interpolation_mode`](vision_encoder.md#MoonViTEncoder.Config.interpolation_mode), [`num_layers`](vision_encoder.md#MoonViTEncoder.Config.num_layers), [`_tpool_patch_merger`](vision_encoder.md#_tpool_patch_merger), [`merge_kernel_size`](vision_encoder.md#MoonViTEncoder.Config.merge_kernel_size)
- used by: [`Module`](../../protocols/module.md#Module), [`Config`](../kimi_k3/vision_encoder.md#KimiK3VisionEncoder.Config), [`Config`](vision_encoder.md#KimiK25VisionEncoder.Config), [`KimiK3VisionEncoder`](../kimi_k3/vision_encoder.md#KimiK3VisionEncoder), [`KimiK25VisionEncoder`](vision_encoder.md#KimiK25VisionEncoder)

### <a id="MoonViTEncoder.Config"></a>`MoonViTEncoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k2_7/vision_encoder.py:332`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L332)
- signature: `class Config(Module.Config):`
- members:
  - <a id="MoonViTEncoder.Config.block"></a>`block` — [`L345`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L345)
  - <a id="MoonViTEncoder.Config.dim"></a>`dim` — [`L333`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L333)
  - <a id="MoonViTEncoder.Config.final_norm"></a>`final_norm` — [`L346`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L346)
  - <a id="MoonViTEncoder.Config.init_pos_emb_height"></a>`init_pos_emb_height` — [`L338`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L338)
  - <a id="MoonViTEncoder.Config.init_pos_emb_width"></a>`init_pos_emb_width` — [`L339`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L339)
  - <a id="MoonViTEncoder.Config.interpolation_mode"></a>`interpolation_mode` — [`L340`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L340)
  - <a id="MoonViTEncoder.Config.merge_kernel_size"></a>`merge_kernel_size` — [`L335`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L335)
  - <a id="MoonViTEncoder.Config.num_layers"></a>`num_layers` — [`L334`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L334)
  - <a id="MoonViTEncoder.Config.patch_embed_proj"></a>`patch_embed_proj` — [`L343`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L343)
  - <a id="MoonViTEncoder.Config.projector"></a>`projector` — [`L347`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L347)
  - <a id="MoonViTEncoder.Config.rotary_pos_emb"></a>`rotary_pos_emb` — [`L344`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L344) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../../protocols/module.md#Module.Config), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`LayerNorm`](../common/nn_modules.md#LayerNorm), [`Config`](../common/nn_modules.md#LayerNorm.Config), [`VisionTransformerBlock`](../common/vision_encoder.md#VisionTransformerBlock), [`Config`](../common/vision_encoder.md#VisionTransformerBlock.Config), [`Config`](vision_encoder.md#VisionRotaryEmbedding2D.Config), [`VisionRotaryEmbedding2D`](vision_encoder.md#VisionRotaryEmbedding2D)
- used by: [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`_set_vision_buffer_sharding`](../kimi_k3/sharding.md#_set_vision_buffer_sharding), [`Config`](../kimi_k3/vision_encoder.md#KimiK3VisionEncoder.Config), [`Config`](vision_encoder.md#KimiK25VisionEncoder.Config), [`layers`](vision_encoder.md#MoonViTEncoder.layers), [`pos_embed`](vision_encoder.md#MoonViTEncoder.pos_embed), [`rotary_pos_emb`](vision_encoder.md#MoonViTEncoder.rotary_pos_emb), [`final_norm`](vision_encoder.md#MoonViTEncoder.final_norm), [`patch_embed`](vision_encoder.md#MoonViTEncoder.patch_embed), [`projector`](vision_encoder.md#MoonViTEncoder.projector), [`merge_kernel_size`](vision_encoder.md#MoonViTEncoder.merge_kernel_size), [`interpolation_mode`](vision_encoder.md#MoonViTEncoder.interpolation_mode), [`__init__`](vision_encoder.md#MoonViTEncoder.__init__)

### <a id="VisionProjector"></a>`VisionProjector`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k2_7/vision_encoder.py:287`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L287)
- doc: Project merged vision features to the language-model hidden size.
- signature: `class VisionProjector(Module):`
- members:
  - <a id="VisionProjector.forward"></a>`forward(self, merged_MK: torch.Tensor)` — [`L314`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L314) — Project packed merged tokens ``(M, kh*kw*vt_hidden_size)``.
  - <a id="VisionProjector.act_fn"></a>`act_fn` — [`L312`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L312)
  - <a id="VisionProjector.linear_1"></a>`linear_1` — [`L310`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L310)
  - <a id="VisionProjector.linear_2"></a>`linear_2` — [`L311`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L311)
  - <a id="VisionProjector.merged_dim"></a>`merged_dim` — [`L308`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L308)
  - <a id="VisionProjector.pre_norm"></a>`pre_norm` — [`L309`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L309)
  - <a id="VisionProjector.vt_hidden_size"></a>`vt_hidden_size` — [`L307`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L307)
- protocol/private: <a id="VisionProjector.__init__"></a>`__init__`[`L305`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L305)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](vision_encoder.md#VisionProjector.Config), [`linear_1`](vision_encoder.md#VisionProjector.Config.linear_1), [`linear_2`](vision_encoder.md#VisionProjector.Config.linear_2), [`pre_norm`](vision_encoder.md#VisionProjector.Config.pre_norm), [`act_fn`](vision_encoder.md#VisionProjector.Config.act_fn), [`merged_dim`](vision_encoder.md#VisionProjector.Config.merged_dim), [`vt_hidden_size`](vision_encoder.md#VisionProjector.Config.vt_hidden_size)
- used by: [`Module`](../../protocols/module.md#Module), [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`Config`](vision_encoder.md#KimiK25VisionEncoder.Config)

### <a id="VisionProjector.Config"></a>`VisionProjector.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k2_7/vision_encoder.py:297`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L297)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VisionProjector.Config.act_fn"></a>`act_fn` — [`L303`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L303)
  - <a id="VisionProjector.Config.linear_1"></a>`linear_1` — [`L301`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L301)
  - <a id="VisionProjector.Config.linear_2"></a>`linear_2` — [`L302`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L302)
  - <a id="VisionProjector.Config.merged_dim"></a>`merged_dim` — [`L299`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L299)
  - <a id="VisionProjector.Config.pre_norm"></a>`pre_norm` — [`L300`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L300)
  - <a id="VisionProjector.Config.vt_hidden_size"></a>`vt_hidden_size` — [`L298`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L298)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`LayerNorm`](../common/nn_modules.md#LayerNorm), [`GELU`](../common/nn_modules.md#GELU), [`Config`](../common/nn_modules.md#LayerNorm.Config), [`Config`](../common/nn_modules.md#GELU.Config)
- used by: [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`Config`](vision_encoder.md#KimiK25VisionEncoder.Config), [`act_fn`](vision_encoder.md#VisionProjector.act_fn), [`linear_1`](vision_encoder.md#VisionProjector.linear_1), [`linear_2`](vision_encoder.md#VisionProjector.linear_2), [`pre_norm`](vision_encoder.md#VisionProjector.pre_norm), [`merged_dim`](vision_encoder.md#VisionProjector.merged_dim), [`vt_hidden_size`](vision_encoder.md#VisionProjector.vt_hidden_size), [`__init__`](vision_encoder.md#VisionProjector.__init__)

### <a id="VisionRotaryEmbedding2D"></a>`VisionRotaryEmbedding2D`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k2_7/vision_encoder.py:234`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L234) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- doc: 2D rotary position embedding for the vision tower.
- signature: `class VisionRotaryEmbedding2D(Module):`
- members:
  - <a id="VisionRotaryEmbedding2D._init_self_buffers"></a>`_init_self_buffers(self, *, buffer_device: torch.device | None = None)` — [`L271`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L271) — Re-compute inv_freq on the target device after to_empty().
  - <a id="VisionRotaryEmbedding2D.forward"></a>`forward(self, seqlen: int)` — [`L276`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L276) — Frequency table ``(seqlen, head_dim/4)`` for positions ``[0, seqlen)``.
  - <a id="VisionRotaryEmbedding2D.head_dim"></a>`head_dim` — [`L256`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L256)
  - <a id="VisionRotaryEmbedding2D.inv_freq"></a>`inv_freq` — [`L274`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L274)
  - <a id="VisionRotaryEmbedding2D.theta"></a>`theta` — [`L257`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L257)
- protocol/private: <a id="VisionRotaryEmbedding2D.__init__"></a>`__init__`[`L250`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L250), <a id="VisionRotaryEmbedding2D._compute_inv_freq"></a>`_compute_inv_freq`[`L260`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L260)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`Config`](vision_encoder.md#VisionRotaryEmbedding2D.Config), [`_maybe_wrap_positions`](../common/rope.md#_maybe_wrap_positions), [`head_dim`](vision_encoder.md#VisionRotaryEmbedding2D.Config.head_dim), [`theta`](vision_encoder.md#VisionRotaryEmbedding2D.Config.theta)
- used by: [`Module`](../../protocols/module.md#Module), [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`_init_self_buffers`](../../protocols/module.md#Module._init_self_buffers), [`rotary_pos_emb`](vision_encoder.md#MoonViTEncoder.Config.rotary_pos_emb)

### <a id="VisionRotaryEmbedding2D.Config"></a>`VisionRotaryEmbedding2D.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k2_7/vision_encoder.py:246`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L246) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VisionRotaryEmbedding2D.Config.head_dim"></a>`head_dim` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L247)
  - <a id="VisionRotaryEmbedding2D.Config.theta"></a>`theta` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L248)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`rotary_pos_emb`](vision_encoder.md#MoonViTEncoder.Config.rotary_pos_emb), [`theta`](vision_encoder.md#VisionRotaryEmbedding2D.theta), [`__init__`](vision_encoder.md#VisionRotaryEmbedding2D.__init__), [`head_dim`](vision_encoder.md#VisionRotaryEmbedding2D.head_dim)

## Functions
- <a id="_compute_2d_rope_cache"></a>`_compute_2d_rope_cache(freq_table: torch.Tensor, grids: list[list[int]], head_dim: int)` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L129) — Compute the packed 2D-RoPE complex ``freqs_cis`` cache in raster order.
- <a id="_compute_learned_pos_embeds"></a>`_compute_learned_pos_embeds(pos_embed: torch.Tensor, grids: list[list[int]], interpolation_mode: str)` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L66) — Interpolated learnable 2D spatial pos-emb + fixed sinusoidal temporal.
- <a id="_get_temporal_pos_embed"></a>`_get_temporal_pos_embed(num_frames: int, embed_dim: int, *, base: float = 10000, device: torch.device | None = None)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L39) — Fixed 1D sinusoidal embeddings for the temporal axis (video frames).
- <a id="_tpool_patch_merger"></a>`_tpool_patch_merger(hidden_TD: torch.Tensor, grids: list[list[int]], merge_kernel_size: tuple[int, int])` — [`L191`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/vision_encoder.py#L191) — Temporal mean pooling + spatial merge over packed visual items.

