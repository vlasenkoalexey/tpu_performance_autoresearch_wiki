"""Compile-only config-fit sweep + OOM-message parsing — pure CPU.

The parse fixtures are verbatim message shapes from campaign incidents:
Mosaic scoped-vmem ("44.05M > 32M", "Ran out of memory in memory space
vmem"), XLA HBM RESOURCE_EXHAUSTED ("Used 34.00G of 30.75G"), and the
byte-count style ("size N exceeds the scoped vmem limit of M").
"""
import json
import textwrap

import pytest

from kernelgate import fit, protocol

MOSAIC_GT = ("Mosaic failed to compile TPU kernel: "
             "Insufficient scoped vmem: 44.05M > 32M")
MOSAIC_RANOUT = ("RESOURCE_EXHAUSTED: XLA:TPU compile permanent error. "
                 "Ran out of memory in memory space vmem. Used 44.05M of 32.00M.")
XLA_HBM = ("RESOURCE_EXHAUSTED: Ran out of memory in memory space hbm. "
           "Used 34.00G of 30.75G.")
SCOPED_BYTES = ("Mosaic scoped allocation with size 45108224 bytes exceeds "
                "the scoped vmem limit of 33554432")


def test_parse_mosaic_gt_style():
    p = fit.parse_oom(MOSAIC_GT)
    assert p["error_class"] == "mosaic_vmem"
    assert p["requested_bytes"] == int(44.05 * 2 ** 20)
    assert p["limit_bytes"] == 32 * 2 ** 20
    assert "44.05M > 32M" in p["raw_line"]


def test_parse_mosaic_ranout_style():
    p = fit.parse_oom(MOSAIC_RANOUT)
    assert p["error_class"] == "mosaic_vmem"
    assert p["requested_bytes"] == int(44.05 * 2 ** 20)
    assert p["limit_bytes"] == 32 * 2 ** 20


def test_parse_xla_hbm_style():
    p = fit.parse_oom(XLA_HBM)
    assert p["error_class"] == "xla_hbm"
    assert p["requested_bytes"] == 34 * 2 ** 30
    assert p["limit_bytes"] == int(30.75 * 2 ** 30)


def test_parse_hlo_temporaries_style():
    # verbatim v6e message shape (captured 2026-07-17 on chip 3)
    p = fit.parse_oom(
        "RESOURCE_EXHAUSTED: Ran out of memory on HBM, the total memory "
        "required for HLO temporaries (64.00G) exceeds available HBM (31.25G).")
    assert p["error_class"] == "xla_hbm"
    assert p["requested_bytes"] == 64 * 2 ** 30
    assert p["limit_bytes"] == int(31.25 * 2 ** 30)


def test_parse_runtime_allocate_style():
    p = fit.parse_oom(
        "RESOURCE_EXHAUSTED: Error allocating device buffer: Attempting to "
        "allocate 64.00G. That was not possible. There are 10.51G free.")
    assert p["error_class"] == "resource_exhausted"
    assert p["requested_bytes"] == 64 * 2 ** 30
    assert p["limit_bytes"] == int(10.51 * 2 ** 30)


def test_parse_scoped_bytecount_style():
    p = fit.parse_oom(SCOPED_BYTES)
    assert p["error_class"] == "mosaic_vmem"
    assert p["requested_bytes"] == 45108224
    assert p["limit_bytes"] == 33554432


def test_parse_non_oom_is_none():
    assert fit.parse_oom("TypeError: unsupported operand type") is None
    assert fit.parse_oom("Mosaic lowering failed: bad block shape") is None


def test_parse_oom_without_numbers_keeps_line():
    p = fit.parse_oom("RESOURCE_EXHAUSTED: Ran out of memory allocating buffers")
    assert p["error_class"] == "resource_exhausted"
    assert p["requested_bytes"] is None
    assert "Ran out of memory" in p["raw_line"]


def test_parse_configs_inline_and_file(tmp_path):
    inline = fit.parse_configs('[{"bq": 512}, {"bq": 1024}]')
    assert inline == [{"bq": 512}, {"bq": 1024}]
    p = tmp_path / "configs.json"
    p.write_text(json.dumps(inline))
    assert fit.parse_configs(str(p)) == inline
    with pytest.raises(ValueError):
        fit.parse_configs('{"not": "a list"}')


# ---------------------------------------------------------------- end-to-end

# The candidate simulates the chip envelope at trace time: configs whose
# footprint exceeds LIMIT raise the verbatim Mosaic scoped-vmem message
# (a real Mosaic OOM surfaces the same way — an exception out of lower/
# compile). Small configs compile for real.
SIZED_CAND = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "sized", "n": 32}

def create_inputs(dtype=jnp.float32):
    key = jax.random.key(42)
    n = CONFIG["n"]
    return (jax.random.normal(key, (n, n), dtype),)

