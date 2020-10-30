# AnyProtocolPortObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PortMetadata**](PortMetadata.md) | Object representing metadata properties. | [optional] 
**overridable** | **bool** | Boolean indicating whether object values can be overridden. | [optional] 
**name** | **str** | User chosen resource name. | [optional] 
**description** | **str** | User provided resource description.  | [optional] 
**links** | [**Links**](Links.md) | Object containing related links. | [optional] 
**overrides** | [**IOverride**](IOverride.md) | Represents an alternate value for an object on a device or domain. | [optional] 
**id** | **str** | Unique identifier. | [optional] 
**type** | **str** | Type associated with resource: AnyProtocolPortObject. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**override_target_id** | **str** | Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


