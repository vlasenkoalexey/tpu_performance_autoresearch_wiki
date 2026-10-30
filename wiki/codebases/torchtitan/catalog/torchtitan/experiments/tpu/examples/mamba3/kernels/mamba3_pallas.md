---
title: 'Module: torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.mamba3.kernels.mamba3_pallas`/
symbols:
  _fwd_mimo_jax: _fwd_mimo_jax().
  ssd3_chunk_scan_pallas: ssd3_chunk_scan_pallas().
  exc: exc.
  _bwd_mimo_jax.surrogate: _bwd_mimo_jax().surrogate().
  _fwd_jax: _fwd_jax().
  _ssd3_core: _ssd3_core().
  _pallas_ssd3_fwd: _pallas_ssd3_fwd.
  _naive_ssd3_plain_jax: _naive_ssd3_plain_jax().
  _naive_ssd3_mimo_plain_jax: _naive_ssd3_mimo_plain_jax().
  _execute_tpu_siso_scan: _execute_tpu_siso_scan().
  _pallas_ssd3_mimo_fwd: _pallas_ssd3_mimo_fwd.
  _pallas_mamba3_scan: _pallas_mamba3_scan().
  _angle_cumsum: _angle_cumsum().
  _rope_trap_preprocess: _rope_trap_preprocess().
  _rope_trap_preprocess_mimo: _rope_trap_preprocess_mimo().
  _pallas_ssd3_bwd: _pallas_ssd3_bwd.
  _pallas_ssd3_mimo_bwd: _pallas_ssd3_mimo_bwd.
  _DummyPallasModule.jax_op: _DummyPallasModule#jax_op().
  _inter_chunk_plain: _inter_chunk_plain().
  _CHUNK_SIZE: _CHUNK_SIZE.
  _cumsum_via_matmul: _cumsum_via_matmul().
  _intra_chunk_one_plain: _intra_chunk_one_plain().
  _bwd_jax.surrogate: _bwd_jax().surrogate().
  _fuse_tr: _fuse_tr().
  _make_intra_kernel_mimo._kernel: _make_intra_kernel_mimo()._kernel().
  _intra_chunk_one_plain_mimo: _intra_chunk_one_plain_mimo().
  _execute_tpu_mimo_scan: _execute_tpu_mimo_scan().
  _intra_chunk_plain: _intra_chunk_plain().
  _segsum_strict_fused: _segsum_strict_fused().
  _intra_chunk_plain_mimo: _intra_chunk_plain_mimo().
  _execute_cpu_siso_scan: _execute_cpu_siso_scan().
  _chunkify: _chunkify().
  _segsum_strict: _segsum_strict().
  _segsum_safe: _segsum_safe().
  _make_inter_kernel: _make_inter_kernel().
  _make_intra_kernel_mimo: _make_intra_kernel_mimo().
  _fwd_mimo_jax.intra_fn: _fwd_mimo_jax().intra_fn().
  _naive_ssd3_mimo_plain_jax.intra_fn: _naive_ssd3_mimo_plain_jax().intra_fn().
  _bwd_mimo_jax: _bwd_mimo_jax().
  _mamba3_bwd_surrogate: _mamba3_bwd_surrogate().
  _mamba3_bwd_surrogate.surrogate: _mamba3_bwd_surrogate().surrogate().
  _backward_impl: _backward_impl().
  _mimo_backward_impl: _mimo_backward_impl().
  _execute_cpu_mimo_scan: _execute_cpu_mimo_scan().
  _DummyJaxOp.__call__: _DummyJaxOp#__call__().
  _inter_chunk_pallas: _inter_chunk_pallas().
  _bwd_jax: _bwd_jax().
  _intra_chunk_pallas_mimo: _intra_chunk_pallas_mimo().
  _logger: _logger.
  _mamba3_fused_chunk_kernel: _mamba3_fused_chunk_kernel().
  _rope_trap_preprocess._rotate: _rope_trap_preprocess()._rotate().
  _rotate_split_half: _rotate_split_half().
  _unfuse_tr: _unfuse_tr().
  _fuse_adt_mimo: _fuse_adt_mimo().
  _execute_tpu_siso_scan._rotate: _execute_tpu_siso_scan()._rotate().
  _execute_cpu_siso_scan._rotate: _execute_cpu_siso_scan()._rotate().
  _execute_cpu_mimo_scan._rotate_split: _execute_cpu_mimo_scan()._rotate_split().
  _TORCH_TPU_PALLAS_AVAILABLE: _TORCH_TPU_PALLAS_AVAILABLE.
  _DummyJaxOp: _DummyJaxOp#
  _DummyJaxOp.name: _DummyJaxOp#name.
  _DummyPallasModule: _DummyPallasModule#
  _make_inter_kernel._kernel: _make_inter_kernel()._kernel().
  _angle_cumsum._mod_add: _angle_cumsum()._mod_add().
  _inter_chunk_one_plain: _inter_chunk_one_plain().
  _setup_context: _setup_context().
  _mimo_setup_context: _mimo_setup_context().
  _DummyJaxOp.__init__: _DummyJaxOp#__init__().
  _DummyJaxOp.fn: _DummyJaxOp#fn.
  _DummyJaxOp.register_autograd: _DummyJaxOp#register_autograd().
  _mamba3_fused_chunk_kernel._init: _mamba3_fused_chunk_kernel()._init().
