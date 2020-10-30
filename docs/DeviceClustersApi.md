# swagger_client.DeviceClustersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_ftd_cluster_device_container**](DeviceClustersApi.md#get_all_ftd_cluster_device_container) | **GET** /api/fmc_config/v1/domain/{domainUUID}/deviceclusters/ftddevicecluster | 
[**get_ftd_cluster_device_container**](DeviceClustersApi.md#get_ftd_cluster_device_container) | **GET** /api/fmc_config/v1/domain/{domainUUID}/deviceclusters/ftddevicecluster/{objectId} | 


# **get_all_ftd_cluster_device_container**
> FTDClusterDeviceContainerListContainer get_all_ftd_cluster_device_container(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the FTD Cluster record associated with the specified ID. If no ID is specified for a GET, retrieves list of all FTD Clusters.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceClustersApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_cluster_device_container(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceClustersApi->get_all_ftd_cluster_device_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**FTDClusterDeviceContainerListContainer**](FTDClusterDeviceContainerListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_cluster_device_container**
> FTDClusterDeviceContainer get_ftd_cluster_device_container(object_id, domain_uuid)



**Retrieves or modifies the FTD Cluster record associated with the specified ID. If no ID is specified for a GET, retrieves list of all FTD Clusters.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceClustersApi()
object_id = 'object_id_example' # str | Identifier of a FTD Cluster.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftd_cluster_device_container(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceClustersApi->get_ftd_cluster_device_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD Cluster. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDClusterDeviceContainer**](FTDClusterDeviceContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

