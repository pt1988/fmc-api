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


class IStaticIPContainer(object):
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
        'address': 'str',
        'netmask': 'str'
    }

    attribute_map = {
        'address': 'address',
        'netmask': 'netmask'
    }

    def __init__(self, address=None, netmask=None):  # noqa: E501
        """IStaticIPContainer - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._netmask = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if netmask is not None:
            self.netmask = netmask

    @property
    def address(self):
        """Gets the address of this IStaticIPContainer.  # noqa: E501


        :return: The address of this IStaticIPContainer.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IStaticIPContainer.


        :param address: The address of this IStaticIPContainer.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def netmask(self):
        """Gets the netmask of this IStaticIPContainer.  # noqa: E501


        :return: The netmask of this IStaticIPContainer.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this IStaticIPContainer.


        :param netmask: The netmask of this IStaticIPContainer.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

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
        if issubclass(IStaticIPContainer, dict):
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
        if not isinstance(other, IStaticIPContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other