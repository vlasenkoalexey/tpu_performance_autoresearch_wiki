"""Problem-module protocol: loading, entry resolution, seeded inputs, hashing.

A problem module exposes:
  CONFIG          dict (optional on candidates)
  create_inputs   () / (seed=..) / (dtype=..) -> tuple of arrays
  <entry>(*inputs) -> output array or pytree

Entry resolution order (when --entry is not given):
  1. well-known candidate entry names (ENTRY_CANDIDATES, in order)
  2. arity scan: exactly one public module-level callable whose required
     positional parameter count equals len(inputs)
Baseline modules default to entry name "workload".
"""
from __future__ import annotations

import hashlib
import importlib.util
import inspect
import os
import sys

ENTRY_CANDIDATES = (
    "workload_cand",
    "custom_workload",
    "workload_pallas",
    "workload_optimized",
    "optimized_workload",
    "workload",
)

# Exact names never auto-selected as candidate entries.
DENY_NAMES = {
    "workload_naive",
    "naive_workload",
    "reference",
    "computation",
}

DENY_PREFIXES = (
    "create_inputs", "bench", "benchmark", "main", "test", "check",
    "get_", "run_", "make_", "build_", "oracle", "verify", "debug",
    "print_", "plot_", "sweep",
)


def load_module(path: str):
    """Import a problem module from a file path.

    The module's directory is prepended to sys.path so sibling imports
    (`import baseline`) inside candidate modules resolve, mirroring how the
    campaign work dirs are laid out.
    """
    path = os.path.abspath(path)
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    d = os.path.dirname(path)
    if d not in sys.path:
        sys.path.insert(0, d)
    # Sibling-import correctness: a candidate's bare `import baseline` must
    # resolve to THIS module's directory. When several families are loaded in
    # one process, sys.path order / a cached sys.modules["baseline"] from an
    # earlier family would otherwise win silently (wrong CONFIG, wrong
    # semantics). Bind the bare name to the sibling file before exec.
    sibling = os.path.join(d, "baseline.py")
    if os.path.isfile(sibling) and os.path.basename(path) != "baseline.py":
        prev = sys.modules.get("baseline")
        if getattr(prev, "__file__", None) != sibling:
            bspec = importlib.util.spec_from_file_location("baseline", sibling)
            bmod = importlib.util.module_from_spec(bspec)
            sys.modules["baseline"] = bmod
            bspec.loader.exec_module(bmod)
    stem = os.path.splitext(os.path.basename(path))[0]
    name = "kgate_mod_%s_%s" % (hashlib.md5(path.encode()).hexdigest()[:8], stem)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    mod.__kgate_path__ = path
    return mod


def _required_positional(fn) -> int | None:
    try:
        sig = inspect.signature(fn)
    except (TypeError, ValueError):
        return None
    n = 0
    for p in sig.parameters.values():
        if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD) and p.default is p.empty:
            n += 1
        elif p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
            continue
    return n


def resolve_entry(mod, entry_name: str | None = None, n_inputs: int | None = None):
    """Return (name, callable) for the module's compute entry point."""
    if entry_name:
        fn = getattr(mod, entry_name, None)
        if not callable(fn):
            raise AttributeError(
                "module %s has no callable %r" % (getattr(mod, "__kgate_path__", mod), entry_name))
        return entry_name, fn
    for name in ENTRY_CANDIDATES:
        fn = getattr(mod, name, None)
        if callable(fn):
            return name, fn
    # arity scan
    matches = []
    for name, fn in vars(mod).items():
        if name.startswith("_") or not callable(fn) or inspect.isclass(fn):
            continue
        if name in DENY_NAMES or any(name.startswith(p) for p in DENY_PREFIXES):
            continue
        if inspect.ismodule(fn):
            continue
        req = _required_positional(fn)
        if req is None:
            continue
        if n_inputs is not None and req == n_inputs:
            matches.append((name, fn))
    if len(matches) == 1:
        return matches[0]
    raise LookupError(
        "cannot resolve entry point in %s (candidates: %s); pass --entry"
        % (getattr(mod, "__kgate_path__", mod), [m[0] for m in matches]))


# Graded measurement basis: when set (e.g. by the CLI --dtype flag), make_inputs
# passes this dtype to create_inputs whenever the module accepts a dtype param and
# no explicit dtype was given. Pins measurement to the harness's grading dtype
# (bfloat16 for JAXBench) — the wave-3 f32-inflation class is prevented here.
GRADED_DTYPE = None


