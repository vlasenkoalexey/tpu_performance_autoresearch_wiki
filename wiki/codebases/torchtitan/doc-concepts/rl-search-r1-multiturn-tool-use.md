---
title: Search-R1 multi-turn retrieval-augmented GRPO recipe
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/examples/search_r1/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Search-R1 multi-turn retrieval-augmented GRPO recipe

## Definition
A multi-turn, tool-using TitanRL example: the policy gets a `search` tool, issues standard tool calls when it needs facts, receives retrieved passages back as `tool`-role messages, and finally answers. The reward is exact match (EM) against golden answers. Rollouts continue until the model stops calling tools or the turn budget is hit, and the whole thing runs on the stock multi-turn rollouter and continuous-batching generator - only the example folder and its config are task-specific.

## In torchtitan (grounded)
- Data: [`SearchR1Dataset`](../catalog/torchtitan/experiments/rl/examples/search_r1/data.md#SearchR1Dataset) / [`SearchR1Sample`](../catalog/torchtitan/experiments/rl/examples/search_r1/data.md#SearchR1Sample) stream the NQ/HotpotQA parquet from the Hugging Face hub on first use (or a local parquet with `question` / `golden_answers` columns).
- Environment: [`SearchR1Env`](../catalog/torchtitan/experiments/rl/examples/search_r1/env.md#SearchR1Env) (a [`MessageEnv`](../catalog/torchtitan/experiments/rl/environment/message.md#MessageEnv)) defines the tool spec, reads renderer-parsed tool calls in [`SearchR1Env.step`](../catalog/torchtitan/experiments/rl/examples/search_r1/env.md#SearchR1Env.step), calls the retrieval server and returns passages. The per-rollout turn budget is the [`TokenEnv`](../catalog/torchtitan/experiments/rl/environment/token.md#TokenEnv) `max_num_turns`.
- Reward: [`RewardExactMatch`](../catalog/torchtitan/experiments/rl/examples/search_r1/rubric.md#RewardExactMatch) - pure 0/1 EM by default, with two opt-in anti-closed-book levers: `no_search_penalty` (a correct answer that never searched scores less) and `retrieval_score` (a wrong answer gets partial credit if a search surfaced the golden answer).
- Wiring: [`SearchR1Rollouter`](../catalog/torchtitan/experiments/rl/examples/search_r1/rollouter.md#SearchR1Rollouter) / [`SearchR1Worker`](../catalog/torchtitan/experiments/rl/examples/search_r1/rollouter.md#SearchR1Worker); configs [`rl_grpo_qwen3_1_7b_search_r1`](../catalog/torchtitan/experiments/rl/examples/search_r1/config_registry.md#rl_grpo_qwen3_1_7b_search_r1), [`rl_grpo_qwen3_8b_search_r1`](../catalog/torchtitan/experiments/rl/examples/search_r1/config_registry.md#rl_grpo_qwen3_8b_search_r1), [`rl_grpo_muse_glimmer_30b_search_r1`](../catalog/torchtitan/experiments/rl/examples/search_r1/config_registry.md#rl_grpo_muse_glimmer_30b_search_r1), and the MoE perf config [`rl_grpo_qwen3_30b_a3b_deepep_search_r1_perf`](../catalog/torchtitan/experiments/rl/examples/search_r1/config_registry.md#rl_grpo_qwen3_30b_a3b_deepep_search_r1_perf).

## Why it matters / when it applies
- Thinking is controlled only by the renderer's `enable_thinking` flag (no injected think tags); this recipe sets it False because chain-of-thought does not help factoid EM and eats the multi-turn token budget.
- Requires a local dense retrieval server (e5 index over a wiki-18 corpus, top-k 3) listening on `http://127.0.0.1:8000/retrieve` before training, pinned to spare GPUs; `message_env.search_url` / `message_env.topk` override it.
- Reported results (README snapshots, held-out NQ test, greedy): Qwen3-1.7B EM ~0.05 -> ~0.41; Qwen3-8B EM ~0.26 -> ~0.45. Watch `validation_reward/_mean`.
- **Performance character:** this is the workload behind the bitwise-parity cost study - steps are dominated by multi-turn orchestration, CPU retrieval round-trips and on-policy straggler waits, which is why batch-invariant mode's ~2.5x compute slowdown did not show in wall-clock ([rl-batch-invariance-bitwise-parity](rl-batch-invariance-bitwise-parity.md)) and why windowed FIFO matters ([rl-windowed-fifo-scheduling](rl-windowed-fifo-scheduling.md)).
- **TPU relevance.** GPU-only recipe.

## Connections
- Code concepts: [rl-training](../concepts/rl-training.md), [qwen3-model](../concepts/qwen3-model.md), [muse-glimmer-model](../concepts/muse-glimmer-model.md)
- Module catalogs: [rl/examples/search_r1/env](../catalog/torchtitan/experiments/rl/examples/search_r1/env.md), [rl/examples/search_r1/rubric](../catalog/torchtitan/experiments/rl/examples/search_r1/rubric.md), [rl/examples/search_r1/config_registry](../catalog/torchtitan/experiments/rl/examples/search_r1/config_registry.md)
- Related doc-concepts: [titanrl-rollouter-api](titanrl-rollouter-api.md), [rl-batch-invariance-bitwise-parity](rl-batch-invariance-bitwise-parity.md), [rl-windowed-fifo-scheduling](rl-windowed-fifo-scheduling.md), [titanrl-architecture](titanrl-architecture.md)

## Source
Extracted from `torchtitan/experiments/rl/examples/search_r1/README.md` (kept in place).
