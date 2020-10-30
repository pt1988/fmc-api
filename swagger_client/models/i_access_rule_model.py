# coding: utf-8

"""
    Cisco Firepower Management Center Open API Specification

    **Specifies the REST URLs and methods supported in the Cisco Firepower Management Center API. Refer to the version specific [REST API Quick Start Guide](https://www.cisco.com/c/en/us/support/security/defense-center/products-programming-reference-guides-list.html) for additional information.**  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: tac@cisco.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IAccessRuleModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'metadata': 'IMetadata',
        'snmp_config': 'ISNMPConfig',
        'source_networks': 'INetworkObjectsContainer',
        'syslog_severity': 'str',
        'time_range_objects': 'list[ITimeRangeModel]',
        'source_zones': 'ISourceZoneContainer',
        'destination_zones': 'ISecurityZoneContainer',
        'description': 'str',
        'original_source_networks': 'INetworkObjectsContainer',
        'enable_syslog': 'bool',
        'type': 'str',
        'safe_search': 'ISafeSearch',
        'enabled': 'bool',
        'syslog_config': 'ISyslogConfig',
        'urls': 'IUrlObjectsContainer',
        'end_point_device_types': 'list[IEndPointDeviceType]',
        'you_tube': 'IYouTube',
        'destination_networks': 'INetworkObjectsContainer',
        'action': 'str',
        'network_access_device_i_ps': 'INetworkObjectsContainer',
        'links': 'ILinks',
        'id': 'str',
        'source_security_group_tags': 'ISecurityGroupTagContainer',
        'destination_security_group_tags': 'ISecurityGroupTagContainer',
        'log_end': 'bool',
        'log_begin': 'bool',
        'send_events_to_fmc': 'bool',
        'destination_ports': 'IPortObjectsContainer',
        'source_ports': 'IPortObjectsContainer',
        'ips_policy': 'IIntrusionPolicyModel',
        'variable_set': 'IVariableSet',
        'version': 'str',
        'users': 'IUsersContainer',
        'log_files': 'bool',
        'new_comments': 'list[str]',
        'file_policy': 'IFilePolicy',
        'comment_history_list': 'list[ICommentHistory]',
        'name': 'str',
        'vlan_tags': 'IVLanTagsContainer',
        'applications': 'IApplicationsContainer'
    }

    attribute_map = {
        'metadata': 'metadata',
        'snmp_config': 'snmpConfig',
        'source_networks': 'sourceNetworks',
        'syslog_severity': 'syslogSeverity',
        'time_range_objects': 'timeRangeObjects',
        'source_zones': 'sourceZones',
        'destination_zones': 'destinationZones',
        'description': 'description',
        'original_source_networks': 'originalSourceNetworks',
        'enable_syslog': 'enableSyslog',
        'type': 'type',
        'safe_search': 'safeSearch',
        'enabled': 'enabled',
        'syslog_config': 'syslogConfig',
        'urls': 'urls',
        'end_point_device_types': 'endPointDeviceTypes',
        'you_tube': 'youTube',
        'destination_networks': 'destinationNetworks',
        'action': 'action',
        'network_access_device_i_ps': 'networkAccessDeviceIPs',
        'links': 'links',
        'id': 'id',
        'source_security_group_tags': 'sourceSecurityGroupTags',
        'destination_security_group_tags': 'destinationSecurityGroupTags',
        'log_end': 'logEnd',
        'log_begin': 'logBegin',
        'send_events_to_fmc': 'sendEventsToFMC',
        'destination_ports': 'destinationPorts',
        'source_ports': 'sourcePorts',
        'ips_policy': 'ipsPolicy',
        'variable_set': 'variableSet',
        'version': 'version',
        'users': 'users',
        'log_files': 'logFiles',
        'new_comments': 'newComments',
        'file_policy': 'filePolicy',
        'comment_history_list': 'commentHistoryList',
        'name': 'name',
        'vlan_tags': 'vlanTags',
        'applications': 'applications'
    }

    def __init__(self, metadata=None, snmp_config=None, source_networks=None, syslog_severity=None, time_range_objects=None, source_zones=None, destination_zones=None, description=None, original_source_networks=None, enable_syslog=None, type=None, safe_search=None, enabled=None, syslog_config=None, urls=None, end_point_device_types=None, you_tube=None, destination_networks=None, action=None, network_access_device_i_ps=None, links=None, id=None, source_security_group_tags=None, destination_security_group_tags=None, log_end=None, log_begin=None, send_events_to_fmc=None, destination_ports=None, source_ports=None, ips_policy=None, variable_set=None, version=None, users=None, log_files=None, new_comments=None, file_policy=None, comment_history_list=None, name=None, vlan_tags=None, applications=None):  # noqa: E501
        """IAccessRuleModel - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._snmp_config = None
        self._source_networks = None
        self._syslog_severity = None
        self._time_range_objects = None
        self._source_zones = None
        self._destination_zones = None
        self._description = None
        self._original_source_networks = None
        self._enable_syslog = None
        self._type = None
        self._safe_search = None
        self._enabled = None
        self._syslog_config = None
        self._urls = None
        self._end_point_device_types = None
        self._you_tube = None
        self._destination_networks = None
        self._action = None
        self._network_access_device_i_ps = None
        self._links = None
        self._id = None
        self._source_security_group_tags = None
        self._destination_security_group_tags = None
        self._log_end = None
        self._log_begin = None
        self._send_events_to_fmc = None
        self._destination_ports = None
        self._source_ports = None
        self._ips_policy = None
        self._variable_set = None
        self._version = None
        self._users = None
        self._log_files = None
        self._new_comments = None
        self._file_policy = None
        self._comment_history_list = None
        self._name = None
        self._vlan_tags = None
        self._applications = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if snmp_config is not None:
            self.snmp_config = snmp_config
        if source_networks is not None:
            self.source_networks = source_networks
        if syslog_severity is not None:
            self.syslog_severity = syslog_severity
        if time_range_objects is not None:
            self.time_range_objects = time_range_objects
        if source_zones is not None:
            self.source_zones = source_zones
        if destination_zones is not None:
            self.destination_zones = destination_zones
        if description is not None:
            self.description = description
        if original_source_networks is not None:
            self.original_source_networks = original_source_networks
        if enable_syslog is not None:
            self.enable_syslog = enable_syslog
        if type is not None:
            self.type = type
        if safe_search is not None:
            self.safe_search = safe_search
        if enabled is not None:
            self.enabled = enabled
        if syslog_config is not None:
            self.syslog_config = syslog_config
        if urls is not None:
            self.urls = urls
        if end_point_device_types is not None:
            self.end_point_device_types = end_point_device_types
        if you_tube is not None:
            self.you_tube = you_tube
        if destination_networks is not None:
            self.destination_networks = destination_networks
        self.action = action
        if network_access_device_i_ps is not None:
            self.network_access_device_i_ps = network_access_device_i_ps
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if source_security_group_tags is not None:
            self.source_security_group_tags = source_security_group_tags
        if destination_security_group_tags is not None:
            self.destination_security_group_tags = destination_security_group_tags
        if log_end is not None:
            self.log_end = log_end
        if log_begin is not None:
            self.log_begin = log_begin
        if send_events_to_fmc is not None:
            self.send_events_to_fmc = send_events_to_fmc
        if destination_ports is not None:
            self.destination_ports = destination_ports
        if source_ports is not None:
            self.source_ports = source_ports
        if ips_policy is not None:
            self.ips_policy = ips_policy
        if variable_set is not None:
            self.variable_set = variable_set
        if version is not None:
            self.version = version
        if users is not None:
            self.users = users
        if log_files is not None:
            self.log_files = log_files
        if new_comments is not None:
            self.new_comments = new_comments
        if file_policy is not None:
            self.file_policy = file_policy
        if comment_history_list is not None:
            self.comment_history_list = comment_history_list
        if name is not None:
            self.name = name
        if vlan_tags is not None:
            self.vlan_tags = vlan_tags
        if applications is not None:
            self.applications = applications

    @property
    def metadata(self):
        """Gets the metadata of this IAccessRuleModel.  # noqa: E501


        :return: The metadata of this IAccessRuleModel.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IAccessRuleModel.


        :param metadata: The metadata of this IAccessRuleModel.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def snmp_config(self):
        """Gets the snmp_config of this IAccessRuleModel.  # noqa: E501


        :return: The snmp_config of this IAccessRuleModel.  # noqa: E501
        :rtype: ISNMPConfig
        """
        return self._snmp_config

    @snmp_config.setter
    def snmp_config(self, snmp_config):
        """Sets the snmp_config of this IAccessRuleModel.


        :param snmp_config: The snmp_config of this IAccessRuleModel.  # noqa: E501
        :type: ISNMPConfig
        """

        self._snmp_config = snmp_config

    @property
    def source_networks(self):
        """Gets the source_networks of this IAccessRuleModel.  # noqa: E501


        :return: The source_networks of this IAccessRuleModel.  # noqa: E501
        :rtype: INetworkObjectsContainer
        """
        return self._source_networks

    @source_networks.setter
    def source_networks(self, source_networks):
        """Sets the source_networks of this IAccessRuleModel.


        :param source_networks: The source_networks of this IAccessRuleModel.  # noqa: E501
        :type: INetworkObjectsContainer
        """

        self._source_networks = source_networks

    @property
    def syslog_severity(self):
        """Gets the syslog_severity of this IAccessRuleModel.  # noqa: E501


        :return: The syslog_severity of this IAccessRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._syslog_severity

    @syslog_severity.setter
    def syslog_severity(self, syslog_severity):
        """Sets the syslog_severity of this IAccessRuleModel.


        :param syslog_severity: The syslog_severity of this IAccessRuleModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALERT", "CRIT", "DEBUG", "EMERG", "ERR", "INFO", "NOTICE", "WARNING"]  # noqa: E501
        if syslog_severity not in allowed_values:
            raise ValueError(
                "Invalid value for `syslog_severity` ({0}), must be one of {1}"  # noqa: E501
                .format(syslog_severity, allowed_values)
            )

        self._syslog_severity = syslog_severity

    @property
    def time_range_objects(self):
        """Gets the time_range_objects of this IAccessRuleModel.  # noqa: E501


        :return: The time_range_objects of this IAccessRuleModel.  # noqa: E501
        :rtype: list[ITimeRangeModel]
        """
        return self._time_range_objects

    @time_range_objects.setter
    def time_range_objects(self, time_range_objects):
        """Sets the time_range_objects of this IAccessRuleModel.


        :param time_range_objects: The time_range_objects of this IAccessRuleModel.  # noqa: E501
        :type: list[ITimeRangeModel]
        """

        self._time_range_objects = time_range_objects

    @property
    def source_zones(self):
        """Gets the source_zones of this IAccessRuleModel.  # noqa: E501


        :return: The source_zones of this IAccessRuleModel.  # noqa: E501
        :rtype: ISourceZoneContainer
        """
        return self._source_zones

    @source_zones.setter
    def source_zones(self, source_zones):
        """Sets the source_zones of this IAccessRuleModel.


        :param source_zones: The source_zones of this IAccessRuleModel.  # noqa: E501
        :type: ISourceZoneContainer
        """

        self._source_zones = source_zones

    @property
    def destination_zones(self):
        """Gets the destination_zones of this IAccessRuleModel.  # noqa: E501


        :return: The destination_zones of this IAccessRuleModel.  # noqa: E501
        :rtype: ISecurityZoneContainer
        """
        return self._destination_zones

    @destination_zones.setter
    def destination_zones(self, destination_zones):
        """Sets the destination_zones of this IAccessRuleModel.


        :param destination_zones: The destination_zones of this IAccessRuleModel.  # noqa: E501
        :type: ISecurityZoneContainer
        """

        self._destination_zones = destination_zones

    @property
    def description(self):
        """Gets the description of this IAccessRuleModel.  # noqa: E501


        :return: The description of this IAccessRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IAccessRuleModel.


        :param description: The description of this IAccessRuleModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def original_source_networks(self):
        """Gets the original_source_networks of this IAccessRuleModel.  # noqa: E501


        :return: The original_source_networks of this IAccessRuleModel.  # noqa: E501
        :rtype: INetworkObjectsContainer
        """
        return self._original_source_networks

    @original_source_networks.setter
    def original_source_networks(self, original_source_networks):
        """Sets the original_source_networks of this IAccessRuleModel.


        :param original_source_networks: The original_source_networks of this IAccessRuleModel.  # noqa: E501
        :type: INetworkObjectsContainer
        """

        self._original_source_networks = original_source_networks

    @property
    def enable_syslog(self):
        """Gets the enable_syslog of this IAccessRuleModel.  # noqa: E501


        :return: The enable_syslog of this IAccessRuleModel.  # noqa: E501
        :rtype: bool
        """
        return self._enable_syslog

    @enable_syslog.setter
    def enable_syslog(self, enable_syslog):
        """Sets the enable_syslog of this IAccessRuleModel.


        :param enable_syslog: The enable_syslog of this IAccessRuleModel.  # noqa: E501
        :type: bool
        """

        self._enable_syslog = enable_syslog

    @property
    def type(self):
        """Gets the type of this IAccessRuleModel.  # noqa: E501


        :return: The type of this IAccessRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IAccessRuleModel.


        :param type: The type of this IAccessRuleModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def safe_search(self):
        """Gets the safe_search of this IAccessRuleModel.  # noqa: E501


        :return: The safe_search of this IAccessRuleModel.  # noqa: E501
        :rtype: ISafeSearch
        """
        return self._safe_search

    @safe_search.setter
    def safe_search(self, safe_search):
        """Sets the safe_search of this IAccessRuleModel.


        :param safe_search: The safe_search of this IAccessRuleModel.  # noqa: E501
        :type: ISafeSearch
        """

        self._safe_search = safe_search

    @property
    def enabled(self):
        """Gets the enabled of this IAccessRuleModel.  # noqa: E501


        :return: The enabled of this IAccessRuleModel.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IAccessRuleModel.


        :param enabled: The enabled of this IAccessRuleModel.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def syslog_config(self):
        """Gets the syslog_config of this IAccessRuleModel.  # noqa: E501


        :return: The syslog_config of this IAccessRuleModel.  # noqa: E501
        :rtype: ISyslogConfig
        """
        return self._syslog_config

    @syslog_config.setter
    def syslog_config(self, syslog_config):
        """Sets the syslog_config of this IAccessRuleModel.


        :param syslog_config: The syslog_config of this IAccessRuleModel.  # noqa: E501
        :type: ISyslogConfig
        """

        self._syslog_config = syslog_config

    @property
    def urls(self):
        """Gets the urls of this IAccessRuleModel.  # noqa: E501


        :return: The urls of this IAccessRuleModel.  # noqa: E501
        :rtype: IUrlObjectsContainer
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this IAccessRuleModel.


        :param urls: The urls of this IAccessRuleModel.  # noqa: E501
        :type: IUrlObjectsContainer
        """

        self._urls = urls

    @property
    def end_point_device_types(self):
        """Gets the end_point_device_types of this IAccessRuleModel.  # noqa: E501


        :return: The end_point_device_types of this IAccessRuleModel.  # noqa: E501
        :rtype: list[IEndPointDeviceType]
        """
        return self._end_point_device_types

    @end_point_device_types.setter
    def end_point_device_types(self, end_point_device_types):
        """Sets the end_point_device_types of this IAccessRuleModel.


        :param end_point_device_types: The end_point_device_types of this IAccessRuleModel.  # noqa: E501
        :type: list[IEndPointDeviceType]
        """

        self._end_point_device_types = end_point_device_types

    @property
    def you_tube(self):
        """Gets the you_tube of this IAccessRuleModel.  # noqa: E501


        :return: The you_tube of this IAccessRuleModel.  # noqa: E501
        :rtype: IYouTube
        """
        return self._you_tube

    @you_tube.setter
    def you_tube(self, you_tube):
        """Sets the you_tube of this IAccessRuleModel.


        :param you_tube: The you_tube of this IAccessRuleModel.  # noqa: E501
        :type: IYouTube
        """

        self._you_tube = you_tube

    @property
    def destination_networks(self):
        """Gets the destination_networks of this IAccessRuleModel.  # noqa: E501


        :return: The destination_networks of this IAccessRuleModel.  # noqa: E501
        :rtype: INetworkObjectsContainer
        """
        return self._destination_networks

    @destination_networks.setter
    def destination_networks(self, destination_networks):
        """Sets the destination_networks of this IAccessRuleModel.


        :param destination_networks: The destination_networks of this IAccessRuleModel.  # noqa: E501
        :type: INetworkObjectsContainer
        """

        self._destination_networks = destination_networks

    @property
    def action(self):
        """Gets the action of this IAccessRuleModel.  # noqa: E501


        :return: The action of this IAccessRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IAccessRuleModel.


        :param action: The action of this IAccessRuleModel.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["ALLOW", "TRUST", "BLOCK", "MONITOR", "BLOCK_RESET", "BLOCK_INTERACTIVE", "BLOCK_RESET_INTERACTIVE"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def network_access_device_i_ps(self):
        """Gets the network_access_device_i_ps of this IAccessRuleModel.  # noqa: E501


        :return: The network_access_device_i_ps of this IAccessRuleModel.  # noqa: E501
        :rtype: INetworkObjectsContainer
        """
        return self._network_access_device_i_ps

    @network_access_device_i_ps.setter
    def network_access_device_i_ps(self, network_access_device_i_ps):
        """Sets the network_access_device_i_ps of this IAccessRuleModel.


        :param network_access_device_i_ps: The network_access_device_i_ps of this IAccessRuleModel.  # noqa: E501
        :type: INetworkObjectsContainer
        """

        self._network_access_device_i_ps = network_access_device_i_ps

    @property
    def links(self):
        """Gets the links of this IAccessRuleModel.  # noqa: E501


        :return: The links of this IAccessRuleModel.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IAccessRuleModel.


        :param links: The links of this IAccessRuleModel.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IAccessRuleModel.  # noqa: E501


        :return: The id of this IAccessRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IAccessRuleModel.


        :param id: The id of this IAccessRuleModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source_security_group_tags(self):
        """Gets the source_security_group_tags of this IAccessRuleModel.  # noqa: E501


        :return: The source_security_group_tags of this IAccessRuleModel.  # noqa: E501
        :rtype: ISecurityGroupTagContainer
        """
        return self._source_security_group_tags

    @source_security_group_tags.setter
    def source_security_group_tags(self, source_security_group_tags):
        """Sets the source_security_group_tags of this IAccessRuleModel.


        :param source_security_group_tags: The source_security_group_tags of this IAccessRuleModel.  # noqa: E501
        :type: ISecurityGroupTagContainer
        """

        self._source_security_group_tags = source_security_group_tags

    @property
    def destination_security_group_tags(self):
        """Gets the destination_security_group_tags of this IAccessRuleModel.  # noqa: E501


        :return: The destination_security_group_tags of this IAccessRuleModel.  # noqa: E501
        :rtype: ISecurityGroupTagContainer
        """
        return self._destination_security_group_tags

    @destination_security_group_tags.setter
    def destination_security_group_tags(self, destination_security_group_tags):
        """Sets the destination_security_group_tags of this IAccessRuleModel.


        :param destination_security_group_tags: The destination_security_group_tags of this IAccessRuleModel.  # noqa: E501
        :type: ISecurityGroupTagContainer
        """

        self._destination_security_group_tags = destination_security_group_tags

    @property
    def log_end(self):
        """Gets the log_end of this IAccessRuleModel.  # noqa: E501


        :return: The log_end of this IAccessRuleModel.  # noqa: E501
        :rtype: bool
        """
        return self._log_end

    @log_end.setter
    def log_end(self, log_end):
        """Sets the log_end of this IAccessRuleModel.


        :param log_end: The log_end of this IAccessRuleModel.  # noqa: E501
        :type: bool
        """

        self._log_end = log_end

    @property
    def log_begin(self):
        """Gets the log_begin of this IAccessRuleModel.  # noqa: E501


        :return: The log_begin of this IAccessRuleModel.  # noqa: E501
        :rtype: bool
        """
        return self._log_begin

    @log_begin.setter
    def log_begin(self, log_begin):
        """Sets the log_begin of this IAccessRuleModel.


        :param log_begin: The log_begin of this IAccessRuleModel.  # noqa: E501
        :type: bool
        """

        self._log_begin = log_begin

    @property
    def send_events_to_fmc(self):
        """Gets the send_events_to_fmc of this IAccessRuleModel.  # noqa: E501


        :return: The send_events_to_fmc of this IAccessRuleModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_events_to_fmc

    @send_events_to_fmc.setter
    def send_events_to_fmc(self, send_events_to_fmc):
        """Sets the send_events_to_fmc of this IAccessRuleModel.


        :param send_events_to_fmc: The send_events_to_fmc of this IAccessRuleModel.  # noqa: E501
        :type: bool
        """

        self._send_events_to_fmc = send_events_to_fmc

    @property
    def destination_ports(self):
        """Gets the destination_ports of this IAccessRuleModel.  # noqa: E501


        :return: The destination_ports of this IAccessRuleModel.  # noqa: E501
        :rtype: IPortObjectsContainer
        """
        return self._destination_ports

    @destination_ports.setter
    def destination_ports(self, destination_ports):
        """Sets the destination_ports of this IAccessRuleModel.


        :param destination_ports: The destination_ports of this IAccessRuleModel.  # noqa: E501
        :type: IPortObjectsContainer
        """

        self._destination_ports = destination_ports

    @property
    def source_ports(self):
        """Gets the source_ports of this IAccessRuleModel.  # noqa: E501


        :return: The source_ports of this IAccessRuleModel.  # noqa: E501
        :rtype: IPortObjectsContainer
        """
        return self._source_ports

    @source_ports.setter
    def source_ports(self, source_ports):
        """Sets the source_ports of this IAccessRuleModel.


        :param source_ports: The source_ports of this IAccessRuleModel.  # noqa: E501
        :type: IPortObjectsContainer
        """

        self._source_ports = source_ports

    @property
    def ips_policy(self):
        """Gets the ips_policy of this IAccessRuleModel.  # noqa: E501


        :return: The ips_policy of this IAccessRuleModel.  # noqa: E501
        :rtype: IIntrusionPolicyModel
        """
        return self._ips_policy

    @ips_policy.setter
    def ips_policy(self, ips_policy):
        """Sets the ips_policy of this IAccessRuleModel.


        :param ips_policy: The ips_policy of this IAccessRuleModel.  # noqa: E501
        :type: IIntrusionPolicyModel
        """

        self._ips_policy = ips_policy

    @property
    def variable_set(self):
        """Gets the variable_set of this IAccessRuleModel.  # noqa: E501


        :return: The variable_set of this IAccessRuleModel.  # noqa: E501
        :rtype: IVariableSet
        """
        return self._variable_set

    @variable_set.setter
    def variable_set(self, variable_set):
        """Sets the variable_set of this IAccessRuleModel.


        :param variable_set: The variable_set of this IAccessRuleModel.  # noqa: E501
        :type: IVariableSet
        """

        self._variable_set = variable_set

    @property
    def version(self):
        """Gets the version of this IAccessRuleModel.  # noqa: E501


        :return: The version of this IAccessRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IAccessRuleModel.


        :param version: The version of this IAccessRuleModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def users(self):
        """Gets the users of this IAccessRuleModel.  # noqa: E501


        :return: The users of this IAccessRuleModel.  # noqa: E501
        :rtype: IUsersContainer
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this IAccessRuleModel.


        :param users: The users of this IAccessRuleModel.  # noqa: E501
        :type: IUsersContainer
        """

        self._users = users

    @property
    def log_files(self):
        """Gets the log_files of this IAccessRuleModel.  # noqa: E501


        :return: The log_files of this IAccessRuleModel.  # noqa: E501
        :rtype: bool
        """
        return self._log_files

    @log_files.setter
    def log_files(self, log_files):
        """Sets the log_files of this IAccessRuleModel.


        :param log_files: The log_files of this IAccessRuleModel.  # noqa: E501
        :type: bool
        """

        self._log_files = log_files

    @property
    def new_comments(self):
        """Gets the new_comments of this IAccessRuleModel.  # noqa: E501


        :return: The new_comments of this IAccessRuleModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_comments

    @new_comments.setter
    def new_comments(self, new_comments):
        """Sets the new_comments of this IAccessRuleModel.


        :param new_comments: The new_comments of this IAccessRuleModel.  # noqa: E501
        :type: list[str]
        """

        self._new_comments = new_comments

    @property
    def file_policy(self):
        """Gets the file_policy of this IAccessRuleModel.  # noqa: E501


        :return: The file_policy of this IAccessRuleModel.  # noqa: E501
        :rtype: IFilePolicy
        """
        return self._file_policy

    @file_policy.setter
    def file_policy(self, file_policy):
        """Sets the file_policy of this IAccessRuleModel.


        :param file_policy: The file_policy of this IAccessRuleModel.  # noqa: E501
        :type: IFilePolicy
        """

        self._file_policy = file_policy

    @property
    def comment_history_list(self):
        """Gets the comment_history_list of this IAccessRuleModel.  # noqa: E501


        :return: The comment_history_list of this IAccessRuleModel.  # noqa: E501
        :rtype: list[ICommentHistory]
        """
        return self._comment_history_list

    @comment_history_list.setter
    def comment_history_list(self, comment_history_list):
        """Sets the comment_history_list of this IAccessRuleModel.


        :param comment_history_list: The comment_history_list of this IAccessRuleModel.  # noqa: E501
        :type: list[ICommentHistory]
        """

        self._comment_history_list = comment_history_list

    @property
    def name(self):
        """Gets the name of this IAccessRuleModel.  # noqa: E501


        :return: The name of this IAccessRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IAccessRuleModel.


        :param name: The name of this IAccessRuleModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vlan_tags(self):
        """Gets the vlan_tags of this IAccessRuleModel.  # noqa: E501


        :return: The vlan_tags of this IAccessRuleModel.  # noqa: E501
        :rtype: IVLanTagsContainer
        """
        return self._vlan_tags

    @vlan_tags.setter
    def vlan_tags(self, vlan_tags):
        """Sets the vlan_tags of this IAccessRuleModel.


        :param vlan_tags: The vlan_tags of this IAccessRuleModel.  # noqa: E501
        :type: IVLanTagsContainer
        """

        self._vlan_tags = vlan_tags

    @property
    def applications(self):
        """Gets the applications of this IAccessRuleModel.  # noqa: E501


        :return: The applications of this IAccessRuleModel.  # noqa: E501
        :rtype: IApplicationsContainer
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this IAccessRuleModel.


        :param applications: The applications of this IAccessRuleModel.  # noqa: E501
        :type: IApplicationsContainer
        """

        self._applications = applications

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IAccessRuleModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IAccessRuleModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other