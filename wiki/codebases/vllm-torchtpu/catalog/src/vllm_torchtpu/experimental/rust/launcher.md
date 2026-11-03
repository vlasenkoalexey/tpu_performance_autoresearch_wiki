---
title: 'Module: src/vllm_torchtpu/experimental/rust/launcher.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/rust/launcher.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.rust.launcher`/
symbols:
  split_args: split_args().
  artifact_for: artifact_for().
  main: main().
  LauncherError: LauncherError#
  resolve_binary: resolve_binary().
  SplitArgs.model: SplitArgs#model.
  _log: _log().
  _fetch: _fetch().
  SplitArgs.export_args: SplitArgs#export_args.
  SplitArgs.serve_args: SplitArgs#serve_args.
  _exec: _exec().
  take_binary_option: take_binary_option().
  SplitArgs: SplitArgs#
  RVLLM_VALUE_FLAGS: RVLLM_VALUE_FLAGS.
  SplitArgs.warnings: SplitArgs#warnings.
  cache_dir: cache_dir().
  _sha256: _sha256().
  PROG: PROG.
  RVLLM_VLLM_DESTS: RVLLM_VLLM_DESTS.
  SHARED_DESTS: SHARED_DESTS.
  RVLLM_BOOL_FLAGS: RVLLM_BOOL_FLAGS.
  WARN_ONLY_DESTS: WARN_ONLY_DESTS.
  LAUNCHER_DESTS: LAUNCHER_DESTS.
  INTERNAL_EXPORT_DESTS: INTERNAL_EXPORT_DESTS.
  _canonical: _canonical().
  _engine_dests: _engine_dests().
  _value_count: _value_count().
  _exporter_source_hash: _exporter_source_hash().
  export_command: export_command().
  run_export: run_export().
---
# Module: [`src/vllm_torchtpu/experimental/rust/launcher.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py)

## Classes
### <a id="LauncherError"></a>`LauncherError`  ·  implements/extends ValueError
- def: [`src/vllm_torchtpu/experimental/rust/launcher.py:124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L124) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- doc: A command line or setting the launcher cannot honor.
- signature: `class LauncherError(ValueError):`
- used by: [`split_args`](launcher.md#split_args), [`artifact_for`](launcher.md#artifact_for), [`main`](launcher.md#main), [`resolve_binary`](launcher.md#resolve_binary), [`_fetch`](launcher.md#_fetch), [`take_binary_option`](launcher.md#take_binary_option)

### <a id="SplitArgs"></a>`SplitArgs`
- def: [`src/vllm_torchtpu/experimental/rust/launcher.py:129`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L129)
- doc: A `vllm serve` command line, split between the exporter and `rvllm serve`.
- signature: `class SplitArgs:`
- members:
  - <a id="SplitArgs.export_args"></a>`export_args` — [`L133`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L133)
  - <a id="SplitArgs.model"></a>`model` — [`L132`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L132)
  - <a id="SplitArgs.serve_args"></a>`serve_args` — [`L134`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L134)
  - <a id="SplitArgs.warnings"></a>`warnings` — [`L135`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L135)
- used by: [`split_args`](launcher.md#split_args), [`artifact_for`](launcher.md#artifact_for), [`main`](launcher.md#main)

## Functions
- <a id="_canonical"></a>`_canonical(option: str)` — [`L138`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L138) — `--max_model_len` -> `--max-model-len`, as vLLM's parser accepts both.
- <a id="_engine_dests"></a>`_engine_dests()` — [`L145`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L145)
- <a id="_exec"></a>`_exec(argv: Sequence[str])` — [`L411`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L411) — Replaces this process with `argv`.
- <a id="_exporter_source_hash"></a>`_exporter_source_hash()` — [`L355`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L355)
- <a id="_fetch"></a>`_fetch(location: str, name: str, dest: Path)` — [`L291`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L291) — Copies `<location>/<name>` to `dest`; location is gs://, https:// or a path.
- <a id="_log"></a>`_log(message: str)` — [`L251`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L251)
- <a id="_sha256"></a>`_sha256(path: Path)` — [`L283`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L283)
- <a id="_value_count"></a>`_value_count(action: argparse.Action, rest: Sequence[str])` — [`L151`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L151) — How many of the following tokens `action` takes as values.
- <a id="artifact_for"></a>`artifact_for(split: SplitArgs)` — [`L387`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L387) — The exported artifact to serve: cached, or exported now.
- <a id="cache_dir"></a>`cache_dir()` — [`L255`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L255)
- <a id="export_command"></a>`export_command(model: str, output_dir: Path, export_args: Sequence[str])` — [`L364`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L364)
- <a id="main"></a>`main(argv: Sequence[str] | None = None)` — [`L416`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L416) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="resolve_binary"></a>`resolve_binary(location: str)` — [`L316`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L316) — The rvllm binary `--rvllm-binary` names, downloaded and verified if needed.
- <a id="run_export"></a>`run_export(command: Sequence[str])` — [`L380`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L380) — Runs the exporter; a failed export ends the launcher with its status.
- <a id="split_args"></a>`split_args(argv: Sequence[str], parser: argparse.ArgumentParser | None = None)` — [`L168`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L168) — Splits `argv`, a `vllm serve` command line without `serve`. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="take_binary_option"></a>`take_binary_option(args: Sequence[str])` — [`L259`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L259) — Takes `--rvllm-binary` out of `args`; returns its value and the rest.

## Module values
- <a id="INTERNAL_EXPORT_DESTS"></a>`INTERNAL_EXPORT_DESTS` — [`L119`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L119)
- <a id="LAUNCHER_DESTS"></a>`LAUNCHER_DESTS` — [`L118`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L118)
- <a id="PROG"></a>`PROG` — [`L64`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L64)
- <a id="RVLLM_BOOL_FLAGS"></a>`RVLLM_BOOL_FLAGS` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L96)
- <a id="RVLLM_VALUE_FLAGS"></a>`RVLLM_VALUE_FLAGS` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L77)
- <a id="RVLLM_VLLM_DESTS"></a>`RVLLM_VLLM_DESTS` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L69)
- <a id="SHARED_DESTS"></a>`SHARED_DESTS` — [`L74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L74)
- <a id="WARN_ONLY_DESTS"></a>`WARN_ONLY_DESTS` — [`L100`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/rust/launcher.py#L100)

