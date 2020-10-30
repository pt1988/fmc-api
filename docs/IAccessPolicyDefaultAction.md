# IAccessPolicyDefaultAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_end** | **bool** | Boolean indicating whether the device will log events at the end of the connection. Default is false. | [optional] 
**log_begin** | **bool** | Boolean indicating whether the device will log events at the beginning of the connection. Default is false. | [optional] 
**metadata** | [**IMetadata**](IMetadata.md) | Object representing metadata properties of response object. | [optional] 
**snmp_config** | [**IReference**](IReference.md) | Object representing the SNMP alert associated with the access rule. | [optional] 
**intrusion_policy** | [**IIntrusionPolicyModel**](IIntrusionPolicyModel.md) |  | [optional] 
**send_events_to_fmc** | **bool** | Boolean indicating whether the device will send events to the Firepower Management Center event viewer. Default is false. | [optional] 
**description** | **str** | User provided description. | [optional] 
**type** | **str** | Response object associated with resource. | [optional] 
**variable_set** | [**IReference**](IReference.md) | Object representing the variable set associated with the access rule. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**syslog_config** | [**IReference**](IReference.md) | Object representing the syslog alert associated with the access rule. | [optional] 
**name** | **str** | User chosen resource name. | [optional] 
**action** | **str** | Specifies the action to take when the conditions defined by the rule are met. One of: BLOCK | TRUST | NETWORK_DISCOVERY | PERMIT. | 
**links** | [**ILinks**](ILinks.md) | Object containing links to this resource. | [optional] 
**id** | **str** | Unique identifier representing resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


