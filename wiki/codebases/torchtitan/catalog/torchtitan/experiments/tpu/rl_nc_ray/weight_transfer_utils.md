---
title: 'Module: torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.rl_nc_ray.weight_transfer_utils`/
symbols:
  load_weights_on_driver: load_weights_on_driver().
  prepare_trainer_state_dict: prepare_trainer_state_dict().
  load_weights_on_worker: load_weights_on_worker().
  logger: logger.
  _load_single_group_on_worker: _load_single_group_on_worker().
  get_layer_group: get_layer_group().
  get_clean_name: get_clean_name().
  get_sorted_groups: get_sorted_groups().
  _prepare_local_tensors_for_loading: _prepare_local_tensors_for_loading().
  SYNC_LAYER_BY_LAYER: SYNC_LAYER_BY_LAYER.
  TPU_COPY_CHUNK_SIZE_PARAMETERS: TPU_COPY_CHUNK_SIZE_PARAMETERS.
---
# Module: [`torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py)

## Functions
- <a id="_load_single_group_on_worker"></a>`_load_single_group_on_worker(vllm_model, group_sd: dict, rank: int)` — [`L410`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L410) — Slices and streams parameters of a single group/layer to TPU worker.
- <a id="_prepare_local_tensors_for_loading"></a>`_prepare_local_tensors_for_loading(items_dict: dict, target_params: dict, rank: int)` — [`L264`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L264) — Takes global CPU tensors (items_dict) transferred from Trainer,
- <a id="get_clean_name"></a>`get_clean_name(name: str)` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L44) — Strip FSDP/DCP wrapper prefixes from state dict keys to match standard model namespaces.
- <a id="get_layer_group"></a>`get_layer_group(key: str)` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L51) — Given a state dict key, returns its group name (e.g. 'embeddings', 'layers.0', 'output').
- <a id="get_sorted_groups"></a>`get_sorted_groups(keys: list[str])` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L66) — Groups state dict keys and returns the group names sorted in forward order.
- <a id="load_weights_on_driver"></a>`load_weights_on_driver(vllm_model, state_dict_data: dict)` — [`L462`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L462) — Fallback weight loader for single-process driver runs where workers do not exist.
- <a id="load_weights_on_worker"></a>`load_weights_on_worker(vllm_model, state_dict: dict, rank: int)` — [`L311`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L311) — Worker-side weight loader. Performs host-side CPU sharding (slicing)
- <a id="prepare_trainer_state_dict"></a>`prepare_trainer_state_dict(model)` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L103) — Extracts, replicates, and offloads model parameters directly using TPU Inter-Chip Connect (ICI).

## Module values
- <a id="SYNC_LAYER_BY_LAYER"></a>`SYNC_LAYER_BY_LAYER` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L32)
- <a id="TPU_COPY_CHUNK_SIZE_PARAMETERS"></a>`TPU_COPY_CHUNK_SIZE_PARAMETERS` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L37)
- <a id="logger"></a>`logger` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py#L26)

