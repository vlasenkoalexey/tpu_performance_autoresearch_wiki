---
title: 'Module: torchtitan/hf_datasets/multimodal/utils/text.py'
type: catalog
provenance: extracted
module: torchtitan/hf_datasets/multimodal/utils/text.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.hf_datasets.multimodal.utils.text`/
symbols:
  insert_vision_placeholders: insert_vision_placeholders().
  pad_seq_len: pad_seq_len().
  pad_batch_dim: pad_batch_dim().
---
# Module: [`torchtitan/hf_datasets/multimodal/utils/text.py`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/text.py)

## Functions
- <a id="insert_vision_placeholders"></a>`insert_vision_placeholders(input_parts: list[str | None], num_vision_tokens: list[int], *, vision_start_token: str, vision_token: str, vision_end_token: str, eos_token: str = "")` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/text.py#L70) — Insert vision placeholder token sequences into text.
- <a id="pad_batch_dim"></a>`pad_batch_dim(input_ids: torch.Tensor, labels: torch.Tensor, target_batch_size: int, *, padding_idx: int, ignore_idx: int)` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/text.py#L42) — Pad batch dimension to target size.
- <a id="pad_seq_len"></a>`pad_seq_len(input_ids: torch.Tensor, labels: torch.Tensor, target_len: int, *, padding_idx: int, ignore_idx: int)` — [`L12`](../../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/utils/text.py#L12) — Pad input_ids and labels to desired sequence length.

