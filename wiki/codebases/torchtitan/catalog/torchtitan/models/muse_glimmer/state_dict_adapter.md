---
title: 'Module: torchtitan/models/muse_glimmer/state_dict_adapter.py'
type: catalog
provenance: extracted
module: torchtitan/models/muse_glimmer/state_dict_adapter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.muse_glimmer.state_dict_adapter`/
symbols:
  MuseGlimmerStateDictAdapter.from_hf: MuseGlimmerStateDictAdapter#from_hf().
  MuseGlimmerStateDictAdapter.to_hf: MuseGlimmerStateDictAdapter#to_hf().
  MuseGlimmerStateDictAdapter.model_config: MuseGlimmerStateDictAdapter#model_config.
  MuseGlimmerStateDictAdapter._attn_geometry: MuseGlimmerStateDictAdapter#_attn_geometry().
  MuseGlimmerStateDictAdapter._vision_num_heads: MuseGlimmerStateDictAdapter#_vision_num_heads().
  MuseGlimmerStateDictAdapter: MuseGlimmerStateDictAdapter#
  MuseGlimmerStateDictAdapter.__init__: MuseGlimmerStateDictAdapter#__init__().
  _dtensor_safe: _dtensor_safe().
  MuseGlimmerStateDictAdapter._permute: MuseGlimmerStateDictAdapter#_permute().
  MuseGlimmerStateDictAdapter._reverse_permute: MuseGlimmerStateDictAdapter#_reverse_permute().
  _HF_VISION_PREFIX: _HF_VISION_PREFIX.
  MuseGlimmerStateDictAdapter._permute_1d: MuseGlimmerStateDictAdapter#_permute_1d().
  MuseGlimmerStateDictAdapter._reverse_permute_1d: MuseGlimmerStateDictAdapter#_reverse_permute_1d().
  _HF_TEXT_PREFIX: _HF_TEXT_PREFIX.
  MuseGlimmerStateDictAdapter.from_hf_map: MuseGlimmerStateDictAdapter#from_hf_map.
  _dtensor_safe.wrapper: _dtensor_safe().wrapper().
---
# Module: [`torchtitan/models/muse_glimmer/state_dict_adapter.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py)

## Classes
### <a id="MuseGlimmerStateDictAdapter"></a>`MuseGlimmerStateDictAdapter`  ·  implements/extends StateDictAdapter
- def: [`torchtitan/models/muse_glimmer/state_dict_adapter.py:106`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L106)
- signature: `class MuseGlimmerStateDictAdapter(StateDictAdapter):`
- members:
  - <a id="MuseGlimmerStateDictAdapter._permute"></a>`_permute(self, w, n_heads_arg, dim1=None, dim2=None)` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L178) — native (interleaved) -> HF (split-half) row order for q/k.
  - <a id="MuseGlimmerStateDictAdapter._permute_1d"></a>`_permute_1d(self, w, n_heads_arg)` — [`L206`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L206) — Permute a 1D bias/vector (split-half -> interleaved, and inverse via
  - <a id="MuseGlimmerStateDictAdapter._reverse_permute"></a>`_reverse_permute(self, w, n_heads_arg, dim1=None, dim2=None)` — [`L192`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L192) — HF (split-half) -> native (interleaved) row order for q/k.
  - <a id="MuseGlimmerStateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L279`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L279) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="MuseGlimmerStateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L242`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L242)
  - <a id="MuseGlimmerStateDictAdapter.from_hf_map"></a>`from_hf_map` — [`L119`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L119)
  - <a id="MuseGlimmerStateDictAdapter.model_config"></a>`model_config` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L113) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- protocol/private: <a id="MuseGlimmerStateDictAdapter.__init__"></a>`__init__`[`L107`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L107), <a id="MuseGlimmerStateDictAdapter._attn_geometry"></a>`_attn_geometry`[`L227`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L227), <a id="MuseGlimmerStateDictAdapter._reverse_permute_1d"></a>`_reverse_permute_1d`[`L218`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L218), <a id="MuseGlimmerStateDictAdapter._vision_num_heads"></a>`_vision_num_heads`[`L237`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L237)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`ComplexRoPE`](../common/rope.md#ComplexRoPE), [`MuseGlimmerModel`](model.md#MuseGlimmerModel), [`Config`](../common/rope.md#ComplexRoPE.Config), [`StateDictAdapter`](../../protocols/state_dict_adapter.md#StateDictAdapter), [`Config`](model.md#MuseGlimmerModel.Config), [`__init__`](../../protocols/state_dict_adapter.md#StateDictAdapter.__init__), [`vision_encoder`](model.md#MuseGlimmerModel.Config.vision_encoder), [`hf_assets_path`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.hf_assets_path), [`dim`](model.md#MuseGlimmerModel.Config.dim), [`_validate_hf_rope_config`](../../protocols/state_dict_adapter.md#StateDictAdapter._validate_hf_rope_config), [`_dtensor_safe`](state_dict_adapter.md#_dtensor_safe), [`_HF_VISION_PREFIX`](state_dict_adapter.md#_HF_VISION_PREFIX), [`_HF_TEXT_PREFIX`](state_dict_adapter.md#_HF_TEXT_PREFIX), [`num_heads`](vision_encoder.md#MuseGlimmerVisionEncoder.Config.num_heads)
- used by: [`model_registry`](../../experiments/tpu/muse_glimmer/__init__.md#model_registry), [`model_registry`](__init__.md#model_registry), [`StateDictAdapter`](../../protocols/state_dict_adapter.md#StateDictAdapter), [`to_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf)  (1 test-only)

## Functions
- <a id="_dtensor_safe"></a>`_dtensor_safe(fn)` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L76) — Run a row-reshaping permute that is invalid on a tensor sharded along the
- <a id="_dtensor_safe.wrapper"></a>`wrapper(self, w, *args, **kwargs)` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L89)

## Module values
- <a id="_HF_TEXT_PREFIX"></a>`_HF_TEXT_PREFIX` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L72)
- <a id="_HF_VISION_PREFIX"></a>`_HF_VISION_PREFIX` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/state_dict_adapter.py#L73)

