---
title: 'Module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.gdn_pcp_fused.pcp_wrapper`/
symbols:
  fused_qkvz_projection_pcp_gdn: fused_qkvz_projection_pcp_gdn().
  _pcp_qkvz_projection_gdn_outer_kernel: _pcp_qkvz_projection_gdn_outer_kernel().
  _TPU_TILE_ROWS: _TPU_TILE_ROWS.
  _compute_gdn_tile: _compute_gdn_tile().
  _pcp_qkvz_projection_gdn_outer_kernel._run: _pcp_qkvz_projection_gdn_outer_kernel()._run().
  _TPU_TILE_COLUMNS: _TPU_TILE_COLUMNS.
  _pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output: _pcp_qkvz_projection_gdn_outer_kernel()._compute_gdn_tile_and_exchange_output().
  _pcp_qkvz_projection_gdn_outer_kernel._run_projection_catchup: _pcp_qkvz_projection_gdn_outer_kernel()._run_projection_catchup().
  _pcp_qkvz_projection_gdn_outer_kernel._start_output_stage: _pcp_qkvz_projection_gdn_outer_kernel()._start_output_stage().
  _pcp_qkvz_projection_gdn_outer_kernel._start_packed_qkv_copy: _pcp_qkvz_projection_gdn_outer_kernel()._start_packed_qkv_copy().
  _pcp_qkvz_projection_gdn_outer_kernel._wait_qkv_send: _pcp_qkvz_projection_gdn_outer_kernel()._wait_qkv_send().
  _pcp_qkvz_projection_gdn_outer_kernel._wait_qkv_recv: _pcp_qkvz_projection_gdn_outer_kernel()._wait_qkv_recv().
  _pcp_qkvz_projection_gdn_outer_kernel._run_projection_catchup._project_missing_tile: _pcp_qkvz_projection_gdn_outer_kernel()._run_projection_catchup()._project_missing_tile().
  _pcp_qkvz_projection_gdn_outer_kernel._run._finish_projection_tail: _pcp_qkvz_projection_gdn_outer_kernel()._run()._finish_projection_tail().
  _ProjectionConfig.token_block_size: _ProjectionConfig#token_block_size.
  _pcp_qkvz_projection_gdn_outer_kernel._wait_output_stage: _pcp_qkvz_projection_gdn_outer_kernel()._wait_output_stage().
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._finish_qkv: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile()._finish_qkv().
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._finish_z: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile()._finish_z().
  _pcp_qkvz_projection_gdn_outer_kernel._start_qkv_stage: _pcp_qkvz_projection_gdn_outer_kernel()._start_qkv_stage().
  _pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile: _pcp_qkvz_projection_gdn_outer_kernel()._start_projection_tile().
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile().
  _pcp_qkvz_projection_gdn_outer_kernel._project_first_token_block._project_out_block: _pcp_qkvz_projection_gdn_outer_kernel()._project_first_token_block()._project_out_block().
  _pcp_qkvz_projection_gdn_outer_kernel._stage_prologue: _pcp_qkvz_projection_gdn_outer_kernel()._stage_prologue().
  _qkv_receive_group_stride: _qkv_receive_group_stride().
  _all_rank_barrier: _all_rank_barrier().
  _pcp_qkvz_projection_gdn_outer_kernel._wait_projection_output: _pcp_qkvz_projection_gdn_outer_kernel()._wait_projection_output().
  _ProjectionConfig.out_block_size: _ProjectionConfig#out_block_size.
  _compute_gdn_tile._load_qkv._load: _compute_gdn_tile()._load_qkv()._load().
  _pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_qkv: _pcp_qkvz_projection_gdn_outer_kernel()._start_projection_tile()._start_qkv().
  _pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_z_group: _pcp_qkvz_projection_gdn_outer_kernel()._start_projection_tile()._start_z_group().
  _pcp_qkvz_projection_gdn_outer_kernel._stage_prologue._start_stage._prefetch_next_stage: _pcp_qkvz_projection_gdn_outer_kernel()._stage_prologue()._start_stage()._prefetch_next_stage().
  _pcp_qkvz_projection_gdn_outer_kernel._stage_prologue._start_stage._prefetch_next_stage._reuse_slot: _pcp_qkvz_projection_gdn_outer_kernel()._stage_prologue()._start_stage()._prefetch_next_stage()._reuse_slot().
  _pcp_qkvz_projection_gdn_outer_kernel._run._start_first_qkv_stage: _pcp_qkvz_projection_gdn_outer_kernel()._run()._start_first_qkv_stage().
  _pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_weight_piece: _pcp_qkvz_projection_gdn_outer_kernel()._start_projection_tile()._start_weight_piece().
  _pcp_qkvz_projection_gdn_outer_kernel._project_first_token_block: _pcp_qkvz_projection_gdn_outer_kernel()._project_first_token_block().
  _pcp_qkvz_projection_gdn_outer_kernel._start_state_pad_copies: _pcp_qkvz_projection_gdn_outer_kernel()._start_state_pad_copies().
  _pcp_qkvz_projection_gdn_outer_kernel._start_state_pad_copies._start: _pcp_qkvz_projection_gdn_outer_kernel()._start_state_pad_copies()._start().
  _pcp_qkvz_projection_gdn_outer_kernel._wait_state_pad_copies: _pcp_qkvz_projection_gdn_outer_kernel()._wait_state_pad_copies().
  _pcp_qkvz_projection_gdn_outer_kernel._wait_state_pad_copies._wait: _pcp_qkvz_projection_gdn_outer_kernel()._wait_state_pad_copies()._wait().
  _scatter_state_updates: _scatter_state_updates().
  _scatter_state_updates._apply_one: _scatter_state_updates()._apply_one().
  _mesh_device_id: _mesh_device_id().
  _pcp_qkvz_projection_gdn_outer_kernel._projection_job: _pcp_qkvz_projection_gdn_outer_kernel()._projection_job().
  _pcp_qkvz_projection_gdn_outer_kernel._projection_tile_for_work_id: _pcp_qkvz_projection_gdn_outer_kernel()._projection_tile_for_work_id().
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._wait_previous_projection_output: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile()._wait_previous_projection_output().
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._write_qkv_projection: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile()._write_qkv_projection().
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._wait_final_projection_output: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile()._wait_final_projection_output().
  _pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output._prefetch_projection_tile: _pcp_qkvz_projection_gdn_outer_kernel()._compute_gdn_tile_and_exchange_output()._prefetch_projection_tile().
  _pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output._reuse_output_stage_slot: _pcp_qkvz_projection_gdn_outer_kernel()._compute_gdn_tile_and_exchange_output()._reuse_output_stage_slot().
  _pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output._compute_projection_tile: _pcp_qkvz_projection_gdn_outer_kernel()._compute_gdn_tile_and_exchange_output()._compute_projection_tile().
  _pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output._finish_output_stage: _pcp_qkvz_projection_gdn_outer_kernel()._compute_gdn_tile_and_exchange_output()._finish_output_stage().
  _pcp_qkvz_projection_gdn_outer_kernel._stage_prologue._start_stage: _pcp_qkvz_projection_gdn_outer_kernel()._stage_prologue()._start_stage().
  _pcp_qkvz_projection_gdn_outer_kernel._run._project_first_live_token_block: _pcp_qkvz_projection_gdn_outer_kernel()._run()._project_first_live_token_block().
  _ProjectionConfig: _ProjectionConfig#
  _ProjectionConfig.qkv_dim: _ProjectionConfig#qkv_dim.
  _ProjectionConfig.full_key_dim: _ProjectionConfig#full_key_dim.
  _ProjectionConfig.kq_replication_factor: _ProjectionConfig#kq_replication_factor.
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._finish_matmul: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile()._finish_matmul().
  _pcp_qkvz_projection_gdn_outer_kernel._state_pad_copy: _pcp_qkvz_projection_gdn_outer_kernel()._state_pad_copy().
  _compute_gdn_tile._load_qkv: _compute_gdn_tile()._load_qkv().
  _scatter_state_updates._apply_one._write: _scatter_state_updates()._apply_one()._write().
  _pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_projection_x: _pcp_qkvz_projection_gdn_outer_kernel()._start_projection_tile()._start_projection_x().
  _pcp_qkvz_projection_gdn_outer_kernel._wait_projection_output._wait_qkv: _pcp_qkvz_projection_gdn_outer_kernel()._wait_projection_output()._wait_qkv().
  _pcp_qkvz_projection_gdn_outer_kernel._wait_projection_output._wait_z: _pcp_qkvz_projection_gdn_outer_kernel()._wait_projection_output()._wait_z().
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._prepare_projection_x: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile()._prepare_projection_x().
  _pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._write_z_projection: _pcp_qkvz_projection_gdn_outer_kernel()._finish_projection_tile()._write_z_projection().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py)

