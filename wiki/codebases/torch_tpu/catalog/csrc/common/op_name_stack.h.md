---
title: 'Module: csrc/common/op_name_stack.h'
type: catalog
provenance: extracted
module: csrc/common/op_name_stack.h
status: fresh
symbol_base: cxx . . $ torch_tpu/internal/
symbols:
  ScopedOpName.ScopedOpName: ScopedOpName#ScopedOpName(eed00ffa8ace304f).
  ScopedOpName: ScopedOpName#
  OpNameStack: OpNameStack#
  ScopedOpName.-ScopedOpName: ScopedOpName#`~ScopedOpName`(ced63f7c635d850d).
  ScopedOpName.operator: ScopedOpName#`operator=`(c0a21fcd35a413ed).
---
# Module: [`csrc/common/op_name_stack.h`](../../../../../../raw/code/torch_tpu/csrc/common/op_name_stack.h)

## Classes
### <a id="OpNameStack"></a>`OpNameStack`
- def: [`csrc/common/op_name_stack.h:29`](../../../../../../raw/code/torch_tpu/csrc/common/op_name_stack.h#L29) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- doc: OpNameStack maintains a thread-local stack of OpName enums.
- signature: `class OpNameStack`
- uses (calls/refs, reference-scoped): [`OpName`](../ops/op_names.h.md#OpName), [`Push`](op_name_stack.cc.md#OpNameStack.Push), [`MaybeTop`](op_name_stack.cc.md#OpNameStack.MaybeTop), [`Top`](op_name_stack.cc.md#OpNameStack.Top), [`Pop`](op_name_stack.cc.md#OpNameStack.Pop)
- used by: [`ScopedOpName`](op_name_stack.h.md#ScopedOpName.ScopedOpName), [`Push`](op_name_stack.cc.md#OpNameStack.Push), [`DispatchOp`](../eager/op_dispatcher.h.md#DispatchOp), [`stack_`](op_name_stack.cc.md#OpNameStack.stack_), [`Top`](op_name_stack.cc.md#OpNameStack.Top), [`TestBody`](op_name_stack_test.cc.md#OpNameStackTest_NestedScopedOpNamesBehaveAsStack_Test.TestBody), [`TestBody`](op_name_stack_test.cc.md#OpNameStackTest_ScopedOpNamePushesAndPops_Test.TestBody), [`IsCurrentOpInPlace`](../ops/foreach_aten_kernels.cc.md#IsCurrentOpInPlace), [`Pop`](op_name_stack.cc.md#OpNameStack.Pop), [`TestBody`](op_name_stack_test.cc.md#OpNameStackTest_EmptyStackReturnsNullopt_Test.TestBody), [`~ScopedOpName`](op_name_stack.h.md#ScopedOpName.-ScopedOpName)

### <a id="ScopedOpName"></a>`ScopedOpName`
- def: [`csrc/common/op_name_stack.h:54`](../../../../../../raw/code/torch_tpu/csrc/common/op_name_stack.h#L54) — documented in [dynamic-shape-ops](../../../concepts/dynamic-shape-ops.md)
- doc: ScopedOpName is an RAII guard that pushes an OpName onto the thread-local
- signature: `class ScopedOpName`
- members:
  - `ScopedOpName(const ScopedOpName&)` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/common/op_name_stack.h#L59)
  - <a id="ScopedOpName.ScopedOpName"></a>`ScopedOpName(OpName op_name)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/op_name_stack.h#L56) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
  - <a id="ScopedOpName.operator"></a>`operator=(const ScopedOpName&)` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/common/op_name_stack.h#L60)
  - <a id="ScopedOpName.-ScopedOpName"></a>`~ScopedOpName()` — [`L57`](../../../../../../raw/code/torch_tpu/csrc/common/op_name_stack.h#L57)
- uses (calls/refs, reference-scoped): [`OpName`](../ops/op_names.h.md#OpName), [`Push`](op_name_stack.cc.md#OpNameStack.Push), [`OpNameStack`](op_name_stack.h.md#OpNameStack), [`Pop`](op_name_stack.cc.md#OpNameStack.Pop)
- used by: [`alltoall`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`AtenPreluKernelBackward`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`AtenMaskedScatter_`](../ops/masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`AtenWeightNormInterface`](../ops/weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`AtenChannelShuffle`](../ops/channel_shuffle/channel_shuffle_aten_kernels.cc.md#AtenChannelShuffle), [`AtenIndexTensorOut`](../ops/index/index_aten_kernels.cc.md#AtenIndexTensorOut), [`allgather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`AtenCtcLossTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenVarMeanCorrection`](../ops/reductions/var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenDigammaOut`](../ops/digamma/digamma_aten_kernels.cc.md#AtenDigammaOut), [`_allgather_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AtenBinCount`](../ops/bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`AtenCtcLossBackwardTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`allreduce`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allreduce), [`AtenLinalgLuSolveOut`](../ops/linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuSolveOut), [`AtenFusedRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNorm), [`AtenArangeStartOut`](../ops/arange/arange_aten_kernels.cc.md#AtenArangeStartOut), [`AtenFusedRmsNormBackward`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNormBackward), [`AtenLinalgSolveExOut`](../ops/linalg/linalg_kernels.cc.md#AtenLinalgSolveExOut), [`AtenReplicationPad3dBackward`](../ops/replication_pad/replication_pad_aten_kernels.cc.md#AtenReplicationPad3dBackward), [`gather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`AtenLinalgSvdU`](../ops/linalg/linalg_svd_kernels.cc.md#AtenLinalgSvdU), [`AtenSegmentReduce`](../ops/segment_reduce/segment_reduce_aten_kernels.cc.md#AtenSegmentReduce), [`_reduce_scatter_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base), [`AtenLinalgInvExInverse`](../ops/linalg/linalg_kernels.cc.md#AtenLinalgInvExInverse), [`AtenAdaptiveAvgPool3dOut`](../ops/pooling/adaptive_avg_pool_aten_kernels.cc.md#AtenAdaptiveAvgPool3dOut), [`AtenGridSampler3dBackward`](../ops/grid_sampler/grid_sampler_aten_kernels.cc.md#AtenGridSampler3dBackward), [`AtenNativeGroupNormBackward`](../ops/group_norm/group_norm_aten_kernels.cc.md#AtenNativeGroupNormBackward), [`AtenViewAsComplex`](../ops/view/view_aten_kernels.cc.md#AtenViewAsComplex), [`AtenCdistBackward`](../ops/distance/dist_aten_kernels.cc.md#AtenCdistBackward), [`AtenCdistForward`](../ops/distance/dist_aten_kernels.cc.md#AtenCdistForward), [`AtenExponential_`](../ops/exponential/exponential_aten_kernels.cc.md#AtenExponential_), [`AtenLinalgLuFactorExOut`](../ops/linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuFactorExOut), [`AtenLinspaceOut`](../ops/linspace/linspace_aten_kernels.cc.md#AtenLinspaceOut), [`AtenReflectionPad2dBackward`](../ops/reflection_pad/reflection_pad_aten_kernels.cc.md#AtenReflectionPad2dBackward), [`AtenReplicationPad2dBackward`](../ops/replication_pad/replication_pad_aten_kernels.cc.md#AtenReplicationPad2dBackward), [`AtenSelectScatterOut`](../ops/select_scatter/select_scatter_aten_kernels.cc.md#AtenSelectScatterOut), [`AtenSliceScatterOut`](../ops/slice_scatter/slice_scatter_aten_kernels.cc.md#AtenSliceScatterOut)  (+729 more)

