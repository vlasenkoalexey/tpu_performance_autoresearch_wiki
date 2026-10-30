---
title: 'Module: torchtitan/distributed/parallel_dims.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/parallel_dims.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.parallel_dims`/
symbols:
  ParallelDims: ParallelDims#
  MeshAxisName: MeshAxisName#
  ParallelDims.get_mesh: ParallelDims#get_mesh().
  ParallelDims.pp: ParallelDims#pp.
  ParallelDims.tp: ParallelDims#tp.
  ParallelDims.get_optional_mesh: ParallelDims#get_optional_mesh().
  ParallelDims.dp_shard: ParallelDims#dp_shard.
  ParallelDims.cp: ParallelDims#cp.
  ParallelDims.ep: ParallelDims#ep.
  ParallelDims.pp_enabled: ParallelDims#pp_enabled().
  ParallelDims.dp_replicate: ParallelDims#dp_replicate.
  ParallelDims.build_mesh: ParallelDims#build_mesh().
  ParallelDims.world_size: ParallelDims#world_size.
  ParallelDims.spmd_backend: ParallelDims#spmd_backend.
  ParallelDims.dp_replicate_enabled: ParallelDims#dp_replicate_enabled().
  ParallelDims.cp_enabled: ParallelDims#cp_enabled().
  ParallelDims.tp_enabled: ParallelDims#tp_enabled().
  ParallelDims.ep_enabled: ParallelDims#ep_enabled().
  ParallelDims.from_config: ParallelDims#from_config().
  ParallelDims._validate_meshes: ParallelDims#_validate_meshes().
  MeshAxisName.CP: MeshAxisName#CP.
  ParallelDims._global_meshes: ParallelDims#_global_meshes.
  ParallelDims._validate: ParallelDims#_validate().
  ParallelDims.dp_enabled: ParallelDims#dp_enabled().
  MeshAxisName.DP: MeshAxisName#DP.
  ParallelDims._single_axis_meshes: ParallelDims#_single_axis_meshes.
  MeshAxisName.TP: MeshAxisName#TP.
  ParallelDims.spmd_dense_mesh: ParallelDims#spmd_dense_mesh().
  ParallelDims.get_activated_mesh: ParallelDims#get_activated_mesh().
  unfold_dp_axis: unfold_dp_axis().
  ParallelDims.dp_cp_enabled: ParallelDims#dp_cp_enabled().
  ParallelDims.get_dense_tp_mesh: ParallelDims#get_dense_tp_mesh().
  ParallelDims.seq_len_divisor: ParallelDims#seq_len_divisor().
  ParallelDims.resolve_mesh: ParallelDims#resolve_mesh().
  ParallelDims._world_mesh: ParallelDims#_world_mesh.
  ParallelDims.spmd_sparse_mesh: ParallelDims#spmd_sparse_mesh().
  ParallelDims.non_data_parallel_size: ParallelDims#non_data_parallel_size().
  ParallelDims.get_all_one_dimensional_meshes: ParallelDims#get_all_one_dimensional_meshes().
  ParallelDims._mesh_exist: ParallelDims#_mesh_exist().
  ParallelDims.resolve_shared_mesh: ParallelDims#resolve_shared_mesh().
  ParallelDims.unflatten_mesh: ParallelDims#unflatten_mesh().
  unfold_dp_axes: unfold_dp_axes().
  ParallelDims.world_mesh: ParallelDims#world_mesh().
  ParallelDims.fsdp_enabled: ParallelDims#fsdp_enabled().
  ParallelDims.dp_shard_enabled: ParallelDims#dp_shard_enabled().
  MeshAxisName.DP_SHARD: MeshAxisName#DP_SHARD.
  MeshAxisName.EP: MeshAxisName#EP.
  MeshAxisName.EFSDP: MeshAxisName#EFSDP.
  ParallelDims._multi_axis_meshes: ParallelDims#_multi_axis_meshes.
  ParallelDims.__post_init__: ParallelDims#__post_init__().
  MeshAxisName.DP_REPLICATE: MeshAxisName#DP_REPLICATE.
  init_device_mesh: init_device_mesh().
  ParallelDims.enable_tpu_topo_mesh: ParallelDims#enable_tpu_topo_mesh.
  __all__: __all__.
  MeshAxisName.FSDP: MeshAxisName#FSDP.
  MeshAxisName.PP: MeshAxisName#PP.
