---
title: 'Area: src/vllm_torchtpu/lora'
type: area
area: 'src/vllm_torchtpu/lora'
description: 'Multi-LoRA serving inside the compiled TPU backbone: a Punica wrapper whose shrink/expand ops compute every adapter slot with a one-hot mask, and LoRA managers that write an adapter into its HBM slot with one precompiled program.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/lora`

## Purpose
This area adapts vLLM's multi-LoRA machinery to the TPU rule that every new shape is a new compiled program. vLLM normally gathers each token's adapter weights with data-dependent indexing. Here the batch's adapter mix never changes the shape of the compiled backbone. The [TPU platform](../concepts/tpu-platform.md) names `PunicaWrapperTPU` as vLLM's Punica wrapper (and validates the LoRA config at startup). The [model runner](../concepts/tpu-model-runner.md) builds `TPUWorkerLoRAManager`, precompiles adapter activation during warm-up, and reports how much HBM a slot write needs so the KV budget can reserve it.

The performance trade-off is explicit in `lora_ops.py`. Each token selects one slot of the stacked LoRA weights (or none), and rather than gathering per token, the ops multiply every token by every slot and keep the selected one with a one-hot mask. Every LoRA layer therefore reads all `max_loras` slots and does `2 * T * L * r * (d + out)` extra FLOPs whichever adapters the batch uses. In exchange there are fixed shapes and no recompiles. `max_loras` and `max_lora_rank` are therefore direct cost knobs.

Loading is the other half. An LRU cache of adapters maps onto a fixed number of HBM slots, and activating an adapter writes all of its layers into its slot through one program (a LoRA slot-update custom op) instead of many small per-layer copies.

## How the units connect
- `torch_punica_tpu.py`: `PunicaWrapperTPU` keeps the per-step LoRA mapping as zero-filled int32 index buffers sized for the maximum token count, and implements vLLM's Punica interface with the ops below, so multi-LoRA stays inside the compiled backbone.
- `lora_ops.py`: `one_hot_slots`, `bgmv_shrink` and `bgmv_expand`, pure-torch shrink/expand that compute all slots and select with a one-hot mask.
- `lora_manager.py`: `TPULoRAModelManager` (LRU over slots) writes an adapter into its slot in one program via the slot-update op in [custom-ops](../concepts/custom-ops.md); `TPUWorkerLoRAManager` is the worker-level manager the runner owns, exposing `precompile_activation` and `slot_write_hbm_bytes` (the HBM reserve fed into [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md)).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/lora`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/lora` | 3 | 53 | 3 | [`TPUWorkerLoRAManager`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPUWorkerLoRAManager "src/vllm_torchtpu/lora/lora_manager.py:L301"), [`precompile_activation`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPUWorkerLoRAManager.precompile_activation "src/vllm_torchtpu/lora/lora_manager.py:L356"), [`slot_write_hbm_bytes`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPUWorkerLoRAManager.slot_write_hbm_bytes "src/vllm_torchtpu/lora/lora_manager.py:L361") | section below |

## Small units
### `src/vllm_torchtpu/lora`
- modules: `src/vllm_torchtpu/lora/lora_manager.py`, `src/vllm_torchtpu/lora/lora_ops.py`, `src/vllm_torchtpu/lora/torch_punica_tpu.py`
- entry points: [`TPUWorkerLoRAManager`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPUWorkerLoRAManager "src/vllm_torchtpu/lora/lora_manager.py:L301"), [`precompile_activation`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPUWorkerLoRAManager.precompile_activation "src/vllm_torchtpu/lora/lora_manager.py:L356"), [`slot_write_hbm_bytes`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPUWorkerLoRAManager.slot_write_hbm_bytes "src/vllm_torchtpu/lora/lora_manager.py:L361")
- hubs: [`write_slot`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#_AdapterSlotWriter.write_slot "src/vllm_torchtpu/lora/lora_manager.py:L216"), [`add_expand`](../catalog/src/vllm_torchtpu/lora/torch_punica_tpu.md#PunicaWrapperTPU.add_expand "src/vllm_torchtpu/lora/torch_punica_tpu.py:L122"), [`add_lora_embedding`](../catalog/src/vllm_torchtpu/lora/torch_punica_tpu.md#PunicaWrapperTPU.add_lora_embedding "src/vllm_torchtpu/lora/torch_punica_tpu.py:L169")

<!-- area:auto:end -->
