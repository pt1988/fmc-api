# AccessPolicyCategoryMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_index** | **int** | Index of the first Access Rule inside the category. Index will be -1 if there are no rules in category | [optional] 
**last_user** | [**MetadataUser**](MetadataUser.md) | The last user who modified this instance. | [optional] 
**end_index** | **int** | Index of the last Access Rule inside the category. Index will be -1 if there are no rules in category | [optional] 
**domain** | [**Domain**](Domain.md) | Object representing the domain under which the operation has been performed. | [optional] 
**read_only** | [**ReadOnly**](ReadOnly.md) | Details regarding the read only status of this instance. | [optional] 
**section** | **str** | Specifies the section into which the rules will be added. Only &#39;mandatory&#39; and &#39;default&#39; are allowed values. If none of the parameters are specified category will be added to &#39;default&#39; section | [optional] 
**access_policy** | [**IReference**](IReference.md) | Object representing the access control containing the rule. | [optional] 
**timestamp** | **int** | The last updated timestamp. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


