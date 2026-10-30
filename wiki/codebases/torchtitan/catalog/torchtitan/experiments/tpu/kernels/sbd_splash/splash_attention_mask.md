---
title: 'Module: torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.sbd_splash.splash_attention_mask`/
symbols:
  Mask.shape: Mask#shape().
  Mask: Mask#
  _ComputableMask.shape: _ComputableMask#shape().
  _ComputableMask.q_sequence: _ComputableMask#q_sequence.
  _ComputableMask: _ComputableMask#
  _ComputableMask.__init__: _ComputableMask#__init__().
  LogicalOr.__init__: LogicalOr#__init__().
  LogicalAnd.__init__: LogicalAnd#__init__().
  _ComputableMask.__getitem__: _ComputableMask#__getitem__().
  LocalMask.__init__: LocalMask#__init__().
  LocalMask.__eq__: LocalMask#__eq__().
  LocalMask.__hash__: LocalMask#__hash__().
  FullMask.shape: FullMask#shape().
  CausalMask.__init__: CausalMask#__init__().
  CausalMask.__eq__: CausalMask#__eq__().
  CausalMask.__hash__: CausalMask#__hash__().
  ChunkedCausalMask.__init__: ChunkedCausalMask#__init__().
  ChunkedCausalMask.__eq__: ChunkedCausalMask#__eq__().
  ChunkedCausalMask.__hash__: ChunkedCausalMask#__hash__().
  NumpyMask.array: NumpyMask#array.
  LogicalOr.left: LogicalOr#left.
  LogicalAnd.left: LogicalAnd#left.
  CausalMask.offset: CausalMask#offset.
  ChunkedCausalMask.chunk_size: ChunkedCausalMask#chunk_size.
  LocalMask.local_mask_function: LocalMask#local_mask_function().
  LogicalOr.right: LogicalOr#right.
  LogicalAnd.right: LogicalAnd#right.
  Mask.__or__: Mask#__or__().
  Mask.__and__: Mask#__and__().
  LogicalOr.shape: LogicalOr#shape().
  LogicalOr.__getitem__: LogicalOr#__getitem__().
  LogicalOr.__hash__: LogicalOr#__hash__().
  LogicalAnd.shape: LogicalAnd#shape().
  LogicalAnd.__getitem__: LogicalAnd#__getitem__().
  LogicalAnd.__hash__: LogicalAnd#__hash__().
  LocalMask.window_size: LocalMask#window_size.
  LocalMask.offset: LocalMask#offset.
  FullMask.__getitem__: FullMask#__getitem__().
  CausalMask: CausalMask#
  _fill_slice: _fill_slice().
  CausalMask.causal_mask_function: CausalMask#causal_mask_function().
  ChunkedCausalMask.chunked_causal_mask_function: ChunkedCausalMask#chunked_causal_mask_function().
  LocalMask: LocalMask#
  NumpyMask: NumpyMask#
  FullMask: FullMask#
  LogicalOr: LogicalOr#
  LogicalAnd: LogicalAnd#
  ChunkedCausalMask: ChunkedCausalMask#
  NumpyMask.__post_init__: NumpyMask#__post_init__().
  NumpyMask.shape: NumpyMask#shape().
  NumpyMask.__getitem__: NumpyMask#__getitem__().
  NumpyMask.__eq__: NumpyMask#__eq__().
  NumpyMask.__hash__: NumpyMask#__hash__().
  FullMask.__post_init__: FullMask#__post_init__().
  FullMask.__eq__: FullMask#__eq__().
  FullMask.__hash__: FullMask#__hash__().
  _ComputableMask._shape: _ComputableMask#_shape.
  _ComputableMask.mask_function: _ComputableMask#mask_function.
  FullMask._shape: FullMask#_shape.
  Mask.__getitem__: Mask#__getitem__().
  Mask.__bool__: Mask#__bool__().
  make_causal_mask: make_causal_mask().
  make_local_attention_mask: make_local_attention_mask().
  make_chunk_attention_mask: make_chunk_attention_mask().
  make_random_mask: make_random_mask().
  _ComputableMask.__eq__: _ComputableMask#__eq__().
  _ComputableMask.__hash__: _ComputableMask#__hash__().
---
# Module: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py)

