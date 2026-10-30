---
title: 'Module: torchtitan/models/muse_glimmer/vision_encoder.py'
type: catalog
provenance: extracted
module: torchtitan/models/muse_glimmer/vision_encoder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.muse_glimmer.vision_encoder`/
symbols:
  MuseGlimmerVisionEncoder.forward: MuseGlimmerVisionEncoder#forward().
  MuseGlimmerVisionEncoder._embed_image: MuseGlimmerVisionEncoder#_embed_image().
  MuseGlimmerVisionEncoder._get_pos_emb: MuseGlimmerVisionEncoder#_get_pos_emb().
  MuseGlimmerVisionAdapter.Config: MuseGlimmerVisionAdapter#Config#
  MuseGlimmerVisionEncoder.Config: MuseGlimmerVisionEncoder#Config#
  MuseGlimmerVisionEncoder.Config.pos_embed: MuseGlimmerVisionEncoder#Config#pos_embed.
  MuseGlimmerVisionEncoder.Config.token_permute: MuseGlimmerVisionEncoder#Config#token_permute.
  MuseGlimmerVisionEncoder.layers: MuseGlimmerVisionEncoder#layers.
  MuseGlimmerVisionAdapter: MuseGlimmerVisionAdapter#
  MuseGlimmerVisionEncoder: MuseGlimmerVisionEncoder#
  MuseGlimmerVisionEncoder.positional_embedding_vlm: MuseGlimmerVisionEncoder#positional_embedding_vlm.
  MuseGlimmerVisionEncoder._get_sparse_perm_and_slens: MuseGlimmerVisionEncoder#_get_sparse_perm_and_slens().
  MuseGlimmerVisionEncoder._finalize_image: MuseGlimmerVisionEncoder#_finalize_image().
  VisionRopeFreq.Config: VisionRopeFreq#Config#
  MuseGlimmerVisionAdapter.Config.c_fc: MuseGlimmerVisionAdapter#Config#c_fc.
  MuseGlimmerVisionAdapter.Config.c_proj: MuseGlimmerVisionAdapter#Config#c_proj.
  MuseGlimmerVisionEncoder.Config.rope_freq: MuseGlimmerVisionEncoder#Config#rope_freq.
  MuseGlimmerVisionEncoder.Config.conv1: MuseGlimmerVisionEncoder#Config#conv1.
  MuseGlimmerVisionEncoder.Config.ln_pre: MuseGlimmerVisionEncoder#Config#ln_pre.
  MuseGlimmerVisionEncoder.Config.block: MuseGlimmerVisionEncoder#Config#block.
  MuseGlimmerVisionEncoder.Config.ln_post: MuseGlimmerVisionEncoder#Config#ln_post.
  MuseGlimmerVisionEncoder.conv1_linear: MuseGlimmerVisionEncoder#conv1_linear.
  MuseGlimmerVisionEncoder.token_permute: MuseGlimmerVisionEncoder#token_permute.
  _annotate_vision_activation_type: _annotate_vision_activation_type().
  _VisionPosEmbed.Config: _VisionPosEmbed#Config#
  _VisionTokenPermute.Config: _VisionTokenPermute#Config#
  VisionRopeFreq._compute: VisionRopeFreq#_compute().
  VisionRopeFreq.rope_theta: VisionRopeFreq#rope_theta.
  MuseGlimmerVisionAdapter.c_fc: MuseGlimmerVisionAdapter#c_fc.
  MuseGlimmerVisionAdapter.c_proj: MuseGlimmerVisionAdapter#c_proj.
  MuseGlimmerVisionEncoder.rope_freq: MuseGlimmerVisionEncoder#rope_freq.
  MuseGlimmerVisionEncoder.ln_pre: MuseGlimmerVisionEncoder#ln_pre.
  MuseGlimmerVisionEncoder.ln_post: MuseGlimmerVisionEncoder#ln_post.
  MuseGlimmerVisionEncoder.pos_embed: MuseGlimmerVisionEncoder#pos_embed.
  MuseGlimmerVisionEncoder._make_2d_rope: MuseGlimmerVisionEncoder#_make_2d_rope().
  VisionRopeFreq: VisionRopeFreq#
  MuseGlimmerVisionAdapter.forward: MuseGlimmerVisionAdapter#forward().
  MuseGlimmerVisionEncoder.downsample_factor: MuseGlimmerVisionEncoder#downsample_factor.
  MuseGlimmerVisionEncoder.sparse_attention_factor: MuseGlimmerVisionEncoder#sparse_attention_factor.
  MuseGlimmerVisionEncoder.pos_emb_grid_h: MuseGlimmerVisionEncoder#pos_emb_grid_h.
  MuseGlimmerVisionEncoder.pos_emb_grid_w: MuseGlimmerVisionEncoder#pos_emb_grid_w.
  MuseGlimmerVisionEncoder.Config.output_dim: MuseGlimmerVisionEncoder#Config#output_dim.
  _VisionPosEmbed: _VisionPosEmbed#
  _VisionTokenPermute: _VisionTokenPermute#
  VisionRopeFreq.head_dim: VisionRopeFreq#head_dim.
  VisionRopeFreq.inv_freq: VisionRopeFreq#inv_freq.
  MuseGlimmerVisionEncoder.latent_dim: MuseGlimmerVisionEncoder#latent_dim.
  MuseGlimmerVisionEncoder.patch_size: MuseGlimmerVisionEncoder#patch_size.
  MuseGlimmerVisionEncoder.patch_temporal: MuseGlimmerVisionEncoder#patch_temporal.
  MuseGlimmerVisionEncoder._pixel_shuffle_downsample: MuseGlimmerVisionEncoder#_pixel_shuffle_downsample().
  MuseGlimmerVisionEncoder.Config.latent_dim: MuseGlimmerVisionEncoder#Config#latent_dim.
  MuseGlimmerVisionEncoder.Config.num_heads: MuseGlimmerVisionEncoder#Config#num_heads.
  MuseGlimmerVisionEncoder.Config.patch_size: MuseGlimmerVisionEncoder#Config#patch_size.
  MuseGlimmerVisionEncoder.Config.patch_temporal: MuseGlimmerVisionEncoder#Config#patch_temporal.
  MuseGlimmerVisionEncoder.Config.downsample_factor: MuseGlimmerVisionEncoder#Config#downsample_factor.
  MuseGlimmerVisionEncoder.Config.pos_emb_grid_h: MuseGlimmerVisionEncoder#Config#pos_emb_grid_h.
  MuseGlimmerVisionEncoder.Config.pos_emb_grid_w: MuseGlimmerVisionEncoder#Config#pos_emb_grid_w.
  _VisionPosEmbed.__init__: _VisionPosEmbed#__init__().
  _VisionPosEmbed.forward: _VisionPosEmbed#forward().
  _VisionTokenPermute.__init__: _VisionTokenPermute#__init__().
  VisionRopeFreq.__init__: VisionRopeFreq#__init__().
  VisionRopeFreq._init_self_buffers: VisionRopeFreq#_init_self_buffers().
  MuseGlimmerVisionAdapter.__init__: MuseGlimmerVisionAdapter#__init__().
  MuseGlimmerVisionEncoder.__init__: MuseGlimmerVisionEncoder#__init__().
  MuseGlimmerVisionEncoder.output_dim: MuseGlimmerVisionEncoder#output_dim.
  MuseGlimmerVisionEncoder.num_heads: MuseGlimmerVisionEncoder#num_heads.
  MuseGlimmerVisionEncoder.head_dim: MuseGlimmerVisionEncoder#head_dim.
  VisionRopeFreq.Config.head_dim: VisionRopeFreq#Config#head_dim.
  VisionRopeFreq.Config.rope_theta: VisionRopeFreq#Config#rope_theta.
  MuseGlimmerVisionEncoder.Config.num_layers: MuseGlimmerVisionEncoder#Config#num_layers.
  MuseGlimmerVisionEncoder.Config.head_dim: MuseGlimmerVisionEncoder#Config#head_dim.
  MuseGlimmerVisionEncoder.Config.sparse_attention_factor: MuseGlimmerVisionEncoder#Config#sparse_attention_factor.
  reorder_patch_vector: reorder_patch_vector().
  _VisionTokenPermute.forward: _VisionTokenPermute#forward().
---
# Module: [`torchtitan/models/muse_glimmer/vision_encoder.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py)

