---
title: 'Module: torchtitan/experiments/rl/losses/dapo.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/losses/dapo.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.losses.dapo`/
symbols:
  DAPOLoss: DAPOLoss#
  DAPOLoss.Config: DAPOLoss#Config#
  DAPOLoss.__call__: DAPOLoss#__call__().
  DAPOLoss.Config.ratio_clip_low: DAPOLoss#Config#ratio_clip_low.
  DAPOLoss.Config.ratio_clip_high: DAPOLoss#Config#ratio_clip_high.
  DAPOLoss.__init__: DAPOLoss#__init__().
  DAPOLoss.ratio_clip_low: DAPOLoss#ratio_clip_low.
  DAPOLoss.ratio_clip_high: DAPOLoss#ratio_clip_high.
  _MAX_LOG_RATIO: _MAX_LOG_RATIO.
---
# Module: [`torchtitan/experiments/rl/losses/dapo.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py)

## Classes
### <a id="DAPOLoss"></a>`DAPOLoss`  ·  implements/extends BaseLoss
- def: [`torchtitan/experiments/rl/losses/dapo.py:23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L23) — documented in [rl-training](../../../../../concepts/rl-training.md)
- doc: Per-token clipped surrogate loss with DAPO-style "clip-higher".
- signature: `class DAPOLoss(BaseLoss):`
- members:
  - <a id="DAPOLoss.__call__"></a>`__call__(self, logits: torch.Tensor, labels: torch.Tensor, global_valid_tokens: float | None = None, *, generator_logprobs: torch.Tensor, advantages: torch.Tensor, loss_mask: torch.Tensor)` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L57) — Compute the per-token clip-higher surrogate loss.
  - <a id="DAPOLoss.ratio_clip_high"></a>`ratio_clip_high` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L55)
  - <a id="DAPOLoss.ratio_clip_low"></a>`ratio_clip_low` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L54)
- protocol/private: <a id="DAPOLoss.__init__"></a>`__init__`[`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L47)
- uses (calls/refs, reference-scoped): [`CompileConfig`](../../../config/configs.md#CompileConfig), [`BaseLoss`](../../../components/loss.md#BaseLoss), [`GRPOLoss`](grpo.md#GRPOLoss), [`compute_logprobs`](../../../components/loss.md#compute_logprobs), [`Config`](dapo.md#DAPOLoss.Config), [`ratio_clip_high`](dapo.md#DAPOLoss.Config.ratio_clip_high), [`ratio_clip_low`](dapo.md#DAPOLoss.Config.ratio_clip_low), [`_MAX_LOG_RATIO`](dapo.md#_MAX_LOG_RATIO)
- used by: [`BaseLoss`](../../../components/loss.md#BaseLoss), [`GRPOLoss`](grpo.md#GRPOLoss), [`__init__`](grpo.md#GRPOLoss.__init__)  (5 test-only)

### <a id="DAPOLoss.Config"></a>`DAPOLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/losses/dapo.py:39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L39)
- signature: `class Config(BaseLoss.Config):`
- members:
  - <a id="DAPOLoss.Config.ratio_clip_high"></a>`ratio_clip_high` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L43) — ---
  - <a id="DAPOLoss.Config.ratio_clip_low"></a>`ratio_clip_low` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L40) — ---
- uses (calls/refs, reference-scoped): [`BaseLoss`](../../../components/loss.md#BaseLoss), [`Config`](../../../components/loss.md#BaseLoss.Config)
- used by: [`__init__`](grpo.md#GRPOLoss.__init__), [`__init__`](dapo.md#DAPOLoss.__init__), [`ratio_clip_high`](dapo.md#DAPOLoss.ratio_clip_high), [`ratio_clip_low`](dapo.md#DAPOLoss.ratio_clip_low)  (5 test-only)

## Module values
- <a id="_MAX_LOG_RATIO"></a>`_MAX_LOG_RATIO` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/dapo.py#L20)

