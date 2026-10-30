---
title: 'Module: csrc/common/to_string.h'
type: catalog
provenance: extracted
module: csrc/common/to_string.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ToString: ToString(41c8a9e84ac56c7e).
  ToString.V: ToString(b1131d58b2f85ca7).V#
  supports_ostream: supports_ostream#
  supports_absl_strcat: supports_absl_strcat#
  supports_tostring_method: supports_tostring_method#
---
# Module: [`csrc/common/to_string.h`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h)

## Classes
### <a id="ToString.V"></a>`ToString.V`
- def: [`csrc/common/to_string.h:186`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L186)
- signature: `using V = typename std::iterator_traits<Iterator>::value_type`
- uses (calls/refs, reference-scoped): [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.cc.md#ToString), [`ToString`](to_string.cc.md#ToString), [`ToString`](to_string.cc.md#ToString), [`ToString`](to_string.cc.md#ToString), [`ToString`](to_string.cc.md#ToString), [`ToString`](to_string.cc.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString), [`ToString`](to_string.h.md#ToString)

### <a id="supports_absl_strcat"></a>`supports_absl_strcat`  ·  implements/extends integral_constant
- def: [`csrc/common/to_string.h:236`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L236)
- doc: Trait: does T support absl::StrCat()?
- signature: `template <typename T, typename = void> struct supports_absl_strcat : std::false_type`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`ToString`](to_string.h.md#ToString)

### <a id="supports_ostream"></a>`supports_ostream`  ·  implements/extends integral_constant
- def: [`csrc/common/to_string.h:244`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L244)
- doc: Trait: does T support operator<<()?
- signature: `template <typename T, typename = void> struct supports_ostream : std::false_type`
- uses (calls/refs, reference-scoped): [`operator<<`](status_builder.h.md#operator), [`operator<<`](status_builder.h.md#operator), [`operator<<`](../ops/view_decomposition/strided_layout.cc.md#operator), [`operator<<`](../distributed/types.cc.md#operator), [`operator<<`](../ops/view_decomposition/transpose_primitive.cc.md#operator)
- used by: [`ToString`](to_string.h.md#ToString)

### <a id="supports_tostring_method"></a>`supports_tostring_method`  ·  implements/extends integral_constant
- def: [`csrc/common/to_string.h:252`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L252)
- doc: Trait: does T support .ToString()?
- signature: `template <typename T, typename = void> struct supports_tostring_method : std::false_type`
- used by: [`ToString`](to_string.h.md#ToString)

## Functions
- `ToString(c10::OptionalArrayRef<T> value)` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L124)
- `ToString(const c10::List<T>& list)` — [`L135`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L135)
- `ToString(absl::Span<T> span)` — [`L168`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L168) — Returns a string representation of the given span. Requires the element type
- `ToString(const at::Generator&)` — [`L114`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L114)
- `ToString(const std::pair<T1, T2>& pair)` — [`L208`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L208) — Returns a string representation of the given pair.
- `ToString(const c10::IListRef<T>& list)` — [`L141`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L141)
- <a id="ToString"></a>`ToString(c10::ArrayRef<T> arr)` — [`L130`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L130)
- `ToString(const T& x)` — [`L261`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L261) — The primary ToString() template. It delegates to absl::StrCat(), the
- `ToString(mlir::stablehlo::Precision precision)` — [`L157`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L157)
- `ToString(const c10d::AllreduceOptions& options)` — [`L118`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L118)
- `ToString(const std::unordered_map<K, V>& map)` — [`L227`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L227)
- `ToString(const absl::InlinedVector<T, N>& vec)` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L173)
- `ToString(const std::optional<T>& value)` — [`L198`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L198)
- `ToString(mlir::stablehlo::Precision precision)` — [`L157`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L157)
- `ToString(Iterator begin, Iterator end)` — [`L185`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L185)
- `ToString(const std::vector<T>& vec)` — [`L217`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L217) — Returns a string representation of the given vector. Requires the element
- `ToString(const bool b)` — [`L180`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L180) — /////////////////////////////////////////////////////////////////////////////
- `ToString(const absl::InlinedVector<T, N>& vec)` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L173)
- `ToString(const std::array<T, kSize>& arr)` — [`L222`](../../../../../../raw/code/torch_tpu/csrc/common/to_string.h#L222)

