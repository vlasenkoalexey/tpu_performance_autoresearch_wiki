---
title: 'Module: csrc/distributed/slicebuilder/discovery.h'
type: catalog
provenance: extracted
module: csrc/distributed/slicebuilder/discovery.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DistributedWorkerConfiguration: DistributedWorkerConfiguration#
  DistributedWorkerConfiguration.rank: DistributedWorkerConfiguration#rank.
  DistributedWorkerConfiguration.sb_addrs: DistributedWorkerConfiguration#sb_addrs.
  DistributedWorkerConfiguration.sb_port: DistributedWorkerConfiguration#sb_port.
  DistributedWorkerConfiguration.topology: DistributedWorkerConfiguration#topology.
  DistributedWorkerConfiguration.local_rank: DistributedWorkerConfiguration#local_rank.
  SlicebuilderMeshConfig.port: SlicebuilderMeshConfig#port.
  DistributedWorkerConfiguration.world_size: DistributedWorkerConfiguration#world_size.
  SlicebuilderMeshConfig: SlicebuilderMeshConfig#
  SlicebuilderMeshConfig.address: SlicebuilderMeshConfig#address.
---
# Module: [`csrc/distributed/slicebuilder/discovery.h`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h)

## Classes
### <a id="DistributedWorkerConfiguration"></a>`DistributedWorkerConfiguration`
- def: [`csrc/distributed/slicebuilder/discovery.h:29`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L29) — documented in [process-group-and-collectives](../../../../concepts/process-group-and-collectives.md)
- signature: `struct DistributedWorkerConfiguration`
- members:
  - <a id="DistributedWorkerConfiguration.local_rank"></a>`local_rank` — [`L31`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L31)
  - <a id="DistributedWorkerConfiguration.rank"></a>`rank` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L30)
  - <a id="DistributedWorkerConfiguration.sb_addrs"></a>`sb_addrs` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L33)
  - <a id="DistributedWorkerConfiguration.sb_port"></a>`sb_port` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L36) — This is also contained in `sb_addrs` (at index `rank`), but we keep it
  - <a id="DistributedWorkerConfiguration.topology"></a>`topology` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L37)
  - <a id="DistributedWorkerConfiguration.world_size"></a>`world_size` — [`L32`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L32)
- used by: [`InitializeDistributedEnvironment`](../../common/environment.cc.md#InitializeDistributedEnvironment), [`GetDistributedWorkerConfiguration`](discovery.cc.md#GetDistributedWorkerConfiguration), [`ValidateRequiredDistributedEnvVars`](discovery.cc.md#ValidateRequiredDistributedEnvVars), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironmentSetsTaskIdUsingSliceRankForMultislice_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironmentSetsChipsBoundsFor4DTopology_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironment_SetsAllowMultipleLibtpuLoad_Test.TestBody), [`TestBody`](discovery_test.cc.md#DiscoveryDeathTest_GetDistributedWorkerConfigurationMultislice_Test.TestBody), [`TestBody`](discovery_test.cc.md#DiscoveryDeathTest_GetDistributedWorkerConfiguration_Test.TestBody), [`TestBody`](discovery_test.cc.md#DiscoveryDeathTest_GetDistributedWorkerConfigurationMissingVars_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitDistEnv_FallsBackOnMalformedTpuVisibleDevicesEnvVar_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitDistEnv_FallsBackOnNegativeTpuVisibleDevicesEnvVar_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitDistEnv_OverwritesExistingTpuVisibleChipsEnvVar_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitDistEnv_OverwritesMultiDeviceTpuVisibleDevicesEnvVar_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitDistEnv_RespectsExistingSingleTpuVisibleDevicesEnvVar_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironment_PopulatesSingleDeviceProcessAddresses_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironment_PopulatesSlicebuilderAddresses_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironmentUnsetsAddressesFirst_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironment_OverridesSlicebuilderInsecureGrpcFlag_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironment_OverridesXlaBarrierFlags_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironment_ResolvesBnsPort_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironment_FailsOnEmptySlicebuilderAddresses_Test.TestBody), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitializeDistributedEnvironment_FailsOnNegativeRank_Test.TestBody), [`MultisliceConfig`](../../common/environment_test.cc.md#MultisliceConfig), [`TestBody`](../../common/environment_test.cc.md#EnvironmentDeathTest_InitDistEnvLeavesMegascalePortsUnsetForSingleSlice_Test.TestBody), [`InitAndPrintMegascalePorts`](../../common/environment_test.cc.md#InitAndPrintMegascalePorts), [`port`](discovery.h.md#SlicebuilderMeshConfig.port), [`kTwoHostSliceAddresses`](../../common/environment_test.cc.md#kTwoHostSliceAddresses)

### <a id="SlicebuilderMeshConfig"></a>`SlicebuilderMeshConfig`
- def: [`csrc/distributed/slicebuilder/discovery.h:40`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L40)
- signature: `struct SlicebuilderMeshConfig`
- members:
  - <a id="SlicebuilderMeshConfig.address"></a>`address` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L41)
  - <a id="SlicebuilderMeshConfig.port"></a>`port` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/distributed/slicebuilder/discovery.h#L42)
- uses (calls/refs, reference-scoped): [`GetDistributedWorkerConfiguration`](discovery.cc.md#GetDistributedWorkerConfiguration), [`DistributedWorkerConfiguration`](discovery.h.md#DistributedWorkerConfiguration)

