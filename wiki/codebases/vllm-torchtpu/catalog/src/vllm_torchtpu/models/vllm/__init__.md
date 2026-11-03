---
title: 'Module: src/vllm_torchtpu/models/vllm/__init__.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/__init__.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm`/
symbols:
  register_models: register_models().
  _TPUQwen2Config.verify_and_update_config: _TPUQwen2Config#verify_and_update_config().
  _QWEN4_EXP_MODEL: _QWEN4_EXP_MODEL.
  _KIMI_MODEL: _KIMI_MODEL.
  _KIMI_K3_MODEL: _KIMI_K3_MODEL.
  _DSV4_MODEL: _DSV4_MODEL.
  _K3_DSPARK_MODEL: _K3_DSPARK_MODEL.
  _DSV4_DSPARK_MODEL: _DSV4_DSPARK_MODEL.
  _QWEN35_MTP_MODEL: _QWEN35_MTP_MODEL.
  _QWEN35_MOE_MTP_MODEL: _QWEN35_MOE_MTP_MODEL.
  _TPUKimiK3Config: _TPUKimiK3Config#
  _TPUQwen2Config: _TPUQwen2Config#
---
# Module: [`src/vllm_torchtpu/models/vllm/__init__.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py)

## Classes
### <a id="_TPUKimiK3Config"></a>`_TPUKimiK3Config`
- def: [`src/vllm_torchtpu/models/vllm/__init__.py:30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L30)
- doc: Keep K3 MXFP4 checkpoints on TPU's packed-weight loader.
- signature: `class _TPUKimiK3Config(VerifyAndUpdateConfig):`
- used by: [`register_models`](__init__.md#register_models)

### <a id="_TPUQwen2Config"></a>`_TPUQwen2Config`
- def: [`src/vllm_torchtpu/models/vllm/__init__.py:34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L34)
- doc: Pad Qwen2 GQA query heads per KV group when heads % tp_size != 0.
- signature: `class _TPUQwen2Config(VerifyAndUpdateConfig):`
- members:
  - <a id="_TPUQwen2Config.verify_and_update_config"></a>`verify_and_update_config(vllm_config)` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L38)
- uses (calls/refs, reference-scoped): [`update_gqa_head_padding_config`](../../gqa_head_padding.md#update_gqa_head_padding_config)
- used by: [`register_models`](__init__.md#register_models)

## Functions
- <a id="register_models"></a>`register_models()` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L45) — documented in [vllm-model-patches](../../../../../concepts/vllm-model-patches.md)

## Module values
- <a id="_DSV4_DSPARK_MODEL"></a>`_DSV4_DSPARK_MODEL` — [`L22`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L22)
- <a id="_DSV4_MODEL"></a>`_DSV4_MODEL` — [`L20`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L20)
- <a id="_K3_DSPARK_MODEL"></a>`_K3_DSPARK_MODEL` — [`L21`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L21)
- <a id="_KIMI_K3_MODEL"></a>`_KIMI_K3_MODEL` — [`L19`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L19)
- <a id="_KIMI_MODEL"></a>`_KIMI_MODEL` — [`L18`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L18)
- <a id="_QWEN35_MOE_MTP_MODEL"></a>`_QWEN35_MOE_MTP_MODEL` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L26)
- <a id="_QWEN35_MTP_MODEL"></a>`_QWEN35_MTP_MODEL` — [`L25`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L25)
- <a id="_QWEN4_EXP_MODEL"></a>`_QWEN4_EXP_MODEL` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/__init__.py#L27)

