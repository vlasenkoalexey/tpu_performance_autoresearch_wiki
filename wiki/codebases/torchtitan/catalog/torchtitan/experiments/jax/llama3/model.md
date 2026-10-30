---
title: 'Module: torchtitan/experiments/jax/llama3/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/jax/llama3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.jax.llama3.model`/
symbols:
  llama3_8b: llama3_8b.
  llama3_70b: llama3_70b.
  Attention.__call__: Attention#__call__().
  llama3_debug: llama3_debug.
  ModelArgs.dim: ModelArgs#dim.
  Transformer.__call__: Transformer#__call__().
  ModelArgs: ModelArgs#
  Transformer.layers: Transformer#layers.
  ScannedTransformerBlocks.__call__: ScannedTransformerBlocks#__call__().
  ModelArgs.head_dim: ModelArgs#head_dim().
  Transformer.freqs_cis: Transformer#freqs_cis.
  ModelArgs.hidden_dim: ModelArgs#hidden_dim().
  TransformerBlock.__call__: TransformerBlock#__call__().
  Attention.wq: Attention#wq.
  Attention.wk: Attention#wk.
  Attention.wv: Attention#wv.
  Attention.wo: Attention#wo.
  TransformerBlock.attention_norm: TransformerBlock#attention_norm.
  TransformerBlock.ffn_norm: TransformerBlock#ffn_norm.
  Transformer.norm: Transformer#norm.
  ModelArgs.n_heads: ModelArgs#n_heads.
  Attention.head_dim: Attention#head_dim.
  FeedForward.__call__: FeedForward#__call__().
  ModelArgs.n_kv_heads: ModelArgs#n_kv_heads.
  ModelArgs.multiple_of: ModelArgs#multiple_of.
  ModelArgs.n_rep: ModelArgs#n_rep().
  FeedForward.w1: FeedForward#w1.
  FeedForward.w2: FeedForward#w2.
  FeedForward.w3: FeedForward#w3.
  Transformer.tok_embeddings: Transformer#tok_embeddings.
  Transformer.output: Transformer#output.
  ModelArgs.n_layers: ModelArgs#n_layers.
  ModelArgs.vocab_size: ModelArgs#vocab_size.
  ModelArgs.norm_eps: ModelArgs#norm_eps.
  RMSNorm.__call__: RMSNorm#__call__().
  Attention.n_heads: Attention#n_heads.
  Attention.n_kv_heads: Attention#n_kv_heads.
  Attention.n_rep: Attention#n_rep.
  ModelArgs.ffn_dim_multiplier: ModelArgs#ffn_dim_multiplier.
  TransformerBlock.attention: TransformerBlock#attention.
  TransformerBlock.feed_forward: TransformerBlock#feed_forward.
  _get_block_param_paths: _get_block_param_paths().
  ScannedTransformerBlocks.checkpoint_policy: ScannedTransformerBlocks#checkpoint_policy.
  ScannedTransformerBlocks._treedef: ScannedTransformerBlocks#_treedef.
  ScannedTransformerBlocks._param_attr_names: ScannedTransformerBlocks#_param_attr_names.
  ModelArgs.rope_theta: ModelArgs#rope_theta.
  RMSNorm: RMSNorm#
  TransformerBlock: TransformerBlock#
  ScannedTransformerBlocks.scan_fn: ScannedTransformerBlocks#scan_fn().
  Attention.__init__: Attention#__init__().
  FeedForward.__init__: FeedForward#__init__().
  TransformerBlock.__init__: TransformerBlock#__init__().
  ScannedTransformerBlocks.__init__: ScannedTransformerBlocks#__init__().
  Transformer.__init__: Transformer#__init__().
  ModelArgs.max_seq_len: ModelArgs#max_seq_len.
  apply_rotary_emb: apply_rotary_emb().
  Attention._attn_fn: Attention#_attn_fn.
  ScannedTransformerBlocks: ScannedTransformerBlocks#
  Transformer: Transformer#
  precompute_freqs_cis: precompute_freqs_cis().
  RMSNorm.weight: RMSNorm#weight.
  RMSNorm.eps: RMSNorm#eps.
  Attention: Attention#
  FeedForward: FeedForward#
  _get_block_param_paths._collect: _get_block_param_paths()._collect().
  ScannedTransformerBlocks._graphdef: ScannedTransformerBlocks#_graphdef.
  ModelArgs.build: ModelArgs#build().
  RMSNorm.__init__: RMSNorm#__init__().
  ScannedTransformerBlocks.n_layers: ScannedTransformerBlocks#n_layers.
  Transformer.args: Transformer#args.
