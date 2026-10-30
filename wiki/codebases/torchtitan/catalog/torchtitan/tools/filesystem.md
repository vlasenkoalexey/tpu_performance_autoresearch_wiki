---
title: 'Module: torchtitan/tools/filesystem.py'
type: catalog
provenance: extracted
module: torchtitan/tools/filesystem.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.tools.filesystem`/
symbols:
  join: join().
  is_remote: is_remote().
  isdir: isdir().
  isfile: isfile().
  listdir: listdir().
  rmtree: rmtree().
  _resolve: _resolve().
  exists: exists().
---
# Module: [`torchtitan/tools/filesystem.py`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py)

## Functions
- <a id="_resolve"></a>`_resolve(path: str | os.PathLike)` — [`L31`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py#L31) — Return ``(fs, path)`` for a remote URI via fsspec.
- <a id="exists"></a>`exists(path: str | os.PathLike)` — [`L43`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py#L43)
- <a id="is_remote"></a>`is_remote(path: str | os.PathLike)` — [`L22`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py#L22) — Whether ``path`` is a remote fsspec URI rather than a local path. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="isdir"></a>`isdir(path: str | os.PathLike)` — [`L50`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py#L50) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="isfile"></a>`isfile(path: str | os.PathLike)` — [`L57`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py#L57) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="join"></a>`join(base: str | os.PathLike, name: str)` — [`L101`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py#L101) — Join ``base`` and ``name``, mirroring ``os.path.join`` for local paths. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="listdir"></a>`listdir(path: str | os.PathLike)` — [`L64`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py#L64) — List directory entries as basenames, matching ``os.listdir``. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="rmtree"></a>`rmtree(path: str | os.PathLike)` — [`L87`](../../../../../../raw/code/torchtitan/torchtitan/tools/filesystem.py#L87)

