import jax
import jax.numpy as jnp
from ejkernel.modules.operations import native_sparse_attention
from ejkernel.modules.operations.configs import NativeSparseAttentionConfig

B, T, HQ, HKV, D = 24, 2048, 32, 4, 128
S = 16
q = jnp.zeros((B, T, HQ, D), dtype=jnp.bfloat16)
k = jnp.zeros((B, T, HKV, D), dtype=jnp.bfloat16)
v = jnp.zeros((B, T, HKV, D), dtype=jnp.bfloat16)
inds = jnp.zeros((B, T, HKV, S), dtype=jnp.int32)
counts = jnp.ones((B, T, HKV), dtype=jnp.int32) * S

cfg = NativeSparseAttentionConfig(block_size=64, platform="pallas", backend="tpu")

def fwd(q, k, v, inds, counts):
    return native_sparse_attention(q, k, v, block_indices=inds, block_counts=counts, platform="pallas", cfg=cfg)

lowered = jax.jit(fwd).lower(q, k, v, inds, counts)
print("Lowered successfully with Pallas!")
