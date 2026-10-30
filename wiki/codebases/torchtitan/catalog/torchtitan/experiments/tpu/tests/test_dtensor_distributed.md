---
title: 'Module: torchtitan/experiments/tpu/tests/test_dtensor_distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_dtensor_distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_dtensor_distributed`/
symbols:
  _test_fully_shard_transformer_block: _test_fully_shard_transformer_block().
  _test_transformer_block_compile_view_behavior: _test_transformer_block_compile_view_behavior().
  _test_parallel_transformer_block: _test_parallel_transformer_block().
  _test_parallel_mlp: _test_parallel_mlp().
  HIDDEN_SIZE: HIDDEN_SIZE.
  TrainMLPDTensorTest.test_transformer_block_compile_view_error: TrainMLPDTensorTest#test_transformer_block_compile_view_error().
  _test_fsdp_complex_bf16_mismatch: _test_fsdp_complex_bf16_mismatch().
  SEQ_LEN: SEQ_LEN.
  Attention.forward: Attention#forward().
  TrainMLPDTensorTest.test_parallel_transformer_block_tp: TrainMLPDTensorTest#test_parallel_transformer_block_tp().
  TrainMLPDTensorTest.test_parallel_transformer_block_tp_sp: TrainMLPDTensorTest#test_parallel_transformer_block_tp_sp().
  BATCH_SIZE: BATCH_SIZE.
  TransformerBlock.forward: TransformerBlock#forward().
  TrainMLPDTensorTest.test_parallel_mlp: TrainMLPDTensorTest#test_parallel_mlp().
  TrainMLPDTensorTest.test_fully_shard_transformer_block: TrainMLPDTensorTest#test_fully_shard_transformer_block().
  TrainMLPDTensorTest.test_fsdp_complex_bf16_mismatch: TrainMLPDTensorTest#test_fsdp_complex_bf16_mismatch().
  TransformerBlock: TransformerBlock#
  INTERMEDIATE_SIZE: INTERMEDIATE_SIZE.
  TransformerBlock.attention: TransformerBlock#attention.
  _get_dtensor_hierarchy_string: _get_dtensor_hierarchy_string().
  LlamaRoPERepro.param: LlamaRoPERepro#param.
  MLP.forward: MLP#forward().
  setup_logger: setup_logger().
  set_device: set_device().
  parallelize_transformer_block_tp: parallelize_transformer_block_tp().
  MLP: MLP#
  Attention.head_dim: Attention#head_dim.
  MLP.dense_h_to_4h: MLP#dense_h_to_4h.
  MLP.dense_4h_to_h: MLP#dense_4h_to_h.
  TransformerBlock.mlp: TransformerBlock#mlp.
  TransformerBlock.init_weights: TransformerBlock#init_weights().
  parallelize_transformer_block_tp_sp: parallelize_transformer_block_tp_sp().
  parallelize_mlp: parallelize_mlp().
  NUM_TRAINING_STEPS: NUM_TRAINING_STEPS.
  NUM_HEADS: NUM_HEADS.
  train_model: train_model().
  _test_fsdp_complex_bf16_mismatch.LlamaRoPERepro.forward: _test_fsdp_complex_bf16_mismatch().LlamaRoPERepro#forward().
  TrainMLPDTensorTest: TrainMLPDTensorTest#
  MLP.intermediate_size: MLP#intermediate_size.
  Attention: Attention#
  Attention.q_proj: Attention#q_proj.
  Attention.k_proj: Attention#k_proj.
  Attention.v_proj: Attention#v_proj.
  Attention.out_proj: Attention#out_proj.
  TransformerBlock.ln_1: TransformerBlock#ln_1.
  TransformerBlock.ln_2: TransformerBlock#ln_2.
  TransformerBlock._init_weights_layer_logic: TransformerBlock#_init_weights_layer_logic().
  _test_fsdp_complex_bf16_mismatch.LlamaRoPERepro: _test_fsdp_complex_bf16_mismatch().LlamaRoPERepro#
  MLP.__init__: MLP#__init__().
  MLP.hidden_size: MLP#hidden_size.
  Attention.__init__: Attention#__init__().
  Attention.hidden_size: Attention#hidden_size.
  Attention.num_heads: Attention#num_heads.
  TransformerBlock.__init__: TransformerBlock#__init__().
  TransformerBlock.hidden_size: TransformerBlock#hidden_size.
  TransformerBlock.num_heads: TransformerBlock#num_heads.
  _test_fsdp_complex_bf16_mismatch.LlamaRoPERepro.__init__: _test_fsdp_complex_bf16_mismatch().LlamaRoPERepro#__init__().
---
# Module: [`torchtitan/experiments/tpu/tests/test_dtensor_distributed.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py)

