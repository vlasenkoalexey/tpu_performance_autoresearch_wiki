---
title: 'Module: src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.moe_dense_expert`/
symbols:
  dense_expert_moe: dense_expert_moe().
  _kernel: _kernel().
  _kernel.run_experts.expert_body: _kernel().run_experts().expert_body().
  _kernel.transfers: _kernel().transfers().
  _select_expert_buffers: _select_expert_buffers().
  _kernel.compute: _kernel().compute().
  _kernel.run_experts: _kernel().run_experts().
  _kernel.run_experts.prime: _kernel().run_experts().prime().
  _kernel.run_experts.expert_body.prefetch: _kernel().run_experts().expert_body().prefetch().
  can_use_dense_expert: can_use_dense_expert().
  _quantize: _quantize().
  _MAX_EXPERT_BUFFERS: _MAX_EXPERT_BUFFERS.
  _kernel.compact: _kernel().compact().
  _kernel.compact.record: _kernel().compact().record().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py)

## Functions
- <a id="_kernel"></a>`_kernel(active_ref, x_ref, coeff_ref, w1_hbm, w2_hbm, s1_hbm, s2_hbm, out_ref, w1_ref, w2_ref, s1_ref, s2_ref, xq_ref, xs_ref, a_ref, aq_ref, asc_ref, owner_ref, active_ids_ref, sem_ref, *, m, h, i, experts, num_buffers)` — [`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L106)
- <a id="_quantize"></a>`_quantize(x, q_ref, scale_ref)` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L94) — Quantize activations to FP8 in up-to-512-wide blocks with BF16 scales.
- <a id="_select_expert_buffers"></a>`_select_expert_buffers(m, h, i, experts, vmem_capacity_bytes)` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L33) — Choose up to three slots, reserving 20% for padding and temporaries.
- <a id="can_use_dense_expert"></a>`can_use_dense_expert(hidden, w1, w2, s1, s2, b1, b2, *, activation, rhs_quant_dtype, skip_padded_tokens)` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L50) — Check arithmetic/layout support; the compiler owns resource limits.
- <a id="_kernel.compact"></a>`compact(e, count)` — [`L183`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L183)
- <a id="_kernel.compute"></a>`compute(e, w1_ref, w2_ref, s1_ref, s2_ref)` — [`L138`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L138)
- <a id="dense_expert_moe"></a>`dense_expert_moe(hidden, w1, w2, s1, s2, topk_weights, local_ids)` — [`L247`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L247) — Local routed contribution, same [tokens, hidden]/BF16 output as GMM.
- <a id="_kernel.run_experts.expert_body"></a>`expert_body(step, _)` — [`L214`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L214)
- <a id="_kernel.run_experts.expert_body.prefetch"></a>`prefetch()` — [`L224`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L224)
- <a id="_kernel.run_experts.prime"></a>`prime(*, initial=initial)` — [`L210`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L210)
- <a id="_kernel.compact.record"></a>`record()` — [`L185`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L185)
- <a id="_kernel.run_experts"></a>`run_experts()` — [`L206`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L206)
- <a id="_kernel.transfers"></a>`transfers(step)` — [`L192`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L192)

## Module values
- <a id="_MAX_EXPERT_BUFFERS"></a>`_MAX_EXPERT_BUFFERS` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/moe_dense_expert.py#L30)

