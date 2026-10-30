---
title: 'Module: torchtitan/experiments/graph_trainer/jit_backend.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/jit_backend.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.jit_backend`/
symbols:
  get_compile_backend_with_passes: get_compile_backend_with_passes().
  get_compile_backend_with_passes.inductor_autobucketing_reordering_pass: get_compile_backend_with_passes().inductor_autobucketing_reordering_pass().
  get_compile_backend_with_passes.inductor_transformer_block_bucketing_reordering_pass: get_compile_backend_with_passes().inductor_transformer_block_bucketing_reordering_pass().
---
# Module: [`torchtitan/experiments/graph_trainer/jit_backend.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/jit_backend.py)

## Functions
- <a id="get_compile_backend_with_passes"></a>`get_compile_backend_with_passes(compile_config: CompileConfig, fsdp_manual_buckets: list[list[str] | str] | None)` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/jit_backend.py#L18) — Apply compile backend and additional graph passes.
- <a id="get_compile_backend_with_passes.inductor_autobucketing_reordering_pass"></a>`inductor_autobucketing_reordering_pass(gm: torch.fx.Graph)` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/jit_backend.py#L68)
- <a id="get_compile_backend_with_passes.inductor_transformer_block_bucketing_reordering_pass"></a>`inductor_transformer_block_bucketing_reordering_pass(gm: torch.fx.Graph)` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/jit_backend.py#L116)