## Classes
### <a id="_ProjectionConfig"></a>`_ProjectionConfig`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py:64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L64)
- doc: Static geometry for the in-kernel QKVZ projection schedule.
- signature: `class _ProjectionConfig:`
- members:
  - <a id="_ProjectionConfig.full_key_dim"></a>`full_key_dim` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L70)
  - <a id="_ProjectionConfig.kq_replication_factor"></a>`kq_replication_factor` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L71)
  - <a id="_ProjectionConfig.out_block_size"></a>`out_block_size` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L68)
  - <a id="_ProjectionConfig.qkv_dim"></a>`qkv_dim` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L69)
  - <a id="_ProjectionConfig.token_block_size"></a>`token_block_size` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L67) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- used by: [`fused_qkvz_projection_pcp_gdn`](pcp_wrapper.md#fused_qkvz_projection_pcp_gdn), [`_pcp_qkvz_projection_gdn_outer_kernel`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel), [`_start_qkv`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_qkv), [`_start_z_group`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_z_group)

## Functions
- <a id="_all_rank_barrier"></a>`_all_rank_barrier(barrier_sem: jax.Ref, rank: jax.Array, pcp_size: int, *, mesh_axis_names: tuple[str, ...], pcp_axis_name: str)` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L121) — Barrier every PCP rank using a remotely addressable regular semaphore.
- <a id="_scatter_state_updates._apply_one"></a>`_apply_one(seq, pool)` — [`L1296`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1296)
- <a id="_compute_gdn_tile"></a>`_compute_gdn_tile(b_slot_ref: jax.Ref, a_slot_ref: jax.Ref, conv_state_in_slot_ref: jax.Ref, recurrent_in_slot_ref: jax.Ref, out_slot_ref: jax.Ref, conv_state_out_slot_ref: jax.Ref, recurrent_out_slot_ref: jax.Ref, metadata_ref: memory_ref.MetadataRef, stage_metadata_ref: pcp_metadata.PcpStageMetadata, weights_ref: memory_ref.WeightRefs, carry_conv_scratch_ref: jax.Ref | None, carry_recurrent_scratch_ref: jax.Ref | None, received_qkv_ref: jax.Array, compute_qkv_ref: jax.Ref, *, cfg: config.GDNConfig, comm_chunk_size: int)` — [`L145`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L145) — Convert one received BF16 tile and run the existing GDN inner kernel. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output"></a>`_compute_gdn_tile_and_exchange_output(b_slot_ref, a_slot_ref, conv_state_in_slot_ref, recurrent_in_slot_ref, out_slot_ref, conv_state_out_slot_ref, recurrent_out_slot_ref, metadata_ref, stage_metadata_ref, weights_ref, carry_conv_scratch_ref, carry_recurrent_scratch_ref, received_qkv_ref, compute_qkv_ref, output_stage_ref, packed_out_ref, output_send_sems, output_recv_sems)` — [`L966`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L966) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output._compute_projection_tile"></a>`_compute_projection_tile()` — [`L1050`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1050)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._finish_matmul"></a>`_finish_matmul(width: int)` — [`L683`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L683)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output._finish_output_stage"></a>`_finish_output_stage()` — [`L1083`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1083)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._run._finish_projection_tail"></a>`_finish_projection_tail(index, _)` — [`L1213`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1213)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile"></a>`_finish_projection_tile(token_block, out_block, *, wait_previous, wait_final)` — [`L644`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L644)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._finish_qkv"></a>`_finish_qkv()` — [`L744`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L744)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._finish_z"></a>`_finish_z()` — [`L754`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L754)
- <a id="_compute_gdn_tile._load_qkv._load"></a>`_load()` — [`L190`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L190)
- <a id="_compute_gdn_tile._load_qkv"></a>`_load_qkv(prefix: int)` — [`L188`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L188)
- <a id="_mesh_device_id"></a>`_mesh_device_id(mesh_axis_names: tuple[str, ...], pcp_axis_name: str, pcp_rank: int | jax.Array)` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L104) — Build the destination's full logical mesh coordinate.
- <a id="_pcp_qkvz_projection_gdn_outer_kernel"></a>`_pcp_qkvz_projection_gdn_outer_kernel(metadata_ref: memory_ref.MetadataRef, stage_metadata_ref: pcp_metadata.PcpStageMetadata, hidden_ref: jax.Array, projection_weight_ref: jax.Array, projection_weight_scale_ref: jax.Array | None, b_ref: jax.Array, a_ref: jax.Array, state_source_ref: jax.Array, state_pad_src_ref: jax.Array, zero_gdn_ref: jax.Array, packed_out_hbm_ref: jax.Array, weights_ref: memory_ref.WeightRefs, gdn_out_ref: jax.Array, packed_out_ref: jax.Array, state_updates_ref: jax.Array, projected_qkv_ref: jax.Array, z_ref: jax.Array, active_rows_out_ref: jax.Array, carry_conv_scratch_ref: jax.Array | None, carry_recurrent_scratch_ref: jax.Array | None, qkv_send_sems: jax.Array, qkv_recv_sems: jax.Array, output_send_sems: jax.Array, output_recv_sems: jax.Array, barrier_sems: jax.Ref, received_qkv_ref: jax.Array, compute_qkv_ref: jax.Array, output_stage_ref: jax.Array, projection_x_sem: jax.Array, projection_weight_sem: jax.Array, projection_scale_sem: jax.Array | None, projection_out_sem: jax.Array, projection_x_ref: jax.Array, projection_x_prepared_ref: jax.Array, projection_x_scale_ref: jax.Array | None, projection_weight_vmem_ref: jax.Array, projection_weight_scale_vmem_ref: jax.Array | None, projection_out_ref: jax.Array, projection_z_out_ref: jax.Array, projection_pending_out_ref: jax.Array, active_rows_smem_ref: jax.Array, active_rows_dma_sem: jax.Array, state_pad_sem: jax.Array, *, cfg: config.GDNConfig, pcp_size: int, comm_chunk_size: int, projection_cfg: _ProjectionConfig, mesh_axis_names: tuple[str, ...], pcp_axis_name: str, state_pad_start: int)` — [`L232`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L232) — Schedule QKVZ projection, QKV remote DMA, and per-sequence GDN. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._stage_prologue._start_stage._prefetch_next_stage"></a>`_prefetch_next_stage()` — [`L1119`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1119)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output._prefetch_projection_tile"></a>`_prefetch_projection_tile()` — [`L1011`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1011)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._prepare_projection_x"></a>`_prepare_projection_x()` — [`L656`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L656)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._run._project_first_live_token_block"></a>`_project_first_live_token_block()` — [`L1167`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1167)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._project_first_token_block"></a>`_project_first_token_block()` — [`L807`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L807)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._run_projection_catchup._project_missing_tile"></a>`_project_missing_tile(index, _)` — [`L941`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L941)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._project_first_token_block._project_out_block"></a>`_project_out_block(out_block, _)` — [`L808`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L808)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._projection_job"></a>`_projection_job(out_block)` — [`L428`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L428)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._projection_tile_for_work_id"></a>`_projection_tile_for_work_id(work_id)` — [`L916`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L916)
- <a id="_qkv_receive_group_stride"></a>`_qkv_receive_group_stride(comm_chunk_size: int, tile_size: int)` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L78) — Return the tile-group capacity reserved for one source rank.
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._compute_gdn_tile_and_exchange_output._reuse_output_stage_slot"></a>`_reuse_output_stage_slot()` — [`L1018`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1018)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._stage_prologue._start_stage._prefetch_next_stage._reuse_slot"></a>`_reuse_slot()` — [`L1127`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1127)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._run"></a>`_run(gdn_out_ref, packed_out_hbm_ref, output_send_sems, output_recv_sems, barrier_sems, allocations)` — [`L1151`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1151) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._run_projection_catchup"></a>`_run_projection_catchup(stage)` — [`L931`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L931)
- <a id="_scatter_state_updates"></a>`_scatter_state_updates(pool: jax.Array, state_updates: jax.Array, state_dst: jax.Array, num_seqs: jax.Array)` — [`L1282`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1282) — Write each compact update to the first slices of its pool block.
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._stage_prologue"></a>`_stage_prologue()` — [`L1108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1108)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_state_pad_copies._start"></a>`_start(seq, _)` — [`L878`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L878)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._run._start_first_qkv_stage"></a>`_start_first_qkv_stage()` — [`L1171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1171)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_output_stage"></a>`_start_output_stage(stage, output_stage_ref, packed_out_ref, output_send_sems, output_recv_sems)` — [`L314`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L314) — Send one row-contiguous output segment to each destination.
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_packed_qkv_copy"></a>`_start_packed_qkv_copy(stage, slot, destination: int)` — [`L434`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L434)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile"></a>`_start_projection_tile(token_block, out_block)` — [`L558`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L558)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_projection_x"></a>`_start_projection_x()` — [`L563`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L563)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_qkv"></a>`_start_qkv()` — [`L604`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L604)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_qkv_stage"></a>`_start_qkv_stage(stage)` — [`L495`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L495)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._stage_prologue._start_stage"></a>`_start_stage()` — [`L1114`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1114)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_state_pad_copies"></a>`_start_state_pad_copies()` — [`L874`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L874)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_weight_piece"></a>`_start_weight_piece(source_row, destination_row: int, width: int)` — [`L573`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L573)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._start_projection_tile._start_z_group"></a>`_start_z_group()` — [`L618`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L618)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._state_pad_copy"></a>`_state_pad_copy(seq)` — [`L855`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L855) — HBM-to-HBM copy of one sequence's non-state granules.
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._wait_state_pad_copies._wait"></a>`_wait(seq, _)` — [`L887`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L887)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._wait_final_projection_output"></a>`_wait_final_projection_output()` — [`L804`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L804)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._wait_output_stage"></a>`_wait_output_stage(stage, active_stages, output_stage_ref, packed_out_ref, output_send_sems, output_recv_sems)` — [`L370`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L370)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._wait_previous_projection_output"></a>`_wait_previous_projection_output()` — [`L652`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L652)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._wait_projection_output"></a>`_wait_projection_output()` — [`L622`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L622)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._wait_projection_output._wait_qkv"></a>`_wait_qkv()` — [`L627`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L627)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._wait_qkv_recv"></a>`_wait_qkv_recv(stage)` — [`L503`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L503)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._wait_qkv_send"></a>`_wait_qkv_send(stage, active_stages)` — [`L528`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L528) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._wait_state_pad_copies"></a>`_wait_state_pad_copies()` — [`L883`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L883)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._wait_projection_output._wait_z"></a>`_wait_z()` — [`L635`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L635)
- <a id="_scatter_state_updates._apply_one._write"></a>`_write(pool)` — [`L1299`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1299)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._write_qkv_projection"></a>`_write_qkv_projection()` — [`L773`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L773)
- <a id="_pcp_qkvz_projection_gdn_outer_kernel._finish_projection_tile._write_z_projection"></a>`_write_z_projection()` — [`L789`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L789)
- <a id="fused_qkvz_projection_pcp_gdn"></a>`fused_qkvz_projection_pcp_gdn(hidden_states: jax.Array, qkvz_weight: jax.Array, qkvz_weight_scale: jax.Array | None, b: jax.Array, a: jax.Array, state_source: jax.Array, conv_weight: jax.Array, conv_bias: jax.Array | None, a_log: jax.Array, dt_bias: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, distribution: jax.Array, seq_lens: jax.Array, *, n_kq: int, n_v: int, d_k: int, d_v: int, kernel_size: int, pcp_size: int, comm_chunk_size: int, mesh_axis_names: tuple[str, ...], pcp_axis_name: str, recurrent_state_dtype: jnp.dtype = jnp.float32.dtype, mixed_tile_size: int = 64, compute_precision: jnp.dtype = jnp.float32.dtype)` — [`L1328`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L1328) — Run ragged PCP prefill with fused QKVZ projection and communication. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)

## Module values
- <a id="_TPU_TILE_COLUMNS"></a>`_TPU_TILE_COLUMNS` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L75) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_TPU_TILE_ROWS"></a>`_TPU_TILE_ROWS` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_wrapper.py#L74) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)