---
# Module: [`torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py)

## Classes
### <a id="_DummyJaxOp"></a>`_DummyJaxOp`
- def: [`torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py:37`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L37)
- doc: Fallback placeholder for JAX op wrapper when torch_tpu is unavailable.
- signature: `class _DummyJaxOp:`
- members:
  - <a id="_DummyJaxOp.register_autograd"></a>`register_autograd(self, backward_impl: Any, setup_context: Any = None)` — [`L50`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L50)
  - <a id="_DummyJaxOp.fn"></a>`fn` — [`L42`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L42)
  - <a id="_DummyJaxOp.name"></a>`name` — [`L41`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L41)
- protocol/private: <a id="_DummyJaxOp.__call__"></a>`__call__`[`L44`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L44), <a id="_DummyJaxOp.__init__"></a>`__init__`[`L40`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L40)
- used by: (1 test-only callers)

### <a id="_DummyPallasModule"></a>`_DummyPallasModule`
- def: [`torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py:55`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L55)
- doc: Fallback placeholder module for torch_tpu._internal.pallas.
- signature: `class _DummyPallasModule:`
- members:
  - <a id="_DummyPallasModule.jax_op"></a>`jax_op(name: str, fn: Any)` — [`L59`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L59)
- uses (calls/refs, reference-scoped): (1 test-only callers)
- used by: (4 test-only callers)

