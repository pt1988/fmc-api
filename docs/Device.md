# Device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Hostname or IP address of the device. If the device is behind NAT, you can leave the host name as blank, and enter the NAT_ID string in the &#39;Unique NAT ID&#39; text box. Use the same NAT_ID string that you used while configuring FMC on the device. | 
**metadata** | [**IMetadata**](IMetadata.md) | Object representing metadata attributes of the Device. | [optional] 
**model_id** | **str** | Model ID of the registered device. | [optional] 
**advanced** | [**IAdvanced**](IAdvanced.md) | Object representing Device Advanced Configuration. | [optional] 
**nat_id** | **str** | Unique ID for a Network address translation (NAT) device (optional; used for device registration). If the device to be registered and the Firepower Management Center are separated by a NAT device, enter a unique NAT ID. | [optional] 
**description** | **str** | User-specified description of the registered device. | [optional] 
**license_caps** | **list[str]** | License capabilities on the managed device. | 
**ftd_mode** | **str** | FTD mode (Example: ROUTED or TRANSPARENT) | [optional] 
**model_type** | **str** | Model type of the registered device. | [optional] 
**type** | **str** | Type of the device; this value is always Device. | [optional] 
**reg_key** | **str** | Registration Key that you entered while configuring FMC on the device. | 
**keep_local_events** | **bool** | Boolean indicating whether local events are recorded and kept on the device. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**sw_version** | **str** | Device version | [optional] 
**health_status** | **str** | Current health status of the device. | [optional] 
**health_policy** | [**IHealthPolicy**](IHealthPolicy.md) | Object representing the system health policy applied to the registered device. | [optional] 
**name** | **str** | User-specified name of the registered device. (Example: Device 01 - 192.168.0.152.) | [optional] 
**links** | [**ILinks**](ILinks.md) | Object containing links to this resource. | [optional] 
**model** | **str** | Model name of the registered device. | [optional] 
**model_number** | **str** | Model number of the registered device. | [optional] 
**id** | **str** | Unique identifier (UUID) representing the registered device. | [optional] 
**access_policy** | [**IPolicyModel**](IPolicyModel.md) | Object representing the currently assigned access control policy. You need to specify an existing access control policy when registering a device. | [optional] 
**prohibit_packet_transfer** | **bool** | Boolean indicating whether to prohibit the registered device from sending packet data with events to the Firepower Management Center (true) or to allow transfer (false). If this field is set to false (the default), the device transfers packets when a certain event is triggered. Not all traffic data is sent; connection events do not include a payload, only connection metadata. | [optional] 
**device_group** | [**IDeviceGroup**](IDeviceGroup.md) | Object representing the device group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


