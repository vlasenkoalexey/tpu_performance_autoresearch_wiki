---
title: 'Module: src/vllm_torchtpu/patch_registry.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/patch_registry.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.patch_registry`/
symbols:
  Patch: Patch#
  apply: apply().
  _ACTIVE._ACTIVE: _ACTIVE._ACTIVE.
  _ENGINE._ENGINE: _ENGINE._ENGINE.
  PATCHES: PATCHES.
  _reset_after_fork: _reset_after_fork().
  Patch.target: Patch#target.
  _active_stages._active_stages: _active_stages._active_stages.
  Stage: Stage.
  Patch.refresh: Patch#refresh.
  Patch.model_config: Patch#model_config.
  _applying._applying: _applying._applying.
  Patch.stages: Patch#stages.
  _lock: _lock.
  _invoke: _invoke().
  _applied._applied: _applied._applied.
  _logger: _logger.
---
# Module: [`src/vllm_torchtpu/patch_registry.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py)

## Classes
### <a id="Patch"></a>`Patch`
- def: [`src/vllm_torchtpu/patch_registry.py:40`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L40)
- doc: Declares a patch's lifecycle and optional binding refresh.
- signature: `class Patch:`
- members:
  - <a id="Patch.model_config"></a>`model_config` — [`L45`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L45)
  - <a id="Patch.refresh"></a>`refresh` — [`L46`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L46)
  - <a id="Patch.stages"></a>`stages` — [`L44`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L44)
  - <a id="Patch.target"></a>`target` — [`L43`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L43)
- uses (calls/refs, reference-scoped): [`Stage`](patch_registry.md#Stage)
- used by: [`apply`](patch_registry.md#apply), [`PATCHES`](patch_registry.md#PATCHES)

## Functions
- <a id="_invoke"></a>`_invoke(target: str, **kwargs)` — [`L194`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L194)
- <a id="_reset_after_fork"></a>`_reset_after_fork()` — [`L182`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L182) — Retains installed patches and resets process-local execution state.
- <a id="apply"></a>`apply(stage: Stage, *, model_config: ModelConfig | None = None)` — [`L202`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L202) — Applies a stage once per patch and refreshes late module bindings.

## Module values
- <a id="PATCHES"></a>`PATCHES` — [`L61`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L61)
- <a id="Stage"></a>`Stage` — [`L34`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L34)
- <a id="_ACTIVE._ACTIVE"></a>`_ACTIVE` — [`L52`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L52)
- <a id="_ENGINE._ENGINE"></a>`_ENGINE` — [`L58`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L58)
- <a id="_active_stages._active_stages"></a>`_active_stages` — [`L177`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L177)
- <a id="_applied._applied"></a>`_applied` — [`L175`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L175)
- <a id="_applying._applying"></a>`_applying` — [`L176`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L176)
- <a id="_lock"></a>`_lock` — [`L178`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L178)
- <a id="_logger"></a>`_logger` — [`L179`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/patch_registry.py#L179)

