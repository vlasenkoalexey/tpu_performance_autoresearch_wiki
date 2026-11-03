---
title: 'Module: src/vllm_torchtpu/runner/greedy_top_tokens.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/greedy_top_tokens.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.greedy_top_tokens`/
symbols:
  logger: logger.
  log_step_path: log_step_path().
  step_eligible: step_eligible().
  top_tokens: top_tokens().
  resolve_head_owner: resolve_head_owner().
---
# Module: [`src/vllm_torchtpu/runner/greedy_top_tokens.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/greedy_top_tokens.py)

## Functions
- <a id="log_step_path"></a>`log_step_path(is_spec_step: bool, req_ids: Sequence[str | None])` — [`L111`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/greedy_top_tokens.py#L111) — Logs, once per path, that a step's tokens came from the top tokens.
- <a id="resolve_head_owner"></a>`resolve_head_owner(model: torch.nn.Module, dp_lockstep: bool)` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/greedy_top_tokens.py#L46) — The module holding ``lm_head`` and its ``logits_processor``.
- <a id="step_eligible"></a>`step_eligible(input_batch: InputBatch, requests: Mapping[str, CachedRequestState])` — [`L129`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/greedy_top_tokens.py#L129) — Whether the step's tokens are fully determined by the top tokens:
- <a id="top_tokens"></a>`top_tokens(owner: torch.nn.Module, hidden_states: torch.Tensor)` — [`L95`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/greedy_top_tokens.py#L95) — The greedy token of each row, ``[rows, 1]`` int64 like

## Module values
- <a id="logger"></a>`logger` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/greedy_top_tokens.py#L43)

