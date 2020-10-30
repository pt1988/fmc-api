# swagger_client.UpdatesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_upgrade**](UpdatesApi.md#create_upgrade) | **POST** /api/fmc_platform/v1/updates/upgrades | 
[**delete_upgrade_package**](UpdatesApi.md#delete_upgrade_package) | **DELETE** /api/fmc_platform/v1/updates/upgradepackages/{objectId} | 
[**get_all_applicable_device**](UpdatesApi.md#get_all_applicable_device) | **GET** /api/fmc_platform/v1/updates/upgradepackages/{containerUUID}/applicabledevices | 
[**get_all_upgrade_package**](UpdatesApi.md#get_all_upgrade_package) | **GET** /api/fmc_platform/v1/updates/upgradepackages | 
[**get_upgrade_package**](UpdatesApi.md#get_upgrade_package) | **GET** /api/fmc_platform/v1/updates/upgradepackages/{objectId} | 


# **create_upgrade**
> Upgrade create_upgrade(body)



**API to trigger upgrade. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdatesApi()
body = swagger_client.Upgrade() # Upgrade | The input representation of Upgrade object model.

try:
    api_response = api_instance.create_upgrade(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesApi->create_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Upgrade**](Upgrade.md)| The input representation of Upgrade object model. | 

### Return type

[**Upgrade**](Upgrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upgrade_package**
> UpgradePackage delete_upgrade_package(object_id)



**API operation for listing upgrade packages. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdatesApi()
object_id = 'object_id_example' # str | Unique identifier of the object.

try:
    api_response = api_instance.delete_upgrade_package(object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesApi->delete_upgrade_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the object. | 

### Return type

[**UpgradePackage**](UpgradePackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_applicable_device**
> ApplicableDeviceListContainer get_all_applicable_device(container_uuid, offset=offset, limit=limit, expanded=expanded)



**Devices available for a particular upgrade package.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdatesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_applicable_device(container_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesApi->get_all_applicable_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**ApplicableDeviceListContainer**](ApplicableDeviceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_upgrade_package**
> UpgradePackageListContainer get_all_upgrade_package(offset=offset, limit=limit, expanded=expanded)



**API operation for listing upgrade packages.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdatesApi()
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_upgrade_package(offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesApi->get_all_upgrade_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**UpgradePackageListContainer**](UpgradePackageListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_package**
> UpgradePackage get_upgrade_package(object_id)



**API operation for listing upgrade packages.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdatesApi()
object_id = 'object_id_example' # str | Unique identifier of the object.

try:
    api_response = api_instance.get_upgrade_package(object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdatesApi->get_upgrade_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the object. | 

### Return type

[**UpgradePackage**](UpgradePackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

