---
title: 'Module: torchtitan/experiments/tpu/gmain.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/gmain.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.gmain`/
symbols:
  _start_trainer: _start_trainer().
  main: main().
  handle_main: handle_main().
  global_start_trainer_func: global_start_trainer_func.
  _verify_requested_device: _verify_requested_device().
  _parse_flags: _parse_flags().
---
# Module: [`torchtitan/experiments/tpu/gmain.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gmain.py)

## Functions
- <a id="_parse_flags"></a>`_parse_flags(argv: Sequence[str])` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gmain.py#L51) — Parses command-line flags.
- <a id="_start_trainer"></a>`_start_trainer(config: tpu_job_config_module.TPUTrainerConfig)` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gmain.py#L23) — Starts the trainer with the specified eager mode if enabled.
- <a id="_verify_requested_device"></a>`_verify_requested_device(requested: str | None)` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gmain.py#L81) — Checks --device against the device that was actually detected.
- <a id="handle_main"></a>`handle_main(start_trainer_func: Callable[[tpu_job_config_module.TPUTrainerConfig], None])` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gmain.py#L124)
- <a id="main"></a>`main(parsed_args: Tuple[argparse.Namespace, List[str]])` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gmain.py#L111)

## Module values
- <a id="global_start_trainer_func"></a>`global_start_trainer_func` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/gmain.py#L20)

