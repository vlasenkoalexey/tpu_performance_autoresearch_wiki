---
title: 'Module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.gdn_pcp_fused.config`/
symbols:
  GDNConfig.seq_tile_size: GDNConfig#seq_tile_size().
  GDNConfig.dtypes: GDNConfig#dtypes.
  GDNConfig.chunk_size: GDNConfig#chunk_size().
  Dtypes.compute: Dtypes#compute.
  GDNConfig.get_scratch_shape_dict: GDNConfig#get_scratch_shape_dict().
  GDNConfig: GDNConfig#
  GDNConfig.num_v_heads: GDNConfig#num_v_heads.
  GDNConfig.conv_hbm_offset: GDNConfig#conv_hbm_offset().
  GDNConfig.kq_head_dim: GDNConfig#kq_head_dim.
  GDNConfig.get_out_shape: GDNConfig#get_out_shape().
  GDNConfig.tile_size: GDNConfig#tile_size.
  GDNConfig.window_size: GDNConfig#window_size.
  GDNConfig.v_per_kq_head: GDNConfig#v_per_kq_head().
  GDNConfig.v_head_dim: GDNConfig#v_head_dim.
  GDNConfig.is_kda: GDNConfig#is_kda().
  GDNConfig.num_kq_heads: GDNConfig#num_kq_heads.
  GDNConfig.prev_kernel_size: GDNConfig#prev_kernel_size().
  GDNConfig.gate_dim: GDNConfig#gate_dim().
  GDNConfig.use_recurrent: GDNConfig#use_recurrent().
  GDNConfig.v_dim_size: GDNConfig#v_dim_size().
  GDNConfig.mode: GDNConfig#mode.
  GDNConfig.dim_size: GDNConfig#dim_size.
  GDNConfig.attention_mode: GDNConfig#attention_mode.
  GDNConfig.triangular_block_size: GDNConfig#triangular_block_size().
  GDNConfig.kq_dim_size: GDNConfig#kq_dim_size().
  GDNMode: GDNMode#
  Dtypes.recurrent_state: Dtypes#recurrent_state.
  GDNConfig.aligned_num_v_heads: GDNConfig#aligned_num_v_heads().
  GDNMode.PER_SEQ: GDNMode#PER_SEQ.
  Dtypes.conv_state: Dtypes#conv_state.
  GDNConfig.batch_size: GDNConfig#batch_size.
  GDNConfig.kernel_size: GDNConfig#kernel_size.
  GDNConfig.aligned_gate_dim: GDNConfig#aligned_gate_dim().
  AttentionMode: AttentionMode#
  Dtypes: Dtypes#
  Dtypes.act_out: Dtypes#act_out.
  GDNConfig.is_shared: GDNConfig#is_shared.
  GDNConfig.recurrent_hbm_offset: GDNConfig#recurrent_hbm_offset().
  AttentionMode.GDN: AttentionMode#GDN.
  AttentionMode.KDA: AttentionMode#KDA.
  Dtypes.act_in: Dtypes#act_in.
  GDNConfig.num_buffers: GDNConfig#num_buffers.
  GDNConfig.get_metadata: GDNConfig#get_metadata().
  GDNMode.BATCHED: GDNMode#BATCHED.
  GDNConfig.gate_lower_bound: GDNConfig#gate_lower_bound.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py)

## Classes
### <a id="AttentionMode"></a>`AttentionMode`  ·  implements/extends StrEnum
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py:31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L31)
- signature: `class AttentionMode(enum.StrEnum):`
- members:
  - <a id="AttentionMode.GDN"></a>`GDN` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L33)
  - <a id="AttentionMode.KDA"></a>`KDA` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L36)
- used by: [`is_kda`](config.md#GDNConfig.is_kda), [`attention_mode`](config.md#GDNConfig.attention_mode)

### <a id="Dtypes"></a>`Dtypes`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py:49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L49)
- signature: `class Dtypes:`
- members:
  - <a id="Dtypes.act_in"></a>`act_in` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L50)
  - <a id="Dtypes.act_out"></a>`act_out` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L51)
  - <a id="Dtypes.compute"></a>`compute` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L52) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="Dtypes.conv_state"></a>`conv_state` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L54)
  - <a id="Dtypes.recurrent_state"></a>`recurrent_state` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L53)
