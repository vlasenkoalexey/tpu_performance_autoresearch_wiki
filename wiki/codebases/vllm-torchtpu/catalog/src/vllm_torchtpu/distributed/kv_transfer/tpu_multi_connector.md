---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.tpu_multi_connector`/
symbols:
  logger: logger.
  TPUMultiConnector.__init__: TPUMultiConnector#__init__().
  TPUMultiConnector: TPUMultiConnector#
  TPUMultiConnector.register_runner: TPUMultiConnector#register_runner().
  TPUMultiConnector.get_block_ids_with_load_errors_group_index: TPUMultiConnector#get_block_ids_with_load_errors_group_index().
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py)

## Classes
### <a id="TPUMultiConnector"></a>`TPUMultiConnector`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py:24`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py#L24)
- doc: MultiConnector combining TPURaidenConnector (disaggregation) with
- signature: `class TPUMultiConnector(MultiConnector):`
- members:
  - <a id="TPUMultiConnector.get_block_ids_with_load_errors_group_index"></a>`get_block_ids_with_load_errors_group_index(self)` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py#L72) — Return the KV cache group shared by all children's load errors.
  - <a id="TPUMultiConnector.register_runner"></a>`register_runner(self, runner)` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py#L63)
- protocol/private: <a id="TPUMultiConnector.__init__"></a>`__init__`[`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py#L36)
- uses (calls/refs, reference-scoped): [`logger`](tpu_multi_connector.md#logger)

## Module values
- <a id="logger"></a>`logger` — [`L21`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_multi_connector.py#L21)

