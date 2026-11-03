---
title: 'Area: src/vllm_torchtpu/structured_decoding'
type: area
area: 'src/vllm_torchtpu/structured_decoding'
description: 'Grammar-constrained decoding on TPU: a runner-owned manager that stages vLLM''s grammar bitmask in pinned host buffers and applies it to padded logits, including speculative target and bonus rows, inside one fixed-shape compiled region.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/structured_decoding`

## Purpose
Structured (grammar-constrained) decoding restricts each request's next token to what its grammar allows. vLLM computes the allowed set on the host as a packed int32 bitmask per request, one bit per vocabulary entry. This area applies that mask to device logits without breaking the TPU fixed-shape rule. The [model runner](../concepts/tpu-model-runner.md) constructs one `StructuredDecodingManager` and calls `mask_logits` on each non-speculative chunk, or `mask_spec_logits` when speculative decoding produces target and bonus rows.

The design keeps the per-step cost to one host-to-device upload and one small compiled kernel. Bitmask and require-mask buffers are preallocated in pinned host memory at the runner's maximum request count. Constant device tensors (a 0..31 bit index and all-true/all-false require masks) are created once. The masking itself is a `torch.compile(backend="tpu", fullgraph=True, dynamic=False)` region that expands the bitmask and applies it with `torch.where`, so rows of requests without a grammar pass through unchanged and padded request rows never change the compiled shape.

Each phase runs under a [trace annotation](../concepts/tracing-annotations.md) (`SD:PrepareInput`, `SD:MaskLogits`, and their spec variants), so its host and device cost shows up by name in a profile.

## How the units connect
- `structured_decoding_manager.py`: `StructuredDecodingManager`. `prepare_structured_decoding_input` / `prepare_spec_structured_decoding_input` copy the scheduler's grammar output into the pinned staging buffers for the current request range (for spec decode, expanding per-request masks over each draft position). `mask_logits` / `mask_spec_logits` then call the compiled `structured_decode`, which applies `apply_grammar_bitmask` only where a request needs it.
- `__init__.py` re-exports the manager. The runner is its only caller; see [runner](runner.md) and, for spec rows, [speculative-decoding](../concepts/speculative-decoding.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/structured_decoding`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/structured_decoding` | 2 | 21 | 5 | [`mask_spec_logits`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.mask_spec_logits "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L273"), [`target_grammar_bitmask_cpu`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.target_grammar_bitmask_cpu "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L79"), [`mask_logits`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.mask_logits "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L244") | section below |

## Small units
### `src/vllm_torchtpu/structured_decoding`
- modules: `src/vllm_torchtpu/structured_decoding/__init__.py`, `src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py`
- entry points: [`mask_spec_logits`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.mask_spec_logits "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L273"), [`target_grammar_bitmask_cpu`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.target_grammar_bitmask_cpu "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L79"), [`mask_logits`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.mask_logits "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L244"), [`structured_decode`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.structured_decode "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L330"), [`StructuredDecodingManager`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L32")
- hubs: [`prepare_spec_structured_decoding_input`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.prepare_spec_structured_decoding_input "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L152"), [`prepare_structured_decoding_input`](../catalog/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.md#StructuredDecodingManager.prepare_structured_decoding_input "src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:L92")

<!-- area:auto:end -->