- used by: [`fused_qkvz_projection_pcp_gdn`](pcp_wrapper.md#fused_qkvz_projection_pcp_gdn), [`create_allocs`](memory_ref.md#create_allocs), [`inner_kernel`](kernel.md#inner_kernel), [`dtypes`](config.md#GDNConfig.dtypes), [`chunked_gdn_per_seq`](compute_gdn.md#chunked_gdn_per_seq), [`recurrent_gdn`](compute_gdn.md#recurrent_gdn), [`chunked_gdn`](compute_gdn.md#chunked_gdn), [`load_and_select_states`](vmem_ldst.md#load_and_select_states), [`recurrent_gdn_per_seq`](compute_gdn.md#recurrent_gdn_per_seq), [`conv_hbm_offset`](config.md#GDNConfig.conv_hbm_offset), [`get_out_shape`](config.md#GDNConfig.get_out_shape)

### <a id="GDNConfig"></a>`GDNConfig`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py:59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L59) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- signature: `class GDNConfig:`
- members:
  - <a id="GDNConfig.aligned_gate_dim"></a>`aligned_gate_dim(self)` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L135)
  - <a id="GDNConfig.aligned_num_v_heads"></a>`aligned_num_v_heads(self)` — [`L186`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L186)
  - <a id="GDNConfig.chunk_size"></a>`chunk_size(self)` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L106) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.conv_hbm_offset"></a>`conv_hbm_offset(self)` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L89) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.gate_dim"></a>`gate_dim(self)` — [`L128`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L128) — Width of the gate activation `a`, in elements per token.
  - <a id="GDNConfig.get_metadata"></a>`get_metadata(self)` — [`L191`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L191)
  - <a id="GDNConfig.get_out_shape"></a>`get_out_shape(self)` — [`L201`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L201) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.get_scratch_shape_dict"></a>`get_scratch_shape_dict(self)` — [`L207`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L207) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.is_kda"></a>`is_kda(self)` — [`L124`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L124)
  - <a id="GDNConfig.kq_dim_size"></a>`kq_dim_size(self)` — [`L178`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L178)
  - <a id="GDNConfig.prev_kernel_size"></a>`prev_kernel_size(self)` — [`L120`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L120) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.recurrent_hbm_offset"></a>`recurrent_hbm_offset(self)` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L102)
  - <a id="GDNConfig.seq_tile_size"></a>`seq_tile_size(self)` — [`L114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L114) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.triangular_block_size"></a>`triangular_block_size(self)` — [`L140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L140) — Sub-block size of the chunked KDA intra-chunk solve.
  - <a id="GDNConfig.use_recurrent"></a>`use_recurrent(self)` — [`L165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L165) — Whether GDN runs the token-recurrent scan instead of the chunked one. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.v_dim_size"></a>`v_dim_size(self)` — [`L174`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L174) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.v_per_kq_head"></a>`v_per_kq_head(self)` — [`L182`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L182)
  - <a id="GDNConfig.attention_mode"></a>`attention_mode` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L70)
  - <a id="GDNConfig.batch_size"></a>`batch_size` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L62)
  - <a id="GDNConfig.dim_size"></a>`dim_size` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L63)
  - <a id="GDNConfig.dtypes"></a>`dtypes` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L61) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.gate_lower_bound"></a>`gate_lower_bound` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L73)
  - <a id="GDNConfig.is_shared"></a>`is_shared` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L86)
  - <a id="GDNConfig.kernel_size"></a>`kernel_size` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L64)
  - <a id="GDNConfig.kq_head_dim"></a>`kq_head_dim` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L68) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.mode"></a>`mode` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L60)
  - <a id="GDNConfig.num_buffers"></a>`num_buffers` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L74)
  - <a id="GDNConfig.num_kq_heads"></a>`num_kq_heads` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L66) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.num_v_heads"></a>`num_v_heads` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L67) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.tile_size"></a>`tile_size` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L65) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.v_head_dim"></a>`v_head_dim` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L69) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
  - <a id="GDNConfig.window_size"></a>`window_size` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L84) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- uses (calls/refs, reference-scoped): [`GDNMode`](config.md#GDNMode), [`recurrent_state`](config.md#Dtypes.recurrent_state), [`PER_SEQ`](config.md#GDNMode.PER_SEQ), [`AttentionMode`](config.md#AttentionMode), [`Dtypes`](config.md#Dtypes), [`act_out`](config.md#Dtypes.act_out), [`GDN`](config.md#AttentionMode.GDN), [`KDA`](config.md#AttentionMode.KDA)
- used by: [`fused_qkvz_projection_pcp_gdn`](pcp_wrapper.md#fused_qkvz_projection_pcp_gdn), [`_compute_pcp_stage_metadata_from_coordinates`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates), [`create_allocs`](memory_ref.md#create_allocs), [`inner_kernel`](kernel.md#inner_kernel), [`_pcp_qkvz_projection_gdn_outer_kernel`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel), [`_compute_gdn_tile`](pcp_wrapper.md#_compute_gdn_tile), [`chunked_gdn_per_seq`](compute_gdn.md#chunked_gdn_per_seq), [`recurrent_gdn`](compute_gdn.md#recurrent_gdn), [`copy_out`](memory_ref.md#StateOutBufferedRef.copy_out), [`chunked_gdn`](compute_gdn.md#chunked_gdn), [`copy_in`](memory_ref.md#StateInBufferedRef.copy_in), [`load_and_select_states`](vmem_ldst.md#load_and_select_states), [`load_activation_as_large`](vmem_ldst.md#load_activation_as_large), [`causal_conv1d`](compute_conv1d.md#causal_conv1d), [`load_activation_as_compact`](vmem_ldst.md#load_activation_as_compact), [`recurrent_gdn_per_seq`](compute_gdn.md#recurrent_gdn_per_seq), [`wait_in`](memory_ref.md#StateInBufferedRef.wait_in), [`wait_out`](memory_ref.md#StateOutBufferedRef.wait_out), [`cfg`](memory_ref.md#BaseBufferedRef.cfg), [`_compute_gdn_tile_and_exchange_output`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output), [`copy_in`](memory_ref.md#InBufferedRef.copy_in), [`copy_out`](memory_ref.md#OutBufferedRef.copy_out), [`compute_pcp_stage_metadata`](pcp_metadata.md#compute_pcp_stage_metadata), [`wait_in`](memory_ref.md#InBufferedRef.wait_in), [`wait_out`](memory_ref.md#OutBufferedRef.wait_out), [`_schedule_capacities`](pcp_metadata.md#_schedule_capacities), [`create`](memory_ref.md#MetadataRef.create), [`_emit_rank_tiles`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates._emit_request._emit_window._emit_rank_tiles), [`_load`](pcp_wrapper.md#_compute_gdn_tile._load_qkv._load), [`create`](memory_ref.md#BaseBufferedRef.create), [`_emit_tile`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates._emit_request._emit_window._emit_rank_tiles._emit_tile)

### <a id="GDNMode"></a>`GDNMode`  ·  implements/extends StrEnum
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py:39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L39)
- signature: `class GDNMode(enum.StrEnum):`
- members:
  - <a id="GDNMode.BATCHED"></a>`BATCHED` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L43)
  - <a id="GDNMode.PER_SEQ"></a>`PER_SEQ` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/config.py#L44)
- used by: [`fused_qkvz_projection_pcp_gdn`](pcp_wrapper.md#fused_qkvz_projection_pcp_gdn), [`seq_tile_size`](config.md#GDNConfig.seq_tile_size), [`chunk_size`](config.md#GDNConfig.chunk_size), [`get_scratch_shape_dict`](config.md#GDNConfig.get_scratch_shape_dict), [`mode`](config.md#GDNConfig.mode)

