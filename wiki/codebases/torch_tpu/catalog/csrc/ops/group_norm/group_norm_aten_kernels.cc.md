---
title: 'Module: csrc/ops/group_norm/group_norm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/group_norm/group_norm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNativeGroupNormBackward: AtenNativeGroupNormBackward(71bd4bc7a732b7e4).
  BuildGroupNormBackwardShlo: '`$anonymous_namespace_csrc/ops/group_norm/group_norm_aten_kernels.cc`/BuildGroupNormBackwardShlo(47727a6e30731dd8).'
  GroupNormBackwardShloResults: GroupNormBackwardShloResults#
  GroupNormBackwardShloResults.grad_input: GroupNormBackwardShloResults#grad_input.
  GroupNormBackwardShloResults.grad_weight: GroupNormBackwardShloResults#grad_weight.
  GroupNormBackwardShloResults.grad_bias: GroupNormBackwardShloResults#grad_bias.
---
# Module: [`csrc/ops/group_norm/group_norm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/group_norm/group_norm_aten_kernels.cc)

## Classes
### <a id="GroupNormBackwardShloResults"></a>`GroupNormBackwardShloResults`
- def: [`csrc/ops/group_norm/group_norm_aten_kernels.cc:53`](../../../../../../../raw/code/torch_tpu/csrc/ops/group_norm/group_norm_aten_kernels.cc#L53)
- signature: `struct GroupNormBackwardShloResults`
- members:
  - <a id="GroupNormBackwardShloResults.grad_bias"></a>`grad_bias` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/group_norm/group_norm_aten_kernels.cc#L56)
  - <a id="GroupNormBackwardShloResults.grad_input"></a>`grad_input` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/group_norm/group_norm_aten_kernels.cc#L54)
  - <a id="GroupNormBackwardShloResults.grad_weight"></a>`grad_weight` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/group_norm/group_norm_aten_kernels.cc#L55)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenNativeGroupNormBackward`](group_norm_aten_kernels.cc.md#AtenNativeGroupNormBackward), [`BuildGroupNormBackwardShlo`](group_norm_aten_kernels.cc.md#BuildGroupNormBackwardShlo)

## Functions
- <a id="AtenNativeGroupNormBackward"></a>`AtenNativeGroupNormBackward(const at::Tensor& grad_out, const at::Tensor& input, const at::Tensor& mean, const at::Tensor& rstd, const std::optional<at::Tensor>& weight, int64_t n, int64_t c, int64_t h_w, int64_t group, std::array<bool, 3> output_mask)` — [`L317`](../../../../../../../raw/code/torch_tpu/csrc/ops/group_norm/group_norm_aten_kernels.cc#L317)
- <a id="BuildGroupNormBackwardShlo"></a>`BuildGroupNormBackwardShlo(mlir::MlirOp grad_output_op, mlir::MlirOp input_op, mlir::MlirOp mean_op, mlir::MlirOp rstd_op, std::optional<mlir::MlirOp> weight_op, int64_t n, int64_t c, int64_t h_w, int64_t group, std::array<bool, 3> output_mask)` — [`L90`](../../../../../../../raw/code/torch_tpu/csrc/ops/group_norm/group_norm_aten_kernels.cc#L90) — Math pseudo code, referencing pytorch decomposition:

