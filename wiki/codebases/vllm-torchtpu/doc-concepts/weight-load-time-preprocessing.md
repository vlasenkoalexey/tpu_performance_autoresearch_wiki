---
title: Do heavy tensor work at weight-load time, not in the forward pass
type: doc-concept
provenance: doc
source: docs/developers_guide/optimization_best_practices.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Do heavy tensor work at weight-load time, not in the forward pass

## Definition
Rule P-14 of the optimization guide: dequantization, scale broadcasting, KV-head
replication and weight transposes are done **once at weight-loading time**, normalized to
the kernel's contract, so no per-backend branching or per-call reshaping survives into
the forward pass. Call-time `jnp.pad` on the inference path needs trace proof or a
redesign, because the runner already pads shapes upstream and kernels should not carry
unaligned-shape complexity. Layout fixes (interleaved splits) are likewise done by
preprocessing weights at load (P-12).

## In vllm-torchtpu (grounded)
- The hook is vLLM's `process_weights_after_loading` on each quant / linear method, e.g.
  [`VllmFp8LinearMethodTPU.process_weights_after_loading`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8LinearMethodTPU.process_weights_after_loading)
  and [`VllmFp8MoEMethodTPU.process_weights_after_loading`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8MoEMethodTPU.process_weights_after_loading),
  and the MoE methods for other formats
  ([`VllmMxfp4MoEMethod.process_weights_after_loading`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.md#VllmMxfp4MoEMethod.process_weights_after_loading),
  [`VllmNvfp4MoEMethod.process_weights_after_loading`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.md#VllmNvfp4MoEMethod.process_weights_after_loading),
  [`VllmCompressedTensorsW4A16MoEMethod.process_weights_after_loading`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.md#VllmCompressedTensorsW4A16MoEMethod.process_weights_after_loading)).
- Weight transposes for the linear kernels are tracked explicitly in
  `layers/adapter/linear_common.py`:
  [`WEIGHT_FLIPPED_ATTR`](../catalog/src/vllm_torchtpu/layers/adapter/linear_common.md#WEIGHT_FLIPPED_ATTR)
  is an idempotence guard (vLLM's reload paths re-enter `process_weights_after_loading`,
  and a second flip would silently transpose back - square `o_proj` weights make it
  undetectable from shape), and
  [`KEEP_VLLM_LAYOUT_ATTR`](../catalog/src/vllm_torchtpu/layers/adapter/linear_common.md#KEEP_VLLM_LAYOUT_ATTR)
  opts a layer out when other code reads the raw weight.
- Loader-side patches registered through the [patch registry](tpu-patch-registry.md)
  shape load-time memory behavior, e.g.
  [`patch_moe_expert_write_staging`](../catalog/src/vllm_torchtpu/model_loader_patches.md#patch_moe_expert_write_staging)
  and [`patch_default_model_loader_page_cache`](../catalog/src/vllm_torchtpu/model_loader_patches.md#patch_default_model_loader_page_cache).

## Why it matters / when it applies
- Anything left in the forward pass is paid every step on every layer; anything moved to
  load time is paid once. The forward graph also stays free of per-format branches,
  which keeps compiled programs uniform across checkpoints.
- The cost moves to HBM residency and load time instead, so the rule comes paired with
  Q-6: compare server `total_hbm_used_gb` before and after (resident growth shrinks the
  KV cache), validate on the largest checkpoint that fits across TP/EP/DP and on a
  sharded last dim that is not 128-divisible, and report load times
  ([perf-evidence-standard](perf-evidence-standard.md)).
- Q-5: track scale tensors independently of the weights they scale - a weight transpose
  does not imply a scale transpose.

## Connections
- Code concepts: [quantization-methods](../concepts/quantization-methods.md),
  [vllm-layer-adapters](../concepts/vllm-layer-adapters.md),
  [fused-moe-kernels](../concepts/fused-moe-kernels.md),
  [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md)
- Module catalogs: [layers/adapter/linear_common](../catalog/src/vllm_torchtpu/layers/adapter/linear_common.md),
  [quantization/fp8](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md),
  [model_loader_patches](../catalog/src/vllm_torchtpu/model_loader_patches.md)
- Related doc-concepts: [generic-quantization-machinery](generic-quantization-machinery.md),
  [kernel-hardware-resource-rules](kernel-hardware-resource-rules.md),
  [perf-evidence-standard](perf-evidence-standard.md)

## Source
Extracted from `docs/developers_guide/optimization_best_practices.md` (P-12, P-14, Q-5,
Q-6) (kept in place).
