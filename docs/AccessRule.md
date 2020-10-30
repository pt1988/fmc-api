# AccessRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**AccessRuleMetadata**](AccessRuleMetadata.md) | Object representing metadata attributes for the access rule. | [optional] 
**snmp_config** | [**ISNMPConfig**](ISNMPConfig.md) | Object representing the SNMP alert associated with the access rule. | [optional] 
**time_range_objects** | [**list[ITimeRangeModel]**](ITimeRangeModel.md) |  | [optional] 
**source_networks** | [**INetworkObjectsContainer**](INetworkObjectsContainer.md) | Object representing source networks selected for the access rule. | [optional] 
**syslog_severity** | **str** | Specifies the Override Severity if alerts are being sent to default syslog configuration. One of: ALERT | CRIT | DEBUG | EMERG | ERR | INFO | NOTICE | WARNING. | [optional] 
**source_zones** | [**ISourceZoneContainer**](ISourceZoneContainer.md) | Object representing source zones selected for the access rule. | [optional] 
**destination_zones** | [**ISecurityZoneContainer**](ISecurityZoneContainer.md) | Object representing destination zones selected for the access rule. | [optional] 
**description** | **str** | User provided resource description.  | [optional] 
**original_source_networks** | [**INetworkObjectsContainer**](INetworkObjectsContainer.md) |  | [optional] 
**type** | **str** | Type of the response object. This value is always AccessRule. | [optional] 
**enable_syslog** | **bool** | Boolean indicating whether the alerts associated with the access rule are sent to default syslog configuration in Access Control Logging. | [optional] 
**safe_search** | [**ISafeSearch**](ISafeSearch.md) | Object representing the SafeSearch attribute (specified on the Applications tab of the Editing Rule dialog). | [optional] 
**enabled** | **bool** | Boolean indicating whether the access rule is in effect (true) or not (false). Default is true. | [optional] 
**dest_sgt_types** | **list[str]** |  | [optional] 
**syslog_config** | [**ISyslogConfig**](ISyslogConfig.md) | Object representing the syslog alert associated with the access rule. | [optional] 
**urls** | [**IUrlObjectsContainer**](IUrlObjectsContainer.md) | Object representing the URLs and categories selected for the rule. | [optional] 
**end_point_device_types** | [**list[IEndPointDeviceType]**](IEndPointDeviceType.md) | Object representing the Endpoint Device Types (specified on the SGT/ISE Attributes tab of the Editing Rule dialog). | [optional] 
**you_tube** | [**IYouTube**](IYouTube.md) | Object representing the YouTubeEDU attribute (specified on the Applications tab of the Editing Rule dialog). | [optional] 
**destination_networks** | [**INetworkObjectsContainer**](INetworkObjectsContainer.md) | Object representing destination networks selected for the access rule. | [optional] 
**action** | **str** | Specifies the action to take when the conditions defined by the rule are met. One of: BLOCK | TRUST | NETWORK_DISCOVERY | PERMIT. | 
**links** | [**ILinks**](ILinks.md) | Object containing links to this resource. | [optional] 
**network_access_device_i_ps** | [**INetworkObjectsContainer**](INetworkObjectsContainer.md) | Object representing the Network Access Device IPs (specified on the SGT/ISE Attributes tab of the Editing Rule dialog). | [optional] 
**id** | **str** | Unique identifier (UUID) for the access rule. | [optional] 
**source_security_group_tags** | [**ISecurityGroupTagContainer**](ISecurityGroupTagContainer.md) | Object representing the Security Group Tag (specified on the SGT/ISE Attributes tab of the Editing Rule dialog). | [optional] 
**destination_security_group_tags** | [**ISecurityGroupTagContainer**](ISecurityGroupTagContainer.md) |  | [optional] 
**log_end** | **bool** | Boolean indicating whether the device will log events at the end of the connection. Default is false. If &#39;MONITOR&#39; action is selected for access rule, logEnd will always be true. | [optional] 
**log_begin** | **bool** | Boolean indicating whether the device will log events at the beginning of the connection. Default is false. If &#39;MONITOR&#39; action is selected for access rule, logBegin will always be false. | [optional] 
**send_events_to_fmc** | **bool** | Boolean indicating whether the device will send events to the Firepower Management Center event viewer. Default is false. If &#39;MONITOR&#39; action is selected for access rule, sendEventsToFMC will always be true. | [optional] 
**destination_ports** | [**IPortObjectsContainer**](IPortObjectsContainer.md) | Object representing destination ports selected for the rule. | [optional] 
**source_ports** | [**IPortObjectsContainer**](IPortObjectsContainer.md) | Object representing source ports selected for the rule. | [optional] 
**ips_policy** | [**IIntrusionPolicyModel**](IIntrusionPolicyModel.md) | Object representing the intrusion policy settings for the rule action (specified on the Inspection tab). For more information on intrusion policies, see \&quot;Access Control Using Intrusion and File Policies\&quot; in the Firepower Management Center Configuration Guide. | [optional] 
**version** | **str** | Version number of the response object. | [optional] 
**variable_set** | [**IVariableSet**](IVariableSet.md) | Object representing the variable set associated with the access rule. | [optional] 
**users** | [**IUsersContainer**](IUsersContainer.md) | Object representing users selected for the rule.  | [optional] 
**log_files** | **bool** | Boolean indicating whether the device will log file events. Default is false. | [optional] 
**file_policy** | [**IFilePolicy**](IFilePolicy.md) | Object representing the file policy settings for the rule action. | [optional] 
**comment_history_list** | [**list[ICommentHistory]**](ICommentHistory.md) | List of comments in the access rule&#39;s comment history. | [optional] 
**name** | **str** | User-specified name of the access rule. | [optional] 
**vlan_tags** | [**IVLanTagsContainer**](IVLanTagsContainer.md) | Object representing the VLAN tag set associated with the access rule. | [optional] 
**applications** | [**IApplicationsContainer**](IApplicationsContainer.md) | Object representing applications selected in the content restriction settings (on the Applications tab of the Editing Rule dialog). This includes the Safe Search and YouTube EDU services. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


