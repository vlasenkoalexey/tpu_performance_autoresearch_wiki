---
title: 'Module: src/vllm_torchtpu/experimental/export/random_sample.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/random_sample.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.random_sample`/
symbols:
  sample_from_logits: sample_from_logits().
  SAMPLING_EPS: SAMPLING_EPS.
  apply_temperature: apply_temperature().
---
# Module: [`src/vllm_torchtpu/experimental/export/random_sample.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/random_sample.py)

## Functions
- <a id="apply_temperature"></a>`apply_temperature(logits: torch.Tensor, temperatures: torch.Tensor)` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/random_sample.py#L35) — Divides logits by the temperature; a zero temperature divides by 1.
- <a id="sample_from_logits"></a>`sample_from_logits(logits: torch.Tensor, temperatures: torch.Tensor, u: torch.Tensor, top_k: torch.Tensor, top_p: torch.Tensor, all_greedy: bool = False, topk_candidates: int = 0, apply_topk_topp: bool = True)` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/random_sample.py#L41) — Samples one token id per row of logits[R, V]; returns [R, 1].

## Module values
- <a id="SAMPLING_EPS"></a>`SAMPLING_EPS` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/random_sample.py#L32)

