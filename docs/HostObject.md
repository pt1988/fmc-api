# HostObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Defines read only details about the object - whether it is system defined, last user who modified the object etc. | [optional] 
**overridable** | **bool** | Set to &#39;true&#39; if the object can be overridden, &#39;false&#39; otherwise. | [optional] 
**name** | **str** |  The unique name for the object. | [optional] 
**description** | **str** | A description about the object. | [optional] 
**links** | [**Links**](Links.md) | Contains the full URL to the current object and its parent (if any) | [optional] 
**overrides** | [**IOverride**](IOverride.md) | This is populated only if this object is an override and contains the parent (global) object id and whether this is an override on device or domain. | [optional] 
**id** | **str** | The unique UUID of this object. | [optional] 
**type** | **str** | The unique type of this object (fixed). | [optional] 
**value** | **str** | The Host IP address value for this object. | [optional] 
**version** | **str** | The unique object version (if any). | [optional] 
**override_target_id** | **str** | The override target id either the device (UUID) or the domain (UUID) on which this override is created. Applicable only for overriden objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


