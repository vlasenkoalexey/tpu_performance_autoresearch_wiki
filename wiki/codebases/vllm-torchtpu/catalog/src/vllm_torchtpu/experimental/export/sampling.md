---
title: 'Module: src/vllm_torchtpu/experimental/export/sampling.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/sampling.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.sampling`/
symbols:
  export_samplers: export_samplers().
  uniform_per_logit: uniform_per_logit().
  dispatch_sample_tokens: dispatch_sample_tokens().
  _sample: _sample().
  export_samplers._tensor_entry: export_samplers()._tensor_entry().
  stochastic_tokens: stochastic_tokens().
  penalized_tokens: penalized_tokens().
  temperature_tokens: temperature_tokens().
  greedy_tokens: greedy_tokens().
  _HASH_SEED_STEP: _HASH_SEED_STEP.
  _HASH_MUL_1: _HASH_MUL_1.
  _HASH_MUL_2: _HASH_MUL_2.
---
# Module: [`src/vllm_torchtpu/experimental/export/sampling.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py)

## Functions
- <a id="_sample"></a>`_sample(logits: torch.Tensor, temperature: torch.Tensor, top_k: torch.Tensor, top_p: torch.Tensor, uniform: torch.Tensor, apply_topk_topp: bool)` — [`L57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L57)
- <a id="export_samplers._tensor_entry"></a>`_tensor_entry(arg_index: int, name: str, shape: tuple[int, ...] | list[int], dtype: str, argument_type: str)` — [`L269`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L269)
- <a id="dispatch_sample_tokens"></a>`dispatch_sample_tokens(logits: torch.Tensor, *, temperature: torch.Tensor | None = None, top_k: torch.Tensor | None = None, top_p: torch.Tensor | None = None, min_p: torch.Tensor | None = None, uniform: torch.Tensor | None = None, repetition_penalty: torch.Tensor | None = None, presence_penalty: torch.Tensor | None = None, frequency_penalty: torch.Tensor | None = None, history: torch.Tensor | None = None, output_start: torch.Tensor | None = None)` — [`L153`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L153) — Dispatches `logits` to the greedy, stochastic or penalized sampler.
- <a id="export_samplers"></a>`export_samplers(output_dir: str, subgraph_index: int, logits_shape: tuple[int, ...], logits_dtype: Any, logits_dtype_name: str, history_len: int, *, subdir: str = "")` — [`L215`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L215) — Writes the samplers over `[R, V]` logits and returns their metadata variants. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="greedy_tokens"></a>`greedy_tokens(logits: torch.Tensor)` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L26) — Returns the argmax token id i64[R, 1] of each row of logits[R, V].
- <a id="penalized_tokens"></a>`penalized_tokens(logits: torch.Tensor, temperature: torch.Tensor, top_k: torch.Tensor, top_p: torch.Tensor, min_p: torch.Tensor, uniform: torch.Tensor, repetition_penalty: torch.Tensor, presence_penalty: torch.Tensor, frequency_penalty: torch.Tensor, history: torch.Tensor, output_start: torch.Tensor)` — [`L114`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L114) — Samples one token id i64[R, 1] per row after applying penalties.
- <a id="stochastic_tokens"></a>`stochastic_tokens(logits: torch.Tensor, temperature: torch.Tensor, top_k: torch.Tensor, top_p: torch.Tensor, min_p: torch.Tensor, uniform: torch.Tensor)` — [`L92`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L92) — Samples one token id i64[R, 1] per row of logits[R, V] with top-k / top-p.
- <a id="temperature_tokens"></a>`temperature_tokens(logits: torch.Tensor, temperature: torch.Tensor, uniform: torch.Tensor)` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L77) — Samples one token id i64[R, 1] per row of logits[R, V] at its temperature.
- <a id="uniform_per_logit"></a>`uniform_per_logit(uniform: torch.Tensor, vocab: int)` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L37) — Expands one uniform per row, uniform[R], into one per logit, f32[R, V] in (0, 1).

## Module values
- <a id="_HASH_MUL_1"></a>`_HASH_MUL_1` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L33)
- <a id="_HASH_MUL_2"></a>`_HASH_MUL_2` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L34)
- <a id="_HASH_SEED_STEP"></a>`_HASH_SEED_STEP` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/sampling.py#L32)

