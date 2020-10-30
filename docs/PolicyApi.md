# swagger_client.PolicyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_policy**](PolicyApi.md#create_access_policy) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies | 
[**create_access_policy_category**](PolicyApi.md#create_access_policy_category) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/categories | 
[**create_ftd_nat_policy**](PolicyApi.md#create_ftd_nat_policy) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies | 
[**create_ftds2_s_vpn_model**](PolicyApi.md#create_ftds2_s_vpn_model) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns | 
[**create_multiple_access_rule**](PolicyApi.md#create_multiple_access_rule) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/accessrules | 
[**create_multiple_ftd_auto_nat_rule**](PolicyApi.md#create_multiple_ftd_auto_nat_rule) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/autonatrules | 
[**create_multiple_ftd_manual_nat_rule**](PolicyApi.md#create_multiple_ftd_manual_nat_rule) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/manualnatrules | 
[**create_multiple_prefilter_rule**](PolicyApi.md#create_multiple_prefilter_rule) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/prefilterrules | 
[**create_prefilter_policy**](PolicyApi.md#create_prefilter_policy) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies | 
[**create_vpn_endpoint**](PolicyApi.md#create_vpn_endpoint) | **POST** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/endpoints | 
[**delete_access_policy**](PolicyApi.md#delete_access_policy) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{objectId} | 
[**delete_access_policy_category**](PolicyApi.md#delete_access_policy_category) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/categories/{objectId} | 
[**delete_access_rule**](PolicyApi.md#delete_access_rule) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/accessrules/{objectId} | 
[**delete_ftd_auto_nat_rule**](PolicyApi.md#delete_ftd_auto_nat_rule) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/autonatrules/{objectId} | 
[**delete_ftd_manual_nat_rule**](PolicyApi.md#delete_ftd_manual_nat_rule) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/manualnatrules/{objectId} | 
[**delete_ftd_nat_policy**](PolicyApi.md#delete_ftd_nat_policy) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{objectId} | 
[**delete_ftds2_s_vpn_model**](PolicyApi.md#delete_ftds2_s_vpn_model) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{objectId} | 
[**delete_hit_count**](PolicyApi.md#delete_hit_count) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/operational/hitcounts | 
[**delete_multiple_access_rule**](PolicyApi.md#delete_multiple_access_rule) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/accessrules | 
[**delete_multiple_prefilter_rule**](PolicyApi.md#delete_multiple_prefilter_rule) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/prefilterrules | 
[**delete_prefilter_hit_count**](PolicyApi.md#delete_prefilter_hit_count) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/operational/hitcounts | 
[**delete_prefilter_policy**](PolicyApi.md#delete_prefilter_policy) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{objectId} | 
[**delete_prefilter_rule**](PolicyApi.md#delete_prefilter_rule) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/prefilterrules/{objectId} | 
[**delete_vpn_endpoint**](PolicyApi.md#delete_vpn_endpoint) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/endpoints/{objectId} | 
[**get_access_policy**](PolicyApi.md#get_access_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{objectId} | 
[**get_access_policy_category**](PolicyApi.md#get_access_policy_category) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/categories/{objectId} | 
[**get_access_policy_inheritance_setting**](PolicyApi.md#get_access_policy_inheritance_setting) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/inheritancesettings/{objectId} | 
[**get_access_policy_logging_setting_model**](PolicyApi.md#get_access_policy_logging_setting_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/loggingsettings/{objectId} | 
[**get_access_rule**](PolicyApi.md#get_access_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/accessrules/{objectId} | 
[**get_all_access_policy**](PolicyApi.md#get_all_access_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies | 
[**get_all_access_policy_category**](PolicyApi.md#get_all_access_policy_category) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/categories | 
[**get_all_access_policy_inheritance_setting**](PolicyApi.md#get_all_access_policy_inheritance_setting) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/inheritancesettings | 
[**get_all_access_policy_logging_setting_model**](PolicyApi.md#get_all_access_policy_logging_setting_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/loggingsettings | 
[**get_all_access_rule**](PolicyApi.md#get_all_access_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/accessrules | 
[**get_all_default_action**](PolicyApi.md#get_all_default_action) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/defaultactions | 
[**get_all_file_policy**](PolicyApi.md#get_all_file_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/filepolicies | 
[**get_all_ftd_auto_nat_rule**](PolicyApi.md#get_all_ftd_auto_nat_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/autonatrules | 
[**get_all_ftd_manual_nat_rule**](PolicyApi.md#get_all_ftd_manual_nat_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/manualnatrules | 
[**get_all_ftd_nat_policy**](PolicyApi.md#get_all_ftd_nat_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies | 
[**get_all_ftd_nat_rule**](PolicyApi.md#get_all_ftd_nat_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/natrules | 
[**get_all_ftds2_s_vpn_model**](PolicyApi.md#get_all_ftds2_s_vpn_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns | 
[**get_all_intrusion_policy**](PolicyApi.md#get_all_intrusion_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/intrusionpolicies | 
[**get_all_prefilter_default_action**](PolicyApi.md#get_all_prefilter_default_action) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/defaultactions | 
[**get_all_prefilter_policy**](PolicyApi.md#get_all_prefilter_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies | 
[**get_all_prefilter_rule**](PolicyApi.md#get_all_prefilter_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/prefilterrules | 
[**get_all_snmp_config**](PolicyApi.md#get_all_snmp_config) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/snmpalerts | 
[**get_all_syslog_config**](PolicyApi.md#get_all_syslog_config) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/syslogalerts | 
[**get_all_vpn_advanced_settings**](PolicyApi.md#get_all_vpn_advanced_settings) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/advancedsettings | 
[**get_all_vpn_endpoint**](PolicyApi.md#get_all_vpn_endpoint) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/endpoints | 
[**get_all_vpn_ike_settings**](PolicyApi.md#get_all_vpn_ike_settings) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/ikesettings | 
[**get_all_vpn_ip_sec_settings**](PolicyApi.md#get_all_vpn_ip_sec_settings) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/ipsecsettings | 
[**get_default_action**](PolicyApi.md#get_default_action) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/defaultactions/{objectId} | 
[**get_file_policy**](PolicyApi.md#get_file_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/filepolicies/{objectId} | 
[**get_ftd_auto_nat_rule**](PolicyApi.md#get_ftd_auto_nat_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/autonatrules/{objectId} | 
[**get_ftd_manual_nat_rule**](PolicyApi.md#get_ftd_manual_nat_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/manualnatrules/{objectId} | 
[**get_ftd_nat_policy**](PolicyApi.md#get_ftd_nat_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{objectId} | 
[**get_ftd_nat_rule**](PolicyApi.md#get_ftd_nat_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/natrules/{objectId} | 
[**get_ftds2_s_vpn_model**](PolicyApi.md#get_ftds2_s_vpn_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{objectId} | 
[**get_hit_count**](PolicyApi.md#get_hit_count) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/operational/hitcounts | 
[**get_intrusion_policy**](PolicyApi.md#get_intrusion_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/intrusionpolicies/{objectId} | 
[**get_prefilter_default_action**](PolicyApi.md#get_prefilter_default_action) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/defaultactions/{objectId} | 
[**get_prefilter_hit_count**](PolicyApi.md#get_prefilter_hit_count) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/operational/hitcounts | 
[**get_prefilter_policy**](PolicyApi.md#get_prefilter_policy) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{objectId} | 
[**get_prefilter_rule**](PolicyApi.md#get_prefilter_rule) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/prefilterrules/{objectId} | 
[**get_snmp_config**](PolicyApi.md#get_snmp_config) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/snmpalerts/{objectId} | 
[**get_syslog_config**](PolicyApi.md#get_syslog_config) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/syslogalerts/{objectId} | 
[**get_vpn_advanced_settings**](PolicyApi.md#get_vpn_advanced_settings) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/advancedsettings/{objectId} | 
[**get_vpn_endpoint**](PolicyApi.md#get_vpn_endpoint) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/endpoints/{objectId} | 
[**get_vpn_ike_settings**](PolicyApi.md#get_vpn_ike_settings) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/ikesettings/{objectId} | 
[**get_vpn_ip_sec_settings**](PolicyApi.md#get_vpn_ip_sec_settings) | **GET** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/ipsecsettings/{objectId} | 
[**update_access_policy**](PolicyApi.md#update_access_policy) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{objectId} | 
[**update_access_policy_category**](PolicyApi.md#update_access_policy_category) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/categories/{objectId} | 
[**update_access_policy_inheritance_setting**](PolicyApi.md#update_access_policy_inheritance_setting) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/inheritancesettings/{objectId} | 
[**update_access_policy_logging_setting_model**](PolicyApi.md#update_access_policy_logging_setting_model) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/loggingsettings/{objectId} | 
[**update_access_rule**](PolicyApi.md#update_access_rule) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/accessrules/{objectId} | 
[**update_default_action**](PolicyApi.md#update_default_action) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/defaultactions/{objectId} | 
[**update_ftd_auto_nat_rule**](PolicyApi.md#update_ftd_auto_nat_rule) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/autonatrules/{objectId} | 
[**update_ftd_manual_nat_rule**](PolicyApi.md#update_ftd_manual_nat_rule) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/manualnatrules/{objectId} | 
[**update_ftd_nat_policy**](PolicyApi.md#update_ftd_nat_policy) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{objectId} | 
[**update_ftds2_s_vpn_model**](PolicyApi.md#update_ftds2_s_vpn_model) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{objectId} | 
[**update_hit_count**](PolicyApi.md#update_hit_count) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/operational/hitcounts | 
[**update_multiple_access_rule**](PolicyApi.md#update_multiple_access_rule) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/accessrules | 
[**update_multiple_prefilter_rule**](PolicyApi.md#update_multiple_prefilter_rule) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/prefilterrules | 
[**update_prefilter_default_action**](PolicyApi.md#update_prefilter_default_action) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/defaultactions/{objectId} | 
[**update_prefilter_hit_count**](PolicyApi.md#update_prefilter_hit_count) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/operational/hitcounts | 
[**update_prefilter_policy**](PolicyApi.md#update_prefilter_policy) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{objectId} | 
[**update_prefilter_rule**](PolicyApi.md#update_prefilter_rule) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/prefilterrules/{objectId} | 
[**update_vpn_advanced_settings**](PolicyApi.md#update_vpn_advanced_settings) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/advancedsettings/{objectId} | 
[**update_vpn_endpoint**](PolicyApi.md#update_vpn_endpoint) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/endpoints/{objectId} | 
[**update_vpn_ike_settings**](PolicyApi.md#update_vpn_ike_settings) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/ikesettings/{objectId} | 
[**update_vpn_ip_sec_settings**](PolicyApi.md#update_vpn_ip_sec_settings) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/policy/ftds2svpns/{containerUUID}/ipsecsettings/{objectId} | 


# **create_access_policy**
> AccessPolicy create_access_policy(body, domain_uuid)



**Retrieves, deletes, creates, or modifies the access control policy associated with the specified ID. Also, retrieves list of all access control policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.AccessPolicy() # AccessPolicy | Input representation of access control policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_access_policy(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessPolicy**](AccessPolicy.md)| Input representation of access control policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicy**](AccessPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_policy_category**
> AccessPolicyCategory create_access_policy_category(body, container_uuid, domain_uuid, section=section, above_category=above_category, insert_before=insert_before, insert_after=insert_after)



**Retrieves, deletes, creates, or modifies the category associated with the specified policy ID. If no ID is specified, retrieves list of all categories associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.AccessPolicyCategory() # AccessPolicyCategory | The input category model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
section = 'section_example' # str | Retrieves, creates or modifies category in given section. Allowed value is 'mandatory' and 'default'. (optional)
above_category = 'above_category_example' # str | creates category above specified category. (optional)
insert_before = 'insert_before_example' # str | creates category above given rule index. (optional)
insert_after = 'insert_after_example' # str | creates category below given rule index.  (optional)

try:
    api_response = api_instance.create_access_policy_category(body, container_uuid, domain_uuid, section=section, above_category=above_category, insert_before=insert_before, insert_after=insert_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_access_policy_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessPolicyCategory**](AccessPolicyCategory.md)| The input category model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **section** | **str**| Retrieves, creates or modifies category in given section. Allowed value is &#39;mandatory&#39; and &#39;default&#39;. | [optional] 
 **above_category** | **str**| creates category above specified category. | [optional] 
 **insert_before** | **str**| creates category above given rule index. | [optional] 
 **insert_after** | **str**| creates category below given rule index.  | [optional] 

### Return type

[**AccessPolicyCategory**](AccessPolicyCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ftd_nat_policy**
> FTDNatPolicy create_ftd_nat_policy(body, domain_uuid)



**Retrieves, deletes, creates, or modifies the NAT policy associated with the specified ID. Also, retrieves list of all NAT policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.FTDNatPolicy() # FTDNatPolicy | Input representation of NAT policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_ftd_nat_policy(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_ftd_nat_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDNatPolicy**](FTDNatPolicy.md)| Input representation of NAT policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDNatPolicy**](FTDNatPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ftds2_s_vpn_model**
> FTDS2SVpnModel create_ftds2_s_vpn_model(body, domain_uuid)



**Retrieves, deletes, creates, or modifies the FTD Site to Site VPN topology associated with the specified ID. If no ID is specified for a GET, retrieves list of all FTD Site to Site VPN topologies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.FTDS2SVpnModel() # FTDS2SVpnModel | Input representation of FTD Site to Site VPN topology.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_ftds2_s_vpn_model(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_ftds2_s_vpn_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDS2SVpnModel**](FTDS2SVpnModel.md)| Input representation of FTD Site to Site VPN topology. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDS2SVpnModel**](FTDS2SVpnModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_access_rule**
> AccessRule create_multiple_access_rule(body, container_uuid, domain_uuid, bulk=bulk, insert_after=insert_after, insert_before=insert_before, section=section, category=category)



**Retrieves, deletes, creates, or modifies the access control rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all access rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.AccessRule() # AccessRule | The input access control rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
bulk = true # bool | This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations. (optional)
insert_after = 'insert_after_example' # str | This parameter specifies that the rules will be inserted after the specified rule index. If no section or category is specified, the rules will be added to the section or category after the insertion point. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply. (optional)
insert_before = 'insert_before_example' # str | This parameter specifies that the rules will be inserted before the specified rule index. If no section or category is specified, the rules will be added to the section or category before the insertion point. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply. (optional)
section = 'section_example' # str | This parameter specifies the section into which the rules will be added. If this parameter is not used the section will be the default section. Only 'mandatory' and 'default' are allowed values. If a section is specified, a category cannot be specified. (optional)
category = 'category_example' # str | This parameter specifies the category into which the rules will be added. If a category is specified it must exist or the request will fail. If a section is specified, a category cannot be specified. (optional)

try:
    api_response = api_instance.create_multiple_access_rule(body, container_uuid, domain_uuid, bulk=bulk, insert_after=insert_after, insert_before=insert_before, section=section, category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_multiple_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessRule**](AccessRule.md)| The input access control rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **bulk** | **bool**| This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations. | [optional] 
 **insert_after** | **str**| This parameter specifies that the rules will be inserted after the specified rule index. If no section or category is specified, the rules will be added to the section or category after the insertion point. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply. | [optional] 
 **insert_before** | **str**| This parameter specifies that the rules will be inserted before the specified rule index. If no section or category is specified, the rules will be added to the section or category before the insertion point. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply. | [optional] 
 **section** | **str**| This parameter specifies the section into which the rules will be added. If this parameter is not used the section will be the default section. Only &#39;mandatory&#39; and &#39;default&#39; are allowed values. If a section is specified, a category cannot be specified. | [optional] 
 **category** | **str**| This parameter specifies the category into which the rules will be added. If a category is specified it must exist or the request will fail. If a section is specified, a category cannot be specified. | [optional] 

### Return type

[**AccessRule**](AccessRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_ftd_auto_nat_rule**
> FTDAutoNatRule create_multiple_ftd_auto_nat_rule(body, container_uuid, domain_uuid, bulk=bulk, section=section)



**Retrieves, deletes, creates, or modifies the Auto NAT rule associated with the specified ID. Also, retrieves list of all Auto NAT rules.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.FTDAutoNatRule() # FTDAutoNatRule | The input Auto NAT rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
bulk = true # bool | Enables bulk create for auto nat rules. (optional)
section = 'section_example' # str | Retrieves, creates or modifies auto nat rule in given section. Allowed value is 'auto'. (optional)

try:
    api_response = api_instance.create_multiple_ftd_auto_nat_rule(body, container_uuid, domain_uuid, bulk=bulk, section=section)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_multiple_ftd_auto_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDAutoNatRule**](FTDAutoNatRule.md)| The input Auto NAT rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **bulk** | **bool**| Enables bulk create for auto nat rules. | [optional] 
 **section** | **str**| Retrieves, creates or modifies auto nat rule in given section. Allowed value is &#39;auto&#39;. | [optional] 

### Return type

[**FTDAutoNatRule**](FTDAutoNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_ftd_manual_nat_rule**
> FTDManualNatRule create_multiple_ftd_manual_nat_rule(body, container_uuid, domain_uuid, bulk=bulk, section=section, target_index=target_index)



**Retrieves, deletes, creates, or modifies the Manual NAT rule associated with the specified ID. Also, retrieves list of all Manual NAT rules.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.FTDManualNatRule() # FTDManualNatRule | The input Manual NAT rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
bulk = true # bool | Enables bulk create for manual nat rules. (optional)
section = 'section_example' # str | Retrieves, creates or modifies manual nat rule in given section. Allowed value is 'before_auto' and 'after_auto'. (optional)
target_index = 'target_index_example' # str | Creates or modifies manual nat rule at given targetIndex. It takes an integer value.  (optional)

try:
    api_response = api_instance.create_multiple_ftd_manual_nat_rule(body, container_uuid, domain_uuid, bulk=bulk, section=section, target_index=target_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_multiple_ftd_manual_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDManualNatRule**](FTDManualNatRule.md)| The input Manual NAT rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **bulk** | **bool**| Enables bulk create for manual nat rules. | [optional] 
 **section** | **str**| Retrieves, creates or modifies manual nat rule in given section. Allowed value is &#39;before_auto&#39; and &#39;after_auto&#39;. | [optional] 
 **target_index** | **str**| Creates or modifies manual nat rule at given targetIndex. It takes an integer value.  | [optional] 

### Return type

[**FTDManualNatRule**](FTDManualNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_prefilter_rule**
> PrefilterRule create_multiple_prefilter_rule(body, container_uuid, domain_uuid, bulk=bulk)



**Retrieves, deletes, creates, or modifies the prefilter rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all prefilter rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.PrefilterRule() # PrefilterRule | The input prefilter rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
bulk = true # bool | This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations. (optional)

try:
    api_response = api_instance.create_multiple_prefilter_rule(body, container_uuid, domain_uuid, bulk=bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_multiple_prefilter_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrefilterRule**](PrefilterRule.md)| The input prefilter rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **bulk** | **bool**| This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations. | [optional] 

### Return type

[**PrefilterRule**](PrefilterRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_prefilter_policy**
> PrefilterPolicy create_prefilter_policy(body, domain_uuid)



**Retrieves prefilter policy associated with the specified ID. Also, retrieves list of all prefilter policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.PrefilterPolicy() # PrefilterPolicy | Input representation of prefilter policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_prefilter_policy(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_prefilter_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrefilterPolicy**](PrefilterPolicy.md)| Input representation of prefilter policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterPolicy**](PrefilterPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpn_endpoint**
> VpnEndpoint create_vpn_endpoint(body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies a specific Endpoint associated with the specified ID inside a VPN Site To Site Topology. If no ID is specifid for a GET, retrieves list of all Endpoints of a topology. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
body = swagger_client.VpnEndpoint() # VpnEndpoint | Input representation of Endpoint.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_vpn_endpoint(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_vpn_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VpnEndpoint**](VpnEndpoint.md)| Input representation of Endpoint. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnEndpoint**](VpnEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_policy**
> AccessPolicy delete_access_policy(object_id, domain_uuid, ignore_warning=ignore_warning)



**Retrieves, deletes, creates, or modifies the access control policy associated with the specified ID. Also, retrieves list of all access control policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for access control policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
ignore_warning = 'ignore_warning_example' # str | Shows any warnings when deleting an access policy, if set to false. If not specified, value is set to true and warnings are ignored. Allowed values are 'true' and 'false'. (optional)

try:
    api_response = api_instance.delete_access_policy(object_id, domain_uuid, ignore_warning=ignore_warning)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for access control policy. | 
 **domain_uuid** | **str**| Domain UUID | 
 **ignore_warning** | **str**| Shows any warnings when deleting an access policy, if set to false. If not specified, value is set to true and warnings are ignored. Allowed values are &#39;true&#39; and &#39;false&#39;. | [optional] 

### Return type

[**AccessPolicy**](AccessPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_policy_category**
> AccessPolicyCategory delete_access_policy_category(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the category associated with the specified policy ID. If no ID is specified, retrieves list of all categories associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a category.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_access_policy_category(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_access_policy_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a category. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicyCategory**](AccessPolicyCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_rule**
> AccessRule delete_access_rule(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the access control rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all access rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of an access control rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_access_rule(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an access control rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessRule**](AccessRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftd_auto_nat_rule**
> FTDAutoNatRule delete_ftd_auto_nat_rule(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the Auto NAT rule associated with the specified ID. Also, retrieves list of all Auto NAT rules.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of an Auto NAT rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftd_auto_nat_rule(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_ftd_auto_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an Auto NAT rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDAutoNatRule**](FTDAutoNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftd_manual_nat_rule**
> FTDManualNatRule delete_ftd_manual_nat_rule(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the Manual NAT rule associated with the specified ID. Also, retrieves list of all Manual NAT rules.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a Manual NAT rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftd_manual_nat_rule(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_ftd_manual_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a Manual NAT rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDManualNatRule**](FTDManualNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftd_nat_policy**
> FTDNatPolicy delete_ftd_nat_policy(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the NAT policy associated with the specified ID. Also, retrieves list of all NAT policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for NAT policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftd_nat_policy(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_ftd_nat_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for NAT policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDNatPolicy**](FTDNatPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftds2_s_vpn_model**
> FTDS2SVpnModel delete_ftds2_s_vpn_model(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the FTD Site to Site VPN topology associated with the specified ID. If no ID is specified for a GET, retrieves list of all FTD Site to Site VPN topologies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for FTD Site to Site VPN topology.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftds2_s_vpn_model(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_ftds2_s_vpn_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for FTD Site to Site VPN topology. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDS2SVpnModel**](FTDS2SVpnModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hit_count**
> HitCount delete_hit_count(filter, container_uuid, domain_uuid)



**Retrieves, refreshes and clears Hit Count _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
filter = 'filter_example' # str | Value is of format (including quotes): <code>\"deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\"</code><br/><code>deviceId</code> is UUID of device and is a mandatory field.<br/><code>ids</code> returns hitcounts of access rules if set to list of rule UUIDs. If this key is not used, all access rules will be returned (Note that this is applicable only in GET and DELETE operations). <br/><code>fetchZeroHitCount</code> returns only access rules whose hit count is zero if <code>true</code> (Note that this is applicable only in GET operation and if <code>ids</code> is not used).
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_hit_count(filter, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_hit_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Value is of format (including quotes): &lt;code&gt;\&quot;deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\&quot;&lt;/code&gt;&lt;br/&gt;&lt;code&gt;deviceId&lt;/code&gt; is UUID of device and is a mandatory field.&lt;br/&gt;&lt;code&gt;ids&lt;/code&gt; returns hitcounts of access rules if set to list of rule UUIDs. If this key is not used, all access rules will be returned (Note that this is applicable only in GET and DELETE operations). &lt;br/&gt;&lt;code&gt;fetchZeroHitCount&lt;/code&gt; returns only access rules whose hit count is zero if &lt;code&gt;true&lt;/code&gt; (Note that this is applicable only in GET operation and if &lt;code&gt;ids&lt;/code&gt; is not used). | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**HitCount**](HitCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_multiple_access_rule**
> AccessRule delete_multiple_access_rule(bulk, filter, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the access control rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all access rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
bulk = true # bool | This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations.
filter = 'filter_example' # str | To be used in conjunction with <code>bulk=true</code> for bulk deletion. Value is of format (including quotes): <code>\"ids:id1,id2,...\"</code>.<br/><code>ids</code> is a comma-separated list of rule IDs to be deleted.
body = swagger_client.AccessRule() # AccessRule | The input access control rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_multiple_access_rule(bulk, filter, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_multiple_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk** | **bool**| This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations. | 
 **filter** | **str**| To be used in conjunction with &lt;code&gt;bulk&#x3D;true&lt;/code&gt; for bulk deletion. Value is of format (including quotes): &lt;code&gt;\&quot;ids:id1,id2,...\&quot;&lt;/code&gt;.&lt;br/&gt;&lt;code&gt;ids&lt;/code&gt; is a comma-separated list of rule IDs to be deleted. | 
 **body** | [**AccessRule**](AccessRule.md)| The input access control rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessRule**](AccessRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_multiple_prefilter_rule**
> PrefilterRule delete_multiple_prefilter_rule(bulk, filter, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the prefilter rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all prefilter rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
bulk = true # bool | This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations.
filter = 'filter_example' # str | To be used in conjunction with <code>bulk=true</code> for bulk deletion. Value is of format (including quotes): <code>\"ids:id1,id2,...\"</code>.<br/><code>ids</code> is a comma-separated list of rule IDs to be deleted.
body = swagger_client.PrefilterRule() # PrefilterRule | The input prefilter rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_multiple_prefilter_rule(bulk, filter, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_multiple_prefilter_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk** | **bool**| This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations. | 
 **filter** | **str**| To be used in conjunction with &lt;code&gt;bulk&#x3D;true&lt;/code&gt; for bulk deletion. Value is of format (including quotes): &lt;code&gt;\&quot;ids:id1,id2,...\&quot;&lt;/code&gt;.&lt;br/&gt;&lt;code&gt;ids&lt;/code&gt; is a comma-separated list of rule IDs to be deleted. | 
 **body** | [**PrefilterRule**](PrefilterRule.md)| The input prefilter rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterRule**](PrefilterRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_prefilter_hit_count**
> PrefilterHitCount delete_prefilter_hit_count(filter, container_uuid, domain_uuid)



**Retrieves, refreshes and clears Hit Count _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
filter = 'filter_example' # str | Value is of format (including quotes): <code>\"deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\"</code><br/><code>deviceId</code> is UUID of device and is a mandatory field.<br/><code>ids</code> returns hitcounts of prefilter rules if set to list of rule UUIDs. If this key is not used, all prefilter rules will be returned (Note that this is applicable only in GET and DELETE operations). <br/><code>fetchZeroHitCount</code> returns only access rules whose hit count is zero if <code>true</code> (Note that this is applicable only in GET operation and if <code>ids</code> is not used).
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_prefilter_hit_count(filter, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_prefilter_hit_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Value is of format (including quotes): &lt;code&gt;\&quot;deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\&quot;&lt;/code&gt;&lt;br/&gt;&lt;code&gt;deviceId&lt;/code&gt; is UUID of device and is a mandatory field.&lt;br/&gt;&lt;code&gt;ids&lt;/code&gt; returns hitcounts of prefilter rules if set to list of rule UUIDs. If this key is not used, all prefilter rules will be returned (Note that this is applicable only in GET and DELETE operations). &lt;br/&gt;&lt;code&gt;fetchZeroHitCount&lt;/code&gt; returns only access rules whose hit count is zero if &lt;code&gt;true&lt;/code&gt; (Note that this is applicable only in GET operation and if &lt;code&gt;ids&lt;/code&gt; is not used). | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterHitCount**](PrefilterHitCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_prefilter_policy**
> PrefilterPolicy delete_prefilter_policy(object_id, domain_uuid)



**Retrieves prefilter policy associated with the specified ID. Also, retrieves list of all prefilter policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for prefilter policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_prefilter_policy(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_prefilter_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for prefilter policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterPolicy**](PrefilterPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_prefilter_rule**
> PrefilterRule delete_prefilter_rule(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the prefilter rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all prefilter rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a prefilter rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_prefilter_rule(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_prefilter_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a prefilter rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterRule**](PrefilterRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vpn_endpoint**
> VpnEndpoint delete_vpn_endpoint(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies a specific Endpoint associated with the specified ID inside a VPN Site To Site Topology. If no ID is specifid for a GET, retrieves list of all Endpoints of a topology. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for an Endpoint in a Site to Site VPN topology.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_vpn_endpoint(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_vpn_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for an Endpoint in a Site to Site VPN topology. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnEndpoint**](VpnEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_policy**
> AccessPolicy get_access_policy(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the access control policy associated with the specified ID. Also, retrieves list of all access control policies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for access control policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_access_policy(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for access control policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicy**](AccessPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_policy_category**
> AccessPolicyCategory get_access_policy_category(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the category associated with the specified policy ID. If no ID is specified, retrieves list of all categories associated with the specified policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a category.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_access_policy_category(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_access_policy_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a category. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicyCategory**](AccessPolicyCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_policy_inheritance_setting**
> AccessPolicyInheritanceSetting get_access_policy_inheritance_setting(object_id, container_uuid, domain_uuid)



**Retrieves and modifies the inheritance settings associated with specified Access Policy.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of the Access Policy Inheritance Setting.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_access_policy_inheritance_setting(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_access_policy_inheritance_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Access Policy Inheritance Setting. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicyInheritanceSetting**](AccessPolicyInheritanceSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_policy_logging_setting_model**
> AccessPolicyLoggingSettingModel get_access_policy_logging_setting_model(object_id, container_uuid, domain_uuid)



**Retrieves or modifies the logging setting associated with the specified access control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified access control policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a logging setting.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_access_policy_logging_setting_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_access_policy_logging_setting_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a logging setting. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicyLoggingSettingModel**](AccessPolicyLoggingSettingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_rule**
> AccessRule get_access_rule(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the access control rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all access rules associated with the specified policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of an access control rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_access_rule(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an access control rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessRule**](AccessRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_access_policy**
> AccessPolicyListContainer get_all_access_policy(domain_uuid, name=name, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the access control policy associated with the specified ID. Also, retrieves list of all access control policies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
name = 'name_example' # str | If parameter is specified, only the policy matching with the specified name will be displayed. Cannot be used if object ID is specified in path. (optional)
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_access_policy(domain_uuid, name=name, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **name** | **str**| If parameter is specified, only the policy matching with the specified name will be displayed. Cannot be used if object ID is specified in path. | [optional] 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**AccessPolicyListContainer**](AccessPolicyListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_access_policy_category**
> AccessPolicyCategoryListContainer get_all_access_policy_category(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the category associated with the specified policy ID. If no ID is specified, retrieves list of all categories associated with the specified policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_access_policy_category(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_access_policy_category: %s\n" % e)
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

[**AccessPolicyCategoryListContainer**](AccessPolicyCategoryListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_access_policy_inheritance_setting**
> AccessPolicyInheritanceSettingListContainer get_all_access_policy_inheritance_setting(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves and modifies the inheritance settings associated with specified Access Policy.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_access_policy_inheritance_setting(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_access_policy_inheritance_setting: %s\n" % e)
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

[**AccessPolicyInheritanceSettingListContainer**](AccessPolicyInheritanceSettingListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_access_policy_logging_setting_model**
> AccessPolicyLoggingSettingModelListContainer get_all_access_policy_logging_setting_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the logging setting associated with the specified access control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified access control policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_access_policy_logging_setting_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_access_policy_logging_setting_model: %s\n" % e)
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

[**AccessPolicyLoggingSettingModelListContainer**](AccessPolicyLoggingSettingModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_access_rule**
> AccessRuleListContainer get_all_access_rule(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the access control rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all access rules associated with the specified policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_access_rule(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_access_rule: %s\n" % e)
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

[**AccessRuleListContainer**](AccessRuleListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_default_action**
> DefaultActionListContainer get_all_default_action(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the default action associated with the specified access control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified access control policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_default_action(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_default_action: %s\n" % e)
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

[**DefaultActionListContainer**](DefaultActionListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_file_policy**
> FilePolicyListContainer get_all_file_policy(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the endpoint device type object associated with the specified ID. If no ID is specified, retrieves list of all endpoint device type objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_file_policy(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_file_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**FilePolicyListContainer**](FilePolicyListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_auto_nat_rule**
> FTDAutoNatRuleListContainer get_all_ftd_auto_nat_rule(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the Auto NAT rule associated with the specified ID. Also, retrieves list of all Auto NAT rules. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_auto_nat_rule(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_ftd_auto_nat_rule: %s\n" % e)
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

[**FTDAutoNatRuleListContainer**](FTDAutoNatRuleListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_manual_nat_rule**
> FTDManualNatRuleListContainer get_all_ftd_manual_nat_rule(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the Manual NAT rule associated with the specified ID. Also, retrieves list of all Manual NAT rules. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_manual_nat_rule(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_ftd_manual_nat_rule: %s\n" % e)
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

[**FTDManualNatRuleListContainer**](FTDManualNatRuleListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_nat_policy**
> FTDNatPolicyListContainer get_all_ftd_nat_policy(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the NAT policy associated with the specified ID. Also, retrieves list of all NAT policies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_nat_policy(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_ftd_nat_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**FTDNatPolicyListContainer**](FTDNatPolicyListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_nat_rule**
> FTDNatRuleListContainer get_all_ftd_nat_rule(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of all NAT rules (manual and auto) associated with the specified policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_nat_rule(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_ftd_nat_rule: %s\n" % e)
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

[**FTDNatRuleListContainer**](FTDNatRuleListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftds2_s_vpn_model**
> FTDS2SVpnModelListContainer get_all_ftds2_s_vpn_model(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the FTD Site to Site VPN topology associated with the specified ID. If no ID is specified for a GET, retrieves list of all FTD Site to Site VPN topologies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftds2_s_vpn_model(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_ftds2_s_vpn_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**FTDS2SVpnModelListContainer**](FTDS2SVpnModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_intrusion_policy**
> IntrusionPolicyListContainer get_all_intrusion_policy(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the intrusion policy associated with the specified ID. If no ID is specified, retrieves list of all intrusion policies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_intrusion_policy(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_intrusion_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**IntrusionPolicyListContainer**](IntrusionPolicyListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_prefilter_default_action**
> PrefilterDefaultActionListContainer get_all_prefilter_default_action(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the default action associated with the specified prefilter control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified prefilter policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_prefilter_default_action(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_prefilter_default_action: %s\n" % e)
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

[**PrefilterDefaultActionListContainer**](PrefilterDefaultActionListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_prefilter_policy**
> PrefilterPolicyListContainer get_all_prefilter_policy(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves prefilter policy associated with the specified ID. Also, retrieves list of all prefilter policies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_prefilter_policy(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_prefilter_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**PrefilterPolicyListContainer**](PrefilterPolicyListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_prefilter_rule**
> PrefilterRuleListContainer get_all_prefilter_rule(container_uuid, domain_uuid, rule_type=rule_type, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the prefilter rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all prefilter rules associated with the specified policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
rule_type = 'rule_type_example' # str | If parameter is specified, only the policies with specified <code>ruleType</code> will be shown. Allowed values are 'PREFILTER' and 'TUNNEL'. Cannot be used if object ID is specified in path. (optional)
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_prefilter_rule(container_uuid, domain_uuid, rule_type=rule_type, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_prefilter_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **rule_type** | **str**| If parameter is specified, only the policies with specified &lt;code&gt;ruleType&lt;/code&gt; will be shown. Allowed values are &#39;PREFILTER&#39; and &#39;TUNNEL&#39;. Cannot be used if object ID is specified in path. | [optional] 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**PrefilterRuleListContainer**](PrefilterRuleListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_snmp_config**
> SNMPConfigListContainer get_all_snmp_config(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the SNMP alert object associated with the specified ID. If no ID is specified, retrieves list of all SNMP alert objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_snmp_config(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_snmp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**SNMPConfigListContainer**](SNMPConfigListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_syslog_config**
> SyslogConfigListContainer get_all_syslog_config(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the syslog alert object associated with the specified ID. If no ID is specified, retrieves list of all syslog alert objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_syslog_config(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_syslog_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**SyslogConfigListContainer**](SyslogConfigListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vpn_advanced_settings**
> VpnAdvancedSettingsListContainer get_all_vpn_advanced_settings(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves and modifies a Advanced settings inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves list containing a single AdvancedSettings entry of the topology.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vpn_advanced_settings(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_vpn_advanced_settings: %s\n" % e)
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

[**VpnAdvancedSettingsListContainer**](VpnAdvancedSettingsListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vpn_endpoint**
> VpnEndpointListContainer get_all_vpn_endpoint(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies a specific Endpoint associated with the specified ID inside a VPN Site To Site Topology. If no ID is specifid for a GET, retrieves list of all Endpoints of a topology.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vpn_endpoint(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_vpn_endpoint: %s\n" % e)
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

[**VpnEndpointListContainer**](VpnEndpointListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vpn_ike_settings**
> VpnIkeSettingsListContainer get_all_vpn_ike_settings(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the IKE Settings associated with the specified ID inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves Ike Settings of a topology.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vpn_ike_settings(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_vpn_ike_settings: %s\n" % e)
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

[**VpnIkeSettingsListContainer**](VpnIkeSettingsListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vpn_ip_sec_settings**
> VpnIPSecSettingsListContainer get_all_vpn_ip_sec_settings(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves and modifies a IPSec Proposal settings inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves list containing a single IPSecSettings entry of the topology.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vpn_ip_sec_settings(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_vpn_ip_sec_settings: %s\n" % e)
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

[**VpnIPSecSettingsListContainer**](VpnIPSecSettingsListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_action**
> DefaultAction get_default_action(object_id, container_uuid, domain_uuid)



**Retrieves or modifies the default action associated with the specified access control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified access control policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a default action.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_default_action(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_default_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a default action. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**DefaultAction**](DefaultAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_policy**
> FilePolicy get_file_policy(object_id, domain_uuid)



**Retrieves the endpoint device type object associated with the specified ID. If no ID is specified, retrieves list of all endpoint device type objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a file policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_file_policy(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_file_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a file policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FilePolicy**](FilePolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_auto_nat_rule**
> FTDAutoNatRule get_ftd_auto_nat_rule(object_id, container_uuid, domain_uuid, section=section)



**Retrieves, deletes, creates, or modifies the Auto NAT rule associated with the specified ID. Also, retrieves list of all Auto NAT rules. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of an Auto NAT rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
section = 'section_example' # str | Retrieves, creates or modifies auto nat rule in given section. Allowed value is 'auto'. (optional)

try:
    api_response = api_instance.get_ftd_auto_nat_rule(object_id, container_uuid, domain_uuid, section=section)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_ftd_auto_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an Auto NAT rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **section** | **str**| Retrieves, creates or modifies auto nat rule in given section. Allowed value is &#39;auto&#39;. | [optional] 

### Return type

[**FTDAutoNatRule**](FTDAutoNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_manual_nat_rule**
> FTDManualNatRule get_ftd_manual_nat_rule(object_id, container_uuid, domain_uuid, section=section)



**Retrieves, deletes, creates, or modifies the Manual NAT rule associated with the specified ID. Also, retrieves list of all Manual NAT rules. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a Manual NAT rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
section = 'section_example' # str | Retrieves, creates or modifies manual nat rule in given section. Allowed value is 'before_auto' and 'after_auto'. (optional)

try:
    api_response = api_instance.get_ftd_manual_nat_rule(object_id, container_uuid, domain_uuid, section=section)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_ftd_manual_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a Manual NAT rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **section** | **str**| Retrieves, creates or modifies manual nat rule in given section. Allowed value is &#39;before_auto&#39; and &#39;after_auto&#39;. | [optional] 

### Return type

[**FTDManualNatRule**](FTDManualNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_nat_policy**
> FTDNatPolicy get_ftd_nat_policy(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the NAT policy associated with the specified ID. Also, retrieves list of all NAT policies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for NAT policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftd_nat_policy(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_ftd_nat_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for NAT policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDNatPolicy**](FTDNatPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_nat_rule**
> FTDNatRule get_ftd_nat_rule(object_id, container_uuid, domain_uuid, section=section)



**Retrieves list of all NAT rules (manual and auto) associated with the specified policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a NAT rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
section = 'section_example' # str | Retrieves nat rule in given section. Allowed value is 'before_auto', 'auto' and 'after_auto'. (optional)

try:
    api_response = api_instance.get_ftd_nat_rule(object_id, container_uuid, domain_uuid, section=section)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_ftd_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a NAT rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **section** | **str**| Retrieves nat rule in given section. Allowed value is &#39;before_auto&#39;, &#39;auto&#39; and &#39;after_auto&#39;. | [optional] 

### Return type

[**FTDNatRule**](FTDNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftds2_s_vpn_model**
> FTDS2SVpnModel get_ftds2_s_vpn_model(object_id, domain_uuid)



**Retrieves, deletes, creates, or modifies the FTD Site to Site VPN topology associated with the specified ID. If no ID is specified for a GET, retrieves list of all FTD Site to Site VPN topologies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for FTD Site to Site VPN topology.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftds2_s_vpn_model(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_ftds2_s_vpn_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for FTD Site to Site VPN topology. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDS2SVpnModel**](FTDS2SVpnModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hit_count**
> HitCountListContainer get_hit_count(filter, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, refreshes and clears Hit Count**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
filter = 'filter_example' # str | Value is of format (including quotes): <code>\"deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\"</code><br/><code>deviceId</code> is UUID of device and is a mandatory field.<br/><code>ids</code> returns hitcounts of access rules if set to list of rule UUIDs. If this key is not used, all access rules will be returned (Note that this is applicable only in GET and DELETE operations). <br/><code>fetchZeroHitCount</code> returns only access rules whose hit count is zero if <code>true</code> (Note that this is applicable only in GET operation and if <code>ids</code> is not used).
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_hit_count(filter, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_hit_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Value is of format (including quotes): &lt;code&gt;\&quot;deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\&quot;&lt;/code&gt;&lt;br/&gt;&lt;code&gt;deviceId&lt;/code&gt; is UUID of device and is a mandatory field.&lt;br/&gt;&lt;code&gt;ids&lt;/code&gt; returns hitcounts of access rules if set to list of rule UUIDs. If this key is not used, all access rules will be returned (Note that this is applicable only in GET and DELETE operations). &lt;br/&gt;&lt;code&gt;fetchZeroHitCount&lt;/code&gt; returns only access rules whose hit count is zero if &lt;code&gt;true&lt;/code&gt; (Note that this is applicable only in GET operation and if &lt;code&gt;ids&lt;/code&gt; is not used). | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**HitCountListContainer**](HitCountListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intrusion_policy**
> IntrusionPolicy get_intrusion_policy(object_id, domain_uuid)



**Retrieves the intrusion policy associated with the specified ID. If no ID is specified, retrieves list of all intrusion policies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for intrusion policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_intrusion_policy(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_intrusion_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for intrusion policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**IntrusionPolicy**](IntrusionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prefilter_default_action**
> PrefilterDefaultAction get_prefilter_default_action(object_id, container_uuid, domain_uuid)



**Retrieves or modifies the default action associated with the specified prefilter control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified prefilter policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a default action.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_prefilter_default_action(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_prefilter_default_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a default action. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterDefaultAction**](PrefilterDefaultAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prefilter_hit_count**
> PrefilterHitCountListContainer get_prefilter_hit_count(filter, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, refreshes and clears Hit Count**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
filter = 'filter_example' # str | Value is of format (including quotes): <code>\"deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\"</code><br/><code>deviceId</code> is UUID of device and is a mandatory field.<br/><code>ids</code> returns hitcounts of prefilter rules if set to list of rule UUIDs. If this key is not used, all prefilter rules will be returned (Note that this is applicable only in GET and DELETE operations). <br/><code>fetchZeroHitCount</code> returns only access rules whose hit count is zero if <code>true</code> (Note that this is applicable only in GET operation and if <code>ids</code> is not used).
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_prefilter_hit_count(filter, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_prefilter_hit_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Value is of format (including quotes): &lt;code&gt;\&quot;deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\&quot;&lt;/code&gt;&lt;br/&gt;&lt;code&gt;deviceId&lt;/code&gt; is UUID of device and is a mandatory field.&lt;br/&gt;&lt;code&gt;ids&lt;/code&gt; returns hitcounts of prefilter rules if set to list of rule UUIDs. If this key is not used, all prefilter rules will be returned (Note that this is applicable only in GET and DELETE operations). &lt;br/&gt;&lt;code&gt;fetchZeroHitCount&lt;/code&gt; returns only access rules whose hit count is zero if &lt;code&gt;true&lt;/code&gt; (Note that this is applicable only in GET operation and if &lt;code&gt;ids&lt;/code&gt; is not used). | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**PrefilterHitCountListContainer**](PrefilterHitCountListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prefilter_policy**
> PrefilterPolicy get_prefilter_policy(object_id, domain_uuid)



**Retrieves prefilter policy associated with the specified ID. Also, retrieves list of all prefilter policies.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for prefilter policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_prefilter_policy(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_prefilter_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for prefilter policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterPolicy**](PrefilterPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prefilter_rule**
> PrefilterRule get_prefilter_rule(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the prefilter rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all prefilter rules associated with the specified policy ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a prefilter rule.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_prefilter_rule(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_prefilter_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a prefilter rule. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterRule**](PrefilterRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snmp_config**
> SNMPConfig get_snmp_config(object_id, domain_uuid)



**Retrieves the SNMP alert object associated with the specified ID. If no ID is specified, retrieves list of all SNMP alert objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a SNMP alert.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_snmp_config(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_snmp_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a SNMP alert. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**SNMPConfig**](SNMPConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syslog_config**
> SyslogConfig get_syslog_config(object_id, domain_uuid)



**Retrieves the syslog alert object associated with the specified ID. If no ID is specified, retrieves list of all syslog alert objects.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a syslog alert.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_syslog_config(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_syslog_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a syslog alert. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**SyslogConfig**](SyslogConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpn_advanced_settings**
> VpnAdvancedSettings get_vpn_advanced_settings(object_id, container_uuid, domain_uuid)



**Retrieves and modifies a Advanced settings inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves list containing a single AdvancedSettings entry of the topology.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for Advanced settings in a Site to Site VPN topology.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vpn_advanced_settings(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_vpn_advanced_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for Advanced settings in a Site to Site VPN topology. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnAdvancedSettings**](VpnAdvancedSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpn_endpoint**
> VpnEndpoint get_vpn_endpoint(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies a specific Endpoint associated with the specified ID inside a VPN Site To Site Topology. If no ID is specifid for a GET, retrieves list of all Endpoints of a topology.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for an Endpoint in a Site to Site VPN topology.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vpn_endpoint(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_vpn_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for an Endpoint in a Site to Site VPN topology. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnEndpoint**](VpnEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpn_ike_settings**
> VpnIkeSettings get_vpn_ike_settings(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IKE Settings associated with the specified ID inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves Ike Settings of a topology.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for an Ike Settings policy in a Site to Site VPN topology.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vpn_ike_settings(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_vpn_ike_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for an Ike Settings policy in a Site to Site VPN topology. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnIkeSettings**](VpnIkeSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpn_ip_sec_settings**
> VpnIPSecSettings get_vpn_ip_sec_settings(object_id, container_uuid, domain_uuid)



**Retrieves and modifies a IPSec Proposal settings inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves list containing a single IPSecSettings entry of the topology.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for IPSec Proposal settings in a Site to Site VPN topology.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vpn_ip_sec_settings(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_vpn_ip_sec_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for IPSec Proposal settings in a Site to Site VPN topology. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnIPSecSettings**](VpnIPSecSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_policy**
> AccessPolicy update_access_policy(object_id, body, domain_uuid)



**Retrieves, deletes, creates, or modifies the access control policy associated with the specified ID. Also, retrieves list of all access control policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for access control policy.
body = swagger_client.AccessPolicy() # AccessPolicy | Input representation of access control policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_access_policy(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for access control policy. | 
 **body** | [**AccessPolicy**](AccessPolicy.md)| Input representation of access control policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicy**](AccessPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_policy_category**
> AccessPolicyCategory update_access_policy_category(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the category associated with the specified policy ID. If no ID is specified, retrieves list of all categories associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a category.
body = swagger_client.AccessPolicyCategory() # AccessPolicyCategory | The input category model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_access_policy_category(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_access_policy_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a category. | 
 **body** | [**AccessPolicyCategory**](AccessPolicyCategory.md)| The input category model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicyCategory**](AccessPolicyCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_policy_inheritance_setting**
> AccessPolicyInheritanceSetting update_access_policy_inheritance_setting(object_id, body, container_uuid, domain_uuid)



**Retrieves and modifies the inheritance settings associated with specified Access Policy. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of the Access Policy Inheritance Setting.
body = swagger_client.AccessPolicyInheritanceSetting() # AccessPolicyInheritanceSetting | Payload representing the Access Policy Inheritance Setting.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_access_policy_inheritance_setting(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_access_policy_inheritance_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of the Access Policy Inheritance Setting. | 
 **body** | [**AccessPolicyInheritanceSetting**](AccessPolicyInheritanceSetting.md)| Payload representing the Access Policy Inheritance Setting. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicyInheritanceSetting**](AccessPolicyInheritanceSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_policy_logging_setting_model**
> AccessPolicyLoggingSettingModel update_access_policy_logging_setting_model(object_id, body, container_uuid, domain_uuid)



**Retrieves or modifies the logging setting associated with the specified access control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified access control policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a logging setting.
body = swagger_client.AccessPolicyLoggingSettingModel() # AccessPolicyLoggingSettingModel | The input default action model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_access_policy_logging_setting_model(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_access_policy_logging_setting_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a logging setting. | 
 **body** | [**AccessPolicyLoggingSettingModel**](AccessPolicyLoggingSettingModel.md)| The input default action model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessPolicyLoggingSettingModel**](AccessPolicyLoggingSettingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_rule**
> AccessRule update_access_rule(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the access control rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all access rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of an access control rule.
body = swagger_client.AccessRule() # AccessRule | The input access control rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_access_rule(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an access control rule. | 
 **body** | [**AccessRule**](AccessRule.md)| The input access control rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessRule**](AccessRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_action**
> DefaultAction update_default_action(object_id, body, container_uuid, domain_uuid)



**Retrieves or modifies the default action associated with the specified access control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified access control policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a default action.
body = swagger_client.DefaultAction() # DefaultAction | The input default action model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_default_action(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_default_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a default action. | 
 **body** | [**DefaultAction**](DefaultAction.md)| The input default action model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**DefaultAction**](DefaultAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_auto_nat_rule**
> FTDAutoNatRule update_ftd_auto_nat_rule(object_id, body, container_uuid, domain_uuid, section=section)



**Retrieves, deletes, creates, or modifies the Auto NAT rule associated with the specified ID. Also, retrieves list of all Auto NAT rules.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of an Auto NAT rule.
body = swagger_client.FTDAutoNatRule() # FTDAutoNatRule | The input Auto NAT rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
section = 'section_example' # str | Retrieves, creates or modifies auto nat rule in given section. Allowed value is 'auto'. (optional)

try:
    api_response = api_instance.update_ftd_auto_nat_rule(object_id, body, container_uuid, domain_uuid, section=section)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_ftd_auto_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an Auto NAT rule. | 
 **body** | [**FTDAutoNatRule**](FTDAutoNatRule.md)| The input Auto NAT rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **section** | **str**| Retrieves, creates or modifies auto nat rule in given section. Allowed value is &#39;auto&#39;. | [optional] 

### Return type

[**FTDAutoNatRule**](FTDAutoNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_manual_nat_rule**
> FTDManualNatRule update_ftd_manual_nat_rule(object_id, body, container_uuid, domain_uuid, section=section, target_index=target_index)



**Retrieves, deletes, creates, or modifies the Manual NAT rule associated with the specified ID. Also, retrieves list of all Manual NAT rules.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a Manual NAT rule.
body = swagger_client.FTDManualNatRule() # FTDManualNatRule | The input Manual NAT rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
section = 'section_example' # str | Retrieves, creates or modifies manual nat rule in given section. Allowed value is 'before_auto' and 'after_auto'. (optional)
target_index = 'target_index_example' # str | Creates or modifies manual nat rule at given targetIndex. It takes an integer value.  (optional)

try:
    api_response = api_instance.update_ftd_manual_nat_rule(object_id, body, container_uuid, domain_uuid, section=section, target_index=target_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_ftd_manual_nat_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a Manual NAT rule. | 
 **body** | [**FTDManualNatRule**](FTDManualNatRule.md)| The input Manual NAT rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **section** | **str**| Retrieves, creates or modifies manual nat rule in given section. Allowed value is &#39;before_auto&#39; and &#39;after_auto&#39;. | [optional] 
 **target_index** | **str**| Creates or modifies manual nat rule at given targetIndex. It takes an integer value.  | [optional] 

### Return type

[**FTDManualNatRule**](FTDManualNatRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_nat_policy**
> FTDNatPolicy update_ftd_nat_policy(object_id, body, domain_uuid)



**Retrieves, deletes, creates, or modifies the NAT policy associated with the specified ID. Also, retrieves list of all NAT policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for NAT policy.
body = swagger_client.FTDNatPolicy() # FTDNatPolicy | Input representation of NAT policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftd_nat_policy(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_ftd_nat_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for NAT policy. | 
 **body** | [**FTDNatPolicy**](FTDNatPolicy.md)| Input representation of NAT policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDNatPolicy**](FTDNatPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftds2_s_vpn_model**
> FTDS2SVpnModel update_ftds2_s_vpn_model(object_id, body, domain_uuid)



**Retrieves, deletes, creates, or modifies the FTD Site to Site VPN topology associated with the specified ID. If no ID is specified for a GET, retrieves list of all FTD Site to Site VPN topologies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for FTD Site to Site VPN topology.
body = swagger_client.FTDS2SVpnModel() # FTDS2SVpnModel | Input representation of FTD Site to Site VPN topology.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftds2_s_vpn_model(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_ftds2_s_vpn_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for FTD Site to Site VPN topology. | 
 **body** | [**FTDS2SVpnModel**](FTDS2SVpnModel.md)| Input representation of FTD Site to Site VPN topology. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDS2SVpnModel**](FTDS2SVpnModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hit_count**
> HitCount update_hit_count(filter, container_uuid, domain_uuid)



**Retrieves, refreshes and clears Hit Count _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
filter = 'filter_example' # str | Value is of format (including quotes): <code>\"deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\"</code><br/><code>deviceId</code> is UUID of device and is a mandatory field.<br/><code>ids</code> returns hitcounts of access rules if set to list of rule UUIDs. If this key is not used, all access rules will be returned (Note that this is applicable only in GET and DELETE operations). <br/><code>fetchZeroHitCount</code> returns only access rules whose hit count is zero if <code>true</code> (Note that this is applicable only in GET operation and if <code>ids</code> is not used).
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_hit_count(filter, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_hit_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Value is of format (including quotes): &lt;code&gt;\&quot;deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\&quot;&lt;/code&gt;&lt;br/&gt;&lt;code&gt;deviceId&lt;/code&gt; is UUID of device and is a mandatory field.&lt;br/&gt;&lt;code&gt;ids&lt;/code&gt; returns hitcounts of access rules if set to list of rule UUIDs. If this key is not used, all access rules will be returned (Note that this is applicable only in GET and DELETE operations). &lt;br/&gt;&lt;code&gt;fetchZeroHitCount&lt;/code&gt; returns only access rules whose hit count is zero if &lt;code&gt;true&lt;/code&gt; (Note that this is applicable only in GET operation and if &lt;code&gt;ids&lt;/code&gt; is not used). | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**HitCount**](HitCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_multiple_access_rule**
> AccessRule update_multiple_access_rule(bulk, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the access control rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all access rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
bulk = true # bool | This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations.
body = swagger_client.AccessRule() # AccessRule | The input access control rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_multiple_access_rule(bulk, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_multiple_access_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk** | **bool**| This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations. | 
 **body** | [**AccessRule**](AccessRule.md)| The input access control rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**AccessRule**](AccessRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_multiple_prefilter_rule**
> PrefilterRule update_multiple_prefilter_rule(bulk, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the prefilter rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all prefilter rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
bulk = true # bool | This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations.
body = swagger_client.PrefilterRule() # PrefilterRule | The input prefilter rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_multiple_prefilter_rule(bulk, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_multiple_prefilter_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk** | **bool**| This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations. | 
 **body** | [**PrefilterRule**](PrefilterRule.md)| The input prefilter rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterRule**](PrefilterRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prefilter_default_action**
> PrefilterDefaultAction update_prefilter_default_action(object_id, body, container_uuid, domain_uuid)



**Retrieves or modifies the default action associated with the specified prefilter control policy ID and default action ID. If no default action ID is specified, retrieves list of all default actions associated with the specified prefilter policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a default action.
body = swagger_client.PrefilterDefaultAction() # PrefilterDefaultAction | The input default action model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_prefilter_default_action(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_prefilter_default_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a default action. | 
 **body** | [**PrefilterDefaultAction**](PrefilterDefaultAction.md)| The input default action model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterDefaultAction**](PrefilterDefaultAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prefilter_hit_count**
> PrefilterHitCount update_prefilter_hit_count(filter, container_uuid, domain_uuid)



**Retrieves, refreshes and clears Hit Count _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
filter = 'filter_example' # str | Value is of format (including quotes): <code>\"deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\"</code><br/><code>deviceId</code> is UUID of device and is a mandatory field.<br/><code>ids</code> returns hitcounts of prefilter rules if set to list of rule UUIDs. If this key is not used, all prefilter rules will be returned (Note that this is applicable only in GET and DELETE operations). <br/><code>fetchZeroHitCount</code> returns only access rules whose hit count is zero if <code>true</code> (Note that this is applicable only in GET operation and if <code>ids</code> is not used).
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_prefilter_hit_count(filter, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_prefilter_hit_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Value is of format (including quotes): &lt;code&gt;\&quot;deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false}\&quot;&lt;/code&gt;&lt;br/&gt;&lt;code&gt;deviceId&lt;/code&gt; is UUID of device and is a mandatory field.&lt;br/&gt;&lt;code&gt;ids&lt;/code&gt; returns hitcounts of prefilter rules if set to list of rule UUIDs. If this key is not used, all prefilter rules will be returned (Note that this is applicable only in GET and DELETE operations). &lt;br/&gt;&lt;code&gt;fetchZeroHitCount&lt;/code&gt; returns only access rules whose hit count is zero if &lt;code&gt;true&lt;/code&gt; (Note that this is applicable only in GET operation and if &lt;code&gt;ids&lt;/code&gt; is not used). | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterHitCount**](PrefilterHitCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prefilter_policy**
> PrefilterPolicy update_prefilter_policy(object_id, body, domain_uuid)



**Retrieves prefilter policy associated with the specified ID. Also, retrieves list of all prefilter policies. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for prefilter policy.
body = swagger_client.PrefilterPolicy() # PrefilterPolicy | Input representation of prefilter policy.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_prefilter_policy(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_prefilter_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for prefilter policy. | 
 **body** | [**PrefilterPolicy**](PrefilterPolicy.md)| Input representation of prefilter policy. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterPolicy**](PrefilterPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prefilter_rule**
> PrefilterRule update_prefilter_rule(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the prefilter rule associated with the specified policy ID and rule ID. If no ID is specified, retrieves list of all prefilter rules associated with the specified policy ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Unique identifier of a prefilter rule.
body = swagger_client.PrefilterRule() # PrefilterRule | The input prefilter rule model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_prefilter_rule(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_prefilter_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a prefilter rule. | 
 **body** | [**PrefilterRule**](PrefilterRule.md)| The input prefilter rule model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**PrefilterRule**](PrefilterRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_advanced_settings**
> VpnAdvancedSettings update_vpn_advanced_settings(object_id, body, container_uuid, domain_uuid)



**Retrieves and modifies a Advanced settings inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves list containing a single AdvancedSettings entry of the topology. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for Advanced settings in a Site to Site VPN topology.
body = swagger_client.VpnAdvancedSettings() # VpnAdvancedSettings | Input representation of Advanced settings in a Site to Site VPN topology.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_vpn_advanced_settings(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_vpn_advanced_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for Advanced settings in a Site to Site VPN topology. | 
 **body** | [**VpnAdvancedSettings**](VpnAdvancedSettings.md)| Input representation of Advanced settings in a Site to Site VPN topology. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnAdvancedSettings**](VpnAdvancedSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_endpoint**
> VpnEndpoint update_vpn_endpoint(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies a specific Endpoint associated with the specified ID inside a VPN Site To Site Topology. If no ID is specifid for a GET, retrieves list of all Endpoints of a topology. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for an Endpoint in a Site to Site VPN topology.
body = swagger_client.VpnEndpoint() # VpnEndpoint | Input representation of Endpoint.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_vpn_endpoint(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_vpn_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for an Endpoint in a Site to Site VPN topology. | 
 **body** | [**VpnEndpoint**](VpnEndpoint.md)| Input representation of Endpoint. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnEndpoint**](VpnEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_ike_settings**
> VpnIkeSettings update_vpn_ike_settings(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IKE Settings associated with the specified ID inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves Ike Settings of a topology. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for an Ike Settings policy in a Site to Site VPN topology.
body = swagger_client.VpnIkeSettings() # VpnIkeSettings | Input representation of Ike Settings.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_vpn_ike_settings(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_vpn_ike_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for an Ike Settings policy in a Site to Site VPN topology. | 
 **body** | [**VpnIkeSettings**](VpnIkeSettings.md)| Input representation of Ike Settings. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnIkeSettings**](VpnIkeSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpn_ip_sec_settings**
> VpnIPSecSettings update_vpn_ip_sec_settings(object_id, body, container_uuid, domain_uuid)



**Retrieves and modifies a IPSec Proposal settings inside a VPN Site To Site Topology. If no ID is specified for a GET, retrieves list containing a single IPSecSettings entry of the topology. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PolicyApi()
object_id = 'object_id_example' # str | Identifier for IPSec Proposal settings in a Site to Site VPN topology.
body = swagger_client.VpnIPSecSettings() # VpnIPSecSettings | Input representation of IPSec Proposal settings.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_vpn_ip_sec_settings(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_vpn_ip_sec_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for IPSec Proposal settings in a Site to Site VPN topology. | 
 **body** | [**VpnIPSecSettings**](VpnIPSecSettings.md)| Input representation of IPSec Proposal settings. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VpnIPSecSettings**](VpnIPSecSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

