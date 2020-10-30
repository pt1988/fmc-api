# swagger_client.DeploymentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment_request**](DeploymentApi.md#create_deployment_request) | **POST** /api/fmc_config/v1/domain/{domainUUID}/deployment/deploymentrequests | 
[**get_deployable_device**](DeploymentApi.md#get_deployable_device) | **GET** /api/fmc_config/v1/domain/{domainUUID}/deployment/deployabledevices | 
[**get_pending_changes**](DeploymentApi.md#get_pending_changes) | **GET** /api/fmc_config/v1/domain/{domainUUID}/deployment/deployabledevices/{containerUUID}/pendingchanges | 


# **create_deployment_request**
> DeploymentRequest create_deployment_request(body, domain_uuid)



**Creates a request for deploying configuration changes to devices. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeploymentApi()
body = swagger_client.DeploymentRequest() # DeploymentRequest | JSON data for deploying to devices.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_deployment_request(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->create_deployment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeploymentRequest**](DeploymentRequest.md)| JSON data for deploying to devices. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**DeploymentRequest**](DeploymentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployable_device**
> DeployableDeviceListContainer get_deployable_device(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of all devices with configuration changes, ready to be deployed.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeploymentApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_deployable_device(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_deployable_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**DeployableDeviceListContainer**](DeployableDeviceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_changes**
> PendingChangesListContainer get_pending_changes(container_uuid, domain_uuid, filter=filter, offset=offset, limit=limit, expanded=expanded)



**Retrieves all the policy and object changes for the selected device.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeploymentApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
filter = 'filter_example' # str | The filter criteria for which the details have to be fetched - Only works when \"expanded\" is set to \"true\". Examples: ParentEntityTypes:AccessPolicy, ParentEntityTypes:RAVPNTopology, EntityUUID:0050568C-35A0-0ed3-0000-004294969351 (optional)
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_pending_changes(container_uuid, domain_uuid, filter=filter, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_pending_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **filter** | **str**| The filter criteria for which the details have to be fetched - Only works when \&quot;expanded\&quot; is set to \&quot;true\&quot;. Examples: ParentEntityTypes:AccessPolicy, ParentEntityTypes:RAVPNTopology, EntityUUID:0050568C-35A0-0ed3-0000-004294969351 | [optional] 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**PendingChangesListContainer**](PendingChangesListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

