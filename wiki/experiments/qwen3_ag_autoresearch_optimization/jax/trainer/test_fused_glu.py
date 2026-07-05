import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu

def fused_glu_fwd_kernel(x_ref, w_up_ref, w_gate_ref, o_ref, acc_up_ref, acc_gate_ref):
    @pl.when(pl.program_id(2) == 0)
    def _():
        acc_up_ref[...] = jnp.zeros_like(acc_up_ref)
        acc_gate_ref[...] = jnp.zeros_like(acc_gate_ref)
    
    acc_up_ref[...] += jnp.dot(x_ref[...], w_up_ref[...].T, preferred_element_type=acc_up_ref.dtype)
    acc_gate_ref[...] += jnp.dot(x_ref[...], w_gate_ref[...].T, preferred_element_type=acc_gate_ref.dtype)
    
    @pl.when(pl.program_id(2) == pl.num_programs(2) - 1)
    def _():
        o_ref[...] = (acc_up_ref[...] * jax.nn.silu(acc_gate_ref[...])).astype(o_ref.dtype)

def fused_glu_fwd(x, w_up, w_gate, block_b=1024, block_f=1024, block_d=1024):
    B, D = x.shape
    F, _ = w_up.shape
    
    grid = (B // block_b, F // block_f, D // block_d)
    
    return pl.pallas_call(
        fused_glu_fwd_kernel,
        out_shape=jax.ShapeDtypeStruct((B, F), x.dtype),
        grid=grid,
        in_specs=[
            pl.BlockSpec((block_b, block_d), lambda i, j, k: (i, k)),
            pl.BlockSpec((block_f, block_d), lambda i, j, k: (j, k)),
            pl.BlockSpec((block_f, block_d), lambda i, j, k: (j, k)),
        ],
        out_specs=pl.BlockSpec((block_b, block_f), lambda i, j, k: (i, j)),
        scratch_shapes=[
            pltpu.VMEM((block_b, block_f), jnp.float32),
            pltpu.VMEM((block_b, block_f), jnp.float32)
        ],
        compiler_params=pltpu.CompilerParams(dimension_semantics=('parallel', 'parallel', 'arbitrary'))
    )(x, w_up, w_gate)

x = jnp.ones((2048, 2048), dtype=jnp.bfloat16)
w_up = jnp.ones((2048, 2048), dtype=jnp.bfloat16)
w_gate = jnp.ones((2048, 2048), dtype=jnp.bfloat16)
out = jax.jit(fused_glu_fwd)(x, w_up, w_gate)
print("Forward out shape:", out.shape)
