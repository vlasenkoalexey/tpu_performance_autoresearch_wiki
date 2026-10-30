---
title: 'Module: torchtitan/hf_datasets/multimodal/utils/video.py'
type: catalog
provenance: extracted
module: torchtitan/hf_datasets/multimodal/utils/video.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.hf_datasets.multimodal.utils.video`/
symbols:
  load_video: load_video().
  process_video: process_video().
---
# Module: [`torchtitan/hf_datasets/multimodal/utils/video.py`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/video.py)

## Functions
- <a id="load_video"></a>`load_video(path: str, fps: float = 2, min_frames: int = 4, max_frames: int = 768)` — [`L19`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/video.py#L19) — Load and sample frames from a video file using PyAV.
- <a id="process_video"></a>`process_video(video: torch.Tensor, patch_size: int, merge_size: int, max_pixels: int, min_pixels: int, image_mean: tuple[float, ...] = (0.5, 0.5, 0.5), image_std: tuple[float, ...] = (0.5, 0.5, 0.5))` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/video.py#L98) — Resize and normalize video frames for VLM training.