---
# Module: [`torchtitan/experiments/jax/llama3/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py)

## Classes
### <a id="Attention"></a>`Attention`  ·  implements/extends Module
- def: [`torchtitan/experiments/jax/llama3/model.py:170`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L170)
- doc: Multi-head attention with Grouped Query Attention (GQA).
- signature: `class Attention(nnx.Module):`
- members:
  - <a id="Attention.head_dim"></a>`head_dim` — [`L184`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L184)
  - <a id="Attention.n_heads"></a>`n_heads` — [`L181`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L181)
  - <a id="Attention.n_kv_heads"></a>`n_kv_heads` — [`L182`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L182)
  - <a id="Attention.n_rep"></a>`n_rep` — [`L183`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L183)
  - <a id="Attention.wk"></a>`wk` — [`L191`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L191)
  - <a id="Attention.wo"></a>`wo` — [`L201`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L201)
  - <a id="Attention.wq"></a>`wq` — [`L186`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L186)
  - <a id="Attention.wv"></a>`wv` — [`L196`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L196)
- protocol/private: <a id="Attention.__call__"></a>`__call__`[`L209`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L209), <a id="Attention.__init__"></a>`__init__`[`L173`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L173), <a id="Attention._attn_fn"></a>`_attn_fn`[`L207`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L207)
- uses (calls/refs, reference-scoped): [`dim`](model.md#ModelArgs.dim), [`ModelArgs`](model.md#ModelArgs), [`head_dim`](model.md#ModelArgs.head_dim), [`n_heads`](model.md#ModelArgs.n_heads), [`n_kv_heads`](model.md#ModelArgs.n_kv_heads), [`n_rep`](model.md#ModelArgs.n_rep), [`apply_rotary_emb`](model.md#apply_rotary_emb)
- used by: [`attention`](model.md#TransformerBlock.attention)

### <a id="FeedForward"></a>`FeedForward`  ·  implements/extends Module
- def: [`torchtitan/experiments/jax/llama3/model.py:251`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L251)
- doc: SwiGLU feed-forward network with separate gate, up, and down projections.
- signature: `class FeedForward(nnx.Module):`
- members:
  - <a id="FeedForward.w1"></a>`w1` — [`L261`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L261)
  - <a id="FeedForward.w2"></a>`w2` — [`L266`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L266)
  - <a id="FeedForward.w3"></a>`w3` — [`L271`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L271)
- protocol/private: <a id="FeedForward.__call__"></a>`__call__`[`L277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L277), <a id="FeedForward.__init__"></a>`__init__`[`L254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L254)
- uses (calls/refs, reference-scoped): [`dim`](model.md#ModelArgs.dim), [`ModelArgs`](model.md#ModelArgs), [`hidden_dim`](model.md#ModelArgs.hidden_dim)
- used by: [`feed_forward`](model.md#TransformerBlock.feed_forward)

### <a id="ModelArgs"></a>`ModelArgs`  ·  implements/extends Config
- def: [`torchtitan/experiments/jax/llama3/model.py:26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L26)
- signature: `class ModelArgs(BaseModel.Config):`
- members:
  - <a id="ModelArgs.build"></a>`build(self)` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L27)
  - <a id="ModelArgs.head_dim"></a>`head_dim(self)` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L42)
  - <a id="ModelArgs.hidden_dim"></a>`hidden_dim(self)` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L46)
  - <a id="ModelArgs.n_rep"></a>`n_rep(self)` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L52) — Number of times each KV head is repeated for GQA.
  - <a id="ModelArgs.dim"></a>`dim` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L30)
  - <a id="ModelArgs.ffn_dim_multiplier"></a>`ffn_dim_multiplier` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L35)
  - <a id="ModelArgs.max_seq_len"></a>`max_seq_len` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L39)
  - <a id="ModelArgs.multiple_of"></a>`multiple_of` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L36)
  - <a id="ModelArgs.n_heads"></a>`n_heads` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L32)
  - <a id="ModelArgs.n_kv_heads"></a>`n_kv_heads` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L33)
  - <a id="ModelArgs.n_layers"></a>`n_layers` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L31)
  - <a id="ModelArgs.norm_eps"></a>`norm_eps` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L37)
  - <a id="ModelArgs.rope_theta"></a>`rope_theta` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L38)
  - <a id="ModelArgs.vocab_size"></a>`vocab_size` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L34)
- uses (calls/refs, reference-scoped): [`BaseModel`](../../../protocols/model.md#BaseModel), [`Config`](../../../protocols/model.md#BaseModel.Config)
- used by: [`setup_model`](../trainer.md#JaxTrainer.setup_model), [`llama3_70b`](model.md#llama3_70b), [`llama3_8b`](model.md#llama3_8b), [`llama3_debug`](model.md#llama3_debug), [`layers`](model.md#Transformer.layers), [`freqs_cis`](model.md#Transformer.freqs_cis), [`attention_norm`](model.md#TransformerBlock.attention_norm), [`ffn_norm`](model.md#TransformerBlock.ffn_norm), [`norm`](model.md#Transformer.norm), [`wk`](model.md#Attention.wk), [`wo`](model.md#Attention.wo), [`wq`](model.md#Attention.wq), [`wv`](model.md#Attention.wv), [`head_dim`](model.md#Attention.head_dim), [`output`](model.md#Transformer.output), [`tok_embeddings`](model.md#Transformer.tok_embeddings), [`w1`](model.md#FeedForward.w1), [`w2`](model.md#FeedForward.w2), [`w3`](model.md#FeedForward.w3), [`n_heads`](model.md#Attention.n_heads), [`n_kv_heads`](model.md#Attention.n_kv_heads), [`n_rep`](model.md#Attention.n_rep), [`__init__`](model.md#Attention.__init__), [`__init__`](model.md#FeedForward.__init__), [`__init__`](model.md#ScannedTransformerBlocks.__init__), [`__init__`](model.md#Transformer.__init__), [`__init__`](model.md#TransformerBlock.__init__)

### <a id="RMSNorm"></a>`RMSNorm`  ·  implements/extends Module
- def: [`torchtitan/experiments/jax/llama3/model.py:148`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L148)
- signature: `class RMSNorm(nnx.Module):`
- members:
  - <a id="RMSNorm.eps"></a>`eps` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L161)
  - <a id="RMSNorm.weight"></a>`weight` — [`L160`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L160)
- protocol/private: <a id="RMSNorm.__call__"></a>`__call__`[`L163`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L163), <a id="RMSNorm.__init__"></a>`__init__`[`L149`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L149)
- used by: [`attention_norm`](model.md#TransformerBlock.attention_norm), [`ffn_norm`](model.md#TransformerBlock.ffn_norm), [`norm`](model.md#Transformer.norm)

### <a id="ScannedTransformerBlocks"></a>`ScannedTransformerBlocks`  ·  implements/extends Module
- def: [`torchtitan/experiments/jax/llama3/model.py:341`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L341) — documented in [jax-lane](../../../../../concepts/jax-lane.md)
- doc: Runs N transformer blocks using jax.lax.scan with stacked parameters.
- signature: `class ScannedTransformerBlocks(nnx.Module):`
- members:
  - <a id="ScannedTransformerBlocks.scan_fn"></a>`scan_fn(carry, layer_arrays)` — [`L424`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L424)
  - <a id="ScannedTransformerBlocks.checkpoint_policy"></a>`checkpoint_policy` — [`L368`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L368)
  - <a id="ScannedTransformerBlocks.n_layers"></a>`n_layers` — [`L367`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L367)
- protocol/private: <a id="ScannedTransformerBlocks.__call__"></a>`__call__`[`L416`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L416), <a id="ScannedTransformerBlocks.__init__"></a>`__init__`[`L357`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L357), <a id="ScannedTransformerBlocks._graphdef"></a>`_graphdef`[`L375`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L375), <a id="ScannedTransformerBlocks._param_attr_names"></a>`_param_attr_names`[`L386`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L386), <a id="ScannedTransformerBlocks._treedef"></a>`_treedef`[`L380`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L380)
- uses (calls/refs, reference-scoped): [`ModelArgs`](model.md#ModelArgs), [`_get_block_param_paths`](model.md#_get_block_param_paths), [`TransformerBlock`](model.md#TransformerBlock)
- used by: [`__call__`](model.md#Transformer.__call__), [`layers`](model.md#Transformer.layers)

### <a id="Transformer"></a>`Transformer`
- def: [`torchtitan/experiments/jax/llama3/model.py:443`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L443)
- members:
  - <a id="Transformer.__call__"></a>`__call__(self, tokens: jax.Array)` — [`L496`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L496) — Forward pass. — documented in [jax-lane](../../../../../concepts/jax-lane.md)
  - <a id="Transformer.args"></a>`args` — [`L458`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L458)
  - <a id="Transformer.freqs_cis"></a>`freqs_cis` — [`L492`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L492)
  - <a id="Transformer.layers"></a>`layers` — [`L467`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L467) — documented in [jax-lane](../../../../../concepts/jax-lane.md)
  - <a id="Transformer.norm"></a>`norm` — [`L483`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L483)
  - <a id="Transformer.output"></a>`output` — [`L486`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L486)
  - <a id="Transformer.tok_embeddings"></a>`tok_embeddings` — [`L459`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L459)
- protocol/private: <a id="Transformer.__init__"></a>`__init__`[`L444`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L444)
- uses (calls/refs, reference-scoped): [`dim`](model.md#ModelArgs.dim), [`ModelArgs`](model.md#ModelArgs), [`head_dim`](model.md#ModelArgs.head_dim), [`n_layers`](model.md#ModelArgs.n_layers), [`norm_eps`](model.md#ModelArgs.norm_eps), [`vocab_size`](model.md#ModelArgs.vocab_size), [`RMSNorm`](model.md#RMSNorm), [`TransformerBlock`](model.md#TransformerBlock), [`rope_theta`](model.md#ModelArgs.rope_theta), [`ScannedTransformerBlocks`](model.md#ScannedTransformerBlocks), [`max_seq_len`](model.md#ModelArgs.max_seq_len), [`precompute_freqs_cis`](model.md#precompute_freqs_cis)
- used by: [`setup_model`](../trainer.md#JaxTrainer.setup_model)

### <a id="TransformerBlock"></a>`TransformerBlock`  ·  implements/extends Module
- def: [`torchtitan/experiments/jax/llama3/model.py:281`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L281)
- signature: `class TransformerBlock(nnx.Module):`
- members:
  - <a id="TransformerBlock.attention"></a>`attention` — [`L290`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L290)
  - <a id="TransformerBlock.attention_norm"></a>`attention_norm` — [`L294`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L294)
  - <a id="TransformerBlock.feed_forward"></a>`feed_forward` — [`L293`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L293)
  - <a id="TransformerBlock.ffn_norm"></a>`ffn_norm` — [`L297`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L297)
- protocol/private: <a id="TransformerBlock.__call__"></a>`__call__`[`L301`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L301), <a id="TransformerBlock.__init__"></a>`__init__`[`L282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L282)
- uses (calls/refs, reference-scoped): [`dim`](model.md#ModelArgs.dim), [`ModelArgs`](model.md#ModelArgs), [`norm_eps`](model.md#ModelArgs.norm_eps), [`RMSNorm`](model.md#RMSNorm), [`Attention`](model.md#Attention), [`FeedForward`](model.md#FeedForward)
- used by: [`layers`](model.md#Transformer.layers), [`_param_attr_names`](model.md#ScannedTransformerBlocks._param_attr_names), [`checkpoint_policy`](model.md#ScannedTransformerBlocks.checkpoint_policy)

## Functions
- <a id="_get_block_param_paths._collect"></a>`_collect(path, leaf)` — [`L322`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L322)
- <a id="_get_block_param_paths"></a>`_get_block_param_paths(state: nnx.State)` — [`L314`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L314) — Return path strings (e.g. 'attention/wq/kernel') for each leaf in state.
- <a id="apply_rotary_emb"></a>`apply_rotary_emb(x: jax.Array, freqs_cis: jax.Array)` — [`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L115) — Apply RoPE to query or key tensor.
- <a id="precompute_freqs_cis"></a>`precompute_freqs_cis(head_dim: int, max_seq_len: int, theta: float = 10000)` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L97) — Precompute RoPE frequency matrix.

## Module values
- <a id="llama3_70b"></a>`llama3_70b` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L80) — documented in [jax-lane](../../../../../concepts/jax-lane.md)
- <a id="llama3_8b"></a>`llama3_8b` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L68) — documented in [jax-lane](../../../../../concepts/jax-lane.md)
- <a id="llama3_debug"></a>`llama3_debug` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/llama3/model.py#L58)

