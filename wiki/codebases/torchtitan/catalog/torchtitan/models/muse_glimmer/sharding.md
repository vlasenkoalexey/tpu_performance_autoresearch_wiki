---
title: 'Module: torchtitan/models/muse_glimmer/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/muse_glimmer/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.muse_glimmer.sharding`/
symbols:
  _set_muse_glimmer_layer_sharding: _set_muse_glimmer_layer_sharding().
  set_muse_glimmer_vision_sharding_config: set_muse_glimmer_vision_sharding_config().
  _set_multimodal_sharding: _set_multimodal_sharding().
  set_muse_glimmer_sharding_config: set_muse_glimmer_sharding_config().
  _set_tok_embeddings_sharding: _set_tok_embeddings_sharding().
  DP: DP.
  CP: CP.
  TP: TP.
  vision_bank_indices_placement: vision_bank_indices_placement().
---
# Module: [`torchtitan/models/muse_glimmer/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py)

## Functions
- <a id="_set_multimodal_sharding"></a>`_set_multimodal_sharding(config: MuseGlimmerModel.Config, *, enable_sp: bool)` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L108) — Configure token-local multimodal fusion. — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_set_muse_glimmer_layer_sharding"></a>`_set_muse_glimmer_layer_sharding(layer_cfg: MuseGlimmerTransformerBlock.Config, *, enable_sp: bool)` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L127) — Set sharding on one decoder block. — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_set_tok_embeddings_sharding"></a>`_set_tok_embeddings_sharding(config: MuseGlimmerModel.Config, *, enable_sp: bool)` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L79) — Move the decoder embedding sharding onto the ``EmbeddingWithNorm`` children. — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="set_muse_glimmer_sharding_config"></a>`set_muse_glimmer_sharding_config(config: MuseGlimmerModel.Config, *, enable_sp: bool)` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L55) — Fill ``sharding_config`` on all Muse Glimmer sub-configs. — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="set_muse_glimmer_vision_sharding_config"></a>`set_muse_glimmer_vision_sharding_config(encoder_cfg: MuseGlimmerVisionEncoder.Config, adapter_cfg: MuseGlimmerVisionAdapter.Config | None = None)` — [`L183`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L183) — Fill ``sharding_config`` on the Muse Glimmer vision encoder (+ optional adapter). — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="vision_bank_indices_placement"></a>`vision_bank_indices_placement(*, enable_sp: bool)` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L42) — Placement for token-aligned indices into the packed vision bank. — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)

## Module values
- <a id="CP"></a>`CP` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L38) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="DP"></a>`DP` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L37) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="TP"></a>`TP` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/sharding.py#L39) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)

