# HitCount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**HitCountMetadata**](HitCountMetadata.md) | Object representing metadata attributes for the hit count entry. | [optional] 
**last_fetch_time_stamp** | **str** | Indicates the last time (in ISO 8601 format) the hit count was retrieved for the mentioned rule. | [optional] 
**hit_count** | **int** | Indicates the number of times the access control rule was hit on the target device. It is based on the data from the last FMC hit count refresh operation. | [optional] 
**first_hit_time_stamp** | **str** | Indicates the time (in ISO 8601 format) when the hit count was first hit for the mentioned rule. | [optional] 
**rule** | [**IPolicyModel**](IPolicyModel.md) | Object representing the access control rule against which the hit count information is retrieved. | [optional] 
**last_hit_time_stamp** | **str** | Indicates the time (in ISO 8601 format) when the hit count was last hit for the mentioned rule. | [optional] 
**description** | **str** |  | [optional] 
**links** | [**ILinks**](ILinks.md) | Object containing links to this resource. | [optional] 
**type** | **str** | Type must be HitCount. | [optional] 
**version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


