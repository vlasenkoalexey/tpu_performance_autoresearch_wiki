---
title: 'Module: torchtitan/models/qwen3_5/vision_encoder.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3_5/vision_encoder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3_5.vision_encoder`/
symbols:
  Qwen35VisionEncoder.compute_position_embeddings: Qwen35VisionEncoder#compute_position_embeddings().
  Qwen35VisionEncoder.forward: Qwen35VisionEncoder#forward().
  PatchMerger.forward: PatchMerger#forward().
  Qwen35VisionEncoder.layers: Qwen35VisionEncoder#layers.
  VisionRotaryEmbedding.inv_freq: VisionRotaryEmbedding#inv_freq.
  Qwen35VisionEncoder.Config: Qwen35VisionEncoder#Config#
  Qwen35VisionEncoder: Qwen35VisionEncoder#
  PatchMerger.Config.act_fn: PatchMerger#Config#act_fn.
  VisionRotaryEmbedding.Config: VisionRotaryEmbedding#Config#
  PatchMerger.Config: PatchMerger#Config#
  PatchMerger.Config.norm: PatchMerger#Config#norm.
  PatchMerger.Config.fc1: PatchMerger#Config#fc1.
  PatchMerger.Config.fc2: PatchMerger#Config#fc2.
  Qwen35VisionEncoder.Config.patch_embed_proj: Qwen35VisionEncoder#Config#patch_embed_proj.
  Qwen35VisionEncoder.Config.block: Qwen35VisionEncoder#Config#block.
  Qwen35VisionEncoder.Config.rotary_pos_emb: Qwen35VisionEncoder#Config#rotary_pos_emb.
  Qwen35VisionEncoder.Config.merger: Qwen35VisionEncoder#Config#merger.
  VisionRotaryEmbedding.forward: VisionRotaryEmbedding#forward().
  Qwen35VisionEncoder._cached_freq_table: Qwen35VisionEncoder#_cached_freq_table.
  VisionRotaryEmbedding.theta: VisionRotaryEmbedding#theta.
  PatchMerger.norm: PatchMerger#norm.
  PatchMerger.linear_fc1: PatchMerger#linear_fc1.
  PatchMerger.act_fn: PatchMerger#act_fn.
  PatchMerger.linear_fc2: PatchMerger#linear_fc2.
  Qwen35VisionEncoder.patch_embed: Qwen35VisionEncoder#patch_embed.
  Qwen35VisionEncoder.pos_embed: Qwen35VisionEncoder#pos_embed.
  Qwen35VisionEncoder.rotary_pos_emb: Qwen35VisionEncoder#rotary_pos_emb.
  Qwen35VisionEncoder.merger: Qwen35VisionEncoder#merger.
  VisionRotaryEmbedding: VisionRotaryEmbedding#
  PatchMerger: PatchMerger#
  Qwen35VisionEncoder.spatial_merge_size: Qwen35VisionEncoder#spatial_merge_size.
  _compute_2d_rope_cache: _compute_2d_rope_cache().
  VisionRotaryEmbedding.dim: VisionRotaryEmbedding#dim.
  VisionRotaryEmbedding.Config.dim: VisionRotaryEmbedding#Config#dim.
  Qwen35VisionEncoder.Config.dim: Qwen35VisionEncoder#Config#dim.
  Qwen35VisionEncoder.Config.spatial_merge_size: Qwen35VisionEncoder#Config#spatial_merge_size.
  Qwen35VisionEncoder.Config.num_position_embeddings: Qwen35VisionEncoder#Config#num_position_embeddings.
  _compute_learned_pos_embeds: _compute_learned_pos_embeds().
  PatchMerger.merged_hidden_size: PatchMerger#merged_hidden_size.
  Qwen35VisionEncoder.num_grid_per_side: Qwen35VisionEncoder#num_grid_per_side.
  VisionRotaryEmbedding.Config.theta: VisionRotaryEmbedding#Config#theta.
  Qwen35VisionEncoder.Config.patch_size: Qwen35VisionEncoder#Config#patch_size.
  Qwen35VisionEncoder.config: Qwen35VisionEncoder#config.
  VisionRotaryEmbedding.__init__: VisionRotaryEmbedding#__init__().
  VisionRotaryEmbedding._init_self_buffers: VisionRotaryEmbedding#_init_self_buffers().
  PatchMerger.__init__: PatchMerger#__init__().
  PatchMerger.spatial_merge_size: PatchMerger#spatial_merge_size.
  Qwen35VisionEncoder.__init__: Qwen35VisionEncoder#__init__().
  Qwen35VisionEncoder.spatial_merge_unit: Qwen35VisionEncoder#spatial_merge_unit.
  Qwen35VisionEncoder.num_position_embeddings: Qwen35VisionEncoder#num_position_embeddings.
  PatchMerger.Config.spatial_merge_size: PatchMerger#Config#spatial_merge_size.
  PatchMerger.Config.merged_hidden_size: PatchMerger#Config#merged_hidden_size.
  Qwen35VisionEncoder.Config.num_layers: Qwen35VisionEncoder#Config#num_layers.
  Qwen35VisionEncoder.Config.num_heads: Qwen35VisionEncoder#Config#num_heads.
  Qwen35VisionEncoder.Config.temporal_patch_size: Qwen35VisionEncoder#Config#temporal_patch_size.
  Qwen35VisionEncoder.Config.in_channels: Qwen35VisionEncoder#Config#in_channels.
