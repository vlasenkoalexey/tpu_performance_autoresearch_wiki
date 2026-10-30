---
title: 'Module: csrc/eager/device_gen_impl.cc'
type: catalog
provenance: extracted
module: csrc/eager/device_gen_impl.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  EagerModeDeviceGeneratorImpl.set_offset: EagerModeDeviceGeneratorImpl#set_offset(2c44cd906ae4e829).
  EagerModeDeviceGeneratorImpl.set_current_seed: EagerModeDeviceGeneratorImpl#set_current_seed(2c44cd906ae4e829).
  EagerModeDeviceGeneratorImpl.seed: EagerModeDeviceGeneratorImpl#seed(f708dce9a8856c70).
  DeviceGeneratorImplBase.AdvanceDeviceStateTensor: DeviceGeneratorImplBase#AdvanceDeviceStateTensor(9c481cfad9b52b43).
  GetDefaultDeviceGenerator: GetDefaultDeviceGenerator(2279cd5805a18fe0).
  DeviceGeneratorState.MaybeMaterializeDeviceStateTensor: DeviceGeneratorState#MaybeMaterializeDeviceStateTensor(fb227b7b046ca026).
  DeviceGenerators.GetDefaultInstance: DeviceGenerators#GetDefaultInstance(47d9700d385480da).
  DeviceGenerators.GetDefaultGenerator: DeviceGenerators#GetDefaultGenerator(2279cd5805a18fe0).
  EagerModeDeviceGeneratorImpl.set_state: EagerModeDeviceGeneratorImpl#set_state(9ea24e05089f324f).
  DeviceGenerators.SetExportModeDefaultGenerator: DeviceGenerators#SetExportModeDefaultGenerator(9c6e79db8d64cf03).
  DeviceGeneratorImplBase.ValidateDeviceStateTensor: DeviceGeneratorImplBase#ValidateDeviceStateTensor(9d75f6569b0a4113).
  NormalizeDeviceIndex: '`$anonymous_namespace_csrc/eager/device_gen_impl.cc`/NormalizeDeviceIndex(f19b2f157e840411).'
  ExportModeDeviceGeneratorImpl.graphsafe_set_state: ExportModeDeviceGeneratorImpl#graphsafe_set_state(794bbbca577513a2).
  EagerModeDeviceGeneratorImpl.graphsafe_set_state: EagerModeDeviceGeneratorImpl#graphsafe_set_state(794bbbca577513a2).
  DeviceGenerators.GetEagerDefaultGenerator: DeviceGenerators#GetEagerDefaultGenerator(2279cd5805a18fe0).
  ExportModeDeviceGeneratorImpl.ExportModeDeviceGeneratorImpl: ExportModeDeviceGeneratorImpl#ExportModeDeviceGeneratorImpl(af5458c3908b1978).
  UpdateDeviceRngState: '`$anonymous_namespace_csrc/eager/device_gen_impl.cc`/UpdateDeviceRngState(25154e0d7e4a6c69).'
  ValidateAndGetEagerBase: '`$anonymous_namespace_csrc/eager/device_gen_impl.cc`/ValidateAndGetEagerBase(eeefcae2507a9ac9).'
  InitDefaultGenerator: InitDefaultGenerator(aee1df1ca83d83bc).
  DeviceGeneratorState.WriteStateToDevice: DeviceGeneratorState#WriteStateToDevice(dda50a5212c4f7e5).
  EagerModeDeviceGeneratorImpl.EagerModeDeviceGeneratorImpl: EagerModeDeviceGeneratorImpl#EagerModeDeviceGeneratorImpl(f4683923fcb3d21f).
  DeviceGeneratorState.SetDeviceStateTensor: DeviceGeneratorState#SetDeviceStateTensor(e861d53347b2ff40).
  EagerModeDeviceGeneratorImpl.SetDeviceStateTensor: EagerModeDeviceGeneratorImpl#SetDeviceStateTensor(e861d53347b2ff40).
  DeviceGeneratorState.clone: DeviceGeneratorState#clone(f3f69472d1666529).
  ExportModeDeviceGeneratorImpl.SetDeviceStateTensor: ExportModeDeviceGeneratorImpl#SetDeviceStateTensor(e861d53347b2ff40).
  CreateDeviceRngStateTensor: '`$anonymous_namespace_csrc/eager/device_gen_impl.cc`/CreateDeviceRngStateTensor(963b86c25da923da).'
  DeviceGenerators: DeviceGenerators#
  DeviceGenerators.CreateGenerator: DeviceGenerators#CreateGenerator(21806386b5f5e2e8).
  SetExportModeDefaultDeviceGenerator: SetExportModeDefaultDeviceGenerator(6fe9e9c2ce0e26ca).
  PyResetDefaultDeviceGeneratorsForTesting: PyResetDefaultDeviceGeneratorsForTesting(49f6e7a06ebc5aa8).
  ExportModeDeviceGeneratorImpl.clone_impl: ExportModeDeviceGeneratorImpl#clone_impl(ee48792689bb4c67).
  DeviceGenerators.operator: DeviceGenerators#`operator=`(5f6599b2f57ff8d8).
  ClearExportModeDefaultDeviceGenerators: ClearExportModeDefaultDeviceGenerators(49f6e7a06ebc5aa8).
  DeviceGenerators.ResetGenerators: DeviceGenerators#ResetGenerators(49f6e7a06ebc5aa8).
  SetManualSeed: SetManualSeed(14e956e2476ce5e2).
  MakeDeviceGenerator: MakeDeviceGenerator(7b54e84b17d612cb).
  EagerModeDeviceGeneratorImpl.get_state: EagerModeDeviceGeneratorImpl#get_state(455f465bc33b4cdf).
  SetManualSeedAll: SetManualSeedAll(2c44cd906ae4e829).
  EagerModeDeviceGeneratorImpl.clone_impl: EagerModeDeviceGeneratorImpl#clone_impl(ee48792689bb4c67).
  DeviceGeneratorImplBase.DeviceGeneratorImplBase: DeviceGeneratorImplBase#DeviceGeneratorImplBase(4af4fd0e2b26c4ac).
  ExportModeDeviceGeneratorImpl.DeviceStateTensor: ExportModeDeviceGeneratorImpl#DeviceStateTensor(30c064dc1e723e42).
  EagerModeDeviceGeneratorImpl.DeviceStateTensor: EagerModeDeviceGeneratorImpl#DeviceStateTensor(30c064dc1e723e42).
  DeviceGenerators.DeviceGenerators: DeviceGenerators#DeviceGenerators(d4f767463ce0a6b3).
  CrashExportModeGeneratorUnsupported: '`$anonymous_namespace_csrc/eager/device_gen_impl.cc`/CrashExportModeGeneratorUnsupported(c8024318075daf50).'
  DeviceGenerators.ClearExportModeDefaultGenerators: DeviceGenerators#ClearExportModeDefaultGenerators(49f6e7a06ebc5aa8).
  EagerModeDeviceGeneratorImpl.current_seed: EagerModeDeviceGeneratorImpl#current_seed(fe4d2d262d4164a8).
  EagerModeDeviceGeneratorImpl.get_offset: EagerModeDeviceGeneratorImpl#get_offset(fe4d2d262d4164a8).
  GetEagerDefaultDeviceGenerator: GetEagerDefaultDeviceGenerator(2279cd5805a18fe0).
  DeviceGenerators.num_devices: DeviceGenerators#num_devices(455f465bc33b4cdf).
  PySetInitDefaultGeneratorFailureForTesting: PySetInitDefaultGeneratorFailureForTesting(8d4ab0a187bf9331).
  UpdateDeviceRngOffset: '`$anonymous_namespace_csrc/eager/device_gen_impl.cc`/UpdateDeviceRngOffset(15f76abdc2722794).'
  ExportModeDeviceGeneratorImpl.current_seed: ExportModeDeviceGeneratorImpl#current_seed(fe4d2d262d4164a8).
  ExportModeDeviceGeneratorImpl.set_state: ExportModeDeviceGeneratorImpl#set_state(9ea24e05089f324f).
  ExportModeDeviceGeneratorImpl.get_offset: ExportModeDeviceGeneratorImpl#get_offset(fe4d2d262d4164a8).
  ExportModeDeviceGeneratorImpl.set_current_seed: ExportModeDeviceGeneratorImpl#set_current_seed(2c44cd906ae4e829).
  ExportModeDeviceGeneratorImpl.set_offset: ExportModeDeviceGeneratorImpl#set_offset(2c44cd906ae4e829).
  ExportModeDeviceGeneratorImpl.seed: ExportModeDeviceGeneratorImpl#seed(f708dce9a8856c70).
  EagerModeDeviceGeneratorImpl.graphsafe_get_state: EagerModeDeviceGeneratorImpl#graphsafe_get_state(ef17f419f916b356).
  ExportModeDeviceGeneratorImpl.get_state: ExportModeDeviceGeneratorImpl#get_state(155cbf890880ff04).
  GetInjectedInitDefaultGeneratorFailure: '`$anonymous_namespace_csrc/eager/device_gen_impl.cc`/GetInjectedInitDefaultGeneratorFailure(75da78375bc7a3dd).'
  GetExportModeDefaultGenerators: '`$anonymous_namespace_csrc/eager/device_gen_impl.cc`/GetExportModeDefaultGenerators(ffa05e89dbf2c50f).'
  ExportModeDeviceGeneratorImpl.graphsafe_get_state: ExportModeDeviceGeneratorImpl#graphsafe_get_state(455f465bc33b4cdf).
  DeviceGeneratorImplBase.device_type: DeviceGeneratorImplBase#device_type(257f012601a17b18).
  DeviceGenerators.num_devices_: DeviceGenerators#num_devices_.
  DeviceGenerators.generators_: DeviceGenerators#generators_.
  DeviceGenerators.generator_init_flags_: DeviceGenerators#generator_init_flags_.
