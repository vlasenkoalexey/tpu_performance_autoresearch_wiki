---
title: 'Module: torchtitan/experiments/torchft/diloco/utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/torchft/diloco/utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.torchft.diloco.utils`/
symbols:
  fragment_llm: fragment_llm().
  module_split: module_split().
  module_split._build_fragment_from_modules: module_split()._build_fragment_from_modules().
---
# Module: [`torchtitan/experiments/torchft/diloco/utils.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/diloco/utils.py)

## Functions
- <a id="module_split._build_fragment_from_modules"></a>`_build_fragment_from_modules(fragment_idx: int, module_names: list[str])` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/diloco/utils.py#L44)
- <a id="fragment_llm"></a>`fragment_llm(model: nn.Module, ft_config: TorchFTConfig, n_layers: int)` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/diloco/utils.py#L112)
- <a id="module_split"></a>`module_split(model: nn.Module, module_fqns_per_model_fragment: list[list[str]])` — [`L15`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/diloco/utils.py#L15) — This API creates fragments based on specified module names for each fragment.

