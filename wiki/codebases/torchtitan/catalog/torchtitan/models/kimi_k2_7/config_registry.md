---
title: 'Module: torchtitan/models/kimi_k2_7/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k2_7/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k2_7.config_registry`/
symbols:
  kimi_k2_5_debugmodel: kimi_k2_5_debugmodel().
  kimi_k2_5: kimi_k2_5().
  moonlight_16b_a3b: moonlight_16b_a3b().
  kimi_vl_a3b: kimi_vl_a3b().
  _dist_muon_optimizer: _dist_muon_optimizer().
  _kimi_multimodal_dataloader: _kimi_multimodal_dataloader().
  _per_expert_compute_layout: _per_expert_compute_layout().
  _KimiTrainerConfig.__post_init__: _KimiTrainerConfig#__post_init__().
  _align_dist_muon_expert_compute_layouts: _align_dist_muon_expert_compute_layouts().
  _KimiTrainerConfig: _KimiTrainerConfig#
  _dist_muon_optimizer.compute_shardings_for_layer: _dist_muon_optimizer().compute_shardings_for_layer().
---
# Module: [`torchtitan/models/kimi_k2_7/config_registry.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py)

## Classes
### <a id="_KimiTrainerConfig"></a>`_KimiTrainerConfig`
- def: [`torchtitan/models/kimi_k2_7/config_registry.py:519`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L519)
- protocol/private: <a id="_KimiTrainerConfig.__post_init__"></a>`__post_init__`[`L520`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L520)
- uses (calls/refs, reference-scoped): [`parallelism`](../../trainer.md#Trainer.Config.parallelism), [`Trainer`](../../trainer.md#Trainer), [`Config`](../../trainer.md#Trainer.Config), [`optimizer`](../../trainer.md#Trainer.Config.optimizer), [`tensor_parallel_degree`](../../config/configs.md#ParallelismConfig.tensor_parallel_degree), [`__post_init__`](../../trainer.md#Trainer.Config.__post_init__), [`_align_dist_muon_expert_compute_layouts`](config_registry.md#_align_dist_muon_expert_compute_layouts)
- used by: [`kimi_k2_5_debugmodel`](config_registry.md#kimi_k2_5_debugmodel), [`kimi_k2_5`](config_registry.md#kimi_k2_5), [`kimi_vl_a3b`](config_registry.md#kimi_vl_a3b), [`moonlight_16b_a3b`](config_registry.md#moonlight_16b_a3b)

## Functions
- <a id="_align_dist_muon_expert_compute_layouts"></a>`_align_dist_muon_expert_compute_layouts(optimizer_config: OptimizersContainer.Config, *, parallelism: ParallelismConfig)` — [`L472`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L472) — Align routed-expert layouts with the final parallelism config. — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="_dist_muon_optimizer"></a>`_dist_muon_optimizer(model_spec: ModelSpec, *, lr: float, parallelism: ParallelismConfig)` — [`L294`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L294) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_kimi_multimodal_dataloader"></a>`_kimi_multimodal_dataloader(dataset: SingleDatasetConfig)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L53)
- <a id="_per_expert_compute_layout"></a>`_per_expert_compute_layout(parallelism: ParallelismConfig)` — [`L267`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L267) — documented in [flex-shard](../../../../concepts/flex-shard.md)
- <a id="_dist_muon_optimizer.compute_shardings_for_layer"></a>`compute_shardings_for_layer(layer_id: int)` — [`L356`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L356)
- <a id="kimi_k2_5"></a>`kimi_k2_5(seq_len: int | None = None)` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L222) — Full Kimi K2.5 (~1T-total / ~32B-active). — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="kimi_k2_5_debugmodel"></a>`kimi_k2_5_debugmodel(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L91) — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="kimi_vl_a3b"></a>`kimi_vl_a3b(seq_len: int | None = None)` — [`L176`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L176) — Kimi-VL A3B: Moonlight text tower + 2D MoonViT vision (image-text). — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)
- <a id="moonlight_16b_a3b"></a>`moonlight_16b_a3b(seq_len: int | None = None)` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k2_7/config_registry.py#L133) — Moonlight 16B-A3B: the text-only DeepSeekV3 sibling (no vision tower). — documented in [kimi-k2-7-model](../../../../concepts/kimi-k2-7-model.md)

