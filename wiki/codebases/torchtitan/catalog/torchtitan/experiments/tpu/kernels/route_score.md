---
title: 'Module: torchtitan/experiments/tpu/kernels/route_score.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/route_score.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.route_score`/
symbols:
  route_score_grad: route_score_grad().
  _route_score_grad_tpu: _route_score_grad_tpu().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/kernels/route_score.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/route_score.py)

## Functions
- <a id="_route_score_grad_tpu"></a>`_route_score_grad_tpu(grad_output_ND: jax.Array, routed_output_ND: jax.Array)` — [`L16`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/route_score.py#L16)
- <a id="route_score_grad"></a>`route_score_grad(grad_output_ND: torch.Tensor, routed_output_ND: torch.Tensor)` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/route_score.py#L27) — Return FP32 dScore[N] without exposing an FP32 [N, D] tensor.

## Module values
- <a id="__all__"></a>`__all__` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/route_score.py#L61)

