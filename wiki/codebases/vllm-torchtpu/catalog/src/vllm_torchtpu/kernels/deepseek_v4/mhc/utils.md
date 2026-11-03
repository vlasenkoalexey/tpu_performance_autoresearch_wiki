---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.mhc.utils`/
symbols:
  select_token_block: select_token_block().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  pad_to: pad_to().
  trim_to: trim_to().
  split_fn3: split_fn3().
  SUBLANE: SUBLANE.
  round_up: round_up().
  mhc_pre_gates: mhc_pre_gates().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py)

## Functions
- <a id="mhc_pre_gates"></a>`mhc_pre_gates(mixes: jax.Array, sqrsum: jax.Array, hc_mult: int, hidden_size: int, hc_scale: jax.Array, hc_base: jax.Array, rms_eps: float, hc_pre_eps: float, hc_sinkhorn_eps: float, hc_post_mult_value: float, sinkhorn_repeat: int)` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py#L91) — Gating / softmax / Sinkhorn on the tiny (T, hc_mult3) mix logits.
- <a id="pad_to"></a>`pad_to(padded_tokens: int, *arrays: jax.Array)` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py#L57) — Zero-pad the leading (token) axis of each array to ``padded_tokens``.
- <a id="round_up"></a>`round_up(x: int, multiple: int)` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py#L30)
- <a id="select_token_block"></a>`select_token_block(num_tokens: int, token_block_size: int, *, vmem_need: Callable[[int], int] | None = None, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py#L34) — Grid token block, and the token count padded to a multiple of it.
- <a id="split_fn3"></a>`split_fn3(fn: jax.Array)` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py#L72) — 3-chunk bf16 split of fn (8 mantissa bits each = f32's 24).
- <a id="trim_to"></a>`trim_to(num_tokens: int, *arrays: jax.Array)` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py#L65) — Inverse of ``pad_to``: drop the rows the padding added.

## Module values
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py#L27)
- <a id="SUBLANE"></a>`SUBLANE` — [`L22`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/mhc/utils.py#L22)

