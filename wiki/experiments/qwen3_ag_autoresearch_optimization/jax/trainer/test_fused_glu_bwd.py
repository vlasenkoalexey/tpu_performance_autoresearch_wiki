import jax
import jax.numpy as jnp
from model.fused_glu import fused_glu_bwd

def jax_native_glu_bwd(g, x, w_up, w_gate):
    def glu_fwd(x, w_up, w_gate):
        return jax.nn.silu(x @ w_gate.T) * (x @ w_up.T)
    
    _, vjp_fn = jax.vjp(glu_fwd, x, w_up, w_gate)
    return vjp_fn(g)

B, D = 1024, 512
F = 2048

x = jax.random.uniform(jax.random.PRNGKey(0), (B, D), minval=-0.1, maxval=0.1, dtype=jnp.float32)
g = jax.random.uniform(jax.random.PRNGKey(1), (B, F), minval=-0.1, maxval=0.1, dtype=jnp.float32)
w_up = jax.random.uniform(jax.random.PRNGKey(2), (F, D), minval=-0.1, maxval=0.1, dtype=jnp.float32)
w_gate = jax.random.uniform(jax.random.PRNGKey(3), (F, D), minval=-0.1, maxval=0.1, dtype=jnp.float32)

# Test native
dx_ref, dw_up_ref, dw_gate_ref = jax_native_glu_bwd(g, x, w_up, w_gate)

# Test Pallas
dx, dw_up, dw_gate = jax.jit(lambda g, x, w_up, w_gate: fused_glu_bwd(g, x, w_up, w_gate, block_b=512, block_f=512))(g, x, w_up, w_gate)

print("dx max diff:", jnp.max(jnp.abs(dx - dx_ref)))
print("dw_up max diff:", jnp.max(jnp.abs(dw_up - dw_up_ref)))
print("dw_gate max diff:", jnp.max(jnp.abs(dw_gate - dw_gate_ref)))
