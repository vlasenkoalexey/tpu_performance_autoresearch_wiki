import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax import custom_vjp
from jax.sharding import PartitionSpec as P

@jax.custom_vjp
def fused_qknorm_rope(x, weight, cos, sin, eps=1e-6):
    def _fused_qknorm_rope_kernel(x_ref, w_ref, cos_ref, sin_ref, eps_ref, out_ref):
        pass

    B, H, T, D = x.shape
    block_size = min(256, T)
    eps_arr = jnp.array([eps], dtype=jnp.float32)
    out = pl.pallas_call(
        _fused_qknorm_rope_kernel,
        out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype),
        grid=(B, H, T // block_size),
        in_specs=[
            pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
            pl.BlockSpec((D,), lambda b, h, t: (0,)),
            pl.BlockSpec((1, block_size, D), lambda b, h, t: (b, t, 0)),
            pl.BlockSpec((1, block_size, D), lambda b, h, t: (b, t, 0)),
            pl.BlockSpec((1,), lambda b, h, t: (0,)),
        ],
        out_specs=pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
    )(x, weight, cos, sin, eps_arr)
    return out

def fwd(x, weight, cos, sin, eps=1e-6):
    return fused_qknorm_rope(x, weight, cos, sin, eps=eps), (x, weight, cos, sin, eps)

def bwd(res, g):
    x, weight, cos, sin, eps = res
    
    # QK-norm standard
    x32 = x.astype(jnp.float32)
    var = jnp.mean(x32 * x32, axis=-1, keepdims=True)
    rsqrt = jax.lax.rsqrt(var + eps)
    x_norm = (x32 * rsqrt).astype(x.dtype)
    x_norm = x_norm * weight
    
    # RoPE standard
    d = x.shape[-1]
    half_d = d // 2
    x_rot = jnp.concatenate([-x_norm[..., half_d:], x_norm[..., :half_d]], axis=-1)
    cos_bcast = jnp.expand_dims(cos, axis=1)
    sin_bcast = jnp.expand_dims(sin, axis=1)
    out_ref = (x_norm * cos_bcast) + (x_rot * sin_bcast)
    
    # Use jax.vjp on the standard op implementation!
    def ref_impl(x_, weight_, cos_, sin_):
        x32_ = x_.astype(jnp.float32)
        var_ = jnp.mean(x32_ * x32_, axis=-1, keepdims=True)
        rsqrt_ = jax.lax.rsqrt(var_ + eps)
        x_norm_ = (x32_ * rsqrt_).astype(x_.dtype)
        x_norm_ = x_norm_ * weight_
        
        x_rot_ = jnp.concatenate([-x_norm_[..., half_d:], x_norm_[..., :half_d]], axis=-1)
        # cos_ and sin_ are [B, T, D]
        # x_norm_ is [B, H, T, D]
        cos_bcast_ = jnp.expand_dims(cos_, axis=1) # [B, 1, T, D]
        sin_bcast_ = jnp.expand_dims(sin_, axis=1) # [B, 1, T, D]
        return (x_norm_ * cos_bcast_) + (x_rot_ * sin_bcast_)
        
    _, vjp_fn = jax.vjp(ref_impl, x, weight, cos, sin)
    dx, dweight, dcos, dsin = vjp_fn(g)
    
    # Return None for the eps gradient
    return dx, dweight, dcos, dsin, None

fused_qknorm_rope.defvjp(fwd, bwd)

x = jnp.ones((8, 256, 128))
q_proj = jnp.ones((128, 2*128))
q_norm = jnp.ones((128,))
cos = jnp.ones((8, 256, 128))
sin = jnp.ones((8, 256, 128))

def loss_fn(x, q_proj, q_norm, cos, sin):
    q = jnp.dot(x, q_proj)
    B, T, _ = q.shape
    q = q.reshape(B, T, 2, 128)
    q = jnp.transpose(q, (0, 2, 1, 3))
    out = fused_qknorm_rope(q, q_norm, cos, sin)
    return jnp.sum(out)

from jax.experimental import mesh_utils
from jax.sharding import Mesh, NamedSharding

mesh = Mesh(mesh_utils.create_device_mesh((8,)), axis_names=('fsdp',))
sharding_x = NamedSharding(mesh, P('fsdp', None, None))
sharding_q_proj = NamedSharding(mesh, P(None, 'fsdp'))
sharding_q_norm = NamedSharding(mesh, P())
sharding_cos = NamedSharding(mesh, P(None, None, None)) # replicated? Actually cos is (B, T, D) but how is it sharded?
# wait, cos is generated from position_ids. position_ids is P('fsdp', None). So cos is P('fsdp', None, None)
sharding_cos = NamedSharding(mesh, P('fsdp', None, None)) 
sharding_sin = NamedSharding(mesh, P('fsdp', None, None)) 

@jax.jit
def train_step(x, q_proj, q_norm, cos, sin):
    return jax.grad(loss_fn, argnums=(0, 1, 2, 3, 4))(x, q_proj, q_norm, cos, sin)

with mesh:
    x_sharded = jax.device_put(x, sharding_x)
    q_proj_sharded = jax.device_put(q_proj, sharding_q_proj)
    q_norm_sharded = jax.device_put(q_norm, sharding_q_norm)
    cos_sharded = jax.device_put(cos, sharding_cos)
    sin_sharded = jax.device_put(sin, sharding_sin)
    print('Testing regular jit lowering:')
    train_step.lower(x_sharded, q_proj_sharded, q_norm_sharded, cos_sharded, sin_sharded)
    print('success')
