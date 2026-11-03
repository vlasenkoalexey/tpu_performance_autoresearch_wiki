---
title: 'Module: src/vllm_torchtpu/kernels/kimi_k3/attention_residual.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/kimi_k3/attention_residual.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.kimi_k3.attention_residual`/
symbols:
  attention_residual: attention_residual().
  _mix_kernel: _mix_kernel().
---
# Module: [`src/vllm_torchtpu/kernels/kimi_k3/attention_residual.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/attention_residual.py)

## Functions
- <a id="_mix_kernel"></a>`_mix_kernel(prefix, history, weight, output, *, eps)` — [`L24`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/attention_residual.py#L24) — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)
- <a id="attention_residual"></a>`attention_residual(prefix, history, folded_weight, *, eps=0.00001, interpret=False)` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/kimi_k3/attention_residual.py#L37) — Mix [tokens,hidden] prefix and [tokens,blocks,hidden] saved blocks. — documented in [kimi-k3-kernels](../../../../../concepts/kimi-k3-kernels.md)

