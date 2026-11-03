---
title: 'Area: src/vllm_torchtpu/models'
type: area
area: 'src/vllm_torchtpu/models'
description: 'TPU-native model implementations and in-place patches for vLLM''s model registry: DeepSeek-V4, Kimi-Linear/K3 and Qwen4Exp, upstream-class patches for Qwen families, and the process-global wrapper context that lets kernels find the mesh and KV cache.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/models`

## Purpose
Most models run unchanged upstream vLLM code on top of the [layer adapters](layers.md). This area covers the exceptions. [vllm-model-patches](../concepts/vllm-model-patches.md) (the `models/vllm` root) explains its three jobs. It registers TPU-native implementations and per-architecture config hooks with vLLM's `ModelRegistry`. It patches upstream classes in place for families that otherwise run upstream code (Qwen2 GQA head padding, Qwen3-VL vision ops, Qwen3.5 sequence-parallel and overlap forwards). It also defines the process-global model-wrapper context the runner installs around load and every forward. Through that context, a Pallas op builder deep inside a layer finds the JAX mesh, the vLLM config and the bundled KV cache without threading them through vLLM's signatures.

The two large model implementations each have a page. [deepseek-v4-model](../concepts/deepseek-v4-model.md) swaps every DSv4 hot path for a TorchTPU-native piece: one Pallas attention op per layer covering the sliding-window and compressed passes, mHC residual mixing as Pallas ops with each layer seam fused, and Pallas ops built outside the trace and cached by geometry. [kimi-k3-model](../concepts/kimi-k3-model.md) implements the Kimi KDA/MLA hybrid with two execution regimes per forward: the default tensor-parallel path and an opt-in 32-way sequence-parallel prefill that swaps generic collectives for fused Pallas ring kernels.

For inference performance, this area is where model-specific fusion decisions live: which seams merge into one kernel, which collectives become ring kernels, and which upstream ops are replaced because they lower poorly on TPU.

## How the units connect
- [vllm-model-patches](../concepts/vllm-model-patches.md) is the entry: `register_models` adds the other units to vLLM's registry, and its wrapper context is read by every model and custom op below.
- [deepseek-v4-model](../concepts/deepseek-v4-model.md) (`deepseek_v4/`) uses the DSv4 kernels in [kernels](kernels.md) through the [custom ops](../concepts/custom-ops.md), plus its own attention backend and supported KV layouts.
- [kimi-k3-model](../concepts/kimi-k3-model.md) (`kimi_k3/`) delegates KDA, MLA and fused-MoE to the shared adapters and uses the ring collectives from [kimi-k3-kernels](../concepts/kimi-k3-kernels.md) on the SP prefill path.
- `qwen4_exp/` (no page) is Qwen4Exp (Qwen3.8 Flash Next) on TPU, which upstream enables only on CUDA and ROCm. `model.py` follows upstream's layer structure, wraps the attention and MoE sublayers in upstream's gated hyper-connections, and reuses the GDN, gated-attention and sparse-MoE layers that Qwen3.5 runs on TPU. `ple.py` ports the hashed n-gram PLE embedding as torch ops; n-gram ids are computed on device from the step's inputs so async scheduling does not need the newest sampled token on the host. `config.py` (`TPUQwen4ExpConfig`) adds checks for features the TPU model does not support yet.

<!-- area:auto:begin -->
## Units
4 planned unit(s) in `src/vllm_torchtpu/models`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/models/vllm/kimi_k3` | 8 | 306 | 0 | (internal) | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| `src/vllm_torchtpu/models/vllm/deepseek_v4` | 7 | 211 | 2 | [`DeepseekV4TPUAttentionBackend`](../catalog/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.md#DeepseekV4TPUAttentionBackend "src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py:L72"), [`supported_kv_cache_layouts`](../catalog/src/vllm_torchtpu/models/vllm/deepseek_v4/attention.md#DeepseekV4TPUAttentionBackend.supported_kv_cache_layouts "src/vllm_torchtpu/models/vllm/deepseek_v4/attention.py:L74") | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| `src/vllm_torchtpu/models/vllm` | 8 | 74 | 41 | [`set_vllm_model_wrapper_context`](../catalog/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.md#set_vllm_model_wrapper_context "src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py:L71"), [`get_vllm_model_wrapper_context`](../catalog/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.md#get_vllm_model_wrapper_context "src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py:L39"), [`get_pallas_op_mesh`](../catalog/src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.md#get_pallas_op_mesh "src/vllm_torchtpu/models/vllm/vllm_model_wrapper_context.py:L48") | [vllm-model-patches](../concepts/vllm-model-patches.md) |
| `src/vllm_torchtpu/models/vllm/qwen4_exp` | 3 | 87 | 1 | [`TPUQwen4ExpConfig`](../catalog/src/vllm_torchtpu/models/vllm/qwen4_exp/config.md#TPUQwen4ExpConfig "src/vllm_torchtpu/models/vllm/qwen4_exp/config.py:L26") | section below |

## Small units
### `src/vllm_torchtpu/models/vllm/qwen4_exp`
- modules: `src/vllm_torchtpu/models/vllm/qwen4_exp/config.py`, `src/vllm_torchtpu/models/vllm/qwen4_exp/model.py`, `src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py`
- entry points: [`TPUQwen4ExpConfig`](../catalog/src/vllm_torchtpu/models/vllm/qwen4_exp/config.md#TPUQwen4ExpConfig "src/vllm_torchtpu/models/vllm/qwen4_exp/config.py:L26")
- hubs: [`forward`](../catalog/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.md#Qwen4ExpPLELayer.forward "src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py:L526"), [`forward`](../catalog/src/vllm_torchtpu/models/vllm/qwen4_exp/ple.md#Qwen4ExpNGramEmbedding.forward "src/vllm_torchtpu/models/vllm/qwen4_exp/ple.py:L372"), [`forward`](../catalog/src/vllm_torchtpu/models/vllm/qwen4_exp/model.md#Qwen4ExpDecoderLayer.forward "src/vllm_torchtpu/models/vllm/qwen4_exp/model.py:L137")

<!-- area:auto:end -->
