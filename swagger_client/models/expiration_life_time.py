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


class ExpirationLifeTime(object):
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
        'prefer_date_time': 'str',
        'valid_date_time': 'str'
    }

    attribute_map = {
        'prefer_date_time': 'preferDateTime',
        'valid_date_time': 'validDateTime'
    }

    def __init__(self, prefer_date_time=None, valid_date_time=None):  # noqa: E501
        """ExpirationLifeTime - a model defined in Swagger"""  # noqa: E501

        self._prefer_date_time = None
        self._valid_date_time = None
        self.discriminator = None

        if prefer_date_time is not None:
            self.prefer_date_time = prefer_date_time
        if valid_date_time is not None:
            self.valid_date_time = valid_date_time

    @property
    def prefer_date_time(self):
        """Gets the prefer_date_time of this ExpirationLifeTime.  # noqa: E501


        :return: The prefer_date_time of this ExpirationLifeTime.  # noqa: E501
        :rtype: str
        """
        return self._prefer_date_time

    @prefer_date_time.setter
    def prefer_date_time(self, prefer_date_time):
        """Sets the prefer_date_time of this ExpirationLifeTime.


        :param prefer_date_time: The prefer_date_time of this ExpirationLifeTime.  # noqa: E501
        :type: str
        """

        self._prefer_date_time = prefer_date_time

    @property
    def valid_date_time(self):
        """Gets the valid_date_time of this ExpirationLifeTime.  # noqa: E501


        :return: The valid_date_time of this ExpirationLifeTime.  # noqa: E501
        :rtype: str
        """
        return self._valid_date_time

    @valid_date_time.setter
    def valid_date_time(self, valid_date_time):
        """Sets the valid_date_time of this ExpirationLifeTime.


        :param valid_date_time: The valid_date_time of this ExpirationLifeTime.  # noqa: E501
        :type: str
        """

        self._valid_date_time = valid_date_time

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
        if issubclass(ExpirationLifeTime, dict):
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
        if not isinstance(other, ExpirationLifeTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
