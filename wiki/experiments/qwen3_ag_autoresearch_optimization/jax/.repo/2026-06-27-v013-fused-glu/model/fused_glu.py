import functools
import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu

def glu_kernel(x_tile_ref, w_up_tile_ref, w_gate_tile_ref, o_tile_ref, acc_up_ref, acc_gate_ref):
    @pl.when(pl.program_id(2) == 0)
    def init():
        acc_up_ref[...] = jnp.zeros_like(acc_up_ref)
        acc_gate_ref[...] = jnp.zeros_like(acc_gate_ref)

    # w_up_tile is [N_block, K_block]. We transpose it to [K_block, N_block]
    w_up = w_up_tile_ref[...].T
    w_gate = w_gate_tile_ref[...].T

    acc_up_ref[...] = acc_up_ref[...] + jnp.dot(
        x_tile_ref[...],
        w_up,
        preferred_element_type=acc_up_ref.dtype,
    )
    acc_gate_ref[...] = acc_gate_ref[...] + jnp.dot(
        x_tile_ref[...],
        w_gate,
        preferred_element_type=acc_gate_ref.dtype,
    )

    @pl.when(pl.program_id(2) == pl.num_programs(2) - 1)
    def finalize():
        o_tile_ref[...] = (acc_up_ref[...] * jax.nn.silu(acc_gate_ref[...])).astype(o_tile_ref.dtype)


from jax.experimental.shard_map import shard_map
from jax.sharding import PartitionSpec as P

@functools.partial(jax.custom_vjp, nondiff_argnums=(3, 4, 5, 6, 7, 8))
def fused_glu(
    x: jax.Array,
    w_up: jax.Array,
    w_gate: jax.Array,
    mesh = None,
    x_sharding = P("fsdp", None, None),
    block_shape=(1024, 1024),
    block_k: int = 256,
    out_dtype: jnp.dtype | None = None,
    debug: bool = False,
) -> jax.Array:
    if out_dtype is None:
        out_dtype = x.dtype
    acc_dtype = jnp.float32

    is_3d = False
    orig_shape = None
    if x.ndim == 3:
        is_3d = True
        orig_shape = x.shape
        x = x.reshape(-1, x.shape[-1])
        # x is now 2D: [B*S, K]. But if it's sharded on B, reshaping it to 2D
        # means it's sharded on the first dimension. So x_sharding is just P("fsdp", None).
        x_sharding = P(x_sharding[0], None)
        
    m, k = x.shape
    n, _ = w_up.shape
    l, r = block_shape

    def run_pallas(x_loc, w_up_loc, w_gate_loc):
        loc_m, loc_k = x_loc.shape
        loc_n, _ = w_up_loc.shape
        return pl.pallas_call(
            glu_kernel,
            out_shape=jax.ShapeDtypeStruct((loc_m, loc_n), out_dtype),
            grid_spec=pltpu.PrefetchScalarGridSpec(
                num_scalar_prefetch=0,
                in_specs=[
                    pl.BlockSpec((l, block_k), lambda i, _, k: (i, k)),
                    pl.BlockSpec((r, block_k), lambda _, j, k: (j, k)),
                    pl.BlockSpec((r, block_k), lambda _, j, k: (j, k)),
                ],
                out_specs=pl.BlockSpec((l, r), lambda i, j, k: (i, j)),
                grid=(loc_m // l, loc_n // r, loc_k // block_k),
                scratch_shapes=[pltpu.VMEM((l, r), acc_dtype), pltpu.VMEM((l, r), acc_dtype)],
            ),
            compiler_params=pltpu.CompilerParams(
                dimension_semantics=("parallel", "parallel", "arbitrary")),
            debug=debug,
        )(x_loc, w_up_loc, w_gate_loc)

    if mesh is not None:
        out = shard_map(
            run_pallas,
            mesh=mesh,
            in_specs=(x_sharding, P(None, None), P(None, None)),
            out_specs=x_sharding,
            check_rep=False
        )(x, w_up, w_gate)
    else:
        out = run_pallas(x, w_up, w_gate)

    if is_3d:
        out = out.reshape(orig_shape[0], orig_shape[1], n)
    return out


def fused_glu_fwd(x, w_up, w_gate, mesh, x_sharding, block_shape, block_k, out_dtype, debug):
    out = fused_glu(x, w_up, w_gate, mesh, x_sharding, block_shape, block_k, out_dtype, debug)
    # Save inputs for the backward pass
    return out, (x, w_up, w_gate)


def fused_glu_bwd(mesh, x_sharding, block_shape, block_k, out_dtype, debug, res, g):
    x, w_up, w_gate = res
    
    # Compute the standard JAX forward ops to get gradients
    # We use standard JAX here because XLA handles standard backward ops reasonably well,
    # and writing a Pallas backward kernel for GLU is complex.
    
    # Recompute U and G
    # x is [..., K], w_up is [N, K], w_gate is [N, K]
    u = jnp.dot(x, w_up.T)
    gate = jnp.dot(x, w_gate.T)
    
    # O = u * silu(gate)
    # dO = g
    
    # silu(x) = x * sigmoid(x)
    # silu'(x) = sigmoid(x) + x * sigmoid(x) * (1 - sigmoid(x))
    sig_gate = jax.nn.sigmoid(gate)
    silu_gate = gate * sig_gate
    silu_grad = sig_gate * (1.0 + gate * (1.0 - sig_gate))
    
    # dU = g * silu(gate)
    du = g * silu_gate
    
    # dG = g * u * silu'(gate)
    dgate = g * u * silu_grad
    
    # Gradients w.r.t inputs
    # dx = du @ w_up.T + dgate @ w_gate.T, but w_up is [N, K], so w_up.T in math is w_up
    dx = jnp.dot(du, w_up) + jnp.dot(dgate, w_gate)
    
    # dw_up = x.T @ du
    # If x is 3D [B, S, K], du is [B, S, N]
    if x.ndim == 3:
        # dw_up needs to be [N, K]. tensordot(du, x) over batch,seq -> [N, K]
        dw_up = jnp.tensordot(du, x, axes=([0, 1], [0, 1]))
        dw_gate = jnp.tensordot(dgate, x, axes=([0, 1], [0, 1]))
    else:
        # du is [M, N], x is [M, K]
        dw_up = jnp.dot(du.T, x)
        dw_gate = jnp.dot(dgate.T, x)
        
    return dx, dw_up, dw_gate

fused_glu.defvjp(fused_glu_fwd, fused_glu_bwd)
