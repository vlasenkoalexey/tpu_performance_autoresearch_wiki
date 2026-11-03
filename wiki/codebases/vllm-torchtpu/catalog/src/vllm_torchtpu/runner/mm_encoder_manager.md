---
title: 'Module: src/vllm_torchtpu/runner/mm_encoder_manager.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/mm_encoder_manager.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.mm_encoder_manager`/
symbols:
  MMEncoderManager.execute_dp_coordinated: MMEncoderManager#execute_dp_coordinated().
  MMEncoderManager._capture_budget_graph: MMEncoderManager#_capture_budget_graph().
  MMEncoderManager._run_budget_graph: MMEncoderManager#_run_budget_graph().
  logger: logger.
  MMEncoderManager._execute_local: MMEncoderManager#_execute_local().
  maybe_create_mm_encoder_manager: maybe_create_mm_encoder_manager().
  MMEncoderManager.budget_templates: MMEncoderManager#budget_templates.
  MMEncoderManager.precompile_vision_encoder: MMEncoderManager#precompile_vision_encoder().
  MMEncoderManager.use_dp: MMEncoderManager#use_dp.
  MMEncoderManager._compiled_budget_forward: MMEncoderManager#_compiled_budget_forward.
  MMEncoderManager: MMEncoderManager#
  MMEncoderManager._pad_to_template: MMEncoderManager#_pad_to_template().
  MMEncoderManager._gather_dp_outputs: MMEncoderManager#_gather_dp_outputs().
  _pack_encoder_items: _pack_encoder_items().
  MMEncoderManager.compiled_budgets: MMEncoderManager#compiled_budgets.
  MMEncoderManager.__init__: MMEncoderManager#__init__().
---
# Module: [`src/vllm_torchtpu/runner/mm_encoder_manager.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py)

## Classes
### <a id="MMEncoderManager"></a>`MMEncoderManager`
- def: [`src/vllm_torchtpu/runner/mm_encoder_manager.py:60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L60)
- doc: Per-budget PyTorch XLA-cache manager for the vision encoder forward.
- signature: `class MMEncoderManager(EncoderCudaGraphManager):`
- members:
  - <a id="MMEncoderManager.__init__"></a>`__init__(self, vllm_config: VllmConfig, device: torch.device, vllm_model: torch.nn.Module)` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L87) — Initialize the MMEncoderManager with budget templates and XLA cache.
  - <a id="MMEncoderManager._capture_budget_graph"></a>`_capture_budget_graph(self, token_budget: int, path: str = "default", axis_keys: CaptureAxisKeys = ())` — [`L192`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L192) — Primes the XLA cache for a specific budget bucket.
  - <a id="MMEncoderManager._execute_local"></a>`_execute_local(self, mm_kwargs: dict[str, Any])` — [`L267`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L267) — Execute locally, temporally chunking videos that exceed max budget.
  - <a id="MMEncoderManager._pad_to_template"></a>`_pad_to_template(self, replay_values: dict[str, torch.Tensor | None], budget: int, path: str = "default")` — [`L156`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L156) — Zero-pads dynamic multimodal inputs up to the static budget template.
  - <a id="MMEncoderManager._run_budget_graph"></a>`_run_budget_graph(self, mm_kwargs: dict[str, Any], token_budget: int, path: str = "default", axis_keys: CaptureAxisKeys = (), *, allow_eager_fallback: bool = True)` — [`L219`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L219) — Pads actual inputs and runs the compiled XLA graph.
  - <a id="MMEncoderManager.execute_dp_coordinated"></a>`execute_dp_coordinated(self, mm_kwargs: dict[str, Any] | None, input_error: str | None = None)` — [`L297`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L297) — Run encoding in lockstep across attention-DP engines sharing EP.
  - <a id="MMEncoderManager.precompile_vision_encoder"></a>`precompile_vision_encoder(self)` — [`L406`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L406) — Prime the XLA compilation cache for all configured token budgets.
  - <a id="MMEncoderManager.budget_templates"></a>`budget_templates` — [`L119`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L119)
  - <a id="MMEncoderManager.compiled_budgets"></a>`compiled_budgets` — [`L136`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L136)
  - <a id="MMEncoderManager.use_dp"></a>`use_dp` — [`L113`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L113)
- protocol/private: <a id="MMEncoderManager._compiled_budget_forward"></a>`_compiled_budget_forward`[`L143`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L143), <a id="MMEncoderManager._gather_dp_outputs"></a>`_gather_dp_outputs`[`L373`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L373)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../utils.md#synchronize_tensors), [`embed_multimodal_chunked`](mm_video_chunking.md#embed_multimodal_chunked), [`get_video_chunk_patch_size`](mm_video_chunking.md#get_video_chunk_patch_size), [`logger`](mm_encoder_manager.md#logger), [`_pack_encoder_items`](mm_encoder_manager.md#_pack_encoder_items)
- used by: [`encoder_cudagraph_manager`](tpu_runner.md#TPUModelRunner.encoder_cudagraph_manager), [`_execute_dp_mm_encoder`](tpu_runner.md#TPUModelRunner._execute_dp_mm_encoder), [`maybe_create_mm_encoder_manager`](mm_encoder_manager.md#maybe_create_mm_encoder_manager)

## Functions
- <a id="_pack_encoder_items"></a>`_pack_encoder_items(tokens: list[int], budgets: list[int], max_items: int)` — [`L37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L37)
- <a id="maybe_create_mm_encoder_manager"></a>`maybe_create_mm_encoder_manager(vllm_config: VllmConfig, device: torch.device, vllm_model: torch.nn.Module)` — [`L413`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L413) — Create an MMEncoderManager instance if enabled and supported.

## Module values
- <a id="logger"></a>`logger` — [`L34`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/mm_encoder_manager.py#L34)

