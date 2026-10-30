---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.tests.cp_pp_numerical`/
symbols:
  _run_case: _run_case().
  _compare: _compare().
  _torchrun: _torchrun().
  _TOL: _TOL.
  main: main().
  _run: _run().
  _COMMON: _COMMON.
  _load_by_cp_coord: _load_by_cp_coord().
  _MODULE: _MODULE.
  _CONFIG: _CONFIG.
  _BALANCER: _BALANCER.
  _rel: _rel().
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py)

## Functions
- <a id="_compare"></a>`_compare(ref_dir: str, cp_pp_dir: str)` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L91) — Every CP-only sample must match some CP+PP microbatch, per CP shard.
- <a id="_load_by_cp_coord"></a>`_load_by_cp_coord(dump_dir: str)` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L76)
- <a id="_rel"></a>`_rel(a: torch.Tensor, b: torch.Tensor)` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L87)
- <a id="_run"></a>`_run(cmd: str, env: dict | None = None)` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L53)
- <a id="_run_case"></a>`_run_case(work: str)` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L119)
- <a id="_torchrun"></a>`_torchrun(ngpu: int, config: str, extra: str)` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L69)
- <a id="main"></a>`main()` — [`L175`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L175)

## Module values
- <a id="_BALANCER"></a>`_BALANCER` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L49)
- <a id="_COMMON"></a>`_COMMON` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L41)
- <a id="_CONFIG"></a>`_CONFIG` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L48)
- <a id="_MODULE"></a>`_MODULE` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L38)
- <a id="_TOL"></a>`_TOL` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py#L50)