---
# Module: [`torchtitan/distributed/parallel_dims.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py)

## Classes
### <a id="MeshAxisName"></a>`MeshAxisName`  ·  implements/extends StrEnum
- def: [`torchtitan/distributed/parallel_dims.py:72`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L72) — documented in [config-overrides](../../../concepts/config-overrides.md)
- doc: Names for axes of a `DeviceMesh`.
- signature: `class MeshAxisName(StrEnum):`
- members:
  - <a id="MeshAxisName.CP"></a>`CP` — [`L90`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L90)
  - <a id="MeshAxisName.DP"></a>`DP` — [`L85`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L85)
  - <a id="MeshAxisName.DP_REPLICATE"></a>`DP_REPLICATE` — [`L86`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L86)
  - <a id="MeshAxisName.DP_SHARD"></a>`DP_SHARD` — [`L87`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L87)
  - <a id="MeshAxisName.EFSDP"></a>`EFSDP` — [`L93`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L93)
  - <a id="MeshAxisName.EP"></a>`EP` — [`L92`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L92)
  - <a id="MeshAxisName.FSDP"></a>`FSDP` — [`L88`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L88)
  - <a id="MeshAxisName.PP"></a>`PP` — [`L91`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L91)
  - <a id="MeshAxisName.TP"></a>`TP` — [`L89`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L89)
