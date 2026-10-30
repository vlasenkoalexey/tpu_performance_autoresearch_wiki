---
title: 'Module: csrc/ops/scaled_dot_product_attention/util.cc'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/util.cc
status: fresh
symbol_base: cxx . . $ mlir/torch_tpu/
symbols:
  ScaleValue: ScaleValue(b66d0a62d94fd0bb).
  CreateKVWindowMaps: CreateKVWindowMaps(79a29cf3c6c47dc2).
  StoreTile: StoreTile(69cd25ada4c49aa1).
  ConvertElementType: ConvertElementType(c387cb747f3b1cf8).
  StoreTileSlice: StoreTileSlice(12da7e0784a8b17a).
  LoadTile: LoadTile(525e7924adb93f5d).
  BuildDropoutKeepMask: BuildDropoutKeepMask(94776475dbb3d7a7).
  SplatConstant: SplatConstant(5ae026241652c840).
  NormalizeLaneDim: NormalizeLaneDim(cc7bc65b6e84da6c).
  SplatNegInf: SplatNegInf(5de2fd3a708522fe).
  CreateSymbolTransformIndicesAttr: CreateSymbolTransformIndicesAttr(6f9f5d4b5a6457f5).
  GetOpString: GetOpString(bb2fe6a5bcd674ce).
  ApplyStructuredMask: ApplyStructuredMask(9d3e2d53401e742c).
  AppendScalarPrefetchTypes: AppendScalarPrefetchTypes(7223415c39b2107a).
  LoadTileSlice: LoadTileSlice(ffe533c7a2efd710).
  ZeroTile: ZeroTile(ff647ae7fab680f).
  SetScalarPrefetchAttr: SetScalarPrefetchAttr(c044bfd380bed518).
  NInfTile: NInfTile(ff647ae7fab680f).
  CreateBelowOrOnDiagCondition: CreateBelowOrOnDiagCondition(8a56d35cce0de705).
  CreateCausalIfOp: CreateCausalIfOp(76384ab0acce9d17).
  CreateReductionInitValue: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/util.cc`/CreateReductionInitValue(fcf8bffbea6487f1).'
  CreateIntersectsDiagCondition: CreateIntersectsDiagCondition(8a56d35cce0de705).
  NeedsPadMask: NeedsPadMask(85e97fb2cd3859e7).
  ClampMinFinite: ClampMinFinite(a47e99fbf7f93d66).
  ReduceBroadcastLane: ReduceBroadcastLane(854003a55f2ee44b).
  CreateLog2: CreateLog2(a47e99fbf7f93d66).
  TileIndices: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/util.cc`/TileIndices(6ce82c1c7bd65978).'
---
# Module: [`csrc/ops/scaled_dot_product_attention/util.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc)

