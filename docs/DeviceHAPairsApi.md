# swagger_client.DeviceHAPairsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ftdha_device_container**](DeviceHAPairsApi.md#create_ftdha_device_container) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs | 
[**create_ftdha_interface_mac_addresses**](DeviceHAPairsApi.md#create_ftdha_interface_mac_addresses) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/failoverinterfacemacaddressconfigs | 
[**delete_ftdha_device_container**](DeviceHAPairsApi.md#delete_ftdha_device_container) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{objectId} | 
[**delete_ftdha_interface_mac_addresses**](DeviceHAPairsApi.md#delete_ftdha_interface_mac_addresses) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/failoverinterfacemacaddressconfigs/{objectId} | 
[**get_all_ftdha_device_container**](DeviceHAPairsApi.md#get_all_ftdha_device_container) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs | 
[**get_all_ftdha_interface_mac_addresses**](DeviceHAPairsApi.md#get_all_ftdha_interface_mac_addresses) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/failoverinterfacemacaddressconfigs | 
[**get_all_ftdha_monitored_interfaces**](DeviceHAPairsApi.md#get_all_ftdha_monitored_interfaces) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/monitoredinterfaces | 
[**get_ftdha_device_container**](DeviceHAPairsApi.md#get_ftdha_device_container) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{objectId} | 
[**get_ftdha_interface_mac_addresses**](DeviceHAPairsApi.md#get_ftdha_interface_mac_addresses) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/failoverinterfacemacaddressconfigs/{objectId} | 
[**get_ftdha_monitored_interfaces**](DeviceHAPairsApi.md#get_ftdha_monitored_interfaces) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/monitoredinterfaces/{objectId} | 
[**update_ftdha_device_container**](DeviceHAPairsApi.md#update_ftdha_device_container) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{objectId} | 
[**update_ftdha_interface_mac_addresses**](DeviceHAPairsApi.md#update_ftdha_interface_mac_addresses) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/failoverinterfacemacaddressconfigs/{objectId} | 
[**update_ftdha_monitored_interfaces**](DeviceHAPairsApi.md#update_ftdha_monitored_interfaces) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/monitoredinterfaces/{objectId} | 


# **create_ftdha_device_container**
> FTDHADeviceContainer create_ftdha_device_container(body, domain_uuid)



**Retrieves or modifies the FTD HA record associated with the specified ID. Creates or breaks or deletes a FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA pairs. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
body = swagger_client.FTDHADeviceContainer() # FTDHADeviceContainer | Input representation of FTD HA pair.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_ftdha_device_container(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->create_ftdha_device_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDHADeviceContainer**](FTDHADeviceContainer.md)| Input representation of FTD HA pair. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHADeviceContainer**](FTDHADeviceContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ftdha_interface_mac_addresses**
> FTDHAInterfaceMACAddresses create_ftdha_interface_mac_addresses(body, container_uuid, domain_uuid)



**Retrieves or modifies the FTD HA failover policy interface MAC addresses record associated with the specified FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA failover policy interface MAC addresses records. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
body = swagger_client.FTDHAInterfaceMACAddresses() # FTDHAInterfaceMACAddresses | Input representation of FTD HA failover policy interface MAC addresses.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_ftdha_interface_mac_addresses(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->create_ftdha_interface_mac_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDHAInterfaceMACAddresses**](FTDHAInterfaceMACAddresses.md)| Input representation of FTD HA failover policy interface MAC addresses. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHAInterfaceMACAddresses**](FTDHAInterfaceMACAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftdha_device_container**
> FTDHADeviceContainer delete_ftdha_device_container(object_id, domain_uuid)



**Retrieves or modifies the FTD HA record associated with the specified ID. Creates or breaks or deletes a FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA pairs. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
object_id = 'object_id_example' # str | Identifier of a FTD HA pair.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftdha_device_container(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->delete_ftdha_device_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD HA pair. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHADeviceContainer**](FTDHADeviceContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftdha_interface_mac_addresses**
> FTDHAInterfaceMACAddresses delete_ftdha_interface_mac_addresses(object_id, container_uuid, domain_uuid)



**Retrieves or modifies the FTD HA failover policy interface MAC addresses record associated with the specified FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA failover policy interface MAC addresses records. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
object_id = 'object_id_example' # str | Identifier of a FTD HA failover policy interface MAC addresses.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftdha_interface_mac_addresses(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->delete_ftdha_interface_mac_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD HA failover policy interface MAC addresses. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHAInterfaceMACAddresses**](FTDHAInterfaceMACAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftdha_device_container**
> FTDHADeviceContainerListContainer get_all_ftdha_device_container(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the FTD HA record associated with the specified ID. Creates or breaks or deletes a FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA pairs.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftdha_device_container(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->get_all_ftdha_device_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**FTDHADeviceContainerListContainer**](FTDHADeviceContainerListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftdha_interface_mac_addresses**
> FTDHAInterfaceMACAddressesListContainer get_all_ftdha_interface_mac_addresses(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the FTD HA failover policy interface MAC addresses record associated with the specified FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA failover policy interface MAC addresses records.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftdha_interface_mac_addresses(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->get_all_ftdha_interface_mac_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**FTDHAInterfaceMACAddressesListContainer**](FTDHAInterfaceMACAddressesListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftdha_monitored_interfaces**
> FTDHAMonitoredInterfacesListContainer get_all_ftdha_monitored_interfaces(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the FTD HA Monitored interface policy record associated with the specified FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA monitored interface policy records.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftdha_monitored_interfaces(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->get_all_ftdha_monitored_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**FTDHAMonitoredInterfacesListContainer**](FTDHAMonitoredInterfacesListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftdha_device_container**
> FTDHADeviceContainer get_ftdha_device_container(object_id, domain_uuid)



**Retrieves or modifies the FTD HA record associated with the specified ID. Creates or breaks or deletes a FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA pairs.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
object_id = 'object_id_example' # str | Identifier of a FTD HA pair.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftdha_device_container(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->get_ftdha_device_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD HA pair. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHADeviceContainer**](FTDHADeviceContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftdha_interface_mac_addresses**
> FTDHAInterfaceMACAddresses get_ftdha_interface_mac_addresses(object_id, container_uuid, domain_uuid)



**Retrieves or modifies the FTD HA failover policy interface MAC addresses record associated with the specified FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA failover policy interface MAC addresses records.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
object_id = 'object_id_example' # str | Identifier of a FTD HA failover policy interface MAC addresses.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftdha_interface_mac_addresses(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->get_ftdha_interface_mac_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD HA failover policy interface MAC addresses. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHAInterfaceMACAddresses**](FTDHAInterfaceMACAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftdha_monitored_interfaces**
> FTDHAMonitoredInterfaces get_ftdha_monitored_interfaces(object_id, container_uuid, domain_uuid)



**Retrieves or modifies the FTD HA Monitored interface policy record associated with the specified FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA monitored interface policy records.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
object_id = 'object_id_example' # str | Identifier of a FTD HA Monitored interface policy.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftdha_monitored_interfaces(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->get_ftdha_monitored_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD HA Monitored interface policy. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHAMonitoredInterfaces**](FTDHAMonitoredInterfaces.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftdha_device_container**
> FTDHADeviceContainer update_ftdha_device_container(object_id, body, domain_uuid)



**Retrieves or modifies the FTD HA record associated with the specified ID. Creates or breaks or deletes a FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA pairs. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
object_id = 'object_id_example' # str | Identifier of a FTD HA pair.
body = swagger_client.FTDHADeviceContainer() # FTDHADeviceContainer | Input representation of FTD HA pair.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftdha_device_container(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->update_ftdha_device_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD HA pair. | 
 **body** | [**FTDHADeviceContainer**](FTDHADeviceContainer.md)| Input representation of FTD HA pair. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHADeviceContainer**](FTDHADeviceContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftdha_interface_mac_addresses**
> FTDHAInterfaceMACAddresses update_ftdha_interface_mac_addresses(object_id, body, container_uuid, domain_uuid)



**Retrieves or modifies the FTD HA failover policy interface MAC addresses record associated with the specified FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA failover policy interface MAC addresses records. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
object_id = 'object_id_example' # str | Identifier of a FTD HA failover policy interface MAC addresses.
body = swagger_client.FTDHAInterfaceMACAddresses() # FTDHAInterfaceMACAddresses | Input representation of FTD HA failover policy interface MAC addresses.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftdha_interface_mac_addresses(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->update_ftdha_interface_mac_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD HA failover policy interface MAC addresses. | 
 **body** | [**FTDHAInterfaceMACAddresses**](FTDHAInterfaceMACAddresses.md)| Input representation of FTD HA failover policy interface MAC addresses. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHAInterfaceMACAddresses**](FTDHAInterfaceMACAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftdha_monitored_interfaces**
> FTDHAMonitoredInterfaces update_ftdha_monitored_interfaces(object_id, body, container_uuid, domain_uuid)



**Retrieves or modifies the FTD HA Monitored interface policy record associated with the specified FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA monitored interface policy records. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceHAPairsApi()
object_id = 'object_id_example' # str | Identifier of a FTD HA Monitored interface policy.
body = swagger_client.FTDHAMonitoredInterfaces() # FTDHAMonitoredInterfaces | Input representation of FTD HA Monitored interface policy.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftdha_monitored_interfaces(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceHAPairsApi->update_ftdha_monitored_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier of a FTD HA Monitored interface policy. | 
 **body** | [**FTDHAMonitoredInterfaces**](FTDHAMonitoredInterfaces.md)| Input representation of FTD HA Monitored interface policy. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDHAMonitoredInterfaces**](FTDHAMonitoredInterfaces.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

