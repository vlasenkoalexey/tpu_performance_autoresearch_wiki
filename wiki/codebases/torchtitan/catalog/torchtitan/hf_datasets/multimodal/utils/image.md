---
title: 'Module: torchtitan/hf_datasets/multimodal/utils/image.py'
type: catalog
provenance: extracted
module: torchtitan/hf_datasets/multimodal/utils/image.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.hf_datasets.multimodal.utils.image`/
symbols:
  process_image: process_image().
  resize_to_pixel_budget: resize_to_pixel_budget().
  resize_to_navit_patch_grid: resize_to_navit_patch_grid().
  smart_resize: smart_resize().
  calculate_vision_tokens: calculate_vision_tokens().
  vision_to_patches: vision_to_patches().
  _decode_image: _decode_image().
---
# Module: [`torchtitan/hf_datasets/multimodal/utils/image.py`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/image.py)

## Functions
- <a id="_decode_image"></a>`_decode_image(image: str | bytes | Image.Image)` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/image.py#L29) — Decode an image to a (C, H, W) uint8 RGB tensor.
- <a id="calculate_vision_tokens"></a>`calculate_vision_tokens(num_frames: int, height: int, width: int, patch_size: int, spatial_merge_size: int, temporal_patch_size: int)` — [`L280`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/image.py#L280) — Calculate the number of visual tokens after patching and merging.
- <a id="process_image"></a>`process_image(image: str | bytes | Image.Image, patch_size: int = 16, merge_size: int = 2, max_pixels: int = 16777216, min_pixels: int = 65536, image_mean: tuple[float, ...] = (0.5, 0.5, 0.5), image_std: tuple[float, ...] = (0.5, 0.5, 0.5), resize_fn: Callable[..., tuple[int, int, int, int]] = resize_to_pixel_budget, max_patches: int = 4096, max_patches_per_side: int = 512)` — [`L200`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/image.py#L200) — Load and preprocess a single image for VLM training. — documented in [hf-datasets](../../../../../concepts/hf-datasets.md)
- <a id="resize_to_navit_patch_grid"></a>`resize_to_navit_patch_grid(height: int, width: int, *, patch_size: int, merge_size: int, max_patches: int, max_patches_per_side: int, **_: object)` — [`L148`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/image.py#L148) — Apply pre-padding total and per-side raw-patch budgets while preserving
- <a id="resize_to_pixel_budget"></a>`resize_to_pixel_budget(height: int, width: int, *, patch_size: int, merge_size: int, min_pixels: int, max_pixels: int, **_: object)` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/image.py#L94) — Resize so the spatial pixel count lands in ``[min_pixels, max_pixels]``, — documented in [hf-datasets](../../../../../concepts/hf-datasets.md)
- <a id="smart_resize"></a>`smart_resize(height: int, width: int, factor: int, min_pixels: int, max_pixels: int)` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/image.py#L50) — Compute target (height, width) that satisfy per-frame pixel budget.
- <a id="vision_to_patches"></a>`vision_to_patches(img: torch.Tensor, patch_size: int, temporal_patch_size: int, merge_size: int, patch_order: str = "block")` — [`L308`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/image.py#L308) — Convert an image/video tensor to flattened patches.

