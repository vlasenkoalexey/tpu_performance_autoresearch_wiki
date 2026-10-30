---
title: 'Module: csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenThnnFusedLstmCellBackwardImpl: AtenThnnFusedLstmCellBackwardImpl(9f3e69ebc5aa71c1).
  AtenThnnFusedLstmCellOut: AtenThnnFusedLstmCellOut(15ef3adf77df8576).
  AtenThnnFusedLstmCell: AtenThnnFusedLstmCell(543bd810bb033040).
  ValidateThnnFusedLstmCellInputs: '`$anonymous_namespace_csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`/ValidateThnnFusedLstmCellInputs(6ddad2e2cbb424ad).'
  DispatchThnnFusedLstmCellCommon: '`$anonymous_namespace_csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`/DispatchThnnFusedLstmCellCommon(750987aed848f48).'
  BuildLstmCellBackwardShlo: '`$anonymous_namespace_csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`/BuildLstmCellBackwardShlo(e8b45523cebc1d3).'
  ThnnFusedLstmCellOutImpl: '`$anonymous_namespace_csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`/ThnnFusedLstmCellOutImpl(75f21e870dfa7298).'
  LstmCellFromGates: '`$anonymous_namespace_csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`/LstmCellFromGates(ab6692c5f786a74b).'
  ThnnFusedLstmCellImpl: '`$anonymous_namespace_csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`/ThnnFusedLstmCellImpl(a3e6b461d68e2c96).'
  BuildTanhForRnnCell: '`$anonymous_namespace_csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`/BuildTanhForRnnCell(caa1d79285ea674e).'
  BuildSigmoidForRnnCell: '`$anonymous_namespace_csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`/BuildSigmoidForRnnCell(caa1d79285ea674e).'
---
# Module: [`csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc)

## Functions
- <a id="AtenThnnFusedLstmCell"></a>`AtenThnnFusedLstmCell(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& cx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias)` — [`L350`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L350) — Fused LSTM cell, matching aten::_thnn_fused_lstm_cell (the op that stock
- <a id="AtenThnnFusedLstmCellBackwardImpl"></a>`AtenThnnFusedLstmCellBackwardImpl(const std::optional<at::Tensor>& grad_hy, const std::optional<at::Tensor>& grad_cy, const at::Tensor& cx, const at::Tensor& cy, const at::Tensor& workspace, bool has_bias)` — [`L383`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L383) — Backward of the fused LSTM cell (aten::_thnn_fused_lstm_cell_backward_impl).
- <a id="AtenThnnFusedLstmCellOut"></a>`AtenThnnFusedLstmCellOut(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& cx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, at::Tensor& out0, at::Tensor& out1, at::Tensor& out2)` — [`L366`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L366)
- <a id="BuildLstmCellBackwardShlo"></a>`BuildLstmCellBackwardShlo(mlir::MlirOp grad_hy, mlir::MlirOp grad_cy, mlir::MlirOp cx, mlir::MlirOp cy, mlir::MlirOp workspace, int64_t batch, int64_t hidden, mlir::ElementType out_dtype)` — [`L154`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L154) — Backward of the fused LSTM cell. `workspace` holds the activated gates
- <a id="BuildSigmoidForRnnCell"></a>`BuildSigmoidForRnnCell(mlir::MlirOp x, mlir::ElementType acc_dtype)` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L71) — Builds forward LSTM cell recurrence in StableHLO from pre-activation gates
- <a id="BuildTanhForRnnCell"></a>`BuildTanhForRnnCell(mlir::MlirOp x, mlir::ElementType acc_dtype)` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L83)
- <a id="DispatchThnnFusedLstmCellCommon"></a>`DispatchThnnFusedLstmCellCommon(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& cx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, OpParamCacheKeys param_keys, Dispatch5&& dispatch5, Dispatch3&& dispatch3)` — [`L224`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L224)
- <a id="LstmCellFromGates"></a>`LstmCellFromGates(mlir::MlirOp gates, mlir::MlirOp cx, int64_t batch, int64_t hidden, mlir::ElementType out_dtype)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L100)
- <a id="ThnnFusedLstmCellImpl"></a>`ThnnFusedLstmCellImpl(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& cx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, OpParamCacheKeys param_keys)` — [`L304`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L304)
- `ThnnFusedLstmCellImpl(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& cx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, OpParamCacheKeys param_keys)` — [`L304`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L304)
- <a id="ThnnFusedLstmCellOutImpl"></a>`ThnnFusedLstmCellOutImpl(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& cx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, OpParamCacheKeys param_keys, at::Tensor& out0, at::Tensor& out1, at::Tensor& out2)` — [`L322`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L322)
- <a id="ValidateThnnFusedLstmCellInputs"></a>`ValidateThnnFusedLstmCellInputs(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& cx)` — [`L203`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc#L203)

