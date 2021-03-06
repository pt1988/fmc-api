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


class VrfOspfPolicyModel(object):
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
        'metadata': 'Metadata',
        'filter_rules': 'list[IOspfFilterRule]',
        'log_adjacency_changes': 'IOspfLogAdjChanges',
        'description': 'str',
        'enable_process': 'str',
        'areas': 'list[IOspfArea]',
        'summary_addresses': 'list[IOspfSummaryAddresses]',
        'type': 'str',
        'version': 'str',
        'process_id': 'str',
        'neighbors': 'list[IOspfNeighbors]',
        'process_configuration': 'IOspfProcessModel',
        'name': 'str',
        'links': 'ILinks',
        'redistribute_protocols': 'list[IRedistributeProtocolBase]',
        'id': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'filter_rules': 'filterRules',
        'log_adjacency_changes': 'logAdjacencyChanges',
        'description': 'description',
        'enable_process': 'enableProcess',
        'areas': 'areas',
        'summary_addresses': 'summaryAddresses',
        'type': 'type',
        'version': 'version',
        'process_id': 'processId',
        'neighbors': 'neighbors',
        'process_configuration': 'processConfiguration',
        'name': 'name',
        'links': 'links',
        'redistribute_protocols': 'redistributeProtocols',
        'id': 'id'
    }

    def __init__(self, metadata=None, filter_rules=None, log_adjacency_changes=None, description=None, enable_process=None, areas=None, summary_addresses=None, type=None, version=None, process_id=None, neighbors=None, process_configuration=None, name=None, links=None, redistribute_protocols=None, id=None):  # noqa: E501
        """VrfOspfPolicyModel - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._filter_rules = None
        self._log_adjacency_changes = None
        self._description = None
        self._enable_process = None
        self._areas = None
        self._summary_addresses = None
        self._type = None
        self._version = None
        self._process_id = None
        self._neighbors = None
        self._process_configuration = None
        self._name = None
        self._links = None
        self._redistribute_protocols = None
        self._id = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if filter_rules is not None:
            self.filter_rules = filter_rules
        if log_adjacency_changes is not None:
            self.log_adjacency_changes = log_adjacency_changes
        if description is not None:
            self.description = description
        if enable_process is not None:
            self.enable_process = enable_process
        if areas is not None:
            self.areas = areas
        if summary_addresses is not None:
            self.summary_addresses = summary_addresses
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if process_id is not None:
            self.process_id = process_id
        if neighbors is not None:
            self.neighbors = neighbors
        if process_configuration is not None:
            self.process_configuration = process_configuration
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if redistribute_protocols is not None:
            self.redistribute_protocols = redistribute_protocols
        if id is not None:
            self.id = id

    @property
    def metadata(self):
        """Gets the metadata of this VrfOspfPolicyModel.  # noqa: E501


        :return: The metadata of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VrfOspfPolicyModel.


        :param metadata: The metadata of this VrfOspfPolicyModel.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def filter_rules(self):
        """Gets the filter_rules of this VrfOspfPolicyModel.  # noqa: E501


        :return: The filter_rules of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: list[IOspfFilterRule]
        """
        return self._filter_rules

    @filter_rules.setter
    def filter_rules(self, filter_rules):
        """Sets the filter_rules of this VrfOspfPolicyModel.


        :param filter_rules: The filter_rules of this VrfOspfPolicyModel.  # noqa: E501
        :type: list[IOspfFilterRule]
        """

        self._filter_rules = filter_rules

    @property
    def log_adjacency_changes(self):
        """Gets the log_adjacency_changes of this VrfOspfPolicyModel.  # noqa: E501


        :return: The log_adjacency_changes of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: IOspfLogAdjChanges
        """
        return self._log_adjacency_changes

    @log_adjacency_changes.setter
    def log_adjacency_changes(self, log_adjacency_changes):
        """Sets the log_adjacency_changes of this VrfOspfPolicyModel.


        :param log_adjacency_changes: The log_adjacency_changes of this VrfOspfPolicyModel.  # noqa: E501
        :type: IOspfLogAdjChanges
        """

        self._log_adjacency_changes = log_adjacency_changes

    @property
    def description(self):
        """Gets the description of this VrfOspfPolicyModel.  # noqa: E501


        :return: The description of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VrfOspfPolicyModel.


        :param description: The description of this VrfOspfPolicyModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable_process(self):
        """Gets the enable_process of this VrfOspfPolicyModel.  # noqa: E501


        :return: The enable_process of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._enable_process

    @enable_process.setter
    def enable_process(self, enable_process):
        """Sets the enable_process of this VrfOspfPolicyModel.


        :param enable_process: The enable_process of this VrfOspfPolicyModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["PROCESS_1", "PROCESS_2"]  # noqa: E501
        if enable_process not in allowed_values:
            raise ValueError(
                "Invalid value for `enable_process` ({0}), must be one of {1}"  # noqa: E501
                .format(enable_process, allowed_values)
            )

        self._enable_process = enable_process

    @property
    def areas(self):
        """Gets the areas of this VrfOspfPolicyModel.  # noqa: E501


        :return: The areas of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: list[IOspfArea]
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        """Sets the areas of this VrfOspfPolicyModel.


        :param areas: The areas of this VrfOspfPolicyModel.  # noqa: E501
        :type: list[IOspfArea]
        """

        self._areas = areas

    @property
    def summary_addresses(self):
        """Gets the summary_addresses of this VrfOspfPolicyModel.  # noqa: E501


        :return: The summary_addresses of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: list[IOspfSummaryAddresses]
        """
        return self._summary_addresses

    @summary_addresses.setter
    def summary_addresses(self, summary_addresses):
        """Sets the summary_addresses of this VrfOspfPolicyModel.


        :param summary_addresses: The summary_addresses of this VrfOspfPolicyModel.  # noqa: E501
        :type: list[IOspfSummaryAddresses]
        """

        self._summary_addresses = summary_addresses

    @property
    def type(self):
        """Gets the type of this VrfOspfPolicyModel.  # noqa: E501


        :return: The type of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VrfOspfPolicyModel.


        :param type: The type of this VrfOspfPolicyModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this VrfOspfPolicyModel.  # noqa: E501


        :return: The version of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VrfOspfPolicyModel.


        :param version: The version of this VrfOspfPolicyModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def process_id(self):
        """Gets the process_id of this VrfOspfPolicyModel.  # noqa: E501


        :return: The process_id of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        """Sets the process_id of this VrfOspfPolicyModel.


        :param process_id: The process_id of this VrfOspfPolicyModel.  # noqa: E501
        :type: str
        """

        self._process_id = process_id

    @property
    def neighbors(self):
        """Gets the neighbors of this VrfOspfPolicyModel.  # noqa: E501


        :return: The neighbors of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: list[IOspfNeighbors]
        """
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors):
        """Sets the neighbors of this VrfOspfPolicyModel.


        :param neighbors: The neighbors of this VrfOspfPolicyModel.  # noqa: E501
        :type: list[IOspfNeighbors]
        """

        self._neighbors = neighbors

    @property
    def process_configuration(self):
        """Gets the process_configuration of this VrfOspfPolicyModel.  # noqa: E501


        :return: The process_configuration of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: IOspfProcessModel
        """
        return self._process_configuration

    @process_configuration.setter
    def process_configuration(self, process_configuration):
        """Sets the process_configuration of this VrfOspfPolicyModel.


        :param process_configuration: The process_configuration of this VrfOspfPolicyModel.  # noqa: E501
        :type: IOspfProcessModel
        """

        self._process_configuration = process_configuration

    @property
    def name(self):
        """Gets the name of this VrfOspfPolicyModel.  # noqa: E501


        :return: The name of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VrfOspfPolicyModel.


        :param name: The name of this VrfOspfPolicyModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this VrfOspfPolicyModel.  # noqa: E501


        :return: The links of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VrfOspfPolicyModel.


        :param links: The links of this VrfOspfPolicyModel.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def redistribute_protocols(self):
        """Gets the redistribute_protocols of this VrfOspfPolicyModel.  # noqa: E501


        :return: The redistribute_protocols of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: list[IRedistributeProtocolBase]
        """
        return self._redistribute_protocols

    @redistribute_protocols.setter
    def redistribute_protocols(self, redistribute_protocols):
        """Sets the redistribute_protocols of this VrfOspfPolicyModel.


        :param redistribute_protocols: The redistribute_protocols of this VrfOspfPolicyModel.  # noqa: E501
        :type: list[IRedistributeProtocolBase]
        """

        self._redistribute_protocols = redistribute_protocols

    @property
    def id(self):
        """Gets the id of this VrfOspfPolicyModel.  # noqa: E501


        :return: The id of this VrfOspfPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VrfOspfPolicyModel.


        :param id: The id of this VrfOspfPolicyModel.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(VrfOspfPolicyModel, dict):
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
        if not isinstance(other, VrfOspfPolicyModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
