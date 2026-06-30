import functools
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

def dx_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dx_ref, *, block_b, block_f, block_d, num_f):
    x = x_ref[...]
    
    def body_fn(f_idx, acc):
        g = g_ref[pl.dslice(0, block_b), pl.dslice(f_idx * block_f, block_f)]
        w_up = w_up_ref[pl.dslice(f_idx * block_f, block_f), pl.dslice(0, block_d)]
        w_gate = w_gate_ref[pl.dslice(f_idx * block_f, block_f), pl.dslice(0, block_d)]
        
        u = jnp.dot(x, w_up.T, preferred_element_type=jnp.float32)
        gate = jnp.dot(x, w_gate.T, preferred_element_type=jnp.float32)
        
        sig_gate = jax.nn.sigmoid(gate)
        silu_gate = gate * sig_gate
        silu_grad = sig_gate + gate * sig_gate * (1.0 - sig_gate)
        
        du = g * silu_gate
        dgate = g * u * silu_grad
        
        return acc + jnp.dot(du, w_up, preferred_element_type=jnp.float32) + jnp.dot(dgate, w_gate, preferred_element_type=jnp.float32)
        
    acc = jnp.zeros_like(x)
    final_acc = jax.lax.fori_loop(0, num_f, body_fn, acc)
    
    dx_ref[...] = final_acc.astype(dx_ref.dtype)

def dw_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dw_up_ref, dw_gate_ref, *, block_b, block_f, block_d, num_b):
    w_up = w_up_ref[...]
    w_gate = w_gate_ref[...]
    
    def body_fn(b_idx, accs):
        acc_up, acc_gate = accs
        
        x = x_ref[pl.dslice(b_idx * block_b, block_b), pl.dslice(0, block_d)]
        g = g_ref[pl.dslice(b_idx * block_b, block_b), pl.dslice(0, block_f)]
        
        u = jnp.dot(x, w_up.T, preferred_element_type=jnp.float32)
        gate = jnp.dot(x, w_gate.T, preferred_element_type=jnp.float32)
        
        sig_gate = jax.nn.sigmoid(gate)
        silu_gate = gate * sig_gate
        silu_grad = sig_gate + gate * sig_gate * (1.0 - sig_gate)
        
        du = g * silu_gate
        dgate = g * u * silu_grad
        
        step_up = jnp.dot(du.T, x, preferred_element_type=jnp.float32)
        step_gate = jnp.dot(dgate.T, x, preferred_element_type=jnp.float32)
        
        return (acc_up + step_up, acc_gate + step_gate)

    acc_up = jnp.zeros((block_f, block_d), dtype=jnp.float32)
    acc_gate = jnp.zeros((block_f, block_d), dtype=jnp.float32)
    
    final_up, final_gate = jax.lax.fori_loop(0, num_b, body_fn, (acc_up, acc_gate))
    
    dw_up_ref[...] = final_up.astype(dw_up_ref.dtype)
    dw_gate_ref[...] = final_gate.astype(dw_gate_ref.dtype)

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
        functools.partial(dx_kernel, block_b=block_b, block_f=block_f, block_d=block_d, num_f=num_f),
        out_shape=jax.ShapeDtypeStruct((B, D), x.dtype),
        grid=(num_b, num_d),
        in_specs=[
            pl.BlockSpec((block_b, block_d), lambda b, d: (b, d)),
            pl.BlockSpec((block_b, F), lambda b, d: (b, 0), memory_space=pltpu.HBM),
            pl.BlockSpec((F, block_d), lambda b, d: (0, d), memory_space=pltpu.HBM),
            pl.BlockSpec((F, block_d), lambda b, d: (0, d), memory_space=pltpu.HBM),
        ],
        out_specs=pl.BlockSpec((block_b, block_d), lambda b, d: (b, d)),
        compiler_params=pltpu.CompilerParams(dimension_semantics=('parallel', 'parallel'))
    )(x_flat, g_flat, w_up, w_gate)
    
    dw_up, dw_gate = pl.pallas_call(
        functools.partial(dw_kernel, block_b=block_b, block_f=block_f, block_d=block_d, num_b=num_b),
        out_shape=[
            jax.ShapeDtypeStruct((F, D), x.dtype),
            jax.ShapeDtypeStruct((F, D), x.dtype)
        ],
        grid=(num_f, num_d),
        in_specs=[
            pl.BlockSpec((B, block_d), lambda f, d: (0, d), memory_space=pltpu.HBM),
            pl.BlockSpec((B, block_f), lambda f, d: (0, f), memory_space=pltpu.HBM),
            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),
            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),
        ],
        out_specs=[
            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),
            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d))
        ],
        compiler_params=pltpu.CompilerParams(dimension_semantics=('parallel', 'parallel'))
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
