---
title: 'Module: torchtitan/models/kimi_k3/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k3/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k3.sharding`/
symbols:
  _set_inner_kda_sharding: _set_inner_kda_sharding().
  set_kimi_k3_sharding_config: set_kimi_k3_sharding_config().
  _set_vision_buffer_sharding: _set_vision_buffer_sharding().
  DP: DP.
---
# Module: [`torchtitan/models/kimi_k3/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/sharding.py)

## Functions
- <a id="_set_inner_kda_sharding"></a>`_set_inner_kda_sharding(inner_kda: Module.Config)` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/sharding.py#L32) — Set the local boundary around Attention Gym's KDA kernels. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="_set_vision_buffer_sharding"></a>`_set_vision_buffer_sharding(config: KimiK3VisionEncoder.Config)` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/sharding.py#L115) — Declare the K3 rotary buffer replicated across DP ranks. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- <a id="set_kimi_k3_sharding_config"></a>`set_kimi_k3_sharding_config(config: KimiK3Model.Config, *, enable_ep: bool, enable_sp: bool = False)` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/sharding.py#L84) — Declare Kimi K3 vision-buffer and expert sharding. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)

## Module values
- <a id="DP"></a>`DP` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/sharding.py#L29)

