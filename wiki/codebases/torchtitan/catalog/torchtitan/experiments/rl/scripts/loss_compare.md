---
title: 'Module: torchtitan/experiments/rl/scripts/loss_compare.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/scripts/loss_compare.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.scripts.loss_compare`/
symbols:
  main: main().
  log_print: log_print().
  extract_losses_from_tensorboard: extract_losses_from_tensorboard().
  assert_losses_equal: assert_losses_equal().
  run_training: run_training().
  TB_LOSS_TAG: TB_LOSS_TAG.
  LOG_PREFIX: LOG_PREFIX.
  assert_losses_equal.LossEqualityTest: assert_losses_equal().LossEqualityTest#
  assert_losses_equal.LossEqualityTest.test_losses_equal: assert_losses_equal().LossEqualityTest#test_losses_equal().
---
# Module: [`torchtitan/experiments/rl/scripts/loss_compare.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py)

## Classes
### <a id="assert_losses_equal.LossEqualityTest"></a>`assert_losses_equal.LossEqualityTest`  ·  implements/extends TestCase
- def: [`torchtitan/experiments/rl/scripts/loss_compare.py:177`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L177)
- signature: `class LossEqualityTest(unittest.TestCase):`
- members:
  - <a id="assert_losses_equal.LossEqualityTest.test_losses_equal"></a>`test_losses_equal(self)` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L178)
- used by: [`assert_losses_equal`](loss_compare.md#assert_losses_equal)

## Functions
- <a id="assert_losses_equal"></a>`assert_losses_equal(actual: dict[int, float], expected: dict[int, float])` — [`L168`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L168) — Assert exact floating-point equality between actual and expected losses.
- <a id="extract_losses_from_tensorboard"></a>`extract_losses_from_tensorboard(tb_dir: str)` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L63) — Extract ``loss/mean`` scalars from TensorBoard event files.
- <a id="log_print"></a>`log_print(message: str = "")` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L51)
- <a id="main"></a>`main()` — [`L221`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L221)
- <a id="run_training"></a>`run_training(hf_assets_path: str, dump_folder: str, config: str, options: str = "")` — [`L113`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L113) — Run RL GRPO training as a subprocess.

## Module values
- <a id="LOG_PREFIX"></a>`LOG_PREFIX` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L46)
- <a id="TB_LOSS_TAG"></a>`TB_LOSS_TAG` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/scripts/loss_compare.py#L48)

