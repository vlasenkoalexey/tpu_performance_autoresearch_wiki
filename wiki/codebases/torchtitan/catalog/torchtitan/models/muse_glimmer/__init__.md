---
title: 'Module: torchtitan/models/muse_glimmer/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/models/muse_glimmer/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.muse_glimmer`/
symbols:
  muse_glimmer_vision_encoder_config: muse_glimmer_vision_encoder_config().
  _muse_glimmer_config: _muse_glimmer_config().
  _build_muse_glimmer_attention: _build_muse_glimmer_attention().
  model_registry: model_registry().
  _build_muse_glimmer_layers: _build_muse_glimmer_layers().
  _vision_linear: _vision_linear().
  _gain_norm: _gain_norm().
  _vision_scaled_bias_rowwise_linear: _vision_scaled_bias_rowwise_linear().
  muse_glimmer_vision_configs: muse_glimmer_vision_configs().
  _vision_layer_norm: _vision_layer_norm().
  _muse_glimmer_debugmodel_mm: _muse_glimmer_debugmodel_mm().
  _scaleless_norm: _scaleless_norm().
  muse_glimmer_vision_adapter_config: muse_glimmer_vision_adapter_config().
  _muse_glimmer_30b: _muse_glimmer_30b().
  muse_glimmer_configs: muse_glimmer_configs.
  _debugmodel: _debugmodel().
  _NORM_EPS: _NORM_EPS.
  _LINEAR_INIT._LINEAR_INIT: _LINEAR_INIT._LINEAR_INIT.
  _depth_init: _depth_init().
  _layer_use_rope: _layer_use_rope().
  _layer_window_size: _layer_window_size().
  _EVERY_N_LAYERS_NOPE: _EVERY_N_LAYERS_NOPE.
  _POST_NORM_EPS: _POST_NORM_EPS.
  _VISION_LINEAR_INIT._VISION_LINEAR_INIT: _VISION_LINEAR_INIT._VISION_LINEAR_INIT.
  _SCALE_QUERY_NUMERATOR: _SCALE_QUERY_NUMERATOR.
  _ROPE_THETA: _ROPE_THETA.
  _FFN_DIM_MULTIPLIER: _FFN_DIM_MULTIPLIER.
  _output_linear_init: _output_linear_init().
  _GAIN_NORM_INIT._GAIN_NORM_INIT: _GAIN_NORM_INIT._GAIN_NORM_INIT.
  _EMBEDDING_INIT._EMBEDDING_INIT: _EMBEDDING_INIT._EMBEDDING_INIT.
  _POS_EMB_INIT._POS_EMB_INIT: _POS_EMB_INIT._POS_EMB_INIT.
  __all__: __all__.
---
# Module: [`torchtitan/models/muse_glimmer/__init__.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py)

