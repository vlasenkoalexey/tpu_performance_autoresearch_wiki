import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

replacement_dx_kernel = """def dx_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dx_ref, *, block_b, block_f, block_d, num_f):
    def body_fn(f_idx, acc):
        x = x_ref[...]
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
        
    acc = jnp.zeros((block_b, block_d), dtype=jnp.float32)
    final_acc = jax.lax.fori_loop(0, num_f, body_fn, acc)
    
    dx_ref[...] = final_acc.astype(dx_ref.dtype)"""

# In v019-v12, I had modified it to:
#    x = x_ref[...]
#    def body_fn(f_idx, acc):
#        ...
# Let's replace the entire `def dx_kernel(...)` up to `dx_ref[...] = ...`

text = re.sub(
    r"def dx_kernel\(x_ref, g_ref, w_up_ref, w_gate_ref, dx_ref, \*, block_b, block_f, block_d, num_f\):.*?dx_ref\[\.\.\.\] = final_acc\.astype\(dx_ref\.dtype\)",
    replacement_dx_kernel,
    text,
    flags=re.DOTALL
)

replacement_dw_kernel = """def dw_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dw_up_ref, dw_gate_ref, *, block_b, block_f, block_d, num_b):
    def body_fn(b_idx, accs):
        w_up = w_up_ref[...]
        w_gate = w_gate_ref[...]
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
    dw_gate_ref[...] = final_gate.astype(dw_gate_ref.dtype)"""

text = re.sub(
    r"def dw_kernel\(x_ref, g_ref, w_up_ref, w_gate_ref, dw_up_ref, dw_gate_ref, \*, block_b, block_f, block_d, num_b\):.*?dw_gate_ref\[\.\.\.\] = final_gate\.astype\(dw_gate_ref\.dtype\)",
    replacement_dw_kernel,
    text,
    flags=re.DOTALL
)

# Fix in_specs for dx_kernel
text = text.replace(
    "        in_specs=[\n            pl.BlockSpec((block_b, block_d), lambda b, d: (b, d)),\n            pl.BlockSpec((B, F), lambda b, d: (0, 0)),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0)),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0)),\n        ],",
    "        in_specs=[\n            pl.BlockSpec((block_b, block_d), lambda b, d: (b, d)),\n            pl.BlockSpec((block_b, F), lambda b, d: (b, 0)),\n            pl.BlockSpec((F, block_d), lambda b, d: (0, d)),\n            pl.BlockSpec((F, block_d), lambda b, d: (0, d)),\n        ],"
)

# Fix in_specs for dw_kernel
text = text.replace(
    "        in_specs=[\n            pl.BlockSpec((B, D), lambda f, d: (0, 0)),\n            pl.BlockSpec((B, F), lambda f, d: (0, 0)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n        ],",
    "        in_specs=[\n            pl.BlockSpec((B, block_d), lambda f, d: (0, d)),\n            pl.BlockSpec((B, block_f), lambda f, d: (0, f)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n        ],"
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

