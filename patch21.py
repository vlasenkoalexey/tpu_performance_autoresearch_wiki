import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

# We got "Loads are only allowed on VMEM and SMEM references" again!
# This means something inside one of the kernels is triggering an abstract load from an HBM reference.
# Looking at the code for dx_kernel:
# x = x_ref[pl.dslice(0, block_b), pl.dslice(0, block_d)] 
#
# BUT wait! x_ref is passed with `pl.BlockSpec((block_b, block_d), lambda b, d: (b, d))`.
# This means x_ref is ALREADY sliced in VMEM!
# It is NOT an HBM reference of shape (B, D). It is a VMEM reference of shape (block_b, block_d).
# So doing x_ref[pl.dslice(...)] is invalid / redundant on a VMEM ref.
# Same for g_ref, w_up_ref, and w_gate_ref in dw_kernel!
# And same for w_up_ref and w_gate_ref in dx_kernel ? No wait, w_up_ref in dx_kernel is mapped as HBM!

# Let's clean this up so ALL inputs are mapped to VMEM using the parallel grid and explicit memory_space=HBM is removed. We don't want ANY HBM references inside the kernel.

replacement = """def dx_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dx_ref, *, block_b, block_f, block_d, num_f):
    x = x_ref[...]
    def body_fn(f_idx, acc):
        g = g_ref[pl.dslice(0, block_b), pl.dslice(f_idx * block_f, block_f)]
        w_up = w_up_ref[pl.dslice(f_idx * block_f, block_f), pl.dslice(0, block_d)]
        w_gate = w_gate_ref[pl.dslice(f_idx * block_f, block_f), pl.dslice(0, block_d)]
"""

text = text.replace(
    "def dx_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dx_ref, *, block_b, block_f, block_d, num_f):\n    def body_fn(f_idx, acc):\n        x = x_ref[pl.dslice(0, block_b), pl.dslice(0, block_d)]\n        g = g_ref[pl.dslice(0, block_b), pl.dslice(f_idx * block_f, block_f)]\n        w_up = w_up_ref[pl.dslice(f_idx * block_f, block_f), pl.dslice(0, block_d)]\n        w_gate = w_gate_ref[pl.dslice(f_idx * block_f, block_f), pl.dslice(0, block_d)]",
    replacement
)

replacement2 = """def dw_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dw_up_ref, dw_gate_ref, *, block_b, block_f, block_d, num_b):
    w_up = w_up_ref[...]
    w_gate = w_gate_ref[...]
    def body_fn(b_idx, accs):
        acc_up, acc_gate = accs
        
        x = x_ref[pl.dslice(b_idx * block_b, block_b), pl.dslice(0, block_d)]
        g = g_ref[pl.dslice(b_idx * block_b, block_b), pl.dslice(0, block_f)]
"""

text = text.replace(
    "def dw_kernel(x_ref, g_ref, w_up_ref, w_gate_ref, dw_up_ref, dw_gate_ref, *, block_b, block_f, block_d, num_b):\n    def body_fn(b_idx, accs):\n        w_up = w_up_ref[pl.dslice(0, block_f), pl.dslice(0, block_d)]\n        w_gate = w_gate_ref[pl.dslice(0, block_f), pl.dslice(0, block_d)]\n        acc_up, acc_gate = accs\n        \n        x = x_ref[pl.dslice(b_idx * block_b, block_b), pl.dslice(0, block_d)]\n        g = g_ref[pl.dslice(b_idx * block_b, block_b), pl.dslice(0, block_f)]",
    replacement2
)

# And now we remove the memory_space=pltpu.HBM again from the in_specs
text = text.replace(
    "        in_specs=[\n            pl.BlockSpec((block_b, block_d), lambda b, d: (b, d)),\n            pl.BlockSpec((B, F), lambda b, d: (0, 0), memory_space=pltpu.HBM),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0), memory_space=pltpu.HBM),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0), memory_space=pltpu.HBM),\n        ],",
    "        in_specs=[\n            pl.BlockSpec((block_b, block_d), lambda b, d: (b, d)),\n            pl.BlockSpec((B, F), lambda b, d: (0, 0)),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0)),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0)),\n        ],"
)

text = text.replace(
    "        in_specs=[\n            pl.BlockSpec((B, D), lambda f, d: (0, 0), memory_space=pltpu.HBM),\n            pl.BlockSpec((B, F), lambda f, d: (0, 0), memory_space=pltpu.HBM),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n        ],",
    "        in_specs=[\n            pl.BlockSpec((B, D), lambda f, d: (0, 0)),\n            pl.BlockSpec((B, F), lambda f, d: (0, 0)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n        ],"
)


with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

