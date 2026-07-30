"""AST static prefilter — pure CPU."""
import os

from kernelgate import lint

TRY_FALLBACK = '''
import jax.numpy as jnp
def workload_cand(q, k, v):
    try:
        return my_kernel(q, k, v)
    except Exception:
        return reference(q, k, v)
'''

CALLS_BASELINE = '''
import baseline
import jax.numpy as jnp
def workload_cand(q, k, v):
    out = baseline.workload(q, k, v)
    return out
'''

BASELINE_FOR_CONFIG_ONLY = '''
import baseline
import jax.numpy as jnp
CONFIG = baseline.CONFIG
def workload_cand(q, k, v):
    return jnp.einsum("bhqd,bhkd->bhqk", q, k)
'''

PASSTHROUGH = '''
def workload_cand(q, k, v):
    return q
'''

PASSTHROUGH_COPY = '''
import jax.numpy as jnp
def workload_cand(q, k, v):
    return q.copy()
'''

CLEAN = '''
import jax
import jax.numpy as jnp
def workload_cand(q, k, v):
    attn = jnp.einsum("bhqd,bhkd->bhqk", q, k)
    return jnp.einsum("bhqk,bhkd->bhqd", jax.nn.softmax(attn, axis=-1), v)
'''


def codes(rep):
    return {f["code"] for f in rep["findings"]}


def test_try_except_flagged():
    rep = lint.lint_source(TRY_FALLBACK)
    assert "L1" in codes(rep)
    assert rep["status"] == "FINDINGS"


def test_baseline_workload_call_flagged():
    rep = lint.lint_source(CALLS_BASELINE)
    assert "L2" in codes(rep)
    assert rep["status"] == "FINDINGS"


def test_baseline_import_for_config_is_info_only():
    rep = lint.lint_source(BASELINE_FOR_CONFIG_ONLY)
    assert "L2" not in codes(rep)
    assert "L2-info" in codes(rep)
    assert rep["status"] == "CLEAN"  # INFO does not set FINDINGS


def test_passthrough_flagged():
    for src in (PASSTHROUGH, PASSTHROUGH_COPY):
        rep = lint.lint_source(src)
        assert "L3" in codes(rep)


def test_no_compute_flagged():
    rep = lint.lint_source(PASSTHROUGH)
    assert "L4" in codes(rep)


def test_clean_module_clean():
    rep = lint.lint_source(CLEAN)
    assert rep["status"] == "CLEAN"
    assert not codes(rep) - {"L2-info"}


def test_syntax_error_is_reported_not_raised():
    rep = lint.lint_source("def broken(:\n")
    assert rep["status"] == "ERROR"


def test_real_good_fixture_is_clean(fixtures_dir):
    rep = lint.run_lint(os.path.join(fixtures_dir, "flex_5p", "good_ag_final.py"))
    warns = [f for f in rep["findings"] if f["level"] == "WARN"]
    assert not warns, warns


def test_real_aliasing_fixture_gets_info_for_baseline_import(fixtures_dir):
    rep = lint.run_lint(os.path.join(fixtures_dir, "paged_6p", "bad_v003_gqa_aliasing.py"))
    # imports baseline (for CONFIG) but must not be flagged as calling workload
    # from the compute path — its exploit class is aliasing, invisible to lint
    assert "L2-info" in codes(rep)
    assert "L2" not in codes(rep)
