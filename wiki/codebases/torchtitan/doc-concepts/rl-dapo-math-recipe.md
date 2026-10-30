---
title: DAPO Math reference RL recipe (Qwen3-4B)
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/examples/dapo_math/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# DAPO Math reference RL recipe (Qwen3-4B)

## Definition
The reference TitanRL experiment: single-turn verifiable math (user problem -> one assistant solution -> binary Math-Verify reward on the last `\boxed{...}` answer) training Qwen3-4B-Base with the DAPO loss on a filtered 12,643-row DAPO-Math-17k split, validated on the 30 AIME 2025 problems. Two configs share everything except token budgets: 8K responses (default) and 32K responses (not yet benchmarked).

## In torchtitan (grounded)
- Configs: [`rl_dapo_qwen3_4b_math_8k`](../catalog/torchtitan/experiments/rl/examples/dapo_math/config_registry.md#rl_dapo_qwen3_4b_math_8k) (prompt 2,048 / response 8,192 / packing 10,240 tokens) and [`rl_dapo_qwen3_4b_math_32k`](../catalog/torchtitan/experiments/rl/examples/dapo_math/config_registry.md#rl_dapo_qwen3_4b_math_32k) (response 32,768 / packing 34,816), both built by [`_qwen3_4b_dapo_math_config`](../catalog/torchtitan/experiments/rl/examples/dapo_math/config_registry.md#_qwen3_4b_dapo_math_config).
- Experiment pieces: [`DapoMathDataset`](../catalog/torchtitan/experiments/rl/examples/dapo_math/data.md#DapoMathDataset), [`AIME2025Dataset`](../catalog/torchtitan/experiments/rl/examples/dapo_math/data.md#AIME2025Dataset), [`DapoMathEnv`](../catalog/torchtitan/experiments/rl/examples/dapo_math/env.md#DapoMathEnv), [`RewardMathVerify`](../catalog/torchtitan/experiments/rl/examples/dapo_math/rubric.md#RewardMathVerify) / [`score_math_response`](../catalog/torchtitan/experiments/rl/examples/dapo_math/rubric.md#score_math_response), composed by [`DapoMathRollouter`](../catalog/torchtitan/experiments/rl/examples/dapo_math/rollouter.md#DapoMathRollouter) and [`DapoMathWorker`](../catalog/torchtitan/experiments/rl/examples/dapo_math/rollouter.md#DapoMathWorker).
- Topology and loop (from the shared builder): one [`PolicyTrainer`](../catalog/torchtitan/experiments/rl/actors/trainer.md#PolicyTrainer) at TP=2 (FSDP degree 1) on 2 GPUs + six [`VLLMGenerator`](../catalog/torchtitan/experiments/rl/actors/generator.md#VLLMGenerator) replicas at TP=1 behind an [`InterGeneratorRouter`](../catalog/torchtitan/experiments/rl/routing/inter_generator_router.md#InterGeneratorRouter) with [`LeastLoadedRoutingStrategy`](../catalog/torchtitan/experiments/rl/routing/strategies.md#LeastLoadedRoutingStrategy); 150 optimizer steps, 8 prompt groups x 16 completions per step, `target_offpolicy_steps=4`.
- Numerics/perf knobs: [`DAPOLoss`](../catalog/torchtitan/experiments/rl/losses/dapo.md#DAPOLoss) with ratio clip `[0.2, 0.28]` wrapped in an 8-chunk [`ChunkedLossWrapper`](../catalog/torchtitan/components/loss.md#ChunkedLossWrapper); fp32 LM head via [`LMHeadCastConverter`](../catalog/torchtitan/experiments/rl/models/cast_linear.md#LMHeadCastConverter) with a bf16 model forward; varlen attention; constant LR 1e-6 (AdamW, betas 0.9/0.98, wd 0.1); trainer compile with the `aot_eager` backend; generator CUDA graphs on ([`VLLMCudagraphConfig`](../catalog/torchtitan/experiments/rl/actors/generator.md#VLLMCudagraphConfig)).

## Why it matters / when it applies
- It is the canonical end-to-end RL workload in the repo: when comparing RL throughput changes, this recipe and its 8-GPU topology are the baseline the README points to.
- Setup: install the recipe's Math-Verify requirement, download `Qwen/Qwen3-4B-Base` into `torchtitan/experiments/rl/example_checkpoint`, run from the repo root with `--module dapo_math --config rl_dapo_qwen3_4b_math_8k` (optionally `--dump-folder ...`).
- Results status: the README has reward and response-length plots for the 150-step 8K run but no eval numbers yet (TODO), and the 32K variant is unbenchmarked.
- The same recipe with the rollout path replaced by Verifiers is [rl-verifiers-integration](rl-verifiers-integration.md).
- **TPU relevance.** GPU-only recipe; the transferable parts are the chunked loss and fp32 LM-head choices, which mirror TPU-lane loss-precision concerns (see [quantization](../concepts/quantization.md)).

## Connections
- Code concepts: [rl-training](../concepts/rl-training.md), [qwen3-model](../concepts/qwen3-model.md), [training-components](../concepts/training-components.md)
- Module catalogs: [rl/examples/dapo_math/config_registry](../catalog/torchtitan/experiments/rl/examples/dapo_math/config_registry.md), [rl/examples/dapo_math/rubric](../catalog/torchtitan/experiments/rl/examples/dapo_math/rubric.md), [rl/losses/dapo](../catalog/torchtitan/experiments/rl/losses/dapo.md)
- Related doc-concepts: [titanrl-rollouter-api](titanrl-rollouter-api.md), [titanrl-architecture](titanrl-architecture.md), [rl-windowed-fifo-scheduling](rl-windowed-fifo-scheduling.md), [rl-verifiers-integration](rl-verifiers-integration.md)

## Source
Extracted from `torchtitan/experiments/rl/examples/dapo_math/README.md` (kept in place).
