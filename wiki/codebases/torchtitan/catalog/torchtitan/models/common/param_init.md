---
title: 'Module: torchtitan/models/common/param_init.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/param_init.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.param_init`/
symbols:
  depth_scaled_std: depth_scaled_std().
  skip_param_init: skip_param_init().
---
# Module: [`torchtitan/models/common/param_init.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/param_init.py)

## Functions
- <a id="depth_scaled_std"></a>`depth_scaled_std(base_std: float, layer_id: int)` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/param_init.py#L28) — Compute depth-dependent std: base_std / sqrt(2 * (layer_id + 1)).
- <a id="skip_param_init"></a>`skip_param_init(param: nn.Parameter)` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/param_init.py#L20) — No-op initializer: explicitly skip initialization for a parameter.