---
# Module: [`torchtitan/models/qwen3_5/vision_encoder.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py)

## Classes
### <a id="PatchMerger"></a>`PatchMerger`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/vision_encoder.py:265`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L265)
- doc: Merge spatial patches to reduce sequence length.
- signature: `class PatchMerger(Module):`
- members:
  - <a id="PatchMerger.forward"></a>`forward(self, x_TD: torch.Tensor)` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L293) — Merge spatial patches and project to output dimension.
  - <a id="PatchMerger.act_fn"></a>`act_fn` — [`L290`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L290)
  - <a id="PatchMerger.linear_fc1"></a>`linear_fc1` — [`L289`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L289)
  - <a id="PatchMerger.linear_fc2"></a>`linear_fc2` — [`L291`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L291)
  - <a id="PatchMerger.merged_hidden_size"></a>`merged_hidden_size` — [`L286`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L286)
  - <a id="PatchMerger.norm"></a>`norm` — [`L288`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L288)
  - <a id="PatchMerger.spatial_merge_size"></a>`spatial_merge_size` — [`L285`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L285)
- protocol/private: <a id="PatchMerger.__init__"></a>`__init__`[`L283`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L283)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`act_fn`](vision_encoder.md#PatchMerger.Config.act_fn), [`Config`](vision_encoder.md#PatchMerger.Config), [`fc1`](vision_encoder.md#PatchMerger.Config.fc1), [`fc2`](vision_encoder.md#PatchMerger.Config.fc2), [`norm`](vision_encoder.md#PatchMerger.Config.norm), [`merged_hidden_size`](vision_encoder.md#PatchMerger.Config.merged_hidden_size), [`spatial_merge_size`](vision_encoder.md#PatchMerger.Config.spatial_merge_size)
- used by: [`Module`](../../protocols/module.md#Module), [`_qwen35_vision_encoder_config`](__init__.md#_qwen35_vision_encoder_config), [`merger`](vision_encoder.md#Qwen35VisionEncoder.Config.merger)

### <a id="PatchMerger.Config"></a>`PatchMerger.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/vision_encoder.py:273`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L273)
- signature: `class Config(Module.Config):`
- members:
  - <a id="PatchMerger.Config.act_fn"></a>`act_fn` — [`L278`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L278)
  - <a id="PatchMerger.Config.fc1"></a>`fc1` — [`L277`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L277)
  - <a id="PatchMerger.Config.fc2"></a>`fc2` — [`L281`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L281)
  - <a id="PatchMerger.Config.merged_hidden_size"></a>`merged_hidden_size` — [`L275`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L275)
  - <a id="PatchMerger.Config.norm"></a>`norm` — [`L276`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L276)
  - <a id="PatchMerger.Config.spatial_merge_size"></a>`spatial_merge_size` — [`L274`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L274)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`LayerNorm`](../common/nn_modules.md#LayerNorm), [`GELU`](../common/nn_modules.md#GELU), [`Config`](../common/nn_modules.md#LayerNorm.Config), [`Config`](../common/nn_modules.md#GELU.Config), [`approximate`](../common/nn_modules.md#GELU.Config.approximate)
- used by: [`_qwen35_vision_encoder_config`](__init__.md#_qwen35_vision_encoder_config), [`_set_vision_encoder_sharding`](sharding.md#_set_vision_encoder_sharding), [`merger`](vision_encoder.md#Qwen35VisionEncoder.Config.merger), [`act_fn`](vision_encoder.md#PatchMerger.act_fn), [`linear_fc1`](vision_encoder.md#PatchMerger.linear_fc1), [`linear_fc2`](vision_encoder.md#PatchMerger.linear_fc2), [`norm`](vision_encoder.md#PatchMerger.norm), [`merged_hidden_size`](vision_encoder.md#PatchMerger.merged_hidden_size), [`__init__`](vision_encoder.md#PatchMerger.__init__), [`spatial_merge_size`](vision_encoder.md#PatchMerger.spatial_merge_size)

### <a id="Qwen35VisionEncoder"></a>`Qwen35VisionEncoder`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/vision_encoder.py:308`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L308)
- doc: Qwen3.5 Vision Encoder with FlexInnerAttention.
- signature: `class Qwen35VisionEncoder(Module):`
- members:
  - <a id="Qwen35VisionEncoder.compute_position_embeddings"></a>`compute_position_embeddings(self, grids: list[list[int]])` — [`L360`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L360) — Compute packed learned position embeddings and RoPE caches.
  - <a id="Qwen35VisionEncoder.forward"></a>`forward(self, pixel_values: torch.Tensor, *, grid_thw: torch.Tensor)` — [`L411`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L411) — Forward pass of the vision encoder.
  - <a id="Qwen35VisionEncoder.config"></a>`config` — [`L337`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L337)
  - <a id="Qwen35VisionEncoder.layers"></a>`layers` — [`L354`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L354)
  - <a id="Qwen35VisionEncoder.merger"></a>`merger` — [`L358`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L358)
  - <a id="Qwen35VisionEncoder.num_grid_per_side"></a>`num_grid_per_side` — [`L349`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L349)
  - <a id="Qwen35VisionEncoder.num_position_embeddings"></a>`num_position_embeddings` — [`L345`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L345)
  - <a id="Qwen35VisionEncoder.patch_embed"></a>`patch_embed` — [`L342`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L342)
  - <a id="Qwen35VisionEncoder.pos_embed"></a>`pos_embed` — [`L346`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L346)
  - <a id="Qwen35VisionEncoder.rotary_pos_emb"></a>`rotary_pos_emb` — [`L351`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L351)
  - <a id="Qwen35VisionEncoder.spatial_merge_size"></a>`spatial_merge_size` — [`L338`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L338)
  - <a id="Qwen35VisionEncoder.spatial_merge_unit"></a>`spatial_merge_unit` — [`L339`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L339)
- protocol/private: <a id="Qwen35VisionEncoder.__init__"></a>`__init__`[`L335`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L335), <a id="Qwen35VisionEncoder._cached_freq_table"></a>`_cached_freq_table`[`L352`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L352)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`CosSinRoPE`](../common/rope.md#CosSinRoPE), [`ModuleDict`](../../protocols/module.md#ModuleDict), [`apply_rotary_emb`](../common/rope.md#CosSinRoPE.apply_rotary_emb), [`create_block_diagonal_mask`](../common/vision_encoder.md#create_block_diagonal_mask), [`Config`](vision_encoder.md#Qwen35VisionEncoder.Config), [`block`](vision_encoder.md#Qwen35VisionEncoder.Config.block), [`merger`](vision_encoder.md#Qwen35VisionEncoder.Config.merger), [`patch_embed_proj`](vision_encoder.md#Qwen35VisionEncoder.Config.patch_embed_proj), [`rotary_pos_emb`](vision_encoder.md#Qwen35VisionEncoder.Config.rotary_pos_emb), [`_compute_2d_rope_cache`](vision_encoder.md#_compute_2d_rope_cache), [`dim`](vision_encoder.md#Qwen35VisionEncoder.Config.dim), [`num_position_embeddings`](vision_encoder.md#Qwen35VisionEncoder.Config.num_position_embeddings), [`spatial_merge_size`](vision_encoder.md#Qwen35VisionEncoder.Config.spatial_merge_size), [`_compute_learned_pos_embeds`](vision_encoder.md#_compute_learned_pos_embeds), [`num_heads`](vision_encoder.md#Qwen35VisionEncoder.Config.num_heads), [`num_layers`](vision_encoder.md#Qwen35VisionEncoder.Config.num_layers)
- used by: [`Module`](../../protocols/module.md#Module), [`_qwen35_vision_encoder_config`](__init__.md#_qwen35_vision_encoder_config), [`_set_vision_encoder_sharding`](sharding.md#_set_vision_encoder_sharding), [`TP`](sharding.md#TP), [`vision_encoder`](model.md#Qwen35Model.Config.vision_encoder)

### <a id="Qwen35VisionEncoder.Config"></a>`Qwen35VisionEncoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/vision_encoder.py:315`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L315)
- doc: Configuration for Qwen3.5 Vision Encoder (ViT).
- signature: `class Config(Module.Config):`
- members:
  - <a id="Qwen35VisionEncoder.Config.block"></a>`block` — [`L331`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L331)
  - <a id="Qwen35VisionEncoder.Config.dim"></a>`dim` — [`L318`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L318)
  - <a id="Qwen35VisionEncoder.Config.in_channels"></a>`in_channels` — [`L324`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L324)
  - <a id="Qwen35VisionEncoder.Config.merger"></a>`merger` — [`L333`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L333)
  - <a id="Qwen35VisionEncoder.Config.num_heads"></a>`num_heads` — [`L320`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L320)
  - <a id="Qwen35VisionEncoder.Config.num_layers"></a>`num_layers` — [`L319`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L319)
  - <a id="Qwen35VisionEncoder.Config.num_position_embeddings"></a>`num_position_embeddings` — [`L327`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L327)
  - <a id="Qwen35VisionEncoder.Config.patch_embed_proj"></a>`patch_embed_proj` — [`L330`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L330)
  - <a id="Qwen35VisionEncoder.Config.patch_size"></a>`patch_size` — [`L322`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L322)
  - <a id="Qwen35VisionEncoder.Config.rotary_pos_emb"></a>`rotary_pos_emb` — [`L332`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L332)
  - <a id="Qwen35VisionEncoder.Config.spatial_merge_size"></a>`spatial_merge_size` — [`L325`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L325)
  - <a id="Qwen35VisionEncoder.Config.temporal_patch_size"></a>`temporal_patch_size` — [`L323`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L323)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`VisionTransformerBlock`](../common/vision_encoder.md#VisionTransformerBlock), [`Config`](../common/vision_encoder.md#VisionTransformerBlock.Config), [`Config`](vision_encoder.md#PatchMerger.Config), [`Config`](vision_encoder.md#VisionRotaryEmbedding.Config), [`PatchMerger`](vision_encoder.md#PatchMerger), [`VisionRotaryEmbedding`](vision_encoder.md#VisionRotaryEmbedding)
- used by: [`_qwen35_vision_encoder_config`](__init__.md#_qwen35_vision_encoder_config), [`_set_vision_encoder_sharding`](sharding.md#_set_vision_encoder_sharding), [`compute_position_embeddings`](vision_encoder.md#Qwen35VisionEncoder.compute_position_embeddings), [`vision_encoder`](model.md#Qwen35Model.Config.vision_encoder), [`to_hf`](state_dict_adapter.md#Qwen35StateDictAdapter.to_hf), [`layers`](vision_encoder.md#Qwen35VisionEncoder.layers), [`merger`](vision_encoder.md#Qwen35VisionEncoder.merger), [`patch_embed`](vision_encoder.md#Qwen35VisionEncoder.patch_embed), [`pos_embed`](vision_encoder.md#Qwen35VisionEncoder.pos_embed), [`rotary_pos_emb`](vision_encoder.md#Qwen35VisionEncoder.rotary_pos_emb), [`spatial_merge_size`](vision_encoder.md#Qwen35VisionEncoder.spatial_merge_size), [`spatial_merge_size`](model.md#Qwen35Model.spatial_merge_size), [`num_grid_per_side`](vision_encoder.md#Qwen35VisionEncoder.num_grid_per_side), [`__init__`](vision_encoder.md#Qwen35VisionEncoder.__init__), [`num_position_embeddings`](vision_encoder.md#Qwen35VisionEncoder.num_position_embeddings), [`spatial_merge_unit`](vision_encoder.md#Qwen35VisionEncoder.spatial_merge_unit)

### <a id="VisionRotaryEmbedding"></a>`VisionRotaryEmbedding`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/vision_encoder.py:225`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L225)
- doc: 2D Rotary Position Embedding for Vision Transformer.
- signature: `class VisionRotaryEmbedding(Module):`
- members:
  - <a id="VisionRotaryEmbedding._init_self_buffers"></a>`_init_self_buffers(self, *, buffer_device: torch.device | None = None)` — [`L243`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L243) — Re-compute inv_freq on the target device after to_empty().
  - <a id="VisionRotaryEmbedding.forward"></a>`forward(self, seqlen: int)` — [`L254`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L254) — Compute rotary frequency table for positions up to seqlen.
  - <a id="VisionRotaryEmbedding.dim"></a>`dim` — [`L235`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L235)
  - <a id="VisionRotaryEmbedding.inv_freq"></a>`inv_freq` — [`L246`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L246)
  - <a id="VisionRotaryEmbedding.theta"></a>`theta` — [`L236`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L236)
- protocol/private: <a id="VisionRotaryEmbedding.__init__"></a>`__init__`[`L233`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L233)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`Config`](vision_encoder.md#VisionRotaryEmbedding.Config), [`_maybe_wrap_positions`](../common/rope.md#_maybe_wrap_positions), [`dim`](vision_encoder.md#VisionRotaryEmbedding.Config.dim), [`theta`](vision_encoder.md#VisionRotaryEmbedding.Config.theta)
- used by: [`Module`](../../protocols/module.md#Module), [`_qwen35_vision_encoder_config`](__init__.md#_qwen35_vision_encoder_config), [`_init_self_buffers`](../../protocols/module.md#Module._init_self_buffers), [`rotary_pos_emb`](vision_encoder.md#Qwen35VisionEncoder.Config.rotary_pos_emb)

### <a id="VisionRotaryEmbedding.Config"></a>`VisionRotaryEmbedding.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/vision_encoder.py:229`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L229)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VisionRotaryEmbedding.Config.dim"></a>`dim` — [`L230`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L230)
  - <a id="VisionRotaryEmbedding.Config.theta"></a>`theta` — [`L231`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L231)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_qwen35_vision_encoder_config`](__init__.md#_qwen35_vision_encoder_config), [`rotary_pos_emb`](vision_encoder.md#Qwen35VisionEncoder.Config.rotary_pos_emb), [`theta`](vision_encoder.md#VisionRotaryEmbedding.theta), [`dim`](vision_encoder.md#VisionRotaryEmbedding.dim), [`__init__`](vision_encoder.md#VisionRotaryEmbedding.__init__)

## Functions
- <a id="_compute_2d_rope_cache"></a>`_compute_2d_rope_cache(freq_table: torch.Tensor, grids: list[list[int]], spatial_merge_size: int, head_dim: int)` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L126) — Compute 2D RoPE cache for vision patches.
- <a id="_compute_learned_pos_embeds"></a>`_compute_learned_pos_embeds(learned_pos_embed: torch.Tensor, grids: list[list[int]], num_grid_per_side: int, spatial_merge_size: int, dim: int)` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/vision_encoder.py#L36) — Compute bilinear-interpolated learned position embeddings.

