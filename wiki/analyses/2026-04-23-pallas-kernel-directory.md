---
title: "Directory: Pallas kernels across the JAX ecosystem"
type: analysis
tags: [directory, pallas, kernels, catalog, tpu, gpu, survey]
created: 2026-04-23
updated: 2026-04-23
---

Repo-by-repo catalog of every Pallas kernel surfaced across ~30 public repositories, with source-code references, stability statements, performance claims (verbatim from source when they exist), application use cases, and known callers. This is a directory, not a synthesis — the page answers "where does Pallas kernel X live, is it maintained, and who uses it?" for the widest possible value of X. **Detailed per-kernel rows live in 6 subpages under [pallas-kernel-directory/](pallas-kernel-directory/);** this page is the cross-cutting index that groups by functional category, summarises the vendoring graph, ranks ingest candidates, and reconciles findings against the [2026-04-23 Pallas kernel source survey](2026-04-23-pallas-kernel-source-survey.md).

**Headline numbers:** ~200 Pallas kernels across ~30 repos. `mosaic_tpu` backend dominates (roughly 60%); the rest are Pallas-on-Triton (GPU), Pallas-Mosaic-GPU (SM90/SM100), or Pallas-XLA fallbacks. Every production-grade TPU kernel in the ecosystem is either published upstream in `jax-ml/jax` / `openxla/tokamax` or vendored from them with modifications. Truly **novel** community kernels are concentrated in a handful of repos (vllm-project/tpu-inference, apple/axlearn, AI-Hypercomputer/maxdiffusion, erfanzar/ejkernel, google-deepmind/alphafold3@v3.0.1). The gaps previously flagged in this wiki — **ring-attention public Pallas impl**, **Pallas fused GLU**, **SSM / Mamba Pallas** — are all closed by identified repos; the gap that **remains open** is **Zig-Zag (load-balanced causal) Ring Attention**, confirmed absent from every repo surveyed.

## Methodology

Six subagents in parallel, one per repo group, each following an identical per-kernel row schema: kernel name, source path (clickable GitHub URL), backend (`mosaic_tpu` / `mosaic_gpu_sm90` / `mosaic_gpu_sm100` / `triton` / `xla_fallback`), stability (`stable` / `experimental` / `research` / `pedagogical` / `deprecated` — with a quoted signal), performance claims (quoted verbatim from source; blank if none), use case (one sentence), known callers (both in-repo and external), and notes (vendoring lineage, autotune surface, hardware matrix, paper refs). Agents verified top candidates via GitHub API + WebFetch on raw file contents; unverified or 404 entries are marked explicitly.

Scope: all repositories listed in [2026-04-23 Pallas kernel source survey](2026-04-23-pallas-kernel-source-survey.md) tiers 1–7, excluding purely pedagogical small repos in Tier 7 which are collected in a single row. The `jondeaton/ring-attention-jax-pallas` entry from the previous survey **returned 404 on re-verification** — confirmed dead, dropped.

## Subpage navigation

| § | Subpage | Repos covered | Notable content |
|---|---|---|---|
| 1 | [Upstream JAX + tokamax](pallas-kernel-directory/01-upstream-jax-tokamax.md) | `jax-ml/jax`, `openxla/tokamax` | ~55 kernels. The root of the vendoring graph. TPU + all three GPU backends (Mosaic SM90/SM100 + Triton) |
| 2 | [AI-Hypercomputer stacks](pallas-kernel-directory/02-ai-hypercomputer.md) | MaxText, MaxDiffusion, JetStream | ~17 kernels, all `mosaic_tpu`. **JetStream archives 2026-02-01.** **MaxDiffusion ships the public Pallas ring attention integration.** |
| 3 | [Inference engines](pallas-kernel-directory/03-inference-engines.md) | vllm-project/tpu-inference, sgl-project/sglang-jax, aphrodite-engine | ~33 kernels. **tpu-inference is the authoritative kernel author** for the engine tier. Novel: MLA v1/v2, fused_moe v1, quantized_matmul blockwise, all_gather_matmul, gdn, sparse_core, batched_rpa. Crown-jewel: ~2,000+ tuned block-size entries in sglang-jax |
| 4 | [Research labs — Apple + DeepMind](pallas-kernel-directory/04-research-labs.md) | apple/axlearn, google-deepmind/{recurrentgemma, simply, graphcast, alphafold3 v3.0.1} | ~18 kernels. **Uniquely-novel Mamba/Mamba2/RAttention SSM Pallas (axlearn).** **Canonical LRU scan (recurrentgemma).** **Fused GLU Pallas (alphafold3 @ v3.0.1).** Non-LLM example: graphcast banded-sparse splash for weather models |
| 5 | [Frameworks & quantization libraries](pallas-kernel-directory/05-frameworks-quant.md) | tunix, qwix, aqt, jaxite, paxml/praxis, pytorch/xla, google-pytorch/torchtitan, marin/levanter, pytorch/pytorch | ~18 kernels. Mostly consumers/re-packagers. **jaxite (FHE polymul) is the rare non-ML Pallas.** **marin/levanter autotune harness is the most portable deployment-time tuner** found |
| 6 | [Community & research-companion repos](pallas-kernel-directory/06-community-research.md) | ejkernel, EasyDeL, jax-flash-attn2, ringattention, flashback, gla-jax, sqtian matmul, maxtext-external, tpu-research, recompute_dont_restore + 4 small | ~50 rows. **ejkernel is the broadest community TPU surface** (17 TPU kernels). Several repos mislabel backend as "Pallas" when they're Triton-only |