## Functions
- <a id="_angle_cumsum"></a>`_angle_cumsum(angle_raw: jax.Array, dt: jax.Array)` — [`L343`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L343) — Computes associative prefix sum of continuous rotary angles modulo 2*pi.
- <a id="_backward_impl"></a>`_backward_impl(ctx: Any, grad_out: torch.Tensor)` — [`L954`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L954) — Computes SISO backward gradients via registered Pallas JAX op.
- <a id="_bwd_jax"></a>`_bwd_jax(x: jax.Array, q_raw: jax.Array, k_raw: jax.Array, q_bias: jax.Array, k_bias: jax.Array, adt: jax.Array, dt: jax.Array, trap_raw: jax.Array, angle_raw: jax.Array, dy: jax.Array, d_qk_dot_gamma: jax.Array)` — [`L512`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L512) — Computes VJP backward gradients for all inputs of the SISO scan in JAX.
- <a id="_bwd_mimo_jax"></a>`_bwd_mimo_jax(v: jax.Array, q_raw: jax.Array, k_raw: jax.Array, q_bias: jax.Array, k_bias: jax.Array, adt: jax.Array, dt: jax.Array, trap_raw: jax.Array, angle_raw: jax.Array, psi: jax.Array, initial_state: jax.Array, dy_full: jax.Array, d_final_state: jax.Array)` — [`L842`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L842) — Computes VJP backward gradients for all inputs of the MIMO scan in JAX.
- <a id="_chunkify"></a>`_chunkify(x: jax.Array, b: int, nt: int, bl: int)` — [`L292`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L292) — Reshapes and permutes a sequence tensor into chunked representation.
- <a id="_cumsum_via_matmul"></a>`_cumsum_via_matmul(x: jax.Array, axis_len: int)` — [`L66`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L66) — Cumsum along axis 0 via lower-triangular matmul for Pallas TPU.
- <a id="_execute_cpu_mimo_scan"></a>`_execute_cpu_mimo_scan(v: torch.Tensor, b: torch.Tensor, c: torch.Tensor, b_bias: torch.Tensor, c_bias: torch.Tensor, adt: torch.Tensor, dt: torch.Tensor, trap_raw: torch.Tensor, angle_raw: torch.Tensor, d: Optional[torch.Tensor], psi: torch.Tensor, phi: torch.Tensor, zeta: torch.Tensor, z: torch.Tensor)` — [`L1366`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1366) — Vectorized PyTorch CPU execution fallback for MIMO multi-channel Mamba-3 scan.
- <a id="_execute_cpu_siso_scan"></a>`_execute_cpu_siso_scan(v: torch.Tensor, b: torch.Tensor, c: torch.Tensor, b_bias: torch.Tensor, c_bias: torch.Tensor, adt: torch.Tensor, dt: torch.Tensor, trap_raw: torch.Tensor, angle_raw: torch.Tensor, d: Optional[torch.Tensor])` — [`L1217`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1217) — Vectorized PyTorch CPU execution fallback for SISO Mamba-3 scan.
- <a id="_execute_tpu_mimo_scan"></a>`_execute_tpu_mimo_scan(v: torch.Tensor, b: torch.Tensor, c: torch.Tensor, b_bias: torch.Tensor, c_bias: torch.Tensor, adt: torch.Tensor, dt: torch.Tensor, trap_raw: torch.Tensor, angle_raw: torch.Tensor, d: Optional[torch.Tensor], chunk_size: int, psi: torch.Tensor, phi: torch.Tensor, zeta: torch.Tensor, z: torch.Tensor)` — [`L1288`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1288) — Executes the fused Pallas TPU scan for MIMO multi-channel configuration.
- <a id="_execute_tpu_siso_scan"></a>`_execute_tpu_siso_scan(v: torch.Tensor, b: torch.Tensor, c: torch.Tensor, b_bias: torch.Tensor, c_bias: torch.Tensor, adt: torch.Tensor, dt: torch.Tensor, trap_raw: torch.Tensor, angle_raw: torch.Tensor, d: Optional[torch.Tensor], chunk_size: int)` — [`L1116`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1116) — Executes the fused Pallas TPU scan for SISO configuration with head grouping.
- <a id="_fuse_adt_mimo"></a>`_fuse_adt_mimo(adt: jax.Array, r: int)` — [`L621`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L621) — Expands and fuses scalar continuous decay across rank dimensions.
- <a id="_fuse_tr"></a>`_fuse_tr(x: jax.Array)` — [`L604`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L604) — Fuses token and channel rank dimensions for MIMO processing.
- <a id="_fwd_jax"></a>`_fwd_jax(x: jax.Array, q_raw: jax.Array, k_raw: jax.Array, q_bias: jax.Array, k_bias: jax.Array, adt: jax.Array, dt: jax.Array, trap_raw: jax.Array, angle_raw: jax.Array)` — [`L403`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L403) — Direct JAX forward pass evaluating RoPE preprocessing and chunked SSD scan.
- <a id="_fwd_mimo_jax"></a>`_fwd_mimo_jax(v: jax.Array, q_raw: jax.Array, k_raw: jax.Array, q_bias: jax.Array, k_bias: jax.Array, adt: jax.Array, dt: jax.Array, trap_raw: jax.Array, angle_raw: jax.Array, psi: jax.Array, initial_state: jax.Array)` — [`L747`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L747) — Forward pass for MIMO multi-channel Mamba-3 scan in JAX.
- <a id="_mamba3_fused_chunk_kernel._init"></a>`_init()` — [`L117`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L117)
- <a id="_inter_chunk_one_plain"></a>`_inter_chunk_one_plain(c_i: jax.Array, state_in: jax.Array, a_cumsum_i: jax.Array)` — [`L470`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L470) — Vectorized reference for single-chunk inter-chunk state projection.
- <a id="_inter_chunk_pallas"></a>`_inter_chunk_pallas(c_c: jax.Array, states_in: jax.Array, a_cumsum_c: jax.Array)` — [`L268`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L268) — Applies inter-chunk recurrent state projection via Pallas TPU kernel.
- <a id="_inter_chunk_plain"></a>`_inter_chunk_plain(c_c: jax.Array, states_in: jax.Array, a_cumsum_c: jax.Array)` — [`L484`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L484) — Batch-vectorized inter-chunk state projection across all chunks and heads.
- <a id="_intra_chunk_one_plain"></a>`_intra_chunk_one_plain(x_i: jax.Array, a_i: jax.Array, b_i: jax.Array, c_i: jax.Array)` — [`L436`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L436) — Vectorized reference for single-chunk intra-chunk attention and state extraction.
- <a id="_intra_chunk_one_plain_mimo"></a>`_intra_chunk_one_plain_mimo(x_i: jax.Array, a_i: jax.Array, b_i: jax.Array, c_i: jax.Array, r: int)` — [`L788`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L788) — Performs intra-chunk attention for a single chunk of MIMO multi-channel inputs.
- <a id="_intra_chunk_pallas_mimo"></a>`_intra_chunk_pallas_mimo(x_c: jax.Array, a_c: jax.Array, b_c: jax.Array, c_c: jax.Array, r: int)` — [`L719`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L719) — Executes fused intra-chunk MIMO attention via Pallas TPU kernel.
- <a id="_intra_chunk_plain"></a>`_intra_chunk_plain(x_c: jax.Array, a_c: jax.Array, b_c: jax.Array, c_c: jax.Array)` — [`L461`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L461) — Batch-vectorized intra-chunk attention across all chunks and heads.
- <a id="_intra_chunk_plain_mimo"></a>`_intra_chunk_plain_mimo(x_c: jax.Array, a_c: jax.Array, b_c: jax.Array, c_c: jax.Array, r: int)` — [`L813`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L813) — Batch-vectorized intra-chunk attention across all chunks and heads for MIMO.
- <a id="_make_inter_kernel._kernel"></a>`_kernel(c_ref: Any, state_ref: Any, acum_ref: Any, yoff_ref: Any)` — [`L248`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L248)
- <a id="_make_intra_kernel_mimo._kernel"></a>`_kernel(x_ref: Any, a_ref: Any, b_ref: Any, c_ref: Any, ydiag_ref: Any, state_ref: Any, acum_ref: Any)` — [`L675`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L675)
- <a id="_make_inter_kernel"></a>`_make_inter_kernel(bl: int)` — [`L244`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L244) — Creates a Pallas TPU kernel for inter-chunk recurrent state projection.
- <a id="_make_intra_kernel_mimo"></a>`_make_intra_kernel_mimo(bl: int, r: int)` — [`L672`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L672) — Constructs a Pallas TPU kernel for intra-chunk MIMO multi-channel attention.
- <a id="_mamba3_bwd_surrogate"></a>`_mamba3_bwd_surrogate(x: jax.Array, adt: jax.Array, k_scaled: jax.Array, q_rot: jax.Array, dy: jax.Array)` — [`L921`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L921) — VJP backward surrogate computing exact gradients with respect to SSD inputs.
- <a id="_mamba3_fused_chunk_kernel"></a>`_mamba3_fused_chunk_kernel(x_ref: Any, adt_ref: Any, b_ref: Any, c_ref: Any, y_ref: Any, s_ref: Any)` — [`L105`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L105) — Fused intra-chunk attention and inter-chunk recurrent state update Pallas TPU kernel.
- <a id="_mimo_backward_impl"></a>`_mimo_backward_impl(ctx: Any, grad_y_full: torch.Tensor, grad_final_state: torch.Tensor)` — [`L1002`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1002) — Computes MIMO backward gradients via registered Pallas JAX op.
- <a id="_mimo_setup_context"></a>`_mimo_setup_context(ctx: Any, inputs: Any, output: Any)` — [`L972`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L972) — Saves forward tensors in autograd context for MIMO backward pass.
- <a id="_angle_cumsum._mod_add"></a>`_mod_add(x: jax.Array, y: jax.Array)` — [`L353`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L353)
- <a id="_naive_ssd3_mimo_plain_jax"></a>`_naive_ssd3_mimo_plain_jax(x: jax.Array, a: jax.Array, k_scaled: jax.Array, q_rot: jax.Array, initial_state: jax.Array, r: int)` — [`L823`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L823) — Reference execution of MIMO SSD-3 scan in plain JAX.
- <a id="_naive_ssd3_plain_jax"></a>`_naive_ssd3_plain_jax(x: jax.Array, a: jax.Array, k_scaled: jax.Array, q_rot: jax.Array, initial_state: jax.Array)` — [`L493`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L493) — Plain JAX reference implementation of SSD-3 scan for CPU and autograd surrogates.
- <a id="_pallas_mamba3_scan"></a>`_pallas_mamba3_scan(x: jax.Array, adt: jax.Array, k_scaled: jax.Array, q_rot: jax.Array)` — [`L175`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L175) — Executes the fused Pallas TPU scan with head group tiling for TPU v7x VMEM limits.
- <a id="_rope_trap_preprocess"></a>`_rope_trap_preprocess(q_raw: jax.Array, k_raw: jax.Array, q_bias: jax.Array, k_bias: jax.Array, angle_raw: jax.Array, dt: jax.Array, trap_raw: jax.Array)` — [`L363`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L363) — Preprocesses queries and keys with 2D continuous RoPE and trapezoidal scaling.
- <a id="_rope_trap_preprocess_mimo"></a>`_rope_trap_preprocess_mimo(v_raw: jax.Array, q_raw: jax.Array, k_raw: jax.Array, q_bias: jax.Array, k_bias: jax.Array, angle_raw: jax.Array, dt_bht: jax.Array, trap_raw_bht: jax.Array, psi: jax.Array)` — [`L629`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L629) — Preprocesses multi-channel inputs with MIMO RoPE and cross-channel attention.
- <a id="_rope_trap_preprocess._rotate"></a>`_rotate(x: jax.Array)` — [`L390`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L390)
- <a id="_execute_tpu_siso_scan._rotate"></a>`_rotate(t_in: torch.Tensor)` — [`L1172`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1172)
- <a id="_execute_cpu_siso_scan._rotate"></a>`_rotate(inp)` — [`L1250`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1250)
- <a id="_execute_cpu_mimo_scan._rotate_split"></a>`_rotate_split(inp)` — [`L1410`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1410)
- <a id="_rotate_split_half"></a>`_rotate_split_half(x: jax.Array, cos: jax.Array, sin: jax.Array, num_rope_angles: int)` — [`L571`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L571) — Rotates the RoPE-designated slice of features while preserving remaining channels.
- <a id="_segsum_safe"></a>`_segsum_safe(x: jax.Array)` — [`L92`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L92) — Cross-chunk inclusive decay mask (s <= l).
- <a id="_segsum_strict"></a>`_segsum_strict(x: jax.Array)` — [`L80`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L80) — Intra-chunk strict causal decay mask (s < l only).
- <a id="_segsum_strict_fused"></a>`_segsum_strict_fused(x: jax.Array, r: int)` — [`L585`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L585) — Computes strict causal decay mask for MIMO multi-channel tokens.
- <a id="_setup_context"></a>`_setup_context(ctx: Any, inputs: Any, output: Any)` — [`L948`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L948) — Saves forward tensors in autograd context for SISO backward pass.
- <a id="_ssd3_core"></a>`_ssd3_core(x: jax.Array, a: jax.Array, k_scaled: jax.Array, q_rot: jax.Array, intra_fn: Any, inter_fn: Any, s0: jax.Array)` — [`L300`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L300) — Core State Space Duality (SSD-3) chunked execution algorithm.
- <a id="_unfuse_tr"></a>`_unfuse_tr(x: jax.Array, r: int)` — [`L612`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L612) — Unfuses token and channel rank dimensions back to separate axes.
- <a id="_fwd_mimo_jax.intra_fn"></a>`intra_fn(x_c: jax.Array, a_c: jax.Array, b_c: jax.Array, c_c: jax.Array)` — [`L770`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L770)
- <a id="_naive_ssd3_mimo_plain_jax.intra_fn"></a>`intra_fn(x_c: jax.Array, a_c: jax.Array, b_c: jax.Array, c_c: jax.Array)` — [`L832`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L832)
- <a id="ssd3_chunk_scan_pallas"></a>`ssd3_chunk_scan_pallas(v: torch.Tensor, b: torch.Tensor, c: torch.Tensor, b_bias: torch.Tensor, c_bias: torch.Tensor, adt: torch.Tensor, dt: torch.Tensor, trap_raw: torch.Tensor, angle_raw: torch.Tensor, d: Optional[torch.Tensor] = None, chunk_size: int = _CHUNK_SIZE, psi: Optional[torch.Tensor] = None, phi: Optional[torch.Tensor] = None, zeta: Optional[torch.Tensor] = None, z: Optional[torch.Tensor] = None, is_mimo: bool = False)` — [`L1060`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1060) — Executes the fused Pallas TPU SSD-3 scan with PyTorch tensor interface.
- <a id="_bwd_jax.surrogate"></a>`surrogate(x_, q_raw_, k_raw_, q_bias_, k_bias_, adt_, dt_, trap_raw_, angle_raw_)` — [`L540`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L540)
- <a id="_bwd_mimo_jax.surrogate"></a>`surrogate(v_, q_raw_, k_raw_, q_bias_, k_bias_, adt_, dt_, trap_raw_, angle_raw_, psi_, s0_)` — [`L872`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L872)
- <a id="_mamba3_bwd_surrogate.surrogate"></a>`surrogate(x_, adt_, k_, q_)` — [`L933`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L933)

## Module values
- <a id="_CHUNK_SIZE"></a>`_CHUNK_SIZE` — [`L30`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L30)
- <a id="_TORCH_TPU_PALLAS_AVAILABLE"></a>`_TORCH_TPU_PALLAS_AVAILABLE` — [`L34`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L34)
- <a id="_logger"></a>`_logger` — [`L28`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L28)
- <a id="_pallas_ssd3_bwd"></a>`_pallas_ssd3_bwd` — [`L944`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L944)
- <a id="_pallas_ssd3_fwd"></a>`_pallas_ssd3_fwd` — [`L941`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L941)
- <a id="_pallas_ssd3_mimo_bwd"></a>`_pallas_ssd3_mimo_bwd` — [`L968`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L968)
- <a id="_pallas_ssd3_mimo_fwd"></a>`_pallas_ssd3_mimo_fwd` — [`L965`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L965)
- <a id="exc"></a>`exc` — [`L1050`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py#L1050)

