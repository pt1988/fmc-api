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


class IOspfv3SummaryPrefix(object):
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
        'tag': 'str',
        'ipv6_prefix': 'INetworkAddress',
        'advertise': 'bool'
    }

    attribute_map = {
        'tag': 'tag',
        'ipv6_prefix': 'ipv6Prefix',
        'advertise': 'advertise'
    }

    def __init__(self, tag=None, ipv6_prefix=None, advertise=None):  # noqa: E501
        """IOspfv3SummaryPrefix - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._ipv6_prefix = None
        self._advertise = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if ipv6_prefix is not None:
            self.ipv6_prefix = ipv6_prefix
        if advertise is not None:
            self.advertise = advertise

    @property
    def tag(self):
        """Gets the tag of this IOspfv3SummaryPrefix.  # noqa: E501


        :return: The tag of this IOspfv3SummaryPrefix.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this IOspfv3SummaryPrefix.


        :param tag: The tag of this IOspfv3SummaryPrefix.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def ipv6_prefix(self):
        """Gets the ipv6_prefix of this IOspfv3SummaryPrefix.  # noqa: E501


        :return: The ipv6_prefix of this IOspfv3SummaryPrefix.  # noqa: E501
        :rtype: INetworkAddress
        """
        return self._ipv6_prefix

    @ipv6_prefix.setter
    def ipv6_prefix(self, ipv6_prefix):
        """Sets the ipv6_prefix of this IOspfv3SummaryPrefix.


        :param ipv6_prefix: The ipv6_prefix of this IOspfv3SummaryPrefix.  # noqa: E501
        :type: INetworkAddress
        """

        self._ipv6_prefix = ipv6_prefix

    @property
    def advertise(self):
        """Gets the advertise of this IOspfv3SummaryPrefix.  # noqa: E501


        :return: The advertise of this IOspfv3SummaryPrefix.  # noqa: E501
        :rtype: bool
        """
        return self._advertise

    @advertise.setter
    def advertise(self, advertise):
        """Sets the advertise of this IOspfv3SummaryPrefix.


        :param advertise: The advertise of this IOspfv3SummaryPrefix.  # noqa: E501
        :type: bool
        """

        self._advertise = advertise

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
        if issubclass(IOspfv3SummaryPrefix, dict):
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
        if not isinstance(other, IOspfv3SummaryPrefix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
