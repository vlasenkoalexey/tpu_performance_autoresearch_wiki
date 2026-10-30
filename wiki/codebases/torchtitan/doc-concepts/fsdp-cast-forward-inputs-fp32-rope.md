---
title: FSDP cast_forward_inputs=False keeps the RoPE table in fp32
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/docs/bitwise_parity.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# FSDP cast_forward_inputs=False keeps the RoPE table in fp32

## Definition
TorchTitan stores the rotary-embedding cache `freqs_cis` in fp32 and passes it as a forward input to every transformer block. FSDP2's `MixedPrecisionPolicy(cast_forward_inputs=True)` would cast it to bf16 at each FSDP boundary; the later multiply promotes back to fp32, but the bf16 rounding of `cos`/`sin` has already happened. Core FSDP therefore wraps decoders with **`cast_forward_inputs=False`** so `freqs_cis` stays fp32 on every path.

## In torchtitan (grounded)
- [`apply_fsdp_to_decoder`](../catalog/torchtitan/distributed/fsdp.md#apply_fsdp_to_decoder) builds `MixedPrecisionPolicy(param_dtype, reduce_dtype, cast_forward_inputs=False)` for the decoder's `fully_shard` calls.
- RL relies on this as its bf16 boundary: [`parallelize_qwen3`](../catalog/torchtitan/models/qwen3/parallelize.md#parallelize_qwen3) applies `apply_fsdp_to_decoder` unconditionally, so even at `data_parallel_shard_degree=1` FSDP acts purely as a param-cast-to-bf16 boundary (the degree-1 all-gather is a no-op but still casts).
- The block-level FSDP parametrization in the graph lane has its own policy type, [`MixedPrecisionPolicy`](../catalog/torchtitan/experiments/graph_trainer/simple_fsdp.md#MixedPrecisionPolicy) (param/reduce dtype only).

## Why it matters / when it applies
- Required for bitwise-identical numerics **across parallelism configs** (e.g. TP-only vs FSDP+TP) and for trainer/generator parity in RL ([rl-batch-invariance-bitwise-parity](rl-batch-invariance-bitwise-parity.md)).
- Safe for LLMs whose float inputs are already `param_dtype`. Models with external fp32 inputs (image models such as Flux or VLM pixel values) may still need `cast_forward_inputs=True` - check before reusing the decoder helper for them.
- **TPU relevance.** This is a precision-boundary fact about core FSDP, not about GPUs. It is relevant when the TPU lane composes FSDP with bf16 params and fp32 RoPE, and when chasing loss-parity gaps between lanes: a RoPE table silently rounded to bf16 is a classic cross-lane mismatch. See [quantization](../concepts/quantization.md) for the precision stack and the TPU guide's [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md).

**Doc vs code at this commit:** the doc says this is set in "the canonical `apply_fsdp` (`torchtitan/distributed/fsdp.py`)". There is no `apply_fsdp` in that module; the setting lives in `apply_fsdp_to_decoder`. Per-model `apply_fsdp` functions exist elsewhere, e.g. in the Flux and transformers-backend parallelize modules.

## Connections
- Code concepts: [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [model-building-blocks](../concepts/model-building-blocks.md), [quantization](../concepts/quantization.md), [qwen3-model](../concepts/qwen3-model.md), [flux-diffusion-model](../concepts/flux-diffusion-model.md)
- Module catalogs: [distributed/fsdp](../catalog/torchtitan/distributed/fsdp.md), [models/qwen3/parallelize](../catalog/torchtitan/models/qwen3/parallelize.md)
- Related doc-concepts: [rl-batch-invariance-bitwise-parity](rl-batch-invariance-bitwise-parity.md), [simple-fsdp](simple-fsdp.md), [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md)

## Source
Extracted from `torchtitan/experiments/rl/docs/bitwise_parity.md` (kept in place).
