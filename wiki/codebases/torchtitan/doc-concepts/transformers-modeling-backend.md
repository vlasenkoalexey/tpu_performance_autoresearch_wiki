---
title: Hugging Face transformers modeling backend
type: doc-concept
provenance: doc
source: torchtitan/experiments/transformers_modeling_backend/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Hugging Face transformers modeling backend

## Definition
This experiment trains **unmodified Hugging Face `transformers` model definitions** inside TorchTitan with 4D parallelism (FSDP / TP / CP / PP) and `torch.compile`, instead of TorchTitan's own model code. Attention is routed onto TorchTitan's flex attention, and HF MoE blocks are swapped for TorchTitan's grouped-experts MoE so expert parallelism and the `grouped_mm` fast path work. It requires `transformers==5.9.0` and `--parallelism.spmd_backend spmd_types`.

## In torchtitan (grounded)
- Config / registry: [`TransformersBackendConfig`](../catalog/torchtitan/experiments/transformers_modeling_backend/config_registry.md#TransformersBackendConfig) adds `hf_model` (HF model ID) to `Trainer.Config`; recipes such as [`transformers_modeling_backend_debugmodel`](../catalog/torchtitan/experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../catalog/torchtitan/experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`transformers_modeling_backend_full`](../catalog/torchtitan/experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full); model spec via [`model_registry`](../catalog/torchtitan/experiments/transformers_modeling_backend/__init__.md#model_registry).
- Model: [`HFTransformerModel`](../catalog/torchtitan/experiments/transformers_modeling_backend/model.md#HFTransformerModel), with HF modules converted to TorchTitan modules by [`convert_hf_to_module`](../catalog/torchtitan/experiments/transformers_modeling_backend/module_conversion.md#convert_hf_to_module).
- Attention: [`HFFlexKernel`](../catalog/torchtitan/experiments/transformers_modeling_backend/model.md#HFFlexKernel) runs [`FlexInnerAttention`](../catalog/torchtitan/models/common/attention.md#FlexInnerAttention); `attn_mask_type` picks `causal` or `block_causal` (causal + same-document, for packed/SFT sequences). CP wraps the flex kernel in [`_wrap_flex_kernel_cp`](../catalog/torchtitan/experiments/transformers_modeling_backend/parallelize.md#_wrap_flex_kernel_cp).
- MoE: [`build_and_swap_native_moe`](../catalog/torchtitan/experiments/transformers_modeling_backend/moe_replacement.md#build_and_swap_native_moe) (after [`prepare_native_moe_configs`](../catalog/torchtitan/experiments/transformers_modeling_backend/moe_replacement.md#prepare_native_moe_configs)) replaces HF MoE blocks with TorchTitan [`MoE`](../catalog/torchtitan/models/common/moe.md#MoE) / [`GroupedExperts`](../catalog/torchtitan/models/common/moe.md#GroupedExperts).
- Parallelism: [`parallelize_hf_transformers`](../catalog/torchtitan/experiments/transformers_modeling_backend/parallelize.md#parallelize_hf_transformers) (raises unless `parallel_dims.spmd_backend == "spmd_types"`), TP/SP plans from [`set_hf_sharding_configs`](../catalog/torchtitan/experiments/transformers_modeling_backend/hf_sharding.md#set_hf_sharding_configs), FSDP via [`apply_fsdp`](../catalog/torchtitan/experiments/transformers_modeling_backend/parallelize.md#apply_fsdp), PP via [`pipeline_hf_transformers`](../catalog/torchtitan/experiments/transformers_modeling_backend/pipeline.md#pipeline_hf_transformers). Backend switch: [`ParallelismConfig.spmd_backend`](../catalog/torchtitan/config/configs.md#ParallelismConfig.spmd_backend).

## Why it matters / when it applies
- **Coverage.** Dense models tested with FSDP/CP/TP/PP/compile include Llama-3.2-1B, phi-2, Qwen2.5-7B, Mistral-7B, Seed-Coder-8B, Qwen3-4B, AFM-4.5B, granite-3b, ERNIE-4.5-0.3B, helium-2b, OLMo-7B and Ministral-8B. MoE support, validated at debug scale (2-step loss decreasing), with FSDP composing with every listed axis:

  | Model(s) | attn | TP | EP | CP | notes |
  |---|---|---|---|---|---|
  | Qwen3-30B-A3B | GQA | yes | yes | yes | full matrix up to TP+EP+CP |
  | Mixtral-8x7B, OLMoE-1B-7B | GQA | yes | yes | yes | TP+EP, EP+CP |
  | DeepSeek-V2-Lite, V3, GLM-4.7 | MLA | yes | yes | yes* | *flex+CP verified on DeepSeek-V2-Lite (EP+CP) |
  | GLM-5 | MLA + DSA | no | yes | no | DSA indexer fails under TP; CP not wired |
  | Gemma-4-26B-A4B | GQA | no | yes | no | attention TP not viable (2 global KV heads) |

  PP is not yet wired for the MoE path.
- **Known performance gap:** HF modeling has lower MFU than TorchTitan-native modeling; it buys model breadth, not speed. A second known issue is `FSDP=2` vs `FSDP=2 + PP=2` losses/grad-norms not matching bitwise (they converge), suspected to be `register_buffer` handling when loading a seed checkpoint.
- Further work: PP for MoE, loading HF weights, LoRA, TitanRL support.
- **TPU relevance.** A TPU variant lives at `experiments/tpu/transformers_modeling_backend`, which replaces the flex path with a Pallas splash-attention forward ([`splash_attention_forward`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/attention.md#splash_attention_forward)). This GPU page is the baseline that variant adapts; see [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) and [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md).

**Doc vs code at this commit:**
- The quick-start train command uses `MODEL=transformers_modeling_backend`, but `run_train.sh` reads `MODULE` (default `llama3`). As written it would train llama3.
- The README says the backend requires `--parallelism.spmd_backend spmd_types`, but its quick-start command omits the flag, and neither the debug configs nor the default (`partial_dtensor`) set it. `parallelize_hf_transformers` raises unless the flag is passed.

## Connections
- Code concepts: [model-building-blocks](../concepts/model-building-blocks.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [model-spec-protocols](../concepts/model-spec-protocols.md), [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md), [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md)
- Module catalogs: [transformers_modeling_backend/parallelize](../catalog/torchtitan/experiments/transformers_modeling_backend/parallelize.md), [transformers_modeling_backend/model](../catalog/torchtitan/experiments/transformers_modeling_backend/model.md), [transformers_modeling_backend/moe_replacement](../catalog/torchtitan/experiments/transformers_modeling_backend/moe_replacement.md), [transformers_modeling_backend/config_registry](../catalog/torchtitan/experiments/transformers_modeling_backend/config_registry.md)
- Related doc-concepts: [experiments-contribution-contract](experiments-contribution-contract.md), [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md)

## Source
Extracted from `torchtitan/experiments/transformers_modeling_backend/README.md` (kept in place).
