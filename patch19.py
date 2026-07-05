import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

# We need to map the entire parameter space to HBM but use slicing to transfer chunks to VMEM
# So instead of dropping the HBM mapping, we restore it, but in the kernels we load everything through explicit pl.dslice bindings instead of referencing entire parameters. 
# It turns out the error was 'Allocation (size=201326592) would exceed memory (size=134217728) :: #allocation5 [shape = 'u8[201326592]{0}', space=vmem, size = 0xc000000'
# which indicates that it IS compiling! But we ran OOM inside VMEM (which has 32MB=33554432 limit, or 128MB=134217728 possibly on some devices/scoped allocs, and our allocation was 201MB).
# So the OOM is because we're not slicing B properly.

text = text.replace(
    "    def body_fn(b_idx, accs):\n        w_up = w_up_ref[pl.dslice(0, block_f), pl.dslice(0, block_d)]\n        w_gate = w_gate_ref[pl.dslice(0, block_f), pl.dslice(0, block_d)]",
    "    w_up = w_up_ref[pl.dslice(0, block_f), pl.dslice(0, block_d)]\n    w_gate = w_gate_ref[pl.dslice(0, block_f), pl.dslice(0, block_d)]\n    def body_fn(b_idx, accs):"
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

