# IRouteMapEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_prefix_list_route_sources** | [**list[IReference]**](IReference.md) | Match IPv4 (routes/traffic) based on the advertising source address of the route.  | [optional] 
**metric_bandwidth** | **int** | Metric value or bandwidth in Kbits per second | [optional] 
**policy_lists** | [**list[IReference]**](IReference.md) | Configure a route map to evaluate and process a BGP policy. | [optional] 
**ipv6_access_list_route_sources** | [**list[IReference]**](IReference.md) | Match IPv6 (routes/traffic) based on the advertising source address of route. | [optional] 
**ipv6_access_list_addresses** | [**list[IReference]**](IReference.md) | Match IPv6 (routes/traffic) based on the route address. | [optional] 
**ipv4_access_list_addresses** | [**list[IReference]**](IReference.md) | Match IPv4 (routes/traffic) based on the route address. | [optional] 
**route_type_nssa_external1** | **bool** | Enable NSSA-External1 route type | [optional] 
**route_type_nssa_external2** | **bool** | Enable NSSA-External2 route type | [optional] 
**ipv6_prefix_list_nexthops** | [**list[IReference]**](IReference.md) | Match IPv6 (routes/traffic) based on the next-hop address. | [optional] 
**next_hop_ipv4_setting** | **str** | Specify a next hop IPv4 address of the next hop to which packets are output. | [optional] 
**metric_type** | **str** | Valid values are : internal, type-1, or type-2. | [optional] 
**next_hop_ipv6_setting** | **str** | Specify a next hop IPv6 address of the next hop to which packets are output. | [optional] 
**ipv4_access_list_next_hops** | [**list[IReference]**](IReference.md) | Match IPv4 (routes/traffic) based on the next-hop address. | [optional] 
**ipv4_prefix_list_nexthops** | [**list[IReference]**](IReference.md) | Match IPv4 (routes/traffic) based on the next-hop address. | [optional] 
**action** | **str** | Indicate the redistribution access: PERMIT or DENY | 
**as_path_lists** | [**list[IReference]**](IReference.md) | Enable matching the BGP autonomous system path access list with the specified path access list. | [optional] 
**tag_values** | **list[int]** | This setting allows you to match any routes that have a specified security group tag. | [optional] 
**community_list_setting_internet** | **bool** | Internet: one of the well-known communities | [optional] 
**community_list_setting** | **int** | Enable matching the BGP community with the specified community. | [optional] 
**ipv6_access_list_next_hops** | [**list[IReference]**](IReference.md) | Match IPv6 (routes/traffic) based on the next-hop address. | [optional] 
**interfaces** | [**list[IReference]**](IReference.md) | Match traffic based on the (ingress/egress) interfaces. Input security Zones. | [optional] 
**specific_i_ps_ipv6_setting** | **list[str]** |  | [optional] 
**origin_setting** | **str** | BGP origin code. Valid values are Local IGP Local IGP and Incomplete. | [optional] 
**community_list_setting_no_export** | **bool** | No-Export: One of the well-known communities | [optional] 
**local_preference_setting** | **int** | Preference value for the autonomous system path | [optional] 
**interface_names** | **list[str]** | Match traffic based on the (ingress/egress) interfaces. Logical names. | [optional] 
**automatic_tag_setting** | **bool** | Automatically compute the tag value. | [optional] 
**ipv4_prefix_list_addresses** | [**list[IReference]**](IReference.md) | Match IPv4 (routes/traffic) based on the route address. | [optional] 
**as_path_prepend_last_as_to_as_path** | **int** | Prepend the AS path with the last AS number. | [optional] 
**ipv6_prefix_list_route_sources** | [**list[IReference]**](IReference.md) | Match IPv6 (routes/traffic) based on the advertising source address of route. | [optional] 
**ipv6_prefix_list_addresses** | [**list[IReference]**](IReference.md) | Match IPv6 (routes/traffic) based on the route address. | [optional] 
**prefix_list_ipv6_setting** | [**IReference**](IReference.md) | Match IPv6 (routes/traffic) based on the route address. | [optional] 
**prefix_list_ipv4_setting** | [**IReference**](IReference.md) | Match IPv4 (routes/traffic) based on the route address. | [optional] 
**sequence** | **int** | Indicates the position a new route map entry will have in the list of route maps entries already configured for this route map object | 
**route_type_external2** | **bool** | Enable External2 route type | [optional] 
**metric_route_values** | **list[int]** | Enable matching the metric of a route | [optional] 
**route_type_external1** | **bool** | Enable External1 route type | [optional] 
**community_list_setting_no_advertise** | **bool** | No Advertise: one of the well-known communities | [optional] 
**community_lists** | [**list[IReference]**](IReference.md) | Enable matching the BGP community with the specified community. | [optional] 
**specific_i_ps_ipv4_setting** | **list[str]** |  | [optional] 
**as_path_prepend_as_path** | **list[int]** | Prepend an arbitrary autonomous system path string to BGP routes. | [optional] 
**ipv4_access_list_route_sources** | [**list[IReference]**](IReference.md) | Match IPv4 (routes/traffic) based on the advertising source address of the route.  | [optional] 
**weight_setting** | **int** | BGP weight for the routing table | [optional] 
**route_type_local** | **bool** | Enable Local route type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


