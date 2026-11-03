---
title: 'Module: src/vllm_torchtpu/omni/rope.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/omni/rope.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.omni.rope`/
symbols:
  wan_self_attention_fused: wan_self_attention_fused().
  apply_rotary_pair_swap: apply_rotary_pair_swap().
  _qk_norm_rope_op: _qk_norm_rope_op().
  rotary_embedding_wan_forward: rotary_embedding_wan_forward().
  split_rope_natural_tables: split_rope_natural_tables().
  apply_split_rotary_half_swap: apply_split_rotary_half_swap().
  wan_self_attention_fused.table: wan_self_attention_fused().table().
  _qk_norm_rope_op.wan_qk_norm_rope: _qk_norm_rope_op().wan_qk_norm_rope().
  _repeat_pairs: _repeat_pairs().
  split_rope_natural_tables.natural: split_rope_natural_tables().natural().
  can_fuse_qk_norm_rope: can_fuse_qk_norm_rope().
  _pair_swap_matrix: _pair_swap_matrix().
  _first_half_lanes: _first_half_lanes().
  _qk_norm_rope_op.fake: _qk_norm_rope_op().fake().
---
# Module: [`src/vllm_torchtpu/omni/rope.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py)

## Functions
- <a id="_first_half_lanes"></a>`_first_half_lanes(width: int, head_dim: int, device: torch.device)` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L90)
- <a id="_pair_swap_matrix"></a>`_pair_swap_matrix(dim: int, dtype: torch.dtype, device: torch.device)` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L46)
- <a id="_qk_norm_rope_op"></a>`_qk_norm_rope_op()` — [`L143`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L143) — Builds the torch custom op wrapping the fused Pallas kernel (once). — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_repeat_pairs"></a>`_repeat_pairs(t: torch.Tensor)` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L56) — ``(..., D/2) -> (..., D)`` repeating each entry for its (even, odd) pair.
- <a id="apply_rotary_pair_swap"></a>`apply_rotary_pair_swap(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor)` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L61) — Interleaved RoPE of ``x`` (..., D) with half-dim ``cos``/``sin`` (..., D/2). — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="apply_split_rotary_half_swap"></a>`apply_split_rotary_half_swap(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor, head_dim: int)` — [`L116`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L116) — Split RoPE of ``x`` (B, T, H * D) with ``split_rope_natural_tables`` tables. — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="can_fuse_qk_norm_rope"></a>`can_fuse_qk_norm_rope(attn, hidden_states: torch.Tensor, rotary_emb: tuple | None)` — [`L167`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L167) — Whether a WanSelfAttention call fits the fused q/k norm + RoPE kernel.
- <a id="_qk_norm_rope_op.fake"></a>`fake(qkv, wq, wk, cos, sin, eps, head_dim)` — [`L159`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L159)
- <a id="split_rope_natural_tables.natural"></a>`natural(first: torch.Tensor, second: torch.Tensor)` — [`L106`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L106)
- <a id="rotary_embedding_wan_forward"></a>`rotary_embedding_wan_forward(self, x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor)` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L75) — Drop-in ``RotaryEmbeddingWan.forward`` for bf16 interleaved half-dim tables. — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="split_rope_natural_tables"></a>`split_rope_natural_tables(cos: torch.Tensor, sin: torch.Tensor)` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L94) — LTX-2 split-RoPE tables ``(B, H, T, D/2) -> (B, 1, T, H * D)``. — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="wan_self_attention_fused.table"></a>`table(t: torch.Tensor)` — [`L198`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L198) — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
- <a id="_qk_norm_rope_op.wan_qk_norm_rope"></a>`wan_qk_norm_rope(qkv: jax.Array, wq: jax.Array, wk: jax.Array, cos: jax.Array, sin: jax.Array, eps: float, head_dim: int)` — [`L146`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L146)
- <a id="wan_self_attention_fused"></a>`wan_self_attention_fused(attn, hidden_states: torch.Tensor, rotary_emb: tuple, attn_metadata=None)` — [`L186`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/omni/rope.py#L186) — ``WanSelfAttention.forward`` with the fused q/k norm + RoPE kernel. — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)

