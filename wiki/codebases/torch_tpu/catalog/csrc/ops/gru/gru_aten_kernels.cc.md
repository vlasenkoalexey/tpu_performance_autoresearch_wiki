---
title: 'Module: csrc/ops/gru/gru_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/gru/gru_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GruInputBackwardImpl: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruInputBackwardImpl(748020315742c06).'
  AtenGruInputForwardCached: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/AtenGruInputForwardCached(3a2bf25562c779b9).'
  AtenGruInputForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/AtenGruInputForward(8de4c825a5857300).'
  kGruUnrollFactor: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/kGruUnrollFactor.'
  AtenGruInputBackward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/AtenGruInputBackward(e29d96902ad8f0a).'
  GruInputImpl: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruInputImpl(9ba97a5e26a9fa57).'
  ValidateGruWeights: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ValidateGruWeights(879fe14b58ee6557).'
  ComputeBidirLayerBackwardChunked: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeBidirLayerBackwardChunked(7e940b75ce4bdc53).'
  ConcatDim: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ConcatDim(6e7c76436169e8ad).'
  ComputeLayerByLayerBackwardStep: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeLayerByLayerBackwardStep(c478c6398316d366).'
  BuildGruBackwardShloGraph: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruBackwardShloGraph(a709eb2c7a2bb94b).'
  ValidateGruInputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ValidateGruInputs(22be081c21bf810c).'
  ComputeLayerBackwardChunked: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeLayerBackwardChunked(355dbc418a131ac2).'
  BuildGruForwardShloGraph: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruForwardShloGraph(d3a15d13f10677dc).'
  ExpandStep3D: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ExpandStep3D(8a89aec4339114aa).'
  BuildGruPipelinedWavefrontBackward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruPipelinedWavefrontBackward(be4212f4c9d60288).'
  BuildWavefrontForwardWhileBody: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildWavefrontForwardWhileBody(d6046b0f7cd37ee6).'
  ReconstructGruForwardPass: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ReconstructGruForwardPass(ce5528af2b0f2b35).'
  ExecuteGruForwardLayerStep: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ExecuteGruForwardLayerStep(b52a3489cf6e4407).'
  EvaluateWavefrontForwardChunkLayer: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/EvaluateWavefrontForwardChunkLayer(db30fe49582f3ecb).'
  ValidateGruTensorShapes: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ValidateGruTensorShapes(7ebaf2cfac8de798).'
  SliceStep2D: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/SliceStep2D(401f1bfb9044e5bc).'
  BuildWavefrontForwardRemainder: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildWavefrontForwardRemainder(c4f5ae66cf3d510).'
  ComputeBidirLayerBackwardStatic: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeBidirLayerBackwardStatic(565467712d95da35).'
  ComputeLayerBackwardStatic: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeLayerBackwardStatic(355dbc418a131ac2).'
  EvaluateWavefrontRemainderLayer: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/EvaluateWavefrontRemainderLayer(2d50d137f89efd18).'
  EvaluateWavefrontBackwardRemainderLayer: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/EvaluateWavefrontBackwardRemainderLayer(544f16b5f0790d27).'
  BuildGruLayerForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruLayerForward(5f86252118dab12d).'
  BuildWavefrontBackwardWhileBody: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildWavefrontBackwardWhileBody(75ff5dbef6a0ed56).'
  BuildBidirLayerBackwardChunkedWhileBody: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildBidirLayerBackwardChunkedWhileBody(7789ded68da27d3e).'
  BuildGruForwardWavefrontPath: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruForwardWavefrontPath(adac5550353dcb47).'
  BuildGruBidirChunkedForwardWhileBody: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruBidirChunkedForwardWhileBody(11cd4cdc4e0a06ff).'
  DispatchGruWavefrontBackwardPath: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/DispatchGruWavefrontBackwardPath(a16ebc2866348c05).'
  MixedPrecisionDotGeneral: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/MixedPrecisionDotGeneral(a80384b34d549af9).'
  ProcessWavefrontBackwardLayerChunk: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ProcessWavefrontBackwardLayerChunk(47214e21e79ce278).'
  BuildGruPipelinedWavefrontForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruPipelinedWavefrontForward(d896604c3547a7a2).'
  BuildLayerBackwardChunkedWhileBody: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildLayerBackwardChunkedWhileBody(9ae5b5e5704f0346).'
  FinalizeGruBidirForwardOutputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/FinalizeGruBidirForwardOutputs(a67b7d67dd2725b4).'
  ComputeBidirBackwardChunkSteps: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeBidirBackwardChunkSteps(3d3f87c499af97f).'
  ComputeGruBackwardChunkSteps: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeGruBackwardChunkSteps(153c79063aaa7634).'
  ComputeGruBackwardStep: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeGruBackwardStep(d7363b87970125b8).'
  RunGruForwardSteps: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/RunGruForwardSteps(f7a6e938f2d8e79).'
  ComputeBidirBackwardRemainder: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeBidirBackwardRemainder(28cef0651e457e83).'
  ComputeGruBackwardRemainder: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeGruBackwardRemainder(e6fa25d5e38a3e27).'
  BuildGruBidirChunkedForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruBidirChunkedForward(516a1adcbb9c9058).'
  BuildGruForwardRemainder: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruForwardRemainder(fa899bead121b27c).'
  BuildGruStaticForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruStaticForward(ca59fb8a01f436d1).'
  EvaluateGruUnidirLayerForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/EvaluateGruUnidirLayerForward(93d6c4629fe9eff5).'
  EvaluateGruBidirLayerForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/EvaluateGruBidirLayerForward(d3d889d25d5cdbc0).'
  AtenGruInputAutograd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/AtenGruInputAutograd#'
  GruBackwardStepResult.delta_pre_ig: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardStepResult#delta_pre_ig.'
  RunGruBidirForwardSteps: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/RunGruBidirForwardSteps(2727ea30a67fb6b3).'
  BuildGruBidirForwardRemainder: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruBidirForwardRemainder(d5683f54b489326d).'
  BuildGruBidirStaticForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruBidirStaticForward(f1a58616f69a4285).'
  ExtractLayer2D: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ExtractLayer2D(c8a45fb15a5a1e6e).'
  MakeDotDims: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/MakeDotDims(37c82e0c86549e0e).'
  ComputeGruForwardOutputLayouts: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeGruForwardOutputLayouts(ced8155c9cd6509b).'
  ComputeLayerBackward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeLayerBackward(2e52159716f2a001).'
  BuildGruBidirLayerForward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildGruBidirLayerForward(f1a58616f69a4285).'
  ComputeBidirLayerBackward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeBidirLayerBackward(7e940b75ce4bdc53).'
  GruBackwardStepResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardStepResult#'
  GruBackwardStepResult.delta_h_prev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardStepResult#delta_h_prev.'
  GruReconstructedForwardData.fwd_cached_acts: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruReconstructedForwardData#fwd_cached_acts.'
  BuildWavefrontBackwardRemainder: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildWavefrontBackwardRemainder(da3701f872337b37).'
  AtenGruInput: AtenGruInput(8de4c825a5857300).
  GruBackwardStepResult.delta_pre_hg: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardStepResult#delta_pre_hg.'
  ApplyInterLayerDropout: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ApplyInterLayerDropout(199cd4b07e16b7be).'
  ApplyDropoutBackward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ApplyDropoutBackward(523d68859211d53).'
  StackPerLayerFinalHiddenStates: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/StackPerLayerFinalHiddenStates(6ee759887a2f18d8).'
  AtenGruInputAutograd.forward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/AtenGruInputAutograd#forward(5d5a0ec29fc053ea).'
  AtenGruInputAutograd.backward: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/AtenGruInputAutograd#backward(305625f81d7e100).'
  GruLayerOutputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerOutputs#'
  BuildWavefrontHPrevSeq: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/BuildWavefrontHPrevSeq(20f996a918432fd4).'
  GruUnrolledForwardSteps: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruUnrolledForwardSteps#'
  GruStepResults: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruStepResults#'
  GruUnrolledForwardSteps.h_final: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruUnrolledForwardSteps#h_final.'
  GruStepResults.act_4h: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruStepResults#act_4h.'
  GruUnrolledForwardSteps.step_outputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruUnrolledForwardSteps#step_outputs.'
  GruStepResults.h_next: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruStepResults#h_next.'
  ApplyLayerDropoutStep: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ApplyLayerDropoutStep(61add758e6d6f6cc).'
  GruBidirLayerOutputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerOutputs#'
  InitWavefrontBackwardRemainderZero: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/InitWavefrontBackwardRemainderZero(4bb7cfa96e3bcb6c).'
  FinalizeWavefrontBackwardOutputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/FinalizeWavefrontBackwardOutputs(3673d1c24e70a14a).'
  GruOutputLayouts.dims_storage: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruOutputLayouts#dims_storage.'
  GruWavefrontLayerWeight: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruWavefrontLayerWeight#'
  FormatGruBackwardOutputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/FormatGruBackwardOutputs(64646e2bab178bbb).'
  GruReconstructedForwardData.layer_inputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruReconstructedForwardData#layer_inputs.'
  GruWavefrontLayerWeight.b_ih: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruWavefrontLayerWeight#b_ih.'
  GruReconstructedForwardData.layer_outputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruReconstructedForwardData#layer_outputs.'
  GruReconstructedForwardData: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruReconstructedForwardData#'
  GruWavefrontLayerWeight.w_hh: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruWavefrontLayerWeight#w_hh.'
  ComputeGruStep: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/ComputeGruStep(faf4865eb10a966b).'
  GruOutputLayouts.dtypes: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruOutputLayouts#dtypes.'
  GruReconstructedForwardData.dropout_masks: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruReconstructedForwardData#dropout_masks.'
  GruLayerBackwardOutputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerBackwardOutputs#'
  GruBidirLayerBackwardOutputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#'
  GruForwardLayerStepResult.cached_acts: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruForwardLayerStepResult#cached_acts.'
  GruBidirLayerOutputs.cached_acts_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerOutputs#cached_acts_fwd.'
  GruLayerOutputs.layer_output_seq: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerOutputs#layer_output_seq.'
  GruForwardLayerStepResult.final_h: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruForwardLayerStepResult#final_h.'
  GruForwardLayerStepResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruForwardLayerStepResult#'
  GruBidirLayerOutputs.layer_output_seq: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerOutputs#layer_output_seq.'
  GruForwardLayerStepResult.layer_output: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruForwardLayerStepResult#layer_output.'
  GruWavefrontLayerWeight.w_ih: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruWavefrontLayerWeight#w_ih.'
  GruMultiLayerBackwardOutputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruMultiLayerBackwardOutputs#'
  WavefrontBackwardRemainderResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderResult#'
  GruOutputLayouts: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruOutputLayouts#'
  GruUnrolledForwardSteps.step_acts: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruUnrolledForwardSteps#step_acts.'
  GruWavefrontLayerWeight.b_hh: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruWavefrontLayerWeight#b_hh.'
  GruBidirBackwardRemainderInit.grad_b_ih_init_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#grad_b_ih_init_fwd.'
  GruBidirBackwardRemainderInit.grad_w_hh_init_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#grad_w_hh_init_rev.'
  GruBidirBackwardRemainderInit.delta_h_next_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#delta_h_next_fwd.'
  WavefrontBackwardRemainderResult.rem_grad_b_ih_init: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderResult#rem_grad_b_ih_init.'
  GruBidirBackwardChunkStepsResult.delta_pre_ig_rev_chunk_2d: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#delta_pre_ig_rev_chunk_2d.'
  GruBackwardChunkStepsResult.delta_pre_hg_chunk_2d: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardChunkStepsResult#delta_pre_hg_chunk_2d.'
  GruLayerOutputs.final_h: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerOutputs#final_h.'
  GruBackwardRemainderInit.grad_b_hh_init: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardRemainderInit#grad_b_hh_init.'
  WavefrontBackwardRemainderResult.rem_grad_w_hh_init: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderResult#rem_grad_w_hh_init.'
  GruBackwardRemainderInit.delta_h_next: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardRemainderInit#delta_h_next.'
  GruBidirBackwardRemainderInit.grad_b_ih_init_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#grad_b_ih_init_rev.'
  GruBidirForwardRemainderResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirForwardRemainderResult#'
  GruBackwardChunkStepsResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardChunkStepsResult#'
  WavefrontRemainderLayerResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontRemainderLayerResult#'
  WavefrontLayerChunkBackwardResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontLayerChunkBackwardResult#'
  WavefrontBackwardRemainderResult.rem_delta_h: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderResult#rem_delta_h.'
  GruBidirBackwardChunkStepsResult.delta_pre_hg_fwd_chunk_2d: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#delta_pre_hg_fwd_chunk_2d.'
  GruBackwardRemainderInit.grad_b_ih_init: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardRemainderInit#grad_b_ih_init.'
  WavefrontBackwardRemainderResult.rem_grad_b_hh_init: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderResult#rem_grad_b_hh_init.'
  InterLayerDropoutResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/InterLayerDropoutResult#'
  GruBidirBackwardChunkStepsResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#'
  GruBackwardRemainderInit.grad_w_hh_init: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardRemainderInit#grad_w_hh_init.'
  GruBidirBackwardRemainderInit.grad_b_hh_init_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#grad_b_hh_init_fwd.'
  GruBackwardRemainderInit.grad_w_ih_init: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardRemainderInit#grad_w_ih_init.'
  GruBidirBackwardChunkStepsResult.delta_pre_ig_fwd_chunk_2d: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#delta_pre_ig_fwd_chunk_2d.'
  GruBidirStepsResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirStepsResult#'
  WavefrontForwardChunkLayerResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontForwardChunkLayerResult#'
  GruBidirBackwardChunkStepsResult.delta_pre_hg_rev_chunk_2d: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#delta_pre_hg_rev_chunk_2d.'
  GruBackwardChunkStepsResult.delta_pre_ig_chunk_2d: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardChunkStepsResult#delta_pre_ig_chunk_2d.'
  GruBackwardRemainderInit.rem_grad_x: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardRemainderInit#rem_grad_x.'
  GruBidirBackwardRemainderInit.grad_w_ih_init_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#grad_w_ih_init_fwd.'
  GruBackwardRemainderInit: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardRemainderInit#'
  GruBidirBackwardRemainderInit.grad_w_hh_init_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#grad_w_hh_init_fwd.'
  GruBidirBackwardRemainderInit.grad_w_ih_init_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#grad_w_ih_init_rev.'
  GruBidirBackwardRemainderInit: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#'
  GruBidirBackwardRemainderInit.delta_h_next_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#delta_h_next_rev.'
  WavefrontBackwardRemainderResult.rem_grad_w_ih_init: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderResult#rem_grad_w_ih_init.'
  GruBidirBackwardRemainderInit.rem_grad_x_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#rem_grad_x_fwd.'
  GruBidirLayerBackwardOutputs.grad_h0: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_h0.'
  GruBidirBackwardRemainderInit.grad_b_hh_init_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#grad_b_hh_init_rev.'
  GruLayerOutputs.cached_acts: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerOutputs#cached_acts.'
  GruBidirLayerOutputs.cached_acts_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerOutputs#cached_acts_rev.'
  GruBidirLayerBackwardOutputs.grad_w_ih_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_w_ih_fwd.'
  GruBidirForwardRemainderResult.final_seq_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirForwardRemainderResult#final_seq_rev.'
  WavefrontBackwardRemainderLayerResult: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderLayerResult#'
  GruLayerBackwardOutputs.grad_w_hh: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerBackwardOutputs#grad_w_hh.'
  GruMultiLayerBackwardOutputs.grad_x: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruMultiLayerBackwardOutputs#grad_x.'
  GruBidirLayerBackwardOutputs.grad_w_hh_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_w_hh_rev.'
  GruLayerBackwardOutputs.grad_h0: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerBackwardOutputs#grad_h0.'
  GruBidirLayerBackwardOutputs.grad_b_hh_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_b_hh_fwd.'
  GruBackwardChunkStepsResult.cur_delta_h_next: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardChunkStepsResult#cur_delta_h_next.'
  GruLayerBackwardOutputs.grad_w_ih: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerBackwardOutputs#grad_w_ih.'
  GruBackwardChunkStepsResult.chunk_grad_x: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBackwardChunkStepsResult#chunk_grad_x.'
  GruBidirBackwardChunkStepsResult.chunk_grad_x_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#chunk_grad_x_fwd.'
  WavefrontLayerChunkBackwardResult.next_delta_h_l: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontLayerChunkBackwardResult#next_delta_h_l.'
  WavefrontRemainderLayerResult.final_h_l: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontRemainderLayerResult#final_h_l.'
  WavefrontLayerChunkBackwardResult.chunk_gw_ih: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontLayerChunkBackwardResult#chunk_gw_ih.'
  GruBidirForwardRemainderResult.final_act_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirForwardRemainderResult#final_act_fwd.'
  WavefrontLayerChunkBackwardResult.chunk_gb_ih: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontLayerChunkBackwardResult#chunk_gb_ih.'
  GetElementTypeEnum: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GetElementTypeEnum(86763d29f90d7077).'
  GruBidirLayerBackwardOutputs.grad_b_hh_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_b_hh_rev.'
  GruBidirStepsResult.rev_chunk_outputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirStepsResult#rev_chunk_outputs.'
  WavefrontForwardChunkLayerResult.next_chunk: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontForwardChunkLayerResult#next_chunk.'
  GruBidirBackwardChunkStepsResult.chunk_grad_x_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#chunk_grad_x_rev.'
  GruBidirForwardRemainderResult.final_h_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirForwardRemainderResult#final_h_rev.'
  GruBidirForwardRemainderResult.final_act_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirForwardRemainderResult#final_act_rev.'
  GruBidirBackwardChunkStepsResult.cur_delta_h_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#cur_delta_h_fwd.'
  GruBidirLayerBackwardOutputs.grad_b_ih_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_b_ih_rev.'
  GruBidirLayerBackwardOutputs.grad_w_hh_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_w_hh_fwd.'
  GruBidirForwardRemainderResult.final_seq_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirForwardRemainderResult#final_seq_fwd.'
  GruMultiLayerBackwardOutputs.grad_h0: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruMultiLayerBackwardOutputs#grad_h0.'
  WavefrontLayerChunkBackwardResult.chunk_gb_hh: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontLayerChunkBackwardResult#chunk_gb_hh.'
  GruBidirStepsResult.h_next_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirStepsResult#h_next_rev.'
  GruBidirStepsResult.fwd_chunk_acts: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirStepsResult#fwd_chunk_acts.'
  GruBidirBackwardRemainderInit.rem_grad_x_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardRemainderInit#rem_grad_x_rev.'
  GruLayerBackwardOutputs.grad_b_ih: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerBackwardOutputs#grad_b_ih.'
  GruBidirStepsResult.h_next_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirStepsResult#h_next_fwd.'
  GruBidirStepsResult.rev_chunk_acts: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirStepsResult#rev_chunk_acts.'
  GruBidirForwardRemainderResult.final_h_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirForwardRemainderResult#final_h_fwd.'
  GruBidirLayerBackwardOutputs.grad_x: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_x.'
  WavefrontRemainderLayerResult.next_rem_seq: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontRemainderLayerResult#next_rem_seq.'
  GruBidirLayerBackwardOutputs.grad_w_ih_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_w_ih_rev.'
  GruBidirLayerOutputs.final_h: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerOutputs#final_h.'
  GruLayerBackwardOutputs.grad_x: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerBackwardOutputs#grad_x.'
  WavefrontForwardChunkLayerResult.next_h_l: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontForwardChunkLayerResult#next_h_l.'
  WavefrontLayerChunkBackwardResult.layer_grad_x: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontLayerChunkBackwardResult#layer_grad_x.'
  GruBidirStepsResult.fwd_chunk_outputs: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirStepsResult#fwd_chunk_outputs.'
  GruBidirBackwardChunkStepsResult.cur_delta_h_rev: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirBackwardChunkStepsResult#cur_delta_h_rev.'
  WavefrontLayerChunkBackwardResult.chunk_gw_hh: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontLayerChunkBackwardResult#chunk_gw_hh.'
  GruBidirLayerBackwardOutputs.grad_b_ih_fwd: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruBidirLayerBackwardOutputs#grad_b_ih_fwd.'
  GruStepResults.h_n: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruStepResults#h_n.'
  InterLayerDropoutResult.dropout_mask: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/InterLayerDropoutResult#dropout_mask.'
  GruStepResults.resetgate: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruStepResults#resetgate.'
  CollectGruInputTensors: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/CollectGruInputTensors(de7d9ce36d42a73c).'
  GruStepResults.updategate: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruStepResults#updategate.'
  WavefrontBackwardRemainderLayerResult.cur_delta_h: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderLayerResult#cur_delta_h.'
  InterLayerDropoutResult.dropped_output: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/InterLayerDropoutResult#dropped_output.'
  GruStepResults.newgate: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruStepResults#newgate.'
  WavefrontBackwardRemainderLayerResult.next_curr_rem_grad_y: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderLayerResult#next_curr_rem_grad_y.'
  GruMultiLayerBackwardOutputs.all_grad_params: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruMultiLayerBackwardOutputs#all_grad_params.'
  WavefrontBackwardRemainderResult.rem_grad_x_0: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/WavefrontBackwardRemainderResult#rem_grad_x_0.'
  GruLayerBackwardOutputs.grad_b_hh: '`$anonymous_namespace_csrc/ops/gru/gru_aten_kernels.cc`/GruLayerBackwardOutputs#grad_b_hh.'