> **Collapsed catalog** (57 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="Attention"></a>`Attention` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L60)
- <a id="Attention.__init__"></a>`Attention.__init__` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L70)
- <a id="Attention.forward"></a>`Attention.forward` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L90)
- <a id="Attention.head_dim"></a>`Attention.head_dim` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L79)
- <a id="Attention.hidden_size"></a>`Attention.hidden_size` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L76)
- <a id="Attention.k_proj"></a>`Attention.k_proj` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L84)
- <a id="Attention.num_heads"></a>`Attention.num_heads` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L77)
- <a id="Attention.out_proj"></a>`Attention.out_proj` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L88)
- <a id="Attention.q_proj"></a>`Attention.q_proj` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L83)
- <a id="Attention.v_proj"></a>`Attention.v_proj` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L85)
- <a id="BATCH_SIZE"></a>`BATCH_SIZE` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L25)
- <a id="HIDDEN_SIZE"></a>`HIDDEN_SIZE` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L27)
- <a id="INTERMEDIATE_SIZE"></a>`INTERMEDIATE_SIZE` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L28)
- <a id="LlamaRoPERepro.param"></a>`LlamaRoPERepro.param` — [`L750`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L750)
- <a id="MLP"></a>`MLP` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L33)
- <a id="MLP.__init__"></a>`MLP.__init__` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L36)
- <a id="MLP.dense_4h_to_h"></a>`MLP.dense_4h_to_h` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L48)
- <a id="MLP.dense_h_to_4h"></a>`MLP.dense_h_to_4h` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L45)
- <a id="MLP.forward"></a>`MLP.forward` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L52)
- <a id="MLP.hidden_size"></a>`MLP.hidden_size` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L42)
- <a id="MLP.intermediate_size"></a>`MLP.intermediate_size` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L43)
- <a id="NUM_HEADS"></a>`NUM_HEADS` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L30)
- <a id="NUM_TRAINING_STEPS"></a>`NUM_TRAINING_STEPS` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L29)
- <a id="SEQ_LEN"></a>`SEQ_LEN` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L26)
- <a id="TrainMLPDTensorTest"></a>`TrainMLPDTensorTest` — [`L790`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L790)
- <a id="TrainMLPDTensorTest.test_fsdp_complex_bf16_mismatch"></a>`TrainMLPDTensorTest.test_fsdp_complex_bf16_mismatch` — [`L846`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L846)
- <a id="TrainMLPDTensorTest.test_fully_shard_transformer_block"></a>`TrainMLPDTensorTest.test_fully_shard_transformer_block` — [`L817`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L817)
- <a id="TrainMLPDTensorTest.test_parallel_mlp"></a>`TrainMLPDTensorTest.test_parallel_mlp` — [`L795`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L795)
- <a id="TrainMLPDTensorTest.test_parallel_transformer_block_tp"></a>`TrainMLPDTensorTest.test_parallel_transformer_block_tp` — [`L800`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L800)
- <a id="TrainMLPDTensorTest.test_parallel_transformer_block_tp_sp"></a>`TrainMLPDTensorTest.test_parallel_transformer_block_tp_sp` — [`L808`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L808)
- <a id="TrainMLPDTensorTest.test_transformer_block_compile_view_error"></a>`TrainMLPDTensorTest.test_transformer_block_compile_view_error` — [`L824`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L824)
- <a id="TransformerBlock"></a>`TransformerBlock` — [`L127`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L127)
- <a id="TransformerBlock.__init__"></a>`TransformerBlock.__init__` — [`L130`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L130)
- <a id="TransformerBlock._init_weights_layer_logic"></a>`TransformerBlock._init_weights_layer_logic` — [`L150`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L150)
- <a id="TransformerBlock.attention"></a>`TransformerBlock.attention` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L142)
- <a id="TransformerBlock.forward"></a>`TransformerBlock.forward` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L161)
- <a id="TransformerBlock.hidden_size"></a>`TransformerBlock.hidden_size` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L137)
- <a id="TransformerBlock.init_weights"></a>`TransformerBlock.init_weights` — [`L148`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L148)
- <a id="TransformerBlock.ln_1"></a>`TransformerBlock.ln_1` — [`L141`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L141)
- <a id="TransformerBlock.ln_2"></a>`TransformerBlock.ln_2` — [`L145`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L145)
- <a id="TransformerBlock.mlp"></a>`TransformerBlock.mlp` — [`L146`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L146)
- <a id="TransformerBlock.num_heads"></a>`TransformerBlock.num_heads` — [`L138`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L138)
- <a id="_get_dtensor_hierarchy_string"></a>`_get_dtensor_hierarchy_string` — [`L397`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L397)
- <a id="_test_fsdp_complex_bf16_mismatch"></a>`_test_fsdp_complex_bf16_mismatch` — [`L736`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L736)
- <a id="_test_fsdp_complex_bf16_mismatch.LlamaRoPERepro"></a>`_test_fsdp_complex_bf16_mismatch.LlamaRoPERepro` — [`L747`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L747)
- <a id="_test_fsdp_complex_bf16_mismatch.LlamaRoPERepro.__init__"></a>`_test_fsdp_complex_bf16_mismatch.LlamaRoPERepro.__init__` — [`L748`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L748)
- <a id="_test_fsdp_complex_bf16_mismatch.LlamaRoPERepro.forward"></a>`_test_fsdp_complex_bf16_mismatch.LlamaRoPERepro.forward` — [`L756`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L756)
- <a id="_test_fully_shard_transformer_block"></a>`_test_fully_shard_transformer_block` — [`L611`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L611)
- <a id="_test_parallel_mlp"></a>`_test_parallel_mlp` — [`L450`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L450)
- <a id="_test_parallel_transformer_block"></a>`_test_parallel_transformer_block` — [`L541`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L541)
- <a id="_test_transformer_block_compile_view_behavior"></a>`_test_transformer_block_compile_view_behavior` — [`L670`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L670)
- <a id="parallelize_mlp"></a>`parallelize_mlp` — [`L268`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L268)
- <a id="parallelize_transformer_block_tp"></a>`parallelize_transformer_block_tp` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L178)
- <a id="parallelize_transformer_block_tp_sp"></a>`parallelize_transformer_block_tp_sp` — [`L216`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L216)
- <a id="set_device"></a>`set_device` — [`L388`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L388)
- <a id="setup_logger"></a>`setup_logger` — [`L378`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L378)
- <a id="train_model"></a>`train_model` — [`L303`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_dtensor_distributed.py#L303)