---
# Module: [`csrc/eager/device_gen_impl.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc)

## Classes
### <a id="DeviceGenerators"></a>`DeviceGenerators`
- def: [`csrc/eager/device_gen_impl.cc:178`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L178)
- doc: A singleton that holds one generator per device. The generators are lazily
- signature: `class DeviceGenerators`
- members:
  - <a id="DeviceGenerators.ClearExportModeDefaultGenerators"></a>`ClearExportModeDefaultGenerators()` — [`L206`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L206)
  - <a id="DeviceGenerators.CreateGenerator"></a>`CreateGenerator(c10::DeviceIndex idx)` — [`L395`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L395) — Creates a new generator for the given device index. If idx is -1, creates a
  - `DeviceGenerators(DeviceGenerators&&)` — [`L183`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L183)
  - <a id="DeviceGenerators.DeviceGenerators"></a>`DeviceGenerators(int num_devices)` — [`L330`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L330)
  - `DeviceGenerators(const DeviceGenerators&)` — [`L181`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L181) — This class is neither copyable nor movable.
  - <a id="DeviceGenerators.GetDefaultGenerator"></a>`GetDefaultGenerator(at::DeviceIndex idx)` — [`L378`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L378) — Returns the default generator for the given device index. If idx is -1,
  - <a id="DeviceGenerators.GetDefaultInstance"></a>`GetDefaultInstance()` — [`L313`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L313)
  - <a id="DeviceGenerators.GetEagerDefaultGenerator"></a>`GetEagerDefaultGenerator(at::DeviceIndex idx)` — [`L353`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L353) — Returns the eager default generator for the given device index. If idx is
  - <a id="DeviceGenerators.ResetGenerators"></a>`ResetGenerators()` — [`L216`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L216) — Resets all generators to uninitialized state.
  - <a id="DeviceGenerators.SetExportModeDefaultGenerator"></a>`SetExportModeDefaultGenerator(c10::DeviceIndex idx, c10::optional<at::Generator> gen)` — [`L335`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L335)
  - <a id="DeviceGenerators.num_devices"></a>`num_devices()` — [`L201`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L201)
  - `operator=(const DeviceGenerators&)` — [`L182`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L182)
  - <a id="DeviceGenerators.operator"></a>`operator=(DeviceGenerators&&)` — [`L184`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L184)
  - <a id="DeviceGenerators.generator_init_flags_"></a>`generator_init_flags_` — [`L224`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L224)
  - <a id="DeviceGenerators.generators_"></a>`generators_` — [`L223`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L223)
  - <a id="DeviceGenerators.num_devices_"></a>`num_devices_` — [`L225`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L225)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/cache_key.cc.md#operator), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`kInvalidArgument`](../common/error_utils.h.md#kInvalidArgument), [`GetStatus`](../common/error_utils.h.md#GetStatus), [`operator=`](../common/error_utils.h.md#ThrowIfErrorAdapter.operator), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter.ThrowIfErrorAdapter), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter), [`Consume`](../common/error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`GetInstance`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetInstance), [`ConsumeRequiringMessage`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ConsumeRequiringMessage), [`PjrtBackend`](../pjrt/pjrt_state.h.md#PjrtBackend), [`EagerMode`](../common/context_states.h.md#EagerMode), [`EagerModeDeviceGeneratorImpl`](device_gen_impl.h.md#EagerModeDeviceGeneratorImpl), [`EnsureInitialized`](../pjrt/pjrt_state.cc.md#PjrtBackend.EnsureInitialized), [`ExportModeDeviceGeneratorImpl`](device_gen_impl.h.md#ExportModeDeviceGeneratorImpl), [`GetEagerMode`](eager_mode.cc.md#GetEagerMode), [`kFailedPrecondition`](../common/error_utils.h.md#kFailedPrecondition), [`NormalizeDeviceIndex`](device_gen_impl.cc.md#NormalizeDeviceIndex), [`InitDefaultGenerator`](device_gen_impl.cc.md#InitDefaultGenerator), [`DeviceGeneratorImplBase`](device_gen_impl.h.md#DeviceGeneratorImplBase), [`GetStatus`](../common/error_utils.h.md#GetStatus), [`kInternalCompileFxGraph`](../common/context_states.h.md#EagerMode.kInternalCompileFxGraph), [`PyResetDefaultDeviceGeneratorsForTesting`](device_gen_impl.cc.md#PyResetDefaultDeviceGeneratorsForTesting), [`GetExportModeDefaultGenerators`](device_gen_impl.cc.md#GetExportModeDefaultGenerators), [`GetExportModeDefaultGenerators`](device_gen_impl.cc.md#GetExportModeDefaultGenerators)
