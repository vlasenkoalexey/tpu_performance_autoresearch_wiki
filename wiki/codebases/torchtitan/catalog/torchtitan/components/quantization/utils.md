---
title: 'Module: torchtitan/components/quantization/utils.py'
type: catalog
provenance: extracted
module: torchtitan/components/quantization/utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.quantization.utils`/
symbols:
  swap_token_dispatcher: swap_token_dispatcher().
  has_quantization: has_quantization().
  module_filter_fn: module_filter_fn().
---
# Module: [`torchtitan/components/quantization/utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/utils.py)

## Functions
- <a id="has_quantization"></a>`has_quantization(model_config)` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/utils.py#L67) — Check if any module in the model config has quantization applied. — documented in [quantization](../../../../concepts/quantization.md)
- <a id="module_filter_fn"></a>`module_filter_fn(config: Linear.Config, fqn: str, filter_fqns: list[str])` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/utils.py#L16) — Filter function to determine which Linear.Config should be converted. — documented in [quantization](../../../../concepts/quantization.md)
- <a id="swap_token_dispatcher"></a>`swap_token_dispatcher(routed_experts_config, pad_multiple: int)` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/utils.py#L33) — Swap the routed-experts token dispatcher config to support padded grouped GEMMs. — documented in [quantization](../../../../concepts/quantization.md)

