---
title: 'Module: torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.transformers_modeling_backend._meta_init`/
symbols:
  params_meta_buffers_real: params_meta_buffers_real().
  params_meta_buffers_real.register_parameter: params_meta_buffers_real().register_parameter().
  to_empty_keep_buffers: to_empty_keep_buffers().
---
# Module: [`torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.py)

## Functions
- <a id="params_meta_buffers_real"></a>`params_meta_buffers_real(build_device: str = "cpu")` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.py#L37) — Build a model with parameters on meta and buffers really computed.
- <a id="params_meta_buffers_real.register_parameter"></a>`register_parameter(module, name, param)` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.py#L41)
- <a id="to_empty_keep_buffers"></a>`to_empty_keep_buffers(model: nn.Module, device)` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.py#L58) — `to_empty()` for parameters; a plain move for buffers.

