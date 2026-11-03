---
title: 'Module: src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.qwen3_vl_patch`/
symbols:
  _orig_torch_ops._orig_torch_ops: _orig_torch_ops._orig_torch_ops.
  _scoped_qwen3_vl_torch_ops: _scoped_qwen3_vl_torch_ops().
  maybe_patch_qwen3_vl: maybe_patch_qwen3_vl().
  _patch_qwen3_vl_get_rope_index.patched_get_rope_index: _patch_qwen3_vl_get_rope_index().patched_get_rope_index().
  _patch_qwen3_vl_vision_transformer: _patch_qwen3_vl_vision_transformer().
  logger: logger.
  _patch_qwen3_vl_get_rope_index: _patch_qwen3_vl_get_rope_index().
  _patch_qwen3_vl_vision_attention: _patch_qwen3_vl_vision_attention().
  _patched_masked_scatter: _patched_masked_scatter().
  _patch_qwen3_vl_get_rope_index.to_cpu: _patch_qwen3_vl_get_rope_index().to_cpu().
  _patch_qwen3_vl_get_rope_index.to_device: _patch_qwen3_vl_get_rope_index().to_device().
  _qwen3_vl_torch_ops_depth: _qwen3_vl_torch_ops_depth.
  _patched_masked_scatter_: _patched_masked_scatter_().
  _patch_qwen3_vl_vision_attention.patched_vision_attn_forward: _patch_qwen3_vl_vision_attention().patched_vision_attn_forward().
  _patch_qwen3_vl_vision_transformer._make_patched_vision_forward.patched_vision_forward: _patch_qwen3_vl_vision_transformer()._make_patched_vision_forward().patched_vision_forward().
  _patched_repeat_interleave: _patched_repeat_interleave().
  _patched_cumsum: _patched_cumsum().
  _patched_tensor_cumsum: _patched_tensor_cumsum().
  _patch_qwen3_vl_vision_transformer._make_patched_vision_forward: _patch_qwen3_vl_vision_transformer()._make_patched_vision_forward().
  _torch_ops_lock: _torch_ops_lock.
  _is_qwen3_vl_model: _is_qwen3_vl_model().
  _patch_qwen3_vl_get_rope_index.fix_grid: _patch_qwen3_vl_get_rope_index().fix_grid().
  _VISION_MODEL_CANDIDATE_NAMES: _VISION_MODEL_CANDIDATE_NAMES.
---
# Module: [`src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py)

## Functions
- <a id="_is_qwen3_vl_model"></a>`_is_qwen3_vl_model(model_config: Optional[ModelConfig])` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L39) — Check if the provided ModelConfig corresponds to a Qwen3-VL model.
- <a id="_patch_qwen3_vl_vision_transformer._make_patched_vision_forward"></a>`_make_patched_vision_forward(orig_forward)` — [`L351`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L351)
- <a id="_patch_qwen3_vl_get_rope_index"></a>`_patch_qwen3_vl_get_rope_index(modeling)` — [`L215`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L215) — Patch Qwen3VLModel.get_rope_index with signature binding and
- <a id="_patch_qwen3_vl_vision_attention"></a>`_patch_qwen3_vl_vision_attention(modeling)` — [`L296`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L296) — Patch Qwen3VLVisionAttention.forward to ensure cu_seqlens is on CPU.
- <a id="_patch_qwen3_vl_vision_transformer"></a>`_patch_qwen3_vl_vision_transformer(modeling)` — [`L343`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L343) — Patch vision encoder forward to scope PyTorch ops during vision encoding.
- <a id="_patched_cumsum"></a>`_patched_cumsum(input: torch.Tensor, *args, **kwargs)` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L127)
- <a id="_patched_masked_scatter"></a>`_patched_masked_scatter(input: torch.Tensor, mask: torch.Tensor, source: torch.Tensor)` — [`L82`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L82)
- <a id="_patched_masked_scatter_"></a>`_patched_masked_scatter_(self: torch.Tensor, mask: torch.Tensor, source: torch.Tensor)` — [`L55`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L55)
- <a id="_patched_repeat_interleave"></a>`_patched_repeat_interleave(input: torch.Tensor, repeats: torch.Tensor | int, dim: int | None = None, output_size: int | None = None)` — [`L107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L107)
- <a id="_patched_tensor_cumsum"></a>`_patched_tensor_cumsum(self: torch.Tensor, *args, **kwargs)` — [`L138`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L138)
- <a id="_scoped_qwen3_vl_torch_ops"></a>`_scoped_qwen3_vl_torch_ops()` — [`L151`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L151) — Temporarily override PyTorch ops with TPU workarounds during vision execution. — documented in [vllm-model-patches](../../../../../concepts/vllm-model-patches.md)
- <a id="_patch_qwen3_vl_get_rope_index.fix_grid"></a>`fix_grid(g)` — [`L228`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L228)
- <a id="maybe_patch_qwen3_vl"></a>`maybe_patch_qwen3_vl(model_config: Optional[ModelConfig] = None)` — [`L373`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L373) — Apply model-specific and PyTorch XLA op-level patches for Qwen3-VL on TPU.
- <a id="_patch_qwen3_vl_get_rope_index.patched_get_rope_index"></a>`patched_get_rope_index(self, *args, **kwargs)` — [`L261`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L261)
- <a id="_patch_qwen3_vl_vision_attention.patched_vision_attn_forward"></a>`patched_vision_attn_forward(self, *args, **kwargs)` — [`L311`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L311)
- <a id="_patch_qwen3_vl_vision_transformer._make_patched_vision_forward.patched_vision_forward"></a>`patched_vision_forward(self, *args, **kwargs)` — [`L353`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L353)
- <a id="_patch_qwen3_vl_get_rope_index.to_cpu"></a>`to_cpu(t, target_device_box)` — [`L236`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L236)
- <a id="_patch_qwen3_vl_get_rope_index.to_device"></a>`to_device(r, target_device)` — [`L247`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L247)

## Module values
- <a id="_VISION_MODEL_CANDIDATE_NAMES"></a>`_VISION_MODEL_CANDIDATE_NAMES` — [`L334`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L334)
- <a id="_orig_torch_ops._orig_torch_ops"></a>`_orig_torch_ops` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L35) — documented in [vllm-model-patches](../../../../../concepts/vllm-model-patches.md)
- <a id="_qwen3_vl_torch_ops_depth"></a>`_qwen3_vl_torch_ops_depth` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L34)
- <a id="_torch_ops_lock"></a>`_torch_ops_lock` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L36)
- <a id="logger"></a>`logger` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.py#L32)

