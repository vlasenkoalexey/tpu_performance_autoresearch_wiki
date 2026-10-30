---
title: Model support overview (parallelism matrix and per-model limits)
type: doc-concept
provenance: doc
source: torchtitan/models/llama3/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Model support overview (parallelism matrix and per-model limits)

## Definition
The per-model READMEs under `torchtitan/models/` state which parallelisms, activation
checkpointing, compile, and precision features each model family supports, plus known gaps. This
page consolidates the short READMEs (Llama 3, Qwen3, DeepSeek-V3, DeepSeek-V4, gpt-oss, Kimi K3,
Qwen3.6, Qwen3.8) and summarizes the families that have their own page (Kimi K2.7, Qwen3.5, Flux,
Muse Glimmer). Where a README and the code at this commit disagree, the code wins and the gap is
noted.

## In torchtitan (grounded)
Model classes and their `parallelize_fn`:
[`Llama3Model`](../catalog/torchtitan/models/llama3/model.md#Llama3Model "torchtitan/models/llama3/model.py:L59") /
[`parallelize_llama`](../catalog/torchtitan/models/llama3/parallelize.md#parallelize_llama "torchtitan/models/llama3/parallelize.py:L23");
[`Qwen3Model`](../catalog/torchtitan/models/qwen3/model.md#Qwen3Model "torchtitan/models/qwen3/model.py:L75") /
[`parallelize_qwen3`](../catalog/torchtitan/models/qwen3/parallelize.md#parallelize_qwen3 "torchtitan/models/qwen3/parallelize.py:L28");
[`DeepSeekV3Model`](../catalog/torchtitan/models/deepseek_v3/model.md#DeepSeekV3Model "torchtitan/models/deepseek_v3/model.py:L237") /
[`parallelize_deepseekv3`](../catalog/torchtitan/models/deepseek_v3/parallelize.md#parallelize_deepseekv3 "torchtitan/models/deepseek_v3/parallelize.py:L21");
[`DeepSeekV4Model`](../catalog/torchtitan/models/deepseek_v4/model.md#DeepSeekV4Model "torchtitan/models/deepseek_v4/model.py:L101");
[`GptOssModel`](../catalog/torchtitan/models/gpt_oss/model.md#GptOssModel "torchtitan/models/gpt_oss/model.py:L195") /
[`parallelize_gptoss`](../catalog/torchtitan/models/gpt_oss/parallelize.md#parallelize_gptoss "torchtitan/models/gpt_oss/parallelize.py:L58");
[`KimiK3Model`](../catalog/torchtitan/models/kimi_k3/model.md#KimiK3Model) /
[`parallelize_kimi_k3`](../catalog/torchtitan/models/kimi_k3/parallelize.md#parallelize_kimi_k3 "torchtitan/models/kimi_k3/parallelize.py:L27");
[`KimiK25Model`](../catalog/torchtitan/models/kimi_k2_7/model.md#KimiK25Model "torchtitan/models/kimi_k2_7/model.py:L45") /
[`parallelize_kimi_k2_5`](../catalog/torchtitan/models/kimi_k2_7/parallelize.md#parallelize_kimi_k2_5 "torchtitan/models/kimi_k2_7/parallelize.py:L36");
[`Qwen35Model`](../catalog/torchtitan/models/qwen3_5/model.md#Qwen35Model "torchtitan/models/qwen3_5/model.py:L248") /
[`parallelize_qwen3_5`](../catalog/torchtitan/models/qwen3_5/parallelize.md#parallelize_qwen3_5 "torchtitan/models/qwen3_5/parallelize.py:L34");
[`MuseGlimmerModel`](../catalog/torchtitan/models/muse_glimmer/model.md#MuseGlimmerModel "torchtitan/models/muse_glimmer/model.py:L262") /
[`parallelize_muse_glimmer`](../catalog/torchtitan/models/muse_glimmer/parallelize.md#parallelize_muse_glimmer "torchtitan/models/muse_glimmer/parallelize.py:L30");
[`FluxModel`](../catalog/torchtitan/models/flux/model/model.md#FluxModel "torchtitan/models/flux/model/model.py:L30") /
[`parallelize_flux`](../catalog/torchtitan/models/flux/parallelize.md#parallelize_flux "torchtitan/models/flux/parallelize.py:L52").

TPU-lane counterparts exist under `torchtitan/experiments/tpu/` for llama3, qwen3, qwen3_5,
deepseek_v3, flux, and muse_glimmer (e.g. [`TPU parallelize_llama`](../catalog/torchtitan/experiments/tpu/llama3/infra/parallelize.md#parallelize_llama),
[`TPU parallelize_qwen3`](../catalog/torchtitan/experiments/tpu/qwen3/infra/parallelize.md#parallelize_qwen3 "torchtitan/experiments/tpu/qwen3/infra/parallelize.py:L23"),
[`TPU parallelize_muse_glimmer`](../catalog/torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.md#parallelize_muse_glimmer),
[`TPU parallelize_flux`](../catalog/torchtitan/experiments/tpu/flux/infra/parallelize.md#parallelize_flux));
the upstream support below describes the shared GPU/default path, not the TPU recipes.

## Why it matters / when it applies

Upstream (non-TPU) support as documented, checked against code guards:

| Family | FSDP/HSDP | TP (+SP) | CP | PP | EP | Other |
|---|---|---|---|---|---|---|
| Llama 3 (8B/70B/405B, debug) | yes | yes; async TP on H100 | yes (with FSDP/HSDP/DDP/TP) | 1F1B, Interleaved1F1B, GPipe | n/a | DDP; selective + full AC; compile; Float8, MXFP8, NVFP4 recipes |
| Qwen3 dense / MoE | yes | yes | yes | not listed | MoE only | DDP; AC; compile; MoE token-choice with aux load-balance loss |
| Qwen3.5 / 3.6 / 3.8 | yes | yes, head-sharded on GatedDeltaNet | **no** (code raises) | 1F1B, Interleaved1F1B | MoE only | own page |
| DeepSeek-V3 | yes | yes | yes | yes, but not with MTP | yes | fused Triton overrides; MTP |
| DeepSeek-V4 | yes | yes | not stated | not stated | yes | smoke-tested FSDP2+TP2+EP2 incl. `spmd_types` |
| gpt-oss | yes | yes | yes | yes (Interleaved1F1B in CI) | yes | grouped GEMM experts |
| Kimi K2.7 | yes | model yes, DistMuon recipes reject | **no** (code raises) | 1F1B, Interleaved1F1B | yes | own page |
| Kimi K3 | FSDP2/HSDP only | **no** | **no** | **no** | not stated | code also rejects model compile |
| Muse Glimmer | yes | yes | yes | yes | n/a | own page |
| Flux | yes | TODO | yes | TODO | n/a | own page |

Cross-cutting limits and notes:
- **Zero-bubble / split-backward PP** schedules are disabled in the integration tests for Llama 3
  and gpt-oss because the FlexInnerAttention `BlockMask` is not a Tensor (`stage_backward_input`
  calls `requires_grad` on every stage input). Full-backward schedules (1F1B, GPipe,
  Interleaved1F1B) are unaffected.
- **DeepSeek-V3 performance option:** fused Triton kernels for MLA Q/KV assembly, ComplexRoPE, and
  SwiGLU via overrides ([`fused_mla`](../catalog/torchtitan/overrides/fused_mla.md#fused_mla "torchtitan/overrides/fused_mla.py:L899"),
  [`fused_swiglu`](../catalog/torchtitan/overrides/fused_swiglu.md#fused_swiglu "torchtitan/overrides/fused_swiglu.py:L585")), checkpoint-layout
  preserving (`--override.imports torchtitan.overrides.fused_mla.fused_mla,torchtitan.overrides.fused_swiglu.fused_swiglu`).
  These are CUDA/Triton kernels; the TPU lane uses its own overrides and Pallas kernels instead.
- **DeepSeek-V3 16B** reuses the deepseek-moe-16b tokenizer, but its weights cannot load (different
  architecture). HF -> DCP conversion is offline/CPU only.
- **DeepSeek-V4** components: sliding-window, heavily-compressed, and compressed-sparse attention
  ([`SlidingWindowAttention`](../catalog/torchtitan/models/deepseek_v4/attention.md#SlidingWindowAttention),
  [`HeavilyCompressedAttention`](../catalog/torchtitan/models/deepseek_v4/attention.md#HeavilyCompressedAttention),
  [`CompressedSparseAttention`](../catalog/torchtitan/models/deepseek_v4/attention.md#CompressedSparseAttention)),
  KV compression/sparse indexing ([`Compressor`](../catalog/torchtitan/models/deepseek_v4/compressor.md#Compressor "torchtitan/models/deepseek_v4/compressor.py:L31"),
  [`Indexer`](../catalog/torchtitan/models/deepseek_v4/compressor.md#Indexer)), hyper-connection
  branch mixing ([`HcPre`](../catalog/torchtitan/models/deepseek_v4/mhc.md#HcPre),
  [`HcPost`](../catalog/torchtitan/models/deepseek_v4/mhc.md#HcPost)), and optional MTP
  (`deepseek_v4_mtp_debugmodel`). Larger configs need checkpoint and convergence validation.
- **Kimi K3:** 2.8T total / 104B active, 69 KDA + 24 gated MLA layers, LatentMoE top-16 of 896
  experts, MoonViT-V2; debug-model parity KL 6.76e-7. Only `kimi_k3_debugmodel` is registered.
- **Qwen3 recipes:** the README says 4B/8B/235B have no pretrain recipes; at this commit an 8B
  NVFP4 pretrain recipe ([`qwen3_8b_first_85_pct_layers_nvfp4`](../catalog/torchtitan/models/qwen3/config_registry.md#qwen3_8b_first_85_pct_layers_nvfp4 "torchtitan/models/qwen3/config_registry.py:L262"))
  does exist, plus `sft_qwen3_8b_math`.
- **Qwen3.6 / Qwen3.8** are version-specific registries ([`qwen3_6 model_registry`](../catalog/torchtitan/models/qwen3_6/__init__.md#model_registry),
  [`qwen3_8 model_registry`](../catalog/torchtitan/models/qwen3_8/__init__.md#model_registry)) over
  the Qwen3.5 implementation; see [qwen3-5-hybrid-attention-family](qwen3-5-hybrid-attention-family.md).
- **Llama 3** is the reference model for validating distributed techniques; the README defers to
  integration tests and `docs/converging.md` (not present in this checkout) instead of any single
  MFU/KL number. The tests it cites now live as recipes in `torchtitan_recipes/tests/` driven by
  `tests/integration_tests/features.py`.

## Connections
- Code concepts: [llama3-model](../concepts/llama3-model.md), [qwen3-model](../concepts/qwen3-model.md),
  [qwen3-5-model](../concepts/qwen3-5-model.md), [deepseek-v3-model](../concepts/deepseek-v3-model.md),
  [deepseek-v4-model](../concepts/deepseek-v4-model.md), [gpt-oss-model](../concepts/gpt-oss-model.md),
  [kimi-k2-7-model](../concepts/kimi-k2-7-model.md), [kimi-k3-model](../concepts/kimi-k3-model.md),
  [muse-glimmer-model](../concepts/muse-glimmer-model.md), [flux-diffusion-model](../concepts/flux-diffusion-model.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md).
- Module catalogs: [torchtitan/models/llama3/parallelize](../catalog/torchtitan/models/llama3/parallelize.md),
  [torchtitan/models/gpt_oss/parallelize](../catalog/torchtitan/models/gpt_oss/parallelize.md),
  [torchtitan/models/kimi_k3/parallelize](../catalog/torchtitan/models/kimi_k3/parallelize.md),
  [torchtitan/models/deepseek_v4/attention](../catalog/torchtitan/models/deepseek_v4/attention.md).
- Related doc-concepts: [tpu-recipe-matrix](tpu-recipe-matrix.md), [model-folder-contract](model-folder-contract.md),
  [kimi-k2-7-model-notes](kimi-k2-7-model-notes.md),
  [qwen3-5-hybrid-attention-family](qwen3-5-hybrid-attention-family.md),
  [flux-training-notes](flux-training-notes.md),
  [muse-glimmer-architecture](muse-glimmer-architecture.md),
  [deepseek-v3-multi-token-prediction](deepseek-v3-multi-token-prediction.md),
  [float8-training](float8-training.md), [nvfp4-training](nvfp4-training.md).

## Source
Extracted from the model READMEs (kept in place): `torchtitan/models/llama3/README.md`,
`torchtitan/models/qwen3/README.md`, `torchtitan/models/deepseek_v3/README.md`,
`torchtitan/models/deepseek_v4/README.md`, `torchtitan/models/gpt_oss/README.md`,
`torchtitan/models/kimi_k3/README.md`, `torchtitan/models/qwen3_6/README.md`,
`torchtitan/models/qwen3_8/README.md` (summary rows also draw on the kimi_k2_7, qwen3_5,
muse_glimmer, and flux READMEs).
