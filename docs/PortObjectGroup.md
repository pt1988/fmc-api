# PortObjectGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PortMetadata**](PortMetadata.md) | Object representing metadata properties of response object. | [optional] 
**objects** | [**list[IPortObject]**](IPortObject.md) | Represents port objects in group. | [optional] 
**overridable** | **bool** | Boolean indicating whether object values can be overridden. | [optional] 
**name** | **str** | User-specified name of the policy assignment. | [optional] 
**description** | **str** | User provided description. | [optional] 
**links** | [**Links**](Links.md) | Object containing links to this resource. | [optional] 
**overrides** | [**IOverride**](IOverride.md) | An object override allows you to define an alternate value for an object. | [optional] 
**id** | **str** | Unique identifier representing resource. | [optional] 
**type** | **str** | Type associated with resource. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**override_target_id** | **str** | Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


