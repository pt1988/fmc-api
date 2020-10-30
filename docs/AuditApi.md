# swagger_client.AuditApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_audit_model**](AuditApi.md#get_all_audit_model) | **GET** /api/fmc_platform/v1/domain/{domainUUID}/audit/auditrecords | 
[**get_audit_model**](AuditApi.md#get_audit_model) | **GET** /api/fmc_platform/v1/domain/{domainUUID}/audit/auditrecords/{objectId} | 


# **get_all_audit_model**
> AuditModelListContainer get_all_audit_model(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**API Operations on audit objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuditApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_audit_model(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_all_audit_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**AuditModelListContainer**](AuditModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_model**
> AuditModel get_audit_model(object_id, domain_uuid)



**API Operations on audit objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuditApi()
object_id = 'object_id_example' # str | Unique identifier of the object.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_audit_model(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the object. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AuditModel**](AuditModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

