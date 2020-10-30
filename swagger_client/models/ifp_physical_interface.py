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


class IFPPhysicalInterface(object):
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
        'description': 'str',
        'type': 'str',
        'version': 'str',
        'enabled': 'int',
        'mtu': 'int',
        'mode': 'str',
        'interface_type': 'str',
        'mdi': 'str',
        'static_arp_entries': 'list[IStaticArpEntry]',
        'name': 'str',
        'ip_addresses': 'list[str]',
        'links': 'ILinks',
        'id': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'description': 'description',
        'type': 'type',
        'version': 'version',
        'enabled': 'enabled',
        'mtu': 'mtu',
        'mode': 'mode',
        'interface_type': 'interfaceType',
        'mdi': 'mdi',
        'static_arp_entries': 'staticArpEntries',
        'name': 'name',
        'ip_addresses': 'ipAddresses',
        'links': 'links',
        'id': 'id'
    }

    def __init__(self, metadata=None, description=None, type=None, version=None, enabled=None, mtu=None, mode=None, interface_type=None, mdi=None, static_arp_entries=None, name=None, ip_addresses=None, links=None, id=None):  # noqa: E501
        """IFPPhysicalInterface - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._description = None
        self._type = None
        self._version = None
        self._enabled = None
        self._mtu = None
        self._mode = None
        self._interface_type = None
        self._mdi = None
        self._static_arp_entries = None
        self._name = None
        self._ip_addresses = None
        self._links = None
        self._id = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if enabled is not None:
            self.enabled = enabled
        if mtu is not None:
            self.mtu = mtu
        if mode is not None:
            self.mode = mode
        if interface_type is not None:
            self.interface_type = interface_type
        if mdi is not None:
            self.mdi = mdi
        if static_arp_entries is not None:
            self.static_arp_entries = static_arp_entries
        if name is not None:
            self.name = name
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id

    @property
    def metadata(self):
        """Gets the metadata of this IFPPhysicalInterface.  # noqa: E501


        :return: The metadata of this IFPPhysicalInterface.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IFPPhysicalInterface.


        :param metadata: The metadata of this IFPPhysicalInterface.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this IFPPhysicalInterface.  # noqa: E501


        :return: The description of this IFPPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IFPPhysicalInterface.


        :param description: The description of this IFPPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this IFPPhysicalInterface.  # noqa: E501


        :return: The type of this IFPPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IFPPhysicalInterface.


        :param type: The type of this IFPPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this IFPPhysicalInterface.  # noqa: E501


        :return: The version of this IFPPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IFPPhysicalInterface.


        :param version: The version of this IFPPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def enabled(self):
        """Gets the enabled of this IFPPhysicalInterface.  # noqa: E501


        :return: The enabled of this IFPPhysicalInterface.  # noqa: E501
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IFPPhysicalInterface.


        :param enabled: The enabled of this IFPPhysicalInterface.  # noqa: E501
        :type: int
        """

        self._enabled = enabled

    @property
    def mtu(self):
        """Gets the mtu of this IFPPhysicalInterface.  # noqa: E501


        :return: The mtu of this IFPPhysicalInterface.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this IFPPhysicalInterface.


        :param mtu: The mtu of this IFPPhysicalInterface.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def mode(self):
        """Gets the mode of this IFPPhysicalInterface.  # noqa: E501


        :return: The mode of this IFPPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this IFPPhysicalInterface.


        :param mode: The mode of this IFPPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def interface_type(self):
        """Gets the interface_type of this IFPPhysicalInterface.  # noqa: E501


        :return: The interface_type of this IFPPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this IFPPhysicalInterface.


        :param interface_type: The interface_type of this IFPPhysicalInterface.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "MANAGEMENT", "PASSIVE", "INLINE", "SWITCHED", "ROUTED", "HA_LINK", "ASA"]  # noqa: E501
        if interface_type not in allowed_values:
            raise ValueError(
                "Invalid value for `interface_type` ({0}), must be one of {1}"  # noqa: E501
                .format(interface_type, allowed_values)
            )

        self._interface_type = interface_type

    @property
    def mdi(self):
        """Gets the mdi of this IFPPhysicalInterface.  # noqa: E501


        :return: The mdi of this IFPPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._mdi

    @mdi.setter
    def mdi(self, mdi):
        """Sets the mdi of this IFPPhysicalInterface.


        :param mdi: The mdi of this IFPPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._mdi = mdi

    @property
    def static_arp_entries(self):
        """Gets the static_arp_entries of this IFPPhysicalInterface.  # noqa: E501


        :return: The static_arp_entries of this IFPPhysicalInterface.  # noqa: E501
        :rtype: list[IStaticArpEntry]
        """
        return self._static_arp_entries

    @static_arp_entries.setter
    def static_arp_entries(self, static_arp_entries):
        """Sets the static_arp_entries of this IFPPhysicalInterface.


        :param static_arp_entries: The static_arp_entries of this IFPPhysicalInterface.  # noqa: E501
        :type: list[IStaticArpEntry]
        """

        self._static_arp_entries = static_arp_entries

    @property
    def name(self):
        """Gets the name of this IFPPhysicalInterface.  # noqa: E501


        :return: The name of this IFPPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IFPPhysicalInterface.


        :param name: The name of this IFPPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this IFPPhysicalInterface.  # noqa: E501


        :return: The ip_addresses of this IFPPhysicalInterface.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this IFPPhysicalInterface.


        :param ip_addresses: The ip_addresses of this IFPPhysicalInterface.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def links(self):
        """Gets the links of this IFPPhysicalInterface.  # noqa: E501


        :return: The links of this IFPPhysicalInterface.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IFPPhysicalInterface.


        :param links: The links of this IFPPhysicalInterface.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IFPPhysicalInterface.  # noqa: E501


        :return: The id of this IFPPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IFPPhysicalInterface.


        :param id: The id of this IFPPhysicalInterface.  # noqa: E501
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
        if issubclass(IFPPhysicalInterface, dict):
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
        if not isinstance(other, IFPPhysicalInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
