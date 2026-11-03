---
title: 'Module: src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.qwen3_5_mtp`/
symbols:
  _predictor_forward: _predictor_forward().
  UPSTREAM_PREDICTOR_FORWARD: UPSTREAM_PREDICTOR_FORWARD.
  Qwen3_5MTP: Qwen3_5MTP#
  Qwen3_5MTP.supports_pp: Qwen3_5MTP#supports_pp.
  Qwen3_5MoeMTP: Qwen3_5MoeMTP#
  Qwen3_5MoeMTP.supports_pp: Qwen3_5MoeMTP#supports_pp.
---
# Module: [`src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py)

## Classes
### <a id="Qwen3_5MTP"></a>`Qwen3_5MTP`
- def: [`src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py:85`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py#L85)
- doc: Upstream's draft, admitted under pipeline parallelism.
- signature: `class Qwen3_5MTP(upstream.Qwen3_5MTP):`
- members:
  - <a id="Qwen3_5MTP.supports_pp"></a>`supports_pp` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py#L97)

### <a id="Qwen3_5MoeMTP"></a>`Qwen3_5MoeMTP`
- def: [`src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py:100`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py#L100)
- doc: The MoE draft, admitted under pipeline parallelism; see `Qwen3_5MTP`.
- signature: `class Qwen3_5MoeMTP(upstream.Qwen3_5MoeMTP):`
- members:
  - <a id="Qwen3_5MoeMTP.supports_pp"></a>`supports_pp` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py#L103)

## Functions
- <a id="_predictor_forward"></a>`_predictor_forward(self: upstream.Qwen3_5MultiTokenPredictor, input_ids: torch.Tensor, positions: torch.Tensor, hidden_states: torch.Tensor, intermediate_tensors: IntermediateTensors | None = None, inputs_embeds: torch.Tensor | None = None, spec_step_idx: int = 0)` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py#L28) — Upstream's forward, branching on the inputs instead of the PP rank.

## Module values
- <a id="UPSTREAM_PREDICTOR_FORWARD"></a>`UPSTREAM_PREDICTOR_FORWARD` — [`L25`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_5_mtp.py#L25)

