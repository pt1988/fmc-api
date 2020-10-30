# swagger_client.DeviceGroupsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_group**](DeviceGroupsApi.md#create_device_group) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devicegroups/devicegrouprecords | 
[**delete_device_group**](DeviceGroupsApi.md#delete_device_group) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devicegroups/devicegrouprecords/{objectId} | 
[**get_all_device_group**](DeviceGroupsApi.md#get_all_device_group) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devicegroups/devicegrouprecords | 
[**get_device_group**](DeviceGroupsApi.md#get_device_group) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devicegroups/devicegrouprecords/{objectId} | 
[**update_device_group**](DeviceGroupsApi.md#update_device_group) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devicegroups/devicegrouprecords/{objectId} | 


# **create_device_group**
> DeviceGroup create_device_group(body, domain_uuid)



**Retrieves, deletes, creates, or modifies the device group associated with the specified ID. If no ID is specified for a GET, retrieves list of all device groups. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
body = swagger_client.DeviceGroup() # DeviceGroup | Input representation of device group.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_device_group(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->create_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroup**](DeviceGroup.md)| Input representation of device group. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group**
> DeviceGroup delete_device_group(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the device group associated with the specified ID. If no ID is specified for a GET, retrieves list of all device groups. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
object_id = 'object_id_example' # str | Identifier for a device group.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_device_group(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->delete_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for a device group. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_device_group**
> DeviceGroupListContainer get_all_device_group(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the device group associated with the specified ID. If no ID is specified for a GET, retrieves list of all device groups.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_device_group(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_all_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**DeviceGroupListContainer**](DeviceGroupListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group**
> DeviceGroup get_device_group(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the device group associated with the specified ID. If no ID is specified for a GET, retrieves list of all device groups.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
object_id = 'object_id_example' # str | Identifier for a device group.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_device_group(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for a device group. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group**
> DeviceGroup update_device_group(object_id, body, domain_uuid)



**Retrieves, deletes, creates, or modifies the device group associated with the specified ID. If no ID is specified for a GET, retrieves list of all device groups. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
object_id = 'object_id_example' # str | Identifier for a device group.
body = swagger_client.DeviceGroup() # DeviceGroup | Input representation of device group.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_device_group(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->update_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for a device group. | 
 **body** | [**DeviceGroup**](DeviceGroup.md)| Input representation of device group. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

