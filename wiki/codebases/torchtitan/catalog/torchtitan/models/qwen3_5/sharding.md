---
title: 'Module: torchtitan/models/qwen3_5/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3_5/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3_5.sharding`/
symbols:
  _set_deltanet_sharding: _set_deltanet_sharding().
  set_qwen35_sharding_config: set_qwen35_sharding_config().
  _set_vision_encoder_sharding: _set_vision_encoder_sharding().
  _set_full_attention_sharding: _set_full_attention_sharding().
  _set_qwen35_layer_sharding: _set_qwen35_layer_sharding().
  TP: TP.
  _set_shared_expert_gate_sharding: _set_shared_expert_gate_sharding().
  _qk_norm_sharding: _qk_norm_sharding().
  annotate_deltanet_cu_seqlens: annotate_deltanet_cu_seqlens().
  _decoder_norm_sharding: _decoder_norm_sharding().
  DP: DP.
  _conv_weight_sharding: _conv_weight_sharding().
  CP: CP.
  _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT: _GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT.
---
# Module: [`torchtitan/models/qwen3_5/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py)

## Functions
- <a id="_conv_weight_sharding"></a>`_conv_weight_sharding()` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L101) — Depthwise Conv1d weight sharded Shard(0) on out-channels (head-sharded).
- <a id="_decoder_norm_sharding"></a>`_decoder_norm_sharding(activation_layout: SpmdType)` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L93)
- <a id="_qk_norm_sharding"></a>`_qk_norm_sharding()` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L81) — Per-head QK-norm sharding: weight Replicate, activations Shard(1).
- <a id="_set_deltanet_sharding"></a>`_set_deltanet_sharding(deltanet_cfg: GatedDeltaNet.Config, *, attention_input_layout: SpmdType, enable_sp: bool)` — [`L303`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L303) — Configure head-sharded TP for GatedDeltaNet. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_set_full_attention_sharding"></a>`_set_full_attention_sharding(attention_cfg: Qwen35Attention.Config, *, attention_input_layout: SpmdType, enable_sp: bool)` — [`L274`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L274) — TP sharding for Qwen35Attention (output gating + partial RoPE). — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_set_qwen35_layer_sharding"></a>`_set_qwen35_layer_sharding(layer_cfg: Qwen35TransformerBlock.Config, *, attention_input_layout: SpmdType, enable_sp: bool, enable_ep: bool)` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L159) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_set_shared_expert_gate_sharding"></a>`_set_shared_expert_gate_sharding(shared_experts: SigmoidGatedFeedForward.Config | None, *, enable_sp: bool)` — [`L211`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L211) — Shard Qwen3.5's shared-expert sigmoid gate.
- <a id="_set_vision_encoder_sharding"></a>`_set_vision_encoder_sharding(ve_cfg: Qwen35VisionEncoder.Config)` — [`L244`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L244) — Sharding for the vision encoder. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="annotate_deltanet_cu_seqlens"></a>`annotate_deltanet_cu_seqlens(attention_masks: Qwen35AttentionMaskDict)` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L65) — Annotate the nested GatedDeltaNet ``cu_seq_q`` offsets as DP-varying.
- <a id="set_qwen35_sharding_config"></a>`set_qwen35_sharding_config(config: Qwen35Model.Config, *, enable_sp: bool, enable_ep: bool)` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L115) — Fill ``sharding_config`` on all Qwen3.5 sub-configs. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)

## Module values
- <a id="CP"></a>`CP` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L50)
- <a id="DP"></a>`DP` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L49)
- <a id="TP"></a>`TP` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L51) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- <a id="_GROUPED_EXPERTS_PARAM_LAYOUT._GROUPED_EXPERTS_PARAM_LAYOUT"></a>`_GROUPED_EXPERTS_PARAM_LAYOUT` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/sharding.py#L108)

