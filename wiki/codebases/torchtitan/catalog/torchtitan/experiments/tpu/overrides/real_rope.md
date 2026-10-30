---
title: 'Module: torchtitan/experiments/tpu/overrides/real_rope.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/overrides/real_rope.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.overrides.real_rope`/
symbols:
  tpu_real_arithmetic_complex_rope: tpu_real_arithmetic_complex_rope().
  TpuRealArithmeticComplexRoPE: TpuRealArithmeticComplexRoPE#
  TpuRealArithmeticComplexRoPE.Config: TpuRealArithmeticComplexRoPE#Config#
  TpuRealArithmeticComplexRoPE.apply_rotary_emb: TpuRealArithmeticComplexRoPE#apply_rotary_emb().
  TpuRealArithmeticComplexRoPE.rotate: TpuRealArithmeticComplexRoPE#rotate().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/overrides/real_rope.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/real_rope.py)

## Classes
### <a id="TpuRealArithmeticComplexRoPE"></a>`TpuRealArithmeticComplexRoPE`  ·  implements/extends ComplexRoPE
- def: [`torchtitan/experiments/tpu/overrides/real_rope.py:30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/real_rope.py#L30)
- doc: The `ComplexRoPE` rotation, with the complex multiply written out.
- signature: `class TpuRealArithmeticComplexRoPE(ComplexRoPE):`
- members:
  - <a id="TpuRealArithmeticComplexRoPE.apply_rotary_emb"></a>`apply_rotary_emb(query: torch.Tensor, key: torch.Tensor | None, rope_cache: torch.Tensor, *, inverse: bool = False)` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/real_rope.py#L53) — Apply complex RoPE using adjacent-dim pairs, in real arithmetic.
  - <a id="TpuRealArithmeticComplexRoPE.rotate"></a>`rotate(x: torch.Tensor)` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/real_rope.py#L66)
- uses (calls/refs, reference-scoped): [`ComplexRoPE`](../../../models/common/rope.md#ComplexRoPE)
- used by: [`ComplexRoPE`](../../../models/common/rope.md#ComplexRoPE), [`tpu_real_arithmetic_complex_rope`](real_rope.md#tpu_real_arithmetic_complex_rope), [`apply_rotary_emb`](../../../models/common/rope.md#ComplexRoPE.apply_rotary_emb)  (5 test-only)

### <a id="TpuRealArithmeticComplexRoPE.Config"></a>`TpuRealArithmeticComplexRoPE.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/overrides/real_rope.py:49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/real_rope.py#L49)
- signature: `class Config(ComplexRoPE.Config):`
- uses (calls/refs, reference-scoped): [`ComplexRoPE`](../../../models/common/rope.md#ComplexRoPE), [`Config`](../../../models/common/rope.md#ComplexRoPE.Config)
- used by: [`tpu_real_arithmetic_complex_rope`](real_rope.md#tpu_real_arithmetic_complex_rope)  (1 test-only)

## Functions
- <a id="tpu_real_arithmetic_complex_rope"></a>`tpu_real_arithmetic_complex_rope(config: ComplexRoPE.Config)` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/real_rope.py#L90)

## Module values
- <a id="__all__"></a>`__all__` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/real_rope.py#L96)

