---
title: 'Module: torchtitan/models/deepseek_v4/compressor.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/compressor.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4.compressor`/
symbols:
  Compressor.forward: Compressor#forward().
  Indexer.forward: Indexer#forward().
  Compressor.Config: Compressor#Config#
  Compressor: Compressor#
  Indexer.Config: Indexer#Config#
  Indexer: Indexer#
  Compressor.Config.rope: Compressor#Config#rope.
  Compressor.Config.wkv: Compressor#Config#wkv.
  Compressor.Config.wgate: Compressor#Config#wgate.
  Compressor.Config.norm: Compressor#Config#norm.
  Compressor.wkv: Compressor#wkv.
  Indexer.Config.rope: Indexer#Config#rope.
  Indexer.Config.wq_b: Indexer#Config#wq_b.
  Indexer.Config.weights_proj: Indexer#Config#weights_proj.
  Indexer.Config.compressor: Indexer#Config#compressor.
  Compressor.rope: Compressor#rope.
  Compressor.wgate: Compressor#wgate.
  Compressor.norm: Compressor#norm.
  Compressor.ape: Compressor#ape.
  Indexer.rope: Indexer#rope.
  Indexer.wq_b: Indexer#wq_b.
  Indexer.weights_proj: Indexer#weights_proj.
  Indexer.compressor: Indexer#compressor.
  Compressor.head_dim: Compressor#head_dim.
  Compressor._overlap_transform: Compressor#_overlap_transform().
  Indexer.num_index_heads: Indexer#num_index_heads.
  Indexer.head_dim: Indexer#head_dim.
  Indexer._rotate_activation: Indexer#_rotate_activation().
  Compressor.Config.compress_ratio: Compressor#Config#compress_ratio.
  Compressor.rope_head_dim: Compressor#rope_head_dim.
  Compressor.compress_ratio: Compressor#compress_ratio.
  Compressor.overlap: Compressor#overlap.
  Indexer.rope_head_dim: Indexer#rope_head_dim.
  Indexer.softmax_scale: Indexer#softmax_scale.
  Indexer.Config.index_head_dim: Indexer#Config#index_head_dim.
  Compressor.__init__: Compressor#__init__().
  Indexer.__init__: Indexer#__init__().
  Compressor.Config.head_dim: Compressor#Config#head_dim.
  Compressor.Config.rope_head_dim: Compressor#Config#rope_head_dim.
  Indexer.Config.num_index_heads: Indexer#Config#num_index_heads.
  Indexer.Config.rope_head_dim: Indexer#Config#rope_head_dim.
  _hadamard: _hadamard().
  Indexer.select: Indexer#select().
---
# Module: [`torchtitan/models/deepseek_v4/compressor.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py)

## Classes
### <a id="Compressor"></a>`Compressor`  ·  implements/extends Module
- def: [`torchtitan/models/deepseek_v4/compressor.py:31`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L31) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- doc: Compress local hidden states into lower-rate KV tokens.
- signature: `class Compressor(Module):`
- members:
  - <a id="Compressor._overlap_transform"></a>`_overlap_transform(self, tensor, value=0)` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L64) — Append previous-token overlap candidates along the ratio dimension.
  - <a id="Compressor.forward"></a>`forward(self, x, positions)` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L85) — Compress hidden states into compressed KV states. — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="Compressor.ape"></a>`ape` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L62)
  - <a id="Compressor.compress_ratio"></a>`compress_ratio` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L55)
  - <a id="Compressor.head_dim"></a>`head_dim` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L53)
  - <a id="Compressor.norm"></a>`norm` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L61)
  - <a id="Compressor.overlap"></a>`overlap` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L56)
  - <a id="Compressor.rope"></a>`rope` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L57)
  - <a id="Compressor.rope_head_dim"></a>`rope_head_dim` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L54)
  - <a id="Compressor.wgate"></a>`wgate` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L60)
  - <a id="Compressor.wkv"></a>`wkv` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L59)
