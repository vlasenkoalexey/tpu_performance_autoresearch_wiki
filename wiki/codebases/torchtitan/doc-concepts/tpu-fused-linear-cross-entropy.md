---
title: Fused linear + softmax cross-entropy on TPU (tokamax Mosaic kernel)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Fused linear + softmax cross-entropy on TPU (tokamax Mosaic kernel)

## Definition
A tokamax Mosaic/Pallas kernel that fuses the `lm_head` matmul with softmax-cross-entropy so the full
`[batch, seq, vocab]` logits tensor is **never materialized**. It is bridged into TorchTPU as a
`custom_call`, composes with compile and FSDP, and turns the loss into one program instead of a chain
of eager ops. Its biggest value is **memory** (removes a huge activation at large vocab x batch, which
buys a bigger batch); the throughput effect grows with batch and is neutral when logits are small.

## In torchtitan (grounded)
- Kernel: [`linear_softmax_cross_entropy_loss`](../catalog/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.md#linear_softmax_cross_entropy_loss)
  (autograd wrapper [`TorchLinearLoss`](../catalog/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.md#TorchLinearLoss)).
- Loss wrapper: [`pallas_cross_entropy_loss`](../catalog/torchtitan/experiments/tpu/loss.md#pallas_cross_entropy_loss)
  flattens to token-major `[tokens, hidden]` / `[tokens]` / `[hidden, vocab]`, masks `IGNORE_INDEX`
  rows (zero hidden state, label 0, subtracts `log(vocab)` per ignored row), and supports an in-kernel
  soft-cap / output multiplier for soft-capped heads.
- Selection (current path): `loss = PallasCrossEntropyLoss.Config(...)`
  ([`PallasCrossEntropyLoss.Config`](../catalog/torchtitan/experiments/tpu/loss.md#PallasCrossEntropyLoss.Config):
  `implementation` `"mosaic_tpu"|"xla"`, `b_block_size=1024`, `h_block_size=512`, `v_block_size=2048`)
  plus the LM-head override [`fused_loss_lm_head`](../catalog/torchtitan/experiments/tpu/overrides/fused_loss.md#fused_loss_lm_head),
  which swaps the head for [`FusedLossLinearWrapper`](../catalog/torchtitan/experiments/tpu/overrides/fused_loss.md#FusedLossLinearWrapper)
  returning `(hidden, weight.T)` instead of logits. Recipes do both in one helper, e.g.
  [`_enable_pallas_cross_entropy`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#_enable_pallas_cross_entropy).
  CLI sweep: `--loss.b_block_size=...`.
- Legacy path: [`LossKernelConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#LossKernelConfig)
  (`use_loss_kernel`, `loss_b_block_size` 1024, `loss_h_block_size` 512, `loss_v_block_size` 2048,
  `enable_pallas_loss_kernel`) is translated by [`_legacy_pallas_loss_config`](../catalog/torchtitan/experiments/tpu/loss.md#_legacy_pallas_loss_config);
  [`build_cross_entropy_loss`](../catalog/torchtitan/experiments/tpu/loss.md#build_cross_entropy_loss)
  prefers an explicit `PallasCrossEntropyLoss.Config` and keeps the `loss_kernel` branch only as a
  migration fallback (marked TODO-remove).

## Why it matters / when it applies
- **Tile constraint:** flattened token count (`batch x seq` per rank) must be a multiple of
  `b_block_size`; keep it divisible by 1024 (or lower the tile for small debug batches). Tune
  `v_block_size` against the vocab size. Tiles are bounded by the scoped VMEM limit
  ([tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md)).
- **Defaults are a start, not an optimum.** The HF-backend lane's sweep (Llama-3.2-1B, 16,384
  tokens/rank) found b=512/1024/2048 -> 20,342 / 21,716 / 22,161 tok/s/device and b=4096
  RESOURCE_EXHAUSTED; h and v were best at 512 / 2048 ([`_fused_ce_loss`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#_fused_ce_loss)).
- It is also a dispatch lever: the loss becomes a single `custom_call` (see
  [tpu-dispatch-bound-mental-model](tpu-dispatch-bound-mental-model.md)).

**Doc vs code (two disagreements):**
1. The guide says a token count not divisible by `loss_b_block_size` makes the kernel *silently fall
   back to XLA*. At this commit `pallas_cross_entropy_loss` **raises `ValueError`** instead
   ("Do not silently switch implementations"); XLA is used only when `implementation="xla"` is chosen
   explicitly.
2. The guide says the `llama3_8b()` / `llama3_70b()` configs set `use_loss_kernel`. They actually
   select `PallasCrossEntropyLoss.Config()` + the fused-loss LM-head override via
   `_enable_pallas_cross_entropy`; `LossKernelConfig` is the legacy route (only one Qwen3 recipe still
   sets `use_loss_kernel=True`). Sweep with `--loss.*`, not `--loss_kernel.*`, on current recipes.

## Connections
- Code concepts: [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [training-components](../concepts/training-components.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [muse-glimmer-model](../concepts/muse-glimmer-model.md), [llama3-model](../concepts/llama3-model.md)
- Module catalogs: [loss (tpu)](../catalog/torchtitan/experiments/tpu/loss.md),
  [kernels/linear_softmax_cross_entropy_loss](../catalog/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.md),
  [overrides/fused_loss](../catalog/torchtitan/experiments/tpu/overrides/fused_loss.md),
  [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md)
- Related doc-concepts: [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md),
  [tpu-dispatch-bound-mental-model](tpu-dispatch-bound-mental-model.md),
  [hf-transformers-backend-on-tpu](hf-transformers-backend-on-tpu.md),
  [tpu-recipe-splash-and-loss-kernel-choices](tpu-recipe-splash-and-loss-kernel-choices.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (section 4, "Fused
linear + cross-entropy"; kept in place), cross-checked against `torchtitan/experiments/tpu/loss.py`.
