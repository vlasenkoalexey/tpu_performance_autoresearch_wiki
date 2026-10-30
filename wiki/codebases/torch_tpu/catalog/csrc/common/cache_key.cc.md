---
title: 'Module: csrc/common/cache_key.cc'
type: catalog
provenance: extracted
module: csrc/common/cache_key.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator<<`(d828ee39d25d73d4).'
  PromotedScalar.GetTensor: PromotedScalar#GetTensor(d2a879f8d515cc4e).
  OpParamCacheKeys.OpParamCacheKeys: OpParamCacheKeys#OpParamCacheKeys(5080e51506028c4b).
  OpParamCacheKeys.GetMapOrDie: OpParamCacheKeys#GetMapOrDie(364e694a406817d).
  OpParamCacheKeys.Builder.operator: OpParamCacheKeys#Builder#`operator*`(61d62bb95165a778).
  EncodeParamCacheKey: internal/EncodeParamCacheKey(921ce6aae4789335).
  PromotedScalar.AvoidPromoting: PromotedScalar#AvoidPromoting(fb36cd3c4b3473d7).
  PadModuleCacheKey: PadModuleCacheKey(6dbe1db46c542ce1).
  ParseNextArgName: internal/ParseNextArgName(81fda34fd2fd2470).
  SliceModuleCacheKey: SliceModuleCacheKey(6f6f3c9f9f237c1b).
  MaybePromotedScalar.IsOne: MaybePromotedScalar#IsOne(50ce9a9e25b4a850).
  MaybePromotedScalar.GetTensor: MaybePromotedScalar#GetTensor(d2a879f8d515cc4e).
  OpParamCacheKeys.operator: OpParamCacheKeys#`operator=`(6a63f44372525f00).
  CompilationCacheKey.CompactFormat: CompilationCacheKey#CompactFormat(219584694fe2b248).
  MaybePromotedScalar.IsZero: MaybePromotedScalar#IsZero(50ce9a9e25b4a850).
  GraphSignature.GetKey: GraphSignature#GetKey(fcf3d970d7b15416).
  GraphSignature.AddOp: GraphSignature#AddOp(ced8e9527fdda64a).
  ShapeDynamismMetadata.GetSliceModuleCacheKey: ShapeDynamismMetadata#GetSliceModuleCacheKey(caeb14d99f82eee0).
  GraphSignature.AddInput: GraphSignature#AddInput(a2cd56d9c9c3db81).
  PromotedScalar.PromotedScalar: PromotedScalar#PromotedScalar(56134589ee570a17).
  GraphSignature.AddGraphOutput: GraphSignature#AddGraphOutput(d4f767463ce0a6b3).
  MaybePromotedScalar.MatchesAny: MaybePromotedScalar#MatchesAny(398f3bf45272d0aa).
  GraphSignature.OpSignatureBuilder.AddOutput: GraphSignature#OpSignatureBuilder#AddOutput(a2cd56d9c9c3db81).
  MaybePromotedScalar.IsMinusOne: MaybePromotedScalar#IsMinusOne(50ce9a9e25b4a850).
  MaybePromotedScalar.MaybePromotedScalar: MaybePromotedScalar#MaybePromotedScalar(f54ffd3f3f7faf0).
  DimensionsKey.DimensionsKey: DimensionsKey#DimensionsKey(5ef8d89b44f30208).
  GraphSignature.OpSignatureBuilder.AddInput: GraphSignature#OpSignatureBuilder#AddInput(d4f767463ce0a6b3).
  ShapeDynamismMetadata.ShapeDynamismMetadata: ShapeDynamismMetadata#ShapeDynamismMetadata(203bfe42f335152a).
  GraphSignature.AddTensor: GraphSignature#AddTensor(a2cd56d9c9c3db81).
  AppendPromotedScalarPointers: internal/AppendPromotedScalarPointers(faaaf3da27faa4c6).
  ShapeDynamismMetadata.IsStaticShapeCompatible: ShapeDynamismMetadata#IsStaticShapeCompatible(d20d9c3a58161887).
  MaybePromotedScalar.ToString: MaybePromotedScalar#ToString(219584694fe2b248).
  PromotedScalar.ToString: PromotedScalar#ToString(219584694fe2b248).
  GetUpperBounds: GetUpperBounds(f5437f001541a286).
  IsShapeCompatibleWithBounds: '`$anonymous_namespace_csrc/common/cache_key.cc`/IsShapeCompatibleWithBounds(a16c48016e42c01f).'
  LogShapes: LogShapes(eb24398db08fb71b).
  IsScalarEqualTo: internal/IsScalarEqualTo(3d64784abdf3679f).
---
# Module: [`csrc/common/cache_key.cc`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc)

## Functions
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const MaybePromotedScalar& arg)` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L173)
- <a id="AppendPromotedScalarPointers"></a>`AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const MaybePromotedScalar& arg)` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L173)
- `EncodeParamCacheKey(const at::Device value)` — [`L129`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L129)
- <a id="EncodeParamCacheKey"></a>`EncodeParamCacheKey(const std::string_view value)` — [`L96`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L96) — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)
- `EncodeParamCacheKey(const at::Layout value)` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L121)
- `EncodeParamCacheKey(const at::MemoryFormat value)` — [`L125`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L125)
- `EncodeParamCacheKey(const c10::SymInt& value)` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L83) — We don't return a FingerprintType, as the SymInt may be symbolic instead of
- `EncodeParamCacheKey(const at::Scalar value)` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L63) — EncodeParamCacheKey() is a family of function templates and overloads that
- `EncodeParamCacheKey(const MaybePromotedScalar& value)` — [`L100`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L100)
- `EncodeParamCacheKey(c10::SymIntArrayRef value)` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L87)
- `EncodeParamCacheKey(const c10d::ReduceOp value)` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L91) — We return a stable string as the enum value is not guaranteed to be stable
- `EncodeParamCacheKey(const absl::Span<const int64_t> value)` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L117)
- <a id="GetUpperBounds"></a>`GetUpperBounds(absl::Span<const DimensionBounds> bounds)` — [`L301`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L301)
- <a id="IsScalarEqualTo"></a>`IsScalarEqualTo(const at::Scalar& scalar, const int value)` — [`L160`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L160)
- <a id="IsShapeCompatibleWithBounds"></a>`IsShapeCompatibleWithBounds(const Shape& shape, absl::Span<const DimensionBounds> bounds)` — [`L342`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L342)
- <a id="LogShapes"></a>`LogShapes(absl::Span<const Shape> shapes, std::string_view prefix)` — [`L406`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L406)
- <a id="PadModuleCacheKey"></a>`PadModuleCacheKey(absl::Span<const Shape> dynamic_shapes, bool pad_only_module)` — [`L413`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L413) — Returns a cache key for the pad module for the given input dynamic shapes. — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)
- <a id="ParseNextArgName"></a>`ParseNextArgName(std::string_view& args_str)` — [`L131`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L131) — Returns the name of the next argument in the given substring of a
- <a id="SliceModuleCacheKey"></a>`SliceModuleCacheKey(absl::Span<const Dimensions> target_shapes, absl::Span<const Dimensions> padded_shapes, absl::Span<const mlir::ElementType> element_types)` — [`L466`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L466) — Returns a cache key for the slice module with the given target and padded — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- <a id="operator"></a>`operator<<(std::ostream& os, const CompilationCacheKey& key)` — [`L276`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L276) — Formats a compilation cache key as a human-readable string. — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)

