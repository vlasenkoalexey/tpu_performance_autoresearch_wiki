---
title: 'Module: csrc/eager/op_dispatcher.h'
type: catalog
provenance: extracted
module: csrc/eager/op_dispatcher.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DispatchOp: DispatchOp(857f31ba8de435af).
  DispatchOpOut: DispatchOpOut(70084a506739c21a).
  DispatchOpOptions: DispatchOpOptions#
  GetTensorSpan: internal/GetTensorSpan(7ca7c626f3953637).
  DeviceBufferRefArray: DeviceBufferRefArray#
  OpInputs: OpInputs#
  TensorHolder: TensorHolder#
  DispatchOpOptions.split_mode: DispatchOpOptions#split_mode.
  DispatchOpOptions.op_name: DispatchOpOptions#op_name.
  DispatchOpOptions.out_dtypes: DispatchOpOptions#out_dtypes.
  TensorGroupTraits: internal/TensorGroupTraits#
  DispatchOpOptions.donated_indices: DispatchOpOptions#donated_indices.
  OpDispatchFailure.failure_message: internal/OpDispatchFailure#failure_message.
  DeviceBufferRefArrayTraits: internal/DeviceBufferRefArrayTraits#
  OpOutputs: OpOutputs#
  DispatchOpOptions.op_param_cache_keys: DispatchOpOptions#op_param_cache_keys.
  DispatchOpOptions.computation_dtype: DispatchOpOptions#computation_dtype.
  DispatchOpOptions.out_dims_list: DispatchOpOptions#out_dims_list.
  TensorHolder.TensorHolder: TensorHolder#TensorHolder(45982de3b0bc1087).
  TensorGroupTraits.type: internal/TensorGroupTraits#type#
  OpInputsTraits: internal/OpInputsTraits#
  OpOutputsTraits: internal/OpOutputsTraits#
  DispatchOpOptions.device_assignment: DispatchOpOptions#device_assignment.
  OpDispatchFailure: internal/OpDispatchFailure#
  DispatchOpOptions.out_dtype: DispatchOpOptions#out_dtype.
  DispatchOpOptions.out_dims: DispatchOpOptions#out_dims.
  DeviceBufferRefArrayTraits.type: internal/DeviceBufferRefArrayTraits#type#
  OpDispatchFailure.op_base_name: internal/OpDispatchFailure#op_base_name.
---
# Module: [`csrc/eager/op_dispatcher.h`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h)

