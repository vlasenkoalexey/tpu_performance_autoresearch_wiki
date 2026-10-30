---
title: 'Module: csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenThnnFusedGruCellBackward: AtenThnnFusedGruCellBackward(5dbeaad3773d797f).
  AtenThnnFusedGruCellOut: AtenThnnFusedGruCellOut(6556a01d327fa99e).
  AtenThnnFusedGruCell: AtenThnnFusedGruCell(8e98e184e6ce1c21).
  ValidateThnnFusedGruCellInputs: '`$anonymous_namespace_csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`/ValidateThnnFusedGruCellInputs(6ddad2e2cbb424ad).'
  DispatchThnnFusedGruCellCommon: '`$anonymous_namespace_csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`/DispatchThnnFusedGruCellCommon(750987aed848f48).'
  BuildGruCellBackwardShlo: '`$anonymous_namespace_csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`/BuildGruCellBackwardShlo(ab6692c5f786a74b).'
  ThnnFusedGruCellOutImpl: '`$anonymous_namespace_csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`/ThnnFusedGruCellOutImpl(9912cf7727008149).'
  BuildGruCellShlo: '`$anonymous_namespace_csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`/BuildGruCellShlo(7fd68d467134d08a).'
  ThnnFusedGruCellImpl: '`$anonymous_namespace_csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`/ThnnFusedGruCellImpl(a3e6b461d68e2c96).'
  BuildTanhForRnnCell: '`$anonymous_namespace_csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`/BuildTanhForRnnCell(caa1d79285ea674e).'
  BuildSigmoidForRnnCell: '`$anonymous_namespace_csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`/BuildSigmoidForRnnCell(caa1d79285ea674e).'
---
# Module: [`csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc)

## Functions
- <a id="AtenThnnFusedGruCell"></a>`AtenThnnFusedGruCell(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& hx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias)` — [`L371`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L371) — Fused GRU cell, matching aten::_thnn_fused_gru_cell (the op stock nn.GRU
- <a id="AtenThnnFusedGruCellBackward"></a>`AtenThnnFusedGruCellBackward(const at::Tensor& grad_hy, const at::Tensor& workspace, bool has_bias)` — [`L402`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L402) — Backward of the fused GRU cell (aten::_thnn_fused_gru_cell_backward).
- <a id="AtenThnnFusedGruCellOut"></a>`AtenThnnFusedGruCellOut(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& hx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, at::Tensor& out0, at::Tensor& out1)` — [`L386`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L386)
- <a id="BuildGruCellBackwardShlo"></a>`BuildGruCellBackwardShlo(mlir::MlirOp grad_hy, mlir::MlirOp workspace, int64_t batch, int64_t hidden, mlir::ElementType out_dtype)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L179) — Backward. workspace = concat(r, z, n, hx, h_n). Returns
- <a id="BuildGruCellShlo"></a>`BuildGruCellShlo(mlir::MlirOp ig, mlir::MlirOp hg, mlir::MlirOp hx, int64_t batch, int64_t hidden, mlir::ElementType out_dtype, std::optional<mlir::MlirOp> ib_b = std::nullopt, std::optional<mlir::MlirOp> hb_b = std::nullopt)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L97)
- <a id="BuildSigmoidForRnnCell"></a>`BuildSigmoidForRnnCell(mlir::MlirOp x, mlir::ElementType acc_dtype)` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L68) — Builds forward GRU cell recurrence in StableHLO from input/hidden gate
- <a id="BuildTanhForRnnCell"></a>`BuildTanhForRnnCell(mlir::MlirOp x, mlir::ElementType acc_dtype)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L80)
- <a id="DispatchThnnFusedGruCellCommon"></a>`DispatchThnnFusedGruCellCommon(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& hx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, OpParamCacheKeys param_keys, Dispatch5&& dispatch5, Dispatch3&& dispatch3)` — [`L251`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L251)
- <a id="ThnnFusedGruCellImpl"></a>`ThnnFusedGruCellImpl(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& hx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, OpParamCacheKeys param_keys)` — [`L327`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L327)
- `ThnnFusedGruCellImpl(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& hx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, OpParamCacheKeys param_keys)` — [`L327`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L327)
- <a id="ThnnFusedGruCellOutImpl"></a>`ThnnFusedGruCellOutImpl(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& hx, const std::optional<at::Tensor>& input_bias, const std::optional<at::Tensor>& hidden_bias, OpParamCacheKeys param_keys, at::Tensor& out0, at::Tensor& out1)` — [`L345`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L345)
- <a id="ValidateThnnFusedGruCellInputs"></a>`ValidateThnnFusedGruCellInputs(const at::Tensor& input_gates, const at::Tensor& hidden_gates, const at::Tensor& hx)` — [`L230`](../../../../../../../raw/code/torch_tpu/csrc/ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc#L230)

