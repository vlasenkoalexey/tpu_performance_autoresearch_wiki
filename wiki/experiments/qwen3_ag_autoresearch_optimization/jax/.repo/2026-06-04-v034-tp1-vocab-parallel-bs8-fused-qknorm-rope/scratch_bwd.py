import jax
import jax.numpy as jnp
from model.fused_rope import fused_qknorm_rope

B, H, T, D = 64, 8, 2048, 128
x = jnp.ones((B, H, T, D), dtype=jnp.bfloat16)
w = jnp.ones((D,), dtype=jnp.bfloat16)
cos = jnp.ones((B, T, D), dtype=jnp.bfloat16)
sin = jnp.ones((B, T, D), dtype=jnp.bfloat16)
eps = 1e-6

def loss_fn(x, w, cos, sin):
    out = fused_qknorm_rope(x, w, cos, sin, eps)
    return jnp.sum(out)

grad_fn = jax.grad(loss_fn, argnums=(0, 1, 2, 3))
g_x, g_w, g_cos, g_sin = grad_fn(x, w, cos, sin)
print("SUCCESS!")
