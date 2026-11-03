---
title: 'Module: src/vllm_torchtpu/experimental/export/cli.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/cli.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.cli`/
symbols:
  run_export_from_args: run_export_from_args().
  main: main().
  _launch_workers: _launch_workers().
  build_arg_parser: build_arg_parser().
  export_speculative_config: export_speculative_config().
  _worker_env: _worker_env().
  parse_args: parse_args().
  ignored_frontend_args: ignored_frontend_args().
  create_vllm_config_from_args: create_vllm_config_from_args().
  _launch_options: _launch_options().
  export_speculative_config.positive: export_speculative_config().positive().
  EXPORT_MODES: EXPORT_MODES.
  _parse_int_list: _parse_int_list().
  _EXPORT_DESTS: _EXPORT_DESTS.
  SPECULATIVE_METHODS: SPECULATIVE_METHODS.
  _SPECULATIVE_FIELDS: _SPECULATIVE_FIELDS.
  UNIFIED_BLOCK_POOL_ENV: UNIFIED_BLOCK_POOL_ENV.
---
# Module: [`src/vllm_torchtpu/experimental/export/cli.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py)

## Functions
- <a id="_launch_options"></a>`_launch_options(argv: Sequence[str])` — [`L531`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L531) — The options `main` dispatches on, read without vLLM's argument parser.
- <a id="_launch_workers"></a>`_launch_workers(argv: Sequence[str], tp_size: int, output_dir: str, *, save_checkpoint: bool = False)` — [`L446`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L446) — Runs one export worker per tensor-parallel rank and keeps rank 0's output.
- <a id="_parse_int_list"></a>`_parse_int_list(raw: str | Sequence[int] | None)` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L45) — Parses a comma-separated string or sequence of integers into a tuple.
- <a id="_worker_env"></a>`_worker_env(tp_size: int)` — [`L422`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L422) — Environment shared by the workers of a `tp_size`-device export.
- <a id="build_arg_parser"></a>`build_arg_parser()` — [`L55`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L55) — Builds the `vllm serve` argument parser plus the export options. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="create_vllm_config_from_args"></a>`create_vllm_config_from_args(args: argparse.Namespace)` — [`L323`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L323) — Creates a `VllmConfig` from parsed CLI `EngineArgs`.
- <a id="export_speculative_config"></a>`export_speculative_config(raw: Any)` — [`L283`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L283) — The `serving_config.speculative_config` for `--speculative-config`.
- <a id="ignored_frontend_args"></a>`ignored_frontend_args(parser: argparse.ArgumentParser, args: argparse.Namespace)` — [`L222`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L222) — The `vllm serve` frontend options set in `args`, which the export ignores.
- <a id="main"></a>`main(argv: Sequence[str] | None = None)` — [`L500`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L500) — CLI entrypoint for `python -m vllm_torchtpu.experimental.export`. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="parse_args"></a>`parse_args(argv: Sequence[str] | None = None)` — [`L256`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L256) — Parses CLI arguments.
- <a id="export_speculative_config.positive"></a>`positive(name: str)` — [`L305`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L305)
- <a id="run_export_from_args"></a>`run_export_from_args(args: argparse.Namespace, *, vllm_config: Any = None, model: Any = None)` — [`L330`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L330) — Executes the AOT model export given parsed CLI arguments. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)

## Module values
- <a id="EXPORT_MODES"></a>`EXPORT_MODES` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L42)
- <a id="SPECULATIVE_METHODS"></a>`SPECULATIVE_METHODS` — [`L277`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L277)
- <a id="UNIFIED_BLOCK_POOL_ENV"></a>`UNIFIED_BLOCK_POOL_ENV` — [`L419`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L419)
- <a id="_EXPORT_DESTS"></a>`_EXPORT_DESTS` — [`L207`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L207)
- <a id="_SPECULATIVE_FIELDS"></a>`_SPECULATIVE_FIELDS` — [`L278`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/cli.py#L278)