## Functions
- <a id="_build_muse_glimmer_attention"></a>`_build_muse_glimmer_attention(*, layer_id: int, n_layers: int, dim: int, n_heads: int, n_kv_heads: int, head_dim: int, max_context_length: int, window_pattern: list[int], attn_backend: str)` — [`L134`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L134) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_build_muse_glimmer_layers"></a>`_build_muse_glimmer_layers(*, n_layers: int, dim: int, n_heads: int, n_kv_heads: int, head_dim: int, max_context_length: int, window_pattern: list[int], attn_backend: str)` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L199) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_debugmodel"></a>`_debugmodel(attn_backend: str, *, seq_len: int)` — [`L430`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L430) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_depth_init"></a>`_depth_init(layer_id: int)` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L101)
- <a id="_gain_norm"></a>`_gain_norm(dim: int, eps: float, gain_center: float)` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L108) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_layer_use_rope"></a>`_layer_use_rope(layer_id: int, n_layers: int)` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L122)
- <a id="_layer_window_size"></a>`_layer_window_size(layer_id: int, n_layers: int, pattern: list[int])` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L127)
- <a id="_muse_glimmer_30b"></a>`_muse_glimmer_30b(attn_backend: str, *, with_vision: bool = False, seq_len: int)` — [`L445`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L445) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_muse_glimmer_config"></a>`_muse_glimmer_config(*, dim: int, n_layers: int, n_heads: int, n_kv_heads: int, head_dim: int, vocab_size: int, max_context_length: int, window_pattern: list[int], output_multiplier: float, attn_backend: str, vision_adapter_dim: int | None = None, vision_encoder: MuseGlimmerVisionEncoder.Config | None = None, vision_adapter: MuseGlimmerVisionAdapter.Config | None = None)` — [`L353`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L353) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_muse_glimmer_debugmodel_mm"></a>`_muse_glimmer_debugmodel_mm(attn_backend: str, *, seq_len: int)` — [`L476`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L476) — Multimodal debug flavor: the debug text decoder that *owns* a scaled-down — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_output_linear_init"></a>`_output_linear_init(dim: int)` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L93)
- <a id="_scaleless_norm"></a>`_scaleless_norm(dim: int, eps: float)` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L117)
- <a id="_vision_layer_norm"></a>`_vision_layer_norm(dim: int)` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L241)
- <a id="_vision_linear"></a>`_vision_linear(in_features: int, out_features: int, *, bias: bool)` — [`L245`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L245) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="_vision_scaled_bias_rowwise_linear"></a>`_vision_scaled_bias_rowwise_linear(in_features: int, out_features: int)` — [`L254`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L254)
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, attn_backend: str = "flex", converters: list[ModelConfigConverter.Config] | None = None)` — [`L526`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L526) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- <a id="muse_glimmer_vision_adapter_config"></a>`muse_glimmer_vision_adapter_config(*, input_dim: int = 6144, output_dim: int = 4096)` — [`L325`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L325)
- <a id="muse_glimmer_vision_configs"></a>`muse_glimmer_vision_configs(vision_adapter_dim: int = 4096)` — [`L336`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L336) — Production (30B) vision encoder + adapter configs.
- <a id="muse_glimmer_vision_encoder_config"></a>`muse_glimmer_vision_encoder_config(*, latent_dim: int = 1536, num_layers: int = 50, num_heads: int = 16, mlp_ratio: float = 8960 / 1536, patch_size: int = 14, patch_temporal: int = 2, downsample_factor: int = 2, sparse_attention_factor: int = 4, pos_emb_grid_h: int = 32, pos_emb_grid_w: int = 32, rope_theta: float = 10000)` — [`L265`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L265) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)

## Module values
- <a id="_EMBEDDING_INIT._EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L77)
- <a id="_EVERY_N_LAYERS_NOPE"></a>`_EVERY_N_LAYERS_NOPE` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L89)
- <a id="_FFN_DIM_MULTIPLIER"></a>`_FFN_DIM_MULTIPLIER` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L90)
- <a id="_GAIN_NORM_INIT._GAIN_NORM_INIT"></a>`_GAIN_NORM_INIT` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L76)
- <a id="_LINEAR_INIT._LINEAR_INIT"></a>`_LINEAR_INIT` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L70)
- <a id="_NORM_EPS"></a>`_NORM_EPS` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L86)
- <a id="_POST_NORM_EPS"></a>`_POST_NORM_EPS` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L87)
- <a id="_POS_EMB_INIT._POS_EMB_INIT"></a>`_POS_EMB_INIT` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L82)
- <a id="_ROPE_THETA"></a>`_ROPE_THETA` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L88)
- <a id="_SCALE_QUERY_NUMERATOR"></a>`_SCALE_QUERY_NUMERATOR` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L68)
- <a id="_VISION_LINEAR_INIT._VISION_LINEAR_INIT"></a>`_VISION_LINEAR_INIT` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L78)
- <a id="__all__"></a>`__all__` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L51)
- <a id="muse_glimmer_configs"></a>`muse_glimmer_configs` — [`L518`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/__init__.py#L518)