## Classes
### <a id="MuseGlimmerVisionAdapter"></a>`MuseGlimmerVisionAdapter`  ·  implements/extends Module
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:188`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L188)
- doc: Two-layer GELU MLP adapter mapping encoder features to the LLM adapter
- signature: `class MuseGlimmerVisionAdapter(Module):`
- members:
  - <a id="MuseGlimmerVisionAdapter.forward"></a>`forward(self, x: torch.Tensor)` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L202)
  - <a id="MuseGlimmerVisionAdapter.c_fc"></a>`c_fc` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L199)
  - <a id="MuseGlimmerVisionAdapter.c_proj"></a>`c_proj` — [`L200`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L200)
- protocol/private: <a id="MuseGlimmerVisionAdapter.__init__"></a>`__init__`[`L197`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L197)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](vision_encoder.md#MuseGlimmerVisionAdapter.Config), [`c_fc`](vision_encoder.md#MuseGlimmerVisionAdapter.Config.c_fc), [`c_proj`](vision_encoder.md#MuseGlimmerVisionAdapter.Config.c_proj)
- used by: [`Module`](../../protocols/module.md#Module), [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`set_muse_glimmer_vision_sharding_config`](sharding.md#set_muse_glimmer_vision_sharding_config), [`muse_glimmer_vision_configs`](__init__.md#muse_glimmer_vision_configs), [`muse_glimmer_vision_adapter_config`](__init__.md#muse_glimmer_vision_adapter_config), [`vision_adapter`](model.md#MuseGlimmerModel.Config.vision_adapter)

### <a id="MuseGlimmerVisionAdapter.Config"></a>`MuseGlimmerVisionAdapter.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:193`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L193)
- signature: `class Config(Module.Config):`
- members:
  - <a id="MuseGlimmerVisionAdapter.Config.c_fc"></a>`c_fc` — [`L194`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L194)
  - <a id="MuseGlimmerVisionAdapter.Config.c_proj"></a>`c_proj` — [`L195`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L195)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`set_muse_glimmer_vision_sharding_config`](sharding.md#set_muse_glimmer_vision_sharding_config), [`muse_glimmer_vision_configs`](__init__.md#muse_glimmer_vision_configs), [`muse_glimmer_vision_adapter_config`](__init__.md#muse_glimmer_vision_adapter_config), [`vision_adapter`](model.md#MuseGlimmerModel.Config.vision_adapter), [`c_fc`](vision_encoder.md#MuseGlimmerVisionAdapter.c_fc), [`c_proj`](vision_encoder.md#MuseGlimmerVisionAdapter.c_proj), [`__init__`](vision_encoder.md#MuseGlimmerVisionAdapter.__init__)

### <a id="MuseGlimmerVisionEncoder"></a>`MuseGlimmerVisionEncoder`  ·  implements/extends Module
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:208`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L208) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- doc: Muse Glimmer vision encoder for a batch of (variable-resolution) images.
- signature: `class MuseGlimmerVisionEncoder(Module):`
- members:
  - <a id="MuseGlimmerVisionEncoder._embed_image"></a>`_embed_image(self, patches: torch.Tensor, grid_h: int, grid_w: int, device: torch.device, dtype: torch.dtype)` — [`L374`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L374) — Phase 1 for one image: conv1 -> pos emb -> ln_pre -> (sparse) perm.
  - <a id="MuseGlimmerVisionEncoder._finalize_image"></a>`_finalize_image(self, x: torch.Tensor, grid_h: int, grid_w: int, sp_perm: torch.Tensor | None)` — [`L409`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L409) — Phase 3 for one image: un-permute (if sparse) -> ln_post -> downsample.
  - <a id="MuseGlimmerVisionEncoder._get_pos_emb"></a>`_get_pos_emb(self, grid_h: int, grid_w: int, device: torch.device)` — [`L306`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L306) — Bilinearly resample the learned positional grid to (grid_h, grid_w).
  - <a id="MuseGlimmerVisionEncoder._get_sparse_perm_and_slens"></a>`_get_sparse_perm_and_slens(self, grid_h: int, grid_w: int, device: torch.device)` — [`L348`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L348) — Group patches into pos_emb_grid_h x pos_emb_grid_w windows.
  - <a id="MuseGlimmerVisionEncoder._make_2d_rope"></a>`_make_2d_rope(self, grid_h: int, grid_w: int, device: torch.device)` — [`L285`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L285) — Complex 2D RoPE frequencies for a grid, shape [grid_h*grid_w, head_dim//2].
  - <a id="MuseGlimmerVisionEncoder._pixel_shuffle_downsample"></a>`_pixel_shuffle_downsample(self, x: torch.Tensor, grid_h: int, grid_w: int)` — [`L326`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L326) — Downsample via pixel shuffle: (h r1 w r2) -> (h w r1 r2).
  - <a id="MuseGlimmerVisionEncoder.forward"></a>`forward(self, pixel_values: torch.Tensor, *, grid_thw: torch.Tensor)` — [`L427`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L427) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="MuseGlimmerVisionEncoder.conv1_linear"></a>`conv1_linear` — [`L260`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L260)
  - <a id="MuseGlimmerVisionEncoder.downsample_factor"></a>`downsample_factor` — [`L254`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L254)
  - <a id="MuseGlimmerVisionEncoder.head_dim"></a>`head_dim` — [`L251`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L251)
  - <a id="MuseGlimmerVisionEncoder.latent_dim"></a>`latent_dim` — [`L248`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L248)
  - <a id="MuseGlimmerVisionEncoder.layers"></a>`layers` — [`L269`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L269)
  - <a id="MuseGlimmerVisionEncoder.ln_post"></a>`ln_post` — [`L272`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L272)
  - <a id="MuseGlimmerVisionEncoder.ln_pre"></a>`ln_pre` — [`L268`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L268)
  - <a id="MuseGlimmerVisionEncoder.num_heads"></a>`num_heads` — [`L250`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L250)
  - <a id="MuseGlimmerVisionEncoder.output_dim"></a>`output_dim` — [`L249`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L249)
  - <a id="MuseGlimmerVisionEncoder.patch_size"></a>`patch_size` — [`L252`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L252)
  - <a id="MuseGlimmerVisionEncoder.patch_temporal"></a>`patch_temporal` — [`L253`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L253)
  - <a id="MuseGlimmerVisionEncoder.pos_emb_grid_h"></a>`pos_emb_grid_h` — [`L256`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L256)
  - <a id="MuseGlimmerVisionEncoder.pos_emb_grid_w"></a>`pos_emb_grid_w` — [`L257`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L257)
  - <a id="MuseGlimmerVisionEncoder.pos_embed"></a>`pos_embed` — [`L278`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L278)
  - <a id="MuseGlimmerVisionEncoder.positional_embedding_vlm"></a>`positional_embedding_vlm` — [`L263`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L263)
  - <a id="MuseGlimmerVisionEncoder.rope_freq"></a>`rope_freq` — [`L258`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L258)
  - <a id="MuseGlimmerVisionEncoder.sparse_attention_factor"></a>`sparse_attention_factor` — [`L255`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L255)
  - <a id="MuseGlimmerVisionEncoder.token_permute"></a>`token_permute` — [`L279`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L279)
- protocol/private: <a id="MuseGlimmerVisionEncoder.__init__"></a>`__init__`[`L246`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L246)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`ComplexRoPE`](../common/rope.md#ComplexRoPE), [`ModuleDict`](../../protocols/module.md#ModuleDict), [`Config`](vision_encoder.md#MuseGlimmerVisionEncoder.Config), [`create_block_diagonal_mask`](../common/vision_encoder.md#create_block_diagonal_mask), [`pos_embed`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.pos_embed), [`token_permute`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.token_permute), [`apply_rotary_emb`](../common/rope.md#ComplexRoPE.apply_rotary_emb), [`block`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.block), [`conv1`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.conv1), [`ln_post`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.ln_post), [`ln_pre`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.ln_pre), [`rope_freq`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.rope_freq), [`_annotate_vision_activation_type`](vision_encoder.md#_annotate_vision_activation_type), [`output_dim`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.output_dim), [`downsample_factor`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.downsample_factor), [`latent_dim`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.latent_dim), [`num_heads`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.num_heads), [`patch_size`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.patch_size), [`patch_temporal`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.patch_temporal), [`pos_emb_grid_h`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.pos_emb_grid_h), [`pos_emb_grid_w`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.pos_emb_grid_w), [`head_dim`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.head_dim), [`num_layers`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.num_layers), [`sparse_attention_factor`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.sparse_attention_factor), [`reorder_patch_vector`](vision_encoder.md#reorder_patch_vector)
- used by: [`Module`](../../protocols/module.md#Module), [`muse_glimmer_vision_encoder_config`](__init__.md#muse_glimmer_vision_encoder_config), [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`set_muse_glimmer_vision_sharding_config`](sharding.md#set_muse_glimmer_vision_sharding_config), [`muse_glimmer_vision_configs`](__init__.md#muse_glimmer_vision_configs), [`vision_encoder`](model.md#MuseGlimmerModel.Config.vision_encoder)

### <a id="MuseGlimmerVisionEncoder.Config"></a>`MuseGlimmerVisionEncoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:226`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L226) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- signature: `class Config(Module.Config):`
- members:
  - <a id="MuseGlimmerVisionEncoder.Config.block"></a>`block` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L241)
  - <a id="MuseGlimmerVisionEncoder.Config.conv1"></a>`conv1` — [`L239`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L239)
  - <a id="MuseGlimmerVisionEncoder.Config.downsample_factor"></a>`downsample_factor` — [`L234`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L234)
  - <a id="MuseGlimmerVisionEncoder.Config.head_dim"></a>`head_dim` — [`L231`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L231)
  - <a id="MuseGlimmerVisionEncoder.Config.latent_dim"></a>`latent_dim` — [`L227`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L227)
  - <a id="MuseGlimmerVisionEncoder.Config.ln_post"></a>`ln_post` — [`L242`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L242)
  - <a id="MuseGlimmerVisionEncoder.Config.ln_pre"></a>`ln_pre` — [`L240`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L240)
  - <a id="MuseGlimmerVisionEncoder.Config.num_heads"></a>`num_heads` — [`L230`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L230)
  - <a id="MuseGlimmerVisionEncoder.Config.num_layers"></a>`num_layers` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L229)
  - <a id="MuseGlimmerVisionEncoder.Config.output_dim"></a>`output_dim` — [`L228`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L228)
  - <a id="MuseGlimmerVisionEncoder.Config.patch_size"></a>`patch_size` — [`L232`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L232)
  - <a id="MuseGlimmerVisionEncoder.Config.patch_temporal"></a>`patch_temporal` — [`L233`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L233)
  - <a id="MuseGlimmerVisionEncoder.Config.pos_emb_grid_h"></a>`pos_emb_grid_h` — [`L236`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L236)
  - <a id="MuseGlimmerVisionEncoder.Config.pos_emb_grid_w"></a>`pos_emb_grid_w` — [`L237`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L237)
  - <a id="MuseGlimmerVisionEncoder.Config.pos_embed"></a>`pos_embed` — [`L243`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L243)
  - <a id="MuseGlimmerVisionEncoder.Config.rope_freq"></a>`rope_freq` — [`L238`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L238)
  - <a id="MuseGlimmerVisionEncoder.Config.sparse_attention_factor"></a>`sparse_attention_factor` — [`L235`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L235)
  - <a id="MuseGlimmerVisionEncoder.Config.token_permute"></a>`token_permute` — [`L244`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L244)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`LayerNorm`](../common/nn_modules.md#LayerNorm), [`Config`](../common/nn_modules.md#LayerNorm.Config), [`VisionTransformerBlock`](../common/vision_encoder.md#VisionTransformerBlock), [`Config`](../common/vision_encoder.md#VisionTransformerBlock.Config), [`Config`](vision_encoder.md#VisionRopeFreq.Config), [`Config`](vision_encoder.md#_VisionPosEmbed.Config), [`Config`](vision_encoder.md#_VisionTokenPermute.Config), [`VisionRopeFreq`](vision_encoder.md#VisionRopeFreq), [`_VisionPosEmbed`](vision_encoder.md#_VisionPosEmbed), [`_VisionTokenPermute`](vision_encoder.md#_VisionTokenPermute)
- used by: [`muse_glimmer_vision_encoder_config`](__init__.md#muse_glimmer_vision_encoder_config), [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`_muse_glimmer_mm_dataloader`](config_registry.md#_muse_glimmer_mm_dataloader), [`set_muse_glimmer_vision_sharding_config`](sharding.md#set_muse_glimmer_vision_sharding_config), [`muse_glimmer_vision_configs`](__init__.md#muse_glimmer_vision_configs), [`_muse_glimmer_debugmodel_mm`](__init__.md#_muse_glimmer_debugmodel_mm), [`layers`](vision_encoder.md#MuseGlimmerVisionEncoder.layers), [`vision_encoder`](model.md#MuseGlimmerModel.Config.vision_encoder), [`_vision_num_heads`](state_dict_adapter.md#MuseGlimmerStateDictAdapter._vision_num_heads), [`positional_embedding_vlm`](vision_encoder.md#MuseGlimmerVisionEncoder.positional_embedding_vlm), [`conv1_linear`](vision_encoder.md#MuseGlimmerVisionEncoder.conv1_linear), [`token_permute`](vision_encoder.md#MuseGlimmerVisionEncoder.token_permute), [`ln_post`](vision_encoder.md#MuseGlimmerVisionEncoder.ln_post), [`ln_pre`](vision_encoder.md#MuseGlimmerVisionEncoder.ln_pre), [`pos_embed`](vision_encoder.md#MuseGlimmerVisionEncoder.pos_embed), [`rope_freq`](vision_encoder.md#MuseGlimmerVisionEncoder.rope_freq), [`downsample_factor`](vision_encoder.md#MuseGlimmerVisionEncoder.downsample_factor), [`pos_emb_grid_h`](vision_encoder.md#MuseGlimmerVisionEncoder.pos_emb_grid_h), [`pos_emb_grid_w`](vision_encoder.md#MuseGlimmerVisionEncoder.pos_emb_grid_w), [`sparse_attention_factor`](vision_encoder.md#MuseGlimmerVisionEncoder.sparse_attention_factor), [`latent_dim`](vision_encoder.md#MuseGlimmerVisionEncoder.latent_dim), [`patch_size`](vision_encoder.md#MuseGlimmerVisionEncoder.patch_size), [`patch_temporal`](vision_encoder.md#MuseGlimmerVisionEncoder.patch_temporal), [`__init__`](vision_encoder.md#MuseGlimmerVisionEncoder.__init__), [`head_dim`](vision_encoder.md#MuseGlimmerVisionEncoder.head_dim), [`num_heads`](vision_encoder.md#MuseGlimmerVisionEncoder.num_heads), [`output_dim`](vision_encoder.md#MuseGlimmerVisionEncoder.output_dim)

### <a id="VisionRopeFreq"></a>`VisionRopeFreq`  ·  implements/extends Module
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:158`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L158)
- doc: Holds the replicated RoPE inverse-frequency table.
- signature: `class VisionRopeFreq(Module):`
- members:
  - <a id="VisionRopeFreq._compute"></a>`_compute(self)` — [`L172`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L172) — RoPE inverse frequencies, shape [head_dim // 4].
  - <a id="VisionRopeFreq.head_dim"></a>`head_dim` — [`L168`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L168)
  - <a id="VisionRopeFreq.inv_freq"></a>`inv_freq` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L185)
  - <a id="VisionRopeFreq.rope_theta"></a>`rope_theta` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L169)
- protocol/private: <a id="VisionRopeFreq.__init__"></a>`__init__`[`L166`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L166), <a id="VisionRopeFreq._init_self_buffers"></a>`_init_self_buffers`[`L181`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L181)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](vision_encoder.md#VisionRopeFreq.Config), [`head_dim`](vision_encoder.md#VisionRopeFreq.Config.head_dim), [`rope_theta`](vision_encoder.md#VisionRopeFreq.Config.rope_theta)
- used by: [`Module`](../../protocols/module.md#Module), [`muse_glimmer_vision_encoder_config`](__init__.md#muse_glimmer_vision_encoder_config), [`_init_self_buffers`](../../protocols/module.md#Module._init_self_buffers), [`rope_freq`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.rope_freq)

### <a id="VisionRopeFreq.Config"></a>`VisionRopeFreq.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:162`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L162)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VisionRopeFreq.Config.head_dim"></a>`head_dim` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L163)
  - <a id="VisionRopeFreq.Config.rope_theta"></a>`rope_theta` — [`L164`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L164)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`muse_glimmer_vision_encoder_config`](__init__.md#muse_glimmer_vision_encoder_config), [`rope_freq`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.rope_freq), [`rope_theta`](vision_encoder.md#VisionRopeFreq.rope_theta), [`head_dim`](vision_encoder.md#VisionRopeFreq.head_dim), [`__init__`](vision_encoder.md#VisionRopeFreq.__init__)

### <a id="_VisionPosEmbed"></a>`_VisionPosEmbed`  ·  implements/extends Module
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:94`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L94)
- doc: Bilinearly resample the learned positional grid to (grid_h, grid_w).
- signature: `class _VisionPosEmbed(Module):`
- members:
  - <a id="_VisionPosEmbed.forward"></a>`forward(self, pos_param: torch.Tensor, *, grid_h: int, grid_w: int, src_grid_h: int, src_grid_w: int, latent_dim: int, device: torch.device)` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L110)
