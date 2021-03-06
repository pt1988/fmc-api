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


class IOspfv3NeighborProperties(object):
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
        'neighbor_cost': 'IOspfv3NeighborCost',
        'neighbor_priority': 'IOspfv3NeighborPriority'
    }

    attribute_map = {
        'neighbor_cost': 'neighborCost',
        'neighbor_priority': 'neighborPriority'
    }

    def __init__(self, neighbor_cost=None, neighbor_priority=None):  # noqa: E501
        """IOspfv3NeighborProperties - a model defined in Swagger"""  # noqa: E501

        self._neighbor_cost = None
        self._neighbor_priority = None
        self.discriminator = None

        if neighbor_cost is not None:
            self.neighbor_cost = neighbor_cost
        if neighbor_priority is not None:
            self.neighbor_priority = neighbor_priority

    @property
    def neighbor_cost(self):
        """Gets the neighbor_cost of this IOspfv3NeighborProperties.  # noqa: E501


        :return: The neighbor_cost of this IOspfv3NeighborProperties.  # noqa: E501
        :rtype: IOspfv3NeighborCost
        """
        return self._neighbor_cost

    @neighbor_cost.setter
    def neighbor_cost(self, neighbor_cost):
        """Sets the neighbor_cost of this IOspfv3NeighborProperties.


        :param neighbor_cost: The neighbor_cost of this IOspfv3NeighborProperties.  # noqa: E501
        :type: IOspfv3NeighborCost
        """

        self._neighbor_cost = neighbor_cost

    @property
    def neighbor_priority(self):
        """Gets the neighbor_priority of this IOspfv3NeighborProperties.  # noqa: E501


        :return: The neighbor_priority of this IOspfv3NeighborProperties.  # noqa: E501
        :rtype: IOspfv3NeighborPriority
        """
        return self._neighbor_priority

    @neighbor_priority.setter
    def neighbor_priority(self, neighbor_priority):
        """Sets the neighbor_priority of this IOspfv3NeighborProperties.


        :param neighbor_priority: The neighbor_priority of this IOspfv3NeighborProperties.  # noqa: E501
        :type: IOspfv3NeighborPriority
        """

        self._neighbor_priority = neighbor_priority

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
        if issubclass(IOspfv3NeighborProperties, dict):
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
        if not isinstance(other, IOspfv3NeighborProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