## Kernel inventory by functional category

One table per category. Each row: one kernel family, columns show which repo offers it and with what backends. **Bold** = **novel** (not derivative of upstream). Use these tables as lookup: pick a category, scan for a TPU kernel in the desired stability tier.

### Attention — dense flash / splash (training)

| Kernel | jax-ml/jax | tokamax | maxtext | maxdiffusion | axlearn | ejkernel | tpu-inference | sglang-jax | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `flash_attention` (TPU, causal+SegmentIds) | `mosaic_tpu` (experimental) | wraps via splash | — | — | wraps upstream (`tpu_attention`) | **`mosaic_tpu`** | `mosaic_tpu` (vendored) | — | Upstream kernel; legacy on TPU |
| `splash_attention` (sparse masks, MQA/GQA) | `mosaic_tpu` (experimental) | `mosaic_tpu` (extended — experimental dir) | `mosaic_tpu` (vendored) | `mosaic_tpu` (vendored, diffusion-tuned) | **`mosaic_tpu` (+ logit sink + in-kernel dropout)** | wraps via ring_attention | — | — | Canonical training kernel for Gemma/Llama/DeepSeek/Qwen/Mistral/Kimi |
| `flash_attention` (GPU, FA2 fwd+bwd) | `triton` | `triton` | — | — | **`triton` (bias, dropout, mask_fn)** | `triton` / `cuda` / `cute` | — | multimodal `mosaic_tpu` | Dao 2022/2023 |
| `flash_attention` (GPU, FA3 on Hopper) | **`mosaic_gpu_sm90`** | `mosaic_gpu_sm90` | — | — | — | — | — | — | WGMMA + TMA warp-specialized |
| `flash_attention` (GPU, Blackwell) | — | **`mosaic_gpu_sm100`** | — | — | — | — | — | — | TCGEN05 / TMEM pipeline |

### Attention — paged KV / ragged / MLA (inference)

| Kernel | jax-ml/jax | tokamax | maxtext | maxdiffusion | jetstream | axlearn | ejkernel | tpu-inference | sglang-jax | pytorch/xla | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `paged_attention` (decode) | `mosaic_tpu` (experimental) | — | wraps upstream (v1) | — | `mosaic_tpu` (vendored, int8 KV) | **`mosaic_tpu` (block-sparse offset mask for sliding window)** | `mosaic_tpu` + `prefill_*` variant | — | `mosaic_tpu` (vendored from JAX) | `mosaic_tpu` (derivative) | Vendoring graph |
| `ragged_paged_attention` v2 (mixed prefill+decode) | `mosaic_tpu` (experimental) | — | `mosaic_tpu` (vendored v2) | — | — | — | **`mosaic_tpu` + `_h64`** | `mosaic_tpu` (vendored) | `mosaic_tpu` (vendored v1) | `mosaic_tpu` (vendored) | 1,200+ tuned entries in tpu-inference |
| `ragged_paged_attention` v3 | `mosaic_tpu` | — | — | — | — | **`mosaic_tpu` + `_v3` and `_h64`** | **`mosaic_tpu` + `_h64`** | `mosaic_tpu` (vendored; custom_mask/sink/xai extensions) | — | — | ~2,000+ tuned entries in sglang-jax |
| `multi_latent_ragged_page_attention` (MLA) | — | — | — | — | — | — | **`mosaic_tpu` v1/v2** | **`mosaic_tpu` v1/v2** | — | — | DeepSeek-V2/V3 architecture |
| `chunked_prefill_attention` | — | — | — | — | **`mosaic_tpu`** | — | — | — | — | — | JetStream prefill counterpart |
| `ragged_decode_attention` (decode-only) | — | — | — | — | — | — | **`mosaic_tpu`** | — | — | — | — |
| `multi_queries_paged_attention` (query_len>1) | — | — | — | — | — | — | — | — | — | **`mosaic_tpu` (derivative)** | — |
| `scatter_update_pages` (KV write) | — | — | — | — | — | `mosaic_tpu` (stopgap; 10× slower than KV projection) | — | — | — | — | `update_kv_cache` (below) is the fast path |
| `update_kv_cache` / `ragged_kv_cache_update` | — | — | — | — | — | — | — | `mosaic_tpu` | `mosaic_tpu` | — | 64 MB VMEM budget |
| `kv_cache_update` | — | — | — | — | — | — | — | — | — | aphrodite | Smallest Pallas file in this catalog |

### Attention — ring / context-parallel

| Kernel | tokamax | maxdiffusion | haoliuhl/ringattention | ejkernel | Notes |
|---|---|---|---|---|---|
| `ring_attention` fwd+bwd | `mosaic_tpu` (experimental; **not reachable via public API**) | **`mosaic_tpu` (integrated with splash as `tokamax_ring`, announced 2026-04-16)** | **`mosaic_tpu`** (canonical paper impl) | `mosaic_tpu` (wraps Splash with ring orchestration — **not novel kernel**) | Zig-Zag / load-balanced variant **absent from every source** |

**This is the most-asked-about kernel family in the wiki.** Three distinct implementations exist:

1. tokamax's experimental copy — kernel present but API gap (documented in [log.md](../log.md) Wave 1).
2. maxdiffusion's integration — reference for how to wire a ring kernel to a splash-style dispatch, with `ring_axis` mesh argument.
3. haoliuhl's standalone paper companion — uses `lax.ppermute` for a unidirectional ring, straight `below_or_on_diag` causal mask. **Not zig-zag.**

