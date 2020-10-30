# swagger_client.PolicyAssignmentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_assignment**](PolicyAssignmentsApi.md#create_policy_assignment) | **POST** /api/fmc_config/v1/domain/{domainUUID}/assignment/policyassignments | 
[**get_all_policy_assignment**](PolicyAssignmentsApi.md#get_all_policy_assignment) | **GET** /api/fmc_config/v1/domain/{domainUUID}/assignment/policyassignments | 
[**get_policy_assignment**](PolicyAssignmentsApi.md#get_policy_assignment) | **GET** /api/fmc_config/v1/domain/{domainUUID}/assignment/policyassignments/{objectId} | 
[**update_policy_assignment**](PolicyAssignmentsApi.md#update_policy_assignment) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/assignment/policyassignments/{objectId} | 


# **create_policy_assignment**
> PolicyAssignment create_policy_assignment(body, domain_uuid)



**Retrieves, creates, or modifies the policy assignments to target devices associated with the specified ID. If no ID is specified, retrieves list of all policy assignments to target devices. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyAssignmentsApi()
body = swagger_client.PolicyAssignment() # PolicyAssignment | The input policy assignment model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_policy_assignment(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyAssignmentsApi->create_policy_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PolicyAssignment**](PolicyAssignment.md)| The input policy assignment model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_policy_assignment**
> PolicyAssignmentListContainer get_all_policy_assignment(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, creates, or modifies the policy assignments to target devices associated with the specified ID. If no ID is specified, retrieves list of all policy assignments to target devices.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyAssignmentsApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_policy_assignment(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyAssignmentsApi->get_all_policy_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**PolicyAssignmentListContainer**](PolicyAssignmentListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_assignment**
> PolicyAssignment get_policy_assignment(object_id, domain_uuid)



**Retrieves, creates, or modifies the policy assignments to target devices associated with the specified ID. If no ID is specified, retrieves list of all policy assignments to target devices.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyAssignmentsApi()
object_id = 'object_id_example' # str | Unique identifier of a policy assignment.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_policy_assignment(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyAssignmentsApi->get_policy_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a policy assignment. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_assignment**
> PolicyAssignment update_policy_assignment(object_id, body, domain_uuid)



**Retrieves, creates, or modifies the policy assignments to target devices associated with the specified ID. If no ID is specified, retrieves list of all policy assignments to target devices. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyAssignmentsApi()
object_id = 'object_id_example' # str | Unique identifier of a policy assignment.
body = swagger_client.PolicyAssignment() # PolicyAssignment | The input policy assignment model.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_policy_assignment(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyAssignmentsApi->update_policy_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a policy assignment. | 
 **body** | [**PolicyAssignment**](PolicyAssignment.md)| The input policy assignment model. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PolicyAssignment**](PolicyAssignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

