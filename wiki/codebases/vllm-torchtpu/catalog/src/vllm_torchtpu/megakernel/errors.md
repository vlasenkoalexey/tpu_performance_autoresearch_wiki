---
title: 'Module: src/vllm_torchtpu/megakernel/errors.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/errors.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.errors`/
symbols:
  MegakernelConfigError: MegakernelConfigError#
  MegakernelLayoutError: MegakernelLayoutError#
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/errors.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/errors.py)

## Classes
### <a id="MegakernelConfigError"></a>`MegakernelConfigError`  ·  implements/extends RuntimeError
- def: [`src/vllm_torchtpu/megakernel/errors.py:19`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/errors.py#L19) — documented in [megakernel-pool](../../../../concepts/megakernel-pool.md)
- doc: A requested configuration cannot be satisfied (e.g. a scratch budget overflow);
- signature: `class MegakernelConfigError(RuntimeError):`
- used by: [`plan`](planner.md#plan), [`scatter_pool_states`](pool/scatter.md#scatter_pool_states), [`derive_pool_layout`](pool/derive.md#derive_pool_layout), [`make_pool_backend`](pool/backend.md#make_pool_backend), [`_discover_schedule`](planner.md#_discover_schedule), [`extra_inputs`](planner.md#extra_inputs), [`_need`](pool/layout.md#PoolLayout._need), [`chip_budget`](profiles/default.md#chip_budget), [`k_tile`](planner.md#k_tile)

### <a id="MegakernelLayoutError"></a>`MegakernelLayoutError`  ·  implements/extends ValueError
- def: [`src/vllm_torchtpu/megakernel/errors.py:25`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/errors.py#L25)
- doc: An externally provided cache layout is incompatible; callers may fall back to
- signature: `class MegakernelLayoutError(ValueError):`

## Module values
- <a id="__all__"></a>`__all__` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/errors.py#L31)

