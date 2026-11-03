---
title: 'Module: src/vllm_torchtpu/lora/lora_ops.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/lora/lora_ops.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.lora.lora_ops`/
symbols:
  one_hot_slots: one_hot_slots().
  bgmv_expand: bgmv_expand().
  bgmv_shrink: bgmv_shrink().
---
# Module: [`src/vllm_torchtpu/lora/lora_ops.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_ops.py)

## Functions
- <a id="bgmv_expand"></a>`bgmv_expand(buf: torch.Tensor, lora_b_stacked: torch.Tensor, onehot: torch.Tensor)` — [`L73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_ops.py#L73) — Projects each token from rank space back out through its adapter.
- <a id="bgmv_shrink"></a>`bgmv_shrink(x: torch.Tensor, lora_a_stacked: torch.Tensor, onehot: torch.Tensor, scale: float)` — [`L42`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_ops.py#L42) — Projects each token into the rank space of its adapter.
- <a id="one_hot_slots"></a>`one_hot_slots(idx: torch.Tensor, num_slots: int)` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_ops.py#L35) — Returns a [T, num_slots] bool mask of each token's slot; slots outside

