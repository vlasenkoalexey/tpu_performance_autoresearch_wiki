# Retrospective: v059c and Splash Attention Transpose Bug

## Context
During the autoresearch loop, `v059c` OOM'd at compile time on a v6e TPU with "program requires 52.16G HBM". The HLO dump showed massive intermediate tensors of shape `36, 4, 4096, 12288` taking up 13.50GB of memory.

## Analysis
Investigation of `modeling_qwen3.py` and `splash_attn.py` revealed a critical transpose bug:
1. `_attn_splash` was mapped using `q_sharding = P("fsdp", "tp", None, None)` for inputs of shape `(B, H, T, Dh)`.
2. The `splash_attn` kernel outputs `(B, H, T, Dh)` naturally due to the passed inputs, but `modeling_qwen3.py` reshapes the output directly via `attn_out.reshape(B, T, self.num_heads * self.head_dim)`.
3. Because there was no transpose between `(B, H, T, Dh)` and `(B, T, H * Dh)`, the `T` and `H` dimensions were physically scrambled. 
4. Even worse, since `H` is sharded over `tp` by the attention kernel, the new `T` dimension became partially sharded on `tp`. To satisfy the downstream Megatron-LM MLP which expects the residual `T` dimension to be replicated (or sharded on sequence, not heads), XLA was forced to insert massive AllToAlls and unsharded the MLP dimension locally.
5. This caused the 13.50GB OOM tensor `(36, 4, 4096, 12288)` to materialize fully in the MLP during the scan over layers.

## Resolution
The bug was fixed by adding `attn_out = jnp.transpose(attn_out, (0, 2, 1, 3))` right after `_attn_splash` returns.
This hypothesis was formulated as `v059d` and is currently running on the `alekseyv-tpu-v6e8-spot-xpk` cluster.
