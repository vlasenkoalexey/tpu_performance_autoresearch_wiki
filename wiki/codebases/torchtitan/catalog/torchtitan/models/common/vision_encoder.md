---
title: 'Module: torchtitan/models/common/vision_encoder.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/vision_encoder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.vision_encoder`/
symbols:
  VisionAttention.forward: VisionAttention#forward().
  VisionTransformerBlock: VisionTransformerBlock#
  VisionTransformerBlock.Config.attn: VisionTransformerBlock#Config#attn.
  VisionTransformerBlock.Config.norm1: VisionTransformerBlock#Config#norm1.
  VisionTransformerBlock.Config.norm2: VisionTransformerBlock#Config#norm2.
  VisionTransformerBlock.Config: VisionTransformerBlock#Config#
  VisionAttention.Config.inner_attention: VisionAttention#Config#inner_attention.
  VisionTransformerBlock.forward: VisionTransformerBlock#forward().
  create_block_diagonal_mask: create_block_diagonal_mask().
  VisionTransformerBlock.Config.mlp: VisionTransformerBlock#Config#mlp.
  VisionMLP: VisionMLP#
  VisionAttention: VisionAttention#
  VisionMLP.Config: VisionMLP#Config#
  VisionMLP.Config.fc1: VisionMLP#Config#fc1.
  VisionMLP.Config.fc2: VisionMLP#Config#fc2.
  VisionAttention.Config: VisionAttention#Config#
  VisionAttention.Config.wq: VisionAttention#Config#wq.
  VisionAttention.Config.wk: VisionAttention#Config#wk.
  VisionAttention.Config.wv: VisionAttention#Config#wv.
  VisionAttention.Config.proj: VisionAttention#Config#proj.
  VisionMLP.Config.act_fn: VisionMLP#Config#act_fn.
  VisionAttention.head_dim: VisionAttention#head_dim.
  VisionMLP.forward: VisionMLP#forward().
  VisionAttention.__init__: VisionAttention#__init__().
  VisionAttention.Config.dim: VisionAttention#Config#dim.
  VisionAttention.Config.num_heads: VisionAttention#Config#num_heads.
  VisionMLP.linear_fc1: VisionMLP#linear_fc1.
  VisionMLP.linear_fc2: VisionMLP#linear_fc2.
  VisionMLP.act_fn: VisionMLP#act_fn.
  VisionAttention.wq: VisionAttention#wq.
  VisionAttention.wk: VisionAttention#wk.
  VisionAttention.wv: VisionAttention#wv.
  VisionAttention.proj: VisionAttention#proj.
  VisionAttention.flex_attention: VisionAttention#flex_attention.
  VisionTransformerBlock.norm1: VisionTransformerBlock#norm1.
  VisionTransformerBlock.norm2: VisionTransformerBlock#norm2.
  VisionTransformerBlock.attn: VisionTransformerBlock#attn.
  VisionTransformerBlock.mlp: VisionTransformerBlock#mlp.
  VisionMLP.__init__: VisionMLP#__init__().
  VisionTransformerBlock.__init__: VisionTransformerBlock#__init__().
  RopeApply: RopeApply.
  compiled_create_block_mask: compiled_create_block_mask.
  create_block_diagonal_mask.mask_mod: create_block_diagonal_mask().mask_mod().
---
# Module: [`torchtitan/models/common/vision_encoder.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py)

## Classes
### <a id="VisionAttention"></a>`VisionAttention`  ·  implements/extends Module
- def: [`torchtitan/models/common/vision_encoder.py:90`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L90)
- doc: Multi-head self-attention with FlexInnerAttention over visual patches.
- signature: `class VisionAttention(Module):`
- members:
  - <a id="VisionAttention.forward"></a>`forward(self, x: torch.Tensor, *, rope_cache: torch.Tensor, rope_apply: RopeApply, attention_mask: BlockMask)` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L125)
  - <a id="VisionAttention.flex_attention"></a>`flex_attention` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L123)
  - <a id="VisionAttention.head_dim"></a>`head_dim` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L117)
  - <a id="VisionAttention.proj"></a>`proj` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L122)
  - <a id="VisionAttention.wk"></a>`wk` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L120)
  - <a id="VisionAttention.wq"></a>`wq` — [`L119`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L119)
  - <a id="VisionAttention.wv"></a>`wv` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L121)
