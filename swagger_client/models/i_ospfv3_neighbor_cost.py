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


class IOspfv3NeighborCost(object):
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
        'cost': 'int',
        'filter_outgoing_lsa': 'bool'
    }

    attribute_map = {
        'cost': 'cost',
        'filter_outgoing_lsa': 'filterOutgoingLSA'
    }

    def __init__(self, cost=None, filter_outgoing_lsa=None):  # noqa: E501
        """IOspfv3NeighborCost - a model defined in Swagger"""  # noqa: E501

        self._cost = None
        self._filter_outgoing_lsa = None
        self.discriminator = None

        if cost is not None:
            self.cost = cost
        if filter_outgoing_lsa is not None:
            self.filter_outgoing_lsa = filter_outgoing_lsa

    @property
    def cost(self):
        """Gets the cost of this IOspfv3NeighborCost.  # noqa: E501


        :return: The cost of this IOspfv3NeighborCost.  # noqa: E501
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this IOspfv3NeighborCost.


        :param cost: The cost of this IOspfv3NeighborCost.  # noqa: E501
        :type: int
        """

        self._cost = cost

    @property
    def filter_outgoing_lsa(self):
        """Gets the filter_outgoing_lsa of this IOspfv3NeighborCost.  # noqa: E501


        :return: The filter_outgoing_lsa of this IOspfv3NeighborCost.  # noqa: E501
        :rtype: bool
        """
        return self._filter_outgoing_lsa

    @filter_outgoing_lsa.setter
    def filter_outgoing_lsa(self, filter_outgoing_lsa):
        """Sets the filter_outgoing_lsa of this IOspfv3NeighborCost.


        :param filter_outgoing_lsa: The filter_outgoing_lsa of this IOspfv3NeighborCost.  # noqa: E501
        :type: bool
        """

        self._filter_outgoing_lsa = filter_outgoing_lsa

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
        if issubclass(IOspfv3NeighborCost, dict):
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
        if not isinstance(other, IOspfv3NeighborCost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other