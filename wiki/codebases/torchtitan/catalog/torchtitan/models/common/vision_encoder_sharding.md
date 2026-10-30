---
title: 'Module: torchtitan/models/common/vision_encoder_sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/vision_encoder_sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.vision_encoder_sharding`/
symbols:
  set_vision_transformer_block_sharding_config: set_vision_transformer_block_sharding_config().
  vision_scaled_bias_rowwise_config: vision_scaled_bias_rowwise_config().
  invariant_norm_config: invariant_norm_config().
  vision_invariant_linear_config: vision_invariant_linear_config().
  _vision_activation_placement: _vision_activation_placement().
  vision_colwise_config: vision_colwise_config().
  _vision_state_placement: _vision_state_placement().
  DP: DP.
  TP: TP.
  CP: CP.
  multimodal_input_sharding: multimodal_input_sharding().
---
# Module: [`torchtitan/models/common/vision_encoder_sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py)

## Functions
- <a id="_vision_activation_placement"></a>`_vision_activation_placement(*, dp: spmd.PerMeshAxisSpmdType = spmd.V, tp: spmd.PerMeshAxisSpmdType = spmd.I, include_cp_axis: bool = False)` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L37)
- <a id="_vision_state_placement"></a>`_vision_state_placement(*, tp: spmd.PerMeshAxisSpmdType, include_cp_axis: bool = False)` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L27)
- <a id="invariant_norm_config"></a>`invariant_norm_config(*, include_cp_axis: bool = False)` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L65) — Norm whose state and activations are invariant across TP ranks.
- <a id="multimodal_input_sharding"></a>`multimodal_input_sharding(*, include_cp_axis: bool = False)` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L48) — SPMD layouts for VLM vision inputs (folded into a model's input_sharding).
- <a id="set_vision_transformer_block_sharding_config"></a>`set_vision_transformer_block_sharding_config(block: VisionTransformerBlock.Config, *, rope_cache_dp: spmd.PerMeshAxisSpmdType, include_cp_axis: bool = False)` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L169) — Set TP sharding for the common vision transformer block. — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- <a id="vision_colwise_config"></a>`vision_colwise_config(*, input_tp: spmd.PerMeshAxisSpmdType = spmd.I, include_cp_axis: bool = False)` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L105) — Colwise vision linear with a TP-replicated local matmul input.
- <a id="vision_invariant_linear_config"></a>`vision_invariant_linear_config(*, include_cp_axis: bool = False)` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L85) — Unsharded linear whose state and activations are invariant at TP.
- <a id="vision_scaled_bias_rowwise_config"></a>`vision_scaled_bias_rowwise_config(*, include_cp_axis: bool = False)` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L136) — Scaled-bias rowwise vision linear returning a TP-invariant activation.

## Module values
- <a id="CP"></a>`CP` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L23)
- <a id="DP"></a>`DP` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L22)
- <a id="TP"></a>`TP` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/vision_encoder_sharding.py#L24)

