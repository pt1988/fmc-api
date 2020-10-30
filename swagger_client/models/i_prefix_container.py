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


class IPrefixContainer(object):
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
        'default': 'bool',
        'address': 'str',
        'advertisement': 'IAdvertisement'
    }

    attribute_map = {
        'default': 'default',
        'address': 'address',
        'advertisement': 'advertisement'
    }

    def __init__(self, default=None, address=None, advertisement=None):  # noqa: E501
        """IPrefixContainer - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._address = None
        self._advertisement = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if address is not None:
            self.address = address
        if advertisement is not None:
            self.advertisement = advertisement

    @property
    def default(self):
        """Gets the default of this IPrefixContainer.  # noqa: E501


        :return: The default of this IPrefixContainer.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this IPrefixContainer.


        :param default: The default of this IPrefixContainer.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def address(self):
        """Gets the address of this IPrefixContainer.  # noqa: E501


        :return: The address of this IPrefixContainer.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IPrefixContainer.


        :param address: The address of this IPrefixContainer.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def advertisement(self):
        """Gets the advertisement of this IPrefixContainer.  # noqa: E501


        :return: The advertisement of this IPrefixContainer.  # noqa: E501
        :rtype: IAdvertisement
        """
        return self._advertisement

    @advertisement.setter
    def advertisement(self, advertisement):
        """Sets the advertisement of this IPrefixContainer.


        :param advertisement: The advertisement of this IPrefixContainer.  # noqa: E501
        :type: IAdvertisement
        """

        self._advertisement = advertisement

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
        if issubclass(IPrefixContainer, dict):
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
        if not isinstance(other, IPrefixContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