---
# Module: [`csrc/ops/gru/gru_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc)

## Classes
### <a id="AtenGruInputAutograd"></a>`AtenGruInputAutograd`  ·  implements/extends Function
- def: [`csrc/ops/gru/gru_aten_kernels.cc:6962`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6962)
- doc: PyTorch Autograd Function integration for GRU.
- signature: `struct AtenGruInputAutograd : public torch::autograd::Function<AtenGruInputAutograd>`
- members:
  - `backward(torch::autograd::AutogradContext* ctx, torch::autograd::variable_list grad_outputs)` — [`L7012`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L7012) — Autograd backward implementation: unpacks saved variables, calls
  - <a id="AtenGruInputAutograd.backward"></a>`backward(torch::autograd::AutogradContext* ctx, torch::autograd::variable_list grad_outputs)` — [`L7012`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L7012) — Autograd backward implementation: unpacks saved variables, calls
  - `forward(torch::autograd::AutogradContext* ctx, const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6977`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6977) — Autograd forward implementation: executes cached forward pass and saves
  - <a id="AtenGruInputAutograd.forward"></a>`forward(torch::autograd::AutogradContext* ctx, const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6977`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6977) — Autograd forward implementation: executes cached forward pass and saves
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`AtenGruInputForwardCached`](gru_aten_kernels.cc.md#AtenGruInputForwardCached), [`AtenGruInputBackward`](gru_aten_kernels.cc.md#AtenGruInputBackward)
- used by: [`AtenGruInput`](gru_aten_kernels.cc.md#AtenGruInput)

### <a id="GruBackwardChunkStepsResult"></a>`GruBackwardChunkStepsResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:3139`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3139)
- doc: Container holding the adjoint pre-activations and input gradients for an
- signature: `struct GruBackwardChunkStepsResult`
- members:
  - <a id="GruBackwardChunkStepsResult.chunk_grad_x"></a>`chunk_grad_x` — [`L3143`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3143)
  - <a id="GruBackwardChunkStepsResult.cur_delta_h_next"></a>`cur_delta_h_next` — [`L3140`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3140)
  - <a id="GruBackwardChunkStepsResult.delta_pre_hg_chunk_2d"></a>`delta_pre_hg_chunk_2d` — [`L3142`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3142)
  - <a id="GruBackwardChunkStepsResult.delta_pre_ig_chunk_2d"></a>`delta_pre_ig_chunk_2d` — [`L3141`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3141)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildLayerBackwardChunkedWhileBody`](gru_aten_kernels.cc.md#BuildLayerBackwardChunkedWhileBody)

### <a id="GruBackwardRemainderInit"></a>`GruBackwardRemainderInit`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:2961`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2961)
- doc: Container holding initialized backward carry state and remainder gradients
- signature: `struct GruBackwardRemainderInit`
- members:
  - <a id="GruBackwardRemainderInit.delta_h_next"></a>`delta_h_next` — [`L2962`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2962)
  - <a id="GruBackwardRemainderInit.grad_b_hh_init"></a>`grad_b_hh_init` — [`L2966`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2966)
  - <a id="GruBackwardRemainderInit.grad_b_ih_init"></a>`grad_b_ih_init` — [`L2965`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2965)
  - <a id="GruBackwardRemainderInit.grad_w_hh_init"></a>`grad_w_hh_init` — [`L2964`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2964)
  - <a id="GruBackwardRemainderInit.grad_w_ih_init"></a>`grad_w_ih_init` — [`L2963`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2963)
  - <a id="GruBackwardRemainderInit.rem_grad_x"></a>`rem_grad_x` — [`L2967`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2967)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeLayerBackwardChunked`](gru_aten_kernels.cc.md#ComputeLayerBackwardChunked)

### <a id="GruBackwardStepResult"></a>`GruBackwardStepResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:698`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L698)
- doc: Container holding the adjoint gradients resulting from a single backward GRU
- signature: `struct GruBackwardStepResult`
- members:
  - <a id="GruBackwardStepResult.delta_h_prev"></a>`delta_h_prev` — [`L701`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L701)
  - <a id="GruBackwardStepResult.delta_pre_hg"></a>`delta_pre_hg` — [`L700`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L700)
  - <a id="GruBackwardStepResult.delta_pre_ig"></a>`delta_pre_ig` — [`L699`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L699)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeBidirLayerBackwardStatic`](gru_aten_kernels.cc.md#ComputeBidirLayerBackwardStatic), [`ComputeLayerBackwardStatic`](gru_aten_kernels.cc.md#ComputeLayerBackwardStatic), [`EvaluateWavefrontBackwardRemainderLayer`](gru_aten_kernels.cc.md#EvaluateWavefrontBackwardRemainderLayer), [`ProcessWavefrontBackwardLayerChunk`](gru_aten_kernels.cc.md#ProcessWavefrontBackwardLayerChunk), [`ComputeBidirBackwardChunkSteps`](gru_aten_kernels.cc.md#ComputeBidirBackwardChunkSteps), [`ComputeGruBackwardChunkSteps`](gru_aten_kernels.cc.md#ComputeGruBackwardChunkSteps), [`ComputeBidirBackwardRemainder`](gru_aten_kernels.cc.md#ComputeBidirBackwardRemainder), [`ComputeGruBackwardRemainder`](gru_aten_kernels.cc.md#ComputeGruBackwardRemainder)

### <a id="GruBidirBackwardChunkStepsResult"></a>`GruBidirBackwardChunkStepsResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:4191`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4191)
- doc: Intermediate result of executing kGruUnrollFactor backward steps concurrently
- signature: `struct GruBidirBackwardChunkStepsResult`
- members:
  - <a id="GruBidirBackwardChunkStepsResult.chunk_grad_x_fwd"></a>`chunk_grad_x_fwd` — [`L4198`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4198)
  - <a id="GruBidirBackwardChunkStepsResult.chunk_grad_x_rev"></a>`chunk_grad_x_rev` — [`L4199`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4199)
  - <a id="GruBidirBackwardChunkStepsResult.cur_delta_h_fwd"></a>`cur_delta_h_fwd` — [`L4192`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4192)
  - <a id="GruBidirBackwardChunkStepsResult.cur_delta_h_rev"></a>`cur_delta_h_rev` — [`L4193`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4193)
  - <a id="GruBidirBackwardChunkStepsResult.delta_pre_hg_fwd_chunk_2d"></a>`delta_pre_hg_fwd_chunk_2d` — [`L4195`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4195)
  - <a id="GruBidirBackwardChunkStepsResult.delta_pre_hg_rev_chunk_2d"></a>`delta_pre_hg_rev_chunk_2d` — [`L4197`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4197)
  - <a id="GruBidirBackwardChunkStepsResult.delta_pre_ig_fwd_chunk_2d"></a>`delta_pre_ig_fwd_chunk_2d` — [`L4194`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4194)
  - <a id="GruBidirBackwardChunkStepsResult.delta_pre_ig_rev_chunk_2d"></a>`delta_pre_ig_rev_chunk_2d` — [`L4196`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4196)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildBidirLayerBackwardChunkedWhileBody`](gru_aten_kernels.cc.md#BuildBidirLayerBackwardChunkedWhileBody)

### <a id="GruBidirBackwardRemainderInit"></a>`GruBidirBackwardRemainderInit`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:3925`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3925)
- doc: Result of evaluating tail remainder steps for bidirectional GRU backward
- signature: `struct GruBidirBackwardRemainderInit`
- members:
  - <a id="GruBidirBackwardRemainderInit.delta_h_next_fwd"></a>`delta_h_next_fwd` — [`L3926`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3926)
  - <a id="GruBidirBackwardRemainderInit.delta_h_next_rev"></a>`delta_h_next_rev` — [`L3927`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3927)
  - <a id="GruBidirBackwardRemainderInit.grad_b_hh_init_fwd"></a>`grad_b_hh_init_fwd` — [`L3931`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3931)
  - <a id="GruBidirBackwardRemainderInit.grad_b_hh_init_rev"></a>`grad_b_hh_init_rev` — [`L3935`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3935)
  - <a id="GruBidirBackwardRemainderInit.grad_b_ih_init_fwd"></a>`grad_b_ih_init_fwd` — [`L3930`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3930)
  - <a id="GruBidirBackwardRemainderInit.grad_b_ih_init_rev"></a>`grad_b_ih_init_rev` — [`L3934`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3934)
  - <a id="GruBidirBackwardRemainderInit.grad_w_hh_init_fwd"></a>`grad_w_hh_init_fwd` — [`L3929`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3929)
  - <a id="GruBidirBackwardRemainderInit.grad_w_hh_init_rev"></a>`grad_w_hh_init_rev` — [`L3933`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3933)
  - <a id="GruBidirBackwardRemainderInit.grad_w_ih_init_fwd"></a>`grad_w_ih_init_fwd` — [`L3928`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3928)
  - <a id="GruBidirBackwardRemainderInit.grad_w_ih_init_rev"></a>`grad_w_ih_init_rev` — [`L3932`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3932)
  - <a id="GruBidirBackwardRemainderInit.rem_grad_x_fwd"></a>`rem_grad_x_fwd` — [`L3936`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3936)
  - <a id="GruBidirBackwardRemainderInit.rem_grad_x_rev"></a>`rem_grad_x_rev` — [`L3937`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3937)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeBidirLayerBackwardChunked`](gru_aten_kernels.cc.md#ComputeBidirLayerBackwardChunked)

### <a id="GruBidirForwardRemainderResult"></a>`GruBidirForwardRemainderResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:2144`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2144)
- doc: Result container for bidirectional GRU remainder step evaluation.
- signature: `struct GruBidirForwardRemainderResult`
- members:
  - <a id="GruBidirForwardRemainderResult.final_act_fwd"></a>`final_act_fwd` — [`L2149`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2149)
  - <a id="GruBidirForwardRemainderResult.final_act_rev"></a>`final_act_rev` — [`L2150`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2150)
  - <a id="GruBidirForwardRemainderResult.final_h_fwd"></a>`final_h_fwd` — [`L2147`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2147)
  - <a id="GruBidirForwardRemainderResult.final_h_rev"></a>`final_h_rev` — [`L2148`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2148)
  - <a id="GruBidirForwardRemainderResult.final_seq_fwd"></a>`final_seq_fwd` — [`L2145`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2145)
  - <a id="GruBidirForwardRemainderResult.final_seq_rev"></a>`final_seq_rev` — [`L2146`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2146)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`FinalizeGruBidirForwardOutputs`](gru_aten_kernels.cc.md#FinalizeGruBidirForwardOutputs)

### <a id="GruBidirLayerBackwardOutputs"></a>`GruBidirLayerBackwardOutputs`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:2779`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2779)
- doc: Struct encapsulating backward outputs for a bidirectional layer.
- signature: `struct GruBidirLayerBackwardOutputs`
- members:
  - <a id="GruBidirLayerBackwardOutputs.grad_b_hh_fwd"></a>`grad_b_hh_fwd` — [`L2785`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2785)
  - <a id="GruBidirLayerBackwardOutputs.grad_b_hh_rev"></a>`grad_b_hh_rev` — [`L2789`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2789)
  - <a id="GruBidirLayerBackwardOutputs.grad_b_ih_fwd"></a>`grad_b_ih_fwd` — [`L2784`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2784)
  - <a id="GruBidirLayerBackwardOutputs.grad_b_ih_rev"></a>`grad_b_ih_rev` — [`L2788`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2788)
  - <a id="GruBidirLayerBackwardOutputs.grad_h0"></a>`grad_h0` — [`L2781`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2781)
  - <a id="GruBidirLayerBackwardOutputs.grad_w_hh_fwd"></a>`grad_w_hh_fwd` — [`L2783`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2783)
  - <a id="GruBidirLayerBackwardOutputs.grad_w_hh_rev"></a>`grad_w_hh_rev` — [`L2787`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2787)
  - <a id="GruBidirLayerBackwardOutputs.grad_w_ih_fwd"></a>`grad_w_ih_fwd` — [`L2782`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2782)
  - <a id="GruBidirLayerBackwardOutputs.grad_w_ih_rev"></a>`grad_w_ih_rev` — [`L2786`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2786)
  - <a id="GruBidirLayerBackwardOutputs.grad_x"></a>`grad_x` — [`L2780`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2780)
