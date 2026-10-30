---
title: 'Module: csrc/ops/lstm/lstm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/lstm/lstm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  LstmInputBackwardImpl: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmInputBackwardImpl(24652b7883f365fb).'
  LstmInputImpl: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmInputImpl(e4768e749b541ce3).'
  kLstmUnrollFactor: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/kLstmUnrollFactor.'
  AtenLstmInputForward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/AtenLstmInputForward(4d7ff64496a57b68).'
  AtenLstmInputForwardCached: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/AtenLstmInputForwardCached(7880dea9d7657063).'
  LstmInputForwardCachedImpl: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmInputForwardCachedImpl(e4768e749b541ce3).'
  ConcatDim: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ConcatDim(6e7c76436169e8ad).'
  AtenLstmInputBackward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/AtenLstmInputBackward(22ee14f7bb668975).'
  ValidateLstmWeights: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ValidateLstmWeights(1401b20f079ac7db).'
  BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_hr: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontBackward(c88c05db16f6ce4a).LayerCarriedState#grad_w_hr.'
  RecomputeLayerForward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/RecomputeLayerForward(10624b7fb81c77a4).'
  ComputeLayerBackwardChunked: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ComputeLayerBackwardChunked(8267983eca45243a).'
  ComputeBidirLayerBackwardChunked: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ComputeBidirLayerBackwardChunked(96b8cd9c977b82ff).'
  ComputeLayerBackwardStatic: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ComputeLayerBackwardStatic(aa453b60df25a58b).'
  ComputeBidirLayerBackwardStatic: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ComputeBidirLayerBackwardStatic(96b8cd9c977b82ff).'
  ValidateLstmInputs: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ValidateLstmInputs(3aa30523407f1ad2).'
  ExpandStep3D: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ExpandStep3D(8a89aec4339114aa).'
  BuildLstmPipelinedWavefrontBackward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontBackward(c88c05db16f6ce4a).'
  BuildLstmPipelinedWavefrontForward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontForward(e506add935b521c5).'
  SliceStep2D: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/SliceStep2D(401f1bfb9044e5bc).'
  ValidateLstmTensorShapes: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ValidateLstmTensorShapes(638bfab7c2dcb3a4).'
  MixedPrecisionDotGeneral: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MixedPrecisionDotGeneral(c4ec13472dc7d72a).'
  BuildLstmLayerForward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmLayerForward(87ba72a5405749eb).'
  ComputeBackwardStep: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ComputeBackwardStep(d423a3f2bf557ff).'
  BuildLstmBidirChunkedForward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmBidirChunkedForward(3637d03f906d1f8c).'
  GetStepActivation: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/GetStepActivation(572dc665e10a31b1).'
  ComputeBidirLayerBackward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ComputeBidirLayerBackward(cdbf4762b5576251).'
  ExtractLayer2D: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ExtractLayer2D(c8a45fb15a5a1e6e).'
  ClumpWeight3H: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ClumpWeight3H(ee5195a48b9d168b).'
  BuildLstmBidirStaticForward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmBidirStaticForward(d27890979d4471c5).'
  BuildLstmStaticForward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmStaticForward(87ba72a5405749eb).'
  ComputeLayerBackward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ComputeLayerBackward(8267983eca45243a).'
  AtenLstmInputAutograd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/AtenLstmInputAutograd#'
  LayerForwardState.cellgate_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#cellgate_seq.'
  LayerForwardState.tanh_c_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#tanh_c_seq.'
  LayerForwardState.c_prev_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#c_prev_seq.'
  LstmStepResults.c_next: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#c_next.'
  LstmStepResults: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#'
  UnclumpWeight3H: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/UnclumpWeight3H(ee5195a48b9d168b).'
  LstmStepResults.h_next: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#h_next.'
  LayerForwardState.ifo_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#ifo_seq.'
  LayerForwardState.h_prev_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#h_prev_seq.'
  LayerForwardState: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#'
  BuildLstmBidirLayerForward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmBidirLayerForward(d27890979d4471c5).'
  ComputeLstmStep: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ComputeLstmStep(605bae580b7f9357).'
  ApplyInterLayerDropout: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ApplyInterLayerDropout(298a919c64156403).'
  BackwardStepResult: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BackwardStepResult#'
  LayerRecomputeResult.state: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerRecomputeResult#state.'
  LayerForwardState.c_prev_list: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#c_prev_list.'
  LayerForwardState.layer_input: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#layer_input.'
  BackwardStepResult.delta_h_rec: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BackwardStepResult#delta_h_rec.'
  AtenLstmInput: AtenLstmInput(4d7ff64496a57b68).
  LayerForwardState.tanh_c_list: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#tanh_c_list.'
  LayerForwardState.ifo_list: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#ifo_list.'
  BackwardStepResult.delta_pre: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BackwardStepResult#delta_pre.'
  BackwardStepResult.delta_c_next: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BackwardStepResult#delta_c_next.'
  LayerForwardState.cellgate_list: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#cellgate_list.'
  ApplyDropoutBackward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ApplyDropoutBackward(523d68859211d53).'
  AtenLstmInputAutograd.forward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/AtenLstmInputAutograd#forward(da3c09af49f6f95b).'
  UnclumpBias3H: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/UnclumpBias3H(660e1616a28e032f).'
  AtenLstmInputAutograd.backward: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/AtenLstmInputAutograd#backward(52c34ab91d035402).'
  MakeDotDims: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MakeDotDims(37c82e0c86549e0e).'
  ClumpBias3H: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/ClumpBias3H(660e1616a28e032f).'
  LayerRecomputeResult: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerRecomputeResult#'
  WavefrontLayerWeight.w_hh: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/WavefrontLayerWeight#w_hh.'
  WavefrontLayerWeight.w_hr: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/WavefrontLayerWeight#w_hr.'
  WavefrontLayerWeight.b_total: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/WavefrontLayerWeight#b_total.'
  LayerForwardState.h_prev_list: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#h_prev_list.'
  LstmLayerOutputs: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmLayerOutputs#'
  MultiLayerBackwardOutputs.grad_bias: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MultiLayerBackwardOutputs#grad_bias.'
  LstmStepResults.ifo_act: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#ifo_act.'
  LayerBackwardOutputs: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerBackwardOutputs#'
  LstmBidirLayerOutputs: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerOutputs#'
  LayerRecomputeResult.layer_output_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerRecomputeResult#layer_output_seq.'
  LstmBidirLayerBackwardOutputs: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#'
  LstmStepResults.cellgate: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#cellgate.'
  LayerForwardState.c_curr_list: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerForwardState#c_curr_list.'
  LstmStepResults.tanh_c: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#tanh_c.'
  MultiLayerBackwardOutputs: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MultiLayerBackwardOutputs#'
  WavefrontLayerWeight.w_ih: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/WavefrontLayerWeight#w_ih.'
  MultiLayerBackwardOutputs.grad_w_ih: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MultiLayerBackwardOutputs#grad_w_ih.'
  UnpackedActivations: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/UnpackedActivations#'
  MultiLayerBackwardOutputs.grad_x: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MultiLayerBackwardOutputs#grad_x.'
  MultiLayerBackwardOutputs.grad_h0: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MultiLayerBackwardOutputs#grad_h0.'
  MultiLayerBackwardOutputs.grad_w_hh: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MultiLayerBackwardOutputs#grad_w_hh.'
  MultiLayerBackwardOutputs.grad_c0: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MultiLayerBackwardOutputs#grad_c0.'
  LstmBidirLayerBackwardOutputs.grad_w_hr_fwd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_w_hr_fwd.'
  LstmLayerOutputs.final_h: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmLayerOutputs#final_h.'
  LstmLayerOutputs.layer_output_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmLayerOutputs#layer_output_seq.'
  WavefrontLayerWeight: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/WavefrontLayerWeight#'
  UnpackedActivations.tanh_c_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/UnpackedActivations#tanh_c_seq.'
  UnpackedActivations.cellgate_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/UnpackedActivations#cellgate_seq.'
  UnpackedActivations.c_prev_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/UnpackedActivations#c_prev_seq.'
  LayerBackwardOutputs.grad_bias: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerBackwardOutputs#grad_bias.'
  LayerRecomputeResult.final_h: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerRecomputeResult#final_h.'
  LstmBidirLayerBackwardOutputs.grad_bias_rev: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_bias_rev.'
  LstmLayerOutputs.final_c: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmLayerOutputs#final_c.'
  LstmBidirLayerBackwardOutputs.grad_bias_fwd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_bias_fwd.'
  UnpackCachedActivations: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/UnpackCachedActivations(d9f7238b325b5ec).'
  LstmBidirLayerBackwardOutputs.grad_w_hr_rev: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_w_hr_rev.'
  UnpackedActivations.h_prev_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/UnpackedActivations#h_prev_seq.'
  MultiLayerBackwardOutputs.grad_w_hr: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/MultiLayerBackwardOutputs#grad_w_hr.'
  LstmBidirLayerBackwardOutputs.grad_w_ih_fwd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_w_ih_fwd.'
  LstmBidirLayerBackwardOutputs.grad_h0_rev: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_h0_rev.'
  LayerBackwardOutputs.grad_x_layer: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerBackwardOutputs#grad_x_layer.'
  LayerBackwardOutputs.grad_w_ih: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerBackwardOutputs#grad_w_ih.'
  LstmBidirLayerBackwardOutputs.grad_h0_fwd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_h0_fwd.'
  LstmBidirLayerBackwardOutputs.grad_w_ih_rev: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_w_ih_rev.'
  LstmBidirLayerBackwardOutputs.grad_w_hh_rev: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_w_hh_rev.'
  LayerBackwardOutputs.grad_c0_layer: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerBackwardOutputs#grad_c0_layer.'
  GetElementTypeEnum: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/GetElementTypeEnum(86763d29f90d7077).'
  LstmBidirLayerBackwardOutputs.grad_w_hh_fwd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_w_hh_fwd.'
  LstmBidirLayerOutputs.final_h_rev: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerOutputs#final_h_rev.'
  LstmBidirLayerBackwardOutputs.grad_c0_fwd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_c0_fwd.'
  LstmBidirLayerOutputs.final_h_fwd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerOutputs#final_h_fwd.'
  LstmBidirLayerBackwardOutputs.grad_x_layer: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_x_layer.'
  LstmBidirLayerBackwardOutputs.grad_c0_rev: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerBackwardOutputs#grad_c0_rev.'
  LayerBackwardOutputs.grad_h0_layer: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerBackwardOutputs#grad_h0_layer.'
  LstmBidirLayerOutputs.final_c_fwd: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerOutputs#final_c_fwd.'
  LstmBidirLayerOutputs.final_c_rev: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerOutputs#final_c_rev.'
  LayerBackwardOutputs.grad_w_hh: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerBackwardOutputs#grad_w_hh.'
  LstmBidirLayerOutputs.layer_output_seq: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmBidirLayerOutputs#layer_output_seq.'
  BuildLstmPipelinedWavefrontBackward.LayerCarriedState.delta_h_rec: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontBackward(c88c05db16f6ce4a).LayerCarriedState#delta_h_rec.'
  BuildLstmPipelinedWavefrontBackward.LayerCarriedState.delta_c_next: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontBackward(c88c05db16f6ce4a).LayerCarriedState#delta_c_next.'
  BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_b: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontBackward(c88c05db16f6ce4a).LayerCarriedState#grad_b.'
  BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_hh: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontBackward(c88c05db16f6ce4a).LayerCarriedState#grad_w_hh.'
  LstmStepResults.outgate: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#outgate.'
  BuildLstmPipelinedWavefrontBackward.LayerCarriedState: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontBackward(f10dd956b13b9df2).LayerCarriedState#'
  LstmStepResults.ingate: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#ingate.'
  BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_ih: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/BuildLstmPipelinedWavefrontBackward(c88c05db16f6ce4a).LayerCarriedState#grad_w_ih.'
  LstmStepResults.forgetgate: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LstmStepResults#forgetgate.'
  LayerRecomputeResult.final_c: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerRecomputeResult#final_c.'
  LayerBackwardOutputs.grad_w_hr: '`$anonymous_namespace_csrc/ops/lstm/lstm_aten_kernels.cc`/LayerBackwardOutputs#grad_w_hr.'
