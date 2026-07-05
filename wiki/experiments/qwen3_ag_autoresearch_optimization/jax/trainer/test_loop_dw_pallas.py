import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl

def dw_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dw_up_ref, dw_gate_ref, *, block_b, block_f, num_b, D):
    w_up = w_up_ref[...]
    w_gate = w_gate_ref[...]
    
    acc_dw_up = jnp.zeros_like(w_up, dtype=jnp.float32)
    acc_dw_gate = jnp.zeros_like(w_gate, dtype=jnp.float32)
    
    def body(i, accs):
        acc_dw_up, acc_dw_gate = accs
        
        x = x_ref[pl.dslice(i * block_b, block_b), :]
        g = g_ref[pl.dslice(i * block_b, block_b), :]
        
        u = jnp.dot(x, w_up.T, preferred_element_type=jnp.float32)
        gate = jnp.dot(x, w_gate.T, preferred_element_type=jnp.float32)
        
        sig_gate = jax.nn.sigmoid(gate)
        silu_gate = gate * sig_gate
        silu_grad = sig_gate + gate * sig_gate * (1.0 - sig_gate)
        
        du = g * silu_gate
        dgate = g * u * silu_grad
        
        acc_dw_up += jnp.dot(du.T, x, preferred_element_type=jnp.float32)
        acc_dw_gate += jnp.dot(dgate.T, x, preferred_element_type=jnp.float32)
        
        return acc_dw_up, acc_dw_gate

    acc_dw_up, acc_dw_gate = jax.lax.fori_loop(0, num_b, body, (acc_dw_up, acc_dw_gate))
    
    dw_up_ref[...] = acc_dw_up.astype(dw_up_ref.dtype)
    dw_gate_ref[...] = acc_dw_gate.astype(dw_gate_ref.dtype)

def test_dw():
    B = 1024
    F = 2048
    D = 512
    block_b = 512
    block_f = 512
    
    x = jax.random.normal(jax.random.PRNGKey(0), (B, D), dtype=jnp.bfloat16)
    g = jax.random.normal(jax.random.PRNGKey(1), (B, F), dtype=jnp.bfloat16)
    w_up = jax.random.normal(jax.random.PRNGKey(2), (F, D), dtype=jnp.bfloat16)
    w_gate = jax.random.normal(jax.random.PRNGKey(3), (F, D), dtype=jnp.bfloat16)
    
    grid = (F // block_f,)
    
    out_up, out_gate = pl.pallas_call(
        lambda *args: dw_kernel(*args, block_b=block_b, block_f=block_f, num_b=B//block_b, D=D),
        out_shape=[
            jax.ShapeDtypeStruct((F, D), jnp.bfloat16),
            jax.ShapeDtypeStruct((F, D), jnp.bfloat16)
        ],
        grid=grid,
        in_specs=[
            pl.BlockSpec((B, D), lambda f: (0, 0)),
            pl.BlockSpec((B, block_f), lambda f: (0, f)),
            pl.BlockSpec((block_f, D), lambda f: (f, 0)),
            pl.BlockSpec((block_f, D), lambda f: (f, 0)),
        ],
        out_specs=[
            pl.BlockSpec((block_f, D), lambda f: (f, 0)),
            pl.BlockSpec((block_f, D), lambda f: (f, 0))
        ]
    )(x, g, w_up, w_gate)
    
    print("Shape up:", out_up.shape, "Shape gate:", out_gate.shape)
    print("Mean up:", jnp.mean(out_up))

test_dw()
