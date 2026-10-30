---
title: 'Module: csrc/ops/lstm/lstm_common.h'
type: catalog
provenance: extracted
module: csrc/ops/lstm/lstm_common.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  LstmGateAdjoints.delta_c_prev: LstmGateAdjoints#delta_c_prev.
  SigmoidBackward: SigmoidBackward(58797ee5e7d65062).
  LstmGateAdjoints: LstmGateAdjoints#
  TanhBackward: TanhBackward(58797ee5e7d65062).
  LstmGateAdjoints.delta_pre_g: LstmGateAdjoints#delta_pre_g.
  LstmGateAdjoints.delta_pre_o: LstmGateAdjoints#delta_pre_o.
  LstmGateAdjoints.delta_pre_i: LstmGateAdjoints#delta_pre_i.
  LstmGateAdjoints.delta_pre_f: LstmGateAdjoints#delta_pre_f.
---
# Module: [`csrc/ops/lstm/lstm_common.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h)

## Classes
### <a id="LstmGateAdjoints"></a>`LstmGateAdjoints`
- def: [`csrc/ops/lstm/lstm_common.h:49`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h#L49)
- doc: Encapsulates the 4 pre-activation gate adjoints and the previous cell state
- signature: `struct LstmGateAdjoints`
- members:
  - <a id="LstmGateAdjoints.delta_c_prev"></a>`delta_c_prev` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h#L56) — Cell gradient propagating to previous timestep (d_cx)
  - <a id="LstmGateAdjoints.delta_pre_f"></a>`delta_pre_f` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h#L51) — Pre-activation forget gate gradient (d_f_pre)
  - <a id="LstmGateAdjoints.delta_pre_g"></a>`delta_pre_g` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h#L53) — Pre-activation cell/candidate gate gradient (d_g_pre)
  - <a id="LstmGateAdjoints.delta_pre_i"></a>`delta_pre_i` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h#L50) — Pre-activation input gate gradient (d_i_pre)
  - <a id="LstmGateAdjoints.delta_pre_o"></a>`delta_pre_o` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h#L54) — Pre-activation output gate gradient (d_o_pre)
- uses (calls/refs, reference-scoped): [`ComputeLstmGateAdjoints`](lstm_common.cc.md#ComputeLstmGateAdjoints)
- used by: [`BuildLstmCellBackwardShlo`](../thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc.md#BuildLstmCellBackwardShlo), [`ComputeBackwardStep`](lstm_aten_kernels.cc.md#ComputeBackwardStep)

## Functions
- <a id="SigmoidBackward"></a>`SigmoidBackward(mlir::MlirOp delta, mlir::MlirOp act, mlir::MlirOp one)` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h#L29) — Computes the gradient through a sigmoid activation using its analytic
- <a id="TanhBackward"></a>`TanhBackward(mlir::MlirOp delta, mlir::MlirOp act, mlir::MlirOp one)` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_common.h#L40) — Computes the gradient through a tanh activation using its analytic

