---
title: 'Module: torchtitan/experiments/tpu/kernels/fp8_scale.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/fp8_scale.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.fp8_scale`/
symbols:
  scale_from_amax: scale_from_amax().
  MIN_SCALE: MIN_SCALE.
---
# Module: [`torchtitan/experiments/tpu/kernels/fp8_scale.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_scale.py)

## Functions
- <a id="scale_from_amax"></a>`scale_from_amax(amax: jax.Array, qdtype: jnp.dtype)` — [`L13`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_scale.py#L13) — FP32 absmax scale ``amax / fmax``, floored at the smallest normal FP32.

## Module values
- <a id="MIN_SCALE"></a>`MIN_SCALE` — [`L10`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/fp8_scale.py#L10)

