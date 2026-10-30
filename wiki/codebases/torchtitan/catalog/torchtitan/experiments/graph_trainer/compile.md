---
title: 'Module: torchtitan/experiments/graph_trainer/compile.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/compile.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.compile`/
symbols:
  apply_compile: apply_compile().
  _apply_jit_compile: _apply_jit_compile().
---
# Module: [`torchtitan/experiments/graph_trainer/compile.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/compile.py)

## Functions
- <a id="_apply_jit_compile"></a>`_apply_jit_compile(model: nn.Module, compile_config: GraphTrainerCompileConfig)` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/compile.py#L38) — Apply JIT compilation (torch.compile with custom backend).
- <a id="apply_compile"></a>`apply_compile(model: nn.Module, *, compile_config: GraphTrainerCompileConfig, parallelism: ParallelismConfig, parallel_dims: ParallelDims, dump_folder: str)` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/compile.py#L56) — Apply compilation to the model based on the configured mode. — documented in [graph-trainer](../../../../concepts/graph-trainer.md)

