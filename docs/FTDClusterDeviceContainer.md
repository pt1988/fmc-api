# FTDClusterDeviceContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_device** | [**IDevice**](IDevice.md) | Current master device ID | 
**metadata** | [**IMetadata**](IMetadata.md) | Object representing metadata properties of response object. | [optional] 
**model_id** | **str** | Model ID | [optional] 
**advanced** | [**IAdvanced**](IAdvanced.md) | Object representing Device Advanced Configuration. | [optional] 
**description** | **str** | User provided resource description. | [optional] 
**slave_devices** | [**list[IDevice]**](IDevice.md) | List of slave devices | 
**model_type** | **str** | Model type of the registered device cluster. | [optional] 
**type** | **str** | Type associated with resource: DeviceCluster | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**sw_version** | **str** | FTD Cluster version | [optional] 
**health_status** | **str** | Current health status of the device, for e.g. green | [optional] 
**health_policy** | [**IHealthPolicy**](IHealthPolicy.md) | Object representing the system health policy applied to the registered device cluster. | [optional] 
**name** | **str** | FTD Cluster name. | [optional] 
**links** | [**ILinks**](ILinks.md) | Object containing related links. | [optional] 
**model** | **str** | Cisco device model name, for e.g. Cisco Firepower 9000 Series SM-24 Threat Defense | [optional] 
**model_number** | **str** | Model number of the registered device. | [optional] 
**id** | **str** | Unique identifier of response object. | [optional] 
**access_policy** | [**IPolicyModel**](IPolicyModel.md) | Object representing the currently assigned access control policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


