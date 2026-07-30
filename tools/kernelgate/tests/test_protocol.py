"""Module loading, entry resolution, seeded inputs — CPU (imports jax on CPU)."""
import os
import textwrap

import pytest

from kernelgate import protocol

TINY = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "tiny", "n": 8}

def create_inputs(dtype=jnp.float32):
    key = jax.random.key(42)
    k1, k2 = jax.random.split(key)
    return jax.random.normal(k1, (8, 8), dtype), jax.random.normal(k2, (8, 8), dtype)

def workload(a, b):
    return a @ b
'''


@pytest.fixture
def tiny_mod(tmp_path):
    p = tmp_path / "tiny_problem.py"
    p.write_text(textwrap.dedent(TINY))
    return protocol.load_module(str(p))


def test_load_and_config(tiny_mod):
    assert protocol.get_config(tiny_mod)["name"] == "tiny"


def test_entry_default_workload(tiny_mod):
    name, fn = protocol.resolve_entry(tiny_mod, None, 2)
    assert name == "workload"


def test_entry_explicit_missing_raises(tiny_mod):
    with pytest.raises(AttributeError):
        protocol.resolve_entry(tiny_mod, "nope", 2)


def test_seed_monkeypatch_changes_inputs(tiny_mod):
    import numpy as np
    a42, _ = protocol.make_inputs(tiny_mod)          # module-hardcoded seed 42
    a42b, _ = protocol.make_inputs(tiny_mod, seed=42)
    a43, _ = protocol.make_inputs(tiny_mod, seed=43)
    assert np.array_equal(np.asarray(a42), np.asarray(a42b))
    assert not np.array_equal(np.asarray(a42), np.asarray(a43))


def test_seed_restores_jax_random(tiny_mod):
    import jax
    orig = jax.random.key
    protocol.make_inputs(tiny_mod, seed=7)
    assert jax.random.key is orig


def test_seed_param_passed_through(tmp_path):
    p = tmp_path / "seeded_problem.py"
    p.write_text(textwrap.dedent('''
        import jax, jax.numpy as jnp
        CONFIG = {}
        def create_inputs(seed=42, dtype=jnp.float32):
            return (jax.random.normal(jax.random.key(seed), (4,), dtype),)
        def workload(x):
            return x * 2
    '''))
    mod = protocol.load_module(str(p))
    import numpy as np
    (x1,) = protocol.make_inputs(mod, seed=1)
    (x2,) = protocol.make_inputs(mod, seed=2)
    assert not np.array_equal(np.asarray(x1), np.asarray(x2))


def test_hash_arrays_detects_change(tiny_mod):
    inputs = protocol.make_inputs(tiny_mod)
    h1 = protocol.hash_arrays(inputs)
    h2 = protocol.hash_arrays(inputs)
    assert h1 == h2
    changed = (inputs[0] + 1, inputs[1])
    assert protocol.hash_arrays(changed) != h1


def test_sibling_baseline_import(fixtures_dir):
    # paged_6p bad candidate does `import baseline` — must resolve to its
    # sibling file via the loader's sys.path insertion
    mod = protocol.load_module(
        os.path.join(fixtures_dir, "paged_6p", "bad_v003_gqa_aliasing.py"))
    assert protocol.get_config(mod)["num_seqs"] == 64
    name, _ = protocol.resolve_entry(mod, None, 6)
    assert name == "workload"


def test_entry_resolution_on_real_fixtures(fixtures_dir):
    cases = [
        ("flash_1p/good_ag_final.py", 3, "flash_attention"),
        ("flex_5p/good_ag_final.py", 4, "workload_cand"),
        ("paged_6p/good_ag_final.py", 6, "workload"),
        ("sparse_4p/bad_v002_coverage.py", 3, "flash_attn_forward_sparse"),
        ("sparse_4p/bad_v013_double_scale.py", 3, "flash_attn_forward_sparse"),
        ("flex_5p/bad_v005_noncompiling.py", 4, "flex_attention_pallas"),
    ]
    for rel, n, expected in cases:
        mod = protocol.load_module(os.path.join(fixtures_dir, rel))
        name, fn = protocol.resolve_entry(mod, None, n)
        assert name == expected, (rel, name)
        assert callable(fn)


def test_as_jitted_idempotent(tiny_mod):
    import jax
    fn = jax.jit(tiny_mod.workload)
    assert protocol.as_jitted(fn) is fn
    wrapped = protocol.as_jitted(tiny_mod.workload)
    assert wrapped is not tiny_mod.workload
