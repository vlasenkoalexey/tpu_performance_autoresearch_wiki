---
title: TPU kernel library map (README kernel list -> code)
type: doc-concept
provenance: doc
source: README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# TPU kernel library map (README kernel list -> code)

## Definition
The README summarizes vllm-torchtpu's performance story in one line: models run as
ordinary vLLM PyTorch code through TorchTPU, while the hot ops are **TPU-tuned Pallas
kernels** - Ragged Paged Attention, dense and sparse MLA, Gated DeltaNet, fused MoE
(including SparseCore offload), and FP8/INT8/MXFP4 quantized matmuls. The supported-models
page attaches those kernels to model families ("Architecture-specific TPU support"). This
page maps each named kernel family to its code and deep concept page, and records which
env vars select among variants.

## In vllm-torchtpu (grounded)
| README kernel family | Entry point(s) | Variant / selection knobs | Deep page |
|---|---|---|---|
| Ragged Paged Attention (RPA v3; default backend for MHA/GQA, `--attention-backend CUSTOM` in recipes) | [`ragged_paged_attention`](../catalog/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.md#ragged_paged_attention), [`ragged_paged_attention_hd64`](../catalog/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.md#ragged_paged_attention_hd64); batched variant [`ragged_paged_attention`](../catalog/src/vllm_torchtpu/kernels/experimental/batched_rpa/wrapper.md#ragged_paged_attention) | [`VLLM_TPU_BLOCK_MAJOR_KV`](../catalog/src/vllm_torchtpu/envs.md#VLLM_TPU_BLOCK_MAJOR_KV), [`USE_RPA_PIPELINED_DMA_STAGING`](../catalog/src/vllm_torchtpu/envs.md#USE_RPA_PIPELINED_DMA_STAGING) | [ragged-paged-attention-kernel](../concepts/ragged-paged-attention-kernel.md), [batched-ragged-paged-attention-kernel](../concepts/batched-ragged-paged-attention-kernel.md) |
| Dense MLA | [`mla_ragged_paged_attention`](../catalog/src/vllm_torchtpu/kernels/mla/v2/kernel.md#mla_ragged_paged_attention), short-KV [`masked_dense_ragged_paged_attention`](../catalog/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.md#masked_dense_ragged_paged_attention) | [`TPU_MLA_MASKED_DENSE_ENABLED`](../catalog/src/vllm_torchtpu/envs.md#TPU_MLA_MASKED_DENSE_ENABLED) via [`admit_layer`](../catalog/src/vllm_torchtpu/kernels/mla/dispatch.md#admit_layer) | [mla-attention-kernels](../concepts/mla-attention-kernels.md) |
| Sparse MLA (DeepSeek-V4, GLM) | [`sparse_ragged_paged_attention`](../catalog/src/vllm_torchtpu/kernels/mla/sparse/kernel.md#sparse_ragged_paged_attention) with [`SPARSECORE_CACHE_LAYOUT`](../catalog/src/vllm_torchtpu/kernels/mla/sparse/kernel.md#SPARSECORE_CACHE_LAYOUT) / [`TENSORCORE_CACHE_LAYOUT`](../catalog/src/vllm_torchtpu/kernels/mla/sparse/kernel.md#TENSORCORE_CACHE_LAYOUT) | [`TPU_SPARSE_MLA_NOPE_LAYOUT`](../catalog/src/vllm_torchtpu/envs.md#TPU_SPARSE_MLA_NOPE_LAYOUT), [`TPU_SPARSE_MLA_ROPE_LAYOUT`](../catalog/src/vllm_torchtpu/envs.md#TPU_SPARSE_MLA_ROPE_LAYOUT) | [mla-attention-kernels](../concepts/mla-attention-kernels.md), [deepseek-v4-streamindex-topk-kernel](../concepts/deepseek-v4-streamindex-topk-kernel.md) |
| Gated DeltaNet (Qwen3.5 hybrid; chunked prefill + recurrent decode) | `kernels/gdn/v3/` ([`derive_gdn_head_geometry`](../catalog/src/vllm_torchtpu/kernels/gdn/head_geometry.md#derive_gdn_head_geometry) for head layout) | [`TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL`](../catalog/src/vllm_torchtpu/envs.md#TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL) (GDN state + KV in one pool) | [gated-deltanet-kernels](../concepts/gated-deltanet-kernels.md), [gdn-pcp-fused-kernel](../concepts/gdn-pcp-fused-kernel.md) |
| Fused MoE | fused EP [`fused_ep_moe_v2`](../catalog/src/vllm_torchtpu/kernels/fused_moe/v2/layer.md#fused_ep_moe_v2); GMM block tables [`get_tuned_block_sizes`](../catalog/src/vllm_torchtpu/kernels/megablox/tuned_block_sizes.md#get_tuned_block_sizes); decode [`fused_moe_decode`](../catalog/src/vllm_torchtpu/kernels/experimental/fused_moe_decode/fused_moe_decode_kernel.md#fused_moe_decode) | [`USE_MOE_FUSED_EP_KERNEL`](../catalog/src/vllm_torchtpu/envs.md#USE_MOE_FUSED_EP_KERNEL), [`MOE_FUSED_EP_KERNEL_IMPL`](../catalog/src/vllm_torchtpu/envs.md#MOE_FUSED_EP_KERNEL_IMPL) (`v2` / `adaptive`), [`MOE_FUSED_EP_ENABLE_W4A8`](../catalog/src/vllm_torchtpu/envs.md#MOE_FUSED_EP_ENABLE_W4A8) | [fused-moe-kernels](../concepts/fused-moe-kernels.md), [adaptive-fused-moe-kernel](../concepts/adaptive-fused-moe-kernel.md) |
| SparseCore offload (MoE permute, ragged gather/reduce) | [`ragged_gather`](../catalog/src/vllm_torchtpu/kernels/sparse_core/ragged_gather.md#ragged_gather), [`ragged_gather_reduce_v2`](../catalog/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.md#ragged_gather_reduce_v2) | [`USE_MOE_SPARSE_CORE`](../catalog/src/vllm_torchtpu/envs.md#USE_MOE_SPARSE_CORE), [`ONEHOT_MOE_PERMUTE_THRESHOLD`](../catalog/src/vllm_torchtpu/envs.md#ONEHOT_MOE_PERMUTE_THRESHOLD) | [sparsecore-ragged-gather-scatter](../concepts/sparsecore-ragged-gather-scatter.md) |
| Quantized matmul (FP8 / INT8 / MXFP4 weights) | [`quantized_matmul_kernel`](../catalog/src/vllm_torchtpu/kernels/quantized_matmul/kernel.md#quantized_matmul_kernel), blockwise [`quantized_matmul_kernel`](../catalog/src/vllm_torchtpu/kernels/quantized_matmul/blockwise_kernel.md#quantized_matmul_kernel) | [`ENABLE_QUANTIZED_MATMUL_KERNEL`](../catalog/src/vllm_torchtpu/envs.md#ENABLE_QUANTIZED_MATMUL_KERNEL), `REQUANTIZE_*` | [quantization-methods](../concepts/quantization-methods.md) |

Not in the README's list but present in the tree and relevant to the same hot paths:
Kimi Delta Attention / Kimi-K3 kernels ([kimi-k3-kernels](../concepts/kimi-k3-kernels.md)),
DeepSeek-V4 compress-and-store ([deepseek-v4-compress-and-store-kernel](../concepts/deepseek-v4-compress-and-store-kernel.md)),
the PCP streaming RPA ([pcp-streaming-rpa-kernel](../concepts/pcp-streaming-rpa-kernel.md)),
and the megakernel ([megakernel](../concepts/megakernel.md), [megakernel-pool](../concepts/megakernel-pool.md)),
which the roadmap ties to the co-maintainer effort (see [roadmap-q4-2026](roadmap-q4-2026.md)).

## Why it matters / when it applies
- Almost every kernel variant above is chosen by an env var rather than a CLI flag, and
  those env vars join the compile cache key; see
  [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md).
- Kernels are bridged into the torch graph as custom ops, so their source files are
  hashed into the compile key explicitly (Dynamo cannot see into them); a kernel edit
  invalidates cached executables unless `TPU_KERNEL_ITER_MODE` is used.
- For a perf investigation, the deep concept page per row is where tile tables, VMEM
  budgets and envelope predicates live.

## Connections
- Code concepts: [ragged-paged-attention-kernel](../concepts/ragged-paged-attention-kernel.md), [mla-attention-kernels](../concepts/mla-attention-kernels.md), [gated-deltanet-kernels](../concepts/gated-deltanet-kernels.md), [fused-moe-kernels](../concepts/fused-moe-kernels.md), [sparsecore-ragged-gather-scatter](../concepts/sparsecore-ragged-gather-scatter.md), [quantization-methods](../concepts/quantization-methods.md), [custom-ops](../concepts/custom-ops.md), [attention-and-layer-core](../concepts/attention-and-layer-core.md)
- Module catalogs: [ragged_paged_attention/v3/kernel](../catalog/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.md), [mla/v2/kernel](../catalog/src/vllm_torchtpu/kernels/mla/v2/kernel.md), [mla/sparse/kernel](../catalog/src/vllm_torchtpu/kernels/mla/sparse/kernel.md), [fused_moe/v2/layer](../catalog/src/vllm_torchtpu/kernels/fused_moe/v2/layer.md), [quantized_matmul/kernel](../catalog/src/vllm_torchtpu/kernels/quantized_matmul/kernel.md)
- Related doc-concepts: [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md), [supported-models-and-feature-matrix](supported-models-and-feature-matrix.md), [tuned-block-size-tables](tuned-block-size-tables.md), [dp-ep-moe-layouts](dp-ep-moe-layouts.md), [tpu-quantization-formats](tpu-quantization-formats.md)

## Source
Extracted from `README.md` ("About" kernel list) and `docs/README.md` (kept in place),
with family attachments from `docs/user_guide/supported_models.md`.
