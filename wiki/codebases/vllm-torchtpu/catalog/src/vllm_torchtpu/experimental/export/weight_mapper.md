---
title: 'Module: src/vllm_torchtpu/experimental/export/weight_mapper.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/weight_mapper.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.weight_mapper`/
symbols:
  infer_weight_sharding: infer_weight_sharding().
  tied_lm_head_alias: tied_lm_head_alias().
  _resolve_submod_and_param: _resolve_submod_and_param().
  _EMBEDDING_NAMES: _EMBEDDING_NAMES.
---
# Module: [`src/vllm_torchtpu/experimental/export/weight_mapper.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/weight_mapper.py)

## Functions
- <a id="_resolve_submod_and_param"></a>`_resolve_submod_and_param(weight_name: str, model: Any = None)` — [`L23`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/weight_mapper.py#L23) — Resolves `(submod, param_or_buf, mod_path, attr)` from `model`.
- <a id="infer_weight_sharding"></a>`infer_weight_sharding(weight_name: str, shape: Sequence[int | str], model: Any = None, explicit_sharding: Any = None, tp_size_hint: int = 1, has_ep_hint: bool = False)` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/weight_mapper.py#L45) — Determines per-tensor mesh sharding from module/param attributes and name.
- <a id="tied_lm_head_alias"></a>`tied_lm_head_alias(names: Iterable[str])` — [`L236`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/weight_mapper.py#L236) — `(lm_head name, embedding name)` when the LM head is tied to the embedding.

## Module values
- <a id="_EMBEDDING_NAMES"></a>`_EMBEDDING_NAMES` — [`L229`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/weight_mapper.py#L229)