- used by: [`GetDefaultDeviceGenerator`](device_gen_impl.cc.md#GetDefaultDeviceGenerator), [`NormalizeDeviceIndex`](device_gen_impl.cc.md#NormalizeDeviceIndex), [`clone`](device_gen_impl.cc.md#DeviceGeneratorState.clone), [`SetExportModeDefaultDeviceGenerator`](device_gen_impl.cc.md#SetExportModeDefaultDeviceGenerator), [`PyResetDefaultDeviceGeneratorsForTesting`](device_gen_impl.cc.md#PyResetDefaultDeviceGeneratorsForTesting), [`ClearExportModeDefaultDeviceGenerators`](device_gen_impl.cc.md#ClearExportModeDefaultDeviceGenerators), [`MakeDeviceGenerator`](device_gen_impl.cc.md#MakeDeviceGenerator), [`SetManualSeed`](device_gen_impl.cc.md#SetManualSeed), [`SetManualSeedAll`](device_gen_impl.cc.md#SetManualSeedAll), [`GetEagerDefaultDeviceGenerator`](device_gen_impl.cc.md#GetEagerDefaultDeviceGenerator)

## Functions
- <a id="ClearExportModeDefaultDeviceGenerators"></a>`ClearExportModeDefaultDeviceGenerators()` — [`L775`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L775) — Clears all export-mode default generator overrides. Under
- <a id="CrashExportModeGeneratorUnsupported"></a>`CrashExportModeGeneratorUnsupported(std::string_view name)` — [`L676`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L676) — Helper for unsupported eager accessors. In Python, user-level calls to these
- <a id="CreateDeviceRngStateTensor"></a>`CreateDeviceRngStateTensor(c10::Device device, uint64_t seed, uint64_t offset)` — [`L133`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L133) — Allocates and initializes the 1D uint64 RNG state tensor ({seed, offset})
- <a id="GetDefaultDeviceGenerator"></a>`GetDefaultDeviceGenerator(c10::DeviceIndex idx)` — [`L779`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L779) — Returns the default generator for the given device index. If idx is -1, — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- <a id="GetEagerDefaultDeviceGenerator"></a>`GetEagerDefaultDeviceGenerator(c10::DeviceIndex idx)` — [`L783`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L783) — Returns the eager default generator for the given device index. If idx is -1,
- `GetExportModeDefaultGenerators()` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L155)
- <a id="GetExportModeDefaultGenerators"></a>`GetExportModeDefaultGenerators()` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L155)
- <a id="GetInjectedInitDefaultGeneratorFailure"></a>`GetInjectedInitDefaultGeneratorFailure()` — [`L149`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L149) — A modifiable string that can be used to force the next InitDefaultGenerator()
- <a id="InitDefaultGenerator"></a>`InitDefaultGenerator(DeviceGeneratorImpl* gen_impl, uint64_t seed)` — [`L164`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L164) — Initializes the default generator with the given seed.
- <a id="MakeDeviceGenerator"></a>`MakeDeviceGenerator(c10::DeviceIndex idx)` — [`L740`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L740) — Creates a new generator for the given device index. If idx is -1, creates a
- <a id="NormalizeDeviceIndex"></a>`NormalizeDeviceIndex(c10::DeviceIndex idx)` — [`L230`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L230)
- <a id="PyResetDefaultDeviceGeneratorsForTesting"></a>`PyResetDefaultDeviceGeneratorsForTesting()` — [`L764`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L764) — Resets all default device generators for testing.
- <a id="PySetInitDefaultGeneratorFailureForTesting"></a>`PySetInitDefaultGeneratorFailureForTesting(std::string failure_message)` — [`L760`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L760) — Injects a failure message to be returned by the next InitDefaultGenerator().
- <a id="SetExportModeDefaultDeviceGenerator"></a>`SetExportModeDefaultDeviceGenerator(c10::optional<at::Generator> gen, c10::DeviceIndex idx)` — [`L768`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L768) — Sets the export-mode default generator for override. If idx is -1, sets the
- <a id="SetManualSeed"></a>`SetManualSeed(uint64_t seed, c10::DeviceIndex idx)` — [`L744`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L744) — Sets the seed for the generator of the given device index. If idx is -1,
- <a id="SetManualSeedAll"></a>`SetManualSeedAll(uint64_t seed)` — [`L753`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L753) — Sets the seed for all TPU generators.
- <a id="UpdateDeviceRngOffset"></a>`UpdateDeviceRngOffset(at::Tensor rng_state, uint64_t value)` — [`L113`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L113)
- <a id="UpdateDeviceRngState"></a>`UpdateDeviceRngState(at::Tensor rng_state, uint64_t value, int64_t position)` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L77)
- <a id="ValidateAndGetEagerBase"></a>`ValidateAndGetEagerBase(const at::Generator& default_generator)` — [`L619`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L619)

