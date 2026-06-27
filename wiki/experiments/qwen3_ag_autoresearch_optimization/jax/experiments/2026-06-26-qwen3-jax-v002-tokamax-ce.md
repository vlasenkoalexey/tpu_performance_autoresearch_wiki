---
hypothesis: qwen3-jax-tokamax-ce
model: qwen3-ag-jax
variant: "8B/v6e-8"
status: in_progress
created: 2026-06-26
---

## Hypothesis under test
**Hypothesis**: Replacing the plain softmax CE (which materializes `[B,L,V=151936]` logits at the lm_head) with `tokamax.linear_softmax_cross_entropy_loss` (mosaic_tpu / chunked_xla, streamed logsumexp over V via shard_map) frees ~2.5 GiB/chip at seq 8192, removing the lm_head memory wall.

**Mechanism**: Toggle `skip_lm_head` so forward returns hidden; compute loss from `hidden` + `lm_head_weight()` inside the jit via the shard_map CE wrapper (mirror the llama3 jax lane's `_ce_tokamax`). fp32 boundary cast required for chunked_xla.

**Predicted signal**: Expect HBM usage to drop significantly compared to plain CE at large sequence lengths.

**Falsification criterion**: no HBM reduction vs plain CE (XLA already fuses the logit+softmax favorably — check HLO pre-filter first) → refuted `xla-already-fuses`.

## Setup

- **Code**: `jax/experiments/.repo/2026-06-26-v002-tokamax-ce` (forked from baseline)
- **Hardware**: TPU v6e-8 (`alekseyv-tpu-v6e8-spot-xpk`)
- **Command**: `python -m train --use_tokamax_ce=True --tokamax_ce_impl=mosaic_tpu --train_steps 20 --batch_size 1 --seqlen 8192`

## Results

**Status**: Crashed (OOM during XLA compilation).

The workload crashed during the HLO compilation phase because the HLO temp size exceeded the v6e-8 device memory limit. Specifically, the compiler attempted to allocate multiple `bf16[32,8192,8192]` tensors (the materialized causal attention score matrix for 32 query heads at 8K sequence length). 

Since this experiment was forked from the baseline, it used the plain `_attn_xla_sdpa` implementation, which fully materializes the `[B, Hq, T, T]` attention matrix. At `seqlen=8192`, this matrix takes ~4.3 GB *per layer*, which completely exhausts the HBM.

## Verdict

**Blocked**. 

While `tokamax-ce` may successfully stream the cross-entropy loss and save memory at the LM head, it is insufficient to unlock the 8K context length on its own. The `[B, Hq, T, T]` attention matrix memory dominates and causes an OOM long before the LM head is reached. 

To evaluate `tokamax-ce` at 8K context, we must combine it with `splash-attention` (which prevents the `[B, Hq, T, T]` materialization).
