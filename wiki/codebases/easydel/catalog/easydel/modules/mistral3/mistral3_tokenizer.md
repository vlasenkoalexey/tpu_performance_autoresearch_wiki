---
title: 'Module: easydel/modules/mistral3/mistral3_tokenizer.py'
type: catalog
provenance: extracted
module: easydel/modules/mistral3/mistral3_tokenizer.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mistral3.mistral3_tokenizer`/Mistral3Tokenizer#
symbols:
  Mistral3Tokenizer.__call__: __call__().
  Mistral3Tokenizer.mistral_tokenizer: mistral_tokenizer.
  Mistral3Tokenizer.apply_chat_template: apply_chat_template().
  Mistral3Tokenizer.encode: encode().
  Mistral3Tokenizer.pad_token_id: pad_token_id.
  Mistral3Tokenizer.padding_side: padding_side.
  Mistral3Tokenizer.decode: decode().
  Mistral3Tokenizer.batch_encode_plus: batch_encode_plus().
  Mistral3Tokenizer.encode_plus: encode_plus().
  Mistral3Tokenizer: ''
  Mistral3Tokenizer.tokenizer: tokenizer.
  Mistral3Tokenizer.__init__: __init__().
  Mistral3Tokenizer.eos_token_id: eos_token_id.
  Mistral3Tokenizer.bos_token_id: bos_token_id.
  Mistral3Tokenizer.from_hf_hub: from_hf_hub().
---
# Module: [`easydel/modules/mistral3/mistral3_tokenizer.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py)

## Classes
### `Mistral3Tokenizer`
- def: [`easydel/modules/mistral3/mistral3_tokenizer.py:29`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L29)
- doc: A wrapper class to make the `mistral-common` tokenizer behave like a
- signature: `class Mistral3Tokenizer:`
- members:
  - `__call__(self, text: str | list[str], padding: bool | str = False, truncation: bool | str = False, max_length: int | None = None, return_tensors: str | None = None, add_special_tokens: bool = True, **kwargs)` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L126) — Tokenizes a single text or a batch of texts, with advanced options for
  - `apply_chat_template(self, conversation: list[dict[str, str]], tokenize: bool = True, add_special_tokens: bool = True, padding: bool = False, truncation: bool = False, max_length: int | None = None, return_tensors: str | None = None, **kwargs)` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L84) — Applies a chat template to a conversation history.
  - `batch_encode_plus(self, *args, **kwargs)` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L219) — Alias for `__call__` for Hugging Face compatibility.
  - `decode(self, token_ids: list[int], skip_special_tokens: bool = True)` — [`L69`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L69) — Decodes a list of token IDs back into a string.
  - `encode(self, text: str, add_special_tokens: bool = True)` — [`L53`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L53) — Encodes a single string into a list of token IDs.
  - `encode_plus(self, *args, **kwargs)` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L223) — Alias for `__call__` for Hugging Face compatibility.
  - `from_hf_hub(cls, model_name: str = "mistralai/Mistral-Nemo-Instruct-2407")` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L228) — Creates an instance from a model name on the Hugging Face Hub.
  - `bos_token_id` — [`L49`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L49)
  - `eos_token_id` — [`L48`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L48)
  - `mistral_tokenizer` — [`L45`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L45)
  - `pad_token_id` — [`L47`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L47)
  - `padding_side` — [`L51`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L51)
  - `tokenizer` — [`L50`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L50)
- protocol/private: `__init__`[`L42`](../../../../../../../raw/code/EasyDeL/easydel/modules/mistral3/mistral3_tokenizer.py#L42)
- used by: [`_import_structure`](../../__init__.md#_import_structure)

