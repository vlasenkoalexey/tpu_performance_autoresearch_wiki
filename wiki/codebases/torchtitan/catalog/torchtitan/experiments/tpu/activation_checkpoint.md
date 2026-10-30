---
title: 'Module: torchtitan/experiments/tpu/activation_checkpoint.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/activation_checkpoint.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.activation_checkpoint`/
symbols:
  tpu_selective_ac_config: tpu_selective_ac_config().
  TPUSelectiveAC: TPUSelectiveAC#
  TPUSelectiveAC.Config: TPUSelectiveAC#Config#
  AttentionSavingSelectiveAC.Config: AttentionSavingSelectiveAC#Config#
  TPUSelectiveAC.get_save_ops: TPUSelectiveAC#get_save_ops().
  _SaveOpsIncludingPallasAttention.__contains__: _SaveOpsIncludingPallasAttention#__contains__().
  AttentionSavingSelectiveAC.get_save_ops: AttentionSavingSelectiveAC#get_save_ops().
  AttentionSavingSelectiveAC: AttentionSavingSelectiveAC#
  _PALLAS_ATTENTION_FWD_MARKER: _PALLAS_ATTENTION_FWD_MARKER.
  _SAVED_COLLECTIVES: _SAVED_COLLECTIVES.
  _op_name: _op_name().
  _SaveOpsIncludingPallasAttention: _SaveOpsIncludingPallasAttention#
---
# Module: [`torchtitan/experiments/tpu/activation_checkpoint.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py)

## Classes
### <a id="AttentionSavingSelectiveAC"></a>`AttentionSavingSelectiveAC`  ·  implements/extends SelectiveAC
- def: [`torchtitan/experiments/tpu/activation_checkpoint.py:93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L93) — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- doc: `SelectiveAC` that also saves the attention output on TPU.
- signature: `class AttentionSavingSelectiveAC(SelectiveAC):`
- members:
  - <a id="AttentionSavingSelectiveAC.get_save_ops"></a>`get_save_ops(self)` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L113)
- uses (calls/refs, reference-scoped): [`SelectiveAC`](../../distributed/activation_checkpoint.md#SelectiveAC), [`get_save_ops`](../../distributed/activation_checkpoint.md#SelectiveAC.get_save_ops), [`_SaveOpsIncludingPallasAttention`](activation_checkpoint.md#_SaveOpsIncludingPallasAttention)
- used by: [`_tpu_hf_config`](transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`SelectiveAC`](../../distributed/activation_checkpoint.md#SelectiveAC), [`get_save_ops`](../../distributed/activation_checkpoint.md#SelectiveAC.get_save_ops)

### <a id="AttentionSavingSelectiveAC.Config"></a>`AttentionSavingSelectiveAC.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/activation_checkpoint.py:110`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L110)
- signature: `class Config(SelectiveAC.Config):`
- uses (calls/refs, reference-scoped): [`SelectiveAC`](../../distributed/activation_checkpoint.md#SelectiveAC), [`Config`](../../distributed/activation_checkpoint.md#SelectiveAC.Config)
- used by: [`_tpu_hf_config`](transformers_modeling_backend/config_registry.md#_tpu_hf_config)

### <a id="TPUSelectiveAC"></a>`TPUSelectiveAC`  ·  implements/extends SelectiveAC
- def: [`torchtitan/experiments/tpu/activation_checkpoint.py:30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L30) — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- doc: `SelectiveAC` that recomputes collectives instead of saving them.
- signature: `class TPUSelectiveAC(SelectiveAC):`
- members:
  - <a id="TPUSelectiveAC.get_save_ops"></a>`get_save_ops(self)` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L58)
- uses (calls/refs, reference-scoped): [`SelectiveAC`](../../distributed/activation_checkpoint.md#SelectiveAC), [`get_save_ops`](../../distributed/activation_checkpoint.md#SelectiveAC.get_save_ops), [`_SAVED_COLLECTIVES`](activation_checkpoint.md#_SAVED_COLLECTIVES)
- used by: [`SelectiveAC`](../../distributed/activation_checkpoint.md#SelectiveAC), [`tpu_selective_ac_config`](activation_checkpoint.md#tpu_selective_ac_config), [`get_save_ops`](../../distributed/activation_checkpoint.md#SelectiveAC.get_save_ops)  (3 test-only)

### <a id="TPUSelectiveAC.Config"></a>`TPUSelectiveAC.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/activation_checkpoint.py:55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L55)
- signature: `class Config(SelectiveAC.Config):`
- uses (calls/refs, reference-scoped): [`SelectiveAC`](../../distributed/activation_checkpoint.md#SelectiveAC), [`Config`](../../distributed/activation_checkpoint.md#SelectiveAC.Config)
- used by: [`tpu_selective_ac_config`](activation_checkpoint.md#tpu_selective_ac_config)  (2 test-only)

### <a id="_SaveOpsIncludingPallasAttention"></a>`_SaveOpsIncludingPallasAttention`  ·  implements/extends set
- def: [`torchtitan/experiments/tpu/activation_checkpoint.py:77`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L77)
- doc: The default save set, plus any Pallas splash-attention forward op.
- signature: `class _SaveOpsIncludingPallasAttention(set):`
- protocol/private: <a id="_SaveOpsIncludingPallasAttention.__contains__"></a>`__contains__`[`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L87)
- uses (calls/refs, reference-scoped): [`_PALLAS_ATTENTION_FWD_MARKER`](activation_checkpoint.md#_PALLAS_ATTENTION_FWD_MARKER), [`_op_name`](activation_checkpoint.md#_op_name)
- used by: [`get_save_ops`](activation_checkpoint.md#AttentionSavingSelectiveAC.get_save_ops)

## Functions
- <a id="_op_name"></a>`_op_name(op)` — [`L19`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L19) — Qualified name of an OpOverload, however this torch build spells it.
- <a id="tpu_selective_ac_config"></a>`tpu_selective_ac_config(ac_config: Any)` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L62) — Returns a plain ``SelectiveAC.Config`` as a ``TPUSelectiveAC.Config``. — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)

## Module values
- <a id="_PALLAS_ATTENTION_FWD_MARKER"></a>`_PALLAS_ATTENTION_FWD_MARKER` — [`L10`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L10)
- <a id="_SAVED_COLLECTIVES"></a>`_SAVED_COLLECTIVES` — [`L13`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/activation_checkpoint.py#L13)

