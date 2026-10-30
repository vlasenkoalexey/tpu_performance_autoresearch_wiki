---
title: 'Module: torchtitan/experiments/rl/losses/grpo.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/losses/grpo.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.losses.grpo`/GRPOLoss#
symbols:
  GRPOLoss: ''
  GRPOLoss.Config: Config#
  GRPOLoss.__init__: __init__().
  GRPOLoss.Config.clip_eps: Config#clip_eps.
---
# Module: [`torchtitan/experiments/rl/losses/grpo.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/grpo.py)

## Classes
### <a id="GRPOLoss"></a>`GRPOLoss`  ·  implements/extends DAPOLoss
- def: [`torchtitan/experiments/rl/losses/grpo.py:17`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/grpo.py#L17) — documented in [rl-training](../../../../../concepts/rl-training.md)
- doc: Per-token clipped surrogate loss for GRPO.
- signature: `class GRPOLoss(DAPOLoss):`
- protocol/private: <a id="GRPOLoss.__init__"></a>`__init__`[`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/grpo.py#L29)
- uses (calls/refs, reference-scoped): [`Config`](grpo.md#GRPOLoss.Config), [`DAPOLoss`](dapo.md#DAPOLoss), [`Config`](dapo.md#DAPOLoss.Config), [`ratio_clip_high`](dapo.md#DAPOLoss.Config.ratio_clip_high), [`ratio_clip_low`](dapo.md#DAPOLoss.Config.ratio_clip_low), [`__init__`](dapo.md#DAPOLoss.__init__), [`clip_eps`](grpo.md#GRPOLoss.Config.clip_eps)
- used by: [`trainer`](../controller.md#Controller.Config.trainer), [`loss`](../actors/trainer.md#PolicyTrainer.Config.loss), [`DAPOLoss`](dapo.md#DAPOLoss)  (13 test-only)

### <a id="GRPOLoss.Config"></a>`GRPOLoss.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/losses/grpo.py:25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/grpo.py#L25)
- signature: `class Config(BaseLoss.Config):`
- members:
  - <a id="GRPOLoss.Config.clip_eps"></a>`clip_eps` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/losses/grpo.py#L26) — ---
- uses (calls/refs, reference-scoped): [`BaseLoss`](../../../components/loss.md#BaseLoss), [`Config`](../../../components/loss.md#BaseLoss.Config)
- used by: [`trainer`](../controller.md#Controller.Config.trainer), [`loss`](../actors/trainer.md#PolicyTrainer.Config.loss), [`__init__`](grpo.md#GRPOLoss.__init__)  (13 test-only)

