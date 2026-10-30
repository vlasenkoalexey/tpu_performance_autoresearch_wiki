---
title: 'Module: torchtitan/experiments/tpu/overrides/fused_loss.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/overrides/fused_loss.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.overrides.fused_loss`/
symbols:
  fused_loss_soft_capped_lm_head: fused_loss_soft_capped_lm_head().
  fused_loss_lm_head: fused_loss_lm_head().
  FusedLossLinearWrapper: FusedLossLinearWrapper#
  FusedLossLinearWrapper.Config: FusedLossLinearWrapper#Config#
  FusedLossLinearWrapper.__init__: FusedLossLinearWrapper#__init__().
  FusedLossLinearWrapper.soft_cap: FusedLossLinearWrapper#soft_cap.
  FusedLossLinearWrapper.output_multiplier: FusedLossLinearWrapper#output_multiplier.
  FusedLossLinearWrapper.Config.soft_cap: FusedLossLinearWrapper#Config#soft_cap.
  FusedLossLinearWrapper.Config.output_multiplier: FusedLossLinearWrapper#Config#output_multiplier.
  FusedLossLinearWrapper.returns_loss_operands: FusedLossLinearWrapper#returns_loss_operands.
  FusedLossLinearWrapper.forward: FusedLossLinearWrapper#forward().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/overrides/fused_loss.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py)

## Classes
### <a id="FusedLossLinearWrapper"></a>`FusedLossLinearWrapper`  ·  implements/extends Linear
- def: [`torchtitan/experiments/tpu/overrides/fused_loss.py:18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L18)
- doc: LM-head replacement that supplies operands to a fused loss.
- signature: `class FusedLossLinearWrapper(Linear):`
- members:
  - <a id="FusedLossLinearWrapper.forward"></a>`forward(self, x: torch.Tensor)` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L53)
  - <a id="FusedLossLinearWrapper.output_multiplier"></a>`output_multiplier` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L51)
  - <a id="FusedLossLinearWrapper.returns_loss_operands"></a>`returns_loss_operands` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L39)
  - <a id="FusedLossLinearWrapper.soft_cap"></a>`soft_cap` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L50)
- protocol/private: <a id="FusedLossLinearWrapper.__init__"></a>`__init__`[`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L46)
- uses (calls/refs, reference-scoped): [`Linear`](../../../models/common/linear.md#Linear), [`bias`](../../../models/common/linear.md#Linear.Config.bias), [`__init__`](../../../models/common/linear.md#Linear.__init__), [`Config`](fused_loss.md#FusedLossLinearWrapper.Config), [`output_multiplier`](fused_loss.md#FusedLossLinearWrapper.Config.output_multiplier), [`soft_cap`](fused_loss.md#FusedLossLinearWrapper.Config.soft_cap)
- used by: [`Linear`](../../../models/common/linear.md#Linear), [`fused_loss_soft_capped_lm_head`](fused_loss.md#fused_loss_soft_capped_lm_head), [`fused_loss_lm_head`](fused_loss.md#fused_loss_lm_head)  (3 test-only)

### <a id="FusedLossLinearWrapper.Config"></a>`FusedLossLinearWrapper.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/overrides/fused_loss.py:42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L42)
- signature: `class Config(Linear.Config):`
- members:
  - <a id="FusedLossLinearWrapper.Config.output_multiplier"></a>`output_multiplier` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L44)
  - <a id="FusedLossLinearWrapper.Config.soft_cap"></a>`soft_cap` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L43)
- uses (calls/refs, reference-scoped): [`Linear`](../../../models/common/linear.md#Linear), [`Config`](../../../models/common/linear.md#Linear.Config)
- used by: [`fused_loss_soft_capped_lm_head`](fused_loss.md#fused_loss_soft_capped_lm_head), [`fused_loss_lm_head`](fused_loss.md#fused_loss_lm_head), [`__init__`](fused_loss.md#FusedLossLinearWrapper.__init__), [`output_multiplier`](fused_loss.md#FusedLossLinearWrapper.output_multiplier), [`soft_cap`](fused_loss.md#FusedLossLinearWrapper.soft_cap)  (2 test-only)

## Functions
- <a id="fused_loss_lm_head"></a>`fused_loss_lm_head(cfg: Linear.Config)` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L66)
- <a id="fused_loss_soft_capped_lm_head"></a>`fused_loss_soft_capped_lm_head(cfg: SoftCappedLinear.Config)` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L79)

## Module values
- <a id="__all__"></a>`__all__` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/fused_loss.py#L90)

