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


class FTDHAInterfaceMACAddresses(object):
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
        'failover_active_mac': 'str',
        'metadata': 'IMetadata',
        'failover_standby_mac': 'str',
        'physical_interface': 'FTDBaseInterface',
        'name': 'str',
        'description': 'str',
        'links': 'ILinks',
        'id': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'failover_active_mac': 'failoverActiveMac',
        'metadata': 'metadata',
        'failover_standby_mac': 'failoverStandbyMac',
        'physical_interface': 'physicalInterface',
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'id': 'id',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, failover_active_mac=None, metadata=None, failover_standby_mac=None, physical_interface=None, name=None, description=None, links=None, id=None, type=None, version=None):  # noqa: E501
        """FTDHAInterfaceMACAddresses - a model defined in Swagger"""  # noqa: E501

        self._failover_active_mac = None
        self._metadata = None
        self._failover_standby_mac = None
        self._physical_interface = None
        self._name = None
        self._description = None
        self._links = None
        self._id = None
        self._type = None
        self._version = None
        self.discriminator = None

        self.failover_active_mac = failover_active_mac
        if metadata is not None:
            self.metadata = metadata
        self.failover_standby_mac = failover_standby_mac
        self.physical_interface = physical_interface
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def failover_active_mac(self):
        """Gets the failover_active_mac of this FTDHAInterfaceMACAddresses.  # noqa: E501

        Interface MAC address in H.H.H format, where H is a 16-bit hexadecimal digit. For example, the MAC address 00-0C-F1-42-4C-DE would be entered as 000C.F142.4CDE  # noqa: E501

        :return: The failover_active_mac of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: str
        """
        return self._failover_active_mac

    @failover_active_mac.setter
    def failover_active_mac(self, failover_active_mac):
        """Sets the failover_active_mac of this FTDHAInterfaceMACAddresses.

        Interface MAC address in H.H.H format, where H is a 16-bit hexadecimal digit. For example, the MAC address 00-0C-F1-42-4C-DE would be entered as 000C.F142.4CDE  # noqa: E501

        :param failover_active_mac: The failover_active_mac of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: str
        """
        if failover_active_mac is None:
            raise ValueError("Invalid value for `failover_active_mac`, must not be `None`")  # noqa: E501

        self._failover_active_mac = failover_active_mac

    @property
    def metadata(self):
        """Gets the metadata of this FTDHAInterfaceMACAddresses.  # noqa: E501

        Object representing metadata properties  # noqa: E501

        :return: The metadata of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FTDHAInterfaceMACAddresses.

        Object representing metadata properties  # noqa: E501

        :param metadata: The metadata of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def failover_standby_mac(self):
        """Gets the failover_standby_mac of this FTDHAInterfaceMACAddresses.  # noqa: E501

        Standby MAC Address  # noqa: E501

        :return: The failover_standby_mac of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: str
        """
        return self._failover_standby_mac

    @failover_standby_mac.setter
    def failover_standby_mac(self, failover_standby_mac):
        """Sets the failover_standby_mac of this FTDHAInterfaceMACAddresses.

        Standby MAC Address  # noqa: E501

        :param failover_standby_mac: The failover_standby_mac of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: str
        """
        if failover_standby_mac is None:
            raise ValueError("Invalid value for `failover_standby_mac`, must not be `None`")  # noqa: E501

        self._failover_standby_mac = failover_standby_mac

    @property
    def physical_interface(self):
        """Gets the physical_interface of this FTDHAInterfaceMACAddresses.  # noqa: E501

        User chosen physical interface  # noqa: E501

        :return: The physical_interface of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: FTDBaseInterface
        """
        return self._physical_interface

    @physical_interface.setter
    def physical_interface(self, physical_interface):
        """Sets the physical_interface of this FTDHAInterfaceMACAddresses.

        User chosen physical interface  # noqa: E501

        :param physical_interface: The physical_interface of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: FTDBaseInterface
        """
        if physical_interface is None:
            raise ValueError("Invalid value for `physical_interface`, must not be `None`")  # noqa: E501

        self._physical_interface = physical_interface

    @property
    def name(self):
        """Gets the name of this FTDHAInterfaceMACAddresses.  # noqa: E501

        System chosen name  # noqa: E501

        :return: The name of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FTDHAInterfaceMACAddresses.

        System chosen name  # noqa: E501

        :param name: The name of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FTDHAInterfaceMACAddresses.  # noqa: E501

        User provided resource description  # noqa: E501

        :return: The description of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FTDHAInterfaceMACAddresses.

        User provided resource description  # noqa: E501

        :param description: The description of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this FTDHAInterfaceMACAddresses.  # noqa: E501

        Object containing related links  # noqa: E501

        :return: The links of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FTDHAInterfaceMACAddresses.

        Object containing related links  # noqa: E501

        :param links: The links of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this FTDHAInterfaceMACAddresses.  # noqa: E501

        Identifier of a Firepower Threat Defense high availability failover interface MAC address  # noqa: E501

        :return: The id of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FTDHAInterfaceMACAddresses.

        Identifier of a Firepower Threat Defense high availability failover interface MAC address  # noqa: E501

        :param id: The id of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this FTDHAInterfaceMACAddresses.  # noqa: E501

        Type of the Firepower Threat Defense high availability failover interface MAC address  # noqa: E501

        :return: The type of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FTDHAInterfaceMACAddresses.

        Type of the Firepower Threat Defense high availability failover interface MAC address  # noqa: E501

        :param type: The type of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this FTDHAInterfaceMACAddresses.  # noqa: E501

        version  # noqa: E501

        :return: The version of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FTDHAInterfaceMACAddresses.

        version  # noqa: E501

        :param version: The version of this FTDHAInterfaceMACAddresses.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(FTDHAInterfaceMACAddresses, dict):
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
        if not isinstance(other, FTDHAInterfaceMACAddresses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
