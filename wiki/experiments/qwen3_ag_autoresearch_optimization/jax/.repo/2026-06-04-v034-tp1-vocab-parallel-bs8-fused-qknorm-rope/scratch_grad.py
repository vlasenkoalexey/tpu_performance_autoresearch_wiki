import jax
import jax.numpy as jnp

from model.fused_rope import fused_qknorm_rope

B, H, T, D = 8, 32, 256, 128
x = jax.random.normal(jax.random.PRNGKey(0), (B, H, T, D))
weight = jax.random.normal(jax.random.PRNGKey(1), (D,))
cos = jax.random.normal(jax.random.PRNGKey(2), (B, T, D))
sin = jax.random.normal(jax.random.PRNGKey(3), (B, T, D))

def loss_fn(x, weight, cos, sin):
    out = fused_qknorm_rope(x, weight, cos, sin)
    return jnp.sum(out)

grad_fn = jax.value_and_grad(loss_fn)
try:
    loss, grads = grad_fn(x, weight, cos, sin)
    print("Success")
except Exception as e:
    import traceback
    traceback.print_exc()

