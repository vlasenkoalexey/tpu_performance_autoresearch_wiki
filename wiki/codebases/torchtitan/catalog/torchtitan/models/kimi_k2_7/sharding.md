---
title: 'Module: torchtitan/models/kimi_k2_7/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k2_7/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k2_7.sharding`/
symbols:
  _shard_decoder_after_embedding_scatter: _shard_decoder_after_embedding_scatter().
  _set_vision_encoder_sharding: _set_vision_encoder_sharding().
  set_kimi_k2_5_sharding_config: set_kimi_k2_5_sharding_config().
  TP: TP.
  DP: DP.
  _REPLICATE_ACT: _REPLICATE_ACT.
---
# Module: [`torchtitan/models/kimi_k2_7/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/sharding.py)

## Functions
- <a id="_set_vision_encoder_sharding"></a>`_set_vision_encoder_sharding(ve_cfg)` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/sharding.py#L96) — Invariant-activation TP plan for the MoonViT3d vision encoder. — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_shard_decoder_after_embedding_scatter"></a>`_shard_decoder_after_embedding_scatter(config: KimiK25Model.Config)` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/sharding.py#L69) — Keep ``tok_embeddings`` ``Replicate`` and resume SP at layer 0's output. — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="set_kimi_k2_5_sharding_config"></a>`set_kimi_k2_5_sharding_config(config: KimiK25Model.Config, *, enable_sp: bool, enable_ep: bool)` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/sharding.py#L52) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)

## Module values
- <a id="DP"></a>`DP` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/sharding.py#L43)
- <a id="TP"></a>`TP` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/sharding.py#L44) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_REPLICATE_ACT"></a>`_REPLICATE_ACT` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/sharding.py#L49)