- protocol/private: <a id="Compressor.__init__"></a>`__init__`[`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L50)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](compressor.md#Compressor.Config), [`norm`](compressor.md#Compressor.Config.norm), [`rope`](compressor.md#Compressor.Config.rope), [`wgate`](compressor.md#Compressor.Config.wgate), [`wkv`](compressor.md#Compressor.Config.wkv), [`compress_ratio`](compressor.md#Compressor.Config.compress_ratio), [`head_dim`](compressor.md#Compressor.Config.head_dim), [`rope_head_dim`](compressor.md#Compressor.Config.rope_head_dim)
- used by: [`Module`](../../protocols/module.md#Module), [`_make_compressor_config`](__init__.md#_make_compressor_config), [`compressor`](attention.md#Attention.Config.compressor), [`compressor_128`](attention.md#Attention.Config.compressor_128), [`compressor`](compressor.md#Indexer.Config.compressor)

### <a id="Compressor.Config"></a>`Compressor.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/compressor.py:41`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L41)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Compressor.Config.compress_ratio"></a>`compress_ratio` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L48)
  - <a id="Compressor.Config.head_dim"></a>`head_dim` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L46)
  - <a id="Compressor.Config.norm"></a>`norm` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L45)
  - <a id="Compressor.Config.rope"></a>`rope` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L42)
  - <a id="Compressor.Config.rope_head_dim"></a>`rope_head_dim` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L47)
  - <a id="Compressor.Config.wgate"></a>`wgate` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L44)
  - <a id="Compressor.Config.wkv"></a>`wkv` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L43)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../../protocols/module.md#Module.Config), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`RoPE`](../common/rope.md#RoPE), [`Config`](../common/rope.md#RoPE.Config)
- used by: [`_make_compressor_config`](__init__.md#_make_compressor_config), [`compressor`](attention.md#Attention.Config.compressor), [`compressor_128`](attention.md#Attention.Config.compressor_128), [`compressor`](compressor.md#Indexer.Config.compressor), [`wkv`](compressor.md#Compressor.wkv), [`ape`](compressor.md#Compressor.ape), [`norm`](compressor.md#Compressor.norm), [`rope`](compressor.md#Compressor.rope), [`wgate`](compressor.md#Compressor.wgate), [`head_dim`](compressor.md#Compressor.head_dim), [`compress_ratio`](compressor.md#Compressor.compress_ratio), [`overlap`](compressor.md#Compressor.overlap), [`rope_head_dim`](compressor.md#Compressor.rope_head_dim), [`__init__`](compressor.md#Compressor.__init__)

### <a id="Indexer"></a>`Indexer`  ·  implements/extends Module
- def: [`torchtitan/models/deepseek_v4/compressor.py:120`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L120)
- doc: Produce low-dimensional query/key features for CSA top-k selection.
- signature: `class Indexer(Module):`
- members:
  - <a id="Indexer.forward"></a>`forward(self, x, qr, *, positions)` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L159) — Project raw indexer queries, keys, and per-head weights. — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="Indexer.select"></a>`select(idx_q, idx_k, idx_w, *, seqlen: int, ratio: int, topk: int)` — [`L183`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L183) — Select top-k compressed positions per folded query token.
  - <a id="Indexer.compressor"></a>`compressor` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L144)
  - <a id="Indexer.head_dim"></a>`head_dim` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L137)
  - <a id="Indexer.num_index_heads"></a>`num_index_heads` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L136)
  - <a id="Indexer.rope"></a>`rope` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L140)
  - <a id="Indexer.rope_head_dim"></a>`rope_head_dim` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L138)
  - <a id="Indexer.softmax_scale"></a>`softmax_scale` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L139)
  - <a id="Indexer.weights_proj"></a>`weights_proj` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L143)
  - <a id="Indexer.wq_b"></a>`wq_b` — [`L142`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L142)
- protocol/private: <a id="Indexer.__init__"></a>`__init__`[`L133`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L133), <a id="Indexer._rotate_activation"></a>`_rotate_activation`[`L147`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L147)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](compressor.md#Indexer.Config), [`compressor`](compressor.md#Indexer.Config.compressor), [`rope`](compressor.md#Indexer.Config.rope), [`weights_proj`](compressor.md#Indexer.Config.weights_proj), [`wq_b`](compressor.md#Indexer.Config.wq_b), [`index_head_dim`](compressor.md#Indexer.Config.index_head_dim), [`num_index_heads`](compressor.md#Indexer.Config.num_index_heads), [`rope_head_dim`](compressor.md#Indexer.Config.rope_head_dim), [`_hadamard`](compressor.md#_hadamard)
- used by: [`Module`](../../protocols/module.md#Module), [`_make_indexer_config`](__init__.md#_make_indexer_config), [`_forward_impl`](attention.md#DSV4FlexInnerAttention._forward_impl), [`indexer`](attention.md#Attention.Config.indexer)

### <a id="Indexer.Config"></a>`Indexer.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/compressor.py:124`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L124)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Indexer.Config.compressor"></a>`compressor` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L128)
  - <a id="Indexer.Config.index_head_dim"></a>`index_head_dim` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L130)
  - <a id="Indexer.Config.num_index_heads"></a>`num_index_heads` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L129)
  - <a id="Indexer.Config.rope"></a>`rope` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L125)
  - <a id="Indexer.Config.rope_head_dim"></a>`rope_head_dim` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L131)
  - <a id="Indexer.Config.weights_proj"></a>`weights_proj` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L127)
  - <a id="Indexer.Config.wq_b"></a>`wq_b` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L126)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`RoPE`](../common/rope.md#RoPE), [`Config`](../common/rope.md#RoPE.Config), [`Config`](compressor.md#Compressor.Config), [`Compressor`](compressor.md#Compressor)
- used by: [`_make_indexer_config`](__init__.md#_make_indexer_config), [`indexer`](attention.md#Attention.Config.indexer), [`compressor`](compressor.md#Indexer.compressor), [`rope`](compressor.md#Indexer.rope), [`weights_proj`](compressor.md#Indexer.weights_proj), [`wq_b`](compressor.md#Indexer.wq_b), [`head_dim`](compressor.md#Indexer.head_dim), [`num_index_heads`](compressor.md#Indexer.num_index_heads), [`rope_head_dim`](compressor.md#Indexer.rope_head_dim), [`softmax_scale`](compressor.md#Indexer.softmax_scale), [`__init__`](compressor.md#Indexer.__init__)

## Functions
- <a id="_hadamard"></a>`_hadamard(dim: int, dtype: torch.dtype, device: torch.device)` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/compressor.py#L22)

