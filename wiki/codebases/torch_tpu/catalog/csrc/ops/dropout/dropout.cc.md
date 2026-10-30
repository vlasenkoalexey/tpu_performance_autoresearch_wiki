---
title: 'Module: csrc/ops/dropout/dropout.cc'
type: catalog
provenance: extracted
module: csrc/ops/dropout/dropout.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildDropoutBackwardShlo: BuildDropoutBackwardShlo(d0b2638901a3a9d0).
  BuildDropoutTrainShlo: BuildDropoutTrainShlo(d0b2638901a3a9d0).
---
# Module: [`csrc/ops/dropout/dropout.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout.cc)

## Functions
- <a id="BuildDropoutBackwardShlo"></a>`BuildDropoutBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp mask, double scale)` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout.cc#L78) — Builds the SHLO for dropout backward.
- `BuildDropoutBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp mask, double scale)` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout.cc#L78) — Builds the SHLO for dropout backward.
- <a id="BuildDropoutTrainShlo"></a>`BuildDropoutTrainShlo(mlir::MlirOp rng_input_state, mlir::MlirOp input, double p)` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout.cc#L35) — Builds the SHLO for dropout in the train mode. When train=False, dropout is
- `BuildDropoutTrainShlo(mlir::MlirOp rng_input_state, mlir::MlirOp input, double p)` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout.cc#L35) — Builds the SHLO for dropout in the train mode. When train=False, dropout is

