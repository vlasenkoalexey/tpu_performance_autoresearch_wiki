---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/hf_sharding.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/hf_sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.hf_sharding`/
symbols:
  set_hf_sharding_configs: set_hf_sharding_configs().
  _attach_flex_kernel: _attach_flex_kernel().
  _set_layer_sharding_configs: _set_layer_sharding_configs().
  _hf_norm_config: _hf_norm_config().
  _hf_activation_placement: _hf_activation_placement().
  _hf_colwise_config: _hf_colwise_config().
  _hf_rowwise_config: _hf_rowwise_config().
  _rope_config: _rope_config().
  _hf_sequence_parallel_placement: _hf_sequence_parallel_placement().
  _replicate_config: _replicate_config().
  DP: DP.
  CP: CP.
  TP: TP.
  _sp_activation: _sp_activation().
  _assert_all_states_sharded: _assert_all_states_sharded().
  _first_forward_arg: _first_forward_arg().
  _moe_subtree: _moe_subtree().
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/hf_sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py)

## Functions
- <a id="_assert_all_states_sharded"></a>`_assert_all_states_sharded(root: nn.Module, *, path: str, skip: tuple[nn.Module, ...] = ())` — [`L491`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L491) — Raise if any param/buffer-bearing submodule of ``root`` lacks a config.
- <a id="_attach_flex_kernel"></a>`_attach_flex_kernel(attn: nn.Module)` — [`L195`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L195) — Attach the flex-attention kernel Module carrying the attention local_map.
- <a id="_first_forward_arg"></a>`_first_forward_arg(module: nn.Module)` — [`L471`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L471) — Return the first positional arg name of ``module.forward``.
- <a id="_hf_activation_placement"></a>`_hf_activation_placement(*, tp: spmd.PerMeshAxisSpmdType, cp: spmd.PerMeshAxisSpmdType = spmd.S(1))` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L44) — Placement for Transformers activations with batch and sequence dims.
- <a id="_hf_colwise_config"></a>`_hf_colwise_config()` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L61) — Column-shard a linear whose output retains HF's batch dimension.
- <a id="_hf_norm_config"></a>`_hf_norm_config(*, enable_sp: bool)` — [`L402`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L402) — Norm sharding using HF's ``hidden_states`` arg name.
- <a id="_hf_rowwise_config"></a>`_hf_rowwise_config(*, output_sp: bool = False)` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L72) — Row-shard a linear whose output retains HF's batch dimension.
- <a id="_hf_sequence_parallel_placement"></a>`_hf_sequence_parallel_placement()` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L53) — Sequence-parallel placement for ``(batch, sequence, hidden)`` tensors.
- <a id="_moe_subtree"></a>`_moe_subtree(layer: nn.Module)` — [`L480`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L480) — Return the Titan MoE module on a layer, or None for dense layers.
- <a id="_replicate_config"></a>`_replicate_config(module: nn.Module)` — [`L420`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L420) — Replicate all params and buffers — ShardingConfig equivalent of NoParallel.
- <a id="_rope_config"></a>`_rope_config(module: nn.Module, *, enable_sp: bool)` — [`L434`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L434) — Sharding config for a rotary embedding module.
- <a id="_set_layer_sharding_configs"></a>`_set_layer_sharding_configs(layer: nn.Module, *, enable_sp: bool)` — [`L242`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L242) — Set ``_sharding_config`` on each sub-module of a decoder layer.
- <a id="_sp_activation"></a>`_sp_activation(*, enable_sp: bool)` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L89) — Activation layout for the sequence-parallel region.
- <a id="set_hf_sharding_configs"></a>`set_hf_sharding_configs(model: nn.Module, *, enable_sp: bool)` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L104) — Set ``_sharding_config`` on all HF modules for TP/EP parallelization.

## Module values
- <a id="CP"></a>`CP` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L40)
- <a id="DP"></a>`DP` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L39)
- <a id="TP"></a>`TP` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/hf_sharding.py#L41)