## Other members
- `AvoidPromoting` — [`L200`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L200)
- `MaybePromotedScalar` — [`L221`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L221) — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)
- `GetMapOrDie` — [`L378`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L378)
- <a id="CompilationCacheKey.CompactFormat"></a>`CompilationCacheKey.CompactFormat` — [`L265`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L265)
- <a id="DimensionsKey.DimensionsKey"></a>`DimensionsKey.DimensionsKey` — [`L285`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L285) — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)
- <a id="GraphSignature.AddGraphOutput"></a>`GraphSignature.AddGraphOutput` — [`L606`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L606)
- <a id="GraphSignature.AddInput"></a>`GraphSignature.AddInput` — [`L548`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L548)
- <a id="GraphSignature.AddOp"></a>`GraphSignature.AddOp` — [`L570`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L570)
- <a id="GraphSignature.AddTensor"></a>`GraphSignature.AddTensor` — [`L537`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L537)
- <a id="GraphSignature.GetKey"></a>`GraphSignature.GetKey` — [`L610`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L610)
- <a id="GraphSignature.OpSignatureBuilder.AddInput"></a>`GraphSignature.OpSignatureBuilder.AddInput` — [`L561`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L561)
- <a id="GraphSignature.OpSignatureBuilder.AddOutput"></a>`GraphSignature.OpSignatureBuilder.AddOutput` — [`L565`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L565)
- <a id="MaybePromotedScalar.GetTensor"></a>`MaybePromotedScalar.GetTensor` — [`L242`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L242)
- <a id="MaybePromotedScalar.IsMinusOne"></a>`MaybePromotedScalar.IsMinusOne` — [`L238`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L238)
- <a id="MaybePromotedScalar.IsOne"></a>`MaybePromotedScalar.IsOne` — [`L234`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L234)
- <a id="MaybePromotedScalar.IsZero"></a>`MaybePromotedScalar.IsZero` — [`L230`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L230)
- <a id="MaybePromotedScalar.MatchesAny"></a>`MaybePromotedScalar.MatchesAny` — [`L205`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L205)
- <a id="MaybePromotedScalar.MaybePromotedScalar"></a>`MaybePromotedScalar.MaybePromotedScalar` — [`L225`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L225)
- <a id="MaybePromotedScalar.ToString"></a>`MaybePromotedScalar.ToString` — [`L250`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L250)
- <a id="OpParamCacheKeys.Builder.operator"></a>`OpParamCacheKeys.Builder.operator` — [`L254`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L254)
- <a id="OpParamCacheKeys.GetMapOrDie"></a>`OpParamCacheKeys.GetMapOrDie` — [`L378`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L378)
- <a id="OpParamCacheKeys.OpParamCacheKeys"></a>`OpParamCacheKeys.OpParamCacheKeys` — [`L357`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L357)
- <a id="OpParamCacheKeys.operator"></a>`OpParamCacheKeys.operator` — [`L365`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L365)
- <a id="PromotedScalar.AvoidPromoting"></a>`PromotedScalar.AvoidPromoting` — [`L196`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L196)
- <a id="PromotedScalar.GetTensor"></a>`PromotedScalar.GetTensor` — [`L186`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L186) — documented in [fused-optimizer-kernels](../../../concepts/fused-optimizer-kernels.md)
- <a id="PromotedScalar.PromotedScalar"></a>`PromotedScalar.PromotedScalar` — [`L182`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L182)
- <a id="PromotedScalar.ToString"></a>`PromotedScalar.ToString` — [`L192`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L192)
- <a id="ShapeDynamismMetadata.GetSliceModuleCacheKey"></a>`ShapeDynamismMetadata.GetSliceModuleCacheKey` — [`L506`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L506) — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)
- <a id="ShapeDynamismMetadata.IsStaticShapeCompatible"></a>`ShapeDynamismMetadata.IsStaticShapeCompatible` — [`L385`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L385) — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)
- <a id="ShapeDynamismMetadata.ShapeDynamismMetadata"></a>`ShapeDynamismMetadata.ShapeDynamismMetadata` — [`L310`](../../../../../../raw/code/torch_tpu/csrc/common/cache_key.cc#L310) — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)

