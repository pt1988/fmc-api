# swagger_client.IntegrationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_lookup**](IntegrationApi.md#create_external_lookup) | **POST** /api/fmc_config/v1/domain/{domainUUID}/integration/externallookups | 
[**delete_external_lookup**](IntegrationApi.md#delete_external_lookup) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/integration/externallookups/{objectId} | 
[**get_all_cloud_events**](IntegrationApi.md#get_all_cloud_events) | **GET** /api/fmc_config/v1/domain/{domainUUID}/integration/cloudeventsconfigs | 
[**get_all_cloud_region**](IntegrationApi.md#get_all_cloud_region) | **GET** /api/fmc_config/v1/domain/{domainUUID}/integration/cloudregions | 
[**get_all_external_lookup**](IntegrationApi.md#get_all_external_lookup) | **GET** /api/fmc_config/v1/domain/{domainUUID}/integration/externallookups | 
[**get_cloud_events**](IntegrationApi.md#get_cloud_events) | **GET** /api/fmc_config/v1/domain/{domainUUID}/integration/cloudeventsconfigs/{objectId} | 
[**get_cloud_region**](IntegrationApi.md#get_cloud_region) | **GET** /api/fmc_config/v1/domain/{domainUUID}/integration/cloudregions/{objectId} | 
[**get_external_lookup**](IntegrationApi.md#get_external_lookup) | **GET** /api/fmc_config/v1/domain/{domainUUID}/integration/externallookups/{objectId} | 
[**update_cloud_events**](IntegrationApi.md#update_cloud_events) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/integration/cloudeventsconfigs/{objectId} | 
[**update_cloud_region**](IntegrationApi.md#update_cloud_region) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/integration/cloudregions/{objectId} | 
[**update_external_lookup**](IntegrationApi.md#update_external_lookup) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/integration/externallookups/{objectId} | 


# **create_external_lookup**
> ExternalLookup create_external_lookup(body, domain_uuid)



**Retrieves, deletes, creates, or modifies the external lookup associated with the specified ID. If no ID is specified for a GET, retrieves list of all external lookups. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
body = swagger_client.ExternalLookup() # ExternalLookup | Input representation of external lookup.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_external_lookup(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->create_external_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalLookup**](ExternalLookup.md)| Input representation of external lookup. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**ExternalLookup**](ExternalLookup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_lookup**
> ExternalLookup delete_external_lookup(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the external lookup associated with the specified ID. If no ID is specified for a GET, retrieves list of all external lookups. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
object_id = 'object_id_example' # str | Identifier for an external lookup.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_external_lookup(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->delete_external_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for an external lookup. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**ExternalLookup**](ExternalLookup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cloud_events**
> CloudEventsListContainer get_all_cloud_events(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the cloud event configuration associated with the specified ID. If no ID is specified for a GET, retrieves a list of the singleton cloud event configuration object.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_cloud_events(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_all_cloud_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**CloudEventsListContainer**](CloudEventsListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cloud_region**
> CloudRegionListContainer get_all_cloud_region(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the cloud region configuration associated with the specified ID. If no ID is specified for a GET, retrieves list of all cloud regions.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_cloud_region(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_all_cloud_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**CloudRegionListContainer**](CloudRegionListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_external_lookup**
> ExternalLookupListContainer get_all_external_lookup(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the external lookup associated with the specified ID. If no ID is specified for a GET, retrieves list of all external lookups.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_external_lookup(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_all_external_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**ExternalLookupListContainer**](ExternalLookupListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_events**
> CloudEvents get_cloud_events(object_id, domain_uuid)



**Retrieves or modifies the cloud event configuration associated with the specified ID. If no ID is specified for a GET, retrieves a list of the singleton cloud event configuration object.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
object_id = 'object_id_example' # str | Identifier for cloud event configuration.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_cloud_events(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_cloud_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for cloud event configuration. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**CloudEvents**](CloudEvents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_region**
> CloudRegion get_cloud_region(object_id, domain_uuid)



**Retrieves or modifies the cloud region configuration associated with the specified ID. If no ID is specified for a GET, retrieves list of all cloud regions.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
object_id = 'object_id_example' # str | Identifier for a cloud region.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_cloud_region(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_cloud_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for a cloud region. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**CloudRegion**](CloudRegion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_lookup**
> ExternalLookup get_external_lookup(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the external lookup associated with the specified ID. If no ID is specified for a GET, retrieves list of all external lookups.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
object_id = 'object_id_example' # str | Identifier for an external lookup.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_external_lookup(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_external_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for an external lookup. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**ExternalLookup**](ExternalLookup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_events**
> CloudEvents update_cloud_events(object_id, body, domain_uuid)



**Retrieves or modifies the cloud event configuration associated with the specified ID. If no ID is specified for a GET, retrieves a list of the singleton cloud event configuration object. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
object_id = 'object_id_example' # str | Identifier for cloud event configuration.
body = swagger_client.CloudEvents() # CloudEvents | Input representation of cloud event configuration.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_cloud_events(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_cloud_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for cloud event configuration. | 
 **body** | [**CloudEvents**](CloudEvents.md)| Input representation of cloud event configuration. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**CloudEvents**](CloudEvents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_region**
> CloudRegion update_cloud_region(object_id, body, domain_uuid)



**Retrieves or modifies the cloud region configuration associated with the specified ID. If no ID is specified for a GET, retrieves list of all cloud regions. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
object_id = 'object_id_example' # str | Identifier for a cloud region.
body = swagger_client.CloudRegion() # CloudRegion | Input representation of cloud region.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_cloud_region(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_cloud_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for a cloud region. | 
 **body** | [**CloudRegion**](CloudRegion.md)| Input representation of cloud region. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**CloudRegion**](CloudRegion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_lookup**
> ExternalLookup update_external_lookup(object_id, body, domain_uuid)



**Retrieves, deletes, creates, or modifies the external lookup associated with the specified ID. If no ID is specified for a GET, retrieves list of all external lookups. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationApi()
object_id = 'object_id_example' # str | Identifier for an external lookup.
body = swagger_client.ExternalLookup() # ExternalLookup | Input representation of external lookup.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_external_lookup(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->update_external_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for an external lookup. | 
 **body** | [**ExternalLookup**](ExternalLookup.md)| Input representation of external lookup. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**ExternalLookup**](ExternalLookup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

