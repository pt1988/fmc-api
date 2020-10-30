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


class IOspfv3Area(object):
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
        'default_cost': 'int',
        'route_summary': 'list[IOspfv3RouteSummary]',
        'area_id': 'str',
        'neighbors': 'IOspfv3Neighbor',
        'area_type': 'IOspfAreaType',
        'virtual_links': 'list[IOspfv3VirtualLinks]'
    }

    attribute_map = {
        'default_cost': 'defaultCost',
        'route_summary': 'routeSummary',
        'area_id': 'areaId',
        'neighbors': 'neighbors',
        'area_type': 'areaType',
        'virtual_links': 'virtualLinks'
    }

    def __init__(self, default_cost=None, route_summary=None, area_id=None, neighbors=None, area_type=None, virtual_links=None):  # noqa: E501
        """IOspfv3Area - a model defined in Swagger"""  # noqa: E501

        self._default_cost = None
        self._route_summary = None
        self._area_id = None
        self._neighbors = None
        self._area_type = None
        self._virtual_links = None
        self.discriminator = None

        if default_cost is not None:
            self.default_cost = default_cost
        if route_summary is not None:
            self.route_summary = route_summary
        if area_id is not None:
            self.area_id = area_id
        if neighbors is not None:
            self.neighbors = neighbors
        if area_type is not None:
            self.area_type = area_type
        if virtual_links is not None:
            self.virtual_links = virtual_links

    @property
    def default_cost(self):
        """Gets the default_cost of this IOspfv3Area.  # noqa: E501


        :return: The default_cost of this IOspfv3Area.  # noqa: E501
        :rtype: int
        """
        return self._default_cost

    @default_cost.setter
    def default_cost(self, default_cost):
        """Sets the default_cost of this IOspfv3Area.


        :param default_cost: The default_cost of this IOspfv3Area.  # noqa: E501
        :type: int
        """

        self._default_cost = default_cost

    @property
    def route_summary(self):
        """Gets the route_summary of this IOspfv3Area.  # noqa: E501


        :return: The route_summary of this IOspfv3Area.  # noqa: E501
        :rtype: list[IOspfv3RouteSummary]
        """
        return self._route_summary

    @route_summary.setter
    def route_summary(self, route_summary):
        """Sets the route_summary of this IOspfv3Area.


        :param route_summary: The route_summary of this IOspfv3Area.  # noqa: E501
        :type: list[IOspfv3RouteSummary]
        """

        self._route_summary = route_summary

    @property
    def area_id(self):
        """Gets the area_id of this IOspfv3Area.  # noqa: E501


        :return: The area_id of this IOspfv3Area.  # noqa: E501
        :rtype: str
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this IOspfv3Area.


        :param area_id: The area_id of this IOspfv3Area.  # noqa: E501
        :type: str
        """

        self._area_id = area_id

    @property
    def neighbors(self):
        """Gets the neighbors of this IOspfv3Area.  # noqa: E501


        :return: The neighbors of this IOspfv3Area.  # noqa: E501
        :rtype: IOspfv3Neighbor
        """
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors):
        """Sets the neighbors of this IOspfv3Area.


        :param neighbors: The neighbors of this IOspfv3Area.  # noqa: E501
        :type: IOspfv3Neighbor
        """

        self._neighbors = neighbors

    @property
    def area_type(self):
        """Gets the area_type of this IOspfv3Area.  # noqa: E501


        :return: The area_type of this IOspfv3Area.  # noqa: E501
        :rtype: IOspfAreaType
        """
        return self._area_type

    @area_type.setter
    def area_type(self, area_type):
        """Sets the area_type of this IOspfv3Area.


        :param area_type: The area_type of this IOspfv3Area.  # noqa: E501
        :type: IOspfAreaType
        """

        self._area_type = area_type

    @property
    def virtual_links(self):
        """Gets the virtual_links of this IOspfv3Area.  # noqa: E501


        :return: The virtual_links of this IOspfv3Area.  # noqa: E501
        :rtype: list[IOspfv3VirtualLinks]
        """
        return self._virtual_links

    @virtual_links.setter
    def virtual_links(self, virtual_links):
        """Sets the virtual_links of this IOspfv3Area.


        :param virtual_links: The virtual_links of this IOspfv3Area.  # noqa: E501
        :type: list[IOspfv3VirtualLinks]
        """

        self._virtual_links = virtual_links

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
        if issubclass(IOspfv3Area, dict):
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
        if not isinstance(other, IOspfv3Area):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
