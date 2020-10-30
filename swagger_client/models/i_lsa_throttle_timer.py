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


class ILsaThrottleTimer(object):
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
        'maximum_delay': 'int',
        'initial_delay': 'int',
        'minimum_delay': 'int'
    }

    attribute_map = {
        'maximum_delay': 'maximumDelay',
        'initial_delay': 'initialDelay',
        'minimum_delay': 'minimumDelay'
    }

    def __init__(self, maximum_delay=None, initial_delay=None, minimum_delay=None):  # noqa: E501
        """ILsaThrottleTimer - a model defined in Swagger"""  # noqa: E501

        self._maximum_delay = None
        self._initial_delay = None
        self._minimum_delay = None
        self.discriminator = None

        if maximum_delay is not None:
            self.maximum_delay = maximum_delay
        if initial_delay is not None:
            self.initial_delay = initial_delay
        if minimum_delay is not None:
            self.minimum_delay = minimum_delay

    @property
    def maximum_delay(self):
        """Gets the maximum_delay of this ILsaThrottleTimer.  # noqa: E501


        :return: The maximum_delay of this ILsaThrottleTimer.  # noqa: E501
        :rtype: int
        """
        return self._maximum_delay

    @maximum_delay.setter
    def maximum_delay(self, maximum_delay):
        """Sets the maximum_delay of this ILsaThrottleTimer.


        :param maximum_delay: The maximum_delay of this ILsaThrottleTimer.  # noqa: E501
        :type: int
        """

        self._maximum_delay = maximum_delay

    @property
    def initial_delay(self):
        """Gets the initial_delay of this ILsaThrottleTimer.  # noqa: E501


        :return: The initial_delay of this ILsaThrottleTimer.  # noqa: E501
        :rtype: int
        """
        return self._initial_delay

    @initial_delay.setter
    def initial_delay(self, initial_delay):
        """Sets the initial_delay of this ILsaThrottleTimer.


        :param initial_delay: The initial_delay of this ILsaThrottleTimer.  # noqa: E501
        :type: int
        """

        self._initial_delay = initial_delay

    @property
    def minimum_delay(self):
        """Gets the minimum_delay of this ILsaThrottleTimer.  # noqa: E501


        :return: The minimum_delay of this ILsaThrottleTimer.  # noqa: E501
        :rtype: int
        """
        return self._minimum_delay

    @minimum_delay.setter
    def minimum_delay(self, minimum_delay):
        """Sets the minimum_delay of this ILsaThrottleTimer.


        :param minimum_delay: The minimum_delay of this ILsaThrottleTimer.  # noqa: E501
        :type: int
        """

        self._minimum_delay = minimum_delay

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
        if issubclass(ILsaThrottleTimer, dict):
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
        if not isinstance(other, ILsaThrottleTimer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
