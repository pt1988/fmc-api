# PrefilterPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Object representing metadata attributes for the prefilter policy. | [optional] 
**default_action** | [**IPrefilterPolicyDefaultAction**](IPrefilterPolicyDefaultAction.md) | Object representing the default action (PrefilterPolicyDefaultAction). The default action determines how the system handles and logs traffic not handled by any other prefilter rules. For more information, see the defaultactions service. | [optional] 
**name** | **str** | User-specified name of the prefilter policy. | [optional] 
**description** | **str** | User provided resource description. | [optional] 
**links** | [**Links**](Links.md) | Object containing links to this resource. | [optional] 
**rules** | **object** | Object containing a list of rules in the prefilter policy. | [optional] 
**id** | **str** | Unique identifier (UUID) representing the prefilter policy. | [optional] 
**type** | **str** | Type of the prefilter policy; this value is always PrefilterPolicy. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


