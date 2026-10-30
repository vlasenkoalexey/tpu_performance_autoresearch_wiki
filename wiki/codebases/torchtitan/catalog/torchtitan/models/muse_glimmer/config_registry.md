---
title: 'Module: torchtitan/models/muse_glimmer/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/models/muse_glimmer/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.muse_glimmer.config_registry`/
symbols:
  muse_glimmer_debugmodel: muse_glimmer_debugmodel().
  muse_glimmer_debugmodel_mm: muse_glimmer_debugmodel_mm().
  muse_glimmer_30b: muse_glimmer_30b().
  muse_glimmer_30b_mm: muse_glimmer_30b_mm().
  _muse_glimmer_mm_dataloader: _muse_glimmer_mm_dataloader().
  MUSE_GLIMMER_SPECIAL_TOKENS: MUSE_GLIMMER_SPECIAL_TOKENS.
---
# Module: [`torchtitan/models/muse_glimmer/config_registry.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/config_registry.py)

## Functions
- <a id="_muse_glimmer_mm_dataloader"></a>`_muse_glimmer_mm_dataloader(model_spec: ModelSpec, dataset_name: str)` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/config_registry.py#L41) — Build the shared multimodal dataloader config, taking the vision-patch — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="muse_glimmer_30b"></a>`muse_glimmer_30b(seq_len: int | None = None)` — [`L205`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/config_registry.py#L205) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="muse_glimmer_30b_mm"></a>`muse_glimmer_30b_mm(seq_len: int | None = None)` — [`L243`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/config_registry.py#L243) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="muse_glimmer_debugmodel"></a>`muse_glimmer_debugmodel(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/config_registry.py#L113) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="muse_glimmer_debugmodel_mm"></a>`muse_glimmer_debugmodel_mm(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/config_registry.py#L154) — Multimodal debug training config. — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)

## Module values
- <a id="MUSE_GLIMMER_SPECIAL_TOKENS"></a>`MUSE_GLIMMER_SPECIAL_TOKENS` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/config_registry.py#L32)