## Classes
### <a id="CausalMask"></a>`CausalMask`  ·  implements/extends _ComputableMask
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:234`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L234)
- doc: Lazy causal mask, prevents the model from attending to future tokens.
- signature: `class CausalMask(_ComputableMask):`
- members:
  - <a id="CausalMask.causal_mask_function"></a>`causal_mask_function(q_ids, kv_ids)` — [`L254`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L254)
  - <a id="CausalMask.offset"></a>`offset` — [`L244`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L244)
- protocol/private: <a id="CausalMask.__eq__"></a>`__eq__`[`L271`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L271), <a id="CausalMask.__hash__"></a>`__hash__`[`L281`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L281), <a id="CausalMask.__init__"></a>`__init__`[`L246`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L246)
- uses (calls/refs, reference-scoped): [`shape`](splash_attention_mask.md#_ComputableMask.shape), [`q_sequence`](splash_attention_mask.md#_ComputableMask.q_sequence), [`_ComputableMask`](splash_attention_mask.md#_ComputableMask), [`__init__`](splash_attention_mask.md#_ComputableMask.__init__)
- used by: [`_build_kernel`](../splash_bias_dropout.md#_build_kernel), [`_make_splash_attention`](splash_attention_kernel.md#_make_splash_attention), [`_ComputableMask`](splash_attention_mask.md#_ComputableMask)

### <a id="ChunkedCausalMask"></a>`ChunkedCausalMask`  ·  implements/extends _ComputableMask
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:290`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L290) — documented in [tpu-pallas-kernels](../../../../../../concepts/tpu-pallas-kernels.md)
- doc: Lazy chunked causal mask.
- signature: `class ChunkedCausalMask(_ComputableMask):`
- members:
  - <a id="ChunkedCausalMask.chunked_causal_mask_function"></a>`chunked_causal_mask_function(q_ids, kv_ids)` — [`L315`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L315) — Computes the mask logic for the given slice indices.
  - <a id="ChunkedCausalMask.chunk_size"></a>`chunk_size` — [`L302`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L302)
