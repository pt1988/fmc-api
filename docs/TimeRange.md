# TimeRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Object representing metadata properties of the response object. | [optional] 
**effective_end_date_time** | **str** | Represents the absolute date and time (in ISO 8601 format) at which the time range object stops being effective. If not specified, value is considered, &#39;never ends&#39;. | [optional] 
**effective_start_date_time** | **str** | Represents the absolute date and time (in ISO 8601 format) at which the time range object starts being effective. If not specified, value is considered, &#39;starts now&#39;. | [optional] 
**name** | **str** | User assigned resource name. | 
**description** | **str** | User provided resource description. | [optional] 
**links** | [**Links**](Links.md) | Object containing related links. | [optional] 
**id** | **str** | Unique identifier representing response object. | [optional] 
**type** | **str** | Type of the response object. This value is always TimeRange. | [optional] 
**recurrence_list** | [**list[IRecurrence]**](IRecurrence.md) | Represents the list of recurring intervals during which the time range is effective. These intervals are valid only between effectiveStartDateTime and effectiveEndDateTime. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


