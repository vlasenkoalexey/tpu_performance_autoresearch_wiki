---
title: 'Module: src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.qwen4_exp.ple`/
symbols:
  Qwen4ExpPLELayer.forward: Qwen4ExpPLELayer#forward().
  Qwen4ExpNGramEmbedding.forward: Qwen4ExpNGramEmbedding#forward().
  Qwen4ExpNGramEmbedding.load_weights: Qwen4ExpNGramEmbedding#load_weights().
  layer_multipliers: layer_multipliers().
  Qwen4ExpNGramEmbedding.split_ngram_parts: Qwen4ExpNGramEmbedding#split_ngram_parts.
  _splitmix64: _splitmix64().
  Qwen4ExpPLETable.local_rows: Qwen4ExpPLETable#local_rows().
  _MASK64: _MASK64.
  Qwen4ExpNGramEmbedding.ngram_embedding: Qwen4ExpNGramEmbedding#ngram_embedding.
  head_vocab_sizes: head_vocab_sizes().
  Qwen4ExpPLELayer.ple_embedding: Qwen4ExpPLELayer#ple_embedding.
  Qwen4ExpPLELayer.conv1d: Qwen4ExpPLELayer#conv1d.
  PLEInputs.input_ids: PLEInputs#input_ids.
  Qwen4ExpPLETable.embedding_method: Qwen4ExpPLETable#embedding_method.
  Qwen4ExpNGramEmbedding.ngram_size: Qwen4ExpNGramEmbedding#ngram_size.
  Qwen4ExpPLELayer: Qwen4ExpPLELayer#
  Qwen4ExpPLELayer.conv_dilation: Qwen4ExpPLELayer#conv_dilation.
  Qwen4ExpPLETable.forward: Qwen4ExpPLETable#forward().
  Qwen4ExpPLELayer.conv_state_len: Qwen4ExpPLELayer#conv_state_len.
  _MAX_INT64: _MAX_INT64.
  _SPLITMIX_GAMMA: _SPLITMIX_GAMMA.
  PLEInputs.query_start_loc: PLEInputs#query_start_loc.
  Qwen4ExpNGramEmbedding.layer_multipliers: Qwen4ExpNGramEmbedding#layer_multipliers.
  Qwen4ExpNGramEmbedding.vocab_size: Qwen4ExpNGramEmbedding#vocab_size.
  Qwen4ExpPLELayer.hidden_size: Qwen4ExpPLELayer#hidden_size.
  _SPLITMIX_M1: _SPLITMIX_M1.
  _SPLITMIX_M2: _SPLITMIX_M2.
  _PLE_LAYER_PRIME: _PLE_LAYER_PRIME.
  _DEFAULT_SEED: _DEFAULT_SEED.
  _is_prime: _is_prime().
  token_requests: token_requests().
  ngram_ids: ngram_ids().
  dilated_short_conv: dilated_short_conv().
  PLEInputs: PLEInputs#
  PLEInputs.ngram_context: PLEInputs#ngram_context.
  Qwen4ExpPLETable: Qwen4ExpPLETable#
  Qwen4ExpPLETable.output_dtype: Qwen4ExpPLETable#output_dtype.
  Qwen4ExpNGramEmbedding: Qwen4ExpNGramEmbedding#
  Qwen4ExpNGramEmbedding.ngram_heads_vocab_sizes: Qwen4ExpNGramEmbedding#ngram_heads_vocab_sizes.
  Qwen4ExpNGramEmbedding.ngram_heads_offsets: Qwen4ExpNGramEmbedding#ngram_heads_offsets.
  Qwen4ExpNGramEmbedding.eos_token_id: Qwen4ExpNGramEmbedding#eos_token_id.
  Qwen4ExpNGramEmbedding.heads_per_ngram: Qwen4ExpNGramEmbedding#heads_per_ngram.
  Qwen4ExpPLELayer.hc_count: Qwen4ExpPLELayer#hc_count.
  Qwen4ExpPLELayer.key_proj: Qwen4ExpPLELayer#key_proj.
  Qwen4ExpPLELayer.value_proj: Qwen4ExpPLELayer#value_proj.
  Qwen4ExpPLELayer.norm_key: Qwen4ExpPLELayer#norm_key.
  Qwen4ExpPLELayer.norm_query: Qwen4ExpPLELayer#norm_query.
  Qwen4ExpPLELayer.norm_conv: Qwen4ExpPLELayer#norm_conv.
  Qwen4ExpPLETable.__init__: Qwen4ExpPLETable#__init__().
  Qwen4ExpPLETable.allocate_embedding_weight: Qwen4ExpPLETable#allocate_embedding_weight().
  Qwen4ExpNGramEmbedding.__init__: Qwen4ExpNGramEmbedding#__init__().
  Qwen4ExpPLELayer.__init__: Qwen4ExpPLELayer#__init__().
---
# Module: [`src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py)

