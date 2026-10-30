---
title: 'Module: torchtitan/experiments/tpu/overrides/discarded_token_counter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/overrides/discarded_token_counter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.overrides.discarded_token_counter`/
symbols:
  tpu_discarded_token_counter: tpu_discarded_token_counter().
  TpuDiscardedTokenCounterMoE.Config: TpuDiscardedTokenCounterMoE#Config#
  TpuDiscardedTokenCounterMoE: TpuDiscardedTokenCounterMoE#
  TpuDiscardedTokenCounterMoE.__getattr__: TpuDiscardedTokenCounterMoE#__getattr__().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/overrides/discarded_token_counter.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/discarded_token_counter.py)

## Classes
### <a id="TpuDiscardedTokenCounterMoE"></a>`TpuDiscardedTokenCounterMoE`  ·  implements/extends MoE
- def: [`torchtitan/experiments/tpu/overrides/discarded_token_counter.py:16`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/discarded_token_counter.py#L16)
- doc: `MoE` that hands out a throwaway in place of its token counter.
- signature: `class TpuDiscardedTokenCounterMoE(MoE):`
- protocol/private: <a id="TpuDiscardedTokenCounterMoE.__getattr__"></a>`__getattr__`[`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/discarded_token_counter.py#L28)
- uses (calls/refs, reference-scoped): [`MoE`](../../../models/common/moe.md#MoE), [`load_balance_coeff`](../../../models/common/moe.md#MoE.load_balance_coeff)
- used by: [`MoE`](../../../models/common/moe.md#MoE), [`tpu_discarded_token_counter`](discarded_token_counter.md#tpu_discarded_token_counter)  (1 test-only)

### <a id="TpuDiscardedTokenCounterMoE.Config"></a>`TpuDiscardedTokenCounterMoE.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/overrides/discarded_token_counter.py:25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/discarded_token_counter.py#L25)
- signature: `class Config(MoE.Config):`
- uses (calls/refs, reference-scoped): [`MoE`](../../../models/common/moe.md#MoE), [`Config`](../../../models/common/moe.md#MoE.Config)
- used by: [`tpu_discarded_token_counter`](discarded_token_counter.md#tpu_discarded_token_counter)  (1 test-only)

## Functions
- <a id="tpu_discarded_token_counter"></a>`tpu_discarded_token_counter(config: MoE.Config)` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/discarded_token_counter.py#L52)

## Module values
- <a id="__all__"></a>`__all__` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/discarded_token_counter.py#L58)

