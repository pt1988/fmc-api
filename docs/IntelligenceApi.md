# swagger_client.IntelligenceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rest_discovery_info**](IntelligenceApi.md#create_rest_discovery_info) | **POST** /api/fmc_tid/v1/domain/{domainUUID}/taxiiconfig/discoveryinfo | 
[**create_rest_taxii_collection**](IntelligenceApi.md#create_rest_taxii_collection) | **POST** /api/fmc_tid/v1/domain/{domainUUID}/taxiiconfig/collections | 
[**create_rest_tid_source**](IntelligenceApi.md#create_rest_tid_source) | **POST** /api/fmc_tid/v1/domain/{domainUUID}/tid/source | 
[**delete_rest_incident**](IntelligenceApi.md#delete_rest_incident) | **DELETE** /api/fmc_tid/v1/domain/{domainUUID}/tid/incident/{objectId} | 
[**delete_rest_tid_source**](IntelligenceApi.md#delete_rest_tid_source) | **DELETE** /api/fmc_tid/v1/domain/{domainUUID}/tid/source/{objectId} | 
[**get_all_rest_element**](IntelligenceApi.md#get_all_rest_element) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/element | 
[**get_all_rest_incident**](IntelligenceApi.md#get_all_rest_incident) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/incident | 
[**get_all_rest_indicator**](IntelligenceApi.md#get_all_rest_indicator) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/indicator | 
[**get_all_rest_observable**](IntelligenceApi.md#get_all_rest_observable) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/observable | 
[**get_all_rest_tid_source**](IntelligenceApi.md#get_all_rest_tid_source) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/source | 
[**get_rest_element**](IntelligenceApi.md#get_rest_element) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/element/{objectId} | 
[**get_rest_incident**](IntelligenceApi.md#get_rest_incident) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/incident/{objectId} | 
[**get_rest_indicator**](IntelligenceApi.md#get_rest_indicator) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/indicator/{objectId} | 
[**get_rest_observable**](IntelligenceApi.md#get_rest_observable) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/observable/{objectId} | 
[**get_rest_settings**](IntelligenceApi.md#get_rest_settings) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/settings/{objectId} | 
[**get_rest_tid_source**](IntelligenceApi.md#get_rest_tid_source) | **GET** /api/fmc_tid/v1/domain/{domainUUID}/tid/source/{objectId} | 
[**update_rest_incident**](IntelligenceApi.md#update_rest_incident) | **PUT** /api/fmc_tid/v1/domain/{domainUUID}/tid/incident/{objectId} | 
[**update_rest_indicator**](IntelligenceApi.md#update_rest_indicator) | **PUT** /api/fmc_tid/v1/domain/{domainUUID}/tid/indicator/{objectId} | 
[**update_rest_observable**](IntelligenceApi.md#update_rest_observable) | **PUT** /api/fmc_tid/v1/domain/{domainUUID}/tid/observable/{objectId} | 
[**update_rest_settings**](IntelligenceApi.md#update_rest_settings) | **PUT** /api/fmc_tid/v1/domain/{domainUUID}/tid/settings/{objectId} | 
[**update_rest_tid_source**](IntelligenceApi.md#update_rest_tid_source) | **PUT** /api/fmc_tid/v1/domain/{domainUUID}/tid/source/{objectId} | 


# **create_rest_discovery_info**
> RESTDiscoveryInfo create_rest_discovery_info(body, domain_uuid)



**API Operations on Discovery Info objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
body = swagger_client.RESTDiscoveryInfo() # RESTDiscoveryInfo | The input Discovery Info object model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_rest_discovery_info(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->create_rest_discovery_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RESTDiscoveryInfo**](RESTDiscoveryInfo.md)| The input Discovery Info object model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTDiscoveryInfo**](RESTDiscoveryInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rest_taxii_collection**
> RESTTaxiiCollection create_rest_taxii_collection(body, domain_uuid)



**API Operations on Taxii Collection objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
body = swagger_client.RESTTaxiiCollection() # RESTTaxiiCollection | The input Taxii Collection object model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_rest_taxii_collection(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->create_rest_taxii_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RESTTaxiiCollection**](RESTTaxiiCollection.md)| The input Taxii Collection object model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTTaxiiCollection**](RESTTaxiiCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rest_tid_source**
> RESTTidSource create_rest_tid_source(body, domain_uuid)



**API Operations on Source objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
body = swagger_client.RESTTidSource() # RESTTidSource | The input Source object model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_rest_tid_source(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->create_rest_tid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RESTTidSource**](RESTTidSource.md)| The input Source object model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTTidSource**](RESTTidSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rest_incident**
> RESTIncident delete_rest_incident(object_id, domain_uuid)



**API Operations on Incident objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Incident.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_rest_incident(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->delete_rest_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Incident. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTIncident**](RESTIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rest_tid_source**
> RESTTidSource delete_rest_tid_source(object_id, domain_uuid)



**API Operations on Source objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Source.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_rest_tid_source(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->delete_rest_tid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Source. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTTidSource**](RESTTidSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rest_element**
> RESTElementListContainer get_all_rest_element(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**API Operations on Element objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_rest_element(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_all_rest_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**RESTElementListContainer**](RESTElementListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rest_incident**
> RESTIncidentListContainer get_all_rest_incident(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**API Operations on Incident objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_rest_incident(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_all_rest_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**RESTIncidentListContainer**](RESTIncidentListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rest_indicator**
> RESTIndicatorListContainer get_all_rest_indicator(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**API Operations on Indicator objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_rest_indicator(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_all_rest_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**RESTIndicatorListContainer**](RESTIndicatorListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rest_observable**
> RESTObservableListContainer get_all_rest_observable(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**API Operations on Observable objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_rest_observable(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_all_rest_observable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**RESTObservableListContainer**](RESTObservableListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rest_tid_source**
> RESTTidSourceListContainer get_all_rest_tid_source(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**API Operations on Source objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_rest_tid_source(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_all_rest_tid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**RESTTidSourceListContainer**](RESTTidSourceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rest_element**
> RESTElement get_rest_element(object_id, domain_uuid)



**API Operations on Element objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Element.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_rest_element(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_rest_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Element. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTElement**](RESTElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rest_incident**
> RESTIncident get_rest_incident(object_id, domain_uuid)



**API Operations on Incident objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Incident.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_rest_incident(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_rest_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Incident. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTIncident**](RESTIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rest_indicator**
> RESTIndicator get_rest_indicator(object_id, domain_uuid)



**API Operations on Indicator objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Indicator.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_rest_indicator(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_rest_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Indicator. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTIndicator**](RESTIndicator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rest_observable**
> RESTObservable get_rest_observable(object_id, domain_uuid)



**API Operations on Observable objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Observable.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_rest_observable(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_rest_observable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Observable. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTObservable**](RESTObservable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rest_settings**
> RESTSettings get_rest_settings(object_id, domain_uuid)



**API Operations on Settings objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Settings object.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_rest_settings(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_rest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Settings object. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTSettings**](RESTSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rest_tid_source**
> RESTTidSource get_rest_tid_source(object_id, domain_uuid)



**API Operations on Source objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Source.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_rest_tid_source(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->get_rest_tid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Source. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTTidSource**](RESTTidSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rest_incident**
> RESTIncident update_rest_incident(object_id, body, domain_uuid)



**API Operations on Incident objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Incident.
body = swagger_client.RESTIncident() # RESTIncident | The input Incident object model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_rest_incident(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->update_rest_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Incident. | 
 **body** | [**RESTIncident**](RESTIncident.md)| The input Incident object model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTIncident**](RESTIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rest_indicator**
> RESTIndicator update_rest_indicator(object_id, body, domain_uuid)



**API Operations on Indicator objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Indicator.
body = swagger_client.RESTIndicator() # RESTIndicator | The input Indicator object model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_rest_indicator(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->update_rest_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Indicator. | 
 **body** | [**RESTIndicator**](RESTIndicator.md)| The input Indicator object model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTIndicator**](RESTIndicator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rest_observable**
> RESTObservable update_rest_observable(object_id, body, domain_uuid)



**API Operations on Observable objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Observable.
body = swagger_client.RESTObservable() # RESTObservable | The input Observable object model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_rest_observable(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->update_rest_observable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Observable. | 
 **body** | [**RESTObservable**](RESTObservable.md)| The input Observable object model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTObservable**](RESTObservable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rest_settings**
> RESTSettings update_rest_settings(object_id, body, domain_uuid)



**API Operations on Settings objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Settings object.
body = swagger_client.RESTSettings() # RESTSettings | The input Settings object model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_rest_settings(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->update_rest_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Settings object. | 
 **body** | [**RESTSettings**](RESTSettings.md)| The input Settings object model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTSettings**](RESTSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rest_tid_source**
> RESTTidSource update_rest_tid_source(object_id, body, domain_uuid)



**API Operations on Source objects. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntelligenceApi()
object_id = 'object_id_example' # str | Unique identifier of the Source.
body = swagger_client.RESTTidSource() # RESTTidSource | The input Source object model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_rest_tid_source(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntelligenceApi->update_rest_tid_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Source. | 
 **body** | [**RESTTidSource**](RESTTidSource.md)| The input Source object model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**RESTTidSource**](RESTTidSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

