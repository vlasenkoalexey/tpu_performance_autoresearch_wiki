import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu

def glu_fwd_kernel(x_ref, w_up_ref, w_gate_ref, o_ref, acc_up_ref, acc_gate_ref):
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
    if x.ndim == 3:
        B1, B2, D = x.shape
        x_flat = x.reshape(B1 * B2, D)
    else:
        x_flat = x
        D = x.shape[-1]
    
    B = x_flat.shape[0]
    F = w_up.shape[0]
    
    grid = (B // block_b, F // block_f, D // block_d)
    
    out = pl.pallas_call(
        glu_fwd_kernel,
        out_shape=jax.ShapeDtypeStruct((B, F), x_flat.dtype),
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
    )(x_flat, w_up, w_gate)
    
    if x.ndim == 3:
        return out.reshape(B1, B2, F)
    return out

def dx_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dx_ref, acc_dx_ref):
    @pl.when(pl.program_id(2) == 0)
    def _():
        acc_dx_ref[...] = jnp.zeros_like(acc_dx_ref)
        
    x = x_ref[...]
    w_up = w_up_ref[...]
    w_gate = w_gate_ref[...]
    g = g_ref[...]
    
    u = jnp.dot(x, w_up.T, preferred_element_type=jnp.float32)
    gate = jnp.dot(x, w_gate.T, preferred_element_type=jnp.float32)
    
    sig_gate = jax.nn.sigmoid(gate)
    silu_gate = gate * sig_gate
    silu_grad = sig_gate + gate * sig_gate * (1.0 - sig_gate)
    
    du = g * silu_gate
    dgate = g * u * silu_grad
    
    acc_dx_ref[...] += jnp.dot(du, w_up, preferred_element_type=jnp.float32) + jnp.dot(dgate, w_gate, preferred_element_type=jnp.float32)
    
    @pl.when(pl.program_id(2) == pl.num_programs(2) - 1)
    def _():
        dx_ref[...] = acc_dx_ref[...].astype(dx_ref.dtype)

def dw_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dw_up_ref, dw_gate_ref, acc_dw_up_ref, acc_dw_gate_ref):
    @pl.when(pl.program_id(2) == 0)
    def _():
        acc_dw_up_ref[...] = jnp.zeros_like(acc_dw_up_ref)
        acc_dw_gate_ref[...] = jnp.zeros_like(acc_dw_gate_ref)
        
    x = x_ref[...]
    w_up = w_up_ref[...]
    w_gate = w_gate_ref[...]
    g = g_ref[...]
    
    u = jnp.dot(x, w_up.T, preferred_element_type=jnp.float32)
    gate = jnp.dot(x, w_gate.T, preferred_element_type=jnp.float32)
    
    sig_gate = jax.nn.sigmoid(gate)
    silu_gate = gate * sig_gate
    silu_grad = sig_gate + gate * sig_gate * (1.0 - sig_gate)
    
    du = g * silu_gate
    dgate = g * u * silu_grad
    
    acc_dw_up_ref[...] += jnp.dot(du.T, x, preferred_element_type=jnp.float32)
    acc_dw_gate_ref[...] += jnp.dot(dgate.T, x, preferred_element_type=jnp.float32)
    
    @pl.when(pl.program_id(2) == pl.num_programs(2) - 1)
    def _():
        dw_up_ref[...] = acc_dw_up_ref[...].astype(dw_up_ref.dtype)
        dw_gate_ref[...] = acc_dw_gate_ref[...].astype(dw_gate_ref.dtype)

def fused_glu_bwd(g, x, w_up, w_gate, block_b=512, block_f=512, block_d=512):
    if x.ndim == 3:
        B1, B2, D = x.shape
        x_flat = x.reshape(B1 * B2, D)
        g_flat = g.reshape(B1 * B2, g.shape[-1])
    else:
        x_flat = x
        g_flat = g
        D = x.shape[-1]
        
    B = x_flat.shape[0]
    F = w_up.shape[0]
    
    num_b = B // block_b
    num_f = F // block_f
    num_d = D // block_d
    
    dx_flat = pl.pallas_call(
        dx_kernel,
        out_shape=jax.ShapeDtypeStruct((B, D), x.dtype),
        grid=(num_b, num_d, num_f),
        in_specs=[
            pl.BlockSpec((block_b, block_d), lambda b, d, f: (b, d)),
            pl.BlockSpec((block_b, block_f), lambda b, d, f: (b, f)),
            pl.BlockSpec((block_f, block_d), lambda b, d, f: (f, d)),
            pl.BlockSpec((block_f, block_d), lambda b, d, f: (f, d)),
        ],
        out_specs=pl.BlockSpec((block_b, block_d), lambda b, d, f: (b, d)),
        scratch_shapes=[pltpu.VMEM((block_b, block_d), jnp.float32)],
        compiler_params=pltpu.CompilerParams(dimension_semantics=('parallel', 'parallel', 'arbitrary'))
    )(x_flat, g_flat, w_up, w_gate)
    
    dw_up, dw_gate = pl.pallas_call(
        dw_kernel,
        out_shape=[
            jax.ShapeDtypeStruct((F, D), x.dtype),
            jax.ShapeDtypeStruct((F, D), x.dtype)
        ],
        grid=(num_f, num_d, num_b),
        in_specs=[
            pl.BlockSpec((block_b, block_d), lambda f, d, b: (b, d)),
            pl.BlockSpec((block_b, block_f), lambda f, d, b: (b, f)),
            pl.BlockSpec((block_f, block_d), lambda f, d, b: (f, d)),
            pl.BlockSpec((block_f, block_d), lambda f, d, b: (f, d)),
        ],
        out_specs=[
            pl.BlockSpec((block_f, block_d), lambda f, d, b: (f, d)),
            pl.BlockSpec((block_f, block_d), lambda f, d, b: (f, d))
        ],
        scratch_shapes=[
            pltpu.VMEM((block_f, block_d), jnp.float32),
            pltpu.VMEM((block_f, block_d), jnp.float32)
        ],
        compiler_params=pltpu.CompilerParams(dimension_semantics=('parallel', 'parallel', 'arbitrary'))
    )(x_flat, g_flat, w_up, w_gate)
    
    if x.ndim == 3:
        dx = dx_flat.reshape(B1, B2, D)
    else:
        dx = dx_flat
        
    return dx, dw_up, dw_gate

@jax.custom_vjp
def fused_glu(x, w_up, w_gate):
    return fused_glu_fwd(x, w_up, w_gate)

def fused_glu_fwd_rule(x, w_up, w_gate):
    out = fused_glu_fwd(x, w_up, w_gate)
    return out, (x, w_up, w_gate)

def fused_glu_bwd_rule(res, g):
    x, w_up, w_gate = res
    dx, dw_up, dw_gate = fused_glu_bwd(g, x, w_up, w_gate)
    return dx, dw_up, dw_gate

fused_glu.defvjp(fused_glu_fwd_rule, fused_glu_bwd_rule)
