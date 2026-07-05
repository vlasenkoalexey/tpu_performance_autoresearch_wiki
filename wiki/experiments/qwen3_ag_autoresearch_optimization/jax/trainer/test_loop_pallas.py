import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl

def dx_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dx_ref, *, block_b, block_f, num_f, D):
    x = x_ref[...]
    acc_dx = jnp.zeros_like(x, dtype=jnp.float32)
    
    def body(i, acc_dx):
        w_up = w_up_ref[pl.dslice(i * block_f, block_f), :]
        w_gate = w_gate_ref[pl.dslice(i * block_f, block_f), :]
        g = g_ref[:, pl.dslice(i * block_f, block_f)]
        
        u = jnp.dot(x, w_up.T, preferred_element_type=jnp.float32)
        gate = jnp.dot(x, w_gate.T, preferred_element_type=jnp.float32)
        
        sig_gate = jax.nn.sigmoid(gate)
        silu_gate = gate * sig_gate
        silu_grad = sig_gate + gate * sig_gate * (1.0 - sig_gate)
        
        du = g * silu_gate
        dgate = g * u * silu_grad
        
        acc_dx += jnp.dot(du, w_up, preferred_element_type=jnp.float32) + jnp.dot(dgate, w_gate, preferred_element_type=jnp.float32)
        return acc_dx

    acc_dx = jax.lax.fori_loop(0, num_f, body, acc_dx)
    dx_ref[...] = acc_dx.astype(dx_ref.dtype)

def test_dx():
    B = 1024
    F = 2048
    D = 512
    block_b = 512
    block_f = 512
    
    x = jax.random.normal(jax.random.PRNGKey(0), (B, D), dtype=jnp.bfloat16)
    g = jax.random.normal(jax.random.PRNGKey(1), (B, F), dtype=jnp.bfloat16)
    w_up = jax.random.normal(jax.random.PRNGKey(2), (F, D), dtype=jnp.bfloat16)
    w_gate = jax.random.normal(jax.random.PRNGKey(3), (F, D), dtype=jnp.bfloat16)
    
    grid = (B // block_b,)
    
    out = pl.pallas_call(
        lambda *args: dx_kernel(*args, block_b=block_b, block_f=block_f, num_f=F//block_f, D=D),
        out_shape=jax.ShapeDtypeStruct((B, D), jnp.bfloat16),
        grid=grid,
        in_specs=[
            pl.BlockSpec((block_b, D), lambda b: (b, 0)),
            pl.BlockSpec((block_b, F), lambda b: (b, 0)),
            pl.BlockSpec((F, D), lambda b: (0, 0)),
            pl.BlockSpec((F, D), lambda b: (0, 0)),
        ],
        out_specs=pl.BlockSpec((block_b, D), lambda b: (b, 0))
    )(x, g, w_up, w_gate)
    
    print("Shape:", out.shape)
    print("Mean:", jnp.mean(out))

test_dx()
