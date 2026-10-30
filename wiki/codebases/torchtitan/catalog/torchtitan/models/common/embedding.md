---
title: 'Module: torchtitan/models/common/embedding.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/embedding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.embedding`/
symbols:
  Embedding: Embedding#
  Embedding.Config: Embedding#Config#
  Embedding.Config.embedding_dim: Embedding#Config#embedding_dim.
  Embedding.Config.num_embeddings: Embedding#Config#num_embeddings.
  Embedding.__init__: Embedding#__init__().
  Embedding.parallelize: Embedding#parallelize().
  Embedding.forward: Embedding#forward().
  Embedding.tp_group: Embedding#tp_group.
  __all__: __all__.
---
# Module: [`torchtitan/models/common/embedding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py)

## Classes
### <a id="Embedding"></a>`Embedding`  ·  implements/extends Module
- def: [`torchtitan/models/common/embedding.py:24`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L24) — documented in [model-building-blocks](../../../../concepts/model-building-blocks.md)
- doc: Configurable embedding with optional local vocab-parallel execution.
- signature: `class Embedding(nn.Embedding, Module):`
- members:
  - <a id="Embedding.forward"></a>`forward(self, input: torch.Tensor)` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L47) — Runs vocab-parallel embedding when the module has a TP group.
  - <a id="Embedding.parallelize"></a>`parallelize(self, parallel_dims: ParallelDims)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L39)
  - <a id="Embedding.tp_group"></a>`tp_group` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L37)
- protocol/private: <a id="Embedding.__init__"></a>`__init__`[`L35`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L35)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`Config`](embedding.md#Embedding.Config), [`embedding_dim`](embedding.md#Embedding.Config.embedding_dim), [`num_embeddings`](embedding.md#Embedding.Config.num_embeddings), [`get_optional_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_optional_mesh)  (2 test-only)
- used by: [`Module`](../../protocols/module.md#Module), [`_debugmodel`](../deepseek_v4/__init__.md#_debugmodel), [`_deepseek_v4_flash`](../deepseek_v4/__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](../deepseek_v4/__init__.md#_deepseek_v4_pro), [`_muse_glimmer_config`](../muse_glimmer/__init__.md#_muse_glimmer_config), [`_kimi_k3_config`](../kimi_k3/__init__.md#_kimi_k3_config), [`_16b`](../deepseek_v3/__init__.md#_16b), [`_236b`](../deepseek_v3/__init__.md#_236b), [`_671b`](../deepseek_v3/__init__.md#_671b), [`_debugmodel`](../deepseek_v3/__init__.md#_debugmodel), [`_testmodel`](../deepseek_v3/__init__.md#_testmodel), [`_debugmodel`](../kimi_k2_7/__init__.md#_debugmodel), [`_kimi_k2_5`](../kimi_k2_7/__init__.md#_kimi_k2_5), [`_120b`](../gpt_oss/__init__.md#_120b), [`_20b`](../gpt_oss/__init__.md#_20b), [`_debugmodel`](../gpt_oss/__init__.md#_debugmodel), [`_testmodel`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel_moe), [`_1b`](../llama3/__init__.md#_1b), [`_3b`](../llama3/__init__.md#_3b), [`_moonlight_16b_a3b_config`](../kimi_k2_7/__init__.md#_moonlight_16b_a3b_config), [`_405b`](../llama3/__init__.md#_405b), [`_70b`](../llama3/__init__.md#_70b), [`_8b`](../llama3/__init__.md#_8b), [`_debugmodel`](../llama3/__init__.md#_debugmodel), [`_27b`](../qwen3_5/__init__.md#_27b), [`_debugmodel`](../qwen3_5/__init__.md#_debugmodel), [`_debugmodel_moe`](../qwen3_5/__init__.md#_debugmodel_moe), [`_35b_a3b`](../qwen3_5/__init__.md#_35b_a3b), [`_0_8b`](../qwen3_5/__init__.md#_0_8b), [`_122b_a10b`](../qwen3_5/__init__.md#_122b_a10b), [`_2b`](../qwen3_5/__init__.md#_2b), [`_397b_a17b`](../qwen3_5/__init__.md#_397b_a17b), [`_4b`](../qwen3_5/__init__.md#_4b), [`_9b`](../qwen3_5/__init__.md#_9b), [`_testmodel`](../../experiments/tpu/llama3/__init__.md#_testmodel), [`tok_embeddings`](decoder.md#Decoder.Config.tok_embeddings), [`_8b_tpu`](../../experiments/tpu/qwen3/__init__.md#_8b_tpu), [`_debugmodel`](../qwen3/__init__.md#_debugmodel), [`_0_6b`](../qwen3/__init__.md#_0_6b)  (+13 more; 4 test-only)

### <a id="Embedding.Config"></a>`Embedding.Config`  ·  implements/extends Config
- def: [`torchtitan/models/common/embedding.py:31`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L31)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Embedding.Config.embedding_dim"></a>`embedding_dim` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L33)
  - <a id="Embedding.Config.num_embeddings"></a>`num_embeddings` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L32)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_debugmodel`](../deepseek_v4/__init__.md#_debugmodel), [`_deepseek_v4_flash`](../deepseek_v4/__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](../deepseek_v4/__init__.md#_deepseek_v4_pro), [`_muse_glimmer_config`](../muse_glimmer/__init__.md#_muse_glimmer_config), [`_kimi_k3_config`](../kimi_k3/__init__.md#_kimi_k3_config), [`_16b`](../deepseek_v3/__init__.md#_16b), [`_236b`](../deepseek_v3/__init__.md#_236b), [`_671b`](../deepseek_v3/__init__.md#_671b), [`_debugmodel`](../deepseek_v3/__init__.md#_debugmodel), [`_testmodel`](../deepseek_v3/__init__.md#_testmodel), [`_debugmodel`](../kimi_k2_7/__init__.md#_debugmodel), [`_kimi_k2_5`](../kimi_k2_7/__init__.md#_kimi_k2_5), [`_120b`](../gpt_oss/__init__.md#_120b), [`_20b`](../gpt_oss/__init__.md#_20b), [`_debugmodel`](../gpt_oss/__init__.md#_debugmodel), [`_testmodel`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel_moe), [`_1b`](../llama3/__init__.md#_1b), [`_3b`](../llama3/__init__.md#_3b), [`_moonlight_16b_a3b_config`](../kimi_k2_7/__init__.md#_moonlight_16b_a3b_config), [`_405b`](../llama3/__init__.md#_405b), [`_70b`](../llama3/__init__.md#_70b), [`_8b`](../llama3/__init__.md#_8b), [`_debugmodel`](../llama3/__init__.md#_debugmodel), [`_27b`](../qwen3_5/__init__.md#_27b), [`_debugmodel`](../qwen3_5/__init__.md#_debugmodel), [`_debugmodel_moe`](../qwen3_5/__init__.md#_debugmodel_moe), [`_35b_a3b`](../qwen3_5/__init__.md#_35b_a3b), [`_0_8b`](../qwen3_5/__init__.md#_0_8b), [`_122b_a10b`](../qwen3_5/__init__.md#_122b_a10b), [`_2b`](../qwen3_5/__init__.md#_2b), [`_397b_a17b`](../qwen3_5/__init__.md#_397b_a17b), [`_4b`](../qwen3_5/__init__.md#_4b), [`_9b`](../qwen3_5/__init__.md#_9b), [`_testmodel`](../../experiments/tpu/llama3/__init__.md#_testmodel), [`tok_embeddings`](decoder.md#Decoder.Config.tok_embeddings), [`_8b_tpu`](../../experiments/tpu/qwen3/__init__.md#_8b_tpu), [`_debugmodel`](../qwen3/__init__.md#_debugmodel), [`_0_6b`](../qwen3/__init__.md#_0_6b), [`_1_7b`](../qwen3/__init__.md#_1_7b)  (+12 more; 5 test-only)

## Module values
- <a id="__all__"></a>`__all__` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/embedding.py#L82)

