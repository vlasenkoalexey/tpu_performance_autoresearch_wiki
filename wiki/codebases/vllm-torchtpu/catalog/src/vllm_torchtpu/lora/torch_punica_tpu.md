---
title: 'Module: src/vllm_torchtpu/lora/torch_punica_tpu.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/lora/torch_punica_tpu.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.lora.torch_punica_tpu`/
symbols:
  PunicaWrapperTPU.add_expand: PunicaWrapperTPU#add_expand().
  PunicaWrapperTPU.add_lora_embedding: PunicaWrapperTPU#add_lora_embedding().
  PunicaWrapperTPU.add_lora_logits: PunicaWrapperTPU#add_lora_logits().
  PunicaWrapperTPU.update_metadata: PunicaWrapperTPU#update_metadata().
  PunicaWrapperTPU.add_shrink: PunicaWrapperTPU#add_shrink().
  PunicaWrapperTPU._token_lora_indices: PunicaWrapperTPU#_token_lora_indices.
  PunicaWrapperTPU.add_lora_linear: PunicaWrapperTPU#add_lora_linear().
  PunicaWrapperTPU._sampler_indices: PunicaWrapperTPU#_sampler_indices.
  PunicaWrapperTPU._embeddings_indices: PunicaWrapperTPU#_embeddings_indices.
  PunicaWrapperTPU.index_buffer: PunicaWrapperTPU#index_buffer().
  _write_head: _write_head().
  _add_delta: _add_delta().
  _resolve_add_inputs: _resolve_add_inputs().
  PunicaWrapperTPU: PunicaWrapperTPU#
  PunicaWrapperTPU.__init__: PunicaWrapperTPU#__init__().
  PunicaWrapperTPU.apply_lora_full_linear: PunicaWrapperTPU#apply_lora_full_linear().
---
# Module: [`src/vllm_torchtpu/lora/torch_punica_tpu.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py)

## Classes
### <a id="PunicaWrapperTPU"></a>`PunicaWrapperTPU`
- def: [`src/vllm_torchtpu/lora/torch_punica_tpu.py:29`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L29)
- doc: Punica wrapper for TPU.
- signature: `class PunicaWrapperTPU(PunicaWrapperBase):`
- members:
  - <a id="PunicaWrapperTPU.add_expand"></a>`add_expand(self, y: torch.Tensor, x: tuple[torch.Tensor, ...] | torch.Tensor, lora_b_stacked: tuple[torch.Tensor, ...], output_slices: tuple[int, ...], offset_start: int = 0, add_inputs: bool | None = None, **kwargs)` — [`L122`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L122) — Performs GEMM for multiple slices of lora_b.
  - <a id="PunicaWrapperTPU.add_lora_embedding"></a>`add_lora_embedding(self, y: torch.Tensor, x: torch.Tensor, lora_b_stacked: torch.Tensor, add_inputs: bool | None = None, **kwargs)` — [`L169`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L169) — Applies LoRA for VocabParallelEmbeddingWithLoRA.
  - <a id="PunicaWrapperTPU.add_lora_linear"></a>`add_lora_linear(self, y: torch.Tensor, x: torch.Tensor, lora_a_stacked: tuple[torch.Tensor, ...], lora_b_stacked: tuple[torch.Tensor, ...], scale: float, output_slices: tuple[int, ...], *, buffer: tuple[torch.Tensor, ...] | None = None, **kwargs)` — [`L201`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L201) — Applies LoRA for linear layers: add_shrink, then add_expand.
  - <a id="PunicaWrapperTPU.add_lora_logits"></a>`add_lora_logits(self, y: torch.Tensor, x: torch.Tensor, lora_a_stacked: torch.Tensor, lora_b_stacked: torch.Tensor, scale: float, *, buffer: torch.Tensor | None = None, **kwargs)` — [`L238`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L238) — Applies LoRA for LogitsProcessorWithLoRA.
  - <a id="PunicaWrapperTPU.add_shrink"></a>`add_shrink(self, y: tuple[torch.Tensor, ...] | torch.Tensor | None, x: torch.Tensor, lora_a_stacked: tuple[torch.Tensor, ...], scale: float, **kwargs)` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L90) — Performs GEMM for multiple slices of lora_a.
  - <a id="PunicaWrapperTPU.apply_lora_full_linear"></a>`apply_lora_full_linear(self, y: torch.Tensor, x: torch.Tensor, weight_stacked: torch.Tensor, bias_stacked: torch.Tensor, module_enabled: torch.Tensor)` — [`L277`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L277) — Applies an adapter's full classification head. Not supported on TPU.
  - <a id="PunicaWrapperTPU.index_buffer"></a>`index_buffer()` — [`L51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L51)
  - <a id="PunicaWrapperTPU.update_metadata"></a>`update_metadata(self, mapping: LoRAMapping, lora_index_to_id: list[int | None], max_loras: int, vocab_size: int, **kwargs)` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L58)
- protocol/private: <a id="PunicaWrapperTPU.__init__"></a>`__init__`[`L38`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L38), <a id="PunicaWrapperTPU._embeddings_indices"></a>`_embeddings_indices`[`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L56), <a id="PunicaWrapperTPU._sampler_indices"></a>`_sampler_indices`[`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L55), <a id="PunicaWrapperTPU._token_lora_indices"></a>`_token_lora_indices`[`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L54)
- uses (calls/refs, reference-scoped): [`one_hot_slots`](lora_ops.md#one_hot_slots), [`bgmv_expand`](lora_ops.md#bgmv_expand), [`_add_delta`](torch_punica_tpu.md#_add_delta), [`_write_head`](torch_punica_tpu.md#_write_head), [`bgmv_shrink`](lora_ops.md#bgmv_shrink), [`_resolve_add_inputs`](torch_punica_tpu.md#_resolve_add_inputs)

## Functions
- <a id="_add_delta"></a>`_add_delta(y: torch.Tensor, delta: torch.Tensor, offset: int, add_inputs: bool)` — [`L323`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L323) — Lays delta over y's columns from offset on. Columns it does not reach,
- <a id="_resolve_add_inputs"></a>`_resolve_add_inputs(add_inputs: bool | None, kwargs: dict)` — [`L309`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L309) — vLLM's PunicaWrapperBase names the flag add_inputs, but its LoRA layers
- <a id="_write_head"></a>`_write_head(buf: torch.Tensor, values: np.ndarray)` — [`L298`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/torch_punica_tpu.py#L298) — Writes values to the head of buf. The runner pads the mapping to the