---
# Module: [`csrc/ops/lstm/lstm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc)

## Classes
### <a id="AtenLstmInputAutograd"></a>`AtenLstmInputAutograd`  ·  implements/extends Function
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:6262`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6262)
- doc: =============================================================================
- signature: `struct AtenLstmInputAutograd : public torch::autograd::Function<AtenLstmInputAutograd>`
- members:
  - `backward(torch::autograd::AutogradContext* ctx, torch::autograd::variable_list grad_outputs)` — [`L6308`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6308)
  - <a id="AtenLstmInputAutograd.backward"></a>`backward(torch::autograd::AutogradContext* ctx, torch::autograd::variable_list grad_outputs)` — [`L6308`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6308)
  - <a id="AtenLstmInputAutograd.forward"></a>`forward(torch::autograd::AutogradContext* ctx, const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6275`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6275)
  - `forward(torch::autograd::AutogradContext* ctx, const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6275`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6275)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`AtenLstmInputForwardCached`](lstm_aten_kernels.cc.md#AtenLstmInputForwardCached), [`AtenLstmInputBackward`](lstm_aten_kernels.cc.md#AtenLstmInputBackward)
- used by: [`AtenLstmInput`](lstm_aten_kernels.cc.md#AtenLstmInput)

### <a id="BackwardStepResult"></a>`BackwardStepResult`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:639`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L639)
- doc: Encapsulates intermediate results produced during a single LSTM recurrent
- signature: `struct BackwardStepResult`
- members:
  - <a id="BackwardStepResult.delta_c_next"></a>`delta_c_next` — [`L641`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L641)
  - <a id="BackwardStepResult.delta_h_rec"></a>`delta_h_rec` — [`L642`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L642)
  - <a id="BackwardStepResult.delta_pre"></a>`delta_pre` — [`L640`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L640)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`grad_w_hr`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_hr), [`ComputeBidirLayerBackwardChunked`](lstm_aten_kernels.cc.md#ComputeBidirLayerBackwardChunked), [`ComputeLayerBackwardChunked`](lstm_aten_kernels.cc.md#ComputeLayerBackwardChunked), [`ComputeBidirLayerBackwardStatic`](lstm_aten_kernels.cc.md#ComputeBidirLayerBackwardStatic), [`ComputeLayerBackwardStatic`](lstm_aten_kernels.cc.md#ComputeLayerBackwardStatic), [`BuildLstmPipelinedWavefrontBackward`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontBackward)

### <a id="BuildLstmPipelinedWavefrontBackward.LayerCarriedState"></a>`BuildLstmPipelinedWavefrontBackward.LayerCarriedState`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:3316`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3316)
- signature: `struct LayerCarriedState`
- members:
  - <a id="BuildLstmPipelinedWavefrontBackward.LayerCarriedState.delta_c_next"></a>`delta_c_next` — [`L3318`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3318)
  - `delta_c_next` — [`L3318`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3318)
  - <a id="BuildLstmPipelinedWavefrontBackward.LayerCarriedState.delta_h_rec"></a>`delta_h_rec` — [`L3317`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3317)
  - `delta_h_rec` — [`L3317`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3317)
  - `grad_b` — [`L3321`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3321)
  - <a id="BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_b"></a>`grad_b` — [`L3321`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3321)
  - `grad_w_hh` — [`L3320`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3320)
  - <a id="BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_hh"></a>`grad_w_hh` — [`L3320`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3320)
  - `grad_w_hr` — [`L3322`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3322)
  - <a id="BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_hr"></a>`grad_w_hr` — [`L3322`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3322)
  - `grad_w_ih` — [`L3319`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3319)
  - <a id="BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_ih"></a>`grad_w_ih` — [`L3319`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3319)
- uses (calls/refs, reference-scoped): [`MakeScalarConstant`](../op_builder_utils.h.md#MakeScalarConstant), [`MakeScalarConstant`](../op_builder_utils.h.md#MakeScalarConstant), [`kLstmUnrollFactor`](lstm_aten_kernels.cc.md#kLstmUnrollFactor), [`ConcatDim`](lstm_aten_kernels.cc.md#ConcatDim), [`ExpandStep3D`](lstm_aten_kernels.cc.md#ExpandStep3D), [`SliceStep2D`](lstm_aten_kernels.cc.md#SliceStep2D), [`MixedPrecisionDotGeneral`](lstm_aten_kernels.cc.md#MixedPrecisionDotGeneral), [`c_prev_seq`](lstm_aten_kernels.cc.md#LayerForwardState.c_prev_seq), [`cellgate_seq`](lstm_aten_kernels.cc.md#LayerForwardState.cellgate_seq), [`tanh_c_seq`](lstm_aten_kernels.cc.md#LayerForwardState.tanh_c_seq), [`UnclumpWeight3H`](lstm_aten_kernels.cc.md#UnclumpWeight3H), [`MixedPrecisionDotGeneral`](lstm_aten_kernels.cc.md#MixedPrecisionDotGeneral), [`ifo_seq`](lstm_aten_kernels.cc.md#LayerForwardState.ifo_seq), [`h_prev_seq`](lstm_aten_kernels.cc.md#LayerForwardState.h_prev_seq), [`BackwardStepResult`](lstm_aten_kernels.cc.md#BackwardStepResult), [`delta_c_next`](lstm_aten_kernels.cc.md#BackwardStepResult.delta_c_next), [`delta_h_rec`](lstm_aten_kernels.cc.md#BackwardStepResult.delta_h_rec), [`delta_pre`](lstm_aten_kernels.cc.md#BackwardStepResult.delta_pre), [`layer_input`](lstm_aten_kernels.cc.md#LayerForwardState.layer_input), [`ApplyDropoutBackward`](lstm_aten_kernels.cc.md#ApplyDropoutBackward), [`UnclumpBias3H`](lstm_aten_kernels.cc.md#UnclumpBias3H), [`ComputeBackwardStep`](lstm_aten_kernels.cc.md#ComputeBackwardStep), [`LstmBidirLayerBackwardOutputs`](lstm_aten_kernels.cc.md#LstmBidirLayerBackwardOutputs), [`grad_bias`](lstm_aten_kernels.cc.md#MultiLayerBackwardOutputs.grad_bias), [`MultiLayerBackwardOutputs`](lstm_aten_kernels.cc.md#MultiLayerBackwardOutputs), [`grad_c0`](lstm_aten_kernels.cc.md#MultiLayerBackwardOutputs.grad_c0), [`grad_h0`](lstm_aten_kernels.cc.md#MultiLayerBackwardOutputs.grad_h0), [`grad_w_hh`](lstm_aten_kernels.cc.md#MultiLayerBackwardOutputs.grad_w_hh), [`grad_w_ih`](lstm_aten_kernels.cc.md#MultiLayerBackwardOutputs.grad_w_ih), [`grad_x`](lstm_aten_kernels.cc.md#MultiLayerBackwardOutputs.grad_x), [`grad_w_hr`](lstm_aten_kernels.cc.md#MultiLayerBackwardOutputs.grad_w_hr), [`LayerCarriedState`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontBackward.LayerCarriedState)

### <a id="LayerBackwardOutputs"></a>`LayerBackwardOutputs`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:1881`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1881)
- doc: Result gradients computed for a single LSTM layer during BPTT:
- signature: `struct LayerBackwardOutputs`
- members:
  - <a id="LayerBackwardOutputs.grad_bias"></a>`grad_bias` — [`L1887`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1887)
  - <a id="LayerBackwardOutputs.grad_c0_layer"></a>`grad_c0_layer` — [`L1884`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1884)
  - <a id="LayerBackwardOutputs.grad_h0_layer"></a>`grad_h0_layer` — [`L1883`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1883)
  - <a id="LayerBackwardOutputs.grad_w_hh"></a>`grad_w_hh` — [`L1886`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1886)
  - <a id="LayerBackwardOutputs.grad_w_hr"></a>`grad_w_hr` — [`L1888`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1888)
  - <a id="LayerBackwardOutputs.grad_w_ih"></a>`grad_w_ih` — [`L1885`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1885)
  - <a id="LayerBackwardOutputs.grad_x_layer"></a>`grad_x_layer` — [`L1882`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1882)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`LstmInputBackwardImpl`](lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`RecomputeLayerForward`](lstm_aten_kernels.cc.md#RecomputeLayerForward), [`ComputeLayerBackwardChunked`](lstm_aten_kernels.cc.md#ComputeLayerBackwardChunked), [`ComputeLayerBackwardStatic`](lstm_aten_kernels.cc.md#ComputeLayerBackwardStatic)

### <a id="LayerForwardState"></a>`LayerForwardState`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:1803`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1803)
- doc: Forward activations recorded per layer during backpropagation recomputation.
- signature: `struct LayerForwardState`
- members:
  - <a id="LayerForwardState.c_curr_list"></a>`c_curr_list` — [`L1808`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1808)
  - <a id="LayerForwardState.c_prev_list"></a>`c_prev_list` — [`L1806`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1806)
  - <a id="LayerForwardState.c_prev_seq"></a>`c_prev_seq` — [`L1815`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1815)
  - <a id="LayerForwardState.cellgate_list"></a>`cellgate_list` — [`L1807`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1807)
  - <a id="LayerForwardState.cellgate_seq"></a>`cellgate_seq` — [`L1816`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1816)
  - <a id="LayerForwardState.h_prev_list"></a>`h_prev_list` — [`L1805`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1805)
  - <a id="LayerForwardState.h_prev_seq"></a>`h_prev_seq` — [`L1814`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1814) — Sequence tensors for chunked BPTT
  - <a id="LayerForwardState.ifo_list"></a>`ifo_list` — [`L1811`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1811) — 3H clumped [i, f, o] activations [B, 3*H]
  - <a id="LayerForwardState.ifo_seq"></a>`ifo_seq` — [`L1818`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1818) — 3H clumped [i, f, o] sequence [seq_len, batch, 3*H]
  - <a id="LayerForwardState.layer_input"></a>`layer_input` — [`L1804`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1804)
  - <a id="LayerForwardState.tanh_c_list"></a>`tanh_c_list` — [`L1809`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1809)
  - <a id="LayerForwardState.tanh_c_seq"></a>`tanh_c_seq` — [`L1817`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1817)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`LstmInputBackwardImpl`](lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`LstmInputForwardCachedImpl`](lstm_aten_kernels.cc.md#LstmInputForwardCachedImpl), [`grad_w_hr`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_hr), [`RecomputeLayerForward`](lstm_aten_kernels.cc.md#RecomputeLayerForward), [`ComputeBidirLayerBackwardChunked`](lstm_aten_kernels.cc.md#ComputeBidirLayerBackwardChunked), [`ComputeLayerBackwardChunked`](lstm_aten_kernels.cc.md#ComputeLayerBackwardChunked), [`ComputeBidirLayerBackwardStatic`](lstm_aten_kernels.cc.md#ComputeBidirLayerBackwardStatic), [`ComputeLayerBackwardStatic`](lstm_aten_kernels.cc.md#ComputeLayerBackwardStatic), [`BuildLstmPipelinedWavefrontBackward`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontBackward), [`ComputeBidirLayerBackward`](lstm_aten_kernels.cc.md#ComputeBidirLayerBackward), [`ComputeLayerBackward`](lstm_aten_kernels.cc.md#ComputeLayerBackward), [`LayerRecomputeResult`](lstm_aten_kernels.cc.md#LayerRecomputeResult)

### <a id="LayerRecomputeResult"></a>`LayerRecomputeResult`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:1823`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1823)
- doc: Encapsulates recorded forward activation state and sequence output for layer
- signature: `struct LayerRecomputeResult`
- members:
  - <a id="LayerRecomputeResult.final_c"></a>`final_c` — [`L1827`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1827)
  - <a id="LayerRecomputeResult.final_h"></a>`final_h` — [`L1826`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1826)
  - <a id="LayerRecomputeResult.layer_output_seq"></a>`layer_output_seq` — [`L1825`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1825)
  - <a id="LayerRecomputeResult.state"></a>`state` — [`L1824`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1824)
- uses (calls/refs, reference-scoped): [`LayerForwardState`](lstm_aten_kernels.cc.md#LayerForwardState)
- used by: [`LstmInputBackwardImpl`](lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`LstmInputForwardCachedImpl`](lstm_aten_kernels.cc.md#LstmInputForwardCachedImpl), [`grad_w_hr_rev`](lstm_aten_kernels.cc.md#LstmBidirLayerBackwardOutputs.grad_w_hr_rev)

### <a id="LstmBidirLayerBackwardOutputs"></a>`LstmBidirLayerBackwardOutputs`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:1921`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1921)
- doc: Result gradients computed for a bidirectional LSTM layer during BPTT:
- signature: `struct LstmBidirLayerBackwardOutputs`
- members:
  - <a id="LstmBidirLayerBackwardOutputs.grad_bias_fwd"></a>`grad_bias_fwd` — [`L1931`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1931)
  - <a id="LstmBidirLayerBackwardOutputs.grad_bias_rev"></a>`grad_bias_rev` — [`L1932`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1932)
  - <a id="LstmBidirLayerBackwardOutputs.grad_c0_fwd"></a>`grad_c0_fwd` — [`L1924`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1924)
  - <a id="LstmBidirLayerBackwardOutputs.grad_c0_rev"></a>`grad_c0_rev` — [`L1926`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1926)
  - <a id="LstmBidirLayerBackwardOutputs.grad_h0_fwd"></a>`grad_h0_fwd` — [`L1923`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1923)
  - <a id="LstmBidirLayerBackwardOutputs.grad_h0_rev"></a>`grad_h0_rev` — [`L1925`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1925)
  - <a id="LstmBidirLayerBackwardOutputs.grad_w_hh_fwd"></a>`grad_w_hh_fwd` — [`L1928`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1928)
  - <a id="LstmBidirLayerBackwardOutputs.grad_w_hh_rev"></a>`grad_w_hh_rev` — [`L1930`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1930)
  - <a id="LstmBidirLayerBackwardOutputs.grad_w_hr_fwd"></a>`grad_w_hr_fwd` — [`L1933`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1933)
  - <a id="LstmBidirLayerBackwardOutputs.grad_w_hr_rev"></a>`grad_w_hr_rev` — [`L1934`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1934)
  - <a id="LstmBidirLayerBackwardOutputs.grad_w_ih_fwd"></a>`grad_w_ih_fwd` — [`L1927`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1927)
  - <a id="LstmBidirLayerBackwardOutputs.grad_w_ih_rev"></a>`grad_w_ih_rev` — [`L1929`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1929)
  - <a id="LstmBidirLayerBackwardOutputs.grad_x_layer"></a>`grad_x_layer` — [`L1922`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1922)
- uses (calls/refs, reference-scoped): [`LayerRecomputeResult`](lstm_aten_kernels.cc.md#LayerRecomputeResult)
- used by: [`LstmInputBackwardImpl`](lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`grad_w_hr`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_hr), [`ComputeBidirLayerBackwardChunked`](lstm_aten_kernels.cc.md#ComputeBidirLayerBackwardChunked), [`ComputeBidirLayerBackwardStatic`](lstm_aten_kernels.cc.md#ComputeBidirLayerBackwardStatic)

### <a id="LstmBidirLayerOutputs"></a>`LstmBidirLayerOutputs`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:1382`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1382)
- doc: Encapsulates output tensors produced by a bidirectional LSTM layer:
- signature: `struct LstmBidirLayerOutputs`
- members:
  - <a id="LstmBidirLayerOutputs.final_c_fwd"></a>`final_c_fwd` — [`L1385`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1385)
  - <a id="LstmBidirLayerOutputs.final_c_rev"></a>`final_c_rev` — [`L1387`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1387)
  - <a id="LstmBidirLayerOutputs.final_h_fwd"></a>`final_h_fwd` — [`L1384`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1384)
  - <a id="LstmBidirLayerOutputs.final_h_rev"></a>`final_h_rev` — [`L1386`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1386)
  - <a id="LstmBidirLayerOutputs.layer_output_seq"></a>`layer_output_seq` — [`L1383`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1383)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`LstmInputImpl`](lstm_aten_kernels.cc.md#LstmInputImpl), [`BuildLstmBidirChunkedForward`](lstm_aten_kernels.cc.md#BuildLstmBidirChunkedForward), [`BuildLstmBidirStaticForward`](lstm_aten_kernels.cc.md#BuildLstmBidirStaticForward)

### <a id="LstmLayerOutputs"></a>`LstmLayerOutputs`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:699`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L699)
- doc: Encapsulates output sequence and final hidden/cell states for a single layer.
- signature: `struct LstmLayerOutputs`
- members:
  - <a id="LstmLayerOutputs.final_c"></a>`final_c` — [`L702`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L702) — [1, B, H]
  - <a id="LstmLayerOutputs.final_h"></a>`final_h` — [`L701`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L701) — [1, B, H]
  - <a id="LstmLayerOutputs.layer_output_seq"></a>`layer_output_seq` — [`L700`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L700) — [T, B, H] or [B, T, H]
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`LstmInputImpl`](lstm_aten_kernels.cc.md#LstmInputImpl), [`BuildLstmStaticForward`](lstm_aten_kernels.cc.md#BuildLstmStaticForward), [`w_hr`](lstm_aten_kernels.cc.md#WavefrontLayerWeight.w_hr)

### <a id="LstmStepResults"></a>`LstmStepResults`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:429`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L429)
- doc: Encapsulates intermediate and final activation tensors produced during a
- signature: `struct LstmStepResults`
- members:
  - <a id="LstmStepResults.c_next"></a>`c_next` — [`L432`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L432) — Next cell state: c_t = f_t * c_{t-1} + i_t * g_t [B, H]
  - <a id="LstmStepResults.cellgate"></a>`cellgate` — [`L436`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L436) — Cell candidate activation: g_t = tanh(g_pre) [B, H]
  - <a id="LstmStepResults.forgetgate"></a>`forgetgate` — [`L435`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L435) — Forget gate activation: f_t = sigmoid(f_pre) [B, H]
  - <a id="LstmStepResults.h_next"></a>`h_next` — [`L430`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L430) — Next hidden state: h_t = o_t * tanh(c_t) [B, H]
  - <a id="LstmStepResults.ifo_act"></a>`ifo_act` — [`L439`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L439) — 3H Gate Clumped activations: [i, f, o] [B, 3*H]
  - <a id="LstmStepResults.ingate"></a>`ingate` — [`L433`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L433) — Input gate activation: i_t = sigmoid(i_pre) [B, H]
  - <a id="LstmStepResults.outgate"></a>`outgate` — [`L437`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L437) — Output gate activation: o_t = sigmoid(o_pre) [B, H]
  - <a id="LstmStepResults.tanh_c"></a>`tanh_c` — [`L438`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L438) — Non-linear cell projection: tanh(c_t) [B, H]
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`RecomputeLayerForward`](lstm_aten_kernels.cc.md#RecomputeLayerForward), [`BuildLstmPipelinedWavefrontForward`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontForward), [`BuildLstmLayerForward`](lstm_aten_kernels.cc.md#BuildLstmLayerForward), [`BuildLstmBidirChunkedForward`](lstm_aten_kernels.cc.md#BuildLstmBidirChunkedForward), [`BuildLstmBidirStaticForward`](lstm_aten_kernels.cc.md#BuildLstmBidirStaticForward), [`BuildLstmStaticForward`](lstm_aten_kernels.cc.md#BuildLstmStaticForward), [`MixedPrecisionDotGeneral`](lstm_aten_kernels.cc.md#MixedPrecisionDotGeneral)

### <a id="MultiLayerBackwardOutputs"></a>`MultiLayerBackwardOutputs`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:1900`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1900)
- doc: Result gradients computed for multi-layer LSTM during Pipelined Wavefront
- signature: `struct MultiLayerBackwardOutputs`
- members:
  - <a id="MultiLayerBackwardOutputs.grad_bias"></a>`grad_bias` — [`L1906`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1906)
  - <a id="MultiLayerBackwardOutputs.grad_c0"></a>`grad_c0` — [`L1903`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1903)
  - <a id="MultiLayerBackwardOutputs.grad_h0"></a>`grad_h0` — [`L1902`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1902)
  - <a id="MultiLayerBackwardOutputs.grad_w_hh"></a>`grad_w_hh` — [`L1905`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1905)
  - <a id="MultiLayerBackwardOutputs.grad_w_hr"></a>`grad_w_hr` — [`L1907`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1907)
  - <a id="MultiLayerBackwardOutputs.grad_w_ih"></a>`grad_w_ih` — [`L1904`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1904)
  - <a id="MultiLayerBackwardOutputs.grad_x"></a>`grad_x` — [`L1901`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1901)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`LstmInputBackwardImpl`](lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`grad_w_hr`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontBackward.LayerCarriedState.grad_w_hr), [`ComputeLayerBackward`](lstm_aten_kernels.cc.md#ComputeLayerBackward)

### <a id="UnpackedActivations"></a>`UnpackedActivations`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:1832`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1832)
- doc: Encapsulates 4 unprojected activation sequences unpacked from a cached packed
- signature: `struct UnpackedActivations`
- members:
  - <a id="UnpackedActivations.c_prev_seq"></a>`c_prev_seq` — [`L1835`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1835)
  - <a id="UnpackedActivations.cellgate_seq"></a>`cellgate_seq` — [`L1833`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1833)
  - <a id="UnpackedActivations.h_prev_seq"></a>`h_prev_seq` — [`L1836`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1836)
  - <a id="UnpackedActivations.tanh_c_seq"></a>`tanh_c_seq` — [`L1834`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1834)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`LstmInputBackwardImpl`](lstm_aten_kernels.cc.md#LstmInputBackwardImpl)

### <a id="WavefrontLayerWeight"></a>`WavefrontLayerWeight`
- def: [`csrc/ops/lstm/lstm_aten_kernels.cc:1045`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1045)
- doc: Weights and optional projection for a single layer in pipelined wavefront.
- signature: `struct WavefrontLayerWeight`
- members:
  - <a id="WavefrontLayerWeight.b_total"></a>`b_total` — [`L1048`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1048) — clumped [4*H] (for l >= 1)
  - <a id="WavefrontLayerWeight.w_hh"></a>`w_hh` — [`L1046`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1046) — clumped [4*H, out_h]
  - <a id="WavefrontLayerWeight.w_hr"></a>`w_hr` — [`L1049`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1049) — optional [out_h, hidden]
  - <a id="WavefrontLayerWeight.w_ih"></a>`w_ih` — [`L1047`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1047) — clumped [4*H, out_h] (for l >= 1)
- uses (calls/refs, reference-scoped): [`LstmLayerOutputs`](lstm_aten_kernels.cc.md#LstmLayerOutputs)
- used by: [`LstmInputImpl`](lstm_aten_kernels.cc.md#LstmInputImpl), [`BuildLstmPipelinedWavefrontForward`](lstm_aten_kernels.cc.md#BuildLstmPipelinedWavefrontForward)

## Functions
- <a id="ApplyDropoutBackward"></a>`ApplyDropoutBackward(mlir::MlirOp grad_output, mlir::MlirOp mask, double dropout)` — [`L1032`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1032) — Applies backward dropout between LSTM layers on the sequence gradient tensor.
- <a id="ApplyInterLayerDropout"></a>`ApplyInterLayerDropout(mlir::MlirOp layer_out, mlir::MlirOp rand_tensor, double dropout)` — [`L1010`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1010)
- <a id="AtenLstmInput"></a>`AtenLstmInput(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6394`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6394) — =============================================================================
- `AtenLstmInputBackward(const at::Tensor& grad_output, const at::Tensor& grad_hy, const at::Tensor& grad_cy, const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, const at::TensorList cached_activations)` — [`L6206`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6206) — Backward execution entry point: wraps LstmInputBackwardImpl with TT_KERNEL
- <a id="AtenLstmInputBackward"></a>`AtenLstmInputBackward(const at::Tensor& grad_output, const at::Tensor& grad_hy, const at::Tensor& grad_cy, const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, const at::TensorList cached_activations)` — [`L6206`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6206) — Backward execution entry point: wraps LstmInputBackwardImpl with TT_KERNEL
- <a id="AtenLstmInputForward"></a>`AtenLstmInputForward(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6069`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6069) — Forward execution entry point: wraps LstmInputImpl with TT_KERNEL for
- `AtenLstmInputForwardCached(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6129`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6129) — Forward execution with intermediate activation caching for zero-recomputation
- <a id="AtenLstmInputForwardCached"></a>`AtenLstmInputForwardCached(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6129`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L6129) — Forward execution with intermediate activation caching for zero-recomputation
- `BuildLstmBidirChunkedForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp c_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp c_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr_fwd, std::optional<mlir::MlirOp> w_hr_rev, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L1484`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1484) — Chunked streaming helper for bidirectional LSTM forward recurrence (seq_len
- <a id="BuildLstmBidirChunkedForward"></a>`BuildLstmBidirChunkedForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp c_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp c_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr_fwd, std::optional<mlir::MlirOp> w_hr_rev, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L1484`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1484) — Chunked streaming helper for bidirectional LSTM forward recurrence (seq_len
- `BuildLstmBidirLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp c_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp c_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr_fwd, std::optional<mlir::MlirOp> w_hr_rev, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L1768`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1768) — Evaluates forward recurrence for a single bidirectional LSTM layer.
- <a id="BuildLstmBidirLayerForward"></a>`BuildLstmBidirLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp c_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp c_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr_fwd, std::optional<mlir::MlirOp> w_hr_rev, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L1768`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1768) — Evaluates forward recurrence for a single bidirectional LSTM layer.
- <a id="BuildLstmBidirStaticForward"></a>`BuildLstmBidirStaticForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp c_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp c_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr_fwd, std::optional<mlir::MlirOp> w_hr_rev, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L1406`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1406) — Evaluates forward recurrence for a bidirectional layer using Concurrent
- `BuildLstmBidirStaticForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp c_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp c_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr_fwd, std::optional<mlir::MlirOp> w_hr_rev, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L1406`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1406) — Evaluates forward recurrence for a bidirectional layer using Concurrent
- <a id="BuildLstmLayerForward"></a>`BuildLstmLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp h_init, mlir::MlirOp c_init, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L769`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L769) — Evaluates forward recurrence using chunked execution with partial unrolling
- `BuildLstmLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp h_init, mlir::MlirOp c_init, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L769`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L769) — Evaluates forward recurrence using chunked execution with partial unrolling
- `BuildLstmPipelinedWavefrontBackward` — [`L3008`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3008) — Evaluates backward recurrence through time (BPTT) for a multi-layer
- <a id="BuildLstmPipelinedWavefrontBackward"></a>`BuildLstmPipelinedWavefrontBackward` — [`L3008`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3008) — Evaluates backward recurrence through time (BPTT) for a multi-layer
- `BuildLstmPipelinedWavefrontForward` — [`L1058`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1058) — Evaluates forward recurrence for multi-layer unidirectional LSTM (L >= 2)
- <a id="BuildLstmPipelinedWavefrontForward"></a>`BuildLstmPipelinedWavefrontForward` — [`L1058`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1058) — Evaluates forward recurrence for multi-layer unidirectional LSTM (L >= 2)
- <a id="BuildLstmStaticForward"></a>`BuildLstmStaticForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp h_init, mlir::MlirOp c_init, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L722`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L722) — Computes forward recurrence for a single LSTM layer across sequence length T.
- `BuildLstmStaticForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp h_init, mlir::MlirOp c_init, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L722`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L722) — Computes forward recurrence for a single LSTM layer across sequence length T.
- <a id="ClumpBias3H"></a>`ClumpBias3H(mlir::MlirBuilder& builder, mlir::MlirOp b, int64_t hidden)` — [`L460`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L460) — Permutes a 1D bias vector [4*H] from PyTorch [i, f, g, o] order to
- <a id="ClumpWeight3H"></a>`ClumpWeight3H(mlir::MlirBuilder& builder, mlir::MlirOp w, int64_t hidden, int64_t in_dim)` — [`L444`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L444) — Permutes a 2D weight matrix [4*H, in_dim] from PyTorch [i, f, g, o] order to
- `ComputeBackwardStep(mlir::MlirBuilder& builder, mlir::MlirOp delta_h, mlir::MlirOp cur_delta_c_next, mlir::MlirOp tanh_c, mlir::MlirOp c_prev, mlir::MlirOp g, mlir::MlirOp ifo, mlir::MlirOp w_hh_clumped, mlir::stablehlo::DotDimensionNumbersAttr bwd_weight_dot_dims, int64_t batch, int64_t hidden, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> bwd_hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L656`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L656) — Computes a single recurrent LSTM backward BPTT step using Fused 4H Gate
- <a id="ComputeBackwardStep"></a>`ComputeBackwardStep(mlir::MlirBuilder& builder, mlir::MlirOp delta_h, mlir::MlirOp cur_delta_c_next, mlir::MlirOp tanh_c, mlir::MlirOp c_prev, mlir::MlirOp g, mlir::MlirOp ifo, mlir::MlirOp w_hh_clumped, mlir::stablehlo::DotDimensionNumbersAttr bwd_weight_dot_dims, int64_t batch, int64_t hidden, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> bwd_hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L656`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L656) — Computes a single recurrent LSTM backward BPTT step using Fused 4H Gate
- <a id="ComputeBidirLayerBackward"></a>`ComputeBidirLayerBackward` — [`L4676`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L4676) — Evaluates backward recurrence through time (BPTT) for a single bidirectional
- `ComputeBidirLayerBackward` — [`L4676`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L4676) — Evaluates backward recurrence through time (BPTT) for a single bidirectional
- <a id="ComputeBidirLayerBackwardChunked"></a>`ComputeBidirLayerBackwardChunked` — [`L3901`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3901) — Chunked streaming helper for bidirectional LSTM backward pass (seq_len >=
- `ComputeBidirLayerBackwardChunked` — [`L3901`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3901) — Chunked streaming helper for bidirectional LSTM backward pass (seq_len >=
- `ComputeBidirLayerBackwardStatic` — [`L3626`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3626) — Evaluates backward recurrence (BPTT) for a bidirectional layer using
- <a id="ComputeBidirLayerBackwardStatic"></a>`ComputeBidirLayerBackwardStatic` — [`L3626`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L3626) — Evaluates backward recurrence (BPTT) for a bidirectional layer using
- `ComputeLayerBackward` — [`L2960`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L2960) — Evaluates backward recurrence through time (BPTT) for a single unidirectional
- <a id="ComputeLayerBackward"></a>`ComputeLayerBackward` — [`L2960`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L2960) — Evaluates backward recurrence through time (BPTT) for a single unidirectional
- <a id="ComputeLayerBackwardChunked"></a>`ComputeLayerBackwardChunked` — [`L2493`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L2493) — Chunked streaming helper for unidirectional LSTM backward pass (seq_len >=
- `ComputeLayerBackwardChunked` — [`L2493`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L2493) — Chunked streaming helper for unidirectional LSTM backward pass (seq_len >=
- <a id="ComputeLayerBackwardStatic"></a>`ComputeLayerBackwardStatic` — [`L2348`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L2348) — Computes backward gradients through time (BPTT) for a single LSTM layer:
- `ComputeLayerBackwardStatic` — [`L2348`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L2348) — Computes backward gradients through time (BPTT) for a single LSTM layer:
- <a id="ComputeLstmStep"></a>`ComputeLstmStep(mlir::MlirOp x_proj_step, mlir::MlirOp h_curr, mlir::MlirOp c_curr, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t batch, int64_t hidden, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L581`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L581)
- `ComputeLstmStep(mlir::MlirOp x_proj_step, mlir::MlirOp h_curr, mlir::MlirOp c_curr, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t batch, int64_t hidden, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, mlir::stablehlo::Precision precision)` — [`L581`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L581)
- <a id="ConcatDim"></a>`ConcatDim(mlir::MlirBuilder& builder, absl::Span<const mlir::MlirOp> ops, int64_t dim)` — [`L386`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L386) — Concatenates a vector of tensors along the specified dimension.
- <a id="ExpandStep3D"></a>`ExpandStep3D(mlir::MlirOp step_2d, int64_t batch, int64_t feature_dim, bool batch_first)` — [`L419`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L419) — Expands a 2D timestep tensor [B, feature_dim] to a 3D singleton sequence
- <a id="ExtractLayer2D"></a>`ExtractLayer2D(mlir::MlirOp tensor_3d, int64_t layer_idx, int64_t batch, int64_t hidden)` — [`L396`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L396) — Extracts a 2D recurrent state slice [B, H] for layer `layer_idx` from the
- <a id="GetElementTypeEnum"></a>`GetElementTypeEnum(mlir::Type type)` — [`L504`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L504)
- <a id="GetStepActivation"></a>`GetStepActivation(mlir::MlirBuilder& builder, const std::vector<mlir::MlirOp>& list, mlir::MlirOp seq, const int64_t t, const int64_t batch, const int64_t feature_dim, const bool batch_first = false)` — [`L1860`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1860) — Slices an individual timestep activation from a sequence tensor if not
- `GetStepActivation(mlir::MlirBuilder& builder, const std::vector<mlir::MlirOp>& list, mlir::MlirOp seq, const int64_t t, const int64_t batch, const int64_t feature_dim, const bool batch_first = false)` — [`L1860`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1860) — Slices an individual timestep activation from a sequence tensor if not
- `LstmInputBackwardImpl(const at::Tensor& grad_output, const at::Tensor& grad_hy, const at::Tensor& grad_cy, const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const at::TensorList cached_activations, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys)` — [`L5160`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L5160) — =============================================================================
- <a id="LstmInputBackwardImpl"></a>`LstmInputBackwardImpl(const at::Tensor& grad_output, const at::Tensor& grad_hy, const at::Tensor& grad_cy, const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const at::TensorList cached_activations, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys)` — [`L5160`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L5160) — =============================================================================
- `LstmInputForwardCachedImpl(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys, std::optional<at::Tensor> rng_state = std::nullopt)` — [`L5711`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L5711) — Evaluates forward multi-layer recurrence while collecting and packing
- <a id="LstmInputForwardCachedImpl"></a>`LstmInputForwardCachedImpl(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys, std::optional<at::Tensor> rng_state = std::nullopt)` — [`L5711`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L5711) — Evaluates forward multi-layer recurrence while collecting and packing
- `LstmInputImpl(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys, std::optional<at::Tensor> rng_state = std::nullopt)` — [`L4737`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L4737) — =============================================================================
- <a id="LstmInputImpl"></a>`LstmInputImpl(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys, std::optional<at::Tensor> rng_state = std::nullopt)` — [`L4737`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L4737) — =============================================================================
- `MakeDotDims(mlir::MLIRContext* ctx, llvm::ArrayRef<int64_t> lhs_contracting, llvm::ArrayRef<int64_t> rhs_contracting)` — [`L375`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L375) — Constructs StableHLO DotDimensionNumbersAttr for matrix contractions.
- <a id="MakeDotDims"></a>`MakeDotDims(mlir::MLIRContext* ctx, llvm::ArrayRef<int64_t> lhs_contracting, llvm::ArrayRef<int64_t> rhs_contracting)` — [`L375`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L375) — Constructs StableHLO DotDimensionNumbersAttr for matrix contractions.
- <a id="MixedPrecisionDotGeneral"></a>`MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::Type acc_dtype, std::optional<mlir::Type> gemm_dtype, mlir::stablehlo::Precision precision)` — [`L517`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L517) — Evaluates DotGeneral with native mixed precision:
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::ElementType acc_dtype, std::optional<mlir::Type> gemm_dtype, mlir::stablehlo::Precision precision)` — [`L555`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L555)
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::Type acc_dtype, std::optional<mlir::Type> gemm_dtype, mlir::stablehlo::Precision precision)` — [`L517`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L517) — Evaluates DotGeneral with native mixed precision:
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::ElementType acc_dtype, std::optional<mlir::Type> gemm_dtype, mlir::stablehlo::Precision precision)` — [`L555`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L555)
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::Type acc_dtype, mlir::stablehlo::Precision precision)` — [`L565`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L565)
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::Type acc_dtype, mlir::stablehlo::Precision precision)` — [`L565`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L565)
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::ElementType acc_dtype, mlir::stablehlo::Precision precision)` — [`L573`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L573)
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::ElementType acc_dtype, mlir::stablehlo::Precision precision)` — [`L573`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L573)
- <a id="RecomputeLayerForward"></a>`RecomputeLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp layer_input_comp, mlir::MlirOp h_0_l, mlir::MlirOp c_0_l, mlir::MlirOp w_ih, mlir::MlirOp w_hh, std::optional<mlir::MlirOp> b_total, mlir::stablehlo::DotDimensionNumbersAttr ih_fwd_dot_dims, mlir::stablehlo::DotDimensionNumbersAttr hh_fwd_dot_dims, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t out_h, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, const bool batch_first, mlir::stablehlo::Precision precision)` — [`L1941`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1941) — Recomputes forward activations for layer l during backpropagation.
- `RecomputeLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp layer_input_comp, mlir::MlirOp h_0_l, mlir::MlirOp c_0_l, mlir::MlirOp w_ih, mlir::MlirOp w_hh, std::optional<mlir::MlirOp> b_total, mlir::stablehlo::DotDimensionNumbersAttr ih_fwd_dot_dims, mlir::stablehlo::DotDimensionNumbersAttr hh_fwd_dot_dims, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t out_h, std::optional<mlir::MlirOp> w_hr, std::optional<mlir::stablehlo::DotDimensionNumbersAttr> hr_dot_dims, const bool batch_first, mlir::stablehlo::Precision precision)` — [`L1941`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1941) — Recomputes forward activations for layer l during backpropagation.
- <a id="SliceStep2D"></a>`SliceStep2D(mlir::MlirOp seq_3d, int64_t t, int64_t batch, int64_t feature_dim, bool batch_first)` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L405) — Slices a 2D timestep [B, feature_dim] at step t from a 3D sequence tensor
- <a id="UnclumpBias3H"></a>`UnclumpBias3H(mlir::MlirBuilder& builder, mlir::MlirOp b, int64_t hidden)` — [`L491`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L491) — Permutes a 1D bias gradient vector [4*H] from [i, f, o, g] clumped order
- <a id="UnclumpWeight3H"></a>`UnclumpWeight3H(mlir::MlirBuilder& builder, mlir::MlirOp w, int64_t hidden, int64_t in_dim)` — [`L475`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L475) — Permutes a 2D weight gradient matrix [4*H, in_dim] from [i, f, o, g] clumped
- <a id="UnpackCachedActivations"></a>`UnpackCachedActivations(mlir::MlirOp pack_3d, int64_t seq_len, int64_t batch, int64_t hidden, int64_t out_h, bool batch_first)` — [`L1841`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L1841) — Unpacks cached activations packed across feature dimension (dim 2):
- <a id="ValidateLstmInputs"></a>`ValidateLstmInputs(const at::Tensor& input, const at::TensorList hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L333`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L333) — Master validation routine verifying sequence dimensions, batch sizes,
- <a id="ValidateLstmTensorShapes"></a>`ValidateLstmTensorShapes(const at::TensorList hx, const int64_t num_layers, const int64_t batch, const bool bidirectional = false)` — [`L203`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L203) — Validates that recurrent initial hidden state (h_0) and cell state (c_0)
- <a id="ValidateLstmWeights"></a>`ValidateLstmWeights(const at::TensorList params, const bool has_biases, const int64_t num_layers, const int64_t input_size, const int64_t hidden, const int64_t proj_size = 0, const bool bidirectional = false)` — [`L252`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L252) — Validates that weights and biases conform to PyTorch's parameter layout:

## Module values
- <a id="kLstmUnrollFactor"></a>`kLstmUnrollFactor` — [`L196`](../../../../../../../raw/code/torch_tpu/csrc/ops/lstm/lstm_aten_kernels.cc#L196) — Static unrolling factor kLstmUnrollFactor for chunked recurrent loop

