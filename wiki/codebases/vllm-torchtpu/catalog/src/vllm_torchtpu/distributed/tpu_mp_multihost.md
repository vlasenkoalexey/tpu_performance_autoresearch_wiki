---
title: 'Module: src/vllm_torchtpu/distributed/tpu_mp_multihost.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/tpu_mp_multihost.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.tpu_mp_multihost`/
symbols:
  prepare_mp_multihost_env: prepare_mp_multihost_env().
  prepare_mp_multihost_dp_env: prepare_mp_multihost_dp_env().
  _rendezvous_host_ips: _rendezvous_host_ips().
  logger: logger.
  _rendezvous_port: _rendezvous_port().
  _DONE_SENTINEL: _DONE_SENTINEL.
  _DP_DONE_SENTINEL: _DP_DONE_SENTINEL.
  _RENDEZVOUS_TIMEOUT_S: _RENDEZVOUS_TIMEOUT_S.
  _keepalive_stores._keepalive_stores: _keepalive_stores._keepalive_stores.
---
# Module: [`src/vllm_torchtpu/distributed/tpu_mp_multihost.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py)

## Functions
- <a id="_rendezvous_host_ips"></a>`_rendezvous_host_ips(*, num_peers: int, peer_index: int, master_addr: str, port: int, key_prefix: str)` — [`L97`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L97) — Exchange every peer's IP (and a shared xprof session id) via TCPStore.
- <a id="_rendezvous_port"></a>`_rendezvous_port(base_port: int)` — [`L88`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L88)
- <a id="prepare_mp_multihost_dp_env"></a>`prepare_mp_multihost_dp_env(parallel_config, total_chips: int)` — [`L203`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L203) — Set TORCH_TPU_* env vars for genuine multi-host DP without Ray. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="prepare_mp_multihost_env"></a>`prepare_mp_multihost_env(parallel_config)` — [`L128`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L128) — Set TORCH_TPU_* env vars for a genuine multi-host `mp` backend run. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)

## Module values
- <a id="_DONE_SENTINEL"></a>`_DONE_SENTINEL` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L76)
- <a id="_DP_DONE_SENTINEL"></a>`_DP_DONE_SENTINEL` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L77)
- <a id="_RENDEZVOUS_TIMEOUT_S"></a>`_RENDEZVOUS_TIMEOUT_S` — [`L78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L78)
- <a id="_keepalive_stores._keepalive_stores"></a>`_keepalive_stores` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L85)
- <a id="logger"></a>`logger` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/tpu_mp_multihost.py#L74)

