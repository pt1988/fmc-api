# TimeZoneObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Object representing metadata properties of the response object. | [optional] 
**time_zone_id** | **str** | Unique identifier of the global time zone from the IANA time zone (tz) database. | [optional] 
**time_zone** | **str** | Read-only field containing description of the specified global time zone (timeZoneId). | [optional] 
**description** | **str** | User provided resource description.  | [optional] 
**overrides** | [**IOverride**](IOverride.md) | An object override allows you to define an alternate value for an object on a device or domain. | [optional] 
**type** | **str** | Type of the response object. This value is always TimeZoneObject. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**override_target_id** | **str** | Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain). | [optional] 
**dst_date_range** | [**ITimeZoneDateRangeFragment**](ITimeZoneDateRangeFragment.md) | Object representing the daylight saving configuration by date range. Either dstDateRange or dstDayRecurrence field must be configured to enable daylight saving for the object. | [optional] 
**dst_day_recurrence** | [**ITimeZoneDayRecurrenceFragment**](ITimeZoneDayRecurrenceFragment.md) | Object representing the daylight saving configuration by day-based recurrence. Either dstDateRange or dstDayRecurrence field must be configured to enable daylight saving. | [optional] 
**name** | **str** | User assigned resource name. | [optional] 
**overridable** | **bool** | Boolean indicating whether object values can be overridden. | [optional] 
**links** | [**Links**](Links.md) | Object containing related links. | [optional] 
**id** | **str** | Unique identifier representing response object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


