---
title: 'Module: torchtitan/experiments/graph_trainer/tests/_trainer_test_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/_trainer_test_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests._trainer_test_utils`/
symbols:
  build_minimal_trainer: build_minimal_trainer().
---
# Module: [`torchtitan/experiments/graph_trainer/tests/_trainer_test_utils.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/_trainer_test_utils.py)

## Functions
- <a id="build_minimal_trainer"></a>`build_minimal_trainer(model: nn.Module, model_config, trainer_cls: type[Trainer], *, activation_checkpoint_mode: str = "none", compile_enable_passes: bool = True, compile_enable_inplace_graph_gradient_accumulation: bool = False, compile_passes: list[str] | None = None, compile_ep_overlap_enabled: bool = False, compile_ep_overlap_chunk_dim: str = "batch", compile_ep_overlap_chunk_strategy: str = "graph", compile_ep_overlap_module_fqn: str = "layers.*", compile_ep_overlap_disable_early_grad_accumulation: bool = False, compile_inductor_compilation: str = "regional", compile_disable_passes: list[str] | None = None, compile_numerics_changing_optim: bool = False, tokenizer=None, fsdp_reshard_after_forward: str = "default")` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/_trainer_test_utils.py#L24) — Build the minimal Trainer/GraphTrainer needed for single-GPU test steps.

