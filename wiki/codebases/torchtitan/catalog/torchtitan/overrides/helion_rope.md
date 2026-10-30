---
title: 'Module: torchtitan/overrides/helion_rope.py'
type: catalog
provenance: extracted
module: torchtitan/overrides/helion_rope.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.overrides.helion_rope`/
symbols:
  _config: _config().
  _apply_helion_cossin_rope: _apply_helion_cossin_rope().
  _apply_helion_complex_rope: _apply_helion_complex_rope().
  helion_cos_sin_rope: helion_cos_sin_rope().
  helion_complex_rope: helion_complex_rope().
  _helion_cossin_rope_fwd: _helion_cossin_rope_fwd().
  _helion_complex_rope_fwd: _helion_complex_rope_fwd().
  _helion_cossin_rope_bwd: _helion_cossin_rope_bwd().
  _run_complex_bwd: _run_complex_bwd().
  HelionCosSinRoPE.forward: HelionCosSinRoPE#forward().
  HelionComplexRoPE.forward: HelionComplexRoPE#forward().
  _to_local: _to_local().
  HelionCosSinRoPE.Config: HelionCosSinRoPE#Config#
  HelionComplexRoPE.Config: HelionComplexRoPE#Config#
  _DEFAULT_CONFIG: _DEFAULT_CONFIG.
  _run_tuned: _run_tuned().
  _HELION_IMPORT_ERROR: _HELION_IMPORT_ERROR.
  HelionCosSinRoPE: HelionCosSinRoPE#
  _helion_complex_rope_bwd: _helion_complex_rope_bwd().
  _resolve_positions: _resolve_positions().
  HelionComplexRoPE: HelionComplexRoPE#
  _from_local: _from_local().
  _rope_cos_sin_bwd: _rope_cos_sin_bwd().
  _rope_complex_fwd: _rope_complex_fwd().
  _rope_complex_bwd: _rope_complex_bwd().
  _cossin_fwd_config: _cossin_fwd_config().
  _cossin_bwd_config: _cossin_bwd_config().
  _complex_fwd_config: _complex_fwd_config().
  _complex_bwd_config: _complex_bwd_config().
  _cossin_fwd_backward: _cossin_fwd_backward().
  _complex_fwd_backward: _complex_fwd_backward().
  _helion_cossin_rope_fwd_thk: _helion_cossin_rope_fwd_thk().
  _helion_complex_rope_fwd_thk: _helion_complex_rope_fwd_thk().
  __all__: __all__.
  _helion_cossin_rope_fwd_fake: _helion_cossin_rope_fwd_fake().
  _helion_cossin_rope_bwd_fake: _helion_cossin_rope_bwd_fake().
  _helion_complex_rope_fwd_fake: _helion_complex_rope_fwd_fake().
  _helion_complex_rope_bwd_fake: _helion_complex_rope_bwd_fake().
  HelionRoPE: HelionRoPE.
  _BOUND_KERNELS: _BOUND_KERNELS.
  _rope_cos_sin_fwd: _rope_cos_sin_fwd().
  _cossin_fwd_setup_context: _cossin_fwd_setup_context().
  _complex_fwd_setup_context: _complex_fwd_setup_context().
  _cossin_eligible: _cossin_eligible().
  _complex_eligible: _complex_eligible().
---
# Module: [`torchtitan/overrides/helion_rope.py`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py)

## Classes
### <a id="HelionComplexRoPE"></a>`HelionComplexRoPE`  ·  implements/extends ComplexRoPE
- def: [`torchtitan/overrides/helion_rope.py:1006`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L1006)
- doc: Complex RoPE applied with a fused real-valued Helion kernel.
- signature: `class HelionComplexRoPE(ComplexRoPE):`
- members:
  - <a id="HelionComplexRoPE.forward"></a>`forward(self, query: torch.Tensor, key: torch.Tensor | None = None, positions: torch.Tensor | None = None, *, inverse: bool = False)` — [`L1020`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L1020) — documented in [config-overrides](../../../concepts/config-overrides.md)
- uses (calls/refs, reference-scoped): [`ComplexRoPE`](../models/common/rope.md#ComplexRoPE), [`_apply_helion_complex_rope`](helion_rope.md#_apply_helion_complex_rope), [`forward`](../models/common/rope.md#RoPE.forward), [`cache`](../models/common/rope.md#RoPE.cache)
- used by: [`ComplexRoPE`](../models/common/rope.md#ComplexRoPE), [`helion_complex_rope`](helion_rope.md#helion_complex_rope), [`forward`](../models/common/rope.md#RoPE.forward)

### <a id="HelionComplexRoPE.Config"></a>`HelionComplexRoPE.Config`  ·  implements/extends Config
- def: [`torchtitan/overrides/helion_rope.py:1017`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L1017)
- signature: `class Config(ComplexRoPE.Config):`
- uses (calls/refs, reference-scoped): [`ComplexRoPE`](../models/common/rope.md#ComplexRoPE), [`Config`](../models/common/rope.md#ComplexRoPE.Config)
- used by: [`helion_complex_rope`](helion_rope.md#helion_complex_rope)

### <a id="HelionCosSinRoPE"></a>`HelionCosSinRoPE`  ·  implements/extends CosSinRoPE
- def: [`torchtitan/overrides/helion_rope.py:972`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L972) — documented in [config-overrides](../../../concepts/config-overrides.md)
- doc: Cos/sin RoPE that applies the rotation with a fused Helion kernel.
- signature: `class HelionCosSinRoPE(CosSinRoPE):`
- members:
  - <a id="HelionCosSinRoPE.forward"></a>`forward(self, query: torch.Tensor, key: torch.Tensor | None = None, positions: torch.Tensor | None = None, *, inverse: bool = False)` — [`L985`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L985) — documented in [config-overrides](../../../concepts/config-overrides.md)
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../models/common/rope.md#CosSinRoPE), [`_apply_helion_cossin_rope`](helion_rope.md#_apply_helion_cossin_rope), [`forward`](../models/common/rope.md#RoPE.forward), [`cache`](../models/common/rope.md#RoPE.cache)
- used by: [`CosSinRoPE`](../models/common/rope.md#CosSinRoPE), [`helion_cos_sin_rope`](helion_rope.md#helion_cos_sin_rope), [`forward`](../models/common/rope.md#RoPE.forward), [`HelionRoPE`](helion_rope.md#HelionRoPE)

### <a id="HelionCosSinRoPE.Config"></a>`HelionCosSinRoPE.Config`  ·  implements/extends Config
- def: [`torchtitan/overrides/helion_rope.py:982`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L982)
- signature: `class Config(CosSinRoPE.Config):`
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../models/common/rope.md#CosSinRoPE), [`Config`](../models/common/rope.md#CosSinRoPE.Config)
- used by: [`helion_cos_sin_rope`](helion_rope.md#helion_cos_sin_rope)

## Functions
- <a id="_apply_helion_complex_rope"></a>`_apply_helion_complex_rope(query: torch.Tensor, key: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor | None)` — [`L887`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L887) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_apply_helion_cossin_rope"></a>`_apply_helion_cossin_rope(query: torch.Tensor, key: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor | None)` — [`L818`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L818) — Run the fused kernel, or return ``None`` if the inputs are unsupported. — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_complex_bwd_config"></a>`_complex_bwd_config(grad_query: torch.Tensor)` — [`L458`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L458)
- <a id="_complex_eligible"></a>`_complex_eligible(xq: torch.Tensor, xk: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L774`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L774)
- <a id="_complex_fwd_backward"></a>`_complex_fwd_backward(ctx, grad_xq_out, grad_xk_out)` — [`L688`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L688)
- <a id="_complex_fwd_config"></a>`_complex_fwd_config(query: torch.Tensor)` — [`L416`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L416)
- <a id="_complex_fwd_setup_context"></a>`_complex_fwd_setup_context(ctx, inputs, output)` — [`L682`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L682)
- <a id="_config"></a>`_config(block_sizes: tuple[int, ...], num_warps: int, num_stages: int | None = None, *, l2_groupings: tuple[int, ...] | None = None, load_eviction_policies: tuple[str, ...] | None = None, pid_type: str | None = None)` — [`L334`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L334) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_cossin_bwd_config"></a>`_cossin_bwd_config(grad_query: torch.Tensor)` — [`L393`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L393)
- <a id="_cossin_eligible"></a>`_cossin_eligible(xq: torch.Tensor, xk: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor)` — [`L736`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L736)
- <a id="_cossin_fwd_backward"></a>`_cossin_fwd_backward(ctx, grad_xq_out, grad_xk_out)` — [`L596`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L596)
- <a id="_cossin_fwd_config"></a>`_cossin_fwd_config(query: torch.Tensor)` — [`L360`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L360)
- <a id="_cossin_fwd_setup_context"></a>`_cossin_fwd_setup_context(ctx, inputs, output)` — [`L590`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L590)
- <a id="_from_local"></a>`_from_local(local: torch.Tensor, spec: torch.Tensor)` — [`L716`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L716)
- <a id="_helion_complex_rope_bwd"></a>`_helion_complex_rope_bwd(grad_xq_out: torch.Tensor, grad_xk_out: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L654`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L654)
- <a id="_helion_complex_rope_bwd_fake"></a>`_helion_complex_rope_bwd_fake(grad_xq_out: torch.Tensor, grad_xk_out: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L663`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L663)
- <a id="_helion_complex_rope_fwd"></a>`_helion_complex_rope_fwd(xq: torch.Tensor, xk: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L624`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L624) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_helion_complex_rope_fwd_fake"></a>`_helion_complex_rope_fwd_fake(xq: torch.Tensor, xk: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L640`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L640)
- <a id="_helion_complex_rope_fwd_thk"></a>`_helion_complex_rope_fwd_thk(xq, xk, cache, pos)` — [`L812`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L812)
- <a id="_helion_cossin_rope_bwd"></a>`_helion_cossin_rope_bwd(grad_xq_out: torch.Tensor, grad_xk_out: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor)` — [`L550`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L550) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_helion_cossin_rope_bwd_fake"></a>`_helion_cossin_rope_bwd_fake(grad_xq_out: torch.Tensor, grad_xk_out: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor)` — [`L570`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L570)
- <a id="_helion_cossin_rope_fwd"></a>`_helion_cossin_rope_fwd(xq: torch.Tensor, xk: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor)` — [`L520`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L520) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_helion_cossin_rope_fwd_fake"></a>`_helion_cossin_rope_fwd_fake(xq: torch.Tensor, xk: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor)` — [`L536`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L536)
- <a id="_helion_cossin_rope_fwd_thk"></a>`_helion_cossin_rope_fwd_thk(xq, xk, cache, pos)` — [`L806`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L806)
- <a id="_resolve_positions"></a>`_resolve_positions(positions: torch.Tensor | None, query_local: torch.Tensor)` — [`L724`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L724)
- <a id="_rope_complex_bwd"></a>`_rope_complex_bwd(grad_xq_out: torch.Tensor, grad_xk_out: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L277`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L277)
- <a id="_rope_complex_fwd"></a>`_rope_complex_fwd(xq: torch.Tensor, xk: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L222`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L222)
- <a id="_rope_cos_sin_bwd"></a>`_rope_cos_sin_bwd(grad_xq_out: torch.Tensor, grad_xk_out: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor)` — [`L149`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L149)
- <a id="_rope_cos_sin_fwd"></a>`_rope_cos_sin_fwd(xq: torch.Tensor, xk: torch.Tensor, rope_cache: torch.Tensor, positions: torch.Tensor)` — [`L79`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L79)
- <a id="_run_complex_bwd"></a>`_run_complex_bwd(grad_xq_out: torch.Tensor, grad_xk_out: torch.Tensor, rope_cache_real: torch.Tensor, positions: torch.Tensor)` — [`L498`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L498)
- <a id="_run_tuned"></a>`_run_tuned(kernel: Any, config: helion.Config, *args: torch.Tensor)` — [`L480`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L480)
- <a id="_to_local"></a>`_to_local(tensor: torch.Tensor)` — [`L712`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L712) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="helion_complex_rope"></a>`helion_complex_rope(cfg: ComplexRoPE.Config)` — [`L1055`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L1055) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="helion_cos_sin_rope"></a>`helion_cos_sin_rope(cfg: CosSinRoPE.Config)` — [`L1041`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L1041) — documented in [config-overrides](../../../concepts/config-overrides.md)

## Module values
- <a id="HelionRoPE"></a>`HelionRoPE` — [`L1003`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L1003)
- <a id="_BOUND_KERNELS"></a>`_BOUND_KERNELS` — [`L478`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L478)
- <a id="_DEFAULT_CONFIG"></a>`_DEFAULT_CONFIG` — [`L76`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L76)
- <a id="_HELION_IMPORT_ERROR"></a>`_HELION_IMPORT_ERROR` — [`L59`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L59)
- <a id="__all__"></a>`__all__` — [`L69`](../../../../../../raw/code/torchtitan/torchtitan/overrides/helion_rope.py#L69)

