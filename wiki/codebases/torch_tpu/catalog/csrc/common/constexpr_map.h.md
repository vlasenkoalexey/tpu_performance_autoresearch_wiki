---
title: 'Module: csrc/common/constexpr_map.h'
type: catalog
provenance: extracted
module: csrc/common/constexpr_map.h
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  ConstexprMap.at: torch_tpu/ConstexprMap#at(d85cdd32efb61893).
  ConstexprMap.contains: torch_tpu/ConstexprMap#contains(52aad8a5ba75b80f).
  ConstexprMap.SortAndValidate: absl/torch_tpu/ConstexprMap#SortAndValidate(49f6e7a06ebc5aa8).
  ConstexprMap.ConstexprMap-Key-Value-kSize-Compare: torch_tpu/ConstexprMap#`ConstexprMap<Key,
    Value, kSize, Compare>`(1c7a8434ed290239).
  ConstexprMap.end: torch_tpu/ConstexprMap#end(a7d475ee38ef3ccf).
  ConstexprMap: torch_tpu/ConstexprMap#
  ConstexprMap.lower_bound: torch_tpu/ConstexprMap#lower_bound(945eaf0deacf4149).
  ConstexprMap.operator: torch_tpu/ConstexprMap#`operator[]`(d85cdd32efb61893).
  ConstexprMap.find: absl/torch_tpu/ConstexprMap#find(945eaf0deacf4149).
  ConstexprMap.begin: torch_tpu/ConstexprMap#begin(a7d475ee38ef3ccf).
  ConstexprMap.empty: torch_tpu/ConstexprMap#empty(77ce49a7840d23c7).
  ConstexprMap.size: torch_tpu/ConstexprMap#size(cee159cc271e827).
  ConstexprMap.KeyLess: torch_tpu/ConstexprMap#KeyLess(da6e4c28b3fc8ed5).
  ConstexprMap.data_: absl/torch_tpu/ConstexprMap#data_.
  ConstexprMap.cbegin: torch_tpu/ConstexprMap#cbegin(a7d475ee38ef3ccf).
  ConstexprMap.comp_: torch_tpu/ConstexprMap#comp_.
  ConstexprMap.Entry: torch_tpu/ConstexprMap#Entry#
  ConstexprMap.KeysEquivalent: torch_tpu/ConstexprMap#KeysEquivalent(da6e4c28b3fc8ed5).
  ConstexprMap.const_iterator: torch_tpu/ConstexprMap#const_iterator#
  MakeConstexprMap: absl/torch_tpu/MakeConstexprMap(cf0abeae90b035fd).
  ConstexprMap.value_type: absl/torch_tpu/ConstexprMap#value_type#
  ConstexprMap.cend: absl/torch_tpu/ConstexprMap#cend(a7d475ee38ef3ccf).
  operator: absl/torch_tpu/`operator==`(637a7d3c6c8abaf1).
  ConstexprMap.iterator: torch_tpu/ConstexprMap#iterator#
  ConstexprMap.Entry.key: torch_tpu/ConstexprMap#Entry#key.
  ConstexprMap.Entry.value: torch_tpu/ConstexprMap#Entry#value.
  ConstexprMap.size_type: torch_tpu/ConstexprMap#size_type#
  ConstexprMap.mapped_type: absl/torch_tpu/ConstexprMap#mapped_type#
  ConstexprMap.key_compare: torch_tpu/ConstexprMap#key_compare#
  ConstexprMap.key_type: absl/torch_tpu/ConstexprMap#key_type#
  ConstexprMap.difference_type: absl/torch_tpu/ConstexprMap#difference_type#
---
# Module: [`csrc/common/constexpr_map.h`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h)

## Classes
### `ConstexprMap`
- def: [`csrc/common/constexpr_map.h:43`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L43)
- doc: A C++20-compliant flat map container with fixed size N that can be evaluated
- signature: `class ConstexprMap`
- members:
  - `ConstexprMap<Key, Value, kSize, Compare>()` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L64) — Constructs an empty map.
  - `ConstexprMap<Key, Value, kSize, Compare>(const value_type (&data)[kSize], Compare comp = Compare())` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L69) — Constructor from C-style array of entries.
  - `ConstexprMap<Key, Value, kSize, Compare>()` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L64) — Constructs an empty map.
  - <a id="ConstexprMap.ConstexprMap-Key-Value-kSize-Compare"></a>`ConstexprMap<Key, Value, kSize, Compare>(const value_type (&data)[kSize], Compare comp = Compare())` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L69) — Constructor from C-style array of entries.
  - `KeyLess(const K1& k1, const K2& k2)` — [`L149`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L149) — Returns true if k1 is less than k2 according to the key comparator.
  - <a id="ConstexprMap.KeyLess"></a>`KeyLess(const K1& k1, const K2& k2)` — [`L149`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L149) — Returns true if k1 is less than k2 according to the key comparator.
  - `KeysEquivalent(const K1& k1, const K2& k2)` — [`L164`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L164) — Returns true if k1 and k2 are equivalent according to the key comparator.
  - <a id="ConstexprMap.KeysEquivalent"></a>`KeysEquivalent(const K1& k1, const K2& k2)` — [`L164`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L164) — Returns true if k1 and k2 are equivalent according to the key comparator.
  - <a id="ConstexprMap.SortAndValidate"></a>`SortAndValidate()` — [`L172`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L172) — Sorts the underlying data and checks for duplicate keys.
  - `SortAndValidate()` — [`L172`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L172) — Sorts the underlying data and checks for duplicate keys.
  - `at(const K& key)` — [`L96`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L96) — Element access
  - <a id="ConstexprMap.at"></a>`at(const K& key)` — [`L96`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L96) — Element access
  - <a id="ConstexprMap.begin"></a>`begin()` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L76) — Iterators
  - `begin()` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L76) — Iterators
  - `cbegin()` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L79)
  - <a id="ConstexprMap.cbegin"></a>`cbegin()` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L79)
  - <a id="ConstexprMap.cend"></a>`cend()` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L86)
  - `cend()` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L86)
  - `contains(const K& key)` — [`L122`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L122) — Returns true if the map contains the given key.
  - <a id="ConstexprMap.contains"></a>`contains(const K& key)` — [`L122`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L122) — Returns true if the map contains the given key.
  - `empty()` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L91) — Capacity
  - <a id="ConstexprMap.empty"></a>`empty()` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L91) — Capacity
  - <a id="ConstexprMap.end"></a>`end()` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L83)
  - `end()` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L83)
  - <a id="ConstexprMap.find"></a>`find(const K& key)` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L112) — Lookup operation.
  - `find(const K& key)` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L112) — Lookup operation.
  - <a id="ConstexprMap.lower_bound"></a>`lower_bound(const K& key)` — [`L136`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L136) — Returns an iterator to the first element in the map whose key is not less
  - `lower_bound(const K& key)` — [`L136`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L136) — Returns an iterator to the first element in the map whose key is not less
  - <a id="ConstexprMap.operator"></a>`operator[](const K& key)` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L106)
  - `operator[](const K& key)` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L106)
  - <a id="ConstexprMap.size"></a>`size()` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L92)
  - `size()` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L92)
  - <a id="ConstexprMap.comp_"></a>`comp_` — [`L188`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L188)
  - `comp_` — [`L188`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L188)
  - <a id="ConstexprMap.data_"></a>`data_` — [`L187`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L187)
  - `data_` — [`L187`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L187)
- uses (calls/refs, reference-scoped): [`ConstexprMap`](constexpr_map.h.md#ConstexprMap), [`Entry`](constexpr_map.h.md#ConstexprMap.Entry), [`Entry`](constexpr_map.h.md#ConstexprMap.Entry), [`const_iterator`](constexpr_map.h.md#ConstexprMap.const_iterator), [`const_iterator`](constexpr_map.h.md#ConstexprMap.const_iterator), [`value_type`](constexpr_map.h.md#ConstexprMap.value_type), [`always_false_v`](utils.h.md#always_false_v), [`key`](constexpr_map.h.md#ConstexprMap.Entry.key), [`key`](constexpr_map.h.md#ConstexprMap.Entry.key), [`size_type`](constexpr_map.h.md#ConstexprMap.size_type), [`size_type`](constexpr_map.h.md#ConstexprMap.size_type), [`value_type`](constexpr_map.h.md#ConstexprMap.value_type), [`always_false_v`](utils.h.md#always_false_v)
- used by: [`GetEnvOnce`](env_vars.h.md#GetEnvOnce), [`kMap`](constexpr_map_test.cc.md#kMap), [`SetEnv`](env_vars.h.md#SetEnv), [`kSingleMap`](constexpr_map_test.cc.md#kSingleMap), [`kEmptyMap`](constexpr_map_test.cc.md#kEmptyMap), [`kSymbolStages`](symbol_stage_test.cc.md#kSymbolStages), [`TestBody`](constexpr_map_test.cc.md#ConstexprMapTest_EmptyMap_Test.TestBody), [`TestBody`](constexpr_map_test.cc.md#ConstexprMapTest_SingleElementMap_Test.TestBody), [`SumValues`](constexpr_map_test.cc.md#SumValues), [`TestBody`](constexpr_map_test.cc.md#ConstexprMapTest_MultiElementLookupAndOrdering_Test.TestBody), [`kDescendingMap`](constexpr_map_test.cc.md#kDescendingMap), [`kFactoryMap`](constexpr_map_test.cc.md#kFactoryMap), [`MakeConstexprMap`](constexpr_map.h.md#MakeConstexprMap)

### `ConstexprMap.Entry`
- def: [`csrc/common/constexpr_map.h:45`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L45)
- signature: `struct Entry`
- members:
  - <a id="ConstexprMap.Entry.key"></a>`key` — [`L46`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L46)
  - `key` — [`L46`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L46)
  - <a id="ConstexprMap.Entry.value"></a>`value` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L47)
  - `value` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L47)
- used by: [`SortAndValidate`](constexpr_map.h.md#ConstexprMap.SortAndValidate), [`SumValues`](constexpr_map_test.cc.md#SumValues), [`lower_bound`](constexpr_map.h.md#ConstexprMap.lower_bound), [`value_type`](constexpr_map.h.md#ConstexprMap.value_type), [`operator==`](constexpr_map.h.md#operator)

### `ConstexprMap.const_iterator`
- def: [`csrc/common/constexpr_map.h:60`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L60)
- signature: `using const_iterator = typename std::array<Entry, kSize>::const_iterator`
- used by: [`ConstexprMap<Key, Value, kSize, Compare>`](constexpr_map.h.md#ConstexprMap.ConstexprMap-Key-Value-kSize-Compare), [`end`](constexpr_map.h.md#ConstexprMap.end), [`contains`](constexpr_map.h.md#ConstexprMap.contains), [`begin`](constexpr_map.h.md#ConstexprMap.begin), [`cbegin`](constexpr_map.h.md#ConstexprMap.cbegin), [`operator[]`](constexpr_map.h.md#ConstexprMap.operator), [`iterator`](constexpr_map.h.md#ConstexprMap.iterator)

### `ConstexprMap.difference_type`
- def: [`csrc/common/constexpr_map.h:58`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L58)
- signature: `using difference_type = std::ptrdiff_t`

### <a id="ConstexprMap.iterator"></a>`ConstexprMap.iterator`
- def: [`csrc/common/constexpr_map.h:61`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L61)
- signature: `using iterator = const_iterator`
- uses (calls/refs, reference-scoped): [`const_iterator`](constexpr_map.h.md#ConstexprMap.const_iterator), [`const_iterator`](constexpr_map.h.md#ConstexprMap.const_iterator)

### `ConstexprMap.key_compare`
- def: [`csrc/common/constexpr_map.h:59`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L59)
- signature: `using key_compare = Compare`

### `ConstexprMap.key_type`
- def: [`csrc/common/constexpr_map.h:54`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L54)
- signature: `using key_type = Key`

### `ConstexprMap.mapped_type`
- def: [`csrc/common/constexpr_map.h:56`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L56)
- signature: `using mapped_type = Value`

### `ConstexprMap.size_type`
- def: [`csrc/common/constexpr_map.h:57`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L57)
- signature: `using size_type = std::size_t`
- used by: [`empty`](constexpr_map.h.md#ConstexprMap.empty)

### `ConstexprMap.value_type`
- def: [`csrc/common/constexpr_map.h:55`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L55)
- signature: `using value_type = Entry`
- used by: [`ConstexprMap<Key, Value, kSize, Compare>`](constexpr_map.h.md#ConstexprMap.ConstexprMap-Key-Value-kSize-Compare)

## Functions
- <a id="MakeConstexprMap"></a>`MakeConstexprMap(const typename ConstexprMap<Key, Value, kSize, Compare>::value_type (&entries)[kSize], Compare comp = Compare())` — [`L195`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L195) — Factory function.
- `MakeConstexprMap(const typename ConstexprMap<Key, Value, kSize, Compare>::value_type (&entries)[kSize], Compare comp = Compare())` — [`L195`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L195) — Factory function.
- `operator==(const Entry& lhs, const Entry& rhs)` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L49)
- <a id="operator"></a>`operator==(const Entry& lhs, const Entry& rhs)` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/common/constexpr_map.h#L49)

