# swagger_client.StatusApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_status**](StatusApi.md#get_task_status) | **GET** /api/fmc_config/v1/domain/{domainUUID}/job/taskstatuses/{objectId} | 


# **get_task_status**
> TaskStatus get_task_status(object_id, domain_uuid)



**Retrieves information about a previously submitted pending job/task with the specified ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusApi()
object_id = 'object_id_example' # str | UUID of request.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_task_status(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->get_task_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| UUID of request. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**TaskStatus**](TaskStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