- protocol/private: <a id="VisionAttention.__init__"></a>`__init__`[`L110`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L110)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`inner_attention`](vision_encoder.md#VisionAttention.Config.inner_attention), [`Config`](vision_encoder.md#VisionAttention.Config), [`proj`](vision_encoder.md#VisionAttention.Config.proj), [`wk`](vision_encoder.md#VisionAttention.Config.wk), [`wq`](vision_encoder.md#VisionAttention.Config.wq), [`wv`](vision_encoder.md#VisionAttention.Config.wv), [`dim`](vision_encoder.md#VisionAttention.Config.dim), [`num_heads`](vision_encoder.md#VisionAttention.Config.num_heads), [`local_head_split`](attention.md#local_head_split), [`RopeApply`](vision_encoder.md#RopeApply)
- used by: [`Module`](../../protocols/module.md#Module), [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_qwen35_vision_encoder_config`](../qwen3_5/__init__.md#_qwen35_vision_encoder_config), [`_vision_encoder_config`](../kimi_k2_7/__init__.md#_vision_encoder_config), [`muse_glimmer_vision_encoder_config`](../muse_glimmer/__init__.md#muse_glimmer_vision_encoder_config), [`attn`](vision_encoder.md#VisionTransformerBlock.Config.attn)

### <a id="VisionAttention.Config"></a>`VisionAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/vision_encoder.py:99`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L99)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VisionAttention.Config.dim"></a>`dim` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L100)
  - <a id="VisionAttention.Config.inner_attention"></a>`inner_attention` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L106)
  - <a id="VisionAttention.Config.num_heads"></a>`num_heads` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L101)
  - <a id="VisionAttention.Config.proj"></a>`proj` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L105)
  - <a id="VisionAttention.Config.wk"></a>`wk` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L103)
  - <a id="VisionAttention.Config.wq"></a>`wq` — [`L102`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L102)
  - <a id="VisionAttention.Config.wv"></a>`wv` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L104)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config), [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`Config`](../../protocols/module.md#Module.Config), [`Config`](attention.md#FlexInnerAttention.Config)
- used by: [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_qwen35_vision_encoder_config`](../qwen3_5/__init__.md#_qwen35_vision_encoder_config), [`_vision_encoder_config`](../kimi_k2_7/__init__.md#_vision_encoder_config), [`muse_glimmer_vision_encoder_config`](../muse_glimmer/__init__.md#muse_glimmer_vision_encoder_config), [`set_vision_transformer_block_sharding_config`](vision_encoder_sharding.md#set_vision_transformer_block_sharding_config), [`attn`](vision_encoder.md#VisionTransformerBlock.Config.attn), [`head_dim`](vision_encoder.md#VisionAttention.head_dim), [`__init__`](vision_encoder.md#VisionAttention.__init__), [`flex_attention`](vision_encoder.md#VisionAttention.flex_attention), [`proj`](vision_encoder.md#VisionAttention.proj), [`wk`](vision_encoder.md#VisionAttention.wk), [`wq`](vision_encoder.md#VisionAttention.wq), [`wv`](vision_encoder.md#VisionAttention.wv)

### <a id="VisionMLP"></a>`VisionMLP`  ·  implements/extends Module
- def: [`torchtitan/models/common/vision_encoder.py:69`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L69)
- doc: Feed-forward network with GELU activation (fc1 -&gt; act -&gt; fc2).
- signature: `class VisionMLP(Module):`
- members:
  - <a id="VisionMLP.forward"></a>`forward(self, x: torch.Tensor)` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L86)
  - <a id="VisionMLP.act_fn"></a>`act_fn` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L84)
  - <a id="VisionMLP.linear_fc1"></a>`linear_fc1` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L82)
  - <a id="VisionMLP.linear_fc2"></a>`linear_fc2` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L83)
- protocol/private: <a id="VisionMLP.__init__"></a>`__init__`[`L80`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L80)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](vision_encoder.md#VisionMLP.Config), [`fc1`](vision_encoder.md#VisionMLP.Config.fc1), [`fc2`](vision_encoder.md#VisionMLP.Config.fc2), [`act_fn`](vision_encoder.md#VisionMLP.Config.act_fn)
- used by: [`Module`](../../protocols/module.md#Module), [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_qwen35_vision_encoder_config`](../qwen3_5/__init__.md#_qwen35_vision_encoder_config), [`_vision_encoder_config`](../kimi_k2_7/__init__.md#_vision_encoder_config), [`muse_glimmer_vision_encoder_config`](../muse_glimmer/__init__.md#muse_glimmer_vision_encoder_config), [`mlp`](vision_encoder.md#VisionTransformerBlock.Config.mlp)

### <a id="VisionMLP.Config"></a>`VisionMLP.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/vision_encoder.py:73`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L73)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VisionMLP.Config.act_fn"></a>`act_fn` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L76)
  - <a id="VisionMLP.Config.fc1"></a>`fc1` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L74)
  - <a id="VisionMLP.Config.fc2"></a>`fc2` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L75)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](linear.md#Linear), [`Config`](linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`GELU`](nn_modules.md#GELU), [`Config`](nn_modules.md#GELU.Config), [`approximate`](nn_modules.md#GELU.Config.approximate)
- used by: [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_qwen35_vision_encoder_config`](../qwen3_5/__init__.md#_qwen35_vision_encoder_config), [`_vision_encoder_config`](../kimi_k2_7/__init__.md#_vision_encoder_config), [`muse_glimmer_vision_encoder_config`](../muse_glimmer/__init__.md#muse_glimmer_vision_encoder_config), [`set_vision_transformer_block_sharding_config`](vision_encoder_sharding.md#set_vision_transformer_block_sharding_config), [`mlp`](vision_encoder.md#VisionTransformerBlock.Config.mlp), [`act_fn`](vision_encoder.md#VisionMLP.act_fn), [`linear_fc1`](vision_encoder.md#VisionMLP.linear_fc1), [`linear_fc2`](vision_encoder.md#VisionMLP.linear_fc2), [`__init__`](vision_encoder.md#VisionMLP.__init__)

### <a id="VisionTransformerBlock"></a>`VisionTransformerBlock`  ·  implements/extends Module
- def: [`torchtitan/models/common/vision_encoder.py:150`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L150)
- doc: Pre-norm transformer block: norm -&gt; attn -&gt; residual -&gt; norm -&gt; mlp.
- signature: `class VisionTransformerBlock(Module):`
- members:
  - <a id="VisionTransformerBlock.forward"></a>`forward(self, x: torch.Tensor, *, rope_cache: torch.Tensor, rope_apply: RopeApply, attention_mask: BlockMask)` — [`L168`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L168)
  - <a id="VisionTransformerBlock.attn"></a>`attn` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L165)
  - <a id="VisionTransformerBlock.mlp"></a>`mlp` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L166)
  - <a id="VisionTransformerBlock.norm1"></a>`norm1` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L163)
  - <a id="VisionTransformerBlock.norm2"></a>`norm2` — [`L164`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L164)
- protocol/private: <a id="VisionTransformerBlock.__init__"></a>`__init__`[`L161`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L161)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`attn`](vision_encoder.md#VisionTransformerBlock.Config.attn), [`norm1`](vision_encoder.md#VisionTransformerBlock.Config.norm1), [`norm2`](vision_encoder.md#VisionTransformerBlock.Config.norm2), [`Config`](vision_encoder.md#VisionTransformerBlock.Config), [`mlp`](vision_encoder.md#VisionTransformerBlock.Config.mlp), [`RopeApply`](vision_encoder.md#RopeApply)
- used by: [`Module`](../../protocols/module.md#Module), [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_qwen35_vision_encoder_config`](../qwen3_5/__init__.md#_qwen35_vision_encoder_config), [`_vision_encoder_config`](../kimi_k2_7/__init__.md#_vision_encoder_config), [`muse_glimmer_vision_encoder_config`](../muse_glimmer/__init__.md#muse_glimmer_vision_encoder_config), [`set_vision_transformer_block_sharding_config`](vision_encoder_sharding.md#set_vision_transformer_block_sharding_config), [`block`](../kimi_k2_7/vision_encoder.md#MoonViTEncoder.Config.block), [`block`](../muse_glimmer/vision_encoder.md#MuseGlimmerVisionEncoder.Config.block), [`block`](../qwen3_5/vision_encoder.md#Qwen35VisionEncoder.Config.block)

### <a id="VisionTransformerBlock.Config"></a>`VisionTransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/vision_encoder.py:154`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L154)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VisionTransformerBlock.Config.attn"></a>`attn` — [`L158`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L158)
  - <a id="VisionTransformerBlock.Config.mlp"></a>`mlp` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L159)
  - <a id="VisionTransformerBlock.Config.norm1"></a>`norm1` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L156)
  - <a id="VisionTransformerBlock.Config.norm2"></a>`norm2` — [`L157`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L157)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`RMSNorm`](nn_modules.md#RMSNorm), [`Config`](../../protocols/module.md#Module.Config), [`Config`](nn_modules.md#RMSNorm.Config), [`LayerNorm`](nn_modules.md#LayerNorm), [`Config`](nn_modules.md#LayerNorm.Config), [`VisionAttention`](vision_encoder.md#VisionAttention), [`VisionMLP`](vision_encoder.md#VisionMLP), [`Config`](vision_encoder.md#VisionAttention.Config), [`Config`](vision_encoder.md#VisionMLP.Config)
- used by: [`_vision_encoder_config`](../kimi_k3/__init__.md#_vision_encoder_config), [`_qwen35_vision_encoder_config`](../qwen3_5/__init__.md#_qwen35_vision_encoder_config), [`_vision_encoder_config`](../kimi_k2_7/__init__.md#_vision_encoder_config), [`muse_glimmer_vision_encoder_config`](../muse_glimmer/__init__.md#muse_glimmer_vision_encoder_config), [`set_vision_transformer_block_sharding_config`](vision_encoder_sharding.md#set_vision_transformer_block_sharding_config), [`block`](../kimi_k2_7/vision_encoder.md#MoonViTEncoder.Config.block), [`block`](../muse_glimmer/vision_encoder.md#MuseGlimmerVisionEncoder.Config.block), [`block`](../qwen3_5/vision_encoder.md#Qwen35VisionEncoder.Config.block), [`attn`](vision_encoder.md#VisionTransformerBlock.attn), [`mlp`](vision_encoder.md#VisionTransformerBlock.mlp), [`norm1`](vision_encoder.md#VisionTransformerBlock.norm1), [`norm2`](vision_encoder.md#VisionTransformerBlock.norm2), [`__init__`](vision_encoder.md#VisionTransformerBlock.__init__)

## Functions
- <a id="create_block_diagonal_mask"></a>`create_block_diagonal_mask(segment_lengths: torch.Tensor, total_tokens: int, device: torch.device)` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L42) — Create a FlexInnerAttention mask over contiguous packed segments.
- <a id="create_block_diagonal_mask.mask_mod"></a>`mask_mod(b, h, q_idx, kv_idx)` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L56)

## Module values
- <a id="RopeApply"></a>`RopeApply` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L37)
- <a id="compiled_create_block_mask"></a>`compiled_create_block_mask` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder.py#L34)