### Attention — speculative decoding trees

| Kernel | sglang-jax | Notes |
|---|---|---|
| `tree_speculative_sampling_target_only` | **`mosaic_tpu` (novel)** | EAGLE tree verification |
| `build_eagle_tree_structure` | **`mosaic_tpu` (novel)** | On-device draft tree build |
| `verify_tree_greedy` | **`mosaic_tpu` (novel)** | Greedy tree verify |

Only sglang-jax among ingested repos authors spec-decode tree kernels.

### Attention — block-sparse / domain-specific

| Kernel | axlearn | ejkernel | graphcast | flashback | maxdiffusion | Notes |
|---|---|---|---|---|---|---|
| `blocksparse_attention` | via `tpu_paged_attention` (offset masks) | **`mosaic_tpu`** | **wraps splash with `WeatherMeshMask`** (non-LLM) | — | — | — |
| `flash_softmax` / `flash_sigmoid` with higher-order grads | — | — | — | **`triton` (GPU)** (backward-over-backward) | — | [arXiv:2503.13751](https://arxiv.org/abs/2503.13751) |
| Chunked causal via `_ring_raw` | — | — | — | — | **`mosaic_tpu` (maxdiffusion variant)** | — |

### Attention — gated-delta / linear

| Kernel | tpu-inference | ejkernel | sglang-jax | axlearn | Notes |
|---|---|---|---|---|---|
| `fused_gdn_decode` + `fused_gdn_recurrent` + `triangle_solver` | **`mosaic_tpu`** | — | — | — | Qwen-Next GDN |
| `gated_delta_rule` / `ragged_gated_delta_rule` | — | **`mosaic_tpu` (README: "3.6× speedup" for ragged GDR decode)** | — | — | Same family |
| `simple_gla` fused recurrent + chunked | — | — | `mosaic_tpu` (vendored from private `primatrix/pallas-kernel`) | — | Provenance risk — upstream went private |
| `linear_attention_kernels` (RAttention) | — | — | — | **`mosaic_tpu` (novel)** | Chunked linear attention; feature maps; residual variants |
| `gla_cumsum` / `gla_rnn` | — | — | — | — | zhixuan-lin/gla-jax: **GPU-only (Triton) despite name** |

### MoE / grouped matmul / expert routing

| Kernel | jax-ml/jax | tokamax | maxtext | ejkernel | tpu-inference | sglang-jax | axlearn | Notes |
|---|---|---|---|---|---|---|---|---|
| `megablox.gmm` / `tgmm` | `mosaic_tpu` (experimental) | — | `mosaic_tpu` (+ int4/int8 via qwix) | **`grouped_matmul v1/v2/v3 mosaic_tpu`** | `mosaic_tpu` (vendored) | `mosaic_tpu` (vendored) | — | Root of MoE-grouped-matmul lineage |
| `ragged_dot` (SM90/SM100 incl. FP8/INT8/post-scale quant) | `mosaic_gpu_sm90` + `sm100` | **`mosaic_gpu_sm90/sm100` + 4 quant variants** | — | — | — | — | — | Tokamax holds the GPU MoE frontier |
| `ragged_dot` (TPU) | — | **`mosaic_tpu`** | Megablox in maxtext fallback here | — | — | — | — | — |
| `megablock.gmm_gpu` | — | — | — | — | — | — | **`triton` (novel GPU counterpart of megablox)** | — |
| `fused_moe v1` (routing + two GMMs) | — | — | — | — | **`mosaic_tpu` (v7-tuned, 28 entries)** | `mosaic_tpu` (vendored) | — | Qwen3-MoE, Mixtral, Llama4-MoE |

### MoE support — gather/scatter, sorting/routing

| Kernel | maxtext | tpu-inference | Notes |
|---|---|---|---|
| `sc_gather_reduce` (SparseCore MoE reduce) | **MLIR-dialect Pallas (unusual)** | — | v5p/v7x SparseCore-gated; MoE unroute/reduce fp32→bf16 |
| `sparse_core` ragged gather/scatter/gather_reduce | — | **`mosaic_tpu` (plsc VectorSubcoreMesh)** | Fallback to regular gather when SC absent |
| `route` / `unroute` / `_sort_activations` | dispatches to sc_gather_reduce | — | MoE token sort/dispatch |

### Normalization (LayerNorm / RMSNorm)

| Kernel | jax-ml/jax | tokamax | Notes |
|---|---|---|---|
| `layer_norm` (GPU fwd+bwd) | `triton` | `triton` | No TPU Pallas — falls back to XLA on TPU |
| `rms_norm` (GPU fwd+bwd) | `triton` | `triton` (same module, `subtract_mean=False`) | Same |

**This is one of the two holes in tokamax's TPU surface that Gemma 4 exp 33 empirically showed XLA already fuses well with neighbor matmuls.** No repo in this directory contains a TPU Pallas RMSNorm. Treat as intentional (XLA-fusion-sufficient).

### Activation / fused MLP (GLU / SwiGLU / GEGLU / REGLU)

| Kernel | jax-ml/jax | tokamax | alphafold3 (v3.0.1) | ejkernel | Notes |
|---|---|---|---|---|---|
| Fused GLU `act(x @ Wg) * (x @ Wu)` (GPU) | — | `mosaic_gpu_sm90` + `sm100` + `triton` | **`mosaic_gpu` via triton (Pallas) — production fused** | — | — |
| Fused GLU (TPU) | — | **XLA fallback only** (no Pallas backend) | — | — | **The second hole in tokamax TPU.** AlphaFold3 v3.0.1 is the only public production reference — GPU-side. Pattern (`_gated_linear_unit_kernel`, `matmul_config.py`, `block.py`) is directly portable to Mosaic-TPU |

### Matmul (dense / quantized / mixed-precision)

| Kernel | jax-ml/jax | tokamax | sqtian | qwix | aqt | pytorch/xla | ejkernel | tpu-inference | sglang-jax | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Dense matmul (example/reference) | `mosaic_tpu` (`matmul.py`) | — | **`mosaic_tpu` v1–v5** (pedagogical) | — | — | — | — | — | — | sqtian v4 nearly matches XLA |
| Hopper dense GEMM (WGMMA+TMA) | **`mosaic_gpu_sm90` (hopper_matmul)** | — | — | — | — | — | — | — | — | — |
| Hopper mixed-type (bf16×int8/fp8) | **`mosaic_gpu_sm90`** | — | — | — | — | — | — | — | — | — |
| Blackwell dense GEMM (TCGEN05/TMEM) | **`mosaic_gpu_sm100`** | — | — | — | — | — | — | — | — | — |
| Quantized matmul (blockwise / int8 / fp8) | — | — | — | **`mosaic_tpu` (QArray, `INTERPRET=True`)** | `mosaic_tpu` (pallas_call + dot_general, **deprecated**) | **`mosaic_tpu` INT8 W8A8/W8A16** (novel — on-the-fly activation quant, scratch reuse) | **`mosaic_tpu`** | **`mosaic_tpu` (600+ tuned entries, v6 96MiB VMEM, v7 48MiB)** | `mosaic_tpu` (vendored) | qwix is AQT's successor |
| `quantized_matmul.py` teaching/benchmark | — | — | — | — | — | — | — | — | — | (sqtian v5) |

### Collective / comms

| Kernel | jax-ml/jax | jetstream | ejkernel | tpu-inference | Notes |
|---|---|---|---|---|---|
| `all_gather` (TPU ring, pedagogical) | **`mosaic_tpu` (disclaimed)** | — | — | — | Docs demo |
| `all_gather_mgpu` / `reduce_scatter_mgpu` | **`mosaic_gpu_sm90`** | — | — | — | NVLink intra-node |
| `collective_matmul_mgpu` | **`mosaic_gpu_sm90`** | — | — | — | AG/RS fused with GEMM across H100 |
| AG+matmul / matmul+RS fused (TPU TP) | — | **(via shard_map + ppermute, not Pallas)** | **`mosaic_tpu` (all_gather_matmul, reduce_scatter_matmul)** | **`mosaic_tpu` (all_gather_matmul, microbench'd)** | ejkernel + tpu-inference ship the novel TPU-native variants |

### State-space / linear recurrence / SSM

| Kernel | axlearn | recurrentgemma | ejkernel | EasyDeL | marin/levanter | Notes |
|---|---|---|---|---|---|---|
| Mamba1 selective scan | **`mosaic_tpu` (novel `mamba_kernels.py`)** | — | — | (via SSM1Op wrapper) | — | Adapted from recurrentgemma LRU scan |
| Mamba2 / SSD chunked scan | **`mosaic_tpu` (novel `ssd_kernels.py`)** | — | — | (via SSM2Op wrapper) | **`xla` only — TPU Pallas explicitly absent** | Two-level chunk/subchunk recomputation pattern |
| Mamba3 MIMO | — | — | — | — | `xla` only | Intentionally no Pallas |
| LRU scan / RG-LRU (Griffin) | derived | **`mosaic_tpu` (canonical; real+complex accumulators)** | — | — | — | Ancestor of axlearn's Mamba |
| Linear attention (RAttention) | **`mosaic_tpu` (novel)** | — | — | — | — | Chunked; feature-map; residual variants |

**Pre-directory state of the wiki**: zero public TPU Pallas SSM kernel ingested. **Directory finds three**: axlearn Mamba1/Mamba2/RAttention + recurrentgemma LRU scan. axlearn is by far the richest SSM Pallas source publicly.

### PRNG

| Kernel | jax-ml/jax | Notes |
|---|---|---|
| `philox_4x32` | `mosaic_tpu` (experimental) | Fused with `shaped_iota` to avoid materializing counters in HBM |
| `threefry_2x32_count` | `mosaic_tpu` (experimental) | Same rationale |

Internal JAX random integration.

### Cross-entropy / loss

| Kernel | tokamax | marin/levanter | Notes |
|---|---|---|---|
| `linear_softmax_cross_entropy_loss` (fused linear + softmax + NLL) | **`mosaic_tpu`** (sole TPU-only kernel in tokamax README) | **`mosaic_tpu`** (tokamax-derived; adds logsumexp penalty, logit soft-cap, loss weighting, argmax return) | [arXiv:2410.10989](https://arxiv.org/abs/2410.10989) — avoids materializing `[B, V]` logits |
| `linear_softmax_cross_entropy_loss` (GPU) | — | **`triton`** (H100/A100 stable; GB10 experimental) | 101,376-byte weight-tile limit shared across NVIDIA |

### Non-ML applications

| Kernel | jaxite | Notes |
|---|---|---|
| Negacyclic polymul (FHE) | **`mosaic_tpu`** (novel) | CGGI boolean-gate bootstrap; 4 bytes-split bf16 matmuls reassembled to u32; `bat_matmul` batched variant. Reference for integer-heavy non-ML Pallas |

### Compiler target

| Entry | pytorch/pytorch | Notes |
|---|---|---|
| `PallasPrinter` + `SIMDKernel` Pallas backend | `torch/_inductor/codegen/pallas.py` | **Not a kernel library — PyTorch Inductor codegen that emits Pallas source.** Relevant for `torch.compile` Pallas backend |

## Stability distribution

Rough counts across all six groups (see subpages for exact rows):

| Tier | Approx kernel count | Commentary |
|---|---|---|
| `stable` (production-used) | ~60 | MaxText training attention, RPA v2/v3 in tpu-inference + sglang-jax, megablox family, tokamax `ragged_dot` + `linear_softmax_cross_entropy_loss`, axlearn flash/decoding/paged |
| `experimental` (explicitly flagged in path or docstring) | ~80 | Everything under `jax/experimental/pallas/ops/*`, `tokamax/_src/ops/experimental/*`, `experimental/batched_rpa/*`, most ejkernel/EasyDeL files, qwix `contrib/`, axlearn scatter_update_pages |
| `research` / `paper companion` | ~25 | haoliuhl/ringattention, flashback, gla-jax, axlearn SSM/RAttention, jaxite, zig-zag-seeking experiments |
| `pedagogical` | ~10 | sqtian matmul series, recompute_dont_restore, nthnluu GPU-kernel-codelab, pallas-forge, upstream `example_kernel.py`/`matmul.py`/`all_gather.py` |
| `deprecated` | ~6 | aqt's four pallas files (replaced by qwix); jax-flash-attn2; Essential-AI maxtext snapshot |
| `vendored-only` (no original content) | ~30 | labyrinth-ssr/tpu-research (wholesale vendor of tpu_inference), Essential-AI/maxtext-external (vendor of maxtext), misc embedded vendored copies |

**Production-grade TPU kernels (stable + called on critical paths)**: a narrow set, ~25 kernels: splash attention (upstream + MaxText + MaxDiffusion + tokamax vendored), paged attention (upstream + derivatives), ragged_paged_attention v2/v3 (tpu-inference + vendored), MLA v1/v2 (tpu-inference), megablox gmm/v2 (upstream + vendored), `linear_softmax_cross_entropy_loss` (tokamax + marin/levanter), fused_moe v1 (tpu-inference + vendored), quantized_matmul blockwise (tpu-inference + vendored), all_gather_matmul (tpu-inference + ejkernel), and a handful of maxtext-specific pieces (`sc_gather_reduce`, `ragged_attention`, paged v2).

## Autotune / perf-tuning artifacts — crown jewels

The highest-value non-kernel artifacts found across the ecosystem. These are directly usable priors for any TPU optimization loop.

### Tuned block-size tables (static expert-knowledge dictionaries)

Ranked by entry count. `mosaic_tpu` unless noted.

| # | Source | Entries | Coverage | Keys | Notes |
|---|---|---|---|---|---|
| 1 | [sglang-jax ragged_paged_attention/tuned_block_sizes.py](https://github.com/sgl-project/sglang-jax/blob/main/python/sgl_jax/srt/kernels/ragged_paged_attention/tuned_block_sizes.py) | ~2,000+ | v4, v5, v6e, v7 | dtype, head-config, page_size, max_context | Largest table in the ecosystem |
| 2 | [tpu-inference ragged_paged_attention/v2/tuned_block_sizes.py](https://github.com/vllm-project/tpu-inference/blob/main/tpu_inference/kernels/ragged_paged_attention/v2/tuned_block_sizes.py) | ~1,200 | v5, v6 | `(q_dtype, kv_dtype, q_head, kv_head, head_dim, page_size, max_context, max_seq)` → `(kv_pages_per_block, queries_per_block)` | Prior-generation reference |
| 3 | [tpu-inference quantized_matmul/tuned_block_sizes.py](https://github.com/vllm-project/tpu-inference/blob/main/tpu_inference/kernels/quantized_matmul/tuned_block_sizes.py) | 600+ | v6 (**96 MiB VMEM**), v7 (**48 MiB VMEM**) | `(tpu_ver, m, n, k, lhs_dtype, rhs_dtype)` | VMEM budgets worth recording as concept facts |
| 4 | [tpu-inference ragged_paged_attention/v3/tuned_block_sizes.py](https://github.com/vllm-project/tpu-inference/blob/main/tpu_inference/kernels/ragged_paged_attention/v3/tuned_block_sizes.py) + hd64 variant | hundreds | v6e, v7 | similar to v2 | Paired with the `_hd64` specialization |
| 5 | [tpu-inference megablox/tuned_block_sizes.py](https://github.com/vllm-project/tpu-inference/blob/main/tpu_inference/kernels/megablox/tuned_block_sizes.py) | 47 | dtype-keyed | `(m, k, n, num_groups, shard_groups, lhs_dtype, rhs_dtype, quant_block)` → `(tm, tk, tn)` | All bf16×fp8_e4m3fn |
| 6 | [tpu-inference fused_moe/v1/tuned_block_sizes.py](https://github.com/vllm-project/tpu-inference/blob/main/tpu_inference/kernels/fused_moe/v1/tuned_block_sizes.py) | 28 | **v7 only** (comment: "formulas only applied to tpu-v7; need more for other generations") | 8-tuple | MoE under-tuned on v5/v6 |
| 7 | [sglang-jax multimodal/kernels/tuned_block_sizes.py](https://github.com/sgl-project/sglang-jax/blob/main/python/sgl_jax/srt/multimodal/kernels/tuned_block_sizes.py) | — | — | — | Separate multimodal flash-attn table |
| 8 | [tpu-inference collectives/all_gather_matmul_tuned_block_sizes.py](https://github.com/vllm-project/tpu-inference/blob/main/tpu_inference/kernels/collectives/all_gather_matmul_tuned_block_sizes.py) | — | v5e, v6e, v7x | weight-dtype-keyed (w16a16…w4a4) | Microbench-driven |
| 9 | [marin/levanter tuned_block_sizes.py](https://github.com/marin-community/marin/blob/main/lib/levanter/src/levanter/kernels/pallas/fused_cross_entropy_loss/tuned_block_sizes.py) | (modest) | per-device-kind: `"default"`, `"NVIDIA"`, `"NVIDIA GB10"`, `"NVIDIA H100"`, `"NVIDIA A100"` | `(dtype, shape_bucket)` → `BlockSizes(b, h, v)` | Hand-curated fallback for the autotune harness |

### Dynamic autotuners (search at deploy-time)

- **[tokamax.autotune](https://github.com/openxla/tokamax/blob/main/tokamax/_src/autotuning/api.py)** — kernel-author tool. Walks HLO, finds Tokamax ops, sweeps `Config` space, returns re-enterable `AutotuningResult`. Write-time, one-shot.
- **[marin/levanter autotune harness](https://github.com/marin-community/marin/tree/main/lib/levanter/src/levanter/kernels/pallas)** (`autotune_utils.py` + `cost_estimate_utils.py` + `autotune_cache_utils.py`) — deployment-time tuner, kernel-agnostic, shard-aware, compile-cost-aware, GCS-persistent. `_AUTOTUNE_COMPILE_HIT_THRESHOLD_S = 0.20` filters candidates whose compile time alone dominates training-step time. VMEM-OOM-aware fallthrough. jaxpr-hashed cache keys. **For this wiki's autoresearch loop, this is the pattern to emulate.**
- **[pallas-forge](../codebases/pallas-forge.md) roofline+autotune** — already ingested; forward-only (no custom_vjp) blocker documented in the Gemma 4 program.
- **[ucb-bar/autocomp](https://github.com/ucb-bar/autocomp)** + **[primatrix/Glaucis](https://github.com/primatrix/Glaucis)** + **[aryatschand/JAXBench](https://github.com/aryatschand/JAXBench)** — meta-agents that *use* Pallas as an optimization target. Novel category; direct analogues of this wiki's autoresearch mission.

### Other tuning-relevant facts distilled from the catalog

- VMEM budgets baked into kernels: quantized_matmul v6=96 MiB, v7=48 MiB; RPA default=100 MiB; update_kv_cache=64 MiB.
- NVIDIA weight-tile-bytes limit from marin: **101,376 bytes** (H100 232,448 per-SM shared minus ~131 KB overhead), same on GB10.
- DMA-overhead-equivalent from [simply](https://github.com/google-deepmind/simply/blob/main/simply/utils/ragged_paged_attention.py): **~0.5 MiB virtual bytes**, assumed constant across TPU generations. Balance against padding overhead.
- AF3 fused-GLU autotune: `block_m ∈ [32, 128]`, `block_n ∈ [32, 256]`, `block_k = 32`; split-K fallback when `num_blocks < core_count`.
- Ragged GDR decode speedup: [ejkernel README](https://github.com/erfanzar/ejkernel) — **3.6×**.

## Reusable Pallas-authoring patterns (concept-page candidates)

These are cross-cutting techniques that appear in multiple kernels and deserve their own concept pages (most are already concepts in the wiki; a handful are new).

1. **Online softmax with logit sink** — axlearn splash extension. Init `m` with sink; add `exp(sink − m_final)` to denominator at normalize. Applies to any flash-attention variant.
2. **Dropout inside kernel from prng_key + block indices** — axlearn splash. Avoids host-materialized dropout mask. Pair with Pallas `key<pl>` lowering bug workaround (prefetch prng_key).
3. **Two-level chunk/subchunk recomputation** — axlearn SSD. Store coarse-grained carries, recompute fine-grained states. Applies to any linear-recurrence Pallas kernel.
4. **Grouped program-IDs to minimize L2 footprint** — AlphaFold3 `_get_best_pids` / `_get_group_cache_usage`. Reusable in any GPU Pallas GEMM.
5. **DMA-overhead-bytes heuristic** for block-size autotuning — simply's `autotune_block_sizes`. Treat DMA setup as ~0.5 MiB "virtual bytes"; balance against padding overhead.
6. **Multi-shard sequence-parallel correction** for linear recurrences — recurrentgemma `multi_shard_correction`. Run local scan per shard, broadcast final `h` and `a_prod`, recompose.
7. **Block-sparse offset masks for paged attention** — axlearn `tpu_paged_attention_kernel`. Precompute `(n_kv_blocks, n_kv_blocks)` offsets into unmasked blocks; turns sliding-window into dense-load-over-sparse-offset.
8. **jaxpr-hash cache keys for autotuning** — marin/levanter `_autotune_jaxpr_hash`. Pins cache entries to jaxpr shape; invalidates silently on dtype/soft-cap changes.
9. **Compile-time-aware candidate filtering** — marin/levanter `_AUTOTUNE_COMPILE_HIT_THRESHOLD_S = 0.20`. Discard candidates whose XLA compile cost alone dominates training-step time.
10. **VMEM-OOM-aware fallthrough** — marin/levanter `_is_tpu_vmem_compile_error`. Demote candidates that hit `resource_exhausted … vmem` during lowering.
11. **Manual MLIR-dialect Pallas (below `pallas_call`)** — maxtext `sc_gather_reduce` + tokamax Blackwell attention. When you need TCGEN05 / SparseCore control that `pl.pallas_call` doesn't expose, drop to `jax.experimental.mosaic` + `jaxlib.mlir.dialects.{arith,func,memref,scf,vector}`.
12. **Pallas-on-Triton fused GEMM+activation+GEMM** — AlphaFold3 GLU. Pattern: two matmuls sharing one activation load, optional epilogue, dst aliasing. Directly portable to a Mosaic-TPU GLU.
13. **Custom splash masks for non-LLM domains** — graphcast `WeatherMeshMask`. Any structured adjacency can become a banded block-sparse splash.

## Confirmed gaps and absences

- **Zig-Zag / load-balanced causal Ring Attention on TPU** — confirmed absent from every repo surveyed, including the canonical haoliuhl/ringattention (unidirectional, straight `below_or_on_diag`), ejkernel (Splash wrapper), EasyDeL (inherits from ejkernel), maxdiffusion's integration, and tokamax's experimental copy. Brandon et al. 2023 striped variant remains publicly unimplemented in Pallas as of 2026-04-23.
- **Pure-TPU Pallas LayerNorm / RMSNorm** — absent from tokamax, upstream, axlearn, maxtext. Gemma 4 exp 33 empirically confirmed this is because **XLA already fuses these patterns with neighbor matmuls** — Pallas loses when the compiler is already at the fused op. **Likely correct to leave unimplemented.**
- **Pure-TPU Pallas fused GLU** — absent from tokamax, upstream, maxtext. AlphaFold3 v3.0.1 provides a GPU fused GLU as a reference architecture; porting to Mosaic-TPU is feasible but needs HLO-level validation that XLA isn't already fusing the pattern (same lesson as norm).
- **Pallas triangle_multiplication** — tokamax ships only an XLA reference (`api.py` `Literal["xla"]`). No Pallas backend anywhere. Potentially addressable if AlphaFold3-style protein work enters the loop.
- **`google-deepmind/gemma`** — not enumerated by any agent. May ship Pallas. Previously flagged as a gap in the 2026-04-23 source survey; still a gap.
- **NVIDIA Mosaic-GPU kernel catalog for GPU-side parity** — Group A enumerated the Mosaic-GPU ops in jax-ml/jax (collective_matmul, all_gather_mgpu, reduce_scatter_mgpu, hopper_matmul, mixed_type_matmul, blackwell_matmul, ragged_dot_mgpu, transposed_ragged_dot_mgpu, blackwell_ragged_dot_mgpu, attention_mgpu, decode_attention, layer_norm, rms_norm, softmax) — but downstream GPU-Pallas repos (beyond tokamax, alphafold3, axlearn) were not exhaustively surveyed.
- **Closed-source training stacks** — Gemini training stacks are private; only partial mirrors on GitHub.
- **Anthropic / xAI / Cohere / Character** — Pallas users per job postings; no public repos.
- **Ragged Paged Attention paper arXiv ID** — agent-A saw `2604.15464` in a search result (likely scrape glitch / future-dated); verify the real ID before citing.

## Direct impact on open wiki state

Cross-references from this directory to existing wiki pages.

1. **[sources/2025-ultrascale-playbook.md](../sources/2025-ultrascale-playbook.md) Gaps & caveats #2** (wire tokamax `ring_attention_kernel` through `dot_product_attention`) — three reference impls now documented: [maxdiffusion](https://github.com/AI-Hypercomputer/maxdiffusion) `ring_attention_kernel.py` (splash-integrated), [haoliuhl/ringattention](https://github.com/haoliuhl/ringattention) (canonical standalone), [ejkernel ring_attention](https://github.com/erfanzar/ejkernel/tree/main/ejkernel/kernels/_pallas/tpu/ring_attention) (splash wrapper + mesh `axis_name`). Reduces hypothesis from "open research" to "port + adapt" with three patterns to choose among.

2. **[sources/2025-ultrascale-playbook.md](../sources/2025-ultrascale-playbook.md) Gaps & caveats #3** (Zig-Zag Ring Attention on TPU — "no implementation found") — **retraction stands.** Ring Attention Pallas exists (§6.4 haoliuhl), but **Zig-Zag causal-balance variant is absent from every surveyed repo.** Remains an open algorithmic port from Brandon et al. 2023.

3. **[sources/2025-ultrascale-playbook.md](../sources/2025-ultrascale-playbook.md) Gaps & caveats #4** (TPU-native Pallas kernels for `gated_linear_unit` and `layer_norm` in tokamax) — **partially retracted.**
   - **RMSNorm/LayerNorm**: the absence from maxtext + tpu-inference + axlearn + upstream is external evidence that XLA-fusion is sufficient. **Gemma 4 exp 33's -8.1% empirical result is consistent with the ecosystem.** Don't build.
   - **Fused GLU**: [alphafold3 v3.0.1](https://github.com/google-deepmind/alphafold3/blob/v3.0.1/src/alphafold3/jax/gated_linear_unit/matmul_ext.py) provides a production Pallas fused-GLU reference (GPU). Porting to Mosaic-TPU is feasible; needs HLO-level validation that XLA isn't already fusing the equivalent pattern.

4. **[analyses/2026-04-23-gemma4-v6e4-optimization-ceiling.md](2026-04-23-gemma4-v6e4-optimization-ceiling.md)** Pallas-loses-to-XLA lesson (exp 33) — the directory substantiates this with **external absence of TPU Pallas norm kernels** and presence of TPU Pallas only where XLA genuinely can't express the fusion (online softmax in splash/flash, grouped matmul, paged-cache DMA patterns).

5. **[log.md](../log.md) Wave 1 tokamax findings** — `ring_attention_kernel` reachability gap remains (tokamax internal experimental tree). `gated_linear_unit` / `layer_norm` TPU Pallas absence now better-contextualized. Splash backward block-size autotuning gap unaddressed by the directory — still a tokamax-internal hypothesis.

## Recommended next ingestion wave (Wave 4 proposal)

If you pursue a Wave 4 to ingest the top novel-content repos as wiki codebases, my read of the directory is:

1. **[apple/axlearn](https://github.com/apple/axlearn)** (scope narrowly: `axlearn/common/flash_attention/`, `ssm_kernels/`, `megablock/`, `kv_cache/`, `rattention/kernels/`). **Uniquely novel SSM Pallas.** Paper [arXiv:2507.05411](https://arxiv.org/pdf/2507.05411).
2. **[vllm-project/tpu-inference](https://github.com/vllm-project/tpu-inference)** — broadest novel kernel surface; 600+ quantized_matmul + 1,200+ RPA v2 tuning tables are immediate usable priors.
3. **[AI-Hypercomputer/maxtext](https://github.com/AI-Hypercomputer/maxtext)** — direct trainer analogue; tokamax-GMM fall-through, ChunkedCausalMask, sc_gather_reduce.
4. **[AI-Hypercomputer/maxdiffusion](https://github.com/AI-Hypercomputer/maxdiffusion)** (narrow: `src/maxdiffusion/kernels/splash_attention/` only) — ring-attention reference impl with splash dispatch.
5. **[haoliuhl/ringattention](https://github.com/haoliuhl/ringattention)** — single-file paper companion; ingest as source + concept page.
6. **[google-deepmind/alphafold3 @ v3.0.1](https://github.com/google-deepmind/alphafold3/tree/v3.0.1/src/alphafold3/jax/gated_linear_unit)** — focused ingest of the `gated_linear_unit/` directory as fused-GEMM+activation+GEMM pattern reference (pin v3.0.1 — removed from main).
7. **[google-deepmind/recurrentgemma](https://github.com/google-deepmind/recurrentgemma)** — small; single LRU scan; link from axlearn for lineage.
8. **[erfanzar/ejkernel](https://github.com/erfanzar/ejkernel)** + **[EasyDeL](https://github.com/erfanzar/EasyDeL)** — broadest community TPU surface; ingest as pair (ejkernel codebase + EasyDeL consuming wrapper).
9. **[sgl-project/sglang-jax](https://github.com/sgl-project/sglang-jax)** (narrow: speculative-decoding kernels only) — only source for tree-verify Pallas.
10. **[marin-community/marin](https://github.com/marin-community/marin)** (narrow: `lib/levanter/src/levanter/kernels/pallas/` — harness + fused CE loss) — autotune-harness pattern is the pattern to emulate in this wiki.

Deferrable or low-priority: jaxite (niche non-ML), graphcast (wrapper), simply (wrapper), qwix/aqt (quantization framework — already referenced implicitly), JetStream (archiving), pytorch/pytorch Inductor (compilation target, not a library), labyrinth-ssr/tpu-research (vendor-only), Essential-AI/maxtext-external (snapshot).

## Sources

- Six web-research subagents, 2026-04-23, running in parallel with identical per-kernel row schemas.
- Raw per-repo reports preserved in subpages §1–§6.
- Every kernel row cites a specific file path as a GitHub URL; every performance claim is quoted verbatim from the source file or README.

## See also

- Subpages: [§1 Upstream JAX + tokamax](pallas-kernel-directory/01-upstream-jax-tokamax.md), [§2 AI-Hypercomputer](pallas-kernel-directory/02-ai-hypercomputer.md), [§3 Inference engines](pallas-kernel-directory/03-inference-engines.md), [§4 Research labs](pallas-kernel-directory/04-research-labs.md), [§5 Frameworks & quant](pallas-kernel-directory/05-frameworks-quant.md), [§6 Community](pallas-kernel-directory/06-community-research.md).
- [2026-04-23 Pallas kernel source survey](2026-04-23-pallas-kernel-source-survey.md) — the predecessor repo-level inventory this directory refines to kernel-level.
- [2026-04-23 Gemma 4 optimization ceiling](2026-04-23-gemma4-v6e4-optimization-ceiling.md) — the Pallas-vs-XLA-fusion lesson from exp 33 that this directory substantiates.
- [sources/2025-ultrascale-playbook.md](../sources/2025-ultrascale-playbook.md) — the hypothesis candidates this directory updates.
- [codebases/jax.md](../codebases/jax.md), [codebases/tokamax.md](../codebases/tokamax.md), [codebases/pallas-forge.md](../codebases/pallas-forge.md) — previously ingested Pallas codebases.
- [concepts/pallas-kernel.md](../concepts/pallas-kernel.md), [concepts/mosaic-kernel.md](../concepts/mosaic-kernel.md), [concepts/splash-attention.md](../concepts/splash-attention.md), [concepts/flash-attention.md](../concepts/flash-attention.md), [concepts/ring-attention.md](../concepts/ring-attention.md), [concepts/ragged-dot.md](../concepts/ragged-dot.md), [concepts/autotuning.md](../concepts/autotuning.md), [concepts/attention-block-sizes.md](../concepts/attention-block-sizes.md).
