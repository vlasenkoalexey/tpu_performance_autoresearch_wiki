---
title: 'Module: torchtitan/models/qwen3_5/rope.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3_5/rope.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3_5.rope`/MRoPE#
symbols:
  MRoPE.Config: Config#
  MRoPE: ''
  MRoPE.Config.mrope_section: Config#mrope_section.
  MRoPE._compute_mrope_cache: _compute_mrope_cache().
  MRoPE.__init__: __init__().
  MRoPE._reshape_cache: _reshape_cache().
---
# Module: [`torchtitan/models/qwen3_5/rope.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/rope.py)

## Classes
### <a id="MRoPE"></a>`MRoPE`  ·  implements/extends CosSinRoPE
- def: [`torchtitan/models/qwen3_5/rope.py:15`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/rope.py#L15) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- doc: Multi-dimensional RoPE for Qwen3.5 temporal/height/width positions.
- signature: `class MRoPE(CosSinRoPE):`
- members:
  - <a id="MRoPE._compute_mrope_cache"></a>`_compute_mrope_cache(self, position_ids: torch.Tensor)` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/rope.py#L66) — Build the interleaved cos/sin cache for 3D MRoPE positions.
  - <a id="MRoPE._reshape_cache"></a>`_reshape_cache(self, query: torch.Tensor, positions: torch.Tensor | None = None)` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/rope.py#L46) — Build a query-broadcastable cos/sin cache.
- protocol/private: <a id="MRoPE.__init__"></a>`__init__`[`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/rope.py#L30)
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../common/rope.md#CosSinRoPE), [`dim`](../common/rope.md#RoPE.Config.dim), [`Config`](rope.md#MRoPE.Config), [`mrope_section`](rope.md#MRoPE.Config.mrope_section), [`_reshape_cache`](../common/rope.md#CosSinRoPE._reshape_cache), [`cache`](../common/rope.md#RoPE.cache), [`_maybe_check_max_pos`](../common/rope.md#_maybe_check_max_pos), [`config`](../common/rope.md#RoPE.config), [`__init__`](../common/rope.md#RoPE.__init__)
- used by: [`_27b`](__init__.md#_27b), [`_debugmodel`](__init__.md#_debugmodel), [`_debugmodel_moe`](__init__.md#_debugmodel_moe), [`_35b_a3b`](__init__.md#_35b_a3b), [`_0_8b`](__init__.md#_0_8b), [`_122b_a10b`](__init__.md#_122b_a10b), [`_2b`](__init__.md#_2b), [`_397b_a17b`](__init__.md#_397b_a17b), [`_4b`](__init__.md#_4b), [`_9b`](__init__.md#_9b), [`CosSinRoPE`](../common/rope.md#CosSinRoPE), [`_qwen3_8_2_4t_a95b`](../qwen3_8/__init__.md#_qwen3_8_2_4t_a95b), [`_qwen35_attention_config`](__init__.md#_qwen35_attention_config), [`_build_qwen35_moe_layers`](__init__.md#_build_qwen35_moe_layers), [`_build_qwen35_layers`](__init__.md#_build_qwen35_layers), [`_reshape_cache`](../common/rope.md#CosSinRoPE._reshape_cache), [`rope`](model.md#Qwen35Attention.Config.rope)

### <a id="MRoPE.Config"></a>`MRoPE.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/rope.py:27`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/rope.py#L27)
- signature: `class Config(CosSinRoPE.Config):`
- members:
  - <a id="MRoPE.Config.mrope_section"></a>`mrope_section` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/rope.py#L28) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../common/rope.md#CosSinRoPE), [`Config`](../common/rope.md#CosSinRoPE.Config)
- used by: [`_27b`](__init__.md#_27b), [`_debugmodel`](__init__.md#_debugmodel), [`_debugmodel_moe`](__init__.md#_debugmodel_moe), [`_35b_a3b`](__init__.md#_35b_a3b), [`_0_8b`](__init__.md#_0_8b), [`_122b_a10b`](__init__.md#_122b_a10b), [`_2b`](__init__.md#_2b), [`_397b_a17b`](__init__.md#_397b_a17b), [`_4b`](__init__.md#_4b), [`_9b`](__init__.md#_9b), [`_qwen3_8_2_4t_a95b`](../qwen3_8/__init__.md#_qwen3_8_2_4t_a95b), [`_qwen35_attention_config`](__init__.md#_qwen35_attention_config), [`_build_qwen35_moe_layers`](__init__.md#_build_qwen35_moe_layers), [`_build_qwen35_layers`](__init__.md#_build_qwen35_layers), [`_compute_mrope_cache`](rope.md#MRoPE._compute_mrope_cache), [`__init__`](rope.md#MRoPE.__init__), [`rope`](model.md#Qwen35Attention.Config.rope)