def make_inputs(mod, seed: int | None = None, dtype=None) -> tuple:
    """Call create_inputs, honoring an optional seed override.

    If create_inputs has a `seed` parameter it is passed through. Otherwise
    (the common campaign baselines hardcode jax.random.key(42)) the seed is
    injected by temporarily monkey-patching jax.random.key / PRNGKey for the
    duration of the call — the same technique the campaign verifier scripts
    used for multi-seed parity.
    """
    fn = mod.create_inputs
    sig = inspect.signature(fn)
    kwargs = {}
    if dtype is None:
        dtype = GRADED_DTYPE
    if dtype is not None and "dtype" in sig.parameters:
        kwargs["dtype"] = dtype
    if seed is not None and "seed" in sig.parameters:
        kwargs["seed"] = seed
        return tuple(fn(**kwargs))
    if seed is None:
        return tuple(fn(**kwargs))
    import jax
    orig_key, orig_prng = jax.random.key, jax.random.PRNGKey
    try:
        jax.random.key = lambda s, *a, **k: orig_key(seed, *a, **k)
        jax.random.PRNGKey = lambda s, *a, **k: orig_prng(seed, *a, **k)
        return tuple(fn(**kwargs))
    finally:
        jax.random.key, jax.random.PRNGKey = orig_key, orig_prng


def is_jitted(fn) -> bool:
    return hasattr(fn, "lower") and hasattr(fn, "__wrapped__") or type(fn).__name__ in (
        "PjitFunction", "JitWrapped")


def as_jitted(fn):
    """jax.jit the entry unless it is already a jit-wrapped callable."""
    import jax
    if is_jitted(fn):
        return fn
    return jax.jit(fn)


def hash_arrays(inputs) -> list:
    """md5 of the raw bytes of every array leaf — the input-mutation fence."""
    import numpy as np
    out = []
    for i, x in enumerate(inputs):
        try:
            b = np.asarray(x).tobytes()
        except Exception:
            out.append({"index": i, "md5": None})
            continue
        out.append({"index": i, "md5": hashlib.md5(b).hexdigest()})
    return out


def sha256_arrays(inputs) -> dict:
    """Receipt-grade input digest: per-array sha256 + shapes + a combined hash.

    Deterministic given the same create_inputs + seed (jax.random is
    platform-invariant), so a receipt verifier can regenerate the inputs and
    compare. Combined = sha256 over the concatenated per-array digests.
    """
    import numpy as np
    shapes, digests = [], []
    combined = hashlib.sha256()
    for x in inputs:
        a = np.asarray(x)
        shapes.append("%s%s" % (a.dtype, list(a.shape)))
        d = hashlib.sha256(a.tobytes()).hexdigest()
        digests.append(d)
        combined.update(d.encode())
    return {"shapes": shapes, "sha256": digests, "combined": combined.hexdigest()}


def sha256_output(out) -> str:
    """Single sha256 over all output leaves' raw bytes (host-side)."""
    import numpy as np
    try:
        import jax
        leaves = jax.tree_util.tree_leaves(out)
    except Exception:
        leaves = [out]
    h = hashlib.sha256()
    for leaf in leaves:
        h.update(np.asarray(leaf).tobytes())
    return h.hexdigest()


def poison_buffers(entry, inputs, factor: int = 3):
    """Pre-poison the allocator with NaN buffers shaped like the output.

    Uses jax.eval_shape (no execution) to learn the output pytree, allocates
    `factor` NaN-filled copies, materializes and frees them — so a candidate
    that "inherits" a previous result from reused allocator memory reads NaN
    instead (Sakana memory-reuse class). Returns a JSON-able note.
    """
    import jax
    import jax.numpy as jnp
    try:
        shapes = jax.eval_shape(entry, *inputs)
    except Exception as e:  # eval_shape itself failing is reported, not fatal
        return {"applied": False, "reason": "eval_shape failed: %r" % (e,)}
    leaves = jax.tree_util.tree_leaves(shapes)
    bufs = []
    try:
        for _ in range(factor):
            for leaf in leaves:
                if jnp.issubdtype(leaf.dtype, jnp.floating):
                    bufs.append(jnp.full(leaf.shape, jnp.nan, leaf.dtype))
                else:
                    bufs.append(jnp.full(leaf.shape, jnp.iinfo(leaf.dtype).max
                                         if jnp.issubdtype(leaf.dtype, jnp.integer) else 0,
                                         leaf.dtype))
        jax.block_until_ready(bufs)
        nbytes = sum(int(b.size) * b.dtype.itemsize for b in bufs)
    finally:
        del bufs
    return {"applied": True, "nbytes": nbytes, "copies": factor}


def get_config(mod) -> dict:
    cfg = getattr(mod, "CONFIG", None)
    if isinstance(cfg, dict):
        return {k: (v if isinstance(v, (int, float, str, bool, list)) else str(v))
                for k, v in cfg.items()}
    return {}
