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


class INeighborHops(object):
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
        'neighbor_ttl_security_hops': 'int',
        'name': 'str',
        'max_hop_count': 'int',
        'links': 'ILinks',
        'disable_connected_check': 'bool',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'neighbor_ttl_security_hops': 'neighborTtlSecurityHops',
        'name': 'name',
        'max_hop_count': 'maxHopCount',
        'links': 'links',
        'disable_connected_check': 'disableConnectedCheck',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, neighbor_ttl_security_hops=None, name=None, max_hop_count=None, links=None, disable_connected_check=None, id=None, type=None):  # noqa: E501
        """INeighborHops - a model defined in Swagger"""  # noqa: E501

        self._neighbor_ttl_security_hops = None
        self._name = None
        self._max_hop_count = None
        self._links = None
        self._disable_connected_check = None
        self._id = None
        self._type = None
        self.discriminator = None

        if neighbor_ttl_security_hops is not None:
            self.neighbor_ttl_security_hops = neighbor_ttl_security_hops
        if name is not None:
            self.name = name
        if max_hop_count is not None:
            self.max_hop_count = max_hop_count
        if links is not None:
            self.links = links
        if disable_connected_check is not None:
            self.disable_connected_check = disable_connected_check
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def neighbor_ttl_security_hops(self):
        """Gets the neighbor_ttl_security_hops of this INeighborHops.  # noqa: E501


        :return: The neighbor_ttl_security_hops of this INeighborHops.  # noqa: E501
        :rtype: int
        """
        return self._neighbor_ttl_security_hops

    @neighbor_ttl_security_hops.setter
    def neighbor_ttl_security_hops(self, neighbor_ttl_security_hops):
        """Sets the neighbor_ttl_security_hops of this INeighborHops.


        :param neighbor_ttl_security_hops: The neighbor_ttl_security_hops of this INeighborHops.  # noqa: E501
        :type: int
        """

        self._neighbor_ttl_security_hops = neighbor_ttl_security_hops

    @property
    def name(self):
        """Gets the name of this INeighborHops.  # noqa: E501


        :return: The name of this INeighborHops.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this INeighborHops.


        :param name: The name of this INeighborHops.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def max_hop_count(self):
        """Gets the max_hop_count of this INeighborHops.  # noqa: E501


        :return: The max_hop_count of this INeighborHops.  # noqa: E501
        :rtype: int
        """
        return self._max_hop_count

    @max_hop_count.setter
    def max_hop_count(self, max_hop_count):
        """Sets the max_hop_count of this INeighborHops.


        :param max_hop_count: The max_hop_count of this INeighborHops.  # noqa: E501
        :type: int
        """

        self._max_hop_count = max_hop_count

    @property
    def links(self):
        """Gets the links of this INeighborHops.  # noqa: E501


        :return: The links of this INeighborHops.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this INeighborHops.


        :param links: The links of this INeighborHops.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def disable_connected_check(self):
        """Gets the disable_connected_check of this INeighborHops.  # noqa: E501


        :return: The disable_connected_check of this INeighborHops.  # noqa: E501
        :rtype: bool
        """
        return self._disable_connected_check

    @disable_connected_check.setter
    def disable_connected_check(self, disable_connected_check):
        """Sets the disable_connected_check of this INeighborHops.


        :param disable_connected_check: The disable_connected_check of this INeighborHops.  # noqa: E501
        :type: bool
        """

        self._disable_connected_check = disable_connected_check

    @property
    def id(self):
        """Gets the id of this INeighborHops.  # noqa: E501


        :return: The id of this INeighborHops.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this INeighborHops.


        :param id: The id of this INeighborHops.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this INeighborHops.  # noqa: E501


        :return: The type of this INeighborHops.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this INeighborHops.


        :param type: The type of this INeighborHops.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(INeighborHops, dict):
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
        if not isinstance(other, INeighborHops):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
