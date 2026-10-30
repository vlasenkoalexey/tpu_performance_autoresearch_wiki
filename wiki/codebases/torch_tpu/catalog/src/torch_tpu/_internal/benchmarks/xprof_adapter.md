---
title: 'Module: src/torch_tpu/_internal/benchmarks/xprof_adapter.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/benchmarks/xprof_adapter.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.benchmarks.xprof_adapter`/
symbols:
  TraceMe: TraceMe#
  TraceMe.__init__: TraceMe#__init__().
  TraceMe.__enter__: TraceMe#__enter__().
  TraceMe.__exit__: TraceMe#__exit__().
  XprofSession: XprofSession#
  XprofSession.__init__: XprofSession#__init__().
  XprofSession.start_session: XprofSession#start_session().
  XprofSession.end_session_and_get_session_id: XprofSession#end_session_and_get_session_id().
  XprofSession.end_session_and_get_url: XprofSession#end_session_and_get_url().
  XprofSession.__enter__: XprofSession#__enter__().
  XprofSession.__exit__: XprofSession#__exit__().
  XprofAnalysisClient: XprofAnalysisClient#
  XprofAnalysisClient.__init__: XprofAnalysisClient#__init__().
  XprofAnalysisClient.get_profile_data: XprofAnalysisClient#get_profile_data().
  XprofAnalysisClient.upload: XprofAnalysisClient#upload().
  XprofAnalysisClient.__enter__: XprofAnalysisClient#__enter__().
  XprofAnalysisClient.__exit__: XprofAnalysisClient#__exit__().
---
# Module: [`src/torch_tpu/_internal/benchmarks/xprof_adapter.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py)

## Classes
### <a id="TraceMe"></a>`TraceMe`  ·  implements/extends AbstractContextManager
- def: [`src/torch_tpu/_internal/benchmarks/xprof_adapter.py:20`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L20)
- doc: A no-op context manager for TraceMe for OSS.
- signature: `class TraceMe(contextlib.AbstractContextManager):`
- protocol/private: <a id="TraceMe.__enter__"></a>`__enter__`[`L26`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L26), <a id="TraceMe.__exit__"></a>`__exit__`[`L29`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L29), <a id="TraceMe.__init__"></a>`__init__`[`L23`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L23)

### <a id="XprofAnalysisClient"></a>`XprofAnalysisClient`  ·  implements/extends AbstractContextManager
- def: [`src/torch_tpu/_internal/benchmarks/xprof_adapter.py:56`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L56)
- doc: A no-op context manager for XprofAnalysisClient for OSS.
- signature: `class XprofAnalysisClient(contextlib.AbstractContextManager):`
- members:
  - <a id="XprofAnalysisClient.get_profile_data"></a>`get_profile_data(self, *args, **kwargs)` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L62)
  - <a id="XprofAnalysisClient.upload"></a>`upload(self, *args, **kwargs)` — [`L65`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L65)
- protocol/private: <a id="XprofAnalysisClient.__enter__"></a>`__enter__`[`L68`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L68), <a id="XprofAnalysisClient.__exit__"></a>`__exit__`[`L71`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L71), <a id="XprofAnalysisClient.__init__"></a>`__init__`[`L59`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L59)

### <a id="XprofSession"></a>`XprofSession`  ·  implements/extends AbstractContextManager
- def: [`src/torch_tpu/_internal/benchmarks/xprof_adapter.py:33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L33)
- doc: A no-op context manager for XprofSession for OSS.
- signature: `class XprofSession(contextlib.AbstractContextManager):`
- members:
  - <a id="XprofSession.end_session_and_get_session_id"></a>`end_session_and_get_session_id(self)` — [`L42`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L42)
  - <a id="XprofSession.end_session_and_get_url"></a>`end_session_and_get_url(self)` — [`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L45)
  - <a id="XprofSession.start_session"></a>`start_session(self, *args, **kwargs)` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L39)
- protocol/private: <a id="XprofSession.__enter__"></a>`__enter__`[`L49`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L49), <a id="XprofSession.__exit__"></a>`__exit__`[`L52`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L52), <a id="XprofSession.__init__"></a>`__init__`[`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/benchmarks/xprof_adapter.py#L36)

