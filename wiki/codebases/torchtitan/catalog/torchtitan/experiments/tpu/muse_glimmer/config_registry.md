---
title: 'Module: torchtitan/experiments/tpu/muse_glimmer/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/muse_glimmer/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.muse_glimmer.config_registry`/
symbols:
  _muse_glimmer_30b_base: _muse_glimmer_30b_base().
  muse_glimmer_debugmodel: muse_glimmer_debugmodel().
  muse_glimmer_30b_full_logits: muse_glimmer_30b_full_logits().
  reg_trainer_muse_glimmer_30b_fused_ce: reg_trainer_muse_glimmer_30b_fused_ce().
  _enable_pallas_cross_entropy: _enable_pallas_cross_entropy().
  graph_trainer_muse_glimmer_debugmodel: graph_trainer_muse_glimmer_debugmodel().
  muse_glimmer_30b_fused_ce: muse_glimmer_30b_fused_ce().
  muse_glimmer_debugmodel_fused_ce: muse_glimmer_debugmodel_fused_ce().
  _MUSE_GLIMMER_4X4X4_FLAGS: _MUSE_GLIMMER_4X4X4_FLAGS.
  _DEBUGMODEL_CONTEXT_LENGTH: _DEBUGMODEL_CONTEXT_LENGTH.
  _30B_CONTEXT_LENGTH: _30B_CONTEXT_LENGTH.
  _FUSED_LOSS_OVERRIDE: _FUSED_LOSS_OVERRIDE.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/muse_glimmer/config_registry.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py)

## Functions
- <a id="_enable_pallas_cross_entropy"></a>`_enable_pallas_cross_entropy(config: TPUTrainerConfig)` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L54) — Select the fused loss and its pre-construction LM-head override together.
- <a id="_muse_glimmer_30b_base"></a>`_muse_glimmer_30b_base()` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L144) — Model, data, optimizer and kernels shared by every 30B recipe.
- <a id="graph_trainer_muse_glimmer_debugmodel"></a>`graph_trainer_muse_glimmer_debugmodel()` — [`L132`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L132) — Muse Glimmer debug model using TPU GraphTrainer.
- <a id="muse_glimmer_30b_full_logits"></a>`muse_glimmer_30b_full_logits()` — [`L221`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L221) — Muse Glimmer 30B GraphTrainer recipe for a tpu7x-4x4x4 slice. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="muse_glimmer_30b_fused_ce"></a>`muse_glimmer_30b_fused_ce()` — [`L269`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L269) — ``muse_glimmer_30b_full_logits`` with the soft-capped fused loss.
- <a id="muse_glimmer_debugmodel"></a>`muse_glimmer_debugmodel()` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L72) — Muse Glimmer debug model (8 layers, dim 256) on TPU with SimpleFSDP.
- <a id="muse_glimmer_debugmodel_fused_ce"></a>`muse_glimmer_debugmodel_fused_ce()` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L119) — ``muse_glimmer_debugmodel`` with the fused Pallas cross entropy.
- <a id="reg_trainer_muse_glimmer_30b_fused_ce"></a>`reg_trainer_muse_glimmer_30b_fused_ce()` — [`L286`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L286) — Muse Glimmer 30B on the regular ``TPUTrainer`` with the fused loss.

## Module values
- <a id="_30B_CONTEXT_LENGTH"></a>`_30B_CONTEXT_LENGTH` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L36)
- <a id="_DEBUGMODEL_CONTEXT_LENGTH"></a>`_DEBUGMODEL_CONTEXT_LENGTH` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L33)
- <a id="_FUSED_LOSS_OVERRIDE"></a>`_FUSED_LOSS_OVERRIDE` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L39)
- <a id="_MUSE_GLIMMER_4X4X4_FLAGS"></a>`_MUSE_GLIMMER_4X4X4_FLAGS` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L46)
- <a id="__all__"></a>`__all__` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/config_registry.py#L24)

