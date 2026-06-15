import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.shard_map import shard_map
from jax.sharding import PartitionSpec as P

def _fused_qknorm_rope_kernel(x_ref, w_ref, cos_ref, sin_ref, eps_ref, out_ref):
    x_val = x_ref[0, 0, :, :]
    w = w_ref[:]
    c = cos_ref[0, :, :]
    s = sin_ref[0, :, :]
    eps_val = eps_ref[0]

    # QK-norm
    x32 = x_val.astype(jnp.float32)
    var = jnp.sum(x32 * x32, axis=-1, keepdims=True)
    inv_d = jnp.array(1.0 / x_val.shape[-1], dtype=jnp.float32)
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


@jax.custom_vjp
def fused_qknorm_rope(x, weight, cos, sin, eps=1e-6):
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
    # This is the forward pass. We apply shard_map HERE, explicitly for the pallas call!
    def sharded_pallas(x_s, weight_s, cos_s, sin_s, eps_s):
        B, H, T, D = x_s.shape
        block_size = min(256, T)
        if T % block_size != 0:
            raise ValueError(f"T ({T}) must be divisible by block_size ({block_size})")

        eps_arr = jnp.array([eps_s], dtype=jnp.float32)
        
        return pl.pallas_call(
            _fused_qknorm_rope_kernel,
            out_shape=jax.ShapeDtypeStruct(x_s.shape, x_s.dtype),
            grid=(B, H, T // block_size),
            in_specs=[
                pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
                pl.BlockSpec((D,), lambda b, h, t: (0,)),
                pl.BlockSpec((1, block_size, D), lambda b, h, t: (b, t, 0)),
                pl.BlockSpec((1, block_size, D), lambda b, h, t: (b, t, 0)),
                pl.BlockSpec((1,), lambda b, h, t: (0,)),
            ],
            out_specs=pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
        )(x_s, weight_s, cos_s, sin_s, eps_s)
        
    fsdp = jax.device_count() // 1
    mesh = jax.make_mesh((fsdp, 1), ("fsdp", "tp"))

    out = shard_map(
        sharded_pallas,
        mesh=mesh,
        in_specs=(P('fsdp', None, None, 'tp'), P('tp',), P('fsdp', None, 'tp'), P('fsdp', None, 'tp'), P()),
        out_specs=P('fsdp', None, None, 'tp'),
        check_rep=False
    )(x, weight, cos, sin, eps)
    
    return out, (x, weight, cos, sin, eps)

def fused_qknorm_rope_bwd(res, g):
    x, weight, cos, sin, eps = res

    def ref_impl(x_, weight_, cos_, sin_, eps_):
        x32_ = x_.astype(jnp.float32)
        var_ = jnp.mean(x32_ * x32_, axis=-1, keepdims=True)
        rsqrt_ = jax.lax.rsqrt(var_ + eps_)
        x_norm_ = (x32_ * rsqrt_).astype(x_.dtype)
        x_norm_ = x_norm_ * weight_
        
        d = x_.shape[-1]
        half_d = d // 2
        x_rot_ = jnp.concatenate([-x_norm_[..., half_d:], x_norm_[..., :half_d]], axis=-1)
        cos_bcast_ = jnp.expand_dims(cos_, axis=1)
        sin_bcast_ = jnp.expand_dims(sin_, axis=1)
        return (x_norm_ * cos_bcast_) + (x_rot_ * sin_bcast_)
        
    _, vjp_fn = jax.vjp(ref_impl, x, weight, cos, sin, eps)
    dx, dweight, dcos, dsin, deps = vjp_fn(g)

    return dx, dweight, dcos, dsin, deps

fused_qknorm_rope.defvjp(fused_qknorm_rope_fwd, fused_qknorm_rope_bwd)

