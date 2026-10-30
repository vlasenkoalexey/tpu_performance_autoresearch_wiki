---
title: 'Module: src/torch_tpu/_internal/distributed/multiprocessing.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/multiprocessing.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.multiprocessing`/
symbols:
  init_spawn: init_spawn().
  parse_absl_flags: parse_absl_flags().
  handle_main: handle_main().
  handle_test_main: handle_test_main().
  get_context: get_context().
---
# Module: [`src/torch_tpu/_internal/distributed/multiprocessing.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/multiprocessing.py)

## Functions
- <a id="get_context"></a>`get_context(method=None)` — [`L40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/multiprocessing.py#L40) — Returns a multiprocessing context.
- <a id="handle_main"></a>`handle_main(main, *args, **kwargs)` — [`L25`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/multiprocessing.py#L25) — Handles main entrypoint for multiprocessing applications in OSS.
- <a id="handle_test_main"></a>`handle_test_main(main, *args, **kwargs)` — [`L30`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/multiprocessing.py#L30) — Handles test main entrypoint for multiprocessing tests in OSS.
- <a id="init_spawn"></a>`init_spawn()` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/multiprocessing.py#L35) — Initializes multiprocessing spawn support in OSS.
- <a id="parse_absl_flags"></a>`parse_absl_flags()` — [`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/multiprocessing.py#L45) — Parses absl flags in spawned worker subprocesses if not already parsed.

