---
title: 'Module: csrc/common/unique_file_descriptor.h'
type: catalog
provenance: extracted
module: csrc/common/unique_file_descriptor.h
status: fresh
symbol_base: cxx . . $ torch_tpu/UniqueFileDescriptor#
symbols:
  UniqueFileDescriptor.valid: valid(50ce9a9e25b4a850).
  UniqueFileDescriptor: ''
  UniqueFileDescriptor.reset: reset(d4f767463ce0a6b3).
  UniqueFileDescriptor.fd_: fd_.
  UniqueFileDescriptor.UniqueFileDescriptor: UniqueFileDescriptor(d4f767463ce0a6b3).
  UniqueFileDescriptor.get: get(455f465bc33b4cdf).
  UniqueFileDescriptor.operator: '`operator=`(87d6c174a4462945).'
  UniqueFileDescriptor.release: release(b126dc7c1de90089).
  UniqueFileDescriptor.-UniqueFileDescriptor: '`~UniqueFileDescriptor`(ced63f7c635d850d).'
  UniqueFileDescriptor.kInvalidFd: kInvalidFd.
---
# Module: [`csrc/common/unique_file_descriptor.h`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h)

## Classes
### <a id="UniqueFileDescriptor"></a>`UniqueFileDescriptor`
- def: [`csrc/common/unique_file_descriptor.h:27`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L27)
- doc: RAII class for managing a file descriptor. A UniqueFileDescriptor object
- signature: `class UniqueFileDescriptor`
- members:
  - `UniqueFileDescriptor(const UniqueFileDescriptor&)` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L38) — The class is not copyable but movable.
  - <a id="UniqueFileDescriptor.UniqueFileDescriptor"></a>`UniqueFileDescriptor(const int fd = kInvalidFd)` — [`L32`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L32) — Takes ownership of the given file descriptor.
  - `UniqueFileDescriptor(UniqueFileDescriptor&& other)` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L40)
  - <a id="UniqueFileDescriptor.get"></a>`get()` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L49) — Returns the underlying file descriptor without releasing ownership.
  - <a id="UniqueFileDescriptor.operator"></a>`operator=(UniqueFileDescriptor&& other)` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L41)
  - `operator=(const UniqueFileDescriptor&)` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L39)
  - <a id="UniqueFileDescriptor.release"></a>`release()` — [`L52`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L52) — Releases ownership of the file descriptor.
  - <a id="UniqueFileDescriptor.reset"></a>`reset(const int fd = kInvalidFd)` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L63) — Sets the file descriptor to the given value. The existing file descriptor
  - <a id="UniqueFileDescriptor.valid"></a>`valid()` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L59) — Returns true if the file descriptor is valid.
  - <a id="UniqueFileDescriptor.-UniqueFileDescriptor"></a>`~UniqueFileDescriptor()` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L35) — Closes the file descriptor if it is valid.
  - <a id="UniqueFileDescriptor.fd_"></a>`fd_` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L72)
  - <a id="UniqueFileDescriptor.kInvalidFd"></a>`kInvalidFd` — [`L29`](../../../../../../raw/code/torch_tpu/csrc/common/unique_file_descriptor.h#L29)
- used by: [`Make`](tier2_compilation_cache.cc.md#MappedCacheEntry.Make), [`Tier2CacheEntryLock`](tier2_compilation_cache.cc.md#Tier2CacheEntryLock.Tier2CacheEntryLock), [`TestBody`](tier2_compilation_cache_test.cc.md#Tier2CacheEntryLockTest_DoesNotCreateLockFileIfItExists_Test.TestBody), [`Release`](tier2_compilation_cache.cc.md#Tier2CacheEntryLock.Release), [`ReadFile`](tier2_compilation_cache_test.cc.md#ReadFile), [`key_`](tier2_compilation_cache.h.md#Tier2CacheEntryLock.key_)

