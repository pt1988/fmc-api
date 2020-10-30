# IRecurrence

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_start_time** | **str** | Represents the time (in ISO 8601 format) at which the time range starts being effective. This field must be used if recurrenceType is specified as RANGE. | 
**range_end_day** | **str** | Represents the time (in ISO 8601 format) at which the time range stops being effective. This field must be used if recurrenceType is specified as RANGE. | 
**range_end_time** | **str** | Represents the day of week at which the time range stops being effective. This field must be used if recurrenceType is specified as RANGE. | 
**range_start_day** | **str** | Represents the day of week at which the time range starts being effective. This field must be used if recurrenceType is specified as RANGE. | 
**daily_start_time** | **str** | Represents the time (in ISO 8601 format) at which the time range starts being effective on selected days. This field must be used if recurrenceType is specified as DAILY_INTERVAL. | 
**days** | **list[str]** | Represents the days of week on which the time range is effective. This field must be used if recurrenceType is specified as DAILY_INTERVAL. | 
**daily_end_time** | **str** | Represents the time (in ISO 8601 format) at which the time range stops being effective on selected days. This field must be used if recurrenceType is specified as DAILY_INTERVAL. | 
**recurrence_type** | **str** | Type of the recurrence interval. This value can be either DAILY_INTERVAL or RANGE. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


