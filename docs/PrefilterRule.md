# PrefilterRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Object representing metadata attributes for the prefilter rule. | [optional] 
**bidirectional** | **bool** | Boolean indicating whether the rule is bidirectional. | [optional] 
**source_interfaces** | [**ISecurityZoneContainer**](ISecurityZoneContainer.md) | Object representing source interfaces for prefilter rule. | [optional] 
**snmp_config** | [**ISNMPConfig**](ISNMPConfig.md) | Object representing the SNMP alert associated with the prefilter rule. | [optional] 
**encapsulation_ports** | **list[str]** | Object representing the encapsulation ports to be used in prefilter rule. | [optional] 
**time_range_objects** | [**list[ITimeRangeModel]**](ITimeRangeModel.md) |  | [optional] 
**source_networks** | [**INetworkObjectsContainer**](INetworkObjectsContainer.md) | Object representing source networks selected for the prefilter rule. | [optional] 
**syslog_severity** | **str** | Specifies the Override Severity if alerts are being sent to default syslog configuration. One of: ALERT | CRIT | DEBUG | EMERG | ERR | INFO | NOTICE | WARNING. | [optional] 
**destination_interfaces** | [**ISecurityZoneContainer**](ISecurityZoneContainer.md) | Object representing destination interfaces for prefilter rule. | [optional] 
**tunnel_zone** | [**ISourceZoneContainer**](ISourceZoneContainer.md) | Object Representing tunnel zones for prefilter rule. | [optional] 
**type** | **str** | Type must be PrefilterRule. | [optional] 
**enable_syslog** | **bool** | Boolean indicating whether the alerts associated with the prefilter rule are sent to default syslog configuration in Prefilter Logging. | [optional] 
**enabled** | **bool** | Boolean indicating whether the prefilter rule is in effect (true) or not (false). Default is true. | [optional] 
**syslog_config** | [**ISyslogConfig**](ISyslogConfig.md) | Object representing the syslog alert associated with the prefilter rule. | [optional] 
**rule_type** | **str** | Object indicating if the Rule is Prefilter Rule or Tunnel Rule. | 
**destination_networks** | [**INetworkObjectsContainer**](INetworkObjectsContainer.md) | Object representing destination networks selected for the prefilter rule. | [optional] 
**action** | **str** | Specifies the action to take when the conditions defined by the rule are met. One of: BLOCK | TRUST | NETWORK_DISCOVERY | PERMIT. | 
**links** | [**ILinks**](ILinks.md) | Object containing links to this resource. | [optional] 
**id** | **str** | Unique identifier (UUID) for the prefilter rule. | [optional] 
**log_end** | **bool** | Boolean indicating whether the device will log events at the end of the connection. Default is false. | [optional] 
**log_begin** | **bool** | Boolean indicating whether the device will log events at the beginning of the connection. Default is false. | [optional] 
**send_events_to_fmc** | **bool** | Boolean indicating whether the device will send events to the Firepower Management Center event viewer. Default is false. | [optional] 
**destination_ports** | [**IPortObjectsContainer**](IPortObjectsContainer.md) | Object representing destination ports selected for the rule. | [optional] 
**source_ports** | [**IPortObjectsContainer**](IPortObjectsContainer.md) | Object representing source ports selected for the rule. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**new_comments** | **list[str]** | Object representing the new comments provided in prefilter rule. | [optional] 
**comment_history_list** | [**list[ICommentHistory]**](ICommentHistory.md) | List of comments in the prefilter rule&#39;s comment history. | [optional] 
**name** | **str** | User-specified name of the prefilter rule. | [optional] 
**vlan_tags** | [**IVLanTagsContainer**](IVLanTagsContainer.md) | Object representing the VLAN tag set associated with the prefilter rule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


