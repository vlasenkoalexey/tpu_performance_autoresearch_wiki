---
title: 'Module: src/vllm_torchtpu/spec_decode/mtp_fused_loop.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/spec_decode/mtp_fused_loop.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.spec_decode.mtp_fused_loop`/
symbols:
  _MtpFusedLoop.forward: _MtpFusedLoop#forward().
  build_mtp_fused_loop: build_mtp_fused_loop().
  _MtpFusedLoop.mtp: _MtpFusedLoop#mtp.
  _MtpFusedLoop.__init__: _MtpFusedLoop#__init__().
  MtpDraftModel: MtpDraftModel#
  MtpDraftModel.forward: MtpDraftModel#forward().
  MtpDraftModel.compute_logits: MtpDraftModel#compute_logits().
  _MtpFusedLoop: _MtpFusedLoop#
  _MtpFusedLoop.num_steps: _MtpFusedLoop#num_steps.
  _MtpFusedLoop.prefix: _MtpFusedLoop#prefix.
---
# Module: [`src/vllm_torchtpu/spec_decode/mtp_fused_loop.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py)

## Classes
### <a id="MtpDraftModel"></a>`MtpDraftModel`  ·  implements/extends Protocol
- def: [`src/vllm_torchtpu/spec_decode/mtp_fused_loop.py:42`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L42)
- doc: What the loop calls on the MTP draft. The draft is an nn.Module, but
- signature: `class MtpDraftModel(Protocol):`
- members:
  - <a id="MtpDraftModel.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor)` — [`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L48)
  - <a id="MtpDraftModel.forward"></a>`forward(self, *args: Any, **kwargs: Any)` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L46)
- used by: [`forward`](mtp_fused_loop.md#_MtpFusedLoop.forward), [`build_mtp_fused_loop`](mtp_fused_loop.md#build_mtp_fused_loop), [`__init__`](mtp_fused_loop.md#_MtpFusedLoop.__init__)

### <a id="_MtpFusedLoop"></a>`_MtpFusedLoop`
- def: [`src/vllm_torchtpu/spec_decode/mtp_fused_loop.py:51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L51)
- signature: `class _MtpFusedLoop(nn.Module):`
- members:
  - <a id="_MtpFusedLoop.forward"></a>`forward(self, input_ids: torch.Tensor, positions: torch.Tensor, hidden_states: torch.Tensor, seq_lens: torch.Tensor, intermediate_tensors: IntermediateTensors | None = None, inputs_embeds: torch.Tensor | None = None)` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L66) — `positions` and `seq_lens` are step 1's. Returns the K-1 draft
  - <a id="_MtpFusedLoop.mtp"></a>`mtp` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L63)
  - <a id="_MtpFusedLoop.num_steps"></a>`num_steps` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L64)
  - <a id="_MtpFusedLoop.prefix"></a>`prefix` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L62)
- protocol/private: <a id="_MtpFusedLoop.__init__"></a>`__init__`[`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L52)
- uses (calls/refs, reference-scoped): [`MtpDraftModel`](mtp_fused_loop.md#MtpDraftModel), [`compute_logits`](mtp_fused_loop.md#MtpDraftModel.compute_logits), [`forward`](mtp_fused_loop.md#MtpDraftModel.forward)
- used by: [`build_mtp_fused_loop`](mtp_fused_loop.md#build_mtp_fused_loop)

## Functions
- <a id="build_mtp_fused_loop"></a>`build_mtp_fused_loop(*, vllm_config: VllmConfig, prefix: str, mtp: MtpDraftModel, num_steps: int, dynamic_arg_dims: dict)` — [`L105`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/mtp_fused_loop.py#L105) — Compile `_MtpFusedLoop` with the draft's own dynamic dims (Qwen3.5's

