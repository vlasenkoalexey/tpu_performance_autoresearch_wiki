---
title: 'Area: src/vllm_torchtpu/spec_decode'
type: area
area: 'src/vllm_torchtpu/spec_decode'
description: 'TPU speculative-decoding drafters (Eagle3/MTP autoregressive heads and DFlash/DSpark block-diffusion drafters), built to keep every draft-path shape stable so drafting never triggers a recompile.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/spec_decode`

## Purpose
This area holds the on-device drafters behind vLLM's `--speculative-config`. Of the user-facing methods, ngram and suffix remain upstream host-side proposers. This area implements the device drafters: `Eagle3Proposer` (Eagle3 and MTP heads run autoregressively for K steps) and `DFlashProposer` (a block-diffusion drafter that proposes all K tokens in one forward), with the DSpark proposer subclassing DFlash and adding a sequential Markov head. The [runner](runner.md) fills each drafter's per-step `DraftChunkInputs` from the target's verify forward and then calls `propose`. Verification uses the rejection sampler in [layers](layers.md).

[speculative-decoding](../concepts/speculative-decoding.md) documents the mechanism. Its key design idea is that on TorchTPU every new shape is a new compiled program, so most of the code keeps the draft path shape-stable. Request counts are padded to buckets, small eager ops are pinned into fixed `torch.compile(backend="tpu")` regions, live counts travel as device scalars, and under EP-DP lockstep idle ranks replay the exact draft collective trace.

For inference performance, speculative decoding trades extra draft compute for fewer target decode steps. Whether that pays off on TPU depends on draft-path overhead, which is what this area works to keep low.

## How the units connect
One unit, owned by [speculative-decoding](../concepts/speculative-decoding.md): `eagle3.py` (`Eagle3Proposer`), `dflash.py` (`DFlashProposer`) and `dspark.py` (DSpark), `mtp_fused_loop.py` (MTP draft loop steps 1..K-1 compiled as one program instead of separate host dispatches per step), `mtp_loop_model.py` (a second compiled program for the loop steps of a DSA MTP layer whose trace-time decisions differ from step 0), and `utils.py` (`DraftChunkInputs`, row bucketing). Drafter models themselves are registered in [models](models.md) (DSpark and Qwen3.5 MTP).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/spec_decode`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/spec_decode` | 6 | 207 | 17 | [`DFlashProposer`](../catalog/src/vllm_torchtpu/spec_decode/dflash.md#DFlashProposer "src/vllm_torchtpu/spec_decode/dflash.py:L71"), [`Eagle3Proposer`](../catalog/src/vllm_torchtpu/spec_decode/eagle3.md#Eagle3Proposer "src/vllm_torchtpu/spec_decode/eagle3.py:L193"), [`DraftChunkInputs`](../catalog/src/vllm_torchtpu/spec_decode/utils.md#DraftChunkInputs "src/vllm_torchtpu/spec_decode/utils.py:L80") | [speculative-decoding](../concepts/speculative-decoding.md) |

<!-- area:auto:end -->