## Other members
- `get_state` — [`L549`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L549)
- `graphsafe_get_state` — [`L585`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L585)
- `graphsafe_set_state` — [`L590`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L590)
- `EagerModeDeviceGeneratorImpl` — [`L484`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L484)
- `EagerModeDeviceGeneratorImpl` — [`L484`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L484)
- `EagerModeDeviceGeneratorImpl` — [`L476`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L476)
- `clone` — [`L305`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L305)
- `ExportModeDeviceGeneratorImpl` — [`L636`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L636)
- `get_state` — [`L692`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L692)
- `graphsafe_set_state` — [`L713`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L713)
- `ExportModeDeviceGeneratorImpl` — [`L651`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L651)
- `ExportModeDeviceGeneratorImpl` — [`L646`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L646)
- `graphsafe_get_state` — [`L708`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L708)
- <a id="DeviceGeneratorImplBase.AdvanceDeviceStateTensor"></a>`DeviceGeneratorImplBase.AdvanceDeviceStateTensor` — [`L425`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L425)
- <a id="DeviceGeneratorImplBase.DeviceGeneratorImplBase"></a>`DeviceGeneratorImplBase.DeviceGeneratorImplBase` — [`L405`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L405) — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- <a id="DeviceGeneratorImplBase.ValidateDeviceStateTensor"></a>`DeviceGeneratorImplBase.ValidateDeviceStateTensor` — [`L411`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L411)
- <a id="DeviceGeneratorImplBase.device_type"></a>`DeviceGeneratorImplBase.device_type` — [`L401`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L401)
- <a id="DeviceGeneratorState.MaybeMaterializeDeviceStateTensor"></a>`DeviceGeneratorState.MaybeMaterializeDeviceStateTensor` — [`L248`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L248)
- <a id="DeviceGeneratorState.SetDeviceStateTensor"></a>`DeviceGeneratorState.SetDeviceStateTensor` — [`L290`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L290)
- <a id="DeviceGeneratorState.WriteStateToDevice"></a>`DeviceGeneratorState.WriteStateToDevice` — [`L297`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L297)
- <a id="DeviceGeneratorState.clone"></a>`DeviceGeneratorState.clone` — [`L305`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L305)
- <a id="EagerModeDeviceGeneratorImpl.DeviceStateTensor"></a>`EagerModeDeviceGeneratorImpl.DeviceStateTensor` — [`L502`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L502) — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- <a id="EagerModeDeviceGeneratorImpl.EagerModeDeviceGeneratorImpl"></a>`EagerModeDeviceGeneratorImpl.EagerModeDeviceGeneratorImpl` — [`L489`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L489)
- <a id="EagerModeDeviceGeneratorImpl.SetDeviceStateTensor"></a>`EagerModeDeviceGeneratorImpl.SetDeviceStateTensor` — [`L506`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L506)
- <a id="EagerModeDeviceGeneratorImpl.clone_impl"></a>`EagerModeDeviceGeneratorImpl.clone_impl` — [`L607`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L607)
- <a id="EagerModeDeviceGeneratorImpl.current_seed"></a>`EagerModeDeviceGeneratorImpl.current_seed` — [`L536`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L536)
- <a id="EagerModeDeviceGeneratorImpl.get_offset"></a>`EagerModeDeviceGeneratorImpl.get_offset` — [`L532`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L532)
- <a id="EagerModeDeviceGeneratorImpl.get_state"></a>`EagerModeDeviceGeneratorImpl.get_state` — [`L549`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L549)
- <a id="EagerModeDeviceGeneratorImpl.graphsafe_get_state"></a>`EagerModeDeviceGeneratorImpl.graphsafe_get_state` — [`L585`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L585)
- <a id="EagerModeDeviceGeneratorImpl.graphsafe_set_state"></a>`EagerModeDeviceGeneratorImpl.graphsafe_set_state` — [`L590`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L590)
- <a id="EagerModeDeviceGeneratorImpl.seed"></a>`EagerModeDeviceGeneratorImpl.seed` — [`L540`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L540)
- <a id="EagerModeDeviceGeneratorImpl.set_current_seed"></a>`EagerModeDeviceGeneratorImpl.set_current_seed` — [`L511`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L511)
- <a id="EagerModeDeviceGeneratorImpl.set_offset"></a>`EagerModeDeviceGeneratorImpl.set_offset` — [`L518`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L518)
- <a id="EagerModeDeviceGeneratorImpl.set_state"></a>`EagerModeDeviceGeneratorImpl.set_state` — [`L559`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L559)
- <a id="ExportModeDeviceGeneratorImpl.DeviceStateTensor"></a>`ExportModeDeviceGeneratorImpl.DeviceStateTensor` — [`L660`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L660) — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- <a id="ExportModeDeviceGeneratorImpl.ExportModeDeviceGeneratorImpl"></a>`ExportModeDeviceGeneratorImpl.ExportModeDeviceGeneratorImpl` — [`L651`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L651)
- <a id="ExportModeDeviceGeneratorImpl.SetDeviceStateTensor"></a>`ExportModeDeviceGeneratorImpl.SetDeviceStateTensor` — [`L664`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L664)
- <a id="ExportModeDeviceGeneratorImpl.clone_impl"></a>`ExportModeDeviceGeneratorImpl.clone_impl` — [`L732`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L732)
- <a id="ExportModeDeviceGeneratorImpl.current_seed"></a>`ExportModeDeviceGeneratorImpl.current_seed` — [`L686`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L686)
- <a id="ExportModeDeviceGeneratorImpl.get_offset"></a>`ExportModeDeviceGeneratorImpl.get_offset` — [`L683`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L683)
- <a id="ExportModeDeviceGeneratorImpl.get_state"></a>`ExportModeDeviceGeneratorImpl.get_state` — [`L692`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L692)
- <a id="ExportModeDeviceGeneratorImpl.graphsafe_get_state"></a>`ExportModeDeviceGeneratorImpl.graphsafe_get_state` — [`L708`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L708)
- <a id="ExportModeDeviceGeneratorImpl.graphsafe_set_state"></a>`ExportModeDeviceGeneratorImpl.graphsafe_set_state` — [`L713`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L713)
- <a id="ExportModeDeviceGeneratorImpl.seed"></a>`ExportModeDeviceGeneratorImpl.seed` — [`L689`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L689)
- <a id="ExportModeDeviceGeneratorImpl.set_current_seed"></a>`ExportModeDeviceGeneratorImpl.set_current_seed` — [`L696`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L696)
- <a id="ExportModeDeviceGeneratorImpl.set_offset"></a>`ExportModeDeviceGeneratorImpl.set_offset` — [`L699`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L699)
- <a id="ExportModeDeviceGeneratorImpl.set_state"></a>`ExportModeDeviceGeneratorImpl.set_state` — [`L702`](../../../../../../raw/code/torch_tpu/csrc/eager/device_gen_impl.cc#L702)