## Classes
### <a id="DeviceBufferRefArray"></a>`DeviceBufferRefArray`
- def: [`csrc/eager/op_dispatcher.h:215`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L215) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- doc: If kSize == kDynamicSize, the type is std::vector<DeviceBufferRef>;
- signature: `template <int kSize> using DeviceBufferRefArray = internal::DeviceBufferRefArrayTraits<kSize>::type`
- uses (calls/refs, reference-scoped): [`DeviceBufferRefArrayTraits`](op_dispatcher.h.md#DeviceBufferRefArrayTraits)
- used by: [`AtenLinalgSvdU`](../ops/linalg/linalg_svd_kernels.cc.md#AtenLinalgSvdU), [`AtenLstmInputForward`](../ops/lstm/lstm_aten_kernels.cc.md#AtenLstmInputForward), [`AtenGeqrf`](../ops/linalg/qr/linalg_qr_kernels.cc.md#AtenGeqrf), [`AtenThnnFusedGruCell`](../ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc.md#AtenThnnFusedGruCell), [`AtenThnnFusedLstmCell`](../ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc.md#AtenThnnFusedLstmCell), [`DispatchThnnFusedGruCellCommon`](../ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc.md#DispatchThnnFusedGruCellCommon), [`DispatchThnnFusedLstmCellCommon`](../ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc.md#DispatchThnnFusedLstmCellCommon), [`TpuBatchNormBackward`](../ops/native_batch_norm/native_batch_norm_aten_kernels.cc.md#TpuBatchNormBackward), [`Svd`](../ops/linalg/linalg_svd_kernels.cc.md#Svd), [`PrepareBatchNormDispatch`](../ops/native_batch_norm/native_batch_norm_aten_kernels.cc.md#PrepareBatchNormDispatch), [`DispatchGeqrf`](../ops/linalg/qr/linalg_qr_kernels.cc.md#DispatchGeqrf), [`UpcastComplexDoubleOutputs`](../ops/linalg/linalg_svd_kernels.cc.md#UpcastComplexDoubleOutputs), [`TpuBatchNormOut`](../ops/native_batch_norm/native_batch_norm_aten_kernels.cc.md#TpuBatchNormOut), [`TpuBatchNorm`](../ops/native_batch_norm/native_batch_norm_aten_kernels.cc.md#TpuBatchNorm), [`GetTensorSpan`](op_dispatcher.h.md#GetTensorSpan), [`Geqrf`](../ops/linalg/qr/linalg_qr_kernels.cc.md#Geqrf), [`GetPromotedTypeBackward`](../ops/convolution/convolution_aten_kernels.cc.md#GetPromotedTypeBackward), [`UpcastToDouble`](../ops/linalg/linalg_svd_kernels.cc.md#UpcastToDouble), [`ComputeBidirLayerBackward`](../ops/lstm/lstm_aten_kernels.cc.md#ComputeBidirLayerBackward), [`ThnnFusedGruCellImpl`](../ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc.md#ThnnFusedGruCellImpl), [`ThnnFusedLstmCellImpl`](../ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc.md#ThnnFusedLstmCellImpl)

### <a id="DeviceBufferRefArrayTraits"></a>`DeviceBufferRefArrayTraits`
- def: [`csrc/eager/op_dispatcher.h:164`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L164)
- doc: Traits for defining DeviceBufferRefArray.
- signature: `template <int kSize> struct DeviceBufferRefArrayTraits`
- uses (calls/refs, reference-scoped): [`kDynamicSize`](../ops/op_builder_utils.h.md#kDynamicSize)
- used by: [`DeviceBufferRefArray`](op_dispatcher.h.md#DeviceBufferRefArray)

### <a id="DeviceBufferRefArrayTraits.type"></a>`DeviceBufferRefArrayTraits.type`
- def: [`csrc/eager/op_dispatcher.h:166`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L166)
- signature: `using type = std::array<DeviceBufferRef, kSize>`
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef)

### <a id="DispatchOpOptions"></a>`DispatchOpOptions`
- def: [`csrc/eager/op_dispatcher.h:108`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L108) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- doc: The primary template is for the case where the number of outputs is known at
- signature: `template <int kNumOutputs> struct DispatchOpOptions`
- members:
  - <a id="DispatchOpOptions.computation_dtype"></a>`computation_dtype` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L121) — If specified, cast all op inputs to the given dtype before the provided
  - <a id="DispatchOpOptions.device_assignment"></a>`device_assignment` — [`L125`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L125) — INT_VEC_OK
  - <a id="DispatchOpOptions.donated_indices"></a>`donated_indices` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L124)
  - <a id="DispatchOpOptions.op_name"></a>`op_name` — [`L113`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L113) — The op name for dispatching. If omitted, use the op name from the active — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
  - <a id="DispatchOpOptions.op_param_cache_keys"></a>`op_param_cache_keys` — [`L122`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L122)
  - <a id="DispatchOpOptions.out_dims"></a>`out_dims` — [`L151`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L151)
  - <a id="DispatchOpOptions.out_dims_list"></a>`out_dims_list` — [`L116`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L116)
  - <a id="DispatchOpOptions.out_dtype"></a>`out_dtype` — [`L150`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L150)
  - <a id="DispatchOpOptions.out_dtypes"></a>`out_dtypes` — [`L114`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L114)
  - <a id="DispatchOpOptions.split_mode"></a>`split_mode` — [`L123`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L123)
- uses (calls/refs, reference-scoped): [`OpName`](../ops/op_names.h.md#OpName), [`OpParamCacheKeys`](../common/cache_key.h.md#OpParamCacheKeys), [`Indices`](../common/dimension_types.h.md#Indices), [`FixedSizeSpan`](../common/fixed_size_span.h.md#FixedSizeSpan), [`kDynamicSize`](../ops/op_builder_utils.h.md#kDynamicSize), [`OpSplitMode`](device_buffer.h.md#OpSplitMode), [`kNone`](device_buffer.h.md#OpSplitMode.kNone)
- used by: [`DispatchOp`](op_dispatcher.h.md#DispatchOp), [`LstmInputBackwardImpl`](../ops/lstm/lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`AtenCtcLossTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenCtcLossBackwardTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenAdaptiveAvgPool3dOut`](../ops/pooling/adaptive_avg_pool_aten_kernels.cc.md#AtenAdaptiveAvgPool3dOut), [`AtenForeachNormScalar`](../ops/foreach_aten_kernels.cc.md#AtenForeachNormScalar), [`AtenCrossEntropyLoss`](../ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#AtenCrossEntropyLoss), [`AtenMseLossBackward`](../ops/mse_loss/mse_loss_aten_kernels.cc.md#AtenMseLossBackward), [`AtenMseLossOut`](../ops/mse_loss/mse_loss_aten_kernels.cc.md#AtenMseLossOut), [`AtenSigmoidBackwardGradInput`](../ops/sigmoid/sigmoid_aten_kernels.cc.md#AtenSigmoidBackwardGradInput), [`CrossEntropyLossBackwardSelfKernel`](../ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#CrossEntropyLossBackwardSelfKernel), [`AtenSparseDenseMatmulGradientStack`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_gradient_stack_aten_kernels.cc.md#AtenSparseDenseMatmulGradientStack), [`AtenAdaptiveAvgPool3dBackwardGradInput`](../ops/pooling/adaptive_avg_pool_aten_kernels.cc.md#AtenAdaptiveAvgPool3dBackwardGradInput), [`AtenSparseDenseMatmulActivationUnstack`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.cc.md#AtenSparseDenseMatmulActivationUnstack), [`BuildGluBackwardOut`](../ops/glu/glu_aten_kernels.cc.md#BuildGluBackwardOut), [`SoftmaxBackwardDataInternalOut`](../ops/softmax/softmax_aten_kernels.cc.md#SoftmaxBackwardDataInternalOut), [`AtenPut_`](../ops/put/put_aten_kernels.cc.md#AtenPut_), [`GruInputBackwardImpl`](../ops/gru/gru_aten_kernels.cc.md#GruInputBackwardImpl), [`DispatchOpOut`](op_dispatcher.h.md#DispatchOpOut), [`PyCallCustomKernel`](../internal/pallas/pallas_py.cc.md#PyCallCustomKernel), [`CrossEntropyLossBackwardTargetKernel`](../ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#CrossEntropyLossBackwardTargetKernel), [`TorchTpuOptimizationBarrier`](../ops/optimization_barrier/optimization_barrier_kernels.cc.md#TorchTpuOptimizationBarrier), [`LstmInputForwardCachedImpl`](../ops/lstm/lstm_aten_kernels.cc.md#LstmInputForwardCachedImpl), [`DispatchBinaryCrossEntropyBackwardOut`](../ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc.md#DispatchBinaryCrossEntropyBackwardOut), [`DispatchBinaryCrossEntropyOut`](../ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc.md#DispatchBinaryCrossEntropyOut), [`GruInputImpl`](../ops/gru/gru_aten_kernels.cc.md#GruInputImpl), [`ForeachAddList`](../ops/foreach_aten_kernels.cc.md#ForeachAddList), [`DispatchAdamw`](../ops/fused_adamw/fused_adamw_aten_kernels.cc.md#DispatchAdamw), [`DispatchAdam`](../ops/fused_adam/fused_adam_aten_kernels.cc.md#DispatchAdam), [`DispatchHardtanh`](../ops/hardtanh/hardtanh_aten_kernels.cc.md#DispatchHardtanh), [`LogSigmoidBackward`](../ops/sigmoid/sigmoid_aten_kernels.cc.md#LogSigmoidBackward), [`ResolveNegativeIndices`](../ops/index_utils.cc.md#ResolveNegativeIndices), [`CtcLossForwardInternal`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#CtcLossForwardInternal), [`CtcLossPublicInternal`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#CtcLossPublicInternal), [`DispatchSgd`](../ops/fused_sgd/fused_sgd_aten_kernels.cc.md#DispatchSgd), [`CtcLossBackwardInternal`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#CtcLossBackwardInternal), [`BuildAvgPoolBackwardGradInputNd`](../ops/pooling/avg_pool_aten_kernels.cc.md#BuildAvgPoolBackwardGradInputNd), [`ForeachDiv`](../ops/foreach_aten_kernels.cc.md#ForeachDiv), [`DispatchThnnFusedGruCellCommon`](../ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc.md#DispatchThnnFusedGruCellCommon), [`DispatchThnnFusedLstmCellCommon`](../ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc.md#DispatchThnnFusedLstmCellCommon)  (+33 more)

### <a id="OpDispatchFailure"></a>`OpDispatchFailure`
- def: [`csrc/eager/op_dispatcher.h:221`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L221)
- doc: Information about an injected op dispatch failure. Used for internal testing
- signature: `struct OpDispatchFailure`
- members:
  - <a id="OpDispatchFailure.failure_message"></a>`failure_message` — [`L226`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L226) — The failure message of the injected op failure.
  - <a id="OpDispatchFailure.op_base_name"></a>`op_base_name` — [`L224`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L224) — The base name of the op that is forced to fail. If empty, no op is forced
- uses (calls/refs, reference-scoped): [`GetOpDispatchFailure`](op_dispatcher.cc.md#GetOpDispatchFailure), [`SetOpDispatchFailure`](op_dispatcher.cc.md#SetOpDispatchFailure)
- used by: [`DispatchOp`](op_dispatcher.h.md#DispatchOp), [`GetOpDispatchFailure`](op_dispatcher.cc.md#GetOpDispatchFailure)

### <a id="OpInputs"></a>`OpInputs`
- def: [`csrc/eager/op_dispatcher.h:262`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L262) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- signature: `template <int kArity> using OpInputs = internal::OpInputsTraits<kArity>::type`
- uses (calls/refs, reference-scoped): [`OpInputsTraits`](op_dispatcher.h.md#OpInputsTraits)
- used by: [`DispatchOp`](op_dispatcher.h.md#DispatchOp), [`DispatchOpOut`](op_dispatcher.h.md#DispatchOpOut), [`DispatchHardtanh`](../ops/hardtanh/hardtanh_aten_kernels.cc.md#DispatchHardtanh), [`DispatchThnnFusedGruCellCommon`](../ops/thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc.md#DispatchThnnFusedGruCellCommon), [`DispatchThnnFusedLstmCellCommon`](../ops/thnn_fused_lstm_cell/thnn_fused_lstm_cell_aten_kernels.cc.md#DispatchThnnFusedLstmCellCommon), [`DispatchHardtanhBackward`](../ops/hardtanh/hardtanh_aten_kernels.cc.md#DispatchHardtanhBackward), [`DispatchLogit`](../ops/logit/logit_aten_kernels.cc.md#DispatchLogit), [`GetTensorSpan`](op_dispatcher.h.md#GetTensorSpan), [`BuildLogitBufferOut`](../ops/logit/logit_aten_kernels.cc.md#BuildLogitBufferOut), [`AtenHardtanhBackwardImpl`](../ops/hardtanh/hardtanh_aten_kernels.cc.md#AtenHardtanhBackwardImpl), [`AtenHardtanhImpl`](../ops/hardtanh/hardtanh_aten_kernels.cc.md#AtenHardtanhImpl), [`BuildLogitBuffer`](../ops/logit/logit_aten_kernels.cc.md#BuildLogitBuffer), [`AtenHardtanhBackwardOutImpl`](../ops/hardtanh/hardtanh_aten_kernels.cc.md#AtenHardtanhBackwardOutImpl), [`AtenHardtanhOutImpl`](../ops/hardtanh/hardtanh_aten_kernels.cc.md#AtenHardtanhOutImpl)

### <a id="OpInputsTraits"></a>`OpInputsTraits`
- def: [`csrc/eager/op_dispatcher.h:254`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L254)
- signature: `template <int kArity> using OpInputsTraits = TensorGroupTraits<kArity>`
- uses (calls/refs, reference-scoped): [`TensorGroupTraits`](op_dispatcher.h.md#TensorGroupTraits)
- used by: [`OpInputs`](op_dispatcher.h.md#OpInputs)

### <a id="OpOutputs"></a>`OpOutputs`
- def: [`csrc/eager/op_dispatcher.h:265`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L265)
- signature: `template <int kNumOutputs> using OpOutputs = internal::OpOutputsTraits<kNumOutputs>::type`
- uses (calls/refs, reference-scoped): [`OpOutputsTraits`](op_dispatcher.h.md#OpOutputsTraits)
- used by: [`DispatchOpOut`](op_dispatcher.h.md#DispatchOpOut), [`DispatchNllLossForwardOut`](../ops/nll_loss/nll_loss_aten_kernels.cc.md#DispatchNllLossForwardOut)

### <a id="OpOutputsTraits"></a>`OpOutputsTraits`
- def: [`csrc/eager/op_dispatcher.h:257`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L257)
- signature: `template <int kNumOutputs> using OpOutputsTraits = TensorGroupTraits<kNumOutputs>`
- uses (calls/refs, reference-scoped): [`TensorGroupTraits`](op_dispatcher.h.md#TensorGroupTraits)
- used by: [`OpOutputs`](op_dispatcher.h.md#OpOutputs)

### <a id="TensorGroupTraits"></a>`TensorGroupTraits`
- def: [`csrc/eager/op_dispatcher.h:239`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L239)
- signature: `template <int kSize> struct TensorGroupTraits`
- uses (calls/refs, reference-scoped): [`kDynamicSize`](../ops/op_builder_utils.h.md#kDynamicSize)
- used by: [`OpInputsTraits`](op_dispatcher.h.md#OpInputsTraits), [`OpOutputsTraits`](op_dispatcher.h.md#OpOutputsTraits)

### <a id="TensorGroupTraits.type"></a>`TensorGroupTraits.type`
- def: [`csrc/eager/op_dispatcher.h:240`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L240)
- signature: `using type = std::array<TensorHolder, kSize>`
- uses (calls/refs, reference-scoped): [`TensorHolder`](op_dispatcher.h.md#TensorHolder)

### <a id="TensorHolder"></a>`TensorHolder`  ·  implements/extends Tensor, TensorBase
- def: [`csrc/eager/op_dispatcher.h:196`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L196)
- doc: Holds an at::Tensor. This class is deliberately not default constructible.
- signature: `class TensorHolder : public at::Tensor`
- members:
  - `TensorHolder()` — [`L199`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L199) — No default constructor. Must be initialized with a Tensor.
  - <a id="TensorHolder.TensorHolder"></a>`TensorHolder(const at::Tensor& tensor)` — [`L202`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L202) — Constructs a TensorHolder that holds the given tensor.
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenSparseGatherBackward`](../ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc.md#AtenSparseGatherBackward), [`AtenSparseGather`](../ops/experimental/sparse_gather/sparse_gather_aten_kernels.cc.md#AtenSparseGather), [`AtenSparseDenseMatmulGradWithSgd`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc.md#AtenSparseDenseMatmulGradWithSgd), [`AtenSparseDenseMatmulGradWithAdagrad`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc.md#AtenSparseDenseMatmulGradWithAdagrad), [`AtenSparseDenseMatmulGradWithAdam`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc.md#AtenSparseDenseMatmulGradWithAdam), [`AtenSparseDenseMatmul`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_aten_kernels.cc.md#AtenSparseDenseMatmul), [`type`](op_dispatcher.h.md#TensorGroupTraits.type)

## Functions
- <a id="DispatchOp"></a>`DispatchOp(NAryMlirOpBuilder<kArity, kNumOutputs> op_builder, const OpInputs<kArity>& inputs, DispatchOpOptions<kNumOutputs> options)` — [`L312`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L312) — Dispatches an op with the given number of inputs (kArity) and given number of — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- `DispatchOp(NAryMlirOpBuilder<kArity, kNumOutputs> op_builder, const OpInputs<kArity>& inputs, DispatchOpOptions<kNumOutputs> options)` — [`L312`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L312) — Dispatches an op with the given number of inputs (kArity) and given number of
- `DispatchOpOut(NAryMlirOpBuilder<kArity, kNumOutputs> op_builder, const OpInputs<kArity>& inputs, const OpOutputs<kNumOutputs>& outputs, DispatchOpOptions<kNumOutputs> options)` — [`L455`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L455) — Dispatches an op with out-tensor(s) (or in-place destination tensor(s)).
- <a id="DispatchOpOut"></a>`DispatchOpOut(NAryMlirOpBuilder<kArity, kNumOutputs> op_builder, const OpInputs<kArity>& inputs, const OpOutputs<kNumOutputs>& outputs, DispatchOpOptions<kNumOutputs> options)` — [`L455`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L455) — Dispatches an op with out-tensor(s) (or in-place destination tensor(s)). — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="GetTensorSpan"></a>`GetTensorSpan(const OpInputs<kSize>& tensors)` — [`L270`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L270) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- `GetTensorSpan(const OpInputs<kSize>& tensors)` — [`L270`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.h#L270)