LIMIT_MIB = 32.0

def workload_cand(x, bq=128, bk=128):
    mib = bq * bk * 4 * 8 / 2**20
    if mib > LIMIT_MIB:
        raise RuntimeError(
            "RESOURCE_EXHAUSTED: XLA:TPU compile permanent error. "
            "Ran out of memory in memory space vmem. "
            "Used %.2fM of %.2fM." % (mib, LIMIT_MIB))
    return x * bq + bk
'''


def _mod(tmp_path, name, src):
    p = tmp_path / name
    p.write_text(textwrap.dedent(src))
    return protocol.load_module(str(p))


def test_fit_sweep_parses_ooms_and_never_crashes(tmp_path):
    cand = _mod(tmp_path, "cand_sized.py", SIZED_CAND)
    configs = [{"bq": 128, "bk": 128},    # 0.5 MiB -> fits
               {"bq": 1024, "bk": 1024},  # 32 MiB  -> fits (at limit)
               {"bq": 2048, "bk": 1024},  # 64 MiB  -> OOM
               {"bq": 4096, "bk": 4096}]  # 512 MiB -> OOM
    rep = fit.run_fit(cand, configs)
    assert rep["status"] == "PASS", rep.get("exception")   # sweep survived
    assert rep["n_configs"] == 4
    assert rep["n_fit"] == 2
    rows = {json.dumps(r["config"], sort_keys=True): r for r in rep["rows"]}
    ok = rows['{"bk": 128, "bq": 128}']
    assert ok["fits"] and ok["error_class"] is None
    oom = rows['{"bk": 1024, "bq": 2048}']
    assert not oom["fits"]
    assert oom["error_class"] == "mosaic_vmem"
    assert oom["requested_bytes"] == 64 * 2 ** 20
    assert oom["limit_bytes"] == 32 * 2 ** 20
    assert "Ran out of memory" in oom["raw_line"]


def test_fit_non_oom_error_is_other(tmp_path):
    cand = _mod(tmp_path, "cand_sized2.py", SIZED_CAND)
    rep = fit.run_fit(cand, [{"bq": "not_an_int", "bk": 128}])
    row = rep["rows"][0]
    assert not row["fits"]
    assert row["error_class"] == "other"
    assert row["raw_line"]


def test_fit_tsv_shape(tmp_path):
    cand = _mod(tmp_path, "cand_sized3.py", SIZED_CAND)
    rep = fit.run_fit(cand, [{"bq": 128, "bk": 128}, {"bq": 4096, "bk": 4096}])
    lines = fit.tsv_lines(rep)
    assert lines[0] == "config\tfits\trequested\tlimit\terror_class"
    assert len(lines) == 3
    assert "\ttrue\t" in lines[1]
    assert "\tfalse\t" in lines[2] and "mosaic_vmem" in lines[2]


def test_fit_inputs_from_baseline(tmp_path):
    base = _mod(tmp_path, "baseline.py", SIZED_CAND.replace(
        "def workload_cand(x, bq=128, bk=128):",
        "def workload(x, bq=128, bk=128):"))
    cand = _mod(tmp_path, "cand_sized4.py", SIZED_CAND)
    rep = fit.run_fit(cand, [{"bq": 128, "bk": 128}], baseline_mod=base)
    assert rep["rows"][0]["fits"]
    assert rep["baseline"]["path"].endswith("baseline.py")


def test_non_oom_mosaic_error_is_not_a_vmem_oom():
    """"mosaic" + "vmem" in a traceback is not OOM evidence: the classifier
    used to accept it and the bare "X > Y" rule then mined a shape comparison
    into fabricated requested/limit BYTE counts."""
    text = ("jax._src.source_info_util.JaxStackTraceBeforeTransformation: "
            "TypeError\nMosaic failed to lower the kernel\n"
            "  memory_space=vmem\n  block shape 512 > 256 for the last dim\n")
    assert fit.classify_oom(text) is None
    assert fit.parse_oom(text) is None


def test_oom_token_is_word_bounded():
    """A path or identifier merely containing 'oom' is not an OOM."""
    assert fit.classify_oom(
        'File "/tmp/pytest/test_fit_non_oom_error_is_othe0/c.py", line 15') is None
    assert fit.classify_oom("OOM when allocating tensor") is not None


def test_real_ooms_still_classify_and_parse():
    vmem = "Mosaic error: Not enough VMEM: requested 131072 bytes, limit of 65536"
    assert fit.classify_oom(vmem) == "mosaic_vmem"
    got = fit.parse_oom(vmem)
    assert got["requested_bytes"] == 131072 and got["limit_bytes"] == 65536
    hbm = "RESOURCE_EXHAUSTED: temporaries (64.00G) exceeds available HBM (31.25G)"
    assert fit.classify_oom(hbm) == "xla_hbm"
