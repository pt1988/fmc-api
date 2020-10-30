# FTDHADeviceContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**IMetadata**](IMetadata.md) | Object representing metadata properties | [optional] 
**model_id** | **str** | Model ID of the FTD Devices used in FTD HA pair. | [optional] 
**advanced** | [**IAdvanced**](IAdvanced.md) | Object representing Device Advanced Configuration. | [optional] 
**description** | **str** | Retrieves or modifies the FTD HA record associated with the specified ID. Creates or breaks or deletes a FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA pairs. | [optional] 
**ftd_ha_failover_trigger_criteria** | [**IFTDHAFailoverInterfacePolicyTrigger**](IFTDHAFailoverInterfacePolicyTrigger.md) | Conditions on which HA failover would be triggered. | [optional] 
**model_type** | **str** | Model type of the FTD Devices used in FTD HA pair. | [optional] 
**type** | **str** | DeviceHAPair. | [optional] 
**version** | **str** | FTD HA model version. | [optional] 
**ftd_ha_bootstrap** | [**IFTDDeviceHABootStrap**](IFTDDeviceHABootStrap.md) | FTD HA Bootstrap object used during POST operation. | 
**sw_version** | **str** | FTD HA device version. | [optional] 
**secondary** | [**IBaseDevice**](IBaseDevice.md) | Represents the secondary device. | 
**health_status** | **str** | Health status of the FTD Devices used in FTD HA pair. | [optional] 
**health_policy** | [**IHealthPolicy**](IHealthPolicy.md) | Health Policy of the FTD Devices used in FTD HA pair. | [optional] 
**name** | **str** | User-chosen name. | [optional] 
**action** | **str** | FTD HA PUT operation action. Specifically used for breaking FTD HA or manual switch. | [optional] 
**links** | [**ILinks**](ILinks.md) | Object containing related links. | [optional] 
**model** | **str** | FTDHADeviceContainer | [optional] 
**model_number** | **str** | Model Number of the FTD Devices used in FTD HA pair. | [optional] 
**force_break** | **bool** | FTD HA Force Break option. | [optional] 
**id** | **str** | FTD HA container UUID. | [optional] 
**access_policy** | [**IPolicyModel**](IPolicyModel.md) | Object representing the access control policy associated with device | [optional] 
**primary** | [**IBaseDevice**](IBaseDevice.md) | Primary Device object for FTD HA. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


