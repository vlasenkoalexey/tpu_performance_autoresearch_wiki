---
title: 'Module: torchtitan/experiments/tpu/overrides/bf16_rope.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/overrides/bf16_rope.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.overrides.bf16_rope`/
symbols:
  tpu_activation_dtype_cossin_rope: tpu_activation_dtype_cossin_rope().
  TpuActivationDtypeCosSinRoPE: TpuActivationDtypeCosSinRoPE#
  TpuActivationDtypeCosSinRoPE.Config: TpuActivationDtypeCosSinRoPE#Config#
  TpuActivationDtypeCosSinRoPE.apply_rotary_emb: TpuActivationDtypeCosSinRoPE#apply_rotary_emb().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/overrides/bf16_rope.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/bf16_rope.py)

## Classes
### <a id="TpuActivationDtypeCosSinRoPE"></a>`TpuActivationDtypeCosSinRoPE`  ·  implements/extends CosSinRoPE
- def: [`torchtitan/experiments/tpu/overrides/bf16_rope.py:26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/bf16_rope.py#L26)
- doc: Apply RoPE without materializing FP32 query/key intermediates.
- signature: `class TpuActivationDtypeCosSinRoPE(CosSinRoPE):`
- members:
  - <a id="TpuActivationDtypeCosSinRoPE.apply_rotary_emb"></a>`apply_rotary_emb(query: torch.Tensor, key: torch.Tensor | None, rope_cache: torch.Tensor, *, inverse: bool = False)` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/bf16_rope.py#L54)
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../../../models/common/rope.md#CosSinRoPE), [`_rotate_half`](../../../models/common/rope.md#CosSinRoPE._rotate_half)
- used by: [`CosSinRoPE`](../../../models/common/rope.md#CosSinRoPE), [`tpu_activation_dtype_cossin_rope`](bf16_rope.md#tpu_activation_dtype_cossin_rope), [`apply_rotary_emb`](../../../models/common/rope.md#CosSinRoPE.apply_rotary_emb)  (4 test-only)

### <a id="TpuActivationDtypeCosSinRoPE.Config"></a>`TpuActivationDtypeCosSinRoPE.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/overrides/bf16_rope.py:45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/bf16_rope.py#L45)
- signature: `class Config(CosSinRoPE.Config):`
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../../../models/common/rope.md#CosSinRoPE), [`Config`](../../../models/common/rope.md#CosSinRoPE.Config)
- used by: [`tpu_activation_dtype_cossin_rope`](bf16_rope.md#tpu_activation_dtype_cossin_rope)  (4 test-only)

## Functions
- <a id="tpu_activation_dtype_cossin_rope"></a>`tpu_activation_dtype_cossin_rope(config: CosSinRoPE.Config)` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/bf16_rope.py#L86)

## Module values
- <a id="__all__"></a>`__all__` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/overrides/bf16_rope.py#L92)

