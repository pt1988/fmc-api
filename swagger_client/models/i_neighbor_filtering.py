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


class INeighborFiltering(object):
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
        'neighbor_maximum_prefix': 'INeighborMaximumPrefix',
        'neighbor_distribute_lists': 'list[INeighborDistributeLists]',
        'neighbor_filter_list': 'list[INeighborFilterList]',
        'neighbor_route_map': 'list[INeighborRouteMap]',
        'name': 'str',
        'neighbor_default_originate': 'INeighborDefaultOriginate',
        'ipv6_prefix_list_filter': 'list[IIpvPrefixListFilter]',
        'links': 'ILinks',
        'id': 'str',
        'type': 'str',
        'ipv4_prefix_list_filter': 'list[IIpvPrefixListFilter]'
    }

    attribute_map = {
        'neighbor_maximum_prefix': 'neighborMaximumPrefix',
        'neighbor_distribute_lists': 'neighborDistributeLists',
        'neighbor_filter_list': 'neighborFilterList',
        'neighbor_route_map': 'neighborRouteMap',
        'name': 'name',
        'neighbor_default_originate': 'neighborDefaultOriginate',
        'ipv6_prefix_list_filter': 'ipv6PrefixListFilter',
        'links': 'links',
        'id': 'id',
        'type': 'type',
        'ipv4_prefix_list_filter': 'ipv4PrefixListFilter'
    }

    def __init__(self, neighbor_maximum_prefix=None, neighbor_distribute_lists=None, neighbor_filter_list=None, neighbor_route_map=None, name=None, neighbor_default_originate=None, ipv6_prefix_list_filter=None, links=None, id=None, type=None, ipv4_prefix_list_filter=None):  # noqa: E501
        """INeighborFiltering - a model defined in Swagger"""  # noqa: E501

        self._neighbor_maximum_prefix = None
        self._neighbor_distribute_lists = None
        self._neighbor_filter_list = None
        self._neighbor_route_map = None
        self._name = None
        self._neighbor_default_originate = None
        self._ipv6_prefix_list_filter = None
        self._links = None
        self._id = None
        self._type = None
        self._ipv4_prefix_list_filter = None
        self.discriminator = None

        if neighbor_maximum_prefix is not None:
            self.neighbor_maximum_prefix = neighbor_maximum_prefix
        if neighbor_distribute_lists is not None:
            self.neighbor_distribute_lists = neighbor_distribute_lists
        if neighbor_filter_list is not None:
            self.neighbor_filter_list = neighbor_filter_list
        if neighbor_route_map is not None:
            self.neighbor_route_map = neighbor_route_map
        if name is not None:
            self.name = name
        if neighbor_default_originate is not None:
            self.neighbor_default_originate = neighbor_default_originate
        if ipv6_prefix_list_filter is not None:
            self.ipv6_prefix_list_filter = ipv6_prefix_list_filter
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if ipv4_prefix_list_filter is not None:
            self.ipv4_prefix_list_filter = ipv4_prefix_list_filter

    @property
    def neighbor_maximum_prefix(self):
        """Gets the neighbor_maximum_prefix of this INeighborFiltering.  # noqa: E501


        :return: The neighbor_maximum_prefix of this INeighborFiltering.  # noqa: E501
        :rtype: INeighborMaximumPrefix
        """
        return self._neighbor_maximum_prefix

    @neighbor_maximum_prefix.setter
    def neighbor_maximum_prefix(self, neighbor_maximum_prefix):
        """Sets the neighbor_maximum_prefix of this INeighborFiltering.


        :param neighbor_maximum_prefix: The neighbor_maximum_prefix of this INeighborFiltering.  # noqa: E501
        :type: INeighborMaximumPrefix
        """

        self._neighbor_maximum_prefix = neighbor_maximum_prefix

    @property
    def neighbor_distribute_lists(self):
        """Gets the neighbor_distribute_lists of this INeighborFiltering.  # noqa: E501


        :return: The neighbor_distribute_lists of this INeighborFiltering.  # noqa: E501
        :rtype: list[INeighborDistributeLists]
        """
        return self._neighbor_distribute_lists

    @neighbor_distribute_lists.setter
    def neighbor_distribute_lists(self, neighbor_distribute_lists):
        """Sets the neighbor_distribute_lists of this INeighborFiltering.


        :param neighbor_distribute_lists: The neighbor_distribute_lists of this INeighborFiltering.  # noqa: E501
        :type: list[INeighborDistributeLists]
        """

        self._neighbor_distribute_lists = neighbor_distribute_lists

    @property
    def neighbor_filter_list(self):
        """Gets the neighbor_filter_list of this INeighborFiltering.  # noqa: E501


        :return: The neighbor_filter_list of this INeighborFiltering.  # noqa: E501
        :rtype: list[INeighborFilterList]
        """
        return self._neighbor_filter_list

    @neighbor_filter_list.setter
    def neighbor_filter_list(self, neighbor_filter_list):
        """Sets the neighbor_filter_list of this INeighborFiltering.


        :param neighbor_filter_list: The neighbor_filter_list of this INeighborFiltering.  # noqa: E501
        :type: list[INeighborFilterList]
        """

        self._neighbor_filter_list = neighbor_filter_list

    @property
    def neighbor_route_map(self):
        """Gets the neighbor_route_map of this INeighborFiltering.  # noqa: E501


        :return: The neighbor_route_map of this INeighborFiltering.  # noqa: E501
        :rtype: list[INeighborRouteMap]
        """
        return self._neighbor_route_map

    @neighbor_route_map.setter
    def neighbor_route_map(self, neighbor_route_map):
        """Sets the neighbor_route_map of this INeighborFiltering.


        :param neighbor_route_map: The neighbor_route_map of this INeighborFiltering.  # noqa: E501
        :type: list[INeighborRouteMap]
        """

        self._neighbor_route_map = neighbor_route_map

    @property
    def name(self):
        """Gets the name of this INeighborFiltering.  # noqa: E501


        :return: The name of this INeighborFiltering.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this INeighborFiltering.


        :param name: The name of this INeighborFiltering.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def neighbor_default_originate(self):
        """Gets the neighbor_default_originate of this INeighborFiltering.  # noqa: E501


        :return: The neighbor_default_originate of this INeighborFiltering.  # noqa: E501
        :rtype: INeighborDefaultOriginate
        """
        return self._neighbor_default_originate

    @neighbor_default_originate.setter
    def neighbor_default_originate(self, neighbor_default_originate):
        """Sets the neighbor_default_originate of this INeighborFiltering.


        :param neighbor_default_originate: The neighbor_default_originate of this INeighborFiltering.  # noqa: E501
        :type: INeighborDefaultOriginate
        """

        self._neighbor_default_originate = neighbor_default_originate

    @property
    def ipv6_prefix_list_filter(self):
        """Gets the ipv6_prefix_list_filter of this INeighborFiltering.  # noqa: E501


        :return: The ipv6_prefix_list_filter of this INeighborFiltering.  # noqa: E501
        :rtype: list[IIpvPrefixListFilter]
        """
        return self._ipv6_prefix_list_filter

    @ipv6_prefix_list_filter.setter
    def ipv6_prefix_list_filter(self, ipv6_prefix_list_filter):
        """Sets the ipv6_prefix_list_filter of this INeighborFiltering.


        :param ipv6_prefix_list_filter: The ipv6_prefix_list_filter of this INeighborFiltering.  # noqa: E501
        :type: list[IIpvPrefixListFilter]
        """

        self._ipv6_prefix_list_filter = ipv6_prefix_list_filter

    @property
    def links(self):
        """Gets the links of this INeighborFiltering.  # noqa: E501


        :return: The links of this INeighborFiltering.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this INeighborFiltering.


        :param links: The links of this INeighborFiltering.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this INeighborFiltering.  # noqa: E501


        :return: The id of this INeighborFiltering.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this INeighborFiltering.


        :param id: The id of this INeighborFiltering.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this INeighborFiltering.  # noqa: E501


        :return: The type of this INeighborFiltering.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this INeighborFiltering.


        :param type: The type of this INeighborFiltering.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def ipv4_prefix_list_filter(self):
        """Gets the ipv4_prefix_list_filter of this INeighborFiltering.  # noqa: E501


        :return: The ipv4_prefix_list_filter of this INeighborFiltering.  # noqa: E501
        :rtype: list[IIpvPrefixListFilter]
        """
        return self._ipv4_prefix_list_filter

    @ipv4_prefix_list_filter.setter
    def ipv4_prefix_list_filter(self, ipv4_prefix_list_filter):
        """Sets the ipv4_prefix_list_filter of this INeighborFiltering.


        :param ipv4_prefix_list_filter: The ipv4_prefix_list_filter of this INeighborFiltering.  # noqa: E501
        :type: list[IIpvPrefixListFilter]
        """

        self._ipv4_prefix_list_filter = ipv4_prefix_list_filter

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
        if issubclass(INeighborFiltering, dict):
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
        if not isinstance(other, INeighborFiltering):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
