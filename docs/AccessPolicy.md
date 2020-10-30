# AccessPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Object representing metadata attributes for the access control policy. | [optional] 
**default_action** | [**IAccessPolicyDefaultAction**](IAccessPolicyDefaultAction.md) | Object representing the default action (AccessPolicyDefaultAction). The default action determines how the system handles and logs traffic not handled by any other access control rules. For more information, see the defaultactions service. | 
**name** | **str** | User-specified name of the access control policy. | [optional] 
**description** | **str** | Description of Access Policy | [optional] 
**links** | [**Links**](Links.md) | Object containing links to this resource. | [optional] 
**rules** | **object** | Object containing a list of rules in the access control policy. | [optional] 
**prefilter_policy_setting** | [**IAccessPolicyPrefilterPolicySettingModel**](IAccessPolicyPrefilterPolicySettingModel.md) |  | [optional] 
**id** | **str** | Unique identifier (UUID) representing the access control policy. | [optional] 
**type** | **str** | Type of the access control policy; this value is always AccessPolicy. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


