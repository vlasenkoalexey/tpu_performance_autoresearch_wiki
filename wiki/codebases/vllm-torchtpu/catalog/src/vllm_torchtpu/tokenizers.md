---
title: 'Module: src/vllm_torchtpu/tokenizers.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/tokenizers.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.tokenizers`/
symbols:
  _tpu_deepseek_v4_tokenizer: _tpu_deepseek_v4_tokenizer().
  _tpu_deepseek_v4_tokenizer._TpuDeepseekV4Tokenizer.__reduce__: _tpu_deepseek_v4_tokenizer()._TpuDeepseekV4Tokenizer#__reduce__().
  TpuDeepseekV4Tokenizer.from_pretrained: TpuDeepseekV4Tokenizer#from_pretrained().
  register_tokenizers: register_tokenizers().
  _tpu_deepseek_v4_tokenizer._TpuDeepseekV4Tokenizer: _tpu_deepseek_v4_tokenizer()._TpuDeepseekV4Tokenizer#
  _tpu_deepseek_v4_tokenizer._TpuDeepseekV4Tokenizer.apply_chat_template: _tpu_deepseek_v4_tokenizer()._TpuDeepseekV4Tokenizer#apply_chat_template().
  TpuDeepseekV4Tokenizer: TpuDeepseekV4Tokenizer#
---
# Module: [`src/vllm_torchtpu/tokenizers.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tokenizers.py)

## Classes
### <a id="TpuDeepseekV4Tokenizer"></a>`TpuDeepseekV4Tokenizer`
- def: [`src/vllm_torchtpu/tokenizers.py:61`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tokenizers.py#L61)
- doc: Registry entry point for `tokenizer_mode=deepseek_v4`.
- signature: `class TpuDeepseekV4Tokenizer(TokenizerLike):`
- members:
  - <a id="TpuDeepseekV4Tokenizer.from_pretrained"></a>`from_pretrained(cls, *args, **kwargs)` — [`L65`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tokenizers.py#L65)
- uses (calls/refs, reference-scoped): [`_tpu_deepseek_v4_tokenizer`](tokenizers.md#_tpu_deepseek_v4_tokenizer)

### <a id="_tpu_deepseek_v4_tokenizer._TpuDeepseekV4Tokenizer"></a>`_tpu_deepseek_v4_tokenizer._TpuDeepseekV4Tokenizer`
- def: [`src/vllm_torchtpu/tokenizers.py:39`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tokenizers.py#L39)
- signature: `class _TpuDeepseekV4Tokenizer(base_cls):`
- members:
  - <a id="_tpu_deepseek_v4_tokenizer._TpuDeepseekV4Tokenizer.apply_chat_template"></a>`apply_chat_template(self, messages, tools=None, **kwargs)` — [`L40`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tokenizers.py#L40) — Set ``wo_eos`` on a trailing assistant turn when
- protocol/private: <a id="_tpu_deepseek_v4_tokenizer._TpuDeepseekV4Tokenizer.__reduce__"></a>`__reduce__`[`L53`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tokenizers.py#L53)
- uses (calls/refs, reference-scoped): [`_tpu_deepseek_v4_tokenizer`](tokenizers.md#_tpu_deepseek_v4_tokenizer)
- used by: [`_tpu_deepseek_v4_tokenizer`](tokenizers.md#_tpu_deepseek_v4_tokenizer)

## Functions
- <a id="_tpu_deepseek_v4_tokenizer"></a>`_tpu_deepseek_v4_tokenizer(tokenizer)` — [`L31`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tokenizers.py#L31) — Return a copy of ``tokenizer`` that honors ``continue_final_message``.
- <a id="register_tokenizers"></a>`register_tokenizers()` — [`L73`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tokenizers.py#L73)