- used by: [`_dist_muon_optimizer`](../models/kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`preprocess_inputs`](../models/qwen3_5/model.md#Qwen35Model.preprocess_inputs), [`forward`](../experiments/tpu/cp_attention.md#KVAllGatherCPInnerAttention.forward), [`preprocess_inputs`](../models/kimi_k3/model.md#KimiK3Model.preprocess_inputs), [`forward`](../models/kimi_k3/model.md#KimiK3Model.forward), [`forward`](../experiments/tpu/cp_attention.md#UlyssesCPInnerAttention.forward), [`TP`](../models/qwen3_5/sharding.md#TP), [`build`](../components/quantization/nvfp4.md#NVFP4Linear.Config.build), [`resolve_placements`](../protocols/sharding.md#resolve_placements), [`_per_expert_compute_layout`](../models/kimi_k2_7/config_registry.md#_per_expert_compute_layout), [`DP`](../models/common/decoder_sharding.md#DP), [`CP`](../models/common/decoder_sharding.md#CP), [`_validate_even_model_parallel_param_sharding`](../protocols/module.md#Module._validate_even_model_parallel_param_sharding), [`TP`](../models/common/decoder_sharding.md#TP), [`annotate_deltanet_cu_seqlens`](../models/qwen3_5/sharding.md#annotate_deltanet_cu_seqlens), [`CP`](../models/muse_glimmer/sharding.md#CP), [`DP`](../models/muse_glimmer/sharding.md#DP), [`forward`](../models/common/cp_attention.md#KVAllGatherCPFlexInnerAttention.forward), [`forward`](../models/common/cp_attention.md#UlyssesCPFlexInnerAttention.forward), [`_maybe_cache_cp_rank`](../experiments/tpu/cp_attention.md#KVAllGatherCPInnerAttention._maybe_cache_cp_rank), [`TP`](../models/muse_glimmer/sharding.md#TP), [`unfold_dp_axis`](parallel_dims.md#unfold_dp_axis), [`TP`](../models/kimi_k2_7/sharding.md#TP), [`_per_axis_types`](spmd_types.md#_per_axis_types), [`spmd_axes`](spmd_types.md#spmd_axes), [`_cp_shard_dims`](context_parallel/api.md#_cp_shard_dims), [`DP`](../models/common/vision_encoder_sharding.md#DP), [`DP`](../models/kimi_k3/sharding.md#DP), [`DP`](../models/qwen3_5/sharding.md#DP), [`TP`](../models/common/vision_encoder_sharding.md#TP), [`resolve_mesh`](parallel_dims.md#ParallelDims.resolve_mesh), [`CP`](../experiments/transformers_modeling_backend/hf_sharding.md#CP), [`DP`](../experiments/transformers_modeling_backend/hf_sharding.md#DP), [`DP`](../models/kimi_k2_7/sharding.md#DP), [`TP`](../experiments/transformers_modeling_backend/hf_sharding.md#TP), [`CP`](../models/common/vision_encoder_sharding.md#CP), [`CP`](../models/deepseek_v4/sharding.md#CP), [`DP`](../models/deepseek_v4/sharding.md#DP), [`TP`](../models/deepseek_v4/sharding.md#TP), [`CP`](../models/flux/sharding.md#CP)  (+12 more; 2 test-only)

### <a id="ParallelDims"></a>`ParallelDims`
- def: [`torchtitan/distributed/parallel_dims.py:112`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L112) — documented in [flux-diffusion-model](../../../concepts/flux-diffusion-model.md)
- signature: `class ParallelDims:`
- members:
  - <a id="ParallelDims._validate_meshes"></a>`_validate_meshes(self)` — [`L349`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L349) — Validate that created meshes have the expected sizes.
  - <a id="ParallelDims.build_mesh"></a>`build_mesh(self)` — [`L192`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L192) — Build the device mesh with the required mesh dimensions. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.cp_enabled"></a>`cp_enabled(self)` — [`L617`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L617)
  - <a id="ParallelDims.dp_cp_enabled"></a>`dp_cp_enabled(self)` — [`L621`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L621)
  - <a id="ParallelDims.dp_enabled"></a>`dp_enabled(self)` — [`L605`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L605)
  - <a id="ParallelDims.dp_replicate_enabled"></a>`dp_replicate_enabled(self)` — [`L609`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L609)
  - <a id="ParallelDims.dp_shard_enabled"></a>`dp_shard_enabled(self)` — [`L613`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L613)
  - <a id="ParallelDims.ep_enabled"></a>`ep_enabled(self)` — [`L637`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L637)
  - <a id="ParallelDims.from_config"></a>`from_config(cls, parallelism_config: ParallelismConfig, world_size: int)` — [`L129`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L129) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.fsdp_enabled"></a>`fsdp_enabled(self)` — [`L625`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L625)
  - <a id="ParallelDims.get_activated_mesh"></a>`get_activated_mesh(self, axes: list[str])` — [`L486`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L486) — Submesh of ``axes`` filtered to those actually enabled in this run.
  - <a id="ParallelDims.get_all_one_dimensional_meshes"></a>`get_all_one_dimensional_meshes(self)` — [`L557`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L557) — Get all enabled one-dimensional device meshes.
  - <a id="ParallelDims.get_dense_tp_mesh"></a>`get_dense_tp_mesh(self)` — [`L480`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L480) — Return the TP-axis mesh used by dense forward/backward computation.
  - <a id="ParallelDims.get_mesh"></a>`get_mesh(self, dims: str | list[str])` — [`L442`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L442) — Get a device mesh by dimension name(s), raising if not available. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.get_optional_mesh"></a>`get_optional_mesh(self, dims: str | list[str], *, include_singleton_axes: bool = False)` — [`L374`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L374) — Get a device mesh by dimension name(s), returning None if not enabled. — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.non_data_parallel_size"></a>`non_data_parallel_size(self)` — [`L641`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L641)
  - <a id="ParallelDims.pp_enabled"></a>`pp_enabled(self)` — [`L633`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L633)
  - <a id="ParallelDims.resolve_mesh"></a>`resolve_mesh(self, axes: Iterable[MeshAxisName | str])` — [`L504`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L504) — Resolve the device mesh for a set of mesh axis names.
  - <a id="ParallelDims.resolve_shared_mesh"></a>`resolve_shared_mesh(self, placements: Iterable[SpmdType | None])` — [`L527`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L527) — Resolve the mesh shared by a list of SpmdLayouts.
  - <a id="ParallelDims.seq_len_divisor"></a>`seq_len_divisor(self)` — [`L645`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L645)
  - <a id="ParallelDims.spmd_dense_mesh"></a>`spmd_dense_mesh(self)` — [`L468`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L468) — Dense SPMD mesh used for forward/backward typechecking.
  - <a id="ParallelDims.spmd_sparse_mesh"></a>`spmd_sparse_mesh(self)` — [`L474`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L474) — Sparse SPMD mesh used inside expert dispatch.
  - <a id="ParallelDims.tp_enabled"></a>`tp_enabled(self)` — [`L629`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L629)
  - <a id="ParallelDims.unflatten_mesh"></a>`unflatten_mesh(world_mesh: DeviceMesh, dim_names: tuple[str, ...], dim_degrees: tuple[int, ...])` — [`L233`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L233) — Unflatten the world mesh to create the required mesh dimensions.
  - <a id="ParallelDims.world_mesh"></a>`world_mesh(self)` — [`L599`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L599)
  - <a id="ParallelDims.cp"></a>`cp` — [`L115`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L115) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.dp_replicate"></a>`dp_replicate` — [`L113`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L113) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.dp_shard"></a>`dp_shard` — [`L114`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L114) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.enable_tpu_topo_mesh"></a>`enable_tpu_topo_mesh` — [`L121`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L121)
  - <a id="ParallelDims.ep"></a>`ep` — [`L118`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L118) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.pp"></a>`pp` — [`L117`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L117) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.spmd_backend"></a>`spmd_backend` — [`L120`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L120) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.tp"></a>`tp` — [`L116`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L116) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
  - <a id="ParallelDims.world_size"></a>`world_size` — [`L119`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L119) — documented in [parallel-dims-and-parallelization](../../../concepts/parallel-dims-and-parallelization.md)
- protocol/private: <a id="ParallelDims.__post_init__"></a>`__post_init__`[`L144`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L144), <a id="ParallelDims._global_meshes"></a>`_global_meshes`[`L316`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L316), <a id="ParallelDims._mesh_exist"></a>`_mesh_exist`[`L175`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L175), <a id="ParallelDims._multi_axis_meshes"></a>`_multi_axis_meshes`[`L125`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L125), <a id="ParallelDims._single_axis_meshes"></a>`_single_axis_meshes`[`L124`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L124), <a id="ParallelDims._validate"></a>`_validate`[`L147`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L147), <a id="ParallelDims._world_mesh"></a>`_world_mesh`[`L126`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L126)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`ParallelismConfig`](../config/configs.md#ParallelismConfig), [`data_parallel_shard_degree`](../config/configs.md#ParallelismConfig.data_parallel_shard_degree), [`MeshAxisName`](parallel_dims.md#MeshAxisName), [`tensor_parallel_degree`](../config/configs.md#ParallelismConfig.tensor_parallel_degree), [`expert_parallel_degree`](../config/configs.md#ParallelismConfig.expert_parallel_degree), [`spmd_backend`](../config/configs.md#ParallelismConfig.spmd_backend), [`context_parallel_degree`](../config/configs.md#ParallelismConfig.context_parallel_degree), [`pipeline_parallel_degree`](../config/configs.md#ParallelismConfig.pipeline_parallel_degree), [`device_type`](../tools/utils.md#device_type), [`data_parallel_replicate_degree`](../config/configs.md#ParallelismConfig.data_parallel_replicate_degree), [`spmd_axes`](spmd_types.md#spmd_axes), [`enable_tpu_topo_mesh`](../config/configs.md#ParallelismConfig.enable_tpu_topo_mesh), [`init_device_mesh`](parallel_dims.md#init_device_mesh)
- used by: [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`__init__`](../experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`pp_schedule`](../experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`transfer_stream`](../trainer.md#Trainer.transfer_stream), [`train_step`](../trainer.md#Trainer.train_step), [`validate`](../models/flux/validate.md#FluxValidator.validate), [`train_step`](../experiments/torchft/trainer.md#FaultTolerantTrainer.train_step), [`parallelize_conformer`](../experiments/tpu/conformer/infra/parallelize.md#parallelize_conformer), [`parallelize_gptoss`](../models/gpt_oss/parallelize.md#parallelize_gptoss), [`parallelize_flux`](../models/flux/parallelize.md#parallelize_flux), [`validate`](../components/validate.md#Validator.validate), [`parallelize_kimi_k3`](../models/kimi_k3/parallelize.md#parallelize_kimi_k3), [`graph_pipeline_llm`](../experiments/graph_trainer/graph_pp/pipeline.md#graph_pipeline_llm), [`parallelize_hf_transformers`](../experiments/transformers_modeling_backend/parallelize.md#parallelize_hf_transformers), [`parallelize_deepseekv3`](../models/deepseek_v3/parallelize.md#parallelize_deepseekv3), [`apply_simple_fsdp`](../experiments/graph_trainer/common_utils.md#apply_simple_fsdp), [`parallelize_qwen3_5`](../models/qwen3_5/parallelize.md#parallelize_qwen3_5), [`parallelize_qwen3`](../models/qwen3/parallelize.md#parallelize_qwen3), [`parallelize_kimi_k2_5`](../models/kimi_k2_7/parallelize.md#parallelize_kimi_k2_5), [`parallelize_muse_glimmer`](../models/muse_glimmer/parallelize.md#parallelize_muse_glimmer), [`parallelize_llama`](../models/llama3/parallelize.md#parallelize_llama), [`parallelize_muse_glimmer`](../experiments/tpu/muse_glimmer/infra/parallelize.md#parallelize_muse_glimmer), [`log`](../components/metrics.md#MetricsProcessor.log), [`train_step`](../models/flux/trainer.md#FluxTrainer.train_step), [`parallelize_autoparallel_deepseekv3`](../experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.md#parallelize_autoparallel_deepseekv3), [`parallelize_autoparallel_llama`](../experiments/graph_trainer/llama3/parallelize_autoparallel.md#parallelize_autoparallel_llama), [`pipeline_llm`](pipeline_parallel.md#pipeline_llm), [`compute_config_fingerprint`](../experiments/graph_trainer/precompile.md#compute_config_fingerprint), [`preprocess_inputs`](../models/qwen3_5/model.md#Qwen35Model.preprocess_inputs), [`__init__`](../components/metrics.md#MetricsProcessor.__init__), [`preprocess_inputs`](../models/muse_glimmer/model.md#MuseGlimmerModel.preprocess_inputs), [`parallel_dims`](../experiments/tpu/train_minimal.md#TrainerMinimal.parallel_dims), [`parallelize_encoders`](../models/flux/parallelize.md#parallelize_encoders), [`_train_step_optimizer_in_graph`](../experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._train_step_optimizer_in_graph), [`forward_backward_step`](../models/flux/trainer.md#FluxTrainer.forward_backward_step), [`forward_backward_step`](../trainer.md#Trainer.forward_backward_step), [`parallelize_llama`](../experiments/tpu/llama3/infra/parallelize.md#parallelize_llama), [`build_and_swap_native_moe`](../experiments/transformers_modeling_backend/moe_replacement.md#build_and_swap_native_moe), [`parallelize_hf_transformers_tpu`](../experiments/tpu/transformers_modeling_backend/parallelize.md#parallelize_hf_transformers_tpu)  (+89 more; 45 test-only)

## Functions
- <a id="init_device_mesh"></a>`init_device_mesh(device_type: str, mesh_shape: tuple[int, ...], mesh_dim_names: tuple[str, ...] | None = None, enable_tpu_topo_mesh: bool = False)` — [`L25`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L25)
- <a id="unfold_dp_axes"></a>`unfold_dp_axes(axes: Iterable[MeshAxisName | str])` — [`L104`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L104) — Expand logical ``dp`` into concrete dense storage mesh axes.
- <a id="unfold_dp_axis"></a>`unfold_dp_axis(axis: MeshAxisName | str)` — [`L96`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L96) — Expand logical ``dp`` into concrete dense storage mesh axes.

## Module values
- <a id="__all__"></a>`__all__` — [`L64`](../../../../../../raw/code/torchtitan/torchtitan/distributed/parallel_dims.py#L64)

