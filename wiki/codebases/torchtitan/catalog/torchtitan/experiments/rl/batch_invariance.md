---
title: 'Module: torchtitan/experiments/rl/batch_invariance.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/batch_invariance.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.batch_invariance`/
symbols:
  BatchInvariantFlexConverter.convert: BatchInvariantFlexConverter#convert().
  force_logprobs_fn_for_batch_invariance: force_logprobs_fn_for_batch_invariance().
  BatchInvariantFlexConverter.Config: BatchInvariantFlexConverter#Config#
  BatchInvariantFlexConverter: BatchInvariantFlexConverter#
  force_logprobs_fn_for_batch_invariance.generator_compute_token_logprobs: force_logprobs_fn_for_batch_invariance().generator_compute_token_logprobs().
  BatchInvariantFlexConverter.__init__: BatchInvariantFlexConverter#__init__().
  logger: logger.
  BatchInvariantFlexConverter._BLOCK_M: BatchInvariantFlexConverter#_BLOCK_M.
  BatchInvariantFlexConverter._BLOCK_N: BatchInvariantFlexConverter#_BLOCK_N.
---
# Module: [`torchtitan/experiments/rl/batch_invariance.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py)

## Classes
### <a id="BatchInvariantFlexConverter"></a>`BatchInvariantFlexConverter`  ·  implements/extends ModelConfigConverter
- def: [`torchtitan/experiments/rl/batch_invariance.py:25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L25)
- doc: Pin flex attention kernel options for batch-invariant mode.
- signature: `class BatchInvariantFlexConverter(ModelConfigConverter):`
- members:
  - <a id="BatchInvariantFlexConverter.convert"></a>`convert(self, model_config)` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L47)
- protocol/private: <a id="BatchInvariantFlexConverter._BLOCK_M"></a>`_BLOCK_M`[`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L37), <a id="BatchInvariantFlexConverter._BLOCK_N"></a>`_BLOCK_N`[`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L38), <a id="BatchInvariantFlexConverter.__init__"></a>`__init__`[`L44`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L44)
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](../../models/common/attention.md#FlexInnerAttention), [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`Config`](../../models/common/attention.md#FlexInnerAttention.Config), [`Config`](batch_invariance.md#BatchInvariantFlexConverter.Config), [`kernel_options`](../../models/common/attention.md#FlexInnerAttention.Config.kernel_options)
- used by: [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`convert`](../../protocols/model.md#ModelConfigConverter.convert)  (1 test-only)

### <a id="BatchInvariantFlexConverter.Config"></a>`BatchInvariantFlexConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/batch_invariance.py:41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L41)
- signature: `class Config(ModelConfigConverter.Config):`
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`Config`](../../protocols/model.md#ModelConfigConverter.Config)
- used by: [`__init__`](batch_invariance.md#BatchInvariantFlexConverter.__init__)  (1 test-only)

## Functions
- <a id="force_logprobs_fn_for_batch_invariance"></a>`force_logprobs_fn_for_batch_invariance()` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L57) — Make vLLM's v2 logprob path dispatch.
- <a id="force_logprobs_fn_for_batch_invariance.generator_compute_token_logprobs"></a>`generator_compute_token_logprobs(logits: torch.Tensor, token_ids: torch.Tensor)` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L71) — Per-token logprobs for vLLM's v2 sampler (replaces its fused kernel).

## Module values
- <a id="logger"></a>`logger` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/batch_invariance.py#L22)

