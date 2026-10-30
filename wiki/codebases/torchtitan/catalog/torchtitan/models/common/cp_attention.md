---
title: 'Module: torchtitan/models/common/cp_attention.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/cp_attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.cp_attention`/
symbols:
  KVAllGatherCPFlexInnerAttention: KVAllGatherCPFlexInnerAttention#
  CPInnerAttention: CPInnerAttention#
  KVAllGatherCPFlexInnerAttention.forward: KVAllGatherCPFlexInnerAttention#forward().
  UlyssesCPFlexInnerAttention.forward: UlyssesCPFlexInnerAttention#forward().
  CPInnerAttention.cp_shard: CPInnerAttention#cp_shard().
  UlyssesCPFlexInnerAttention: UlyssesCPFlexInnerAttention#
  KVAllGatherCPFlexInnerAttention.__init__: KVAllGatherCPFlexInnerAttention#__init__().
  KVAllGatherCPFlexInnerAttention.Config: KVAllGatherCPFlexInnerAttention#Config#
  UlyssesCPFlexInnerAttention.Config: UlyssesCPFlexInnerAttention#Config#
  _TOKEN_DIM: _TOKEN_DIM.
  KVAllGatherCPFlexInnerAttention.cp_shard: KVAllGatherCPFlexInnerAttention#cp_shard().
  UlyssesCPFlexInnerAttention.cp_shard: UlyssesCPFlexInnerAttention#cp_shard().
  _HEAD_DIM: _HEAD_DIM.
  KVAllGatherCPFlexInnerAttention.Config.reduce_dtype: KVAllGatherCPFlexInnerAttention#Config#reduce_dtype.
  KVAllGatherCPFlexInnerAttention.reduce_dtype: KVAllGatherCPFlexInnerAttention#reduce_dtype.
  __all__: __all__.
---
# Module: [`torchtitan/models/common/cp_attention.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py)

## Classes
### <a id="CPInnerAttention"></a>`CPInnerAttention`  ·  implements/extends ABC
- def: [`torchtitan/models/common/cp_attention.py:39`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L39) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- doc: Inner attention that owns its context-parallel behavior.
- signature: `class CPInnerAttention(ABC):`
- members:
  - <a id="CPInnerAttention.cp_shard"></a>`cp_shard(cls, input_dict: dict[str, Any], input_shardings: dict[str, Any] | None, cp_mesh: DeviceMesh, load_balancer_type: str | None, ptrr_mask_key: str | None)` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L44) — Shard model inputs for this attention implementation.
- uses (calls/refs, reference-scoped): [`KVAllGatherCPFlexInnerAttention`](cp_attention.md#KVAllGatherCPFlexInnerAttention), [`cp_shard`](../../experiments/tpu/cp_attention.md#KVAllGatherCPInnerAttention.cp_shard), [`UlyssesCPFlexInnerAttention`](cp_attention.md#UlyssesCPFlexInnerAttention), [`_TPUCPInnerAttention`](../../experiments/tpu/cp_attention.md#_TPUCPInnerAttention), [`cp_shard`](../../experiments/tpu/cp_attention.md#UlyssesCPInnerAttention.cp_shard), [`cp_shard`](cp_attention.md#KVAllGatherCPFlexInnerAttention.cp_shard), [`cp_shard`](cp_attention.md#UlyssesCPFlexInnerAttention.cp_shard)
- used by: [`validate_context_parallel`](../../config/validation.md#validate_context_parallel), [`_cp_shard_inputs`](decoder.md#Decoder._cp_shard_inputs), [`KVAllGatherCPFlexInnerAttention`](cp_attention.md#KVAllGatherCPFlexInnerAttention), [`UlyssesCPFlexInnerAttention`](cp_attention.md#UlyssesCPFlexInnerAttention), [`_TPUCPInnerAttention`](../../experiments/tpu/cp_attention.md#_TPUCPInnerAttention), [`__post_init__`](../../config/transform/context_parallel.md#ContextParallelTransform.__post_init__)

### <a id="KVAllGatherCPFlexInnerAttention"></a>`KVAllGatherCPFlexInnerAttention`  ·  implements/extends CPInnerAttention, FlexInnerAttention
- def: [`torchtitan/models/common/cp_attention.py:55`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L55) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- doc: FlexInnerAttention with sharded Q and all-gathered K/V.
- signature: `class KVAllGatherCPFlexInnerAttention(CPInnerAttention, FlexInnerAttention):`
- members:
  - <a id="KVAllGatherCPFlexInnerAttention.cp_shard"></a>`cp_shard(cls, input_dict: dict[str, Any], input_shardings: dict[str, Any] | None, cp_mesh: DeviceMesh, load_balancer_type: str | None, ptrr_mask_key: str | None)` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L68)
  - <a id="KVAllGatherCPFlexInnerAttention.forward"></a>`forward(self, q_THK: torch.Tensor, k_THK: torch.Tensor, v_THV: torch.Tensor, **kwargs)` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L88)
  - <a id="KVAllGatherCPFlexInnerAttention.reduce_dtype"></a>`reduce_dtype` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L65)
