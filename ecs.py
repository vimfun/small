from aliyun import client, desc_it, result_mapper

from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest
from aliyunsdkecs.request.v20140526.ActivateRouterInterfaceRequest import ActivateRouterInterfaceRequest
from aliyunsdkecs.request.v20140526.AddBandwidthPackageIpsRequest import AddBandwidthPackageIpsRequest
from aliyunsdkecs.request.v20140526.AddTagsRequest import AddTagsRequest
from aliyunsdkecs.request.v20140526.AllocateDedicatedHostsRequest import AllocateDedicatedHostsRequest
from aliyunsdkecs.request.v20140526.AllocateEipAddressRequest import AllocateEipAddressRequest
from aliyunsdkecs.request.v20140526.AllocatePublicIpAddressRequest import AllocatePublicIpAddressRequest
from aliyunsdkecs.request.v20140526.ApplyAutoSnapshotPolicyRequest import ApplyAutoSnapshotPolicyRequest
from aliyunsdkecs.request.v20140526.AssignIpv6AddressesRequest import AssignIpv6AddressesRequest
from aliyunsdkecs.request.v20140526.AssignPrivateIpAddressesRequest import AssignPrivateIpAddressesRequest
from aliyunsdkecs.request.v20140526.AssociateEipAddressRequest import AssociateEipAddressRequest
from aliyunsdkecs.request.v20140526.AssociateHaVipRequest import AssociateHaVipRequest
from aliyunsdkecs.request.v20140526.AttachClassicLinkVpcRequest import AttachClassicLinkVpcRequest
from aliyunsdkecs.request.v20140526.AttachDiskRequest import AttachDiskRequest
from aliyunsdkecs.request.v20140526.AttachInstanceRamRoleRequest import AttachInstanceRamRoleRequest
from aliyunsdkecs.request.v20140526.AttachKeyPairRequest import AttachKeyPairRequest
from aliyunsdkecs.request.v20140526.AttachNetworkInterfaceRequest import AttachNetworkInterfaceRequest
from aliyunsdkecs.request.v20140526.AuthorizeSecurityGroupEgressRequest import AuthorizeSecurityGroupEgressRequest
from aliyunsdkecs.request.v20140526.AuthorizeSecurityGroupRequest import AuthorizeSecurityGroupRequest
from aliyunsdkecs.request.v20140526.CancelAutoSnapshotPolicyRequest import CancelAutoSnapshotPolicyRequest
from aliyunsdkecs.request.v20140526.CancelCopyImageRequest import CancelCopyImageRequest
from aliyunsdkecs.request.v20140526.CancelPhysicalConnectionRequest import CancelPhysicalConnectionRequest
from aliyunsdkecs.request.v20140526.CancelSimulatedSystemEventsRequest import CancelSimulatedSystemEventsRequest
from aliyunsdkecs.request.v20140526.CancelTaskRequest import CancelTaskRequest
from aliyunsdkecs.request.v20140526.ConnectRouterInterfaceRequest import ConnectRouterInterfaceRequest
from aliyunsdkecs.request.v20140526.ConvertNatPublicIpToEipRequest import ConvertNatPublicIpToEipRequest
from aliyunsdkecs.request.v20140526.CopyImageRequest import CopyImageRequest
from aliyunsdkecs.request.v20140526.CreateAutoProvisioningGroupRequest import CreateAutoProvisioningGroupRequest
from aliyunsdkecs.request.v20140526.CreateAutoSnapshotPolicyRequest import CreateAutoSnapshotPolicyRequest
from aliyunsdkecs.request.v20140526.CreateCommandRequest import CreateCommandRequest
from aliyunsdkecs.request.v20140526.CreateDemandRequest import CreateDemandRequest
from aliyunsdkecs.request.v20140526.CreateDeploymentSetRequest import CreateDeploymentSetRequest
from aliyunsdkecs.request.v20140526.CreateDiskRequest import CreateDiskRequest
from aliyunsdkecs.request.v20140526.CreateForwardEntryRequest import CreateForwardEntryRequest
from aliyunsdkecs.request.v20140526.CreateHaVipRequest import CreateHaVipRequest
from aliyunsdkecs.request.v20140526.CreateHpcClusterRequest import CreateHpcClusterRequest
from aliyunsdkecs.request.v20140526.CreateImageRequest import CreateImageRequest
from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
from aliyunsdkecs.request.v20140526.CreateKeyPairRequest import CreateKeyPairRequest
from aliyunsdkecs.request.v20140526.CreateLaunchTemplateRequest import CreateLaunchTemplateRequest
from aliyunsdkecs.request.v20140526.CreateLaunchTemplateVersionRequest import CreateLaunchTemplateVersionRequest
from aliyunsdkecs.request.v20140526.CreateNatGatewayRequest import CreateNatGatewayRequest
from aliyunsdkecs.request.v20140526.CreateNetworkInterfacePermissionRequest import CreateNetworkInterfacePermissionRequest
from aliyunsdkecs.request.v20140526.CreateNetworkInterfaceRequest import CreateNetworkInterfaceRequest
from aliyunsdkecs.request.v20140526.CreatePhysicalConnectionRequest import CreatePhysicalConnectionRequest
from aliyunsdkecs.request.v20140526.CreateRouteEntryRequest import CreateRouteEntryRequest
from aliyunsdkecs.request.v20140526.CreateRouterInterfaceRequest import CreateRouterInterfaceRequest
from aliyunsdkecs.request.v20140526.CreateSecurityGroupRequest import CreateSecurityGroupRequest
from aliyunsdkecs.request.v20140526.CreateSimulatedSystemEventsRequest import CreateSimulatedSystemEventsRequest
from aliyunsdkecs.request.v20140526.CreateSnapshotRequest import CreateSnapshotRequest
from aliyunsdkecs.request.v20140526.CreateStorageSetRequest import CreateStorageSetRequest
from aliyunsdkecs.request.v20140526.CreateVSwitchRequest import CreateVSwitchRequest
from aliyunsdkecs.request.v20140526.CreateVirtualBorderRouterRequest import CreateVirtualBorderRouterRequest
from aliyunsdkecs.request.v20140526.CreateVpcRequest import CreateVpcRequest
from aliyunsdkecs.request.v20140526.DeactivateRouterInterfaceRequest import DeactivateRouterInterfaceRequest
from aliyunsdkecs.request.v20140526.DeleteAutoProvisioningGroupRequest import DeleteAutoProvisioningGroupRequest
from aliyunsdkecs.request.v20140526.DeleteAutoSnapshotPolicyRequest import DeleteAutoSnapshotPolicyRequest
from aliyunsdkecs.request.v20140526.DeleteBandwidthPackageRequest import DeleteBandwidthPackageRequest
from aliyunsdkecs.request.v20140526.DeleteCommandRequest import DeleteCommandRequest
from aliyunsdkecs.request.v20140526.DeleteDemandRequest import DeleteDemandRequest
from aliyunsdkecs.request.v20140526.DeleteDeploymentSetRequest import DeleteDeploymentSetRequest
from aliyunsdkecs.request.v20140526.DeleteDiskRequest import DeleteDiskRequest
from aliyunsdkecs.request.v20140526.DeleteForwardEntryRequest import DeleteForwardEntryRequest
from aliyunsdkecs.request.v20140526.DeleteHaVipRequest import DeleteHaVipRequest
from aliyunsdkecs.request.v20140526.DeleteHpcClusterRequest import DeleteHpcClusterRequest
from aliyunsdkecs.request.v20140526.DeleteImageRequest import DeleteImageRequest
from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526.DeleteInstancesRequest import DeleteInstancesRequest
from aliyunsdkecs.request.v20140526.DeleteKeyPairsRequest import DeleteKeyPairsRequest
from aliyunsdkecs.request.v20140526.DeleteLaunchTemplateRequest import DeleteLaunchTemplateRequest
from aliyunsdkecs.request.v20140526.DeleteLaunchTemplateVersionRequest import DeleteLaunchTemplateVersionRequest
from aliyunsdkecs.request.v20140526.DeleteNatGatewayRequest import DeleteNatGatewayRequest
from aliyunsdkecs.request.v20140526.DeleteNetworkInterfacePermissionRequest import DeleteNetworkInterfacePermissionRequest
from aliyunsdkecs.request.v20140526.DeleteNetworkInterfaceRequest import DeleteNetworkInterfaceRequest
from aliyunsdkecs.request.v20140526.DeletePhysicalConnectionRequest import DeletePhysicalConnectionRequest
from aliyunsdkecs.request.v20140526.DeleteRouteEntryRequest import DeleteRouteEntryRequest
from aliyunsdkecs.request.v20140526.DeleteRouterInterfaceRequest import DeleteRouterInterfaceRequest
from aliyunsdkecs.request.v20140526.DeleteSecurityGroupRequest import DeleteSecurityGroupRequest
from aliyunsdkecs.request.v20140526.DeleteSnapshotRequest import DeleteSnapshotRequest
from aliyunsdkecs.request.v20140526.DeleteStorageSetRequest import DeleteStorageSetRequest
from aliyunsdkecs.request.v20140526.DeleteVSwitchRequest import DeleteVSwitchRequest
from aliyunsdkecs.request.v20140526.DeleteVirtualBorderRouterRequest import DeleteVirtualBorderRouterRequest
from aliyunsdkecs.request.v20140526.DeleteVpcRequest import DeleteVpcRequest
from aliyunsdkecs.request.v20140526.DescribeAccessPointsRequest import DescribeAccessPointsRequest
from aliyunsdkecs.request.v20140526.DescribeAccountAttributesRequest import DescribeAccountAttributesRequest
from aliyunsdkecs.request.v20140526.DescribeAutoProvisioningGroupHistoryRequest import DescribeAutoProvisioningGroupHistoryRequest
from aliyunsdkecs.request.v20140526.DescribeAutoProvisioningGroupInstancesRequest import DescribeAutoProvisioningGroupInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeAutoProvisioningGroupsRequest import DescribeAutoProvisioningGroupsRequest
from aliyunsdkecs.request.v20140526.DescribeAutoSnapshotPolicyExRequest import DescribeAutoSnapshotPolicyExRequest
from aliyunsdkecs.request.v20140526.DescribeAvailableResourceRequest import DescribeAvailableResourceRequest
from aliyunsdkecs.request.v20140526.DescribeBandwidthLimitationRequest import DescribeBandwidthLimitationRequest
from aliyunsdkecs.request.v20140526.DescribeBandwidthPackagesRequest import DescribeBandwidthPackagesRequest
from aliyunsdkecs.request.v20140526.DescribeClassicLinkInstancesRequest import DescribeClassicLinkInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeCloudAssistantStatusRequest import DescribeCloudAssistantStatusRequest
from aliyunsdkecs.request.v20140526.DescribeClustersRequest import DescribeClustersRequest
from aliyunsdkecs.request.v20140526.DescribeCommandsRequest import DescribeCommandsRequest
from aliyunsdkecs.request.v20140526.DescribeDedicatedHostAutoRenewRequest import DescribeDedicatedHostAutoRenewRequest
from aliyunsdkecs.request.v20140526.DescribeDedicatedHostTypesRequest import DescribeDedicatedHostTypesRequest
from aliyunsdkecs.request.v20140526.DescribeDedicatedHostsRequest import DescribeDedicatedHostsRequest
from aliyunsdkecs.request.v20140526.DescribeDemandsRequest import DescribeDemandsRequest
from aliyunsdkecs.request.v20140526.DescribeDeploymentSetsRequest import DescribeDeploymentSetsRequest
from aliyunsdkecs.request.v20140526.DescribeDiskMonitorDataRequest import DescribeDiskMonitorDataRequest
from aliyunsdkecs.request.v20140526.DescribeDisksFullStatusRequest import DescribeDisksFullStatusRequest
from aliyunsdkecs.request.v20140526.DescribeDisksRequest import DescribeDisksRequest
from aliyunsdkecs.request.v20140526.DescribeEipAddressesRequest import DescribeEipAddressesRequest
from aliyunsdkecs.request.v20140526.DescribeEipMonitorDataRequest import DescribeEipMonitorDataRequest
from aliyunsdkecs.request.v20140526.DescribeEniMonitorDataRequest import DescribeEniMonitorDataRequest
from aliyunsdkecs.request.v20140526.DescribeForwardTableEntriesRequest import DescribeForwardTableEntriesRequest
from aliyunsdkecs.request.v20140526.DescribeHaVipsRequest import DescribeHaVipsRequest
from aliyunsdkecs.request.v20140526.DescribeHpcClustersRequest import DescribeHpcClustersRequest
from aliyunsdkecs.request.v20140526.DescribeImageSharePermissionRequest import DescribeImageSharePermissionRequest
from aliyunsdkecs.request.v20140526.DescribeImageSupportInstanceTypesRequest import DescribeImageSupportInstanceTypesRequest
from aliyunsdkecs.request.v20140526.DescribeImagesRequest import DescribeImagesRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceAttributeRequest import DescribeInstanceAttributeRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceAutoRenewAttributeRequest import DescribeInstanceAutoRenewAttributeRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceHistoryEventsRequest import DescribeInstanceHistoryEventsRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceMaintenanceAttributesRequest import DescribeInstanceMaintenanceAttributesRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceMonitorDataRequest import DescribeInstanceMonitorDataRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceRamRoleRequest import DescribeInstanceRamRoleRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceStatusRequest import DescribeInstanceStatusRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceTopologyRequest import DescribeInstanceTopologyRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceTypeFamiliesRequest import DescribeInstanceTypeFamiliesRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceTypesRequest import DescribeInstanceTypesRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceVncPasswdRequest import DescribeInstanceVncPasswdRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceVncUrlRequest import DescribeInstanceVncUrlRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesFullStatusRequest import DescribeInstancesFullStatusRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeInvocationResultsRequest import DescribeInvocationResultsRequest
from aliyunsdkecs.request.v20140526.DescribeInvocationsRequest import DescribeInvocationsRequest
from aliyunsdkecs.request.v20140526.DescribeKeyPairsRequest import DescribeKeyPairsRequest
from aliyunsdkecs.request.v20140526.DescribeLaunchTemplateVersionsRequest import DescribeLaunchTemplateVersionsRequest
from aliyunsdkecs.request.v20140526.DescribeLaunchTemplatesRequest import DescribeLaunchTemplatesRequest
from aliyunsdkecs.request.v20140526.DescribeLimitationRequest import DescribeLimitationRequest
from aliyunsdkecs.request.v20140526.DescribeNatGatewaysRequest import DescribeNatGatewaysRequest
from aliyunsdkecs.request.v20140526.DescribeNetworkInterfacePermissionsRequest import DescribeNetworkInterfacePermissionsRequest
from aliyunsdkecs.request.v20140526.DescribeNetworkInterfacesRequest import DescribeNetworkInterfacesRequest
from aliyunsdkecs.request.v20140526.DescribeNewProjectEipMonitorDataRequest import DescribeNewProjectEipMonitorDataRequest
from aliyunsdkecs.request.v20140526.DescribePhysicalConnectionsRequest import DescribePhysicalConnectionsRequest
from aliyunsdkecs.request.v20140526.DescribePriceRequest import DescribePriceRequest
from aliyunsdkecs.request.v20140526.DescribeRecommendInstanceTypeRequest import DescribeRecommendInstanceTypeRequest
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdkecs.request.v20140526.DescribeRenewalPriceRequest import DescribeRenewalPriceRequest
from aliyunsdkecs.request.v20140526.DescribeReservedInstancesRequest import DescribeReservedInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeResourceByTagsRequest import DescribeResourceByTagsRequest
from aliyunsdkecs.request.v20140526.DescribeResourcesModificationRequest import DescribeResourcesModificationRequest
from aliyunsdkecs.request.v20140526.DescribeRouteTablesRequest import DescribeRouteTablesRequest
from aliyunsdkecs.request.v20140526.DescribeRouterInterfacesRequest import DescribeRouterInterfacesRequest
from aliyunsdkecs.request.v20140526.DescribeSecurityGroupAttributeRequest import DescribeSecurityGroupAttributeRequest
from aliyunsdkecs.request.v20140526.DescribeSecurityGroupReferencesRequest import DescribeSecurityGroupReferencesRequest
from aliyunsdkecs.request.v20140526.DescribeSecurityGroupsRequest import DescribeSecurityGroupsRequest
from aliyunsdkecs.request.v20140526.DescribeSnapshotLinksRequest import DescribeSnapshotLinksRequest
from aliyunsdkecs.request.v20140526.DescribeSnapshotMonitorDataRequest import DescribeSnapshotMonitorDataRequest
from aliyunsdkecs.request.v20140526.DescribeSnapshotPackageRequest import DescribeSnapshotPackageRequest
from aliyunsdkecs.request.v20140526.DescribeSnapshotsRequest import DescribeSnapshotsRequest
from aliyunsdkecs.request.v20140526.DescribeSnapshotsUsageRequest import DescribeSnapshotsUsageRequest
from aliyunsdkecs.request.v20140526.DescribeSpotPriceHistoryRequest import DescribeSpotPriceHistoryRequest
from aliyunsdkecs.request.v20140526.DescribeStorageSetDetailsRequest import DescribeStorageSetDetailsRequest
from aliyunsdkecs.request.v20140526.DescribeStorageSetsRequest import DescribeStorageSetsRequest
from aliyunsdkecs.request.v20140526.DescribeTagsRequest import DescribeTagsRequest
from aliyunsdkecs.request.v20140526.DescribeTaskAttributeRequest import DescribeTaskAttributeRequest
from aliyunsdkecs.request.v20140526.DescribeTasksRequest import DescribeTasksRequest
from aliyunsdkecs.request.v20140526.DescribeUserBusinessBehaviorRequest import DescribeUserBusinessBehaviorRequest
from aliyunsdkecs.request.v20140526.DescribeUserDataRequest import DescribeUserDataRequest
from aliyunsdkecs.request.v20140526.DescribeVRoutersRequest import DescribeVRoutersRequest
from aliyunsdkecs.request.v20140526.DescribeVSwitchesRequest import DescribeVSwitchesRequest
from aliyunsdkecs.request.v20140526.DescribeVirtualBorderRoutersForPhysicalConnectionRequest import DescribeVirtualBorderRoutersForPhysicalConnectionRequest
from aliyunsdkecs.request.v20140526.DescribeVirtualBorderRoutersRequest import DescribeVirtualBorderRoutersRequest
from aliyunsdkecs.request.v20140526.DescribeVpcsRequest import DescribeVpcsRequest
from aliyunsdkecs.request.v20140526.DescribeZonesRequest import DescribeZonesRequest
from aliyunsdkecs.request.v20140526.DetachClassicLinkVpcRequest import DetachClassicLinkVpcRequest
from aliyunsdkecs.request.v20140526.DetachDiskRequest import DetachDiskRequest
from aliyunsdkecs.request.v20140526.DetachInstanceRamRoleRequest import DetachInstanceRamRoleRequest
from aliyunsdkecs.request.v20140526.DetachKeyPairRequest import DetachKeyPairRequest
from aliyunsdkecs.request.v20140526.DetachNetworkInterfaceRequest import DetachNetworkInterfaceRequest
from aliyunsdkecs.request.v20140526.EipFillParamsRequest import EipFillParamsRequest
from aliyunsdkecs.request.v20140526.EipFillProductRequest import EipFillProductRequest
from aliyunsdkecs.request.v20140526.EipNotifyPaidRequest import EipNotifyPaidRequest
from aliyunsdkecs.request.v20140526.EnablePhysicalConnectionRequest import EnablePhysicalConnectionRequest
from aliyunsdkecs.request.v20140526.ExportImageRequest import ExportImageRequest
from aliyunsdkecs.request.v20140526.ExportSnapshotRequest import ExportSnapshotRequest
from aliyunsdkecs.request.v20140526.GetInstanceConsoleOutputRequest import GetInstanceConsoleOutputRequest
from aliyunsdkecs.request.v20140526.GetInstanceScreenshotRequest import GetInstanceScreenshotRequest
from aliyunsdkecs.request.v20140526.ImportImageRequest import ImportImageRequest
from aliyunsdkecs.request.v20140526.ImportKeyPairRequest import ImportKeyPairRequest
from aliyunsdkecs.request.v20140526.ImportSnapshotRequest import ImportSnapshotRequest
from aliyunsdkecs.request.v20140526.InstallCloudAssistantRequest import InstallCloudAssistantRequest
from aliyunsdkecs.request.v20140526.InvokeCommandRequest import InvokeCommandRequest
from aliyunsdkecs.request.v20140526.JoinResourceGroupRequest import JoinResourceGroupRequest
from aliyunsdkecs.request.v20140526.JoinSecurityGroupRequest import JoinSecurityGroupRequest
from aliyunsdkecs.request.v20140526.LeaveSecurityGroupRequest import LeaveSecurityGroupRequest
from aliyunsdkecs.request.v20140526.ListTagResourcesRequest import ListTagResourcesRequest
from aliyunsdkecs.request.v20140526.ModifyAutoProvisioningGroupRequest import ModifyAutoProvisioningGroupRequest
from aliyunsdkecs.request.v20140526.ModifyAutoSnapshotPolicyExRequest import ModifyAutoSnapshotPolicyExRequest
from aliyunsdkecs.request.v20140526.ModifyAutoSnapshotPolicyRequest import ModifyAutoSnapshotPolicyRequest
from aliyunsdkecs.request.v20140526.ModifyBandwidthPackageSpecRequest import ModifyBandwidthPackageSpecRequest
from aliyunsdkecs.request.v20140526.ModifyCommandRequest import ModifyCommandRequest
from aliyunsdkecs.request.v20140526.ModifyDedicatedHostAttributeRequest import ModifyDedicatedHostAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyDedicatedHostAutoReleaseTimeRequest import ModifyDedicatedHostAutoReleaseTimeRequest
from aliyunsdkecs.request.v20140526.ModifyDedicatedHostAutoRenewAttributeRequest import ModifyDedicatedHostAutoRenewAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyDemandRequest import ModifyDemandRequest
from aliyunsdkecs.request.v20140526.ModifyDeploymentSetAttributeRequest import ModifyDeploymentSetAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyDiskAttributeRequest import ModifyDiskAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyDiskChargeTypeRequest import ModifyDiskChargeTypeRequest
from aliyunsdkecs.request.v20140526.ModifyDiskSpecRequest import ModifyDiskSpecRequest
from aliyunsdkecs.request.v20140526.ModifyEipAddressAttributeRequest import ModifyEipAddressAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyForwardEntryRequest import ModifyForwardEntryRequest
from aliyunsdkecs.request.v20140526.ModifyHaVipAttributeRequest import ModifyHaVipAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyHpcClusterAttributeRequest import ModifyHpcClusterAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyImageAttributeRequest import ModifyImageAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyImageShareGroupPermissionRequest import ModifyImageShareGroupPermissionRequest
from aliyunsdkecs.request.v20140526.ModifyImageSharePermissionRequest import ModifyImageSharePermissionRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceAttributeRequest import ModifyInstanceAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceAutoReleaseTimeRequest import ModifyInstanceAutoReleaseTimeRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceAutoRenewAttributeRequest import ModifyInstanceAutoRenewAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceChargeTypeRequest import ModifyInstanceChargeTypeRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceDeploymentRequest import ModifyInstanceDeploymentRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceMaintenanceAttributesRequest import ModifyInstanceMaintenanceAttributesRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceNetworkSpecRequest import ModifyInstanceNetworkSpecRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceSpecRequest import ModifyInstanceSpecRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceVncPasswdRequest import ModifyInstanceVncPasswdRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceVpcAttributeRequest import ModifyInstanceVpcAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyLaunchTemplateDefaultVersionRequest import ModifyLaunchTemplateDefaultVersionRequest
from aliyunsdkecs.request.v20140526.ModifyNetworkInterfaceAttributeRequest import ModifyNetworkInterfaceAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyPhysicalConnectionAttributeRequest import ModifyPhysicalConnectionAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyPrepayInstanceSpecRequest import ModifyPrepayInstanceSpecRequest
from aliyunsdkecs.request.v20140526.ModifyReservedInstanceAttributeRequest import ModifyReservedInstanceAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyReservedInstancesRequest import ModifyReservedInstancesRequest
from aliyunsdkecs.request.v20140526.ModifyRouterInterfaceAttributeRequest import ModifyRouterInterfaceAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyRouterInterfaceSpecRequest import ModifyRouterInterfaceSpecRequest
from aliyunsdkecs.request.v20140526.ModifySecurityGroupAttributeRequest import ModifySecurityGroupAttributeRequest
from aliyunsdkecs.request.v20140526.ModifySecurityGroupEgressRuleRequest import ModifySecurityGroupEgressRuleRequest
from aliyunsdkecs.request.v20140526.ModifySecurityGroupPolicyRequest import ModifySecurityGroupPolicyRequest
from aliyunsdkecs.request.v20140526.ModifySecurityGroupRuleRequest import ModifySecurityGroupRuleRequest
from aliyunsdkecs.request.v20140526.ModifySnapshotAttributeRequest import ModifySnapshotAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyStorageSetAttributeRequest import ModifyStorageSetAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyUserBusinessBehaviorRequest import ModifyUserBusinessBehaviorRequest
from aliyunsdkecs.request.v20140526.ModifyVRouterAttributeRequest import ModifyVRouterAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyVSwitchAttributeRequest import ModifyVSwitchAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyVirtualBorderRouterAttributeRequest import ModifyVirtualBorderRouterAttributeRequest
from aliyunsdkecs.request.v20140526.ModifyVpcAttributeRequest import ModifyVpcAttributeRequest
from aliyunsdkecs.request.v20140526.PurchaseReservedInstancesOfferingRequest import PurchaseReservedInstancesOfferingRequest
from aliyunsdkecs.request.v20140526.ReActivateInstancesRequest import ReActivateInstancesRequest
from aliyunsdkecs.request.v20140526.ReInitDiskRequest import ReInitDiskRequest
from aliyunsdkecs.request.v20140526.RebootInstanceRequest import RebootInstanceRequest
from aliyunsdkecs.request.v20140526.RecoverVirtualBorderRouterRequest import RecoverVirtualBorderRouterRequest
from aliyunsdkecs.request.v20140526.RedeployDedicatedHostRequest import RedeployDedicatedHostRequest
from aliyunsdkecs.request.v20140526.RedeployInstanceRequest import RedeployInstanceRequest
from aliyunsdkecs.request.v20140526.ReleaseDedicatedHostRequest import ReleaseDedicatedHostRequest
from aliyunsdkecs.request.v20140526.ReleaseEipAddressRequest import ReleaseEipAddressRequest
from aliyunsdkecs.request.v20140526.ReleasePublicIpAddressRequest import ReleasePublicIpAddressRequest
from aliyunsdkecs.request.v20140526.RemoveBandwidthPackageIpsRequest import RemoveBandwidthPackageIpsRequest
from aliyunsdkecs.request.v20140526.RemoveTagsRequest import RemoveTagsRequest
from aliyunsdkecs.request.v20140526.RenewDedicatedHostsRequest import RenewDedicatedHostsRequest
from aliyunsdkecs.request.v20140526.RenewInstanceRequest import RenewInstanceRequest
from aliyunsdkecs.request.v20140526.ReplaceSystemDiskRequest import ReplaceSystemDiskRequest
from aliyunsdkecs.request.v20140526.ReportInstancesStatusRequest import ReportInstancesStatusRequest
from aliyunsdkecs.request.v20140526.ResetDiskRequest import ResetDiskRequest
from aliyunsdkecs.request.v20140526.ResizeDiskRequest import ResizeDiskRequest
from aliyunsdkecs.request.v20140526.RevokeSecurityGroupEgressRequest import RevokeSecurityGroupEgressRequest
from aliyunsdkecs.request.v20140526.RevokeSecurityGroupRequest import RevokeSecurityGroupRequest
from aliyunsdkecs.request.v20140526.RunCommandRequest import RunCommandRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
from aliyunsdkecs.request.v20140526.StopInvocationRequest import StopInvocationRequest
from aliyunsdkecs.request.v20140526.TagResourcesRequest import TagResourcesRequest
from aliyunsdkecs.request.v20140526.TerminatePhysicalConnectionRequest import TerminatePhysicalConnectionRequest
from aliyunsdkecs.request.v20140526.TerminateVirtualBorderRouterRequest import TerminateVirtualBorderRouterRequest
from aliyunsdkecs.request.v20140526.UnassignIpv6AddressesRequest import UnassignIpv6AddressesRequest
from aliyunsdkecs.request.v20140526.UnassignPrivateIpAddressesRequest import UnassignPrivateIpAddressesRequest
from aliyunsdkecs.request.v20140526.UnassociateEipAddressRequest import UnassociateEipAddressRequest
from aliyunsdkecs.request.v20140526.UnassociateHaVipRequest import UnassociateHaVipRequest
from aliyunsdkecs.request.v20140526.UntagResourcesRequest import UntagResourcesRequest

def desc_ECS_insts():
    request = DescribeInstancesRequest()
    request.set_accept_format('json')

    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))


@result_mapper(
    lambda x: {
        'Instances': x['Instances']['Instance'],
        'TotalCount': x['TotalCount'],
        'PageSize': x['PageSize'],
        'PageNumber': x['PageNumber']
    }
)
@desc_it
def get_instances(status='Running', pageSize=100):
    r = DescribeInstancesRequest()
    r.set_Status('Running')
    r.set_PageSize(pageSize)
    return r


@desc_it
def DescRegionsRequest():
    request = DescribeRegionsRequest()
    request.set_accept_format('json')
    return request

if __name__ == '__main__':
    # desc_ECS_insts()
    import json
    def build_for_zabbix(instance):
        return {
            "{#ALI_INSTANCE_NAME}": instance['InstanceName'],
            "{#ALI_INSTANCE_ID}": instance['InstanceId'],
            "{#ALI_INSTANCE_MAIN_IP}": instance['NetworkInterfaces']['NetworkInterface'][0]['PrimaryIpAddress'],
        }
    ins =  get_instances()
    print(
        json.dumps(
            list(map(build_for_zabbix, ins['Instances'])),
            indent=2
        )
    )