- uses (calls/refs, reference-scoped): [`GruLayerBackwardOutputs`](gru_aten_kernels.cc.md#GruLayerBackwardOutputs)
- used by: [`ComputeBidirLayerBackwardChunked`](gru_aten_kernels.cc.md#ComputeBidirLayerBackwardChunked), [`ComputeLayerByLayerBackwardStep`](gru_aten_kernels.cc.md#ComputeLayerByLayerBackwardStep), [`BuildBidirLayerBackwardChunkedWhileBody`](gru_aten_kernels.cc.md#BuildBidirLayerBackwardChunkedWhileBody), [`ComputeLayerBackward`](gru_aten_kernels.cc.md#ComputeLayerBackward)

### <a id="GruBidirLayerOutputs"></a>`GruBidirLayerOutputs`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:915`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L915)
- doc: Container holding the forward outputs of a bidirectional GRU layer.
- signature: `struct GruBidirLayerOutputs`
- members:
  - <a id="GruBidirLayerOutputs.cached_acts_fwd"></a>`cached_acts_fwd` — [`L918`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L918)
  - <a id="GruBidirLayerOutputs.cached_acts_rev"></a>`cached_acts_rev` — [`L919`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L919)
  - <a id="GruBidirLayerOutputs.final_h"></a>`final_h` — [`L917`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L917)
  - <a id="GruBidirLayerOutputs.layer_output_seq"></a>`layer_output_seq` — [`L916`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L916)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ExecuteGruForwardLayerStep`](gru_aten_kernels.cc.md#ExecuteGruForwardLayerStep), [`ReconstructGruForwardPass`](gru_aten_kernels.cc.md#ReconstructGruForwardPass), [`BuildGruBidirChunkedForwardWhileBody`](gru_aten_kernels.cc.md#BuildGruBidirChunkedForwardWhileBody), [`BuildGruPipelinedWavefrontForward`](gru_aten_kernels.cc.md#BuildGruPipelinedWavefrontForward), [`FinalizeGruBidirForwardOutputs`](gru_aten_kernels.cc.md#FinalizeGruBidirForwardOutputs), [`BuildGruBidirChunkedForward`](gru_aten_kernels.cc.md#BuildGruBidirChunkedForward), [`EvaluateGruUnidirLayerForward`](gru_aten_kernels.cc.md#EvaluateGruUnidirLayerForward)

### <a id="GruBidirStepsResult"></a>`GruBidirStepsResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:2026`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2026)
- doc: Result container for dual-directional chunk step unrolling.
- signature: `struct GruBidirStepsResult`
- members:
  - <a id="GruBidirStepsResult.fwd_chunk_acts"></a>`fwd_chunk_acts` — [`L2031`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2031)
  - <a id="GruBidirStepsResult.fwd_chunk_outputs"></a>`fwd_chunk_outputs` — [`L2029`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2029)
  - <a id="GruBidirStepsResult.h_next_fwd"></a>`h_next_fwd` — [`L2027`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2027)
  - <a id="GruBidirStepsResult.h_next_rev"></a>`h_next_rev` — [`L2028`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2028)
  - <a id="GruBidirStepsResult.rev_chunk_acts"></a>`rev_chunk_acts` — [`L2032`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2032)
  - <a id="GruBidirStepsResult.rev_chunk_outputs"></a>`rev_chunk_outputs` — [`L2030`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2030)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildGruBidirChunkedForwardWhileBody`](gru_aten_kernels.cc.md#BuildGruBidirChunkedForwardWhileBody)

### <a id="GruForwardLayerStepResult"></a>`GruForwardLayerStepResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:5902`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5902)
- doc: Result of evaluating a single layer forward step.
- signature: `struct GruForwardLayerStepResult`
- members:
  - <a id="GruForwardLayerStepResult.cached_acts"></a>`cached_acts` — [`L5905`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5905)
  - <a id="GruForwardLayerStepResult.final_h"></a>`final_h` — [`L5904`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5904)
  - <a id="GruForwardLayerStepResult.layer_output"></a>`layer_output` — [`L5903`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5903)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildGruForwardShloGraph`](gru_aten_kernels.cc.md#BuildGruForwardShloGraph), [`ExecuteGruForwardLayerStep`](gru_aten_kernels.cc.md#ExecuteGruForwardLayerStep)

### <a id="GruLayerBackwardOutputs"></a>`GruLayerBackwardOutputs`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:2749`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2749)
- doc: Struct encapsulating backward outputs for a single unidirectional layer.
- signature: `struct GruLayerBackwardOutputs`
- members:
  - <a id="GruLayerBackwardOutputs.grad_b_hh"></a>`grad_b_hh` — [`L2755`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2755)
  - <a id="GruLayerBackwardOutputs.grad_b_ih"></a>`grad_b_ih` — [`L2754`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2754)
  - <a id="GruLayerBackwardOutputs.grad_h0"></a>`grad_h0` — [`L2751`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2751)
  - <a id="GruLayerBackwardOutputs.grad_w_hh"></a>`grad_w_hh` — [`L2753`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2753)
  - <a id="GruLayerBackwardOutputs.grad_w_ih"></a>`grad_w_ih` — [`L2752`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2752)
  - <a id="GruLayerBackwardOutputs.grad_x"></a>`grad_x` — [`L2750`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2750)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeLayerByLayerBackwardStep`](gru_aten_kernels.cc.md#ComputeLayerByLayerBackwardStep), [`ComputeLayerBackwardChunked`](gru_aten_kernels.cc.md#ComputeLayerBackwardChunked), [`BuildLayerBackwardChunkedWhileBody`](gru_aten_kernels.cc.md#BuildLayerBackwardChunkedWhileBody), [`grad_b_hh_rev`](gru_aten_kernels.cc.md#GruBidirLayerBackwardOutputs.grad_b_hh_rev)

### <a id="GruLayerOutputs"></a>`GruLayerOutputs`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:898`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L898)
- doc: Container holding the forward outputs of a unidirectional GRU layer.
- signature: `struct GruLayerOutputs`
- members:
  - <a id="GruLayerOutputs.cached_acts"></a>`cached_acts` — [`L901`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L901)
  - <a id="GruLayerOutputs.final_h"></a>`final_h` — [`L900`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L900)
  - <a id="GruLayerOutputs.layer_output_seq"></a>`layer_output_seq` — [`L899`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L899)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildGruPipelinedWavefrontBackward`](gru_aten_kernels.cc.md#BuildGruPipelinedWavefrontBackward), [`BuildWavefrontForwardWhileBody`](gru_aten_kernels.cc.md#BuildWavefrontForwardWhileBody), [`ExecuteGruForwardLayerStep`](gru_aten_kernels.cc.md#ExecuteGruForwardLayerStep), [`ReconstructGruForwardPass`](gru_aten_kernels.cc.md#ReconstructGruForwardPass), [`BuildGruForwardWavefrontPath`](gru_aten_kernels.cc.md#BuildGruForwardWavefrontPath), [`RunGruForwardSteps`](gru_aten_kernels.cc.md#RunGruForwardSteps), [`BuildGruForwardRemainder`](gru_aten_kernels.cc.md#BuildGruForwardRemainder), [`BuildGruStaticForward`](gru_aten_kernels.cc.md#BuildGruStaticForward), [`StackPerLayerFinalHiddenStates`](gru_aten_kernels.cc.md#StackPerLayerFinalHiddenStates)

### <a id="GruMultiLayerBackwardOutputs"></a>`GruMultiLayerBackwardOutputs`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:4905`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4905)
- doc: Container holding all gradient outputs for a multi-layer GRU backward pass.
- signature: `struct GruMultiLayerBackwardOutputs`
- members:
  - <a id="GruMultiLayerBackwardOutputs.all_grad_params"></a>`all_grad_params` — [`L4909`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4909) — Parameter gradients [W_ih,
  - <a id="GruMultiLayerBackwardOutputs.grad_h0"></a>`grad_h0` — [`L4908`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4908) — Initial hidden states gradient [num_layers, B, hidden].
  - <a id="GruMultiLayerBackwardOutputs.grad_x"></a>`grad_x` — [`L4906`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4906) — Input gradient tensor [T, B, input_size].
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildWavefrontBackwardWhileBody`](gru_aten_kernels.cc.md#BuildWavefrontBackwardWhileBody), [`DispatchGruWavefrontBackwardPath`](gru_aten_kernels.cc.md#DispatchGruWavefrontBackwardPath), [`FinalizeWavefrontBackwardOutputs`](gru_aten_kernels.cc.md#FinalizeWavefrontBackwardOutputs)

### <a id="GruOutputLayouts"></a>`GruOutputLayouts`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:6115`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6115)
- doc: Layout configuration of output tensors.
- signature: `struct GruOutputLayouts`
- members:
  - <a id="GruOutputLayouts.dims_storage"></a>`dims_storage` — [`L6117`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6117)
  - <a id="GruOutputLayouts.dtypes"></a>`dtypes` — [`L6116`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6116)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`GruInputImpl`](gru_aten_kernels.cc.md#GruInputImpl), [`ComputeGruForwardOutputLayouts`](gru_aten_kernels.cc.md#ComputeGruForwardOutputLayouts)

### <a id="GruReconstructedForwardData"></a>`GruReconstructedForwardData`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:6241`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6241)
- doc: Reconstructed forward data required by backward pass.
- signature: `struct GruReconstructedForwardData`
- members:
  - <a id="GruReconstructedForwardData.dropout_masks"></a>`dropout_masks` — [`L6245`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6245)
  - <a id="GruReconstructedForwardData.fwd_cached_acts"></a>`fwd_cached_acts` — [`L6244`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6244)
  - <a id="GruReconstructedForwardData.layer_inputs"></a>`layer_inputs` — [`L6242`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6242)
  - <a id="GruReconstructedForwardData.layer_outputs"></a>`layer_outputs` — [`L6243`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6243)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ComputeLayerByLayerBackwardStep`](gru_aten_kernels.cc.md#ComputeLayerByLayerBackwardStep), [`BuildGruBackwardShloGraph`](gru_aten_kernels.cc.md#BuildGruBackwardShloGraph), [`ReconstructGruForwardPass`](gru_aten_kernels.cc.md#ReconstructGruForwardPass), [`DispatchGruWavefrontBackwardPath`](gru_aten_kernels.cc.md#DispatchGruWavefrontBackwardPath)

### <a id="GruStepResults"></a>`GruStepResults`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:587`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L587)
- doc: Container holding the intermediate and final outputs of a single GRU forward
- signature: `struct GruStepResults`
- members:
  - <a id="GruStepResults.act_4h"></a>`act_4h` — [`L593`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L593)
  - <a id="GruStepResults.h_n"></a>`h_n` — [`L592`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L592)
  - <a id="GruStepResults.h_next"></a>`h_next` — [`L588`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L588)
  - <a id="GruStepResults.newgate"></a>`newgate` — [`L591`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L591)
  - <a id="GruStepResults.resetgate"></a>`resetgate` — [`L589`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L589)
  - <a id="GruStepResults.updategate"></a>`updategate` — [`L590`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L590)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`RunGruForwardSteps`](gru_aten_kernels.cc.md#RunGruForwardSteps), [`BuildGruBidirForwardRemainder`](gru_aten_kernels.cc.md#BuildGruBidirForwardRemainder), [`BuildGruBidirStaticForward`](gru_aten_kernels.cc.md#BuildGruBidirStaticForward), [`RunGruBidirForwardSteps`](gru_aten_kernels.cc.md#RunGruBidirForwardSteps)

### <a id="GruUnrolledForwardSteps"></a>`GruUnrolledForwardSteps`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:932`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L932)
- doc: Helper struct capturing the outputs of a series of unrolled GRU forward
- signature: `struct GruUnrolledForwardSteps`
- members:
  - <a id="GruUnrolledForwardSteps.h_final"></a>`h_final` — [`L933`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L933)
  - <a id="GruUnrolledForwardSteps.step_acts"></a>`step_acts` — [`L935`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L935)
  - <a id="GruUnrolledForwardSteps.step_outputs"></a>`step_outputs` — [`L934`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L934)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildWavefrontForwardWhileBody`](gru_aten_kernels.cc.md#BuildWavefrontForwardWhileBody), [`EvaluateWavefrontForwardChunkLayer`](gru_aten_kernels.cc.md#EvaluateWavefrontForwardChunkLayer), [`BuildWavefrontForwardRemainder`](gru_aten_kernels.cc.md#BuildWavefrontForwardRemainder), [`BuildGruLayerForward`](gru_aten_kernels.cc.md#BuildGruLayerForward), [`EvaluateWavefrontRemainderLayer`](gru_aten_kernels.cc.md#EvaluateWavefrontRemainderLayer), [`BuildGruForwardRemainder`](gru_aten_kernels.cc.md#BuildGruForwardRemainder), [`BuildGruStaticForward`](gru_aten_kernels.cc.md#BuildGruStaticForward)

### <a id="GruWavefrontLayerWeight"></a>`GruWavefrontLayerWeight`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:883`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L883)
- doc: Weight and bias containers for a single layer in pipelined wavefront
- signature: `struct GruWavefrontLayerWeight`
- members:
  - <a id="GruWavefrontLayerWeight.b_hh"></a>`b_hh` — [`L887`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L887)
  - <a id="GruWavefrontLayerWeight.b_ih"></a>`b_ih` — [`L886`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L886)
  - <a id="GruWavefrontLayerWeight.w_hh"></a>`w_hh` — [`L884`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L884)
  - <a id="GruWavefrontLayerWeight.w_ih"></a>`w_ih` — [`L885`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L885)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildWavefrontForwardWhileBody`](gru_aten_kernels.cc.md#BuildWavefrontForwardWhileBody), [`EvaluateWavefrontForwardChunkLayer`](gru_aten_kernels.cc.md#EvaluateWavefrontForwardChunkLayer), [`BuildWavefrontForwardRemainder`](gru_aten_kernels.cc.md#BuildWavefrontForwardRemainder), [`EvaluateWavefrontRemainderLayer`](gru_aten_kernels.cc.md#EvaluateWavefrontRemainderLayer), [`BuildGruForwardWavefrontPath`](gru_aten_kernels.cc.md#BuildGruForwardWavefrontPath), [`BuildGruPipelinedWavefrontForward`](gru_aten_kernels.cc.md#BuildGruPipelinedWavefrontForward)

### <a id="InterLayerDropoutResult"></a>`InterLayerDropoutResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:814`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L814)
- doc: Applies inverted dropout between stacked recurrent layers during the forward
- signature: `struct InterLayerDropoutResult`
- members:
  - <a id="InterLayerDropoutResult.dropout_mask"></a>`dropout_mask` — [`L816`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L816)
  - <a id="InterLayerDropoutResult.dropped_output"></a>`dropped_output` — [`L815`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L815)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`EvaluateGruBidirLayerForward`](gru_aten_kernels.cc.md#EvaluateGruBidirLayerForward)

### <a id="WavefrontBackwardRemainderLayerResult"></a>`WavefrontBackwardRemainderLayerResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:4970`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4970)
- doc: Computes remainder backward pass across layers when rem_steps > 0.
- signature: `struct WavefrontBackwardRemainderLayerResult`
- members:
  - <a id="WavefrontBackwardRemainderLayerResult.cur_delta_h"></a>`cur_delta_h` — [`L4971`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4971)
  - <a id="WavefrontBackwardRemainderLayerResult.next_curr_rem_grad_y"></a>`next_curr_rem_grad_y` — [`L4972`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4972)
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="WavefrontBackwardRemainderResult"></a>`WavefrontBackwardRemainderResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:4915`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4915)
- doc: Container holding the initialized accumulators and carry states computed
- signature: `struct WavefrontBackwardRemainderResult`
- members:
  - <a id="WavefrontBackwardRemainderResult.rem_delta_h"></a>`rem_delta_h` — [`L4920`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4920)
  - <a id="WavefrontBackwardRemainderResult.rem_grad_b_hh_init"></a>`rem_grad_b_hh_init` — [`L4919`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4919)
  - <a id="WavefrontBackwardRemainderResult.rem_grad_b_ih_init"></a>`rem_grad_b_ih_init` — [`L4918`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4918)
  - <a id="WavefrontBackwardRemainderResult.rem_grad_w_hh_init"></a>`rem_grad_w_hh_init` — [`L4917`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4917)
  - <a id="WavefrontBackwardRemainderResult.rem_grad_w_ih_init"></a>`rem_grad_w_ih_init` — [`L4916`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4916)
  - <a id="WavefrontBackwardRemainderResult.rem_grad_x_0"></a>`rem_grad_x_0` — [`L4921`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4921)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildGruPipelinedWavefrontBackward`](gru_aten_kernels.cc.md#BuildGruPipelinedWavefrontBackward), [`EvaluateWavefrontBackwardRemainderLayer`](gru_aten_kernels.cc.md#EvaluateWavefrontBackwardRemainderLayer), [`InitWavefrontBackwardRemainderZero`](gru_aten_kernels.cc.md#InitWavefrontBackwardRemainderZero)

### <a id="WavefrontForwardChunkLayerResult"></a>`WavefrontForwardChunkLayerResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:1616`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1616)
- doc: Evaluates a chunk of k=8 timesteps for a single subsequent layer l (l >= 1)
- signature: `struct WavefrontForwardChunkLayerResult`
- members:
  - <a id="WavefrontForwardChunkLayerResult.next_chunk"></a>`next_chunk` — [`L1618`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1618)
  - <a id="WavefrontForwardChunkLayerResult.next_h_l"></a>`next_h_l` — [`L1617`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1617)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildWavefrontForwardWhileBody`](gru_aten_kernels.cc.md#BuildWavefrontForwardWhileBody)

### <a id="WavefrontLayerChunkBackwardResult"></a>`WavefrontLayerChunkBackwardResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:5190`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5190)
- doc: Result of evaluating a single layer's chunk backward execution in the
- signature: `struct WavefrontLayerChunkBackwardResult`
- members:
  - <a id="WavefrontLayerChunkBackwardResult.chunk_gb_hh"></a>`chunk_gb_hh` — [`L5196`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5196)
  - <a id="WavefrontLayerChunkBackwardResult.chunk_gb_ih"></a>`chunk_gb_ih` — [`L5195`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5195)
  - <a id="WavefrontLayerChunkBackwardResult.chunk_gw_hh"></a>`chunk_gw_hh` — [`L5194`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5194)
  - <a id="WavefrontLayerChunkBackwardResult.chunk_gw_ih"></a>`chunk_gw_ih` — [`L5193`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5193)
  - <a id="WavefrontLayerChunkBackwardResult.layer_grad_x"></a>`layer_grad_x` — [`L5192`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5192)
  - <a id="WavefrontLayerChunkBackwardResult.next_delta_h_l"></a>`next_delta_h_l` — [`L5191`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5191)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildWavefrontBackwardWhileBody`](gru_aten_kernels.cc.md#BuildWavefrontBackwardWhileBody)

### <a id="WavefrontRemainderLayerResult"></a>`WavefrontRemainderLayerResult`
- def: [`csrc/ops/gru/gru_aten_kernels.cc:1420`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1420)
- doc: Evaluates wavefront remainder steps across all layers when seq_len %
- signature: `struct WavefrontRemainderLayerResult`
- members:
  - <a id="WavefrontRemainderLayerResult.final_h_l"></a>`final_h_l` — [`L1421`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1421)
  - <a id="WavefrontRemainderLayerResult.next_rem_seq"></a>`next_rem_seq` — [`L1422`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1422)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildWavefrontForwardRemainder`](gru_aten_kernels.cc.md#BuildWavefrontForwardRemainder)

## Functions
- <a id="ApplyDropoutBackward"></a>`ApplyDropoutBackward(mlir::MlirOp grad_output, mlir::MlirOp mask, double dropout)` — [`L860`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L860) — Applies the adjoint backward pass of inverted dropout to upstream gradients.
- <a id="ApplyInterLayerDropout"></a>`ApplyInterLayerDropout(mlir::MlirOp layer_out, mlir::MlirOp rand_tensor, double dropout)` — [`L819`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L819)
- <a id="ApplyLayerDropoutStep"></a>`ApplyLayerDropoutStep(mlir::MlirOp current_layer_out, mlir::MlirOp rand_op, const int64_t l, const int64_t batch, const int64_t seq_len, const int64_t out_dim, const bool batch_first, const double dropout)` — [`L5829`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5829) — Applies inter-layer dropout between stacked recurrent layers.
- <a id="AtenGruInput"></a>`AtenGruInput(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L7090`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L7090) — Top-level public ATen operator for GRU execution on TPU.
- `AtenGruInputBackward(const at::Tensor& grad_output, const at::Tensor& grad_hy, const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, const at::TensorList cached_activations)` — [`L6929`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6929) — ATen entry point for GRU backward pass.
- <a id="AtenGruInputBackward"></a>`AtenGruInputBackward(const at::Tensor& grad_output, const at::Tensor& grad_hy, const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, const at::TensorList cached_activations)` — [`L6929`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6929) — ATen entry point for GRU backward pass.
- <a id="AtenGruInputForward"></a>`AtenGruInputForward(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6782`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6782) — ATen entry point for GRU forward pass without autograd activation caching.
- `AtenGruInputForwardCached(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6845`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6845) — ATen entry point for GRU forward pass with activation caching for autograd
- <a id="AtenGruInputForwardCached"></a>`AtenGruInputForwardCached(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L6845`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6845) — ATen entry point for GRU forward pass with activation caching for autograd
- `BuildBidirLayerBackwardChunkedWhileBody` — [`L4380`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4380) — Computes the chunked recurrence backward pass for a bidirectional GRU layer
- <a id="BuildBidirLayerBackwardChunkedWhileBody"></a>`BuildBidirLayerBackwardChunkedWhileBody` — [`L4380`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4380) — Computes the chunked recurrence backward pass for a bidirectional GRU layer
- `BuildGruBackwardShloGraph(absl::Span<mlir::MlirOp> builder_inputs, mlir::MlirBuilder& builder, const int64_t batch, const int64_t seq_len, const int64_t hidden, const int64_t input_size, const bool has_biases, const int64_t num_layers, const double dropout, const bool bidirectional, const int64_t num_directions, const bool batch_first, const mlir::ElementType out_dtype, const mlir::ElementType acc_dtype, const size_t params_per_layer, const size_t params_per_direction, const bool has_dropout, const mlir::stablehlo::Precision current_precision)` — [`L6560`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6560) — Builds the complete StableHLO computational graph for multi-layer GRU
- <a id="BuildGruBackwardShloGraph"></a>`BuildGruBackwardShloGraph(absl::Span<mlir::MlirOp> builder_inputs, mlir::MlirBuilder& builder, const int64_t batch, const int64_t seq_len, const int64_t hidden, const int64_t input_size, const bool has_biases, const int64_t num_layers, const double dropout, const bool bidirectional, const int64_t num_directions, const bool batch_first, const mlir::ElementType out_dtype, const mlir::ElementType acc_dtype, const size_t params_per_layer, const size_t params_per_direction, const bool has_dropout, const mlir::stablehlo::Precision current_precision)` — [`L6560`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6560) — Builds the complete StableHLO computational graph for multi-layer GRU
- `BuildGruBidirChunkedForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const int64_t seq_len, const int64_t batch, const int64_t hidden, const bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, const mlir::stablehlo::Precision precision, const bool cache_activations)` — [`L2557`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2557) — Builds a bidirectional GRU forward layer using chunked recurrence inside a
- <a id="BuildGruBidirChunkedForward"></a>`BuildGruBidirChunkedForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const int64_t seq_len, const int64_t batch, const int64_t hidden, const bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, const mlir::stablehlo::Precision precision, const bool cache_activations)` — [`L2557`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2557) — Builds a bidirectional GRU forward layer using chunked recurrence inside a
- <a id="BuildGruBidirChunkedForwardWhileBody"></a>`BuildGruBidirChunkedForwardWhileBody(mlir::MlirBuilder& builder, mlir::Block* body_block, mlir::Location loc, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t chunked_steps, int64_t batch, int64_t hidden, bool batch_first, int64_t concat_dim, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L2341`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2341) — Builds a bidirectional GRU forward layer using chunked recurrence inside a
- `BuildGruBidirChunkedForwardWhileBody(mlir::MlirBuilder& builder, mlir::Block* body_block, mlir::Location loc, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t chunked_steps, int64_t batch, int64_t hidden, bool batch_first, int64_t concat_dim, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L2341`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2341) — Builds a bidirectional GRU forward layer using chunked recurrence inside a
- <a id="BuildGruBidirForwardRemainder"></a>`BuildGruBidirForwardRemainder` — [`L2194`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2194) — Computes tail remainder steps (seq_len % kGruUnrollFactor) for bidirectional
- `BuildGruBidirForwardRemainder` — [`L2194`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2194) — Computes tail remainder steps (seq_len % kGruUnrollFactor) for bidirectional
- <a id="BuildGruBidirLayerForward"></a>`BuildGruBidirLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L2716`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2716) — Dispatcher for bidirectional GRU layer forward evaluation.
- `BuildGruBidirLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L2716`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2716) — Dispatcher for bidirectional GRU layer forward evaluation.
- `BuildGruBidirStaticForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L1939`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1939) — Builds a static forward sweep for bidirectional GRU for short sequences
- <a id="BuildGruBidirStaticForward"></a>`BuildGruBidirStaticForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_fwd, mlir::MlirOp x_proj_rev, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L1939`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1939) — Builds a static forward sweep for bidirectional GRU for short sequences
- <a id="BuildGruForwardRemainder"></a>`BuildGruForwardRemainder(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp chunked_y, mlir::MlirOp final_loop_h, std::optional<mlir::MlirOp> chunked_act, int64_t chunked_steps, int64_t rem_steps, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L1097`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1097) — Evaluates the tail remainder steps (seq_len % kGruUnrollFactor) following
- `BuildGruForwardRemainder(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp chunked_y, mlir::MlirOp final_loop_h, std::optional<mlir::MlirOp> chunked_act, int64_t chunked_steps, int64_t rem_steps, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L1097`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1097) — Evaluates the tail remainder steps (seq_len % kGruUnrollFactor) following
- `BuildGruForwardShloGraph(absl::Span<mlir::MlirOp> builder_inputs, mlir::MlirBuilder& builder, const bool has_biases, const int64_t num_layers, const bool batch_first, const int64_t batch, const int64_t seq_len, const int64_t hidden, const mlir::ElementType out_dtype, const mlir::ElementType acc_dtype, const size_t params_per_layer, const bool bidirectional, const int64_t num_directions, const size_t params_per_direction, const bool has_dropout, const double dropout, const bool train, const bool cache_activations, const mlir::stablehlo::Precision current_precision)` — [`L6002`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6002) — Builds the complete StableHLO computational graph for multi-layer GRU forward
- <a id="BuildGruForwardShloGraph"></a>`BuildGruForwardShloGraph(absl::Span<mlir::MlirOp> builder_inputs, mlir::MlirBuilder& builder, const bool has_biases, const int64_t num_layers, const bool batch_first, const int64_t batch, const int64_t seq_len, const int64_t hidden, const mlir::ElementType out_dtype, const mlir::ElementType acc_dtype, const size_t params_per_layer, const bool bidirectional, const int64_t num_directions, const size_t params_per_direction, const bool has_dropout, const double dropout, const bool train, const bool cache_activations, const mlir::stablehlo::Precision current_precision)` — [`L6002`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6002) — Builds the complete StableHLO computational graph for multi-layer GRU forward
- <a id="BuildGruForwardWavefrontPath"></a>`BuildGruForwardWavefrontPath` — [`L5850`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5850) — Builds pipelined wavefront forward path for multi-layer unidirectional GRU.
- `BuildGruForwardWavefrontPath` — [`L5850`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5850) — Builds pipelined wavefront forward path for multi-layer unidirectional GRU.
- <a id="BuildGruLayerForward"></a>`BuildGruLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp h_init, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L1176`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1176) — Builds a unidirectional GRU forward layer using chunked static unrolling
- `BuildGruLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp h_init, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L1176`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1176) — Builds a unidirectional GRU forward layer using chunked static unrolling
- `BuildGruPipelinedWavefrontBackward` — [`L5546`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5546) — Builds pipelined wavefront backward pass for multi-layer unidirectional GRU.
- <a id="BuildGruPipelinedWavefrontBackward"></a>`BuildGruPipelinedWavefrontBackward` — [`L5546`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5546) — Builds pipelined wavefront backward pass for multi-layer unidirectional GRU.
- <a id="BuildGruPipelinedWavefrontForward"></a>`BuildGruPipelinedWavefrontForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_0, const absl::Span<const mlir::MlirOp> h_inits, const absl::Span<const GruWavefrontLayerWeight> layer_weights, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t num_layers, const bool batch_first, ToOutFn to_out, const double dropout, const bool train, std::optional<mlir::MlirOp> rand_op, const mlir::stablehlo::Precision precision)` — [`L1798`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1798) — Builds a pipelined wavefront forward pass across stacked recurrent layers (L
- `BuildGruPipelinedWavefrontForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_0, const absl::Span<const mlir::MlirOp> h_inits, const absl::Span<const GruWavefrontLayerWeight> layer_weights, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t num_layers, const bool batch_first, ToOutFn to_out, const double dropout, const bool train, std::optional<mlir::MlirOp> rand_op, const mlir::stablehlo::Precision precision)` — [`L1798`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1798) — Builds a pipelined wavefront forward pass across stacked recurrent layers (L
- <a id="BuildGruStaticForward"></a>`BuildGruStaticForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp h_init, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L1040`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1040) — Builds a static unrolled forward sweep for short sequences (seq_len <
- `BuildGruStaticForward(mlir::MlirBuilder& builder, mlir::MlirOp x_proj, mlir::MlirOp h_init, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L1040`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1040) — Builds a static unrolled forward sweep for short sequences (seq_len <
- `BuildLayerBackwardChunkedWhileBody(mlir::MlirBuilder& builder, mlir::Block* body_block, mlir::Location loc, mlir::MlirOp grad_y, mlir::MlirOp act_4h_seq, mlir::MlirOp h_prev_seq, mlir::MlirOp layer_in, mlir::MlirOp w_hh, mlir::MlirOp w_ih, const mlir::stablehlo::DotDimensionNumbersAttr hh_bwd_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr x_bwd_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr w_dot_dims, int64_t chunked_steps, int64_t batch, int64_t hidden, int64_t in_dim, bool batch_first, int64_t concat_dim, mlir::Type acc_dtype, mlir::MlirOp one, bool has_biases, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, mlir::stablehlo::Precision precision)` — [`L3307`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3307) — Computes chunked reverse BPTT backward pass for a single unidirectional GRU
- <a id="BuildLayerBackwardChunkedWhileBody"></a>`BuildLayerBackwardChunkedWhileBody(mlir::MlirBuilder& builder, mlir::Block* body_block, mlir::Location loc, mlir::MlirOp grad_y, mlir::MlirOp act_4h_seq, mlir::MlirOp h_prev_seq, mlir::MlirOp layer_in, mlir::MlirOp w_hh, mlir::MlirOp w_ih, const mlir::stablehlo::DotDimensionNumbersAttr hh_bwd_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr x_bwd_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr w_dot_dims, int64_t chunked_steps, int64_t batch, int64_t hidden, int64_t in_dim, bool batch_first, int64_t concat_dim, mlir::Type acc_dtype, mlir::MlirOp one, bool has_biases, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, mlir::stablehlo::Precision precision)` — [`L3307`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3307) — Computes chunked reverse BPTT backward pass for a single unidirectional GRU
- `BuildWavefrontBackwardRemainder` — [`L5135`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5135) — Computes remainder backward pass across layers when rem_steps > 0.
- <a id="BuildWavefrontBackwardRemainder"></a>`BuildWavefrontBackwardRemainder` — [`L5135`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5135) — Computes remainder backward pass across layers when rem_steps > 0.
- <a id="BuildWavefrontBackwardWhileBody"></a>`BuildWavefrontBackwardWhileBody` — [`L5317`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5317) — Builds while loop body for pipelined wavefront backward pass.
- `BuildWavefrontBackwardWhileBody` — [`L5317`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5317) — Builds while loop body for pipelined wavefront backward pass.
- `BuildWavefrontForwardRemainder(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_0, mlir::MlirOp chunked_y, const std::vector<mlir::MlirOp>& final_h, const absl::Span<const GruWavefrontLayerWeight> layer_weights, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, int64_t chunked_steps, int64_t rem_steps, int64_t seq_len, int64_t batch, int64_t hidden, int64_t num_layers, bool batch_first, ToOutFn to_out, double dropout, bool has_dropout, std::optional<mlir::MlirOp> rand_op, mlir::stablehlo::Precision precision)` — [`L1538`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1538) — Evaluates wavefront remainder steps across all layers when seq_len %
- <a id="BuildWavefrontForwardRemainder"></a>`BuildWavefrontForwardRemainder(mlir::MlirBuilder& builder, mlir::MlirOp x_proj_0, mlir::MlirOp chunked_y, const std::vector<mlir::MlirOp>& final_h, const absl::Span<const GruWavefrontLayerWeight> layer_weights, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, int64_t chunked_steps, int64_t rem_steps, int64_t seq_len, int64_t batch, int64_t hidden, int64_t num_layers, bool batch_first, ToOutFn to_out, double dropout, bool has_dropout, std::optional<mlir::MlirOp> rand_op, mlir::stablehlo::Precision precision)` — [`L1538`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1538) — Evaluates wavefront remainder steps across all layers when seq_len %
- `BuildWavefrontForwardWhileBody(mlir::MlirBuilder& builder, mlir::Block* body_block, mlir::Location loc, mlir::MlirOp x_proj_0, const absl::Span<const GruWavefrontLayerWeight> layer_weights, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, int64_t batch, int64_t hidden, int64_t num_layers, bool batch_first, int64_t concat_dim, ToOutFn to_out, double dropout, bool has_dropout, std::optional<mlir::MlirOp> rand_op, mlir::stablehlo::Precision precision)` — [`L1683`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1683) — Builds the body block of the pipelined wavefront forward while loop.
- <a id="BuildWavefrontForwardWhileBody"></a>`BuildWavefrontForwardWhileBody(mlir::MlirBuilder& builder, mlir::Block* body_block, mlir::Location loc, mlir::MlirOp x_proj_0, const absl::Span<const GruWavefrontLayerWeight> layer_weights, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, int64_t batch, int64_t hidden, int64_t num_layers, bool batch_first, int64_t concat_dim, ToOutFn to_out, double dropout, bool has_dropout, std::optional<mlir::MlirOp> rand_op, mlir::stablehlo::Precision precision)` — [`L1683`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1683) — Builds the body block of the pipelined wavefront forward while loop.
- <a id="BuildWavefrontHPrevSeq"></a>`BuildWavefrontHPrevSeq(mlir::MlirBuilder& builder, absl::Span<const mlir::MlirOp> h_inits, absl::Span<const mlir::MlirOp> layer_outputs, int64_t num_layers, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, int64_t concat_dim, ToAccFn to_acc)` — [`L5290`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5290) — Reconstructs previous hidden state sequences [h_0, y_1, ..., y_{T-1}] for
- `BuildWavefrontHPrevSeq(mlir::MlirBuilder& builder, absl::Span<const mlir::MlirOp> h_inits, absl::Span<const mlir::MlirOp> layer_outputs, int64_t num_layers, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, int64_t concat_dim, ToAccFn to_acc)` — [`L5290`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5290) — Reconstructs previous hidden state sequences [h_0, y_1, ..., y_{T-1}] for
- <a id="CollectGruInputTensors"></a>`CollectGruInputTensors(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, bool has_dropout, const std::optional<at::Tensor>& rng_state)` — [`L6098`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6098) — Collects and packs all Torch input tensors for GRU execution.
- `CollectGruInputTensors(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, bool has_dropout, const std::optional<at::Tensor>& rng_state)` — [`L6098`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6098) — Collects and packs all Torch input tensors for GRU execution.
- `ComputeBidirBackwardChunkSteps` — [`L4230`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4230) — Computes kGruUnrollFactor backward steps concurrently for forward and reverse
- <a id="ComputeBidirBackwardChunkSteps"></a>`ComputeBidirBackwardChunkSteps` — [`L4230`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4230) — Computes kGruUnrollFactor backward steps concurrently for forward and reverse
- <a id="ComputeBidirBackwardRemainder"></a>`ComputeBidirBackwardRemainder` — [`L3973`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3973) — Evaluates tail remainder backward steps for bidirectional GRU.
- `ComputeBidirBackwardRemainder` — [`L3973`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3973) — Evaluates tail remainder backward steps for bidirectional GRU.
- <a id="ComputeBidirLayerBackward"></a>`ComputeBidirLayerBackward(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp y_out_fwd, mlir::MlirOp y_out_rev, mlir::MlirOp act_fwd_seq, mlir::MlirOp act_rev_seq, mlir::MlirOp w_ih_fwd, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_ih_rev, mlir::MlirOp w_hh_rev, bool has_biases, int64_t seq_len, int64_t batch, int64_t hidden, int64_t in_dim, bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, mlir::stablehlo::Precision precision)` — [`L4881`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4881) — Dispatches backward pass for a bidirectional GRU layer to static unrolling
- `ComputeBidirLayerBackward(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp y_out_fwd, mlir::MlirOp y_out_rev, mlir::MlirOp act_fwd_seq, mlir::MlirOp act_rev_seq, mlir::MlirOp w_ih_fwd, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_ih_rev, mlir::MlirOp w_hh_rev, bool has_biases, int64_t seq_len, int64_t batch, int64_t hidden, int64_t in_dim, bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, mlir::stablehlo::Precision precision)` — [`L4881`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4881) — Dispatches backward pass for a bidirectional GRU layer to static unrolling
- <a id="ComputeBidirLayerBackwardChunked"></a>`ComputeBidirLayerBackwardChunked(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp y_out_fwd, mlir::MlirOp y_out_rev, mlir::MlirOp act_fwd_seq, mlir::MlirOp act_rev_seq, mlir::MlirOp w_ih_fwd, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_ih_rev, mlir::MlirOp w_hh_rev, const bool has_biases, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t in_dim, const bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, const mlir::stablehlo::Precision precision)` — [`L4609`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4609) — Computes the chunked recurrence backward pass for a bidirectional GRU layer
- `ComputeBidirLayerBackwardChunked(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp y_out_fwd, mlir::MlirOp y_out_rev, mlir::MlirOp act_fwd_seq, mlir::MlirOp act_rev_seq, mlir::MlirOp w_ih_fwd, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_ih_rev, mlir::MlirOp w_hh_rev, const bool has_biases, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t in_dim, const bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, const mlir::stablehlo::Precision precision)` — [`L4609`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4609) — Computes the chunked recurrence backward pass for a bidirectional GRU layer
- `ComputeBidirLayerBackwardStatic(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp y_out_fwd, mlir::MlirOp y_out_rev, mlir::MlirOp act_fwd_seq, mlir::MlirOp act_rev_seq, mlir::MlirOp w_ih_fwd, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_ih_rev, mlir::MlirOp w_hh_rev, bool has_biases, int64_t seq_len, int64_t batch, int64_t hidden, int64_t in_dim, bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, mlir::stablehlo::Precision precision)` — [`L3710`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3710) — Computes the backward pass for a single bidirectional GRU layer using static
- <a id="ComputeBidirLayerBackwardStatic"></a>`ComputeBidirLayerBackwardStatic(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init_fwd, mlir::MlirOp h_init_rev, mlir::MlirOp y_out_fwd, mlir::MlirOp y_out_rev, mlir::MlirOp act_fwd_seq, mlir::MlirOp act_rev_seq, mlir::MlirOp w_ih_fwd, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_ih_rev, mlir::MlirOp w_hh_rev, bool has_biases, int64_t seq_len, int64_t batch, int64_t hidden, int64_t in_dim, bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, mlir::stablehlo::Precision precision)` — [`L3710`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3710) — Computes the backward pass for a single bidirectional GRU layer using static
- <a id="ComputeGruBackwardChunkSteps"></a>`ComputeGruBackwardChunkSteps(mlir::MlirBuilder& builder, mlir::MlirOp grad_y_chunk, mlir::MlirOp act_chunk, mlir::MlirOp h_prev_chunk, mlir::MlirOp cur_delta_h_next, mlir::MlirOp w_hh, mlir::MlirOp w_ih, const mlir::stablehlo::DotDimensionNumbersAttr hh_bwd_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr x_bwd_dot_dims, const int64_t batch, const int64_t hidden, const int64_t in_dim, const bool batch_first, const int64_t concat_dim, const mlir::Type acc_dtype, mlir::MlirOp one, const mlir::stablehlo::Precision precision)` — [`L3182`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3182) — Computes kGruUnrollFactor backward steps for a single chunk.
- `ComputeGruBackwardChunkSteps(mlir::MlirBuilder& builder, mlir::MlirOp grad_y_chunk, mlir::MlirOp act_chunk, mlir::MlirOp h_prev_chunk, mlir::MlirOp cur_delta_h_next, mlir::MlirOp w_hh, mlir::MlirOp w_ih, const mlir::stablehlo::DotDimensionNumbersAttr hh_bwd_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr x_bwd_dot_dims, const int64_t batch, const int64_t hidden, const int64_t in_dim, const bool batch_first, const int64_t concat_dim, const mlir::Type acc_dtype, mlir::MlirOp one, const mlir::stablehlo::Precision precision)` — [`L3182`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3182) — Computes kGruUnrollFactor backward steps for a single chunk.
- `ComputeGruBackwardRemainder` — [`L3020`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3020) — Evaluates tail remainder backward steps (from seq_len - 1 down to
- <a id="ComputeGruBackwardRemainder"></a>`ComputeGruBackwardRemainder` — [`L3020`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3020) — Evaluates tail remainder backward steps (from seq_len - 1 down to
- `ComputeGruBackwardStep(mlir::MlirBuilder& builder, mlir::MlirOp delta_h, mlir::MlirOp h_prev, mlir::MlirOp act_4h, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_bwd_dot_dims, int64_t batch, int64_t hidden, mlir::MlirOp one, mlir::stablehlo::Precision precision)` — [`L744`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L744) — Evaluates a single recurrent timestep of the GRU cell backward pass using
- <a id="ComputeGruBackwardStep"></a>`ComputeGruBackwardStep(mlir::MlirBuilder& builder, mlir::MlirOp delta_h, mlir::MlirOp h_prev, mlir::MlirOp act_4h, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_bwd_dot_dims, int64_t batch, int64_t hidden, mlir::MlirOp one, mlir::stablehlo::Precision precision)` — [`L744`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L744) — Evaluates a single recurrent timestep of the GRU cell backward pass using
- <a id="ComputeGruForwardOutputLayouts"></a>`ComputeGruForwardOutputLayouts(mlir::ElementType out_dtype, mlir::ElementType acc_dtype, int64_t batch, int64_t seq_len, int64_t hidden, int64_t num_layers, int64_t num_directions, bool batch_first, bool cache_activations)` — [`L6121`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6121) — Computes output dtypes and tensor dimension shapes for GRU forward dispatch.
- `ComputeGruStep(mlir::MlirOp x_proj_step, mlir::MlirOp h_curr, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t batch, int64_t hidden, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision)` — [`L632`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L632) — Evaluates a single recurrent timestep of the GRU cell forward pass on TPU
- <a id="ComputeGruStep"></a>`ComputeGruStep(mlir::MlirOp x_proj_step, mlir::MlirOp h_curr, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t batch, int64_t hidden, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision)` — [`L632`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L632) — Evaluates a single recurrent timestep of the GRU cell forward pass on TPU
- <a id="ComputeLayerBackward"></a>`ComputeLayerBackward(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init, mlir::MlirOp y_out, mlir::MlirOp act_4h_seq, mlir::MlirOp w_ih, mlir::MlirOp w_hh, const bool has_biases, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t in_dim, const bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, const mlir::stablehlo::Precision precision)` — [`L3643`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3643) — Dispatcher for unidirectional GRU layer backward evaluation.
- `ComputeLayerBackward(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init, mlir::MlirOp y_out, mlir::MlirOp act_4h_seq, mlir::MlirOp w_ih, mlir::MlirOp w_hh, const bool has_biases, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t in_dim, const bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, const mlir::stablehlo::Precision precision)` — [`L3643`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3643) — Dispatcher for unidirectional GRU layer backward evaluation.
- <a id="ComputeLayerBackwardChunked"></a>`ComputeLayerBackwardChunked(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init, mlir::MlirOp y_out, mlir::MlirOp act_4h_seq, mlir::MlirOp w_ih, mlir::MlirOp w_hh, const bool has_biases, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t in_dim, const bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, const mlir::stablehlo::Precision precision)` — [`L3462`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3462) — Computes chunked reverse BPTT backward pass for a single unidirectional GRU
- `ComputeLayerBackwardChunked(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init, mlir::MlirOp y_out, mlir::MlirOp act_4h_seq, mlir::MlirOp w_ih, mlir::MlirOp w_hh, const bool has_biases, const int64_t seq_len, const int64_t batch, const int64_t hidden, const int64_t in_dim, const bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, const mlir::stablehlo::Precision precision)` — [`L3462`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L3462) — Computes chunked reverse BPTT backward pass for a single unidirectional GRU
- <a id="ComputeLayerBackwardStatic"></a>`ComputeLayerBackwardStatic(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init, mlir::MlirOp y_out, mlir::MlirOp act_4h_seq, mlir::MlirOp w_ih, mlir::MlirOp w_hh, bool has_biases, int64_t seq_len, int64_t batch, int64_t hidden, int64_t in_dim, bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, mlir::stablehlo::Precision precision)` — [`L2836`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2836) — Computes static backward pass (reverse BPTT) for a single unidirectional GRU
- `ComputeLayerBackwardStatic(mlir::MlirBuilder& builder, mlir::MlirOp grad_y, mlir::MlirOp grad_hy, mlir::MlirOp layer_in, mlir::MlirOp h_init, mlir::MlirOp y_out, mlir::MlirOp act_4h_seq, mlir::MlirOp w_ih, mlir::MlirOp w_hh, bool has_biases, int64_t seq_len, int64_t batch, int64_t hidden, int64_t in_dim, bool batch_first, ToOutFn to_out, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, mlir::stablehlo::Precision precision)` — [`L2836`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2836) — Computes static backward pass (reverse BPTT) for a single unidirectional GRU
- `ComputeLayerByLayerBackwardStep(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> builder_inputs, int64_t l, int64_t num_layers, int64_t num_directions, int64_t batch, int64_t seq_len, int64_t hidden, int64_t input_size, bool batch_first, bool bidirectional, bool has_biases, size_t params_offset, size_t params_per_layer, size_t params_per_direction, mlir::MlirOp hx_val, mlir::MlirOp incoming_grad_hy, const GruReconstructedForwardData& fwd_data, mlir::MlirOp& curr_grad_y, std::vector<mlir::MlirOp>& all_grad_h0, std::vector<mlir::MlirOp>& all_grad_params, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, ToOutFn to_out, mlir::stablehlo::Precision current_precision)` — [`L6377`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6377) — Evaluates backward pass for a single layer in the reverse topological
- <a id="ComputeLayerByLayerBackwardStep"></a>`ComputeLayerByLayerBackwardStep(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> builder_inputs, int64_t l, int64_t num_layers, int64_t num_directions, int64_t batch, int64_t seq_len, int64_t hidden, int64_t input_size, bool batch_first, bool bidirectional, bool has_biases, size_t params_offset, size_t params_per_layer, size_t params_per_direction, mlir::MlirOp hx_val, mlir::MlirOp incoming_grad_hy, const GruReconstructedForwardData& fwd_data, mlir::MlirOp& curr_grad_y, std::vector<mlir::MlirOp>& all_grad_h0, std::vector<mlir::MlirOp>& all_grad_params, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, ToOutFn to_out, mlir::stablehlo::Precision current_precision)` — [`L6377`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6377) — Evaluates backward pass for a single layer in the reverse topological
- <a id="ConcatDim"></a>`ConcatDim(mlir::MlirBuilder& builder, absl::Span<const mlir::MlirOp> ops, int64_t dim)` — [`L381`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L381) — Concatenates a span of StableHLO tensor operations along the specified
- `DispatchGruWavefrontBackwardPath(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> builder_inputs, mlir::MlirOp hx_val, mlir::MlirOp incoming_grad_y, mlir::MlirOp incoming_grad_hy, const GruReconstructedForwardData& fwd_data, const size_t params_offset, const size_t params_per_layer, const int64_t num_layers, const int64_t batch, const int64_t seq_len, const int64_t hidden, const int64_t input_size, const bool batch_first, const bool has_biases, const bool has_dropout, const double dropout, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, ToOutFn to_out, const mlir::stablehlo::Precision current_precision)` — [`L6328`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6328) — Dispatches pipelined wavefront backward pass for multi-layer unidirectional
- <a id="DispatchGruWavefrontBackwardPath"></a>`DispatchGruWavefrontBackwardPath(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> builder_inputs, mlir::MlirOp hx_val, mlir::MlirOp incoming_grad_y, mlir::MlirOp incoming_grad_hy, const GruReconstructedForwardData& fwd_data, const size_t params_offset, const size_t params_per_layer, const int64_t num_layers, const int64_t batch, const int64_t seq_len, const int64_t hidden, const int64_t input_size, const bool batch_first, const bool has_biases, const bool has_dropout, const double dropout, mlir::MlirOp zero_const, ReduceBuilderFn sum_reduce_builder, ToOutFn to_out, const mlir::stablehlo::Precision current_precision)` — [`L6328`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6328) — Dispatches pipelined wavefront backward pass for multi-layer unidirectional
- `EvaluateGruBidirLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp current_input, absl::Span<mlir::MlirOp> builder_inputs, const size_t params_offset, const size_t params_per_layer, const size_t params_per_direction, const int64_t l, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::ElementType acc_dtype, const mlir::stablehlo::Precision current_precision, const bool has_biases, mlir::MlirOp h_0_acc, const int64_t batch, const int64_t hidden, const int64_t seq_len, const bool batch_first, ToOutFn to_out, ToAccFn to_acc, const bool cache_activations)` — [`L5779`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5779) — Evaluates forward pass for a single bidirectional layer l.
- <a id="EvaluateGruBidirLayerForward"></a>`EvaluateGruBidirLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp current_input, absl::Span<mlir::MlirOp> builder_inputs, const size_t params_offset, const size_t params_per_layer, const size_t params_per_direction, const int64_t l, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::ElementType acc_dtype, const mlir::stablehlo::Precision current_precision, const bool has_biases, mlir::MlirOp h_0_acc, const int64_t batch, const int64_t hidden, const int64_t seq_len, const bool batch_first, ToOutFn to_out, ToAccFn to_acc, const bool cache_activations)` — [`L5779`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5779) — Evaluates forward pass for a single bidirectional layer l.
- <a id="EvaluateGruUnidirLayerForward"></a>`EvaluateGruUnidirLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp current_input, absl::Span<mlir::MlirOp> builder_inputs, const size_t params_offset, const size_t params_per_layer, const int64_t l, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::ElementType acc_dtype, const mlir::stablehlo::Precision current_precision, const bool has_biases, mlir::MlirOp h_0_acc, const int64_t batch, const int64_t hidden, const int64_t seq_len, const bool batch_first, ToOutFn to_out, ToAccFn to_acc, const bool cache_activations)` — [`L5737`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5737) — Builds the complete StableHLO computational graph for multi-layer GRU forward
- `EvaluateGruUnidirLayerForward(mlir::MlirBuilder& builder, mlir::MlirOp current_input, absl::Span<mlir::MlirOp> builder_inputs, const size_t params_offset, const size_t params_per_layer, const int64_t l, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::ElementType acc_dtype, const mlir::stablehlo::Precision current_precision, const bool has_biases, mlir::MlirOp h_0_acc, const int64_t batch, const int64_t hidden, const int64_t seq_len, const bool batch_first, ToOutFn to_out, ToAccFn to_acc, const bool cache_activations)` — [`L5737`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5737) — Builds the complete StableHLO computational graph for multi-layer GRU forward
- `EvaluateWavefrontBackwardRemainderLayer` — [`L4976`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4976)
- <a id="EvaluateWavefrontBackwardRemainderLayer"></a>`EvaluateWavefrontBackwardRemainderLayer` — [`L4976`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L4976)
- <a id="EvaluateWavefrontForwardChunkLayer"></a>`EvaluateWavefrontForwardChunkLayer(mlir::MlirBuilder& builder, mlir::MlirOp curr_chunk, mlir::MlirOp body_h_l, mlir::MlirOp body_step_idx, mlir::MlirOp zero_i64, mlir::IntegerType i64, const GruWavefrontLayerWeight& layer_weight, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, int64_t l, int64_t batch, int64_t hidden, bool batch_first, int64_t concat_dim, ToOutFn to_out, double dropout, bool has_dropout, std::optional<mlir::MlirOp> rand_op, mlir::stablehlo::Precision precision)` — [`L1622`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1622)
- `EvaluateWavefrontForwardChunkLayer(mlir::MlirBuilder& builder, mlir::MlirOp curr_chunk, mlir::MlirOp body_h_l, mlir::MlirOp body_step_idx, mlir::MlirOp zero_i64, mlir::IntegerType i64, const GruWavefrontLayerWeight& layer_weight, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, int64_t l, int64_t batch, int64_t hidden, bool batch_first, int64_t concat_dim, ToOutFn to_out, double dropout, bool has_dropout, std::optional<mlir::MlirOp> rand_op, mlir::stablehlo::Precision precision)` — [`L1622`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1622)
- <a id="EvaluateWavefrontRemainderLayer"></a>`EvaluateWavefrontRemainderLayer(mlir::MlirBuilder& builder, mlir::MlirOp curr_rem_seq, mlir::MlirOp prev_h, const GruWavefrontLayerWeight& layer_weight, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, int64_t l, int64_t chunked_steps, int64_t rem_steps, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, int64_t concat_dim, ToOutFn to_out, double dropout, bool has_dropout, std::optional<mlir::MlirOp> rand_op, mlir::stablehlo::Precision precision)` — [`L1426`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1426)
- `EvaluateWavefrontRemainderLayer(mlir::MlirBuilder& builder, mlir::MlirOp curr_rem_seq, mlir::MlirOp prev_h, const GruWavefrontLayerWeight& layer_weight, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const mlir::stablehlo::DotDimensionNumbersAttr ih_dot_dims, int64_t l, int64_t chunked_steps, int64_t rem_steps, int64_t seq_len, int64_t batch, int64_t hidden, bool batch_first, int64_t concat_dim, ToOutFn to_out, double dropout, bool has_dropout, std::optional<mlir::MlirOp> rand_op, mlir::stablehlo::Precision precision)` — [`L1426`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1426)
- `ExecuteGruForwardLayerStep` — [`L5911`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5911) — Executes forward computation for a single layer l and collects cached
- <a id="ExecuteGruForwardLayerStep"></a>`ExecuteGruForwardLayerStep` — [`L5911`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5911) — Executes forward computation for a single layer l and collects cached
- <a id="ExpandStep3D"></a>`ExpandStep3D(mlir::MlirOp step_2d, int64_t batch, int64_t feature_dim, bool batch_first)` — [`L457`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L457) — Reshapes a 2D timestep tensor [batch, feature_dim] into a 3D sequence tensor
- <a id="ExtractLayer2D"></a>`ExtractLayer2D(mlir::MlirOp tensor_3d, int64_t layer_idx, int64_t batch, int64_t hidden)` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L405) — Extracts a single layer's 2D hidden state from a stacked 3D hidden state
- <a id="FinalizeGruBidirForwardOutputs"></a>`FinalizeGruBidirForwardOutputs` — [`L2468`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2468) — Finalizes bidirectional GRU forward outputs after chunked while loop
- `FinalizeGruBidirForwardOutputs` — [`L2468`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2468) — Finalizes bidirectional GRU forward outputs after chunked while loop
- <a id="FinalizeWavefrontBackwardOutputs"></a>`FinalizeWavefrontBackwardOutputs(mlir::MlirBuilder& builder, mlir::stablehlo::WhileOp while_op, const std::optional<mlir::MlirOp>& rem_grad_x_0, int64_t num_layers, int64_t batch, int64_t hidden, bool has_biases, int64_t concat_dim, ToOutFn to_out)` — [`L5474`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5474) — Finalizes output gradients for pipelined wavefront backward pass.
- `FinalizeWavefrontBackwardOutputs(mlir::MlirBuilder& builder, mlir::stablehlo::WhileOp while_op, const std::optional<mlir::MlirOp>& rem_grad_x_0, int64_t num_layers, int64_t batch, int64_t hidden, bool has_biases, int64_t concat_dim, ToOutFn to_out)` — [`L5474`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5474) — Finalizes output gradients for pipelined wavefront backward pass.
- <a id="FormatGruBackwardOutputs"></a>`FormatGruBackwardOutputs(mlir::MlirBuilder& builder, mlir::MlirOp curr_grad_y, absl::Span<const mlir::MlirOp> all_grad_h0, absl::Span<const mlir::MlirOp> all_grad_params, int64_t batch, int64_t hidden, ToOutFn to_out)` — [`L6486`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6486) — Formats final input gradients, initial hidden gradients, and parameter
- `FormatGruBackwardOutputs(mlir::MlirBuilder& builder, mlir::MlirOp curr_grad_y, absl::Span<const mlir::MlirOp> all_grad_h0, absl::Span<const mlir::MlirOp> all_grad_params, int64_t batch, int64_t hidden, ToOutFn to_out)` — [`L6486`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6486) — Formats final input gradients, initial hidden gradients, and parameter
- <a id="GetElementTypeEnum"></a>`GetElementTypeEnum(mlir::Type type)` — [`L476`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L476) — Converts an MLIR Type into the corresponding mlir::ElementType enum.
- `GruInputBackwardImpl(const at::Tensor& grad_output, const at::Tensor& grad_hy, const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const at::TensorList cached_activations, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys)` — [`L6672`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6672) — Internal implementation helper that validates inputs and dispatches the
- <a id="GruInputBackwardImpl"></a>`GruInputBackwardImpl(const at::Tensor& grad_output, const at::Tensor& grad_hy, const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const at::TensorList cached_activations, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys)` — [`L6672`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6672) — Internal implementation helper that validates inputs and dispatches the
- `GruInputImpl(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys, const bool cache_activations, std::optional<at::Tensor> rng_state = std::nullopt)` — [`L6172`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6172) — Internal implementation helper that validates GRU inputs and dispatches the
- <a id="GruInputImpl"></a>`GruInputImpl(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first, OpParamCacheKeys param_keys, const bool cache_activations, std::optional<at::Tensor> rng_state = std::nullopt)` — [`L6172`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6172) — Internal implementation helper that validates GRU inputs and dispatches the
- <a id="InitWavefrontBackwardRemainderZero"></a>`InitWavefrontBackwardRemainderZero(absl::Span<const mlir::MlirOp> grad_hy_list, int64_t num_layers, int64_t input_size, int64_t hidden, bool has_biases, mlir::Type acc_elem_type, mlir::MlirOp zero_scalar)` — [`L5100`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5100) — Initializes zero parameter gradient accumulators when rem_steps == 0.
- <a id="MakeDotDims"></a>`MakeDotDims(mlir::MLIRContext* ctx, llvm::ArrayRef<int64_t> lhs_contracting, llvm::ArrayRef<int64_t> rhs_contracting)` — [`L357`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L357) — Constructs DotDimensionNumbersAttr for StableHLO DotGeneral matrix
- `MakeDotDims(mlir::MLIRContext* ctx, llvm::ArrayRef<int64_t> lhs_contracting, llvm::ArrayRef<int64_t> rhs_contracting)` — [`L357`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L357) — Constructs DotDimensionNumbersAttr for StableHLO DotGeneral matrix
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::ElementType acc_dtype, std::optional<mlir::Type> gemm_dtype, mlir::stablehlo::Precision precision)` — [`L544`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L544) — MixedPrecisionDotGeneral overload accepting ElementType enum with optional
- <a id="MixedPrecisionDotGeneral"></a>`MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::Type acc_dtype, mlir::stablehlo::Precision precision)` — [`L556`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L556) — MixedPrecisionDotGeneral overload accepting mlir::Type with default nullopt
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::ElementType acc_dtype, std::optional<mlir::Type> gemm_dtype, mlir::stablehlo::Precision precision)` — [`L544`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L544) — MixedPrecisionDotGeneral overload accepting ElementType enum with optional
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::Type acc_dtype, std::optional<mlir::Type> gemm_dtype, mlir::stablehlo::Precision precision)` — [`L504`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L504) — Emits a StableHLO DotGeneral matrix multiplication on TPU with
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::ElementType acc_dtype, mlir::stablehlo::Precision precision)` — [`L566`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L566) — MixedPrecisionDotGeneral overload accepting ElementType enum with default
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::Type acc_dtype, mlir::stablehlo::Precision precision)` — [`L556`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L556) — MixedPrecisionDotGeneral overload accepting mlir::Type with default nullopt
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::ElementType acc_dtype, mlir::stablehlo::Precision precision)` — [`L566`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L566) — MixedPrecisionDotGeneral overload accepting ElementType enum with default
- `MixedPrecisionDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::DotDimensionNumbersAttr dot_dims, mlir::Type acc_dtype, std::optional<mlir::Type> gemm_dtype, mlir::stablehlo::Precision precision)` — [`L504`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L504) — Emits a StableHLO DotGeneral matrix multiplication on TPU with
- `ProcessWavefrontBackwardLayerChunk` — [`L5201`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5201) — Computes backward chunk for a single layer in the wavefront backward loop.
- <a id="ProcessWavefrontBackwardLayerChunk"></a>`ProcessWavefrontBackwardLayerChunk` — [`L5201`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L5201) — Computes backward chunk for a single layer in the wavefront backward loop.
- <a id="ReconstructGruForwardPass"></a>`ReconstructGruForwardPass` — [`L6251`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6251) — Reconstructs forward activations and layer outputs needed for backward
- `ReconstructGruForwardPass` — [`L6251`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L6251) — Reconstructs forward activations and layer outputs needed for backward
- <a id="RunGruBidirForwardSteps"></a>`RunGruBidirForwardSteps(mlir::MlirOp x_chunk_fwd, mlir::MlirOp x_chunk_rev, mlir::MlirOp curr_h_fwd, mlir::MlirOp curr_h_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const int64_t batch, const int64_t hidden, const bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, const mlir::stablehlo::Precision precision, const bool cache_activations)` — [`L2073`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2073) — Concurrently evaluates kGruUnrollFactor forward and reverse steps for a
- `RunGruBidirForwardSteps(mlir::MlirOp x_chunk_fwd, mlir::MlirOp x_chunk_rev, mlir::MlirOp curr_h_fwd, mlir::MlirOp curr_h_rev, mlir::MlirOp w_hh_fwd, mlir::MlirOp w_hh_rev, const mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, const int64_t batch, const int64_t hidden, const bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh_fwd, std::optional<mlir::MlirOp> b_hh_rev, const mlir::stablehlo::Precision precision, const bool cache_activations)` — [`L2073`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L2073) — Concurrently evaluates kGruUnrollFactor forward and reverse steps for a
- `RunGruForwardSteps(mlir::MlirOp x_seq_3d, int64_t start_step, int64_t num_steps, mlir::MlirOp h_start, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L971`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L971) — Executes a sequence of unrolled recurrent GRU forward steps starting at
- <a id="RunGruForwardSteps"></a>`RunGruForwardSteps(mlir::MlirOp x_seq_3d, int64_t start_step, int64_t num_steps, mlir::MlirOp h_start, mlir::MlirOp w_hh, mlir::stablehlo::DotDimensionNumbersAttr hh_dot_dims, int64_t batch, int64_t hidden, bool batch_first, ToOutFn to_out, std::optional<mlir::MlirOp> b_hh, mlir::stablehlo::Precision precision, bool cache_activations)` — [`L971`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L971) — Executes a sequence of unrolled recurrent GRU forward steps starting at
- <a id="SliceStep2D"></a>`SliceStep2D(mlir::MlirOp seq_3d, int64_t t, int64_t batch, int64_t feature_dim, bool batch_first)` — [`L430`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L430) — Extracts a single timestep slice from a 3D sequence tensor as a 2D tensor.
- <a id="StackPerLayerFinalHiddenStates"></a>`StackPerLayerFinalHiddenStates(mlir::MlirBuilder& builder, const absl::Span<const mlir::MlirOp> final_h, int64_t batch, int64_t hidden, ToOutFn to_out)` — [`L1486`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L1486) — Stacks per-layer final hidden states [num_layers, batch, hidden].
- <a id="ValidateGruInputs"></a>`ValidateGruInputs(const at::Tensor& input, const at::Tensor& hx, const at::TensorList params, const bool has_biases, const int64_t num_layers, const double dropout, const bool train, const bool bidirectional, const bool batch_first)` — [`L303`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L303) — Top-level input validator verifying user-supplied input tensors and
- <a id="ValidateGruTensorShapes"></a>`ValidateGruTensorShapes(const at::Tensor& hx, const int64_t num_layers, const int64_t batch, const bool bidirectional = false)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L165) — Validates the shape and dimensionality of the initial hidden state tensor
- <a id="ValidateGruWeights"></a>`ValidateGruWeights(const at::TensorList params, const bool has_biases, const int64_t num_layers, const int64_t input_size, const int64_t hidden, const bool bidirectional = false)` — [`L217`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L217) — Validates the count and tensor dimensions of all GRU weight and bias

## Module values
- <a id="kGruUnrollFactor"></a>`kGruUnrollFactor` — [`L143`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_aten_kernels.cc#L143) — The recurrence unroll factor k = 8 governs the granularity of chunked loop

