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


class INeighborAdvanced(object):
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
        'neighbor_transport_connection_mode': 'INeighborTransportConnectionMode',
        'neighbor_secret': 'str',
        'neighbor_version': 'int',
        'neighbor_transport_path_mtu_discovery': 'INeighborTransportPathMTUDiscovery',
        'next_hop_self': 'bool',
        'name': 'str',
        'links': 'ILinks',
        'neighbor_hops': 'INeighborHops',
        'id': 'str',
        'neighbor_weight': 'int',
        'type': 'str',
        'send_community': 'bool'
    }

    attribute_map = {
        'neighbor_transport_connection_mode': 'neighborTransportConnectionMode',
        'neighbor_secret': 'neighborSecret',
        'neighbor_version': 'neighborVersion',
        'neighbor_transport_path_mtu_discovery': 'neighborTransportPathMTUDiscovery',
        'next_hop_self': 'nextHopSelf',
        'name': 'name',
        'links': 'links',
        'neighbor_hops': 'neighborHops',
        'id': 'id',
        'neighbor_weight': 'neighborWeight',
        'type': 'type',
        'send_community': 'sendCommunity'
    }

    def __init__(self, neighbor_transport_connection_mode=None, neighbor_secret=None, neighbor_version=None, neighbor_transport_path_mtu_discovery=None, next_hop_self=None, name=None, links=None, neighbor_hops=None, id=None, neighbor_weight=None, type=None, send_community=None):  # noqa: E501
        """INeighborAdvanced - a model defined in Swagger"""  # noqa: E501

        self._neighbor_transport_connection_mode = None
        self._neighbor_secret = None
        self._neighbor_version = None
        self._neighbor_transport_path_mtu_discovery = None
        self._next_hop_self = None
        self._name = None
        self._links = None
        self._neighbor_hops = None
        self._id = None
        self._neighbor_weight = None
        self._type = None
        self._send_community = None
        self.discriminator = None

        if neighbor_transport_connection_mode is not None:
            self.neighbor_transport_connection_mode = neighbor_transport_connection_mode
        if neighbor_secret is not None:
            self.neighbor_secret = neighbor_secret
        if neighbor_version is not None:
            self.neighbor_version = neighbor_version
        if neighbor_transport_path_mtu_discovery is not None:
            self.neighbor_transport_path_mtu_discovery = neighbor_transport_path_mtu_discovery
        if next_hop_self is not None:
            self.next_hop_self = next_hop_self
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if neighbor_hops is not None:
            self.neighbor_hops = neighbor_hops
        if id is not None:
            self.id = id
        if neighbor_weight is not None:
            self.neighbor_weight = neighbor_weight
        if type is not None:
            self.type = type
        if send_community is not None:
            self.send_community = send_community

    @property
    def neighbor_transport_connection_mode(self):
        """Gets the neighbor_transport_connection_mode of this INeighborAdvanced.  # noqa: E501


        :return: The neighbor_transport_connection_mode of this INeighborAdvanced.  # noqa: E501
        :rtype: INeighborTransportConnectionMode
        """
        return self._neighbor_transport_connection_mode

    @neighbor_transport_connection_mode.setter
    def neighbor_transport_connection_mode(self, neighbor_transport_connection_mode):
        """Sets the neighbor_transport_connection_mode of this INeighborAdvanced.


        :param neighbor_transport_connection_mode: The neighbor_transport_connection_mode of this INeighborAdvanced.  # noqa: E501
        :type: INeighborTransportConnectionMode
        """

        self._neighbor_transport_connection_mode = neighbor_transport_connection_mode

    @property
    def neighbor_secret(self):
        """Gets the neighbor_secret of this INeighborAdvanced.  # noqa: E501


        :return: The neighbor_secret of this INeighborAdvanced.  # noqa: E501
        :rtype: str
        """
        return self._neighbor_secret

    @neighbor_secret.setter
    def neighbor_secret(self, neighbor_secret):
        """Sets the neighbor_secret of this INeighborAdvanced.


        :param neighbor_secret: The neighbor_secret of this INeighborAdvanced.  # noqa: E501
        :type: str
        """

        self._neighbor_secret = neighbor_secret

    @property
    def neighbor_version(self):
        """Gets the neighbor_version of this INeighborAdvanced.  # noqa: E501


        :return: The neighbor_version of this INeighborAdvanced.  # noqa: E501
        :rtype: int
        """
        return self._neighbor_version

    @neighbor_version.setter
    def neighbor_version(self, neighbor_version):
        """Sets the neighbor_version of this INeighborAdvanced.


        :param neighbor_version: The neighbor_version of this INeighborAdvanced.  # noqa: E501
        :type: int
        """

        self._neighbor_version = neighbor_version

    @property
    def neighbor_transport_path_mtu_discovery(self):
        """Gets the neighbor_transport_path_mtu_discovery of this INeighborAdvanced.  # noqa: E501


        :return: The neighbor_transport_path_mtu_discovery of this INeighborAdvanced.  # noqa: E501
        :rtype: INeighborTransportPathMTUDiscovery
        """
        return self._neighbor_transport_path_mtu_discovery

    @neighbor_transport_path_mtu_discovery.setter
    def neighbor_transport_path_mtu_discovery(self, neighbor_transport_path_mtu_discovery):
        """Sets the neighbor_transport_path_mtu_discovery of this INeighborAdvanced.


        :param neighbor_transport_path_mtu_discovery: The neighbor_transport_path_mtu_discovery of this INeighborAdvanced.  # noqa: E501
        :type: INeighborTransportPathMTUDiscovery
        """

        self._neighbor_transport_path_mtu_discovery = neighbor_transport_path_mtu_discovery

    @property
    def next_hop_self(self):
        """Gets the next_hop_self of this INeighborAdvanced.  # noqa: E501


        :return: The next_hop_self of this INeighborAdvanced.  # noqa: E501
        :rtype: bool
        """
        return self._next_hop_self

    @next_hop_self.setter
    def next_hop_self(self, next_hop_self):
        """Sets the next_hop_self of this INeighborAdvanced.


        :param next_hop_self: The next_hop_self of this INeighborAdvanced.  # noqa: E501
        :type: bool
        """

        self._next_hop_self = next_hop_self

    @property
    def name(self):
        """Gets the name of this INeighborAdvanced.  # noqa: E501


        :return: The name of this INeighborAdvanced.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this INeighborAdvanced.


        :param name: The name of this INeighborAdvanced.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this INeighborAdvanced.  # noqa: E501


        :return: The links of this INeighborAdvanced.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this INeighborAdvanced.


        :param links: The links of this INeighborAdvanced.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def neighbor_hops(self):
        """Gets the neighbor_hops of this INeighborAdvanced.  # noqa: E501


        :return: The neighbor_hops of this INeighborAdvanced.  # noqa: E501
        :rtype: INeighborHops
        """
        return self._neighbor_hops

    @neighbor_hops.setter
    def neighbor_hops(self, neighbor_hops):
        """Sets the neighbor_hops of this INeighborAdvanced.


        :param neighbor_hops: The neighbor_hops of this INeighborAdvanced.  # noqa: E501
        :type: INeighborHops
        """

        self._neighbor_hops = neighbor_hops

    @property
    def id(self):
        """Gets the id of this INeighborAdvanced.  # noqa: E501


        :return: The id of this INeighborAdvanced.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this INeighborAdvanced.


        :param id: The id of this INeighborAdvanced.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def neighbor_weight(self):
        """Gets the neighbor_weight of this INeighborAdvanced.  # noqa: E501


        :return: The neighbor_weight of this INeighborAdvanced.  # noqa: E501
        :rtype: int
        """
        return self._neighbor_weight

    @neighbor_weight.setter
    def neighbor_weight(self, neighbor_weight):
        """Sets the neighbor_weight of this INeighborAdvanced.


        :param neighbor_weight: The neighbor_weight of this INeighborAdvanced.  # noqa: E501
        :type: int
        """

        self._neighbor_weight = neighbor_weight

    @property
    def type(self):
        """Gets the type of this INeighborAdvanced.  # noqa: E501


        :return: The type of this INeighborAdvanced.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this INeighborAdvanced.


        :param type: The type of this INeighborAdvanced.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def send_community(self):
        """Gets the send_community of this INeighborAdvanced.  # noqa: E501


        :return: The send_community of this INeighborAdvanced.  # noqa: E501
        :rtype: bool
        """
        return self._send_community

    @send_community.setter
    def send_community(self, send_community):
        """Sets the send_community of this INeighborAdvanced.


        :param send_community: The send_community of this INeighborAdvanced.  # noqa: E501
        :type: bool
        """

        self._send_community = send_community

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
        if issubclass(INeighborAdvanced, dict):
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
        if not isinstance(other, INeighborAdvanced):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other