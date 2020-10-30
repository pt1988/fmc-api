# RangeObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Object representing metadata properties of response object. | [optional] 
**overridable** | **bool** | Boolean indicating whether object values can be overridden. | [optional] 
**name** | **str** | User chosen resource name. | [optional] 
**description** | **str** | User provided description. | [optional] 
**links** | [**Links**](Links.md) | Contains the full URL to the current object and its parent (if any) | [optional] 
**overrides** | [**IOverride**](IOverride.md) | This is populated only if this object is an override and contains the parent (global) object id and whether this is an override on device or domain. | [optional] 
**id** | **str** | Unique identifier representing resource. | [optional] 
**type** | **str** | The unique type of this object. | [optional] 
**value** | **str** | Actual value of range. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**override_target_id** | **str** | Unique identifier of domain or device when override assigned to child domain. Used as path query parameter to GET override details for a specific object on a specific target (device or domain). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


