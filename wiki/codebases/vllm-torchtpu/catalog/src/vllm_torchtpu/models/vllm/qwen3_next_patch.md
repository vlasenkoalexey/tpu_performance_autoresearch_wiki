---
title: 'Module: src/vllm_torchtpu/models/vllm/qwen3_next_patch.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/qwen3_next_patch.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.qwen3_next_patch`/
symbols:
  maybe_patch_qwen3_next: maybe_patch_qwen3_next().
  logger: logger.
  patched_decoder_layer_forward: patched_decoder_layer_forward().
  patched_model_forward: patched_model_forward().
  _check_tokens_divide_by_tp: _check_tokens_divide_by_tp().
  UPSTREAM_DECODER_LAYER_FORWARD: UPSTREAM_DECODER_LAYER_FORWARD.
  UPSTREAM_MODEL_FORWARD: UPSTREAM_MODEL_FORWARD.
---
# Module: [`src/vllm_torchtpu/models/vllm/qwen3_next_patch.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_next_patch.py)

## Functions
- <a id="_check_tokens_divide_by_tp"></a>`_check_tokens_divide_by_tp(num_tokens: int)` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_next_patch.py#L49)
- <a id="maybe_patch_qwen3_next"></a>`maybe_patch_qwen3_next(*args: object, **kwargs: object)` — [`L189`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_next_patch.py#L189) — Install trace-stable forwards when TPU_MOE_SEQUENCE_PARALLEL=1.
- <a id="patched_decoder_layer_forward"></a>`patched_decoder_layer_forward(self, hidden_states: torch.Tensor, residual: torch.Tensor | None, positions: torch.Tensor, **kwargs: object)` — [`L55`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_next_patch.py#L55)
- <a id="patched_model_forward"></a>`patched_model_forward(self, input_ids: torch.Tensor | None, positions: torch.Tensor, intermediate_tensors: IntermediateTensors | None = None, inputs_embeds: torch.Tensor | None = None)` — [`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_next_patch.py#L126)

## Module values
- <a id="UPSTREAM_DECODER_LAYER_FORWARD"></a>`UPSTREAM_DECODER_LAYER_FORWARD` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_next_patch.py#L45)
- <a id="UPSTREAM_MODEL_FORWARD"></a>`UPSTREAM_MODEL_FORWARD` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_next_patch.py#L46)
- <a id="logger"></a>`logger` — [`L43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_next_patch.py#L43)

