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


class INeighborHaMode(object):
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
        'disable': 'bool',
        'name': 'str',
        'links': 'ILinks',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'disable': 'disable',
        'name': 'name',
        'links': 'links',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, disable=None, name=None, links=None, id=None, type=None):  # noqa: E501
        """INeighborHaMode - a model defined in Swagger"""  # noqa: E501

        self._disable = None
        self._name = None
        self._links = None
        self._id = None
        self._type = None
        self.discriminator = None

        if disable is not None:
            self.disable = disable
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def disable(self):
        """Gets the disable of this INeighborHaMode.  # noqa: E501


        :return: The disable of this INeighborHaMode.  # noqa: E501
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        """Sets the disable of this INeighborHaMode.


        :param disable: The disable of this INeighborHaMode.  # noqa: E501
        :type: bool
        """

        self._disable = disable

    @property
    def name(self):
        """Gets the name of this INeighborHaMode.  # noqa: E501


        :return: The name of this INeighborHaMode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this INeighborHaMode.


        :param name: The name of this INeighborHaMode.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this INeighborHaMode.  # noqa: E501


        :return: The links of this INeighborHaMode.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this INeighborHaMode.


        :param links: The links of this INeighborHaMode.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this INeighborHaMode.  # noqa: E501


        :return: The id of this INeighborHaMode.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this INeighborHaMode.


        :param id: The id of this INeighborHaMode.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this INeighborHaMode.  # noqa: E501


        :return: The type of this INeighborHaMode.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this INeighborHaMode.


        :param type: The type of this INeighborHaMode.  # noqa: E501
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
        if issubclass(INeighborHaMode, dict):
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
        if not isinstance(other, INeighborHaMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
