---
title: 'Module: src/vllm_torchtpu/worker/runai_repull.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/worker/runai_repull.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.worker.runai_repull`/
symbols:
  ensure_runai_aux_files: ensure_runai_aux_files().
  _is_complete: _is_complete().
  logger: logger.
  _report_tokenizer_gap: _report_tokenizer_gap().
  PULLING_SENTINEL: PULLING_SENTINEL.
  _touch: _touch().
  COMPLETE_SENTINEL: COMPLETE_SENTINEL.
---
# Module: [`src/vllm_torchtpu/worker/runai_repull.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/runai_repull.py)

## Functions
- <a id="_is_complete"></a>`_is_complete(local_dir: str)` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/runai_repull.py#L85)
- <a id="_report_tokenizer_gap"></a>`_report_tokenizer_gap(model_config)` — [`L146`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/runai_repull.py#L146) — A tokenizer served from a different object-storage URI than the
- <a id="_touch"></a>`_touch(path: str, content: str)` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/runai_repull.py#L80)
- <a id="ensure_runai_aux_files"></a>`ensure_runai_aux_files(model_config)` — [`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/runai_repull.py#L96) — Make sure this host has the model's Run:AI aux files and that

## Module values
- <a id="COMPLETE_SENTINEL"></a>`COMPLETE_SENTINEL` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/runai_repull.py#L77)
- <a id="PULLING_SENTINEL"></a>`PULLING_SENTINEL` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/runai_repull.py#L76)
- <a id="logger"></a>`logger` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/runai_repull.py#L74)

