---
title: 'Module: csrc/ops/multinomial/multinomial.cc'
type: catalog
provenance: extracted
module: csrc/ops/multinomial/multinomial.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildMultinomialShlo: BuildMultinomialShlo(7d8e2ea2c4fb7faf).
  BuildGumbelNoise: '`$anonymous_namespace_csrc/ops/multinomial/multinomial.cc`/BuildGumbelNoise(9dd408ac7de815bd).'
---
# Module: [`csrc/ops/multinomial/multinomial.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial.cc)

## Functions
- <a id="BuildGumbelNoise"></a>`BuildGumbelNoise(mlir::MlirOp rng_input_state, mlir::MlirOp target_op)` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial.cc#L46) — Generates Gumbel noise matching `target_op`'s type and shape using the
- <a id="BuildMultinomialShlo"></a>`BuildMultinomialShlo(mlir::MlirOp input_op, mlir::MlirOp rng_input_state, int64_t num_samples, bool replacement)` — [`L75`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial.cc#L75) — This uses the Gumbel-Max trick to sample from the multinomial distribution.