## Classes
### <a id="PLEInputs"></a>`PLEInputs`
- def: [`src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py:232`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L232)
- doc: Per-step token inputs for one batch.
- signature: `class PLEInputs:`
- members:
  - <a id="PLEInputs.input_ids"></a>`input_ids` — [`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L242)
  - <a id="PLEInputs.ngram_context"></a>`ngram_context` — [`L244`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L244)
  - <a id="PLEInputs.query_start_loc"></a>`query_start_loc` — [`L243`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L243)
- used by: [`forward`](ple.md#Qwen4ExpPLELayer.forward)

### <a id="Qwen4ExpNGramEmbedding"></a>`Qwen4ExpNGramEmbedding`
- def: [`src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py:309`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L309)
- doc: Hashes each token's bigram and trigram into the PLE table.
- signature: `class Qwen4ExpNGramEmbedding(nn.Module):`
- members:
  - <a id="Qwen4ExpNGramEmbedding.forward"></a>`forward(self, input_ids: torch.Tensor, ngram_context: torch.Tensor, request: torch.Tensor, chunk_pos: torch.Tensor)` — [`L372`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L372)
  - <a id="Qwen4ExpNGramEmbedding.load_weights"></a>`load_weights(self, weights: Iterable[tuple[str, torch.Tensor]])` — [`L398`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L398) — Load the hash buffers, the table scale and the split table rows.
  - <a id="Qwen4ExpNGramEmbedding.eos_token_id"></a>`eos_token_id` — [`L337`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L337)
  - <a id="Qwen4ExpNGramEmbedding.heads_per_ngram"></a>`heads_per_ngram` — [`L339`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L339)
  - <a id="Qwen4ExpNGramEmbedding.layer_multipliers"></a>`layer_multipliers` — [`L312`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L312)
  - <a id="Qwen4ExpNGramEmbedding.ngram_embedding"></a>`ngram_embedding` — [`L360`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L360)
  - <a id="Qwen4ExpNGramEmbedding.ngram_heads_offsets"></a>`ngram_heads_offsets` — [`L314`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L314)
  - <a id="Qwen4ExpNGramEmbedding.ngram_heads_vocab_sizes"></a>`ngram_heads_vocab_sizes` — [`L313`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L313)
  - <a id="Qwen4ExpNGramEmbedding.ngram_size"></a>`ngram_size` — [`L338`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L338)
  - <a id="Qwen4ExpNGramEmbedding.split_ngram_parts"></a>`split_ngram_parts` — [`L343`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L343)
  - <a id="Qwen4ExpNGramEmbedding.vocab_size"></a>`vocab_size` — [`L340`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L340)
- protocol/private: <a id="Qwen4ExpNGramEmbedding.__init__"></a>`__init__`[`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L316)
- uses (calls/refs, reference-scoped): [`layer_multipliers`](ple.md#layer_multipliers), [`head_vocab_sizes`](ple.md#head_vocab_sizes), [`embedding_method`](ple.md#Qwen4ExpPLETable.embedding_method), [`_MAX_INT64`](ple.md#_MAX_INT64), [`Qwen4ExpPLETable`](ple.md#Qwen4ExpPLETable), [`_DEFAULT_SEED`](ple.md#_DEFAULT_SEED), [`ngram_ids`](ple.md#ngram_ids)
- used by: [`ple_embedding`](ple.md#Qwen4ExpPLELayer.ple_embedding)

### <a id="Qwen4ExpPLELayer"></a>`Qwen4ExpPLELayer`
- def: [`src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py:461`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L461)
- doc: Adds gated n-gram features, then a dilated short conv, to every stream.
- signature: `class Qwen4ExpPLELayer(nn.Module):`
- members:
  - <a id="Qwen4ExpPLELayer.forward"></a>`forward(self, hidden_states: torch.Tensor, inputs: PLEInputs, conv_windows: torch.Tensor)` — [`L526`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L526) — Returns the term to add to the hc_count * hidden_size residual, and — documented in [vllm-model-patches](../../../../../../concepts/vllm-model-patches.md)
  - <a id="Qwen4ExpPLELayer.conv1d"></a>`conv1d` — [`L516`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L516)
  - <a id="Qwen4ExpPLELayer.conv_dilation"></a>`conv_dilation` — [`L484`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L484)
  - <a id="Qwen4ExpPLELayer.conv_state_len"></a>`conv_state_len` — [`L485`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L485)
  - <a id="Qwen4ExpPLELayer.hc_count"></a>`hc_count` — [`L478`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L478)
  - <a id="Qwen4ExpPLELayer.hidden_size"></a>`hidden_size` — [`L477`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L477)
  - <a id="Qwen4ExpPLELayer.key_proj"></a>`key_proj` — [`L493`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L493)
  - <a id="Qwen4ExpPLELayer.norm_conv"></a>`norm_conv` — [`L508`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L508)
  - <a id="Qwen4ExpPLELayer.norm_key"></a>`norm_key` — [`L508`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L508)
  - <a id="Qwen4ExpPLELayer.norm_query"></a>`norm_query` — [`L508`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L508)
  - <a id="Qwen4ExpPLELayer.ple_embedding"></a>`ple_embedding` — [`L486`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L486)
  - <a id="Qwen4ExpPLELayer.value_proj"></a>`value_proj` — [`L500`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L500)
- protocol/private: <a id="Qwen4ExpPLELayer.__init__"></a>`__init__`[`L464`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L464)
- uses (calls/refs, reference-scoped): [`input_ids`](ple.md#PLEInputs.input_ids), [`query_start_loc`](ple.md#PLEInputs.query_start_loc), [`PLEInputs`](ple.md#PLEInputs), [`Qwen4ExpNGramEmbedding`](ple.md#Qwen4ExpNGramEmbedding), [`dilated_short_conv`](ple.md#dilated_short_conv), [`ngram_context`](ple.md#PLEInputs.ngram_context), [`token_requests`](ple.md#token_requests)
- used by: [`ple`](model.md#Qwen4ExpDecoderLayer.ple), [`load_weights`](model.md#Qwen4ExpForCausalLM.load_weights)

### <a id="Qwen4ExpPLETable"></a>`Qwen4ExpPLETable`
- def: [`src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py:247`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L247)
- doc: N-gram table split by rows across TP ranks.
- signature: `class Qwen4ExpPLETable(PLEVocabParallelEmbedding):`
- members:
  - <a id="Qwen4ExpPLETable.allocate_embedding_weight"></a>`allocate_embedding_weight(self, num_embeddings: int, embedding_dim: int, dtype: torch.dtype)` — [`L273`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L273) — Storage for this rank's rows, called by the embedding method.
  - <a id="Qwen4ExpPLETable.forward"></a>`forward(self, input_: torch.Tensor)` — [`L302`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L302)
  - <a id="Qwen4ExpPLETable.local_rows"></a>`local_rows(self, ids: torch.Tensor)` — [`L279`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L279) — Rows owned by this rank; rows of other ranks come back as zeros.
  - <a id="Qwen4ExpPLETable.embedding_method"></a>`embedding_method` — [`L270`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L270)
  - <a id="Qwen4ExpPLETable.output_dtype"></a>`output_dtype` — [`L271`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L271)
- protocol/private: <a id="Qwen4ExpPLETable.__init__"></a>`__init__`[`L254`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L254)
- used by: [`load_weights`](ple.md#Qwen4ExpNGramEmbedding.load_weights), [`ngram_embedding`](ple.md#Qwen4ExpNGramEmbedding.ngram_embedding)

## Functions
- <a id="_is_prime"></a>`_is_prime(value: int)` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L78)
- <a id="_splitmix64"></a>`_splitmix64(value: int)` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L55)
- <a id="dilated_short_conv"></a>`dilated_short_conv(x: torch.Tensor, weight: torch.Tensor, dilation: int, windows: torch.Tensor, query_start_loc: torch.Tensor, request: torch.Tensor, chunk_pos: torch.Tensor)` — [`L177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L177) — Depthwise causal conv over a ragged batch that carries each request's
- <a id="head_vocab_sizes"></a>`head_vocab_sizes(ngram_vocab_size_base: int, ngram_heads: int, ple_layer_index: int)` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L86) — Each head hashes into its own prime-sized slice of the table.
- <a id="layer_multipliers"></a>`layer_multipliers(vocab_size: int, ngram_size: int, ple_layer_index: int, seed: int)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L62) — Odd hash multipliers small enough that token * multiplier fits int64.
- <a id="ngram_ids"></a>`ngram_ids(input_ids: torch.Tensor, ngram_context: torch.Tensor, request: torch.Tensor, chunk_pos: torch.Tensor, multipliers: torch.Tensor, vocab_sizes: torch.Tensor, offsets: torch.Tensor, *, eos_token_id: int, heads_per_ngram: int)` — [`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L129) — Table rows for every head of every token, shape [num_tokens, heads].
- <a id="token_requests"></a>`token_requests(query_start_loc: torch.Tensor, num_tokens: int)` — [`L105`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L105) — Each token's request and its offset within that request's chunk.

## Module values
- <a id="_DEFAULT_SEED"></a>`_DEFAULT_SEED` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L52)
- <a id="_MASK64"></a>`_MASK64` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L46)
- <a id="_MAX_INT64"></a>`_MAX_INT64` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L47)
- <a id="_PLE_LAYER_PRIME"></a>`_PLE_LAYER_PRIME` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L51)
- <a id="_SPLITMIX_GAMMA"></a>`_SPLITMIX_GAMMA` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L48)
- <a id="_SPLITMIX_M1"></a>`_SPLITMIX_M1` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L49)
- <a id="_SPLITMIX_M2"></a>`_SPLITMIX_M2` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py#L50)

