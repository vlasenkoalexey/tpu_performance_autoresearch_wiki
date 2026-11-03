---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.lora_slot_update_op`/
symbols:
  _slot_update_op: _slot_update_op.
  write_adapter_to_slot: write_adapter_to_slot().
  _write_adapter_to_slot: _write_adapter_to_slot().
  _compute_slot_update: _compute_slot_update().
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.py)

## Functions
- <a id="_compute_slot_update"></a>`_compute_slot_update(stacked_weights: list[jax.Array], slot_weights: jax.Array, slot_index: jax.Array)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.py#L34)
- <a id="_write_adapter_to_slot"></a>`_write_adapter_to_slot(stacked_weights: list[torch.Tensor], slot_weights: torch.Tensor, slot_index: torch.Tensor)` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.py#L78)
- <a id="write_adapter_to_slot"></a>`write_adapter_to_slot(stacked_weights: list[torch.Tensor], slot_weights: torch.Tensor, slot_index: torch.Tensor)` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.py#L90) — Writes one slot of every stacked tensor from slot_weights, packed in

## Module values
- <a id="_slot_update_op"></a>`_slot_update_op` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.py#L67)

