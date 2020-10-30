# PolicyList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standard_access_list_route_sources** | [**list[IReference]**](IReference.md) | Routes that have been advertised by routers and access servers at the address specified by the access lists. | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**ipv4_prefix_list_route_sources** | [**list[IReference]**](IReference.md) | Routes that have been advertised by routers and access servers at the address specified by the prefix lists. | [optional] 
**interfaces** | [**list[IReference]**](IReference.md) | Add the Security zones/Interface groups that contain the interfaces through which the device communicates with the management station | [optional] 
**standard_access_list_next_hops** | [**list[IReference]**](IReference.md) | A next hop router address passed by one of the access lists specified. (standardAccessListNextHops and ipv4PrefixListAddresses are mutually exclusive) | [optional] 
**description** | **str** |  | [optional] 
**overrides** | [**IOverride**](IOverride.md) |  | [optional] 
**type** | **str** | PolicyList - type of this object | [optional] 
**interface_names** | **list[str]** | Interface logical names associated with this object | [optional] 
**ipv4_prefix_list_addresses** | [**list[IReference]**](IReference.md) | A destination address that is permitted by a prefix list (standardAccessListAddresses and ipv4PrefixListAddresses are mutually exclusive) | [optional] 
**version** | **str** |  | [optional] 
**standard_access_list_addresses** | [**list[IReference]**](IReference.md) | A destination address that is permitted by a standard access list (standardAccessListAddresses and ipv4PrefixListAddresses are mutually exclusive) | [optional] 
**match_community_exactly** | **bool** | Match the BGP community exactly with the specified community | [optional] 
**community_lists** | [**list[IReference]**](IReference.md) | The route can match either community | [optional] 
**metric** | **int** | This setting allows you to match any routes that have a specified metric. The metric values can range from 0 to 4294967295. | [optional] 
**ipv4_prefix_list_nexthops** | [**list[IReference]**](IReference.md) | A next hop router address passed by one of the prefix lists specified.(standardAccessListNextHops and ipv4PrefixListAddresses are mutually exclusive) | [optional] 
**name** | **str** | Name for the policy list object | 
**overridable** | **bool** |  | [optional] 
**action** | **str** | Action to take for this matching criteria: PERMIT or DENY | 
**links** | [**Links**](Links.md) |  | [optional] 
**as_path_lists** | [**list[IReference]**](IReference.md) | BGP autonomous system path for matching criteria. | [optional] 
**tag** | **int** | This setting allows you to match any routes that have a specified security group tag. The tag values can range from 0 to 4294967295 | [optional] 
**id** | **str** | unique object identifier | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


