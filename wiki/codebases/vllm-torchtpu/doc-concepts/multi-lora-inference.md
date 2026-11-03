---
title: Multi-LoRA inference on TPU (slot-stacked adapters inside the compiled graph)
type: doc-concept
provenance: doc
source: docs/api_and_code_examples/offline_lora_inference.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Multi-LoRA inference on TPU (slot-stacked adapters inside the compiled graph)

## Definition
The LoRA example (`examples/offline_lora_inference.py`, also quickstart section 4) runs offline
generation with `--enable-lora --max-lora-rank 8` on `Qwen/Qwen2.5-3B-Instruct`, attaching one
adapter per request through a `LoRARequest(name, id, path)`. Defaults are deliberately tiny
(`max_model_len=256`, `max_num_seqs=8`, 16 output tokens). The doc only shows usage; the TPU
mechanism behind it is a fixed number of adapter **slots** (`max_loras`) stacked into every LoRA
layer, all computed inside the one compiled backbone, so mixing adapters in a batch never
changes graph shapes.

## In vllm-torchtpu (grounded)
- **Manager.** [`TPUModelRunner.load_lora_model`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.load_lora_model)
  installs [`TPUWorkerLoRAManager`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPUWorkerLoRAManager)
  in place of vLLM's LRU worker manager. It widens vLLM's LoRA index buffers to the runner's
  largest compile size (a user `compile_sizes` entry can exceed `max_num_batched_tokens`, which
  otherwise fails at startup), and
  [`_load_adapter`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPUWorkerLoRAManager._load_adapter)
  rejects adapters with NaN/Inf weights: because every slot is computed for every token, a NaN in
  one adapter's LoRA B would poison every request in every batch while it sits in a slot.
- **One-program slot write.** [`TPULoRAModelManager`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPULoRAModelManager)
  keeps vLLM's slot choice but stages the per-layer writes on the host and lands the finished slot
  with a single program ([`write_adapter_to_slot`](../catalog/src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.md#write_adapter_to_slot)).
  Upstream writes cost "one small program per write and slow every later step".
  [`precompile_activation`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPULoRAModelManager.precompile_activation)
  compiles that program at warmup by writing zeros into slot 0, and
  [`slot_write_hbm_bytes`](../catalog/src/vllm_torchtpu/lora/lora_manager.md#TPULoRAModelManager.slot_write_hbm_bytes)
  reports the transient HBM the write needs, which the worker subtracts from the KV budget as
  `lora_slot_write_hbm_gb` (see [profile-cache-and-free-hbm-probe](profile-cache-and-free-hbm-probe.md)).
- **Compute.** [`PunicaWrapperTPU`](../catalog/src/vllm_torchtpu/lora/torch_punica_tpu.md#PunicaWrapperTPU)
  keeps the per-step token -> slot mapping; [`bgmv_shrink`](../catalog/src/vllm_torchtpu/lora/lora_ops.md#bgmv_shrink)
  and [`bgmv_expand`](../catalog/src/vllm_torchtpu/lora/lora_ops.md#bgmv_expand) are pure torch:
  they compute **every** slot and select with a one-hot mask instead of gathering per-token weights.

Owning modules: `lora/lora_manager.py`, `lora/torch_punica_tpu.py`, `lora/lora_ops.py`,
`layers/adapter/custom_ops/lora_slot_update_op.py`.

## Why it matters / when it applies
The cost model is written down in `lora/lora_ops.py`: with T tokens, L = `max_loras`, r =
`max_lora_rank` (lower-rank adapters are zero-padded to r), each LoRA slice adds
2 x T x L x r x (d + out) FLOPs and reads L x r x (d + out) weights, regardless of how many
adapters the batch actually uses. With d = out = 4096 and L = 16, that is +12.5% over the base
layer at r = 16 and +50% at r = 64; merged layers (QKV) pay it per slice. So:
- `--max-loras` and `--max-lora-rank` are direct throughput knobs - size them to the real adapter
  mix, not the maximum you might load.
- Adapter swaps are cheap per step (one program) but occupy transient HBM accounted in the KV
  budget.
- The example's own settings (one adapter, rank 8, 8 sequences, 256-token context) exercise
  correctness, not performance.

## Connections
- Code concepts: [tpu-model-runner](../concepts/tpu-model-runner.md),
  [custom-ops](../concepts/custom-ops.md),
  [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md).
- Module catalogs: [lora/lora_manager](../catalog/src/vllm_torchtpu/lora/lora_manager.md),
  [lora/torch_punica_tpu](../catalog/src/vllm_torchtpu/lora/torch_punica_tpu.md),
  [lora/lora_ops](../catalog/src/vllm_torchtpu/lora/lora_ops.md),
  [layers/adapter/custom_ops/lora_slot_update_op](../catalog/src/vllm_torchtpu/layers/adapter/custom_ops/lora_slot_update_op.md).
- Related doc-concepts: [offline-inference-example](offline-inference-example.md),
  [profile-cache-and-free-hbm-probe](profile-cache-and-free-hbm-probe.md).

## Source
Extracted from `docs/api_and_code_examples/offline_lora_inference.md` (which embeds
`examples/offline_lora_inference.py`) and quickstart section 4 (kept in place).