- protocol/private: <a id="KVAllGatherCPFlexInnerAttention.__init__"></a>`__init__`[`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L63)
- uses (calls/refs, reference-scoped): [`TORCH_DTYPE_MAP`](../../config/__init__.md#TORCH_DTYPE_MAP), [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`MeshAxisName`](../../distributed/parallel_dims.md#MeshAxisName), [`forward`](attention.md#FlexInnerAttention.forward), [`prepare_context_parallel_input`](../../distributed/context_parallel/api.md#prepare_context_parallel_input), [`CP`](../../distributed/parallel_dims.md#MeshAxisName.CP), [`CPInnerAttention`](cp_attention.md#CPInnerAttention), [`spmd_mesh_group`](../../distributed/spmd_types.md#spmd_mesh_group), [`Config`](cp_attention.md#KVAllGatherCPFlexInnerAttention.Config), [`__init__`](attention.md#FlexInnerAttention.__init__), [`_TOKEN_DIM`](cp_attention.md#_TOKEN_DIM), [`reduce_dtype`](cp_attention.md#KVAllGatherCPFlexInnerAttention.Config.reduce_dtype)
- used by: [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`forward`](attention.md#FlexInnerAttention.forward), [`CPInnerAttention`](cp_attention.md#CPInnerAttention), [`cp_shard`](cp_attention.md#CPInnerAttention.cp_shard)  (18 test-only)

### <a id="KVAllGatherCPFlexInnerAttention.Config"></a>`KVAllGatherCPFlexInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/cp_attention.py:59`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L59)
- signature: `class Config(FlexInnerAttention.Config):`
- members:
  - <a id="KVAllGatherCPFlexInnerAttention.Config.reduce_dtype"></a>`reduce_dtype` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L60) — ---
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`Config`](attention.md#FlexInnerAttention.Config)
- used by: [`__init__`](cp_attention.md#KVAllGatherCPFlexInnerAttention.__init__)

### <a id="UlyssesCPFlexInnerAttention"></a>`UlyssesCPFlexInnerAttention`  ·  implements/extends CPInnerAttention, FlexInnerAttention
- def: [`torchtitan/models/common/cp_attention.py:113`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L113) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- doc: Run FlexInnerAttention with sequence-to-head all-to-all redistribution.
- signature: `class UlyssesCPFlexInnerAttention(CPInnerAttention, FlexInnerAttention):`
- members:
  - <a id="UlyssesCPFlexInnerAttention.cp_shard"></a>`cp_shard(cls, input_dict: dict[str, Any], input_shardings: dict[str, Any] | None, cp_mesh: DeviceMesh, load_balancer_type: str | None, ptrr_mask_key: str | None)` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L121)
  - <a id="UlyssesCPFlexInnerAttention.forward"></a>`forward(self, q_THK: torch.Tensor, k_THK: torch.Tensor, v_THV: torch.Tensor, **kwargs)` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L145)
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`MeshAxisName`](../../distributed/parallel_dims.md#MeshAxisName), [`forward`](attention.md#FlexInnerAttention.forward), [`prepare_context_parallel_input`](../../distributed/context_parallel/api.md#prepare_context_parallel_input), [`CP`](../../distributed/parallel_dims.md#MeshAxisName.CP), [`CPInnerAttention`](cp_attention.md#CPInnerAttention), [`spmd_mesh_group`](../../distributed/spmd_types.md#spmd_mesh_group), [`_TOKEN_DIM`](cp_attention.md#_TOKEN_DIM), [`_HEAD_DIM`](cp_attention.md#_HEAD_DIM)
- used by: [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`parallelize_gptoss`](../gpt_oss/parallelize.md#parallelize_gptoss), [`validate_context_parallel`](../../config/validation.md#validate_context_parallel), [`forward`](attention.md#FlexInnerAttention.forward), [`CPInnerAttention`](cp_attention.md#CPInnerAttention), [`cp_shard`](cp_attention.md#CPInnerAttention.cp_shard)  (1 test-only)

### <a id="UlyssesCPFlexInnerAttention.Config"></a>`UlyssesCPFlexInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/cp_attention.py:117`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L117)
- signature: `class Config(FlexInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](attention.md#FlexInnerAttention), [`Config`](attention.md#FlexInnerAttention.Config)
- used by: [`parallelize_gptoss`](../gpt_oss/parallelize.md#parallelize_gptoss)

## Module values
- <a id="_HEAD_DIM"></a>`_HEAD_DIM` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L36)
- <a id="_TOKEN_DIM"></a>`_TOKEN_DIM` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L35)
- <a id="__all__"></a>`__all__` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/cp_attention.py#L29)

