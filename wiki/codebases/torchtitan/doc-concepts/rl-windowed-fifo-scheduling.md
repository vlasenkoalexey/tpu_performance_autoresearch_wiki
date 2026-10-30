---
title: Windowed FIFO rollout scheduling and the off-policy bound
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/docs/windowed_fifo.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Windowed FIFO rollout scheduling and the off-policy bound

## Definition
TitanRL's async loop holds `B = (S + 1) * P` active prompt groups, where `P` is prompt groups per train step and `S` the target steady-state off-policy steps. **Strict FIFO** (always consume the oldest group) keeps every group within `S` steps but suffers head-of-line blocking: one slow group stalls the trainer even when younger groups are done. **Windowed FIFO** lets up to `W - 1` younger groups bypass the oldest, with the window anchored at the oldest active group, where `W = max(1, floor(f * B))` and `f` is `window_fraction` (default 0.3, after Section 6.2.4 of the MiniMax paper, arXiv 2605.26494).

## In torchtitan (grounded)
- Knobs on [`AsyncLoopConfig`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig): [`num_prompts_per_train_step`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig.num_prompts_per_train_step) (`P`, default 8), [`target_offpolicy_steps`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig.target_offpolicy_steps) (`S`, default 3), [`window_fraction`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig.window_fraction) (`f`, default 0.3; `None` = strict FIFO).
- Derived properties: [`max_active_rollout_groups`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig.max_active_rollout_groups) (`B`), [`window_size`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig.window_size) (`W`), [`max_offpolicy_steps`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig.max_offpolicy_steps) (`(B + W - 2) // P`). [`AsyncLoopConfig.__post_init__`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig.__post_init__) warns and falls back to `W = 1` when `f * B < 1`.
- Enforcement: [`RolloutGroupWorkBuffer`](../catalog/torchtitan/experiments/rl/components/work_buffer.md#RolloutGroupWorkBuffer) - slots acquired by [`RolloutGroupWorkBuffer.add_work`](../catalog/torchtitan/experiments/rl/components/work_buffer.md#RolloutGroupWorkBuffer.add_work) / [`RolloutGroupWorkBuffer.wait_for_slot`](../catalog/torchtitan/experiments/rl/components/work_buffer.md#RolloutGroupWorkBuffer.wait_for_slot), finished groups handed out by [`RolloutGroupWorkBuffer.take_finalized`](../catalog/torchtitan/experiments/rl/components/work_buffer.md#RolloutGroupWorkBuffer.take_finalized) within the window, slots freed by [`RolloutGroupWorkBuffer.release_active_groups`](../catalog/torchtitan/experiments/rl/components/work_buffer.md#RolloutGroupWorkBuffer.release_active_groups) after the train step's weight push/pull completes. Observed policy age is checked against the bound in [`compute_policy_age_metrics`](../catalog/torchtitan/experiments/rl/controller_metrics.md#compute_policy_age_metrics).

## Why it matters / when it applies
- Alternatives the doc rejects: **stall** (trainer idle), **greedy drop** (wastes completed rollouts, biases which samples reach training), **raise S** (ages every sample to accommodate a few stragglers). Windowed FIFO ages only the bypassed straggler, slightly.
- **Bound:** a target group admitted behind `B - 1` older groups, then bypassed by `W - 1` younger ones, is consumed after `B + W - 2` groups, so `max_offpolicy_steps = S + ceil((W - 1) / P)`; windowed FIFO adds at most `ceil((W - 1) / P)` steps of off-policyness.
- Worked example: `S=1, P=3, f=0.5` -> `B=6, W=3`; with group 2 slow, groups 3 and 4 may bypass it, group 5 stays blocked until 2 is consumed.
- Throughput angle: this is the RL pipeline's main defense against generator stragglers keeping the trainer idle; the bitwise-parity doc's Search-R1 measurements show straggler waits dominating step time.
- **TPU relevance.** Not TPU-specific; listed for completeness of the RL lane.

## Connections
- Code concepts: [rl-training](../concepts/rl-training.md), [observability](../concepts/observability.md)
- Module catalogs: [rl/controller](../catalog/torchtitan/experiments/rl/controller.md), [rl/components/work_buffer](../catalog/torchtitan/experiments/rl/components/work_buffer.md), [rl/controller_metrics](../catalog/torchtitan/experiments/rl/controller_metrics.md)
- Related doc-concepts: [titanrl-architecture](titanrl-architecture.md), [rl-batch-invariance-bitwise-parity](rl-batch-invariance-bitwise-parity.md), [rl-dapo-math-recipe](rl-dapo-math-recipe.md)

## Source
Extracted from `torchtitan/experiments/rl/docs/windowed_fifo.md` (kept in place).
