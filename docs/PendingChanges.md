# PendingChanges

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**IMetadata**](IMetadata.md) |  | [optional] 
**entity_uuid** | **str** |  An identifier of entity which does not change with time. | [optional] 
**entity_type** | **str** | An Entity type type that has been modified. | [optional] 
**value_updated** | [**list[IValueUpdate]**](IValueUpdate.md) | Values that were specified compared to its other state.  | [optional] 
**message** | **str** | In case for an entity there is no diff, due to no modification or some error during generation proper message will be given for that entity. | [optional] 
**version** | **str** |  | [optional] 
**value_deleted** | [**list[IValueDelete]**](IValueDelete.md) | Values that were deleted compared to its other state. | [optional] 
**parent_uuid** | **str** | UUID of the entity to which this entity is grouped to. If it&#39;s empty, it means the entity is the parent entity. | [optional] 
**references_deleted** | [**list[IReferenceUpdate]**](IReferenceUpdate.md) | References that were deleted compared to its other state. | [optional] 
**value_added** | [**list[IValueAdd]**](IValueAdd.md) | Values that were added compared to its other state.  | [optional] 
**entity_name** | **str** | A name field value of modified Entity.  | [optional] 
**action** | **str** | Action done on the entity | [optional] 
**links** | [**ILinks**](ILinks.md) |  | [optional] 
**references_added** | [**list[IReferenceUpdate]**](IReferenceUpdate.md) | References that were added compared to its other state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


