---
title: 'Module: csrc/common/environment.cc'
type: catalog
provenance: extracted
module: csrc/common/environment.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  InitializeDistributedEnvironment: InitializeDistributedEnvironment(9df54338d187c708).
  InitializeSingleDeviceEnvironment: InitializeSingleDeviceEnvironment(c8a92d17d58c956f).
  ConfigureLibtpuInitArgs: '`$anonymous_namespace_csrc/common/environment.cc`/ConfigureLibtpuInitArgs(6ccff4770ff7ddc3).'
  AssignMegascalePorts: '`$anonymous_namespace_csrc/common/environment.cc`/AssignMegascalePorts(d4f767463ce0a6b3).'
  EnsureUndefokFlag: '`$anonymous_namespace_csrc/common/environment.cc`/EnsureUndefokFlag(cc69e8a11a076049).'
  EnsureLibtpuBoolFlag: '`$anonymous_namespace_csrc/common/environment.cc`/EnsureLibtpuBoolFlag(54f78eb18246ae94).'
  AppendUndefokItem: '`$anonymous_namespace_csrc/common/environment.cc`/AppendUndefokItem(67392fd876b89d96).'
  kMegascaleBasePort: '`$anonymous_namespace_csrc/common/environment.cc`/kMegascaleBasePort.'
---
# Module: [`csrc/common/environment.cc`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc)

## Functions
- <a id="AppendUndefokItem"></a>`AppendUndefokItem(std::string_view item, std::string& undefok_flag)` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L84) — Appends `item` to the comma-separated list in `undefok_flag` (which starts
- <a id="AssignMegascalePorts"></a>`AssignMegascalePorts(const int local_rank)` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L48) — Gives the process with `local_rank` its own MegaScale ports in a multi-slice
- <a id="ConfigureLibtpuInitArgs"></a>`ConfigureLibtpuInitArgs(std::string_view raw_args)` — [`L114`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L114) — Normalizes `LIBTPU_INIT_ARGS` (`raw_args`) for distributed execution by
- <a id="EnsureLibtpuBoolFlag"></a>`EnsureLibtpuBoolFlag(std::string_view flag_prefix, std::string_view bad_flag, std::string_view target_flag, std::string_view warning_message, std::vector<std::string>& flags)` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L62) — Ensures `flags` sets the boolean flag matching `flag_prefix` to
- `EnsureLibtpuBoolFlag(std::string_view flag_prefix, std::string_view bad_flag, std::string_view target_flag, std::string_view warning_message, std::vector<std::string>& flags)` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L62) — Ensures `flags` sets the boolean flag matching `flag_prefix` to
- `EnsureUndefokFlag(std::string_view flag_name, std::vector<std::string>& flags)` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L99) — Ensures `flag_name` is listed in `--undefok` within `flags`, either by
- <a id="EnsureUndefokFlag"></a>`EnsureUndefokFlag(std::string_view flag_name, std::vector<std::string>& flags)` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L99) — Ensures `flag_name` is listed in `--undefok` within `flags`, either by
- <a id="InitializeDistributedEnvironment"></a>`InitializeDistributedEnvironment(const DistributedWorkerConfiguration& config)` — [`L149`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L149) — This function handles the environment initialization for distributed TPU
- <a id="InitializeSingleDeviceEnvironment"></a>`InitializeSingleDeviceEnvironment()` — [`L207`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L207) — Configures the local environment for single-device execution.

## Module values
- <a id="kMegascaleBasePort"></a>`kMegascaleBasePort` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/common/environment.cc#L41) — libtpu's default MegaScale port. Local rank 0 keeps it, so a MegaScale

