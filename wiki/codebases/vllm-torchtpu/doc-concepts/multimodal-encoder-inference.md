---
title: Multimodal (vision-language) inference and the budgeted vision-encoder graphs
type: doc-concept
provenance: doc
source: docs/api_and_code_examples/multi_modal_inference.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Multimodal (vision-language) inference and the budgeted vision-encoder graphs

## Definition
The multimodal example (`examples/multi_modal_inference.py`, also quickstart section 3) runs
offline image+text generation on `Qwen/Qwen2.5-VL-3B-Instruct`: one image per prompt
(`limit_mm_per_prompt` sets every other modality to 0 "to save memory"), image resolution
bounded by `min_pixels`/`max_pixels` processor kwargs, `max_num_seqs=5`, sampling at temperature
0.2. On TPU the hard part is the vision encoder: image token counts vary with resolution and
aspect ratio, while TPU graphs are static-shape.

## In vllm-torchtpu (grounded)
- [`MMEncoderManager`](../catalog/src/vllm_torchtpu/runner/mm_encoder_manager.md#MMEncoderManager)
  is the TPU answer to GPU encoder CUDA graphs: it maps variable encoder inputs onto a discrete
  set of static **token budgets** (e.g. 256 / 512 / 1024 / 2048), compiles the model's
  `encoder_cudagraph_forward` once per budget with `torch.compile(backend="tpu", fullgraph=True,
  dynamic=False)`, greedily packs incoming images into the smallest fitting budget and zero-pads
  to its template.
  [`precompile_vision_encoder`](../catalog/src/vllm_torchtpu/runner/mm_encoder_manager.md#MMEncoderManager.precompile_vision_encoder)
  warms every budget during [`capture_model`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.capture_model).
- It is **opt-in**: [`maybe_create_mm_encoder_manager`](../catalog/src/vllm_torchtpu/runner/mm_encoder_manager.md#maybe_create_mm_encoder_manager)
  returns None unless `compilation_config.cudagraph_mm_encoder` is true, the model implements the
  encoder-cudagraph interface, and it declares no capture axes. Otherwise the runner uses the eager
  `embed_multimodal` path with no budget padding.
- vLLM's `--mm-encoder-tp-mode data` makes the encoder data-parallel across the TP ranks: the
  manager's `use_dp` is set when the model reports `use_data_parallel` and TP > 1, so images are
  split across ranks and gathered instead of every rank encoding every image.
- For **attention DP + EP** deployments the runner requires the manager (it raises otherwise) and
  calls [`execute_dp_coordinated`](../catalog/src/vllm_torchtpu/runner/mm_encoder_manager.md#MMEncoderManager.execute_dp_coordinated)
  so all DP engines sharing EP encode in lockstep; this path accepts images only, no LoRA, and one
  image batch per step.
- Long videos go through `runner/mm_video_chunking.py`
  ([`embed_multimodal_chunked`](../catalog/src/vllm_torchtpu/runner/mm_video_chunking.md#embed_multimodal_chunked)).

Owning modules: `runner/mm_encoder_manager.py`, `runner/mm_video_chunking.py`,
`runner/tpu_runner.py`.

## Why it matters / when it applies
- **Encoder compile behavior is a config choice.** The CI multimodal recipe for gemma-4-31B sets
  `--compilation-config '{"cudagraph_mm_encoder":true,"encoder_cudagraph_max_vision_items_per_batch":8,
  "encoder_cudagraph_max_frames_per_batch":8}'`, `--disable-chunked-mm-input` and
  `mm-encoder-tp-mode` data (measured 6477 output tok/s at 1k/1k, concurrency 128, on v7x-8; see
  [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md)). The example sets none of these,
  so it measures the eager encoder path.
- **Budget padding is wasted compute.** Images that land just above a budget pay for the next one;
  `max_pixels` and the items-per-batch caps trade padding waste against the number of compiled
  graphs.
- **Text-only serving of VLM checkpoints.** The large-MoE recipes pass `--language-model-only`
  and `--limit-mm-per-prompt '{"image":0,"video":0}'` so no encoder memory or graphs are reserved.

## Doc vs code at this commit
- The gemma-4-31B CI config passes the encoder mode as `--additional_config
  '{"mm-encoder-tp-mode":"data"}'`, a key no module under `src/vllm_torchtpu` reads, while its
  gemma-4-26B sibling config uses the real vLLM flag `--mm-encoder-tp-mode data`. The 31B
  baseline may therefore have been measured with the default (weights-sharded) encoder mode.
- The quickstart says vllm-torchtpu supports VLMs "such as Qwen/Qwen2.5-VL-3B-Instruct and
  Qwen/Qwen3.5-397B-A17B" right above the example command, but the example hard-codes the
  Qwen2.5-VL prompt template (`model_example_map["qwen2_5_vl"]`, with the comment "Currently, only
  Qwen2.5-VL is supported") and only the image modality (video is commented out). Passing another
  `--model` reuses the Qwen2.5-VL chat format.

## Connections
- Code concepts: [tpu-model-runner](../concepts/tpu-model-runner.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [kimi-k3-model](../concepts/kimi-k3-model.md) (implements the encoder-cudagraph interface).
- Module catalogs: [runner/mm_encoder_manager](../catalog/src/vllm_torchtpu/runner/mm_encoder_manager.md),
  [runner/mm_video_chunking](../catalog/src/vllm_torchtpu/runner/mm_video_chunking.md).
- Related doc-concepts: [offline-inference-example](offline-inference-example.md),
  [token-padding-buckets](token-padding-buckets.md),
  [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md).

## Source
Extracted from `docs/api_and_code_examples/multi_modal_inference.md` (which embeds
`examples/multi_modal_inference.py`) and quickstart section 3 (kept in place).