## Functions
- <a id="AppendScalarPrefetchTypes"></a>`AppendScalarPrefetchTypes(MLIRContext* context, const FlashAttnConfig& config, SmallVectorImpl<Type>& types)` — [`L422`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L422) — Appends the `scalar_prefetch` operand types for `config` to `types`.
- `AppendScalarPrefetchTypes(MLIRContext* context, const FlashAttnConfig& config, SmallVectorImpl<Type>& types)` — [`L422`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L422) — Appends the `scalar_prefetch` operand types for `config` to `types`.
- <a id="ApplyStructuredMask"></a>`ApplyStructuredMask(ImplicitLocOpBuilder& b, Value sij, Value row_block_idx, Value col_block_idx, int64_t qt, int64_t kt, int64_t q_seq_len, int64_t kv_seq_len, bool is_causal, int64_t row_offset, int64_t col_offset)` — [`L204`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L204) — Apply structured masking (causal and/or sequence boundary masking) to `sij`.
- <a id="BuildDropoutKeepMask"></a>`BuildDropoutKeepMask(ImplicitLocOpBuilder& b, const FlashAttnConfig& config, int64_t qt, int64_t kt, Value batch_idx, Value head_idx, Value row_block_idx, Value col_block_idx, Value seed_smem, int64_t row_offset, int64_t col_offset, int64_t rows, int64_t cols)` — [`L503`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L503) — Builds a stateless, tile-size-invariant dropout mask of type
- `BuildDropoutKeepMask(ImplicitLocOpBuilder& b, const FlashAttnConfig& config, int64_t qt, int64_t kt, Value batch_idx, Value head_idx, Value row_block_idx, Value col_block_idx, Value seed_smem, int64_t row_offset, int64_t col_offset, int64_t rows, int64_t cols)` — [`L503`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L503) — Builds a stateless, tile-size-invariant dropout mask of type
- <a id="ClampMinFinite"></a>`ClampMinFinite(ImplicitLocOpBuilder& b, Value input)` — [`L322`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L322) — Clamp the given value to the minimum finite value.
- <a id="ConvertElementType"></a>`ConvertElementType(ImplicitLocOpBuilder& b, Type target_element_type, Value input)` — [`L365`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L365) — Cast the input value element type to the given target type.
- <a id="CreateBelowOrOnDiagCondition"></a>`CreateBelowOrOnDiagCondition(ImplicitLocOpBuilder& b, Value row_idx, Value col_idx, int64_t row_block_size, int64_t col_block_size)` — [`L334`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L334) — Returns an i1 condition indicating whether the tile at (row_idx, col_idx)
- `CreateCausalIfOp(ImplicitLocOpBuilder& b, Value row_idx, Value col_idx, int64_t row_block_size, int64_t col_block_size)` — [`L352`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L352) — Create an scf.IfOp where the then block will be executed when
- <a id="CreateCausalIfOp"></a>`CreateCausalIfOp(ImplicitLocOpBuilder& b, Value row_idx, Value col_idx, int64_t row_block_size, int64_t col_block_size)` — [`L352`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L352) — Create an scf.IfOp where the then block will be executed when
- <a id="CreateIntersectsDiagCondition"></a>`CreateIntersectsDiagCondition(ImplicitLocOpBuilder& b, Value row_idx, Value col_idx, int64_t row_block_size, int64_t col_block_size)` — [`L279`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L279) — Returns an i1 condition indicating whether the tile at (row_idx, col_idx)
- `CreateKVWindowMaps(OpBuilder& builder, func::FuncOp fn, const FlashAttnConfig& config, const Tiling& tiling)` — [`L440`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L440) — Creates the KV window maps (k_map and v_map) for MHA, GQA, or MQA.
- <a id="CreateKVWindowMaps"></a>`CreateKVWindowMaps(OpBuilder& builder, func::FuncOp fn, const FlashAttnConfig& config, const Tiling& tiling)` — [`L440`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L440) — Creates the KV window maps (k_map and v_map) for MHA, GQA, or MQA.
- <a id="CreateLog2"></a>`CreateLog2(ImplicitLocOpBuilder& b, Value input)` — [`L499`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L499) — Create a log2 operation.
- <a id="CreateReductionInitValue"></a>`CreateReductionInitValue(ImplicitLocOpBuilder& b, FloatType element_type, ArrayRef<int64_t> shape, vector::CombiningKind kind)` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L57)
- `CreateReductionInitValue(ImplicitLocOpBuilder& b, FloatType element_type, ArrayRef<int64_t> shape, vector::CombiningKind kind)` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L57)
- <a id="CreateSymbolTransformIndicesAttr"></a>`CreateSymbolTransformIndicesAttr(Builder& builder, llvm::StringRef function_name, llvm::ArrayRef<int64_t> window_bounds)` — [`L410`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L410)
- <a id="GetOpString"></a>`GetOpString(Operation* op)` — [`L102`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L102) — Get the string representation of an operation.
- <a id="LoadTile"></a>`LoadTile(ImplicitLocOpBuilder& b, Value arg)` — [`L148`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L148) — Load a 2D tile from the given argument.
- `LoadTile(ImplicitLocOpBuilder& b, Value arg)` — [`L148`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L148) — Load a 2D tile from the given argument.
- `LoadTileSlice(ImplicitLocOpBuilder& b, Value arg, int64_t row_offset, int64_t num_rows, int64_t col_offset, int64_t num_cols)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L130) — Load the [num_rows, num_cols] sub-tile of the given argument starting at
- <a id="LoadTileSlice"></a>`LoadTileSlice(ImplicitLocOpBuilder& b, Value arg, int64_t row_offset, int64_t num_rows, int64_t col_offset, int64_t num_cols)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L130) — Load the [num_rows, num_cols] sub-tile of the given argument starting at
- <a id="NInfTile"></a>`NInfTile(ImplicitLocOpBuilder& b, Value arg)` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L187) — Initialize a 2D tile with -inf.
- <a id="NeedsPadMask"></a>`NeedsPadMask(int64_t qt, int64_t kt, int64_t q_seq_len, int64_t kv_seq_len)` — [`L199`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L199) — Whether any sequence boundary masking is required for the given
- <a id="NormalizeLaneDim"></a>`NormalizeLaneDim(ImplicitLocOpBuilder& builder, Value input, int64_t target_lane_size)` — [`L387`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L387) — Normalizes the lane dimension of the input vector.
- <a id="ReduceBroadcastLane"></a>`ReduceBroadcastLane(ImplicitLocOpBuilder& b, Value input, vector::CombiningKind kind, int64_t broadcast_lane_size)` — [`L299`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L299) — Reduce the 2D input to a 1D across the lane dimension and then broadcast the
- `ReduceBroadcastLane(ImplicitLocOpBuilder& b, Value input, vector::CombiningKind kind, int64_t broadcast_lane_size)` — [`L299`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L299) — Reduce the 2D input to a 1D across the lane dimension and then broadcast the
- <a id="ScaleValue"></a>`ScaleValue(ImplicitLocOpBuilder& b, Value input, float scale)` — [`L360`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L360) — Scale the input vector by the given scale factor. — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- `SetScalarPrefetchAttr(const FlashAttnConfig& config, func::FuncOp fn, OpBuilder& builder)` — [`L432`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L432) — Sets the `scalar_prefetch` attribute on `fn`, if `config` needs one.
- <a id="SetScalarPrefetchAttr"></a>`SetScalarPrefetchAttr(const FlashAttnConfig& config, func::FuncOp fn, OpBuilder& builder)` — [`L432`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L432) — Sets the `scalar_prefetch` attribute on `fn`, if `config` needs one.
- <a id="SplatConstant"></a>`SplatConstant(ImplicitLocOpBuilder& b, Type type, float value)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L115) — Creates a constant vector with all elements set to `value`.
- `SplatConstant(ImplicitLocOpBuilder& b, ShapedType type, Attribute value_attr)` — [`L110`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L110)
- `SplatConstant(ImplicitLocOpBuilder& b, ShapedType type, Attribute value_attr)` — [`L110`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L110)
- <a id="SplatNegInf"></a>`SplatNegInf(ImplicitLocOpBuilder& b, Type type)` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L121) — Creates a constant vector with all elements set to -infinity.
- <a id="StoreTile"></a>`StoreTile(ImplicitLocOpBuilder& b, Value value, Value arg)` — [`L175`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L175) — Store a 2D tile to the given argument.
- <a id="StoreTileSlice"></a>`StoreTileSlice(ImplicitLocOpBuilder& b, Value value, Value arg, int64_t row_offset, int64_t col_offset)` — [`L154`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L154) — Store a 2D value at (row_offset, col_offset) of the trailing 2D tile of the
- `TileIndices(ImplicitLocOpBuilder& b, MemRefType arg_type, int64_t row_offset, int64_t col_offset)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L80) — Returns the indices for a load / store of the trailing 2D tile of `arg`
- <a id="TileIndices"></a>`TileIndices(ImplicitLocOpBuilder& b, MemRefType arg_type, int64_t row_offset, int64_t col_offset)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L80) — Returns the indices for a load / store of the trailing 2D tile of `arg`
- <a id="ZeroTile"></a>`ZeroTile(ImplicitLocOpBuilder& b, Value arg)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.cc#L179) — Initialize a 2D tile with zeros.

