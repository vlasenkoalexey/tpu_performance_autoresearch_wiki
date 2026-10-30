---
title: 'Module: torchtitan/models/common/decoder_sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/decoder_sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.decoder_sharding`/
symbols:
  dense_activation_placement: dense_activation_placement().
  dense_param_placement: dense_param_placement().
  dense_sequence_parallel_placement: dense_sequence_parallel_placement().
  set_gqa_attention_sharding: set_gqa_attention_sharding().
  set_decoder_sharding_config: set_decoder_sharding_config().
  set_dense_ffn_sharding: set_dense_ffn_sharding().
  set_gqa_inner_attention_local_map: set_gqa_inner_attention_local_map().
  norm_config: norm_config().
  colwise_config: colwise_config().
  rowwise_config: rowwise_config().
  decoder_input_sharding: decoder_input_sharding().
  set_qkv_linear_sharding: set_qkv_linear_sharding().
  pre_lm_head_norm_config: pre_lm_head_norm_config().
  token_id_placement: token_id_placement().
  DP: DP.
  CP: CP.
  attention_activation_placement: attention_activation_placement().
  TP: TP.
  token_id_sequence_parallel_placement: token_id_sequence_parallel_placement().
---
# Module: [`torchtitan/models/common/decoder_sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py)

## Functions
- <a id="attention_activation_placement"></a>`attention_activation_placement(*, cp: spmd.PerMeshAxisSpmdType = spmd.S(0))` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L92) — Placement for attention activations with shape ``(tokens, heads, dim)``.
- <a id="colwise_config"></a>`colwise_config()` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L138) — ColwiseParallel: weight S(0), output S(-1).
- <a id="decoder_input_sharding"></a>`decoder_input_sharding()` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L126) — Default ``input_sharding`` for decoder-only models.
- <a id="dense_activation_placement"></a>`dense_activation_placement(*, tp: spmd.PerMeshAxisSpmdType, cp: spmd.PerMeshAxisSpmdType)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L39) — Placement for dense-path activations. — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- <a id="dense_param_placement"></a>`dense_param_placement(*, tp: spmd.PerMeshAxisSpmdType)` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L24) — Placement for dense-path params/buffers. — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- <a id="dense_sequence_parallel_placement"></a>`dense_sequence_parallel_placement()` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L114) — Sequence-parallel ``(tokens, hidden)`` activation placement.
- <a id="norm_config"></a>`norm_config(*, enable_sp: bool)` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L169) — Norm sharding.
- <a id="pre_lm_head_norm_config"></a>`pre_lm_head_norm_config(*, enable_sp: bool)` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L187) — Root decoder norm sharding before ``lm_head`` / chunked CE loss.
- <a id="rowwise_config"></a>`rowwise_config(*, output_sp: bool = False)` — [`L149`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L149) — RowwiseParallel: weight S(1), bias R (no-op if bias absent).
- <a id="set_decoder_sharding_config"></a>`set_decoder_sharding_config(config, *, enable_sp: bool)` — [`L365`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L365) — Set sharding on root-level configs only: ``tok_embeddings``, ``norm``,
- <a id="set_dense_ffn_sharding"></a>`set_dense_ffn_sharding(feed_forward_cfg, *, attn_x_layout: SpmdType, enable_sp: bool)` — [`L329`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L329) — Standard dense FFN (``w1``/``w2``/``w3``) TP sharding.
- <a id="set_gqa_attention_sharding"></a>`set_gqa_attention_sharding(attention_cfg, *, enable_sp: bool)` — [`L228`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L228) — Standard GQA attention (``qkv_linear``/``wo``) TP sharding.
- <a id="set_gqa_inner_attention_local_map"></a>`set_gqa_inner_attention_local_map(inner_attention_cfg)` — [`L291`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L291) — Localize TNH attention inputs without changing their placements.
- <a id="set_qkv_linear_sharding"></a>`set_qkv_linear_sharding(qkv_linear_cfg)` — [`L210`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L210) — Colwise-shard each Q/K/V projection of a ``BaseQKVLinear``.
- <a id="token_id_placement"></a>`token_id_placement()` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L64) — Placement for decoder token IDs with shape ``(tokens,)``.
- <a id="token_id_sequence_parallel_placement"></a>`token_id_sequence_parallel_placement()` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L76) — Sequence-parallel token IDs with shape ``(tokens,)``.

## Module values
- <a id="CP"></a>`CP` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L20)
- <a id="DP"></a>`DP` — [`L19`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L19)
- <a id="TP"></a>`TP` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/decoder_sharding.py#L21)

