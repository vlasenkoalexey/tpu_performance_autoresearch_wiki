---
title: 'Module: torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.transformers_modeling_backend._structure`/
symbols:
  find_head: find_head().
  find_embedding: find_embedding().
  find_layers: find_layers().
  find_norm: find_norm().
  _resolve: _resolve().
  find_backbone: find_backbone().
  find_position_embedding: find_position_embedding().
  _ask_hf: _ask_hf().
  find_rotary: find_rotary().
  position_capacity: position_capacity().
  _walk: _walk().
  _LAYER_PATHS: _LAYER_PATHS.
  _EMBED_PATHS: _EMBED_PATHS.
  _NORM_PATHS: _NORM_PATHS.
  _HEAD_PATHS: _HEAD_PATHS.
  _path_of: _path_of().
  set_at: set_at().
  _POS_EMBED_PATHS: _POS_EMBED_PATHS.
  head_out_features: head_out_features().
  accepted_kwargs: accepted_kwargs().
  derive_head_dim: derive_head_dim().
  moe_attr_name: moe_attr_name().
  derive_dim: derive_dim().
---
# Module: [`torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py)

## Functions
- <a id="_ask_hf"></a>`_ask_hf(root, getter)` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L83) — Ask the HF model itself where a part lives.
- <a id="_path_of"></a>`_path_of(root, target)` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L73) — The dotted path of an existing submodule, by identity.
- <a id="_resolve"></a>`_resolve(root, paths)` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L65)
- <a id="_walk"></a>`_walk(root, path)` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L56)
- <a id="accepted_kwargs"></a>`accepted_kwargs(fn)` — [`L272`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L272) — The keyword names a forward accepts, or None if it takes **kwargs.
- <a id="derive_dim"></a>`derive_dim(config, field, default=1)` — [`L314`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L314) — Read a structural size the top-level config does not state.
- <a id="derive_head_dim"></a>`derive_head_dim(config)` — [`L333`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L333) — head_dim for an architecture that does not state it at the top level.
- <a id="find_backbone"></a>`find_backbone(root)` — [`L177`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L177) — The module that owns the block stack (model / transformer / decoder).
- <a id="find_embedding"></a>`find_embedding(root)` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L128)
- <a id="find_head"></a>`find_head(root)` — [`L154`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L154) — The output projection, or (None, None) for a model that has none.
- <a id="find_layers"></a>`find_layers(root)` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L103) — The decoder/encoder block stack.
- <a id="find_norm"></a>`find_norm(root)` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L144) — The final norm, or (None, None) for a model that has none.
- <a id="find_position_embedding"></a>`find_position_embedding(root)` — [`L211`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L211) — The learned absolute position table, or (None, None) under RoPE.
- <a id="find_rotary"></a>`find_rotary(root)` — [`L188`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L188) — Rotary embedding module, or (None, None) for learned-position models.
- <a id="head_out_features"></a>`head_out_features(head)` — [`L253`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L253) — How many classes the head projects to, or None if it cannot be read.
- <a id="moe_attr_name"></a>`moe_attr_name(layer)` — [`L294`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L294) — The attribute holding this layer's MoE block, or None if it has none.
- <a id="position_capacity"></a>`position_capacity(root)` — [`L233`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L233) — Longest sequence the model can position, or None if unbounded (RoPE).
- <a id="set_at"></a>`set_at(root, path, value)` — [`L167`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L167) — Assign back through a path returned by one of the finders.

## Module values
- <a id="_EMBED_PATHS"></a>`_EMBED_PATHS` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L29)
- <a id="_HEAD_PATHS"></a>`_HEAD_PATHS` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L47)
- <a id="_LAYER_PATHS"></a>`_LAYER_PATHS` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L20)
- <a id="_NORM_PATHS"></a>`_NORM_PATHS` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L37)
- <a id="_POS_EMBED_PATHS"></a>`_POS_EMBED_PATHS` — [`L199`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py#L199)

