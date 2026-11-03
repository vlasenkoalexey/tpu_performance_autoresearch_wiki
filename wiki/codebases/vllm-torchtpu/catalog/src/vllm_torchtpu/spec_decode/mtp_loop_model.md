---
title: 'Module: src/vllm_torchtpu/spec_decode/mtp_loop_model.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/spec_decode/mtp_loop_model.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.spec_decode.mtp_loop_model`/
symbols:
  MTP_DYNAMIC_ARG_DIMS.MTP_DYNAMIC_ARG_DIMS: MTP_DYNAMIC_ARG_DIMS.MTP_DYNAMIC_ARG_DIMS.
  MtpLoopStepModel.forward: MtpLoopStepModel#forward().
  MtpLoopStepModel: MtpLoopStepModel#
  MtpLoopStepModel.mtp: MtpLoopStepModel#mtp.
  MtpLoopStepModel.__init__: MtpLoopStepModel#__init__().
  MtpLoopStepModel.prefix: MtpLoopStepModel#prefix.
---
# Module: [`src/vllm_torchtpu/spec_decode/mtp_loop_model.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_loop_model.py)

## Classes
### <a id="MtpLoopStepModel"></a>`MtpLoopStepModel`
- def: [`src/vllm_torchtpu/spec_decode/mtp_loop_model.py:49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_loop_model.py#L49)
- doc: Runs an MTP draft's own `forward` as a separately compiled program.
- signature: `class MtpLoopStepModel(nn.Module):`
- members:
  - <a id="MtpLoopStepModel.forward"></a>`forward(self, input_ids: torch.Tensor | None, positions: torch.Tensor, hidden_states: torch.Tensor, intermediate_tensors: IntermediateTensors | None = None, inputs_embeds: torch.Tensor | None = None, spec_step_idx: int = 0)` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_loop_model.py#L65)
  - <a id="MtpLoopStepModel.mtp"></a>`mtp` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_loop_model.py#L63)
  - <a id="MtpLoopStepModel.prefix"></a>`prefix` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_loop_model.py#L62)
- protocol/private: <a id="MtpLoopStepModel.__init__"></a>`__init__`[`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_loop_model.py#L52)
- used by: [`_build_mtp_loop_model`](eagle3.md#Eagle3Proposer._build_mtp_loop_model)

## Module values
- <a id="MTP_DYNAMIC_ARG_DIMS.MTP_DYNAMIC_ARG_DIMS"></a>`MTP_DYNAMIC_ARG_DIMS` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_loop_model.py#L39)

