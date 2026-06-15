import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from .sharding import get_mesh
from jax.experimental.shard_map import shard_map
from jax.sharding import PartitionSpec as P

def _fused_qknorm_rope_pallas(x, weight, cos, sin, eps=1e-6):
    B, H, T, D = x.shape
    block_size = min(256, T)
    if T % block_size != 0:
        raise ValueError(f"T ({T}) must be divisible by block_size ({block_size})")

    eps_arr = jnp.array([eps], dtype=jnp.float32)

    def _fused_qknorm_rope_kernel(x_ref, w_ref, cos_ref, sin_ref, eps_ref, out_ref):
        x_val = x_ref[0, 0, :, :]
        w = w_ref[:]
        c = cos_ref[0, :, :]
        s = sin_ref[0, :, :]
        eps_val = eps_ref[0]
        
        # QK-norm
        x32 = x_val.astype(jnp.float32)
        # Avoid jnp.mean which might capture a constant for the denominator inside JIT
        var = jnp.sum(x32 * x32, axis=-1, keepdims=True)
        # Explicit division by float(D) using JAX primitives avoiding implicit constant capture if possible
        # Actually, let's just do var = var * (1.0 / D)
        inv_d = jnp.array(1.0 / D, dtype=jnp.float32)
        var = var * inv_d
        
        rsqrt = jax.lax.rsqrt(var + eps_val)
        x_norm = (x32 * rsqrt).astype(x_val.dtype)
        x_norm = x_norm * w
        
        # RoPE
        d = x_val.shape[-1]
        half_d = d // 2
        x_rot = jnp.concatenate([-x_norm[:, half_d:], x_norm[:, :half_d]], axis=-1)
        
        out_val = (x_norm * c) + (x_rot * s)
        out_ref[0, 0, :, :] = out_val.astype(out_ref.dtype)

    mesh = get_mesh(tp=1)
    
    def _sharded_pallas_call(x_local, w_local, cos_local, sin_local, eps_local):
        B_local = x_local.shape[0]
        return pl.pallas_call(
            _fused_qknorm_rope_kernel,
            out_shape=jax.ShapeDtypeStruct(x_local.shape, x_local.dtype),
            grid=(B_local, H, T // block_size),
            in_specs=[
                pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
                pl.BlockSpec((D,), lambda b, h, t: (0,)),
                pl.BlockSpec((1, block_size, D), lambda b, h, t: (b, t, 0)),
                pl.BlockSpec((1, block_size, D), lambda b, h, t: (b, t, 0)),
                pl.BlockSpec((1,), lambda b, h, t: (0,)),
            ],
            out_specs=pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
        )(x_local, w_local, cos_local, sin_local, eps_local)

    sharded_fn = shard_map(
        _sharded_pallas_call,
        mesh=mesh,
        in_specs=(P('fsdp', None, None, None), P(), P('fsdp', None, None), P('fsdp', None, None), P()),
        out_specs=P('fsdp', None, None, None),
        check_rep=False
    )
    return sharded_fn(x, weight, cos, sin, eps_arr)

@jax.custom_vjp
def fused_qknorm_rope(x, weight, cos, sin, eps=1e-6):
    """
    Applies RMSNorm followed by RoPE.
    This primal function uses standard ops so `jax.checkpoint` can linearize it without crashing.
    """
    x32 = x.astype(jnp.float32)
    var = jnp.mean(x32 * x32, axis=-1, keepdims=True)
    rsqrt = jax.lax.rsqrt(var + eps)
    x_norm = (x32 * rsqrt).astype(x.dtype)
    x_norm = x_norm * weight
    d = x.shape[-1]
    half_d = d // 2
    x_rot = jnp.concatenate([-x_norm[..., half_d:], x_norm[..., :half_d]], axis=-1)
    cos_bcast = jnp.expand_dims(cos, axis=1)
    sin_bcast = jnp.expand_dims(sin, axis=1)
    return (x_norm * cos_bcast) + (x_rot * sin_bcast)

def fused_qknorm_rope_fwd(x, weight, cos, sin, eps=1e-6):
    # At execution time, run the optimized Pallas kernel to save HBM
    out = _fused_qknorm_rope_pallas(x, weight, cos, sin, eps=eps)
    return out, (x, weight, cos, sin, eps)

def fused_qknorm_rope_bwd(res, g):
    x, weight, cos, sin, eps = res
    print(f"BWD x: {x.shape}, weight: {weight.shape}, cos: {cos.shape}, sin: {sin.shape}, g: {g.shape}")
    
    # Reconstruct standard ops for VJP
    def ref_impl(x_, weight_, cos_, sin_):
        x32_ = x_.astype(jnp.float32)
        var_ = jnp.mean(x32_ * x32_, axis=-1, keepdims=True)
        rsqrt_ = jax.lax.rsqrt(var_ + eps)
        x_norm_ = (x32_ * rsqrt_).astype(x_.dtype)
        x_norm_ = x_norm_ * weight_
        
        d = x_.shape[-1]
        half_d = d // 2
        x_rot_ = jnp.concatenate([-x_norm_[..., half_d:], x_norm_[..., :half_d]], axis=-1)
        cos_bcast_ = jnp.expand_dims(cos_, axis=1)
        sin_bcast_ = jnp.expand_dims(sin_, axis=1)
        return (x_norm_ * cos_bcast_) + (x_rot_ * sin_bcast_)
        
    try:
        _, vjp_fn = jax.vjp(ref_impl, x, weight, cos, sin)
        dx, dweight, dcos, dsin = vjp_fn(g)
    except Exception as e:
        print(f"Exception during vjp tracing: {e}")
        raise e
    
    return dx, dweight, dcos, dsin, None

fused_qknorm_rope.defvjp(fused_qknorm_rope_fwd, fused_qknorm_rope_bwd)