- protocol/private: <a id="ChunkedCausalMask.__eq__"></a>`__eq__`[`L331`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L331), <a id="ChunkedCausalMask.__hash__"></a>`__hash__`[`L341`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L341), <a id="ChunkedCausalMask.__init__"></a>`__init__`[`L304`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L304)
- uses (calls/refs, reference-scoped): [`shape`](splash_attention_mask.md#_ComputableMask.shape), [`q_sequence`](splash_attention_mask.md#_ComputableMask.q_sequence), [`_ComputableMask`](splash_attention_mask.md#_ComputableMask), [`__init__`](splash_attention_mask.md#_ComputableMask.__init__)
- used by: [`_ComputableMask`](splash_attention_mask.md#_ComputableMask)

### <a id="FullMask"></a>`FullMask`  ·  implements/extends Mask
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:468`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L468)
- doc: Lazy full mask, allows all tokens to attend to all other tokens.
- signature: `class FullMask(Mask):`
- members:
  - <a id="FullMask.shape"></a>`shape(self)` — [`L480`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L480)
- protocol/private: <a id="FullMask.__eq__"></a>`__eq__`[`L493`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L493), <a id="FullMask.__getitem__"></a>`__getitem__`[`L483`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L483), <a id="FullMask.__hash__"></a>`__hash__`[`L499`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L499), <a id="FullMask.__post_init__"></a>`__post_init__`[`L475`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L475), <a id="FullMask._shape"></a>`_shape`[`L473`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L473)
- uses (calls/refs, reference-scoped): [`Mask`](splash_attention_mask.md#Mask), [`_fill_slice`](splash_attention_mask.md#_fill_slice)
- used by: [`_build_kernel`](../splash_bias_dropout.md#_build_kernel), [`shape`](splash_attention_mask.md#Mask.shape), [`Mask`](splash_attention_mask.md#Mask)

### <a id="LocalMask"></a>`LocalMask`  ·  implements/extends _ComputableMask
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:350`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L350)
- doc: Lazy local mask, prevents model from attending to tokens outside window.
- signature: `class LocalMask(_ComputableMask):`
- members:
  - <a id="LocalMask.local_mask_function"></a>`local_mask_function(q_ids, kv_ids)` — [`L375`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L375) — Computes the local attention mask for the given slice indices.
  - <a id="LocalMask.offset"></a>`offset` — [`L363`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L363)
  - <a id="LocalMask.window_size"></a>`window_size` — [`L362`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L362)
- protocol/private: <a id="LocalMask.__eq__"></a>`__eq__`[`L407`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L407), <a id="LocalMask.__hash__"></a>`__hash__`[`L418`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L418), <a id="LocalMask.__init__"></a>`__init__`[`L365`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L365)
- uses (calls/refs, reference-scoped): [`shape`](splash_attention_mask.md#_ComputableMask.shape), [`q_sequence`](splash_attention_mask.md#_ComputableMask.q_sequence), [`_ComputableMask`](splash_attention_mask.md#_ComputableMask), [`__init__`](splash_attention_mask.md#_ComputableMask.__init__)
- used by: [`_build_kernel`](../splash_bias_dropout.md#_build_kernel), [`_ComputableMask`](splash_attention_mask.md#_ComputableMask)

### <a id="LogicalAnd"></a>`LogicalAnd`
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:143`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L143)
- members:
  - <a id="LogicalAnd.shape"></a>`shape(self)` — [`L154`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L154)
  - <a id="LogicalAnd.left"></a>`left` — [`L144`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L144)
  - <a id="LogicalAnd.right"></a>`right` — [`L145`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L145)
- protocol/private: <a id="LogicalAnd.__getitem__"></a>`__getitem__`[`L157`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L157), <a id="LogicalAnd.__hash__"></a>`__hash__`[`L160`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L160), <a id="LogicalAnd.__init__"></a>`__init__`[`L147`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L147)
- uses (calls/refs, reference-scoped): [`shape`](splash_attention_mask.md#Mask.shape), [`Mask`](splash_attention_mask.md#Mask)
- used by: [`shape`](splash_attention_mask.md#Mask.shape), [`__and__`](splash_attention_mask.md#Mask.__and__)

### <a id="LogicalOr"></a>`LogicalOr`
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:121`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L121)
- members:
  - <a id="LogicalOr.shape"></a>`shape(self)` — [`L132`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L132)
  - <a id="LogicalOr.left"></a>`left` — [`L122`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L122)
  - <a id="LogicalOr.right"></a>`right` — [`L123`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L123)
- protocol/private: <a id="LogicalOr.__getitem__"></a>`__getitem__`[`L135`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L135), <a id="LogicalOr.__hash__"></a>`__hash__`[`L138`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L138), <a id="LogicalOr.__init__"></a>`__init__`[`L125`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L125)
- uses (calls/refs, reference-scoped): [`shape`](splash_attention_mask.md#Mask.shape), [`Mask`](splash_attention_mask.md#Mask)
- used by: [`shape`](splash_attention_mask.md#Mask.shape), [`__or__`](splash_attention_mask.md#Mask.__or__)

### <a id="Mask"></a>`Mask`
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:14`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L14)
- doc: A base class for splash attention masks.
- signature: `class Mask:`
- members:
  - <a id="Mask.shape"></a>`shape(self)` — [`L18`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L18)
- protocol/private: <a id="Mask.__and__"></a>`__and__`[`L37`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L37), <a id="Mask.__bool__"></a>`__bool__`[`L24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L24), <a id="Mask.__getitem__"></a>`__getitem__`[`L21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L21), <a id="Mask.__or__"></a>`__or__`[`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L30)
- uses (calls/refs, reference-scoped): [`shape`](splash_attention_mask.md#_ComputableMask.shape), [`_ComputableMask`](splash_attention_mask.md#_ComputableMask), [`shape`](splash_attention_mask.md#FullMask.shape), [`shape`](splash_attention_mask.md#LogicalAnd.shape), [`shape`](splash_attention_mask.md#LogicalOr.shape), [`FullMask`](splash_attention_mask.md#FullMask), [`LogicalAnd`](splash_attention_mask.md#LogicalAnd), [`LogicalOr`](splash_attention_mask.md#LogicalOr), [`NumpyMask`](splash_attention_mask.md#NumpyMask), [`shape`](splash_attention_mask.md#NumpyMask.shape)
- used by: [`_make_splash_attention`](splash_attention_kernel.md#_make_splash_attention), [`_process_mask`](splash_attention_mask_info.md#_process_mask), [`_ComputableMask`](splash_attention_mask.md#_ComputableMask), [`__init__`](splash_attention_mask.md#LogicalAnd.__init__), [`__init__`](splash_attention_mask.md#LogicalOr.__init__), [`left`](splash_attention_mask.md#LogicalAnd.left), [`left`](splash_attention_mask.md#LogicalOr.left), [`right`](splash_attention_mask.md#LogicalAnd.right), [`right`](splash_attention_mask.md#LogicalOr.right), [`_check_mask`](splash_attention_mask_info.md#_check_mask), [`shape`](splash_attention_mask.md#LogicalAnd.shape), [`shape`](splash_attention_mask.md#LogicalOr.shape), [`FullMask`](splash_attention_mask.md#FullMask), [`LogicalAnd`](splash_attention_mask.md#LogicalAnd), [`LogicalOr`](splash_attention_mask.md#LogicalOr), [`NumpyMask`](splash_attention_mask.md#NumpyMask)

### <a id="NumpyMask"></a>`NumpyMask`  ·  implements/extends Mask
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:429`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L429)
- doc: A mask backed by a dense numpy array.
- signature: `class NumpyMask(Mask):`
- members:
  - <a id="NumpyMask.shape"></a>`shape(self)` — [`L442`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L442)
  - <a id="NumpyMask.array"></a>`array` — [`L432`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L432)
- protocol/private: <a id="NumpyMask.__eq__"></a>`__eq__`[`L448`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L448), <a id="NumpyMask.__getitem__"></a>`__getitem__`[`L445`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L445), <a id="NumpyMask.__hash__"></a>`__hash__`[`L454`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L454), <a id="NumpyMask.__post_init__"></a>`__post_init__`[`L434`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L434)
- uses (calls/refs, reference-scoped): [`Mask`](splash_attention_mask.md#Mask)
- used by: [`_make_splash_attention`](splash_attention_kernel.md#_make_splash_attention), [`shape`](splash_attention_mask.md#Mask.shape), [`Mask`](splash_attention_mask.md#Mask)

### <a id="_ComputableMask"></a>`_ComputableMask`  ·  implements/extends Mask
- def: [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py:164`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L164)
- doc: Superclass for all masks that can be computed inside the kernel using a callable object.
- signature: `class _ComputableMask(Mask):`
- members:
  - <a id="_ComputableMask.shape"></a>`shape(self)` — [`L208`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L208)
  - <a id="_ComputableMask.mask_function"></a>`mask_function` — [`L187`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L187)
  - <a id="_ComputableMask.q_sequence"></a>`q_sequence` — [`L186`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L186)
- protocol/private: <a id="_ComputableMask.__eq__"></a>`__eq__`[`L227`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L227), <a id="_ComputableMask.__getitem__"></a>`__getitem__`[`L211`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L211), <a id="_ComputableMask.__hash__"></a>`__hash__`[`L230`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L230), <a id="_ComputableMask.__init__"></a>`__init__`[`L189`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L189), <a id="_ComputableMask._shape"></a>`_shape`[`L185`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L185)
- uses (calls/refs, reference-scoped): [`Mask`](splash_attention_mask.md#Mask), [`CausalMask`](splash_attention_mask.md#CausalMask), [`_fill_slice`](splash_attention_mask.md#_fill_slice), [`LocalMask`](splash_attention_mask.md#LocalMask), [`ChunkedCausalMask`](splash_attention_mask.md#ChunkedCausalMask)
- used by: [`shape`](splash_attention_mask.md#Mask.shape), [`Mask`](splash_attention_mask.md#Mask), [`__eq__`](splash_attention_mask.md#LocalMask.__eq__), [`__hash__`](splash_attention_mask.md#LocalMask.__hash__), [`__init__`](splash_attention_mask.md#LocalMask.__init__), [`__eq__`](splash_attention_mask.md#CausalMask.__eq__), [`__eq__`](splash_attention_mask.md#ChunkedCausalMask.__eq__), [`__hash__`](splash_attention_mask.md#CausalMask.__hash__), [`__hash__`](splash_attention_mask.md#ChunkedCausalMask.__hash__), [`__init__`](splash_attention_mask.md#CausalMask.__init__), [`__init__`](splash_attention_mask.md#ChunkedCausalMask.__init__), [`CausalMask`](splash_attention_mask.md#CausalMask), [`LocalMask`](splash_attention_mask.md#LocalMask), [`ChunkedCausalMask`](splash_attention_mask.md#ChunkedCausalMask)

## Functions
- <a id="_fill_slice"></a>`_fill_slice(inp_slice: slice, size: int)` — [`L458`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L458)
- <a id="make_causal_mask"></a>`make_causal_mask(shape: tuple[int, int], offset: int = 0)` — [`L45`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L45) — Makes a causal attention mask.
- <a id="make_chunk_attention_mask"></a>`make_chunk_attention_mask(shape: tuple[int, int], chunk_size: int)` — [`L83`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L83) — Makes a chunked causal attention mask.
- <a id="make_local_attention_mask"></a>`make_local_attention_mask(shape: tuple[int, int], window_size: tuple[int | None, int | None], *, offset: int = 0)` — [`L64`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L64) — Makes a local attention mask.
- <a id="make_random_mask"></a>`make_random_mask(shape: tuple[int, int], sparsity: float, seed: int)` — [`L112`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py#L112) — Makes a random attention mask.