- protocol/private: <a id="_VisionPosEmbed.__init__"></a>`__init__`[`L107`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L107)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`_annotate_vision_activation_type`](vision_encoder.md#_annotate_vision_activation_type), [`Config`](vision_encoder.md#_VisionPosEmbed.Config)
- used by: [`Module`](../../protocols/module.md#Module), [`pos_embed`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.pos_embed)

### <a id="_VisionPosEmbed.Config"></a>`_VisionPosEmbed.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:104`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L104)
- signature: `class Config(Module.Config):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`pos_embed`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.pos_embed), [`__init__`](vision_encoder.md#_VisionPosEmbed.__init__)

### <a id="_VisionTokenPermute"></a>`_VisionTokenPermute`  ·  implements/extends Module
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:138`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L138)
- doc: Advanced-index a token sequence by a permutation: `x[index]`.
- signature: `class _VisionTokenPermute(Module):`
- members:
  - <a id="_VisionTokenPermute.forward"></a>`forward(self, x: torch.Tensor, index: torch.Tensor)` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L154)
- protocol/private: <a id="_VisionTokenPermute.__init__"></a>`__init__`[`L151`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L151)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](vision_encoder.md#_VisionTokenPermute.Config)
- used by: [`Module`](../../protocols/module.md#Module), [`token_permute`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.token_permute)

### <a id="_VisionTokenPermute.Config"></a>`_VisionTokenPermute.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/vision_encoder.py:148`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L148)
- signature: `class Config(Module.Config):`
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`token_permute`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.token_permute), [`__init__`](vision_encoder.md#_VisionTokenPermute.__init__)

## Functions
- <a id="_annotate_vision_activation_type"></a>`_annotate_vision_activation_type(tensor: torch.Tensor)` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L50) — Annotate a tensor created inside the vision forward.
- <a id="reorder_patch_vector"></a>`reorder_patch_vector(patches: torch.Tensor, *, patch_size: int, patch_temporal: int)` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/vision_encoder.py#L61) — Reorder a patch vector from the shared collator's ``(c, pt, ph, pw)``

