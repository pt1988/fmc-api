# swagger_client.DevicesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DevicesApi.md#create_device) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords | 
[**create_device_copy_config_request**](DevicesApi.md#create_device_copy_config_request) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/copyconfigrequests | 
[**create_fp_logical_interface**](DevicesApi.md#create_fp_logical_interface) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fplogicalinterfaces | 
[**create_ftd_bridge_group_interface**](DevicesApi.md#create_ftd_bridge_group_interface) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/bridgegroupinterfaces | 
[**create_ftd_ether_channel_interface**](DevicesApi.md#create_ftd_ether_channel_interface) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/etherchannelinterfaces | 
[**create_ftd_redundant_interface**](DevicesApi.md#create_ftd_redundant_interface) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/redundantinterfaces | 
[**create_ftd_vlan_interface**](DevicesApi.md#create_ftd_vlan_interface) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/vlaninterfaces | 
[**create_inline_set**](DevicesApi.md#create_inline_set) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/inlinesets | 
[**create_interface_event**](DevicesApi.md#create_interface_event) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/interfaceevents | 
[**create_multiple_ftd_sub_interface**](DevicesApi.md#create_multiple_ftd_sub_interface) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/subinterfaces | 
[**create_multiple_i_pv4_static_route_model**](DevicesApi.md#create_multiple_i_pv4_static_route_model) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv4staticroutes | 
[**create_multiple_i_pv6_static_route_model**](DevicesApi.md#create_multiple_i_pv6_static_route_model) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv6staticroutes | 
[**create_virtual_router_model**](DevicesApi.md#create_virtual_router_model) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters | 
[**create_virtual_switch**](DevicesApi.md#create_virtual_switch) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/virtualswitches | 
[**create_vrf_i_pv4_static_route_model**](DevicesApi.md#create_vrf_i_pv4_static_route_model) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv4staticroutes | 
[**create_vrf_i_pv6_static_route_model**](DevicesApi.md#create_vrf_i_pv6_static_route_model) | **POST** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv6staticroutes | 
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{objectId} | 
[**delete_fp_logical_interface**](DevicesApi.md#delete_fp_logical_interface) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fplogicalinterfaces/{objectId} | 
[**delete_ftd_bridge_group_interface**](DevicesApi.md#delete_ftd_bridge_group_interface) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/bridgegroupinterfaces/{objectId} | 
[**delete_ftd_ether_channel_interface**](DevicesApi.md#delete_ftd_ether_channel_interface) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/etherchannelinterfaces/{objectId} | 
[**delete_ftd_redundant_interface**](DevicesApi.md#delete_ftd_redundant_interface) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/redundantinterfaces/{objectId} | 
[**delete_ftd_sub_interface**](DevicesApi.md#delete_ftd_sub_interface) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/subinterfaces/{objectId} | 
[**delete_ftd_vlan_interface**](DevicesApi.md#delete_ftd_vlan_interface) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/vlaninterfaces/{objectId} | 
[**delete_i_pv4_static_route_model**](DevicesApi.md#delete_i_pv4_static_route_model) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv4staticroutes/{objectId} | 
[**delete_i_pv6_static_route_model**](DevicesApi.md#delete_i_pv6_static_route_model) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv6staticroutes/{objectId} | 
[**delete_inline_set**](DevicesApi.md#delete_inline_set) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/inlinesets/{objectId} | 
[**delete_virtual_router_model**](DevicesApi.md#delete_virtual_router_model) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{objectId} | 
[**delete_virtual_switch**](DevicesApi.md#delete_virtual_switch) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/virtualswitches/{objectId} | 
[**delete_vrf_i_pv4_static_route_model**](DevicesApi.md#delete_vrf_i_pv4_static_route_model) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv4staticroutes/{objectId} | 
[**delete_vrf_i_pv6_static_route_model**](DevicesApi.md#delete_vrf_i_pv6_static_route_model) | **DELETE** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv6staticroutes/{objectId} | 
[**get_all_bgp_general_setting_model**](DevicesApi.md#get_all_bgp_general_setting_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/bgpgeneralsettings | 
[**get_all_bgpi_pv_address_family_model**](DevicesApi.md#get_all_bgpi_pv_address_family_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/bgp | 
[**get_all_device**](DevicesApi.md#get_all_device) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords | 
[**get_all_fp_logical_interface**](DevicesApi.md#get_all_fp_logical_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fplogicalinterfaces | 
[**get_all_fp_physical_interface**](DevicesApi.md#get_all_fp_physical_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fpphysicalinterfaces | 
[**get_all_ftd_bridge_group_interface**](DevicesApi.md#get_all_ftd_bridge_group_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/bridgegroupinterfaces | 
[**get_all_ftd_ether_channel_interface**](DevicesApi.md#get_all_ftd_ether_channel_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/etherchannelinterfaces | 
[**get_all_ftd_physical_interface**](DevicesApi.md#get_all_ftd_physical_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/physicalinterfaces | 
[**get_all_ftd_redundant_interface**](DevicesApi.md#get_all_ftd_redundant_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/redundantinterfaces | 
[**get_all_ftd_sub_interface**](DevicesApi.md#get_all_ftd_sub_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/subinterfaces | 
[**get_all_ftd_vlan_interface**](DevicesApi.md#get_all_ftd_vlan_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/vlaninterfaces | 
[**get_all_i_pv4_static_route_model**](DevicesApi.md#get_all_i_pv4_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv4staticroutes | 
[**get_all_i_pv6_static_route_model**](DevicesApi.md#get_all_i_pv6_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv6staticroutes | 
[**get_all_inline_set**](DevicesApi.md#get_all_inline_set) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/inlinesets | 
[**get_all_ospf_interface_policy_model**](DevicesApi.md#get_all_ospf_interface_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ospfinterface | 
[**get_all_ospf_policy_model**](DevicesApi.md#get_all_ospf_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ospfv2routes | 
[**get_all_ospfv3_interface_policy_model**](DevicesApi.md#get_all_ospfv3_interface_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ospfv3interfaces | 
[**get_all_ospfv3_policy_model**](DevicesApi.md#get_all_ospfv3_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ospfv3routes | 
[**get_all_static_route_model**](DevicesApi.md#get_all_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/staticroutes | 
[**get_all_virtual_router_model**](DevicesApi.md#get_all_virtual_router_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters | 
[**get_all_virtual_switch**](DevicesApi.md#get_all_virtual_switch) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/virtualswitches | 
[**get_all_vrf_bgpi_pv_address_family_model**](DevicesApi.md#get_all_vrf_bgpi_pv_address_family_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/bgp | 
[**get_all_vrf_i_pv4_static_route_model**](DevicesApi.md#get_all_vrf_i_pv4_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv4staticroutes | 
[**get_all_vrf_i_pv6_static_route_model**](DevicesApi.md#get_all_vrf_i_pv6_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv6staticroutes | 
[**get_all_vrf_ospf_interface_policy_model**](DevicesApi.md#get_all_vrf_ospf_interface_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ospfinterface | 
[**get_all_vrf_ospf_policy_model**](DevicesApi.md#get_all_vrf_ospf_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ospfv2routes | 
[**get_all_vrf_static_route_model**](DevicesApi.md#get_all_vrf_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/staticroutes | 
[**get_bgp_general_setting_model**](DevicesApi.md#get_bgp_general_setting_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/bgpgeneralsettings/{objectId} | 
[**get_bgpi_pv_address_family_model**](DevicesApi.md#get_bgpi_pv_address_family_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/bgp/{objectId} | 
[**get_commands**](DevicesApi.md#get_commands) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/operational/commands | 
[**get_device**](DevicesApi.md#get_device) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{objectId} | 
[**get_fp_interface_statistics**](DevicesApi.md#get_fp_interface_statistics) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fpinterfacestatistics | 
[**get_fp_logical_interface**](DevicesApi.md#get_fp_logical_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fplogicalinterfaces/{objectId} | 
[**get_fp_physical_interface**](DevicesApi.md#get_fp_physical_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fpphysicalinterfaces/{objectId} | 
[**get_ftd_bridge_group_interface**](DevicesApi.md#get_ftd_bridge_group_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/bridgegroupinterfaces/{objectId} | 
[**get_ftd_ether_channel_interface**](DevicesApi.md#get_ftd_ether_channel_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/etherchannelinterfaces/{objectId} | 
[**get_ftd_physical_interface**](DevicesApi.md#get_ftd_physical_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/physicalinterfaces/{objectId} | 
[**get_ftd_redundant_interface**](DevicesApi.md#get_ftd_redundant_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/redundantinterfaces/{objectId} | 
[**get_ftd_sub_interface**](DevicesApi.md#get_ftd_sub_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/subinterfaces/{objectId} | 
[**get_ftd_vlan_interface**](DevicesApi.md#get_ftd_vlan_interface) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/vlaninterfaces/{objectId} | 
[**get_health_monitor_model**](DevicesApi.md#get_health_monitor_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/operational/metrics | 
[**get_i_pv4_static_route_model**](DevicesApi.md#get_i_pv4_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv4staticroutes/{objectId} | 
[**get_i_pv6_static_route_model**](DevicesApi.md#get_i_pv6_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv6staticroutes/{objectId} | 
[**get_inline_set**](DevicesApi.md#get_inline_set) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/inlinesets/{objectId} | 
[**get_interface_event**](DevicesApi.md#get_interface_event) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/interfaceevents | 
[**get_ospf_interface_policy_model**](DevicesApi.md#get_ospf_interface_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ospfinterface/{objectId} | 
[**get_ospf_policy_model**](DevicesApi.md#get_ospf_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ospfv2routes/{objectId} | 
[**get_ospfv3_interface_policy_model**](DevicesApi.md#get_ospfv3_interface_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ospfv3interfaces/{objectId} | 
[**get_ospfv3_policy_model**](DevicesApi.md#get_ospfv3_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ospfv3routes/{objectId} | 
[**get_static_route_model**](DevicesApi.md#get_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/staticroutes/{objectId} | 
[**get_virtual_router_model**](DevicesApi.md#get_virtual_router_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{objectId} | 
[**get_virtual_switch**](DevicesApi.md#get_virtual_switch) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/virtualswitches/{objectId} | 
[**get_vrf_bgpi_pv_address_family_model**](DevicesApi.md#get_vrf_bgpi_pv_address_family_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/bgp/{objectId} | 
[**get_vrf_i_pv4_static_route_model**](DevicesApi.md#get_vrf_i_pv4_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv4staticroutes/{objectId} | 
[**get_vrf_i_pv6_static_route_model**](DevicesApi.md#get_vrf_i_pv6_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv6staticroutes/{objectId} | 
[**get_vrf_ospf_interface_policy_model**](DevicesApi.md#get_vrf_ospf_interface_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ospfinterface/{objectId} | 
[**get_vrf_ospf_policy_model**](DevicesApi.md#get_vrf_ospf_policy_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ospfv2routes/{objectId} | 
[**get_vrf_static_route_model**](DevicesApi.md#get_vrf_static_route_model) | **GET** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/staticroutes/{objectId} | 
[**update_device**](DevicesApi.md#update_device) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{objectId} | 
[**update_fp_logical_interface**](DevicesApi.md#update_fp_logical_interface) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fplogicalinterfaces/{objectId} | 
[**update_fp_physical_interface**](DevicesApi.md#update_fp_physical_interface) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/fpphysicalinterfaces/{objectId} | 
[**update_ftd_bridge_group_interface**](DevicesApi.md#update_ftd_bridge_group_interface) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/bridgegroupinterfaces/{objectId} | 
[**update_ftd_ether_channel_interface**](DevicesApi.md#update_ftd_ether_channel_interface) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/etherchannelinterfaces/{objectId} | 
[**update_ftd_physical_interface**](DevicesApi.md#update_ftd_physical_interface) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/physicalinterfaces/{objectId} | 
[**update_ftd_redundant_interface**](DevicesApi.md#update_ftd_redundant_interface) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/redundantinterfaces/{objectId} | 
[**update_ftd_sub_interface**](DevicesApi.md#update_ftd_sub_interface) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/subinterfaces/{objectId} | 
[**update_ftd_vlan_interface**](DevicesApi.md#update_ftd_vlan_interface) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/vlaninterfaces/{objectId} | 
[**update_i_pv4_static_route_model**](DevicesApi.md#update_i_pv4_static_route_model) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv4staticroutes/{objectId} | 
[**update_i_pv6_static_route_model**](DevicesApi.md#update_i_pv6_static_route_model) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ipv6staticroutes/{objectId} | 
[**update_inline_set**](DevicesApi.md#update_inline_set) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/inlinesets/{objectId} | 
[**update_virtual_router_model**](DevicesApi.md#update_virtual_router_model) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{objectId} | 
[**update_virtual_switch**](DevicesApi.md#update_virtual_switch) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/virtualswitches/{objectId} | 
[**update_vrf_i_pv4_static_route_model**](DevicesApi.md#update_vrf_i_pv4_static_route_model) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv4staticroutes/{objectId} | 
[**update_vrf_i_pv6_static_route_model**](DevicesApi.md#update_vrf_i_pv6_static_route_model) | **PUT** /api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/ipv6staticroutes/{objectId} | 


# **create_device**
> Device create_device(body, domain_uuid)



**Retrieves or modifies the device record associated with the specified ID. Registers or unregisters a device. If no ID is specified for a GET, retrieves list of all device records. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.Device() # Device | Input representation of device.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_device(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Device**](Device.md)| Input representation of device. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_copy_config_request**
> DeviceCopyConfigRequest create_device_copy_config_request(body, domain_uuid)



**Copy configuration operation on device. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.DeviceCopyConfigRequest() # DeviceCopyConfigRequest | Input for Copy configuration request.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_device_copy_config_request(body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device_copy_config_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceCopyConfigRequest**](DeviceCopyConfigRequest.md)| Input for Copy configuration request. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**DeviceCopyConfigRequest**](DeviceCopyConfigRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fp_logical_interface**
> FPLogicalInterface create_fp_logical_interface(body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the logical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all logical interfaces associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.FPLogicalInterface() # FPLogicalInterface | The input logical interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_fp_logical_interface(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_fp_logical_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FPLogicalInterface**](FPLogicalInterface.md)| The input logical interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FPLogicalInterface**](FPLogicalInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ftd_bridge_group_interface**
> FTDBridgeGroupInterface create_ftd_bridge_group_interface(body, container_uuid, domain_uuid)



**Retrieves the bridge group interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all bridge group interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.FTDBridgeGroupInterface() # FTDBridgeGroupInterface | The input bridge group interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_ftd_bridge_group_interface(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_ftd_bridge_group_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDBridgeGroupInterface**](FTDBridgeGroupInterface.md)| The input bridge group interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDBridgeGroupInterface**](FTDBridgeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ftd_ether_channel_interface**
> FTDEtherChannelInterface create_ftd_ether_channel_interface(body, container_uuid, domain_uuid)



**Retrieves the ethernet channel interface associated with the specified NGFW device ID and interface ID. If no ID is specified, retrieves list of all ethernet channel interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.FTDEtherChannelInterface() # FTDEtherChannelInterface | The input ethernet channel interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_ftd_ether_channel_interface(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_ftd_ether_channel_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDEtherChannelInterface**](FTDEtherChannelInterface.md)| The input ethernet channel interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDEtherChannelInterface**](FTDEtherChannelInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ftd_redundant_interface**
> FTDRedundantInterface create_ftd_redundant_interface(body, container_uuid, domain_uuid)



**Retrieves the redundant interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all redundant interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.FTDRedundantInterface() # FTDRedundantInterface | The input redundant interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_ftd_redundant_interface(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_ftd_redundant_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDRedundantInterface**](FTDRedundantInterface.md)| The input redundant interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDRedundantInterface**](FTDRedundantInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ftd_vlan_interface**
> FTDVlanInterface create_ftd_vlan_interface(body, container_uuid, domain_uuid)



**Retrieves the vlan interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all vlan interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.FTDVlanInterface() # FTDVlanInterface | The input NGFW vlan interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_ftd_vlan_interface(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_ftd_vlan_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDVlanInterface**](FTDVlanInterface.md)| The input NGFW vlan interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDVlanInterface**](FTDVlanInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inline_set**
> InlineSet create_inline_set(body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the inline set associated with the specified NGIPS device ID and inline set ID. If no inline set ID is specified, retrieves list of all inline sets associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.InlineSet() # InlineSet | The input inline set model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_inline_set(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_inline_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineSet**](InlineSet.md)| The input inline set model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**InlineSet**](InlineSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interface_event**
> InterfaceEvent create_interface_event(body, container_uuid, domain_uuid)



**Retrieves list of all netmod events on the device. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.InterfaceEvent() # InterfaceEvent | The input representing action to be performed on netmod events. 
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_interface_event(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_interface_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterfaceEvent**](InterfaceEvent.md)| The input representing action to be performed on netmod events.  | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**InterfaceEvent**](InterfaceEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_ftd_sub_interface**
> FTDSubInterface create_multiple_ftd_sub_interface(body, container_uuid, domain_uuid, bulk=bulk)



**Retrieves the sub-interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all sub-interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.FTDSubInterface() # FTDSubInterface | The input sub-interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
bulk = true # bool | Enables bulk create for FTD sub interfaces. (optional)

try:
    api_response = api_instance.create_multiple_ftd_sub_interface(body, container_uuid, domain_uuid, bulk=bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_multiple_ftd_sub_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FTDSubInterface**](FTDSubInterface.md)| The input sub-interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **bulk** | **bool**| Enables bulk create for FTD sub interfaces. | [optional] 

### Return type

[**FTDSubInterface**](FTDSubInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_i_pv4_static_route_model**
> IPv4StaticRouteModel create_multiple_i_pv4_static_route_model(body, container_uuid, domain_uuid, bulk=bulk)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified ID. Also, retrieves list of all IPv4 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.IPv4StaticRouteModel() # IPv4StaticRouteModel | The input IPv4 Static Route model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
bulk = true # bool | Enables bulk create for IPv4 static routes. (optional)

try:
    api_response = api_instance.create_multiple_i_pv4_static_route_model(body, container_uuid, domain_uuid, bulk=bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_multiple_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPv4StaticRouteModel**](IPv4StaticRouteModel.md)| The input IPv4 Static Route model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **bulk** | **bool**| Enables bulk create for IPv4 static routes. | [optional] 

### Return type

[**IPv4StaticRouteModel**](IPv4StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_i_pv6_static_route_model**
> IPv6StaticRouteModel create_multiple_i_pv6_static_route_model(body, container_uuid, domain_uuid, bulk=bulk)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified ID. Also, retrieves list of all IPv6 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.IPv6StaticRouteModel() # IPv6StaticRouteModel | The input IPv6 Static Route model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
bulk = true # bool | Enables bulk create for IPv6 static routes. (optional)

try:
    api_response = api_instance.create_multiple_i_pv6_static_route_model(body, container_uuid, domain_uuid, bulk=bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_multiple_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPv6StaticRouteModel**](IPv6StaticRouteModel.md)| The input IPv6 Static Route model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **bulk** | **bool**| Enables bulk create for IPv6 static routes. | [optional] 

### Return type

[**IPv6StaticRouteModel**](IPv6StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_router_model**
> VirtualRouterModel create_virtual_router_model(body, container_uuid, domain_uuid)



**Retrieves list of all virtual routers created in the specified device. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.VirtualRouterModel() # VirtualRouterModel | The input Virtual Router Model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_virtual_router_model(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_virtual_router_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VirtualRouterModel**](VirtualRouterModel.md)| The input Virtual Router Model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VirtualRouterModel**](VirtualRouterModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_switch**
> VirtualSwitch create_virtual_switch(body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the virtual switch associated with the specified NGIPS device ID and virtual switch ID. If no virtual switch ID is specified, retrieves list of all virtual switches associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.VirtualSwitch() # VirtualSwitch | The input virtual switch model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_virtual_switch(body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_virtual_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VirtualSwitch**](VirtualSwitch.md)| The input virtual switch model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VirtualSwitch**](VirtualSwitch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vrf_i_pv4_static_route_model**
> VrfIPv4StaticRouteModel create_vrf_i_pv4_static_route_model(body, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified virtual router. Also, retrieves list of all IPv4 Static routes.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.VrfIPv4StaticRouteModel() # VrfIPv4StaticRouteModel | The input IPv4 Static Route model.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_vrf_i_pv4_static_route_model(body, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_vrf_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VrfIPv4StaticRouteModel**](VrfIPv4StaticRouteModel.md)| The input IPv4 Static Route model. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfIPv4StaticRouteModel**](VrfIPv4StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vrf_i_pv6_static_route_model**
> VrfIPv6StaticRouteModel create_vrf_i_pv6_static_route_model(body, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified virtual router. Also, retrieves list of all IPv6 Static routes.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
body = swagger_client.VrfIPv6StaticRouteModel() # VrfIPv6StaticRouteModel | The input IPv6 Static Route model.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.create_vrf_i_pv6_static_route_model(body, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_vrf_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VrfIPv6StaticRouteModel**](VrfIPv6StaticRouteModel.md)| The input IPv6 Static Route model. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfIPv6StaticRouteModel**](VrfIPv6StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> Device delete_device(object_id, domain_uuid)



**Retrieves or modifies the device record associated with the specified ID. Registers or unregisters a device. If no ID is specified for a GET, retrieves list of all device records. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Identifier for a device.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_device(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for a device. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fp_logical_interface**
> FPLogicalInterface delete_fp_logical_interface(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the logical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all logical interfaces associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a logical interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_fp_logical_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_fp_logical_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a logical interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FPLogicalInterface**](FPLogicalInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftd_bridge_group_interface**
> FTDBridgeGroupInterface delete_ftd_bridge_group_interface(object_id, container_uuid, domain_uuid)



**Retrieves the bridge group interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all bridge group interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a bridge group interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftd_bridge_group_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_ftd_bridge_group_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a bridge group interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDBridgeGroupInterface**](FTDBridgeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftd_ether_channel_interface**
> FTDEtherChannelInterface delete_ftd_ether_channel_interface(object_id, container_uuid, domain_uuid)



**Retrieves the ethernet channel interface associated with the specified NGFW device ID and interface ID. If no ID is specified, retrieves list of all ethernet channel interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a ethernet channel interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftd_ether_channel_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_ftd_ether_channel_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a ethernet channel interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDEtherChannelInterface**](FTDEtherChannelInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftd_redundant_interface**
> FTDRedundantInterface delete_ftd_redundant_interface(object_id, container_uuid, domain_uuid)



**Retrieves the redundant interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all redundant interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a redundant interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftd_redundant_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_ftd_redundant_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a redundant interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDRedundantInterface**](FTDRedundantInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftd_sub_interface**
> FTDSubInterface delete_ftd_sub_interface(object_id, container_uuid, domain_uuid)



**Retrieves the sub-interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all sub-interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a sub-interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftd_sub_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_ftd_sub_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a sub-interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDSubInterface**](FTDSubInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ftd_vlan_interface**
> FTDVlanInterface delete_ftd_vlan_interface(object_id, container_uuid, domain_uuid)



**Retrieves the vlan interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all vlan interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a NGFW vlan interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_ftd_vlan_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_ftd_vlan_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a NGFW vlan interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDVlanInterface**](FTDVlanInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_i_pv4_static_route_model**
> IPv4StaticRouteModel delete_i_pv4_static_route_model(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified ID. Also, retrieves list of all IPv4 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv4 Static Route.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_i_pv4_static_route_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv4 Static Route. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**IPv4StaticRouteModel**](IPv4StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_i_pv6_static_route_model**
> IPv6StaticRouteModel delete_i_pv6_static_route_model(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified ID. Also, retrieves list of all IPv6 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv6 Static Route.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_i_pv6_static_route_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv6 Static Route. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**IPv6StaticRouteModel**](IPv6StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inline_set**
> InlineSet delete_inline_set(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the inline set associated with the specified NGIPS device ID and inline set ID. If no inline set ID is specified, retrieves list of all inline sets associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of an inline set.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_inline_set(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_inline_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an inline set. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**InlineSet**](InlineSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_router_model**
> VirtualRouterModel delete_virtual_router_model(object_id, container_uuid, domain_uuid)



**Retrieves list of all virtual routers created in the specified device. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_virtual_router_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_virtual_router_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VirtualRouterModel**](VirtualRouterModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_switch**
> VirtualSwitch delete_virtual_switch(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the virtual switch associated with the specified NGIPS device ID and virtual switch ID. If no virtual switch ID is specified, retrieves list of all virtual switches associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a virtual switch.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_virtual_switch(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_virtual_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a virtual switch. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VirtualSwitch**](VirtualSwitch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vrf_i_pv4_static_route_model**
> VrfIPv4StaticRouteModel delete_vrf_i_pv4_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified virtual router. Also, retrieves list of all IPv4 Static routes.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv4 Static Route.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_vrf_i_pv4_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_vrf_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv4 Static Route. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfIPv4StaticRouteModel**](VrfIPv4StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vrf_i_pv6_static_route_model**
> VrfIPv6StaticRouteModel delete_vrf_i_pv6_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified virtual router. Also, retrieves list of all IPv6 Static routes.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv6 Static Route.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.delete_vrf_i_pv6_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_vrf_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv6 Static Route. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfIPv6StaticRouteModel**](VrfIPv6StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bgp_general_setting_model**
> BGPGeneralSettingModelListContainer get_all_bgp_general_setting_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves BGP general settings associated with the specified device.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_bgp_general_setting_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_bgp_general_setting_model: %s\n" % e)
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

[**BGPGeneralSettingModelListContainer**](BGPGeneralSettingModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bgpi_pv_address_family_model**
> BGPIPvAddressFamilyModelListContainer get_all_bgpi_pv_address_family_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of all BGP (ipv4 and ipv6) associated with the specified device. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_bgpi_pv_address_family_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_bgpi_pv_address_family_model: %s\n" % e)
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

[**BGPIPvAddressFamilyModelListContainer**](BGPIPvAddressFamilyModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_device**
> DeviceListContainer get_all_device(domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves or modifies the device record associated with the specified ID. Registers or unregisters a device. If no ID is specified for a GET, retrieves list of all device records.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_device(domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**DeviceListContainer**](DeviceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_fp_logical_interface**
> FPLogicalInterfaceListContainer get_all_fp_logical_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the logical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all logical interfaces associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_fp_logical_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_fp_logical_interface: %s\n" % e)
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

[**FPLogicalInterfaceListContainer**](FPLogicalInterfaceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_fp_physical_interface**
> FPPhysicalInterfaceListContainer get_all_fp_physical_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the physical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all physical interfaces associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_fp_physical_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_fp_physical_interface: %s\n" % e)
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

[**FPPhysicalInterfaceListContainer**](FPPhysicalInterfaceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_bridge_group_interface**
> FTDBridgeGroupInterfaceListContainer get_all_ftd_bridge_group_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the bridge group interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all bridge group interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_bridge_group_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ftd_bridge_group_interface: %s\n" % e)
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

[**FTDBridgeGroupInterfaceListContainer**](FTDBridgeGroupInterfaceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_ether_channel_interface**
> FTDEtherChannelInterfaceListContainer get_all_ftd_ether_channel_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the ethernet channel interface associated with the specified NGFW device ID and interface ID. If no ID is specified, retrieves list of all ethernet channel interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_ether_channel_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ftd_ether_channel_interface: %s\n" % e)
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

[**FTDEtherChannelInterfaceListContainer**](FTDEtherChannelInterfaceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_physical_interface**
> FTDPhysicalInterfaceListContainer get_all_ftd_physical_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the physical interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all physical interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_physical_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ftd_physical_interface: %s\n" % e)
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

[**FTDPhysicalInterfaceListContainer**](FTDPhysicalInterfaceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_redundant_interface**
> FTDRedundantInterfaceListContainer get_all_ftd_redundant_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the redundant interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all redundant interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_redundant_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ftd_redundant_interface: %s\n" % e)
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

[**FTDRedundantInterfaceListContainer**](FTDRedundantInterfaceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_sub_interface**
> FTDSubInterfaceListContainer get_all_ftd_sub_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the sub-interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all sub-interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_sub_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ftd_sub_interface: %s\n" % e)
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

[**FTDSubInterfaceListContainer**](FTDSubInterfaceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ftd_vlan_interface**
> FTDVlanInterfaceListContainer get_all_ftd_vlan_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves the vlan interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all vlan interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ftd_vlan_interface(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ftd_vlan_interface: %s\n" % e)
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

[**FTDVlanInterfaceListContainer**](FTDVlanInterfaceListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_i_pv4_static_route_model**
> IPv4StaticRouteModelListContainer get_all_i_pv4_static_route_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified ID. Also, retrieves list of all IPv4 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_i_pv4_static_route_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_i_pv4_static_route_model: %s\n" % e)
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

[**IPv4StaticRouteModelListContainer**](IPv4StaticRouteModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_i_pv6_static_route_model**
> IPv6StaticRouteModelListContainer get_all_i_pv6_static_route_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified ID. Also, retrieves list of all IPv6 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_i_pv6_static_route_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_i_pv6_static_route_model: %s\n" % e)
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

[**IPv6StaticRouteModelListContainer**](IPv6StaticRouteModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_inline_set**
> InlineSetListContainer get_all_inline_set(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the inline set associated with the specified NGIPS device ID and inline set ID. If no inline set ID is specified, retrieves list of all inline sets associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_inline_set(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_inline_set: %s\n" % e)
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

[**InlineSetListContainer**](InlineSetListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ospf_interface_policy_model**
> OspfInterfacePolicyModelListContainer get_all_ospf_interface_policy_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the OSPF Interface associated with the specified ID. Also, retrieves list of all OSPF v2 process. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ospf_interface_policy_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ospf_interface_policy_model: %s\n" % e)
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

[**OspfInterfacePolicyModelListContainer**](OspfInterfacePolicyModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ospf_policy_model**
> OspfPolicyModelListContainer get_all_ospf_policy_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the OSPF V2 associated with the specified ID. Also, retrieves list of all OSPF v2 process. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ospf_policy_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ospf_policy_model: %s\n" % e)
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

[**OspfPolicyModelListContainer**](OspfPolicyModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ospfv3_interface_policy_model**
> Ospfv3InterfacePolicyModelListContainer get_all_ospfv3_interface_policy_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of OSPF v3 process. Also, deletes, creates, or modifies the OSPFv3 Interface associated with the specified ID. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ospfv3_interface_policy_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ospfv3_interface_policy_model: %s\n" % e)
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

[**Ospfv3InterfacePolicyModelListContainer**](Ospfv3InterfacePolicyModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ospfv3_policy_model**
> Ospfv3PolicyModelListContainer get_all_ospfv3_policy_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of OSPF v3 process. Also, deletes, creates, or modifies the OSPF V3 associated with the specified ID. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_ospfv3_policy_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_ospfv3_policy_model: %s\n" % e)
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

[**Ospfv3PolicyModelListContainer**](Ospfv3PolicyModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_static_route_model**
> StaticRouteModelListContainer get_all_static_route_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of all Static routes (ipv4 and ipv6) associated with the specified device. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_static_route_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_static_route_model: %s\n" % e)
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

[**StaticRouteModelListContainer**](StaticRouteModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_virtual_router_model**
> VirtualRouterModelListContainer get_all_virtual_router_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of all virtual routers created in the specified device.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_virtual_router_model(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_virtual_router_model: %s\n" % e)
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

[**VirtualRouterModelListContainer**](VirtualRouterModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_virtual_switch**
> VirtualSwitchListContainer get_all_virtual_switch(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the virtual switch associated with the specified NGIPS device ID and virtual switch ID. If no virtual switch ID is specified, retrieves list of all virtual switches associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_virtual_switch(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_virtual_switch: %s\n" % e)
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

[**VirtualSwitchListContainer**](VirtualSwitchListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vrf_bgpi_pv_address_family_model**
> VrfBGPIPvAddressFamilyModelListContainer get_all_vrf_bgpi_pv_address_family_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of all BGP (ipv4 and ipv6) associated with the specified device for specified vrf.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vrf_bgpi_pv_address_family_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_vrf_bgpi_pv_address_family_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**VrfBGPIPvAddressFamilyModelListContainer**](VrfBGPIPvAddressFamilyModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vrf_i_pv4_static_route_model**
> VrfIPv4StaticRouteModelListContainer get_all_vrf_i_pv4_static_route_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified virtual router. Also, retrieves list of all IPv4 Static routes. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vrf_i_pv4_static_route_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_vrf_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**VrfIPv4StaticRouteModelListContainer**](VrfIPv4StaticRouteModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vrf_i_pv6_static_route_model**
> VrfIPv6StaticRouteModelListContainer get_all_vrf_i_pv6_static_route_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified virtual router. Also, retrieves list of all IPv6 Static routes. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vrf_i_pv6_static_route_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_vrf_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**VrfIPv6StaticRouteModelListContainer**](VrfIPv6StaticRouteModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vrf_ospf_interface_policy_model**
> VrfOspfInterfacePolicyModelListContainer get_all_vrf_ospf_interface_policy_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the OSPF Interface associated with the specified ID. Also, retrieves list of all OSPF v2 process. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vrf_ospf_interface_policy_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_vrf_ospf_interface_policy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**VrfOspfInterfacePolicyModelListContainer**](VrfOspfInterfacePolicyModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vrf_ospf_policy_model**
> VrfOspfPolicyModelListContainer get_all_vrf_ospf_policy_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves, deletes, creates, or modifies the OSPFV2 associated with the specified ID. Also, retrieves list of all OSPF v2 process. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vrf_ospf_policy_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_vrf_ospf_policy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**VrfOspfPolicyModelListContainer**](VrfOspfPolicyModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vrf_static_route_model**
> VrfStaticRouteModelListContainer get_all_vrf_static_route_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of all Static routes (ipv4 and ipv6) associated with the specified virtual router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_all_vrf_static_route_model(virtualrouter_uuid, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_all_vrf_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**VrfStaticRouteModelListContainer**](VrfStaticRouteModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_general_setting_model**
> BGPGeneralSettingModel get_bgp_general_setting_model(object_id, container_uuid, domain_uuid)



**Retrieves BGP general settings associated with the specified device.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a BGP general settings.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_bgp_general_setting_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_bgp_general_setting_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a BGP general settings. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**BGPGeneralSettingModel**](BGPGeneralSettingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgpi_pv_address_family_model**
> BGPIPvAddressFamilyModel get_bgpi_pv_address_family_model(object_id, container_uuid, domain_uuid)



**Retrieves list of all BGP (ipv4 and ipv6) associated with the specified device. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a BGP (ipv4 or ipv6) model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_bgpi_pv_address_family_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_bgpi_pv_address_family_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a BGP (ipv4 or ipv6) model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**BGPIPvAddressFamilyModel**](BGPIPvAddressFamilyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commands**
> CommandsListContainer get_commands(command, container_uuid, domain_uuid, parameters=parameters, offset=offset, limit=limit, expanded=expanded)



**Retrieves the show command output from the device. Make sure the minimum device version required for using commands api is >= 6.6.0.<br/> This api supports multi threading. Only 1 request can be handled per device concurrently and across devices upto 10 devices are supported by commands api concurrently.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
command = 'command_example' # str | The command filter query parameter should have value of show commands. The maximum word size of this field is 2. For eg: show interface, show running-config etc.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
parameters = 'parameters_example' # str | The parameters filter query parameter should have values containing command values exceeding word size of 2 should be given as part of parameters field. For eg: ip brief, vpn etc. (optional)
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_commands(command, container_uuid, domain_uuid, parameters=parameters, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**| The command filter query parameter should have value of show commands. The maximum word size of this field is 2. For eg: show interface, show running-config etc. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **parameters** | **str**| The parameters filter query parameter should have values containing command values exceeding word size of 2 should be given as part of parameters field. For eg: ip brief, vpn etc. | [optional] 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**CommandsListContainer**](CommandsListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> Device get_device(object_id, domain_uuid)



**Retrieves or modifies the device record associated with the specified ID. Registers or unregisters a device. If no ID is specified for a GET, retrieves list of all device records.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Identifier for a device.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_device(object_id, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for a device. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fp_interface_statistics**
> FPInterfaceStatisticsListContainer get_fp_interface_statistics(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of statistics for all interfaces associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_fp_interface_statistics(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_fp_interface_statistics: %s\n" % e)
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

[**FPInterfaceStatisticsListContainer**](FPInterfaceStatisticsListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fp_logical_interface**
> FPLogicalInterface get_fp_logical_interface(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the logical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all logical interfaces associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a logical interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_fp_logical_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_fp_logical_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a logical interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FPLogicalInterface**](FPLogicalInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fp_physical_interface**
> FPPhysicalInterface get_fp_physical_interface(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the physical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all physical interfaces associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a physical interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_fp_physical_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_fp_physical_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a physical interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FPPhysicalInterface**](FPPhysicalInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_bridge_group_interface**
> FTDBridgeGroupInterface get_ftd_bridge_group_interface(object_id, container_uuid, domain_uuid)



**Retrieves the bridge group interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all bridge group interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a bridge group interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftd_bridge_group_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ftd_bridge_group_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a bridge group interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDBridgeGroupInterface**](FTDBridgeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_ether_channel_interface**
> FTDEtherChannelInterface get_ftd_ether_channel_interface(object_id, container_uuid, domain_uuid)



**Retrieves the ethernet channel interface associated with the specified NGFW device ID and interface ID. If no ID is specified, retrieves list of all ethernet channel interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a ethernet channel interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftd_ether_channel_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ftd_ether_channel_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a ethernet channel interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDEtherChannelInterface**](FTDEtherChannelInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_physical_interface**
> FTDPhysicalInterface get_ftd_physical_interface(object_id, container_uuid, domain_uuid)



**Retrieves the physical interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all physical interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a NGFW physical interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftd_physical_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ftd_physical_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a NGFW physical interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDPhysicalInterface**](FTDPhysicalInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_redundant_interface**
> FTDRedundantInterface get_ftd_redundant_interface(object_id, container_uuid, domain_uuid)



**Retrieves the redundant interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all redundant interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a redundant interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftd_redundant_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ftd_redundant_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a redundant interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDRedundantInterface**](FTDRedundantInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_sub_interface**
> FTDSubInterface get_ftd_sub_interface(object_id, container_uuid, domain_uuid)



**Retrieves the sub-interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all sub-interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a sub-interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftd_sub_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ftd_sub_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a sub-interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDSubInterface**](FTDSubInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftd_vlan_interface**
> FTDVlanInterface get_ftd_vlan_interface(object_id, container_uuid, domain_uuid)



**Retrieves the vlan interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all vlan interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a NGFW vlan interface.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ftd_vlan_interface(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ftd_vlan_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a NGFW vlan interface. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDVlanInterface**](FTDVlanInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_monitor_model**
> HealthMonitorModelListContainer get_health_monitor_model(filter, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves HealthMonitor metrics for the device.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
filter = 'filter_example' # str | The metric filter query parameter should have healthmonitor name.Currently supports only <code>metric:memory & metric:cpu</code>
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_health_monitor_model(filter, container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_health_monitor_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The metric filter query parameter should have healthmonitor name.Currently supports only &lt;code&gt;metric:memory &amp; metric:cpu&lt;/code&gt; | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 
 **offset** | **int**| Index of first item to return. | [optional] 
 **limit** | **int**| Number of items to return. | [optional] 
 **expanded** | **bool**| If set to true, the GET response displays a list of objects with additional attributes. | [optional] 

### Return type

[**HealthMonitorModelListContainer**](HealthMonitorModelListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_i_pv4_static_route_model**
> IPv4StaticRouteModel get_i_pv4_static_route_model(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified ID. Also, retrieves list of all IPv4 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv4 Static Route.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_i_pv4_static_route_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv4 Static Route. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**IPv4StaticRouteModel**](IPv4StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_i_pv6_static_route_model**
> IPv6StaticRouteModel get_i_pv6_static_route_model(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified ID. Also, retrieves list of all IPv6 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv6 Static Route.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_i_pv6_static_route_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv6 Static Route. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**IPv6StaticRouteModel**](IPv6StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inline_set**
> InlineSet get_inline_set(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the inline set associated with the specified NGIPS device ID and inline set ID. If no inline set ID is specified, retrieves list of all inline sets associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of an inline set.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_inline_set(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_inline_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an inline set. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**InlineSet**](InlineSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interface_event**
> InterfaceEventListContainer get_interface_event(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)



**Retrieves list of all netmod events on the device.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID
offset = 56 # int | Index of first item to return. (optional)
limit = 56 # int | Number of items to return. (optional)
expanded = true # bool | If set to true, the GET response displays a list of objects with additional attributes. (optional)

try:
    api_response = api_instance.get_interface_event(container_uuid, domain_uuid, offset=offset, limit=limit, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_interface_event: %s\n" % e)
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

[**InterfaceEventListContainer**](InterfaceEventListContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ospf_interface_policy_model**
> OspfInterfacePolicyModel get_ospf_interface_policy_model(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the OSPF Interface associated with the specified ID. Also, retrieves list of all OSPF v2 process. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a OSPF Interface Policy.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ospf_interface_policy_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ospf_interface_policy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a OSPF Interface Policy. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**OspfInterfacePolicyModel**](OspfInterfacePolicyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ospf_policy_model**
> OspfPolicyModel get_ospf_policy_model(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the OSPF V2 associated with the specified ID. Also, retrieves list of all OSPF v2 process. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a OSPF Policy.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ospf_policy_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ospf_policy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a OSPF Policy. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**OspfPolicyModel**](OspfPolicyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ospfv3_interface_policy_model**
> Ospfv3InterfacePolicyModel get_ospfv3_interface_policy_model(object_id, container_uuid, domain_uuid)



**Retrieves list of OSPF v3 process. Also, deletes, creates, or modifies the OSPFv3 Interface associated with the specified ID. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a OSPFv3 Interface Policy.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ospfv3_interface_policy_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ospfv3_interface_policy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a OSPFv3 Interface Policy. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**Ospfv3InterfacePolicyModel**](Ospfv3InterfacePolicyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ospfv3_policy_model**
> Ospfv3PolicyModel get_ospfv3_policy_model(object_id, container_uuid, domain_uuid)



**Retrieves list of OSPF v3 process. Also, deletes, creates, or modifies the OSPF V3 associated with the specified ID. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a OSPFv3 Policy.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_ospfv3_policy_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_ospfv3_policy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a OSPFv3 Policy. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**Ospfv3PolicyModel**](Ospfv3PolicyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_static_route_model**
> StaticRouteModel get_static_route_model(object_id, container_uuid, domain_uuid)



**Retrieves list of all Static routes (ipv4 and ipv6) associated with the specified device. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a Static Route
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_static_route_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a Static Route | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**StaticRouteModel**](StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_router_model**
> VirtualRouterModel get_virtual_router_model(object_id, container_uuid, domain_uuid)



**Retrieves list of all virtual routers created in the specified device.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_virtual_router_model(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_virtual_router_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VirtualRouterModel**](VirtualRouterModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_switch**
> VirtualSwitch get_virtual_switch(object_id, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the virtual switch associated with the specified NGIPS device ID and virtual switch ID. If no virtual switch ID is specified, retrieves list of all virtual switches associated with the specified NGIPS device ID.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a virtual switch.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_virtual_switch(object_id, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_virtual_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a virtual switch. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VirtualSwitch**](VirtualSwitch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vrf_bgpi_pv_address_family_model**
> VrfBGPIPvAddressFamilyModel get_vrf_bgpi_pv_address_family_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves list of all BGP (ipv4 and ipv6) associated with the specified device for specified vrf.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a BGP general settings.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vrf_bgpi_pv_address_family_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_vrf_bgpi_pv_address_family_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a BGP general settings. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfBGPIPvAddressFamilyModel**](VrfBGPIPvAddressFamilyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vrf_i_pv4_static_route_model**
> VrfIPv4StaticRouteModel get_vrf_i_pv4_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified virtual router. Also, retrieves list of all IPv4 Static routes. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv4 Static Route.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vrf_i_pv4_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_vrf_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv4 Static Route. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfIPv4StaticRouteModel**](VrfIPv4StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vrf_i_pv6_static_route_model**
> VrfIPv6StaticRouteModel get_vrf_i_pv6_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified virtual router. Also, retrieves list of all IPv6 Static routes. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv6 Static Route.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vrf_i_pv6_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_vrf_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv6 Static Route. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfIPv6StaticRouteModel**](VrfIPv6StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vrf_ospf_interface_policy_model**
> VrfOspfInterfacePolicyModel get_vrf_ospf_interface_policy_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the OSPF Interface associated with the specified ID. Also, retrieves list of all OSPF v2 process. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a OSPF Interface Policy.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vrf_ospf_interface_policy_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_vrf_ospf_interface_policy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a OSPF Interface Policy. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfOspfInterfacePolicyModel**](VrfOspfInterfacePolicyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vrf_ospf_policy_model**
> VrfOspfPolicyModel get_vrf_ospf_policy_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the OSPFV2 associated with the specified ID. Also, retrieves list of all OSPF v2 process. **

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a OSPF Policy.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vrf_ospf_policy_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_vrf_ospf_policy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a OSPF Policy. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfOspfPolicyModel**](VrfOspfPolicyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vrf_static_route_model**
> VrfStaticRouteModel get_vrf_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves list of all Static routes (ipv4 and ipv6) associated with the specified virtual router.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a Static Route
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.get_vrf_static_route_model(object_id, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_vrf_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a Static Route | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfStaticRouteModel**](VrfStaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> Device update_device(object_id, body, domain_uuid)



**Retrieves or modifies the device record associated with the specified ID. Registers or unregisters a device. If no ID is specified for a GET, retrieves list of all device records. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Identifier for a device.
body = swagger_client.Device() # Device | Input representation of device.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_device(object_id, body, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Identifier for a device. | 
 **body** | [**Device**](Device.md)| Input representation of device. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fp_logical_interface**
> FPLogicalInterface update_fp_logical_interface(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the logical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all logical interfaces associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a logical interface.
body = swagger_client.FPLogicalInterface() # FPLogicalInterface | The input logical interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_fp_logical_interface(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_fp_logical_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a logical interface. | 
 **body** | [**FPLogicalInterface**](FPLogicalInterface.md)| The input logical interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FPLogicalInterface**](FPLogicalInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fp_physical_interface**
> FPPhysicalInterface update_fp_physical_interface(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the physical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all physical interfaces associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a physical interface.
body = swagger_client.FPPhysicalInterface() # FPPhysicalInterface | The input physical interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_fp_physical_interface(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_fp_physical_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a physical interface. | 
 **body** | [**FPPhysicalInterface**](FPPhysicalInterface.md)| The input physical interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FPPhysicalInterface**](FPPhysicalInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_bridge_group_interface**
> FTDBridgeGroupInterface update_ftd_bridge_group_interface(object_id, body, container_uuid, domain_uuid)



**Retrieves the bridge group interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all bridge group interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a bridge group interface.
body = swagger_client.FTDBridgeGroupInterface() # FTDBridgeGroupInterface | The input bridge group interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftd_bridge_group_interface(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_ftd_bridge_group_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a bridge group interface. | 
 **body** | [**FTDBridgeGroupInterface**](FTDBridgeGroupInterface.md)| The input bridge group interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDBridgeGroupInterface**](FTDBridgeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_ether_channel_interface**
> FTDEtherChannelInterface update_ftd_ether_channel_interface(object_id, body, container_uuid, domain_uuid)



**Retrieves the ethernet channel interface associated with the specified NGFW device ID and interface ID. If no ID is specified, retrieves list of all ethernet channel interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a ethernet channel interface.
body = swagger_client.FTDEtherChannelInterface() # FTDEtherChannelInterface | The input ethernet channel interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftd_ether_channel_interface(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_ftd_ether_channel_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a ethernet channel interface. | 
 **body** | [**FTDEtherChannelInterface**](FTDEtherChannelInterface.md)| The input ethernet channel interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDEtherChannelInterface**](FTDEtherChannelInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_physical_interface**
> FTDPhysicalInterface update_ftd_physical_interface(object_id, body, container_uuid, domain_uuid)



**Retrieves the physical interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all physical interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a NGFW physical interface.
body = swagger_client.FTDPhysicalInterface() # FTDPhysicalInterface | The input NGFW physical interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftd_physical_interface(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_ftd_physical_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a NGFW physical interface. | 
 **body** | [**FTDPhysicalInterface**](FTDPhysicalInterface.md)| The input NGFW physical interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDPhysicalInterface**](FTDPhysicalInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_redundant_interface**
> FTDRedundantInterface update_ftd_redundant_interface(object_id, body, container_uuid, domain_uuid)



**Retrieves the redundant interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all redundant interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a redundant interface.
body = swagger_client.FTDRedundantInterface() # FTDRedundantInterface | The input redundant interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftd_redundant_interface(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_ftd_redundant_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a redundant interface. | 
 **body** | [**FTDRedundantInterface**](FTDRedundantInterface.md)| The input redundant interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDRedundantInterface**](FTDRedundantInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_sub_interface**
> FTDSubInterface update_ftd_sub_interface(object_id, body, container_uuid, domain_uuid)



**Retrieves the sub-interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all sub-interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a sub-interface.
body = swagger_client.FTDSubInterface() # FTDSubInterface | The input sub-interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftd_sub_interface(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_ftd_sub_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a sub-interface. | 
 **body** | [**FTDSubInterface**](FTDSubInterface.md)| The input sub-interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDSubInterface**](FTDSubInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftd_vlan_interface**
> FTDVlanInterface update_ftd_vlan_interface(object_id, body, container_uuid, domain_uuid)



**Retrieves the vlan interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all vlan interfaces associated with the specified NGFW device ID. <div class=\"alert alert-warning\">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div> _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a NGFW vlan interface.
body = swagger_client.FTDVlanInterface() # FTDVlanInterface | The input NGFW vlan interface model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_ftd_vlan_interface(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_ftd_vlan_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a NGFW vlan interface. | 
 **body** | [**FTDVlanInterface**](FTDVlanInterface.md)| The input NGFW vlan interface model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**FTDVlanInterface**](FTDVlanInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_i_pv4_static_route_model**
> IPv4StaticRouteModel update_i_pv4_static_route_model(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified ID. Also, retrieves list of all IPv4 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv4 Static Route.
body = swagger_client.IPv4StaticRouteModel() # IPv4StaticRouteModel | The input IPv4 Static Route model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_i_pv4_static_route_model(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv4 Static Route. | 
 **body** | [**IPv4StaticRouteModel**](IPv4StaticRouteModel.md)| The input IPv4 Static Route model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**IPv4StaticRouteModel**](IPv4StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_i_pv6_static_route_model**
> IPv6StaticRouteModel update_i_pv6_static_route_model(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified ID. Also, retrieves list of all IPv6 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv6 Static Route.
body = swagger_client.IPv6StaticRouteModel() # IPv6StaticRouteModel | The input IPv6 Static Route model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_i_pv6_static_route_model(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv6 Static Route. | 
 **body** | [**IPv6StaticRouteModel**](IPv6StaticRouteModel.md)| The input IPv6 Static Route model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**IPv6StaticRouteModel**](IPv6StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inline_set**
> InlineSet update_inline_set(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the inline set associated with the specified NGIPS device ID and inline set ID. If no inline set ID is specified, retrieves list of all inline sets associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of an inline set.
body = swagger_client.InlineSet() # InlineSet | The input inline set model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_inline_set(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_inline_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of an inline set. | 
 **body** | [**InlineSet**](InlineSet.md)| The input inline set model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**InlineSet**](InlineSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_router_model**
> VirtualRouterModel update_virtual_router_model(object_id, body, container_uuid, domain_uuid)



**Retrieves list of all virtual routers created in the specified device. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a Virtual Router
body = swagger_client.VirtualRouterModel() # VirtualRouterModel | The input Virtual Router Model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_virtual_router_model(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_virtual_router_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a Virtual Router | 
 **body** | [**VirtualRouterModel**](VirtualRouterModel.md)| The input Virtual Router Model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VirtualRouterModel**](VirtualRouterModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_switch**
> VirtualSwitch update_virtual_switch(object_id, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the virtual switch associated with the specified NGIPS device ID and virtual switch ID. If no virtual switch ID is specified, retrieves list of all virtual switches associated with the specified NGIPS device ID. _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a virtual switch.
body = swagger_client.VirtualSwitch() # VirtualSwitch | The input virtual switch model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_virtual_switch(object_id, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_virtual_switch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a virtual switch. | 
 **body** | [**VirtualSwitch**](VirtualSwitch.md)| The input virtual switch model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VirtualSwitch**](VirtualSwitch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vrf_i_pv4_static_route_model**
> VrfIPv4StaticRouteModel update_vrf_i_pv4_static_route_model(object_id, virtualrouter_uuid, body, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified virtual router. Also, retrieves list of all IPv4 Static routes.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv4 Static Route.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
body = swagger_client.VrfIPv4StaticRouteModel() # VrfIPv4StaticRouteModel | The input IPv4 Static Route model.
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_vrf_i_pv4_static_route_model(object_id, virtualrouter_uuid, body, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_vrf_i_pv4_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv4 Static Route. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **body** | [**VrfIPv4StaticRouteModel**](VrfIPv4StaticRouteModel.md)| The input IPv4 Static Route model. | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfIPv4StaticRouteModel**](VrfIPv4StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vrf_i_pv6_static_route_model**
> VrfIPv6StaticRouteModel update_vrf_i_pv6_static_route_model(object_id, body, virtualrouter_uuid, container_uuid, domain_uuid)



**Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified virtual router. Also, retrieves list of all IPv6 Static routes.  _Check the response section for applicable examples (if any)._**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
object_id = 'object_id_example' # str | Unique identifier of a IPv6 Static Route.
body = swagger_client.VrfIPv6StaticRouteModel() # VrfIPv6StaticRouteModel | The input IPv6 Static Route model.
virtualrouter_uuid = 'virtualrouter_uuid_example' # str | Unique identifier of Virtual Router
container_uuid = 'container_uuid_example' # str | The container id under which this specific resource is contained.
domain_uuid = 'domain_uuid_example' # str | Domain UUID

try:
    api_response = api_instance.update_vrf_i_pv6_static_route_model(object_id, body, virtualrouter_uuid, container_uuid, domain_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_vrf_i_pv6_static_route_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Unique identifier of a IPv6 Static Route. | 
 **body** | [**VrfIPv6StaticRouteModel**](VrfIPv6StaticRouteModel.md)| The input IPv6 Static Route model. | 
 **virtualrouter_uuid** | **str**| Unique identifier of Virtual Router | 
 **container_uuid** | **str**| The container id under which this specific resource is contained. | 
 **domain_uuid** | **str**| Domain UUID | 

### Return type

[**VrfIPv6StaticRouteModel**](VrfIPv6StaticRouteModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

