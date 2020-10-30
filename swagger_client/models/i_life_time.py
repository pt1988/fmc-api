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


class ILifeTime(object):
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
        'end_life_time_value': 'str',
        'start_life_time_value': 'str',
        'time_zone': 'str',
        'end_lifetime_type': 'str'
    }

    attribute_map = {
        'end_life_time_value': 'endLifeTimeValue',
        'start_life_time_value': 'startLifeTimeValue',
        'time_zone': 'timeZone',
        'end_lifetime_type': 'endLifetimeType'
    }

    def __init__(self, end_life_time_value=None, start_life_time_value=None, time_zone=None, end_lifetime_type=None):  # noqa: E501
        """ILifeTime - a model defined in Swagger"""  # noqa: E501

        self._end_life_time_value = None
        self._start_life_time_value = None
        self._time_zone = None
        self._end_lifetime_type = None
        self.discriminator = None

        if end_life_time_value is not None:
            self.end_life_time_value = end_life_time_value
        if start_life_time_value is not None:
            self.start_life_time_value = start_life_time_value
        if time_zone is not None:
            self.time_zone = time_zone
        if end_lifetime_type is not None:
            self.end_lifetime_type = end_lifetime_type

    @property
    def end_life_time_value(self):
        """Gets the end_life_time_value of this ILifeTime.  # noqa: E501


        :return: The end_life_time_value of this ILifeTime.  # noqa: E501
        :rtype: str
        """
        return self._end_life_time_value

    @end_life_time_value.setter
    def end_life_time_value(self, end_life_time_value):
        """Sets the end_life_time_value of this ILifeTime.


        :param end_life_time_value: The end_life_time_value of this ILifeTime.  # noqa: E501
        :type: str
        """

        self._end_life_time_value = end_life_time_value

    @property
    def start_life_time_value(self):
        """Gets the start_life_time_value of this ILifeTime.  # noqa: E501


        :return: The start_life_time_value of this ILifeTime.  # noqa: E501
        :rtype: str
        """
        return self._start_life_time_value

    @start_life_time_value.setter
    def start_life_time_value(self, start_life_time_value):
        """Sets the start_life_time_value of this ILifeTime.


        :param start_life_time_value: The start_life_time_value of this ILifeTime.  # noqa: E501
        :type: str
        """

        self._start_life_time_value = start_life_time_value

    @property
    def time_zone(self):
        """Gets the time_zone of this ILifeTime.  # noqa: E501


        :return: The time_zone of this ILifeTime.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ILifeTime.


        :param time_zone: The time_zone of this ILifeTime.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def end_lifetime_type(self):
        """Gets the end_lifetime_type of this ILifeTime.  # noqa: E501


        :return: The end_lifetime_type of this ILifeTime.  # noqa: E501
        :rtype: str
        """
        return self._end_lifetime_type

    @end_lifetime_type.setter
    def end_lifetime_type(self, end_lifetime_type):
        """Sets the end_lifetime_type of this ILifeTime.


        :param end_lifetime_type: The end_lifetime_type of this ILifeTime.  # noqa: E501
        :type: str
        """
        allowed_values = ["INFINITE", "DURATION", "DATETIME"]  # noqa: E501
        if end_lifetime_type not in allowed_values:
            raise ValueError(
                "Invalid value for `end_lifetime_type` ({0}), must be one of {1}"  # noqa: E501
                .format(end_lifetime_type, allowed_values)
            )

        self._end_lifetime_type = end_lifetime_type

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
        if issubclass(ILifeTime, dict):
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
        if not isinstance(other, ILifeTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
