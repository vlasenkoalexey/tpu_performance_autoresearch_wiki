---
title: 'Module: src/vllm_torchtpu/megakernel/pool_alias.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool_alias.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool_alias`/
symbols:
  _install: _install().
  view: view().
  _lower: _lower().
  storage_size: storage_size().
  _original: _original.
  _installed: _installed.
  Reinterpret: Reinterpret#
---
# Module: [`src/vllm_torchtpu/megakernel/pool_alias.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool_alias.py)

## Classes
### <a id="Reinterpret"></a>`Reinterpret`  ·  implements/extends ReshapeTransform
- def: [`src/vllm_torchtpu/megakernel/pool_alias.py:41`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool_alias.py#L41)
- doc: Ref transform marking a raw `(8, 128)`-tiled VMEM shape reinterpretation.
- signature: `class Reinterpret(types.ReshapeTransform):`
- used by: [`view`](pool_alias.md#view), [`_lower`](pool_alias.md#_lower)

## Functions
- <a id="_install"></a>`_install()` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool_alias.py#L83)
- <a id="_lower"></a>`_lower(ref, transform, aval, block_shape)` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool_alias.py#L49)
- <a id="storage_size"></a>`storage_size(shape, dtype)` — [`L95`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool_alias.py#L95) — Bytes occupied by `(8, 128)`-tiled layout (rounding up the two minor dims).
- <a id="view"></a>`view(ref, shape, dtype)` — [`L105`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool_alias.py#L105) — Return a `shape`/`dtype` view aliasing `ref`'s physical tiled storage.

## Module values
- <a id="_installed"></a>`_installed` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool_alias.py#L46)
- <a id="_original"></a>`_original` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool_alias.py#L45)

