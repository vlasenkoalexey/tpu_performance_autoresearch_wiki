"""Env capture + roofline math — pure CPU."""
import json

from kernelgate import envinfo, roofline


def test_env_capture_keys():
    info = envinfo.capture(include_devices=False)
    assert "LIBTPU_INIT_ARGS" in info["env"]       # present even when unset (None)
    assert "XLA_FLAGS" in info["env"]
    assert "jax" in info["versions"]
    assert info["python"]
    assert info["hostname"]


def test_env_capture_picks_up_set_vars(monkeypatch):
    monkeypatch.setenv("LIBTPU_INIT_ARGS", "--foo=1 --bar=2")
    monkeypatch.setenv("TPU_VISIBLE_DEVICES", "2")
    info = envinfo.capture(include_devices=False)
    assert info["env"]["LIBTPU_INIT_ARGS"] == "--foo=1 --bar=2"
    assert info["env"]["TPU_VISIBLE_DEVICES"] == "2"


def test_env_capture_json_serializable():
    json.dumps(envinfo.capture(include_devices=False))


def _measure_stub(p50_ms, kind="TPU v6e"):
    return {"env": {"devices": {"kind": kind}},
            "timing": {"pooled": {"candidate": {"p50_ms": p50_ms},
                                  "baseline": {"p50_ms": p50_ms * 2}}}}


def test_roofline_pass():
    # 1e12 flops at 918 TFLOP/s -> bound ~1.089 ms; measured 2 ms is legal
    rep = roofline.run_roofline(_measure_stub(2.0), flops=1e12, bytes_moved=1e6)
    assert rep["status"] == "PASS"
    assert rep["binding_resource"] == "compute"
    assert rep["utilization_pct"] < 100


def test_roofline_invalid_below_light():
    # measured 0.5 ms is faster than the 1.089 ms bound -> INVALID
    rep = roofline.run_roofline(_measure_stub(0.5), flops=1e12, bytes_moved=1e6)
    assert rep["status"] == "INVALID"


def test_roofline_memory_bound():
    # tiny flops, 1 GB moved at 1640 GB/s -> bound 0.61 ms
    rep = roofline.run_roofline(_measure_stub(1.0), flops=1e6, bytes_moved=1e9)
    assert rep["binding_resource"] == "memory"
    assert rep["status"] == "PASS"


def test_roofline_unknown_device_needs_peaks():
    rep = roofline.run_roofline(_measure_stub(1.0, kind="TPU vFuture"),
                                flops=1e12, bytes_moved=1e6)
    assert rep["status"] == "ERROR"
    rep = roofline.run_roofline(_measure_stub(1.0, kind="TPU vFuture"),
                                flops=1e12, bytes_moved=1e6,
                                peak_tflops=100.0, peak_gbps=1000.0)
    assert rep["status"] in ("PASS", "INVALID")


def test_device_peak_lookup():
    assert roofline.peaks_for_device("TPU v5p") == (459.0, 2765.0)
    assert roofline.peaks_for_device("TPU v6e") == (918.0, 1640.0)
    assert roofline.peaks_for_device("TPU v6 lite") == (918.0, 1640.0)
    assert roofline.peaks_for_device(None) is None
