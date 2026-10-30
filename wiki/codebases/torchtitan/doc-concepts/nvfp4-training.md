---
title: NVFP4 training with a BF16 tail (layer-selective low precision)
type: doc-concept
provenance: doc
source: torchtitan/components/quantization/nvfp4.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# NVFP4 training with a BF16 tail (layer-selective low precision)

## Definition
Experimental NVFP4 training dynamically quantizes linear GEMM activations, weights, and gradients
to NVFP4 through a TorchAO prototype, while model weights and distributed collectives stay BF16.
The recommended recipe is **layer-selective**: convert most decoder layers, keep roughly the final
15% of decoder blocks and the LM head in BF16. NVIDIA Blackwell (SM100+) only; not CI-guarded.

## In torchtitan (grounded)
- [`NVFP4LinearConverter`](../catalog/torchtitan/components/quantization/nvfp4.md#NVFP4LinearConverter "torchtitan/components/quantization/nvfp4.py:L267")
  ([`fqns`](../catalog/torchtitan/components/quantization/nvfp4.md#NVFP4LinearConverter.Config.fqns "torchtitan/components/quantization/nvfp4.py:L272"))
  builds [`NVFP4Linear`](../catalog/torchtitan/components/quantization/nvfp4.md#NVFP4Linear "torchtitan/components/quantization/nvfp4.py:L84") modules.
- [`nvfp4_bf16_tail_fqns`](../catalog/torchtitan/components/quantization/nvfp4.md#nvfp4_bf16_tail_fqns)
  computes the converted-layer FQNs for a given BF16 tail fraction.
- Recipes: [`llama3_8b_first_85_pct_layers_nvfp4`](../catalog/torchtitan/models/llama3/config_registry.md#llama3_8b_first_85_pct_layers_nvfp4 "torchtitan/models/llama3/config_registry.py:L292")
  (layers 0-26 NVFP4, 27-31 BF16; enables `CompileConfig(enable=True, components=["model"])` and
  `spmd_backend="spmd_types"`), [`qwen3_8b_first_85_pct_layers_nvfp4`](../catalog/torchtitan/models/qwen3/config_registry.md#qwen3_8b_first_85_pct_layers_nvfp4 "torchtitan/models/qwen3/config_registry.py:L262")
  (layers 0-29 NVFP4, 30-35 + LM head BF16), plus debug-model variants.
- The override docs show the same policy expressed as an `@override` on `Linear.Config` with
  `fqns=["*.layers.*.attention.*", "*.layers.*.feed_forward.*"]` (see
  [configurable-overrides](configurable-overrides.md)).

## Why it matters / when it applies
- **Shape constraint:** local GEMM dims (after TP sharding) must be multiples of 128; non-conforming
  linears (e.g. the vocab projection) must be excluded, which is why the LM head stays BF16.
- **Compile required** for competitive performance.
- **Precision-switch guidance (from the cited NVFP4 papers):** most of the loss gap comes from
  forward-pass quantization; a forward-only switch to BF16 is the efficient fix but is **not
  supported** by the current integration. The fallback is a full-BF16 finish: checkpoint at the
  switch boundary, restart with the converter/override disabled and BF16 dtype, restoring model,
  optimizer, LR scheduler, dataloader, and step. Switch shortly before LR decay for full recovery,
  later for more NVFP4 utilization, or skip if quality already suffices.
- **Reported evidence (200M tokens, C4, FSDP=4):** Llama 3 8B - NVFP4 30,040 tok/s/GPU vs MXFP8
  28,084 vs BF16 21,919, with ~111 GiB vs ~180/~174 GiB memory and on-par loss. Qwen3 8B - NVFP4
  +28% vs BF16 and 30% less peak memory, 3% slower than MXFP8.
- **Limits:** prototype, SM100+ only, no CI coverage, GEMMs only (TP all-gather/reduce-scatter stay
  BF16); results are limited to the documented configs.
- **TPU relevance:** none directly (no FP4 path on TPU in this repo); the transferable idea is the
  layer-selective "precision-sensitive tail stays high precision" policy, which applies equally to
  the TPU float8 converter's `filter_fqns`.
- **Doc vs code.** The usage command passes `--dataloader.dataset c4` and other legacy CLI flags;
  CLI flags are frozen/deprecated (see [full-configuration-recipes](full-configuration-recipes.md)).

## Connections
- Code concepts: [quantization](../concepts/quantization.md),
  [llama3-model](../concepts/llama3-model.md), [qwen3-model](../concepts/qwen3-model.md),
  [checkpointing](../concepts/checkpointing.md).
- Module catalogs: [torchtitan/components/quantization/nvfp4](../catalog/torchtitan/components/quantization/nvfp4.md),
  [torchtitan/models/llama3/config_registry](../catalog/torchtitan/models/llama3/config_registry.md).
- Related doc-concepts: [float8-training](float8-training.md), [mxfp8-training](mxfp8-training.md),
  [configurable-overrides](configurable-overrides.md).

## Source
Extracted from `torchtitan/components/quantization/nvfp4.md` (kept in place).
