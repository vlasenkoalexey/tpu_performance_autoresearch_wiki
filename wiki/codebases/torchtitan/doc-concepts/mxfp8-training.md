---
title: MXFP8 training (block-scaled linears, FSDP post-all-gather quantization, activation storage)
type: doc-concept
provenance: doc
source: torchtitan/components/quantization/mxfp8/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# MXFP8 training (block-scaled linears, FSDP post-all-gather quantization, activation storage)

## Definition
MXFP8 is the OCP microscaling format: float8 e4m3 data with one shared e8m0 scale per **block of 32
elements**, versus one scale per tensor or per row in plain Float8. TorchTitan uses it for dense
linears (activations 1x32 blocks, weights **square 32x32 tiles**) and for MoE grouped GEMMs. The
doc is NVIDIA Blackwell-specific (B200/SM100, cuBLAS/CUTLASS kernels), but its FSDP-lifecycle and
activation-storage design are general lessons for any low-precision recipe.

## In torchtitan (grounded)
- Converters: [`MXFP8LinearConverter`](../catalog/torchtitan/components/quantization/mxfp8/converter.md#MXFP8LinearConverter "torchtitan/components/quantization/mxfp8/converter.py:L58")
  ([`fqns`](../catalog/torchtitan/components/quantization/mxfp8/converter.md#MXFP8LinearConverter.Config.fqns),
  [`linears_saving_inputs_for_backward_in_mxfp8`](../catalog/torchtitan/components/quantization/mxfp8/converter.md#MXFP8LinearConverter.Config.linears_saving_inputs_for_backward_in_mxfp8))
  and [`MXFP8GroupedExpertsConverter`](../catalog/torchtitan/components/quantization/mxfp8/converter.md#MXFP8GroupedExpertsConverter "torchtitan/components/quantization/mxfp8/converter.py:L236")
  ([`recipe_name`](../catalog/torchtitan/components/quantization/mxfp8/converter.md#MXFP8GroupedExpertsConverter.Config.recipe_name)
  `"mxfp8_rceil"`, [`pad_multiple`](../catalog/torchtitan/components/quantization/mxfp8/converter.md#MXFP8GroupedExpertsConverter.Config.pad_multiple) 32).
- Module: [`MXFP8Linear`](../catalog/torchtitan/components/quantization/mxfp8/linear.md#MXFP8Linear "torchtitan/components/quantization/mxfp8/linear.py:L303")
  with [`InputActivationFormatForBackward`](../catalog/torchtitan/components/quantization/mxfp8/linear.md#InputActivationFormatForBackward)
  (`bf16` default vs `mxfp8`).
- FSDP lifecycle: a sharded-parameter tensor subclass
  [`_ShardedFSDPTensor`](../catalog/torchtitan/components/quantization/_fsdp_tensor.md#_ShardedFSDPTensor "torchtitan/components/quantization/_fsdp_tensor.py:L259")
  whose [`fsdp_post_all_gather`](../catalog/torchtitan/components/quantization/_fsdp_tensor.md#_ShardedFSDPTensor.fsdp_post_all_gather "torchtitan/components/quantization/_fsdp_tensor.py:L398")
  quantizes the unsharded BF16 weight; the MXFP8 specialization is
  [`_LinearShardedTensorWithMXFP8Compute`](../catalog/torchtitan/components/quantization/mxfp8/tensor.md#_LinearShardedTensorWithMXFP8Compute)
  producing [`_MXFP8LinearOperands`](../catalog/torchtitan/components/quantization/mxfp8/tensor.md#_MXFP8LinearOperands).
- MoE alignment: [`swap_token_dispatcher`](../catalog/torchtitan/components/quantization/utils.md#swap_token_dispatcher "torchtitan/components/quantization/utils.py:L33")
  swaps in a padded dispatcher ([`TorchAOTokenDispatcher`](../catalog/torchtitan/models/common/token_dispatcher.md#TorchAOTokenDispatcher)
  or [`DeepEPTokenDispatcher`](../catalog/torchtitan/models/common/token_dispatcher.md#DeepEPTokenDispatcher)).
- Recipes: [`llama3_8b_mxfp8`](../catalog/torchtitan/models/llama3/config_registry.md#llama3_8b_mxfp8 "torchtitan/models/llama3/config_registry.py:L316"),
  [`deepseek_v3_debugmodel_mxfp8`](../catalog/torchtitan/models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel_mxfp8 "torchtitan/models/deepseek_v3/config_registry.py:L118"),
  [`flux_schnell_mxfp8`](../catalog/torchtitan/models/flux/config_registry.md#flux_schnell_mxfp8 "torchtitan/models/flux/config_registry.py:L244").

## Why it matters / when it applies
- **Quantize after the all-gather, let FSDP own the buffers.** FSDP all-gathers the BF16 weight; the
  post-all-gather hook builds MXFP8 FPROP and DGRAD operands and the BF16 gather output is released.
  With `reshard_after_forward=False` operands are built once and reused through backward (and across
  PP microbatches); with `True`, backward re-gathers and re-quantizes. Communication therefore stays
  BF16 - no all-gather bandwidth savings. Square 32x32 weight tiles make FPROP and DGRAD share one
  quantized allocation.
- **Saving inputs for WGRAD is model- and remat-dependent.** `bf16` (default) saves the BF16 input
  and quantizes columnwise in backward; `mxfp8` saves columnwise MXFP8 and skips that pass, but only
  saves memory when no other op already retains the same BF16 tensor (flash attention outputs often
  are). Under full activation checkpointing the configured format applies to both the original and
  recomputed forward, so an `mxfp8` linear computes then discards columnwise operands in the
  original forward. Built-in opt-ins: Llama 3 `attention.qkv_linear.wqkv`, `feed_forward.w2`;
  DeepSeek V3 `attention.wkv_b`, `feed_forward.w2`, `shared_experts.w2`; Flux none.
- **MoE constraints:** token group sizes must be multiples of 32, EP must be enabled, and the padded
  dispatcher is installed automatically.
- **Requirements/limits:** SM100, PyTorch nightly, TorchAO >= 0.18 with CUTLASS DSL; prototype, no
  BC guarantees; dense local weight dims divisible by 32; composable with compile, FSDP2/TP/EP/PP,
  full AC. Reported: up to +20% (dense, 8xB200) and +20.3% (Llama4 Scout MoE, 512 GB200) over BF16.
- **TPU relevance:** there is no TPU MXFP8 path in this repo; on TPU the analogous mechanism is the
  float8 path via [`TpuFloat8LinearConverter`](../catalog/torchtitan/experiments/tpu/float8_converter.md#TpuFloat8LinearConverter)
  (see [float8-training](float8-training.md)). The FSDP post-all-gather pattern is the reference
  design if block-scaled formats are added for TPU.
- **Doc vs code.** Usage snippets pass `quantization=[...]` to `model_registry`; the real keyword
  is `converters=`.

## Connections
- Code concepts: [quantization](../concepts/quantization.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md),
  [flux-diffusion-model](../concepts/flux-diffusion-model.md),
  [deepseek-v3-model](../concepts/deepseek-v3-model.md).
- Module catalogs: [torchtitan/components/quantization/mxfp8/converter](../catalog/torchtitan/components/quantization/mxfp8/converter.md),
  [torchtitan/components/quantization/mxfp8/linear](../catalog/torchtitan/components/quantization/mxfp8/linear.md),
  [torchtitan/components/quantization/mxfp8/tensor](../catalog/torchtitan/components/quantization/mxfp8/tensor.md),
  [torchtitan/components/quantization/_fsdp_tensor](../catalog/torchtitan/components/quantization/_fsdp_tensor.md).
- Related doc-concepts: [float8-training](float8-training.md), [nvfp4-training](nvfp4-training.md),
  [flux-training-notes](flux-training-notes.md).

## Source
Extracted from `torchtitan/components/quantization/mxfp8/README.md` (kept in place).
