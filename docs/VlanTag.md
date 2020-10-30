# VlanTag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Object representing metadata properties of response object. | [optional] 
**data** | [**IVlanTagLiteral**](IVlanTagLiteral.md) | Object containing starting and ending VLAN identifier (VID) specifying the VLAN to which the frame belongs. | [optional] 
**overridable** | **bool** | Boolean indicating whether object values can be overridden. | [optional] 
**name** | **str** | User assigned resource name. | [optional] 
**description** | **str** | User provided resource description. | [optional] 
**links** | [**Links**](Links.md) | Object containing related links. | [optional] 
**overrides** | [**IOverride**](IOverride.md) | An object override allows you to define an alternate value for an object. | [optional] 
**id** | **str** | Unique identifier representing response object. | [optional] 
**type** | **str** | Type associated with resource. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**override_target_id** | **str** | Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


