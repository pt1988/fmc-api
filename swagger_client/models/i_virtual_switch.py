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


class IVirtualSwitch(object):
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
        'drop_bpdu': 'bool',
        'metadata': 'IMetadata',
        'sensor_policy': 'IAccessPolicyModel',
        'description': 'str',
        'type': 'str',
        'strict_tcp_enforcement': 'bool',
        'version': 'str',
        'domain_id': 'int',
        'static_mac_entries': 'list[IStaticMacEntry]',
        'name': 'str',
        'switched_interfaces': 'list[IInterface]',
        'enable_spanning_tree_protocol': 'bool',
        'links': 'ILinks',
        'id': 'str',
        'hybrid_interface': 'IInterface'
    }

    attribute_map = {
        'drop_bpdu': 'dropBPDU',
        'metadata': 'metadata',
        'sensor_policy': 'sensorPolicy',
        'description': 'description',
        'type': 'type',
        'strict_tcp_enforcement': 'strictTCPEnforcement',
        'version': 'version',
        'domain_id': 'domainId',
        'static_mac_entries': 'staticMacEntries',
        'name': 'name',
        'switched_interfaces': 'switchedInterfaces',
        'enable_spanning_tree_protocol': 'enableSpanningTreeProtocol',
        'links': 'links',
        'id': 'id',
        'hybrid_interface': 'hybridInterface'
    }

    def __init__(self, drop_bpdu=None, metadata=None, sensor_policy=None, description=None, type=None, strict_tcp_enforcement=None, version=None, domain_id=None, static_mac_entries=None, name=None, switched_interfaces=None, enable_spanning_tree_protocol=None, links=None, id=None, hybrid_interface=None):  # noqa: E501
        """IVirtualSwitch - a model defined in Swagger"""  # noqa: E501

        self._drop_bpdu = None
        self._metadata = None
        self._sensor_policy = None
        self._description = None
        self._type = None
        self._strict_tcp_enforcement = None
        self._version = None
        self._domain_id = None
        self._static_mac_entries = None
        self._name = None
        self._switched_interfaces = None
        self._enable_spanning_tree_protocol = None
        self._links = None
        self._id = None
        self._hybrid_interface = None
        self.discriminator = None

        if drop_bpdu is not None:
            self.drop_bpdu = drop_bpdu
        if metadata is not None:
            self.metadata = metadata
        if sensor_policy is not None:
            self.sensor_policy = sensor_policy
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if strict_tcp_enforcement is not None:
            self.strict_tcp_enforcement = strict_tcp_enforcement
        if version is not None:
            self.version = version
        if domain_id is not None:
            self.domain_id = domain_id
        if static_mac_entries is not None:
            self.static_mac_entries = static_mac_entries
        if name is not None:
            self.name = name
        if switched_interfaces is not None:
            self.switched_interfaces = switched_interfaces
        if enable_spanning_tree_protocol is not None:
            self.enable_spanning_tree_protocol = enable_spanning_tree_protocol
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if hybrid_interface is not None:
            self.hybrid_interface = hybrid_interface

    @property
    def drop_bpdu(self):
        """Gets the drop_bpdu of this IVirtualSwitch.  # noqa: E501


        :return: The drop_bpdu of this IVirtualSwitch.  # noqa: E501
        :rtype: bool
        """
        return self._drop_bpdu

    @drop_bpdu.setter
    def drop_bpdu(self, drop_bpdu):
        """Sets the drop_bpdu of this IVirtualSwitch.


        :param drop_bpdu: The drop_bpdu of this IVirtualSwitch.  # noqa: E501
        :type: bool
        """

        self._drop_bpdu = drop_bpdu

    @property
    def metadata(self):
        """Gets the metadata of this IVirtualSwitch.  # noqa: E501


        :return: The metadata of this IVirtualSwitch.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IVirtualSwitch.


        :param metadata: The metadata of this IVirtualSwitch.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def sensor_policy(self):
        """Gets the sensor_policy of this IVirtualSwitch.  # noqa: E501


        :return: The sensor_policy of this IVirtualSwitch.  # noqa: E501
        :rtype: IAccessPolicyModel
        """
        return self._sensor_policy

    @sensor_policy.setter
    def sensor_policy(self, sensor_policy):
        """Sets the sensor_policy of this IVirtualSwitch.


        :param sensor_policy: The sensor_policy of this IVirtualSwitch.  # noqa: E501
        :type: IAccessPolicyModel
        """

        self._sensor_policy = sensor_policy

    @property
    def description(self):
        """Gets the description of this IVirtualSwitch.  # noqa: E501


        :return: The description of this IVirtualSwitch.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IVirtualSwitch.


        :param description: The description of this IVirtualSwitch.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this IVirtualSwitch.  # noqa: E501


        :return: The type of this IVirtualSwitch.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IVirtualSwitch.


        :param type: The type of this IVirtualSwitch.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def strict_tcp_enforcement(self):
        """Gets the strict_tcp_enforcement of this IVirtualSwitch.  # noqa: E501


        :return: The strict_tcp_enforcement of this IVirtualSwitch.  # noqa: E501
        :rtype: bool
        """
        return self._strict_tcp_enforcement

    @strict_tcp_enforcement.setter
    def strict_tcp_enforcement(self, strict_tcp_enforcement):
        """Sets the strict_tcp_enforcement of this IVirtualSwitch.


        :param strict_tcp_enforcement: The strict_tcp_enforcement of this IVirtualSwitch.  # noqa: E501
        :type: bool
        """

        self._strict_tcp_enforcement = strict_tcp_enforcement

    @property
    def version(self):
        """Gets the version of this IVirtualSwitch.  # noqa: E501


        :return: The version of this IVirtualSwitch.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IVirtualSwitch.


        :param version: The version of this IVirtualSwitch.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def domain_id(self):
        """Gets the domain_id of this IVirtualSwitch.  # noqa: E501


        :return: The domain_id of this IVirtualSwitch.  # noqa: E501
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this IVirtualSwitch.


        :param domain_id: The domain_id of this IVirtualSwitch.  # noqa: E501
        :type: int
        """

        self._domain_id = domain_id

    @property
    def static_mac_entries(self):
        """Gets the static_mac_entries of this IVirtualSwitch.  # noqa: E501


        :return: The static_mac_entries of this IVirtualSwitch.  # noqa: E501
        :rtype: list[IStaticMacEntry]
        """
        return self._static_mac_entries

    @static_mac_entries.setter
    def static_mac_entries(self, static_mac_entries):
        """Sets the static_mac_entries of this IVirtualSwitch.


        :param static_mac_entries: The static_mac_entries of this IVirtualSwitch.  # noqa: E501
        :type: list[IStaticMacEntry]
        """

        self._static_mac_entries = static_mac_entries

    @property
    def name(self):
        """Gets the name of this IVirtualSwitch.  # noqa: E501


        :return: The name of this IVirtualSwitch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IVirtualSwitch.


        :param name: The name of this IVirtualSwitch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def switched_interfaces(self):
        """Gets the switched_interfaces of this IVirtualSwitch.  # noqa: E501


        :return: The switched_interfaces of this IVirtualSwitch.  # noqa: E501
        :rtype: list[IInterface]
        """
        return self._switched_interfaces

    @switched_interfaces.setter
    def switched_interfaces(self, switched_interfaces):
        """Sets the switched_interfaces of this IVirtualSwitch.


        :param switched_interfaces: The switched_interfaces of this IVirtualSwitch.  # noqa: E501
        :type: list[IInterface]
        """

        self._switched_interfaces = switched_interfaces

    @property
    def enable_spanning_tree_protocol(self):
        """Gets the enable_spanning_tree_protocol of this IVirtualSwitch.  # noqa: E501


        :return: The enable_spanning_tree_protocol of this IVirtualSwitch.  # noqa: E501
        :rtype: bool
        """
        return self._enable_spanning_tree_protocol

    @enable_spanning_tree_protocol.setter
    def enable_spanning_tree_protocol(self, enable_spanning_tree_protocol):
        """Sets the enable_spanning_tree_protocol of this IVirtualSwitch.


        :param enable_spanning_tree_protocol: The enable_spanning_tree_protocol of this IVirtualSwitch.  # noqa: E501
        :type: bool
        """

        self._enable_spanning_tree_protocol = enable_spanning_tree_protocol

    @property
    def links(self):
        """Gets the links of this IVirtualSwitch.  # noqa: E501


        :return: The links of this IVirtualSwitch.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IVirtualSwitch.


        :param links: The links of this IVirtualSwitch.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IVirtualSwitch.  # noqa: E501


        :return: The id of this IVirtualSwitch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IVirtualSwitch.


        :param id: The id of this IVirtualSwitch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def hybrid_interface(self):
        """Gets the hybrid_interface of this IVirtualSwitch.  # noqa: E501


        :return: The hybrid_interface of this IVirtualSwitch.  # noqa: E501
        :rtype: IInterface
        """
        return self._hybrid_interface

    @hybrid_interface.setter
    def hybrid_interface(self, hybrid_interface):
        """Sets the hybrid_interface of this IVirtualSwitch.


        :param hybrid_interface: The hybrid_interface of this IVirtualSwitch.  # noqa: E501
        :type: IInterface
        """

        self._hybrid_interface = hybrid_interface

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
        if issubclass(IVirtualSwitch, dict):
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
        if not isinstance(other, IVirtualSwitch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
