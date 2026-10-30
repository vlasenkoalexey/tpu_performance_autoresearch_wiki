---
title: 'Module: torchtitan/experiments/tpu/rl_nc_ray/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/rl_nc_ray/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.rl_nc_ray`/
symbols:
  monarch_actor: monarch_actor.
  monarch_rdma: monarch_rdma.
  RankObj.rank: RankObj#rank.
  monarch_spmd: monarch_spmd.
  monarch: monarch.
  real_file: real_file.
  DummyActor: DummyActor#
  dummy_endpoint: dummy_endpoint().
  dummy_setup_torch_elastic_env_async: dummy_setup_torch_elastic_env_async().
  DummyChannel: DummyChannel#
  RankObj: RankObj#
  logger: logger.
  DummyChannel.open: DummyChannel#open().
  RankObj.__init__: RankObj#__init__().
---
# Module: [`torchtitan/experiments/tpu/rl_nc_ray/__init__.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py)

## Classes
### <a id="DummyActor"></a>`DummyActor`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/__init__.py:40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L40)
- signature: `class DummyActor:`

### <a id="DummyChannel"></a>`DummyChannel`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/__init__.py:74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L74)
- signature: `class DummyChannel:`
- members:
  - <a id="DummyChannel.open"></a>`open()` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L76)
- used by: [`rank`](__init__.md#RankObj.rank)

### <a id="RankObj"></a>`RankObj`
- def: [`torchtitan/experiments/tpu/rl_nc_ray/__init__.py:79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L79)
- signature: `class RankObj:`
- members:
  - <a id="RankObj.rank"></a>`rank` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L82)
- protocol/private: <a id="RankObj.__init__"></a>`__init__`[`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L80)
- uses (calls/refs, reference-scoped): [`monarch_actor`](__init__.md#monarch_actor), [`monarch_rdma`](__init__.md#monarch_rdma), [`monarch_spmd`](__init__.md#monarch_spmd), [`DummyChannel`](__init__.md#DummyChannel), [`dummy_setup_torch_elastic_env_async`](__init__.md#dummy_setup_torch_elastic_env_async)

## Functions
- <a id="dummy_endpoint"></a>`dummy_endpoint(func)` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L64)
- <a id="dummy_setup_torch_elastic_env_async"></a>`dummy_setup_torch_elastic_env_async(*args, **kwargs)` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L67)

## Module values
- <a id="logger"></a>`logger` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L24)
- <a id="monarch"></a>`monarch` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L50)
- <a id="monarch_actor"></a>`monarch_actor` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L52)
- <a id="monarch_rdma"></a>`monarch_rdma` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L56)
- <a id="monarch_spmd"></a>`monarch_spmd` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L54)
- <a id="real_file"></a>`real_file` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/__init__.py#L48)

