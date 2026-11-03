---
title: 'Module: src/vllm_torchtpu/env_override.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/env_override.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.env_override`/
symbols:
  _flag_name: _flag_name.
  _assembled: _assembled.
  _libtpu_extra_args._libtpu_extra_args: _libtpu_extra_args._libtpu_extra_args.
  _resolve_sc_offload_threshold_bytes: _resolve_sc_offload_threshold_bytes().
  set_libtpu_flag_default: set_libtpu_flag_default().
  _sc_offload_bytes: _sc_offload_bytes.
  logger: logger.
  _user_has_flag: _user_has_flag().
  _existing_libtpu_args: _existing_libtpu_args.
  _TPU_VMEM_BYTES_PER_TENSOR_CORE: _TPU_VMEM_BYTES_PER_TENSOR_CORE.
  _fetch_tpu_type_from_metadata: _fetch_tpu_type_from_metadata().
  experimental_libtpu_init_args: experimental_libtpu_init_args().
  _patch_jax_pallas_fori_lowering: _patch_jax_pallas_fori_lowering().
---
# Module: [`src/vllm_torchtpu/env_override.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py)

## Functions
- <a id="_fetch_tpu_type_from_metadata"></a>`_fetch_tpu_type_from_metadata()` — [`L109`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L109)
- <a id="_patch_jax_pallas_fori_lowering"></a>`_patch_jax_pallas_fori_lowering()` — [`L221`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L221) — Elide the dead remainder ``scf.for`` from Pallas ``fori_loop`` lowering.
- <a id="_resolve_sc_offload_threshold_bytes"></a>`_resolve_sc_offload_threshold_bytes()` — [`L130`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L130)
- <a id="_user_has_flag"></a>`_user_has_flag(flag_name: str, args_string: str | None = None)` — [`L152`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L152)
- <a id="experimental_libtpu_init_args"></a>`experimental_libtpu_init_args()` — [`L179`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L179) — The flags libtpu will read from ``LIBTPU_INIT_ARGS``, one per token.
- <a id="set_libtpu_flag_default"></a>`set_libtpu_flag_default(flag_name: str, value: str)` — [`L163`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L163) — Append ``<flag_name>=<value>`` to ``LIBTPU_INIT_ARGS`` unless already set. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)

## Module values
- <a id="_TPU_VMEM_BYTES_PER_TENSOR_CORE"></a>`_TPU_VMEM_BYTES_PER_TENSOR_CORE` — [`L95`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L95)
- <a id="_assembled"></a>`_assembled` — [`L215`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L215)
- <a id="_existing_libtpu_args"></a>`_existing_libtpu_args` — [`L149`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L149)
- <a id="_flag_name"></a>`_flag_name` — [`L207`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L207)
- <a id="_libtpu_extra_args._libtpu_extra_args"></a>`_libtpu_extra_args` — [`L191`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L191)
- <a id="_sc_offload_bytes"></a>`_sc_offload_bytes` — [`L205`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L205)
- <a id="logger"></a>`logger` — [`L22`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/env_override.py#L22)

