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


class IValueDelete(object):
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
        'field_name': 'str',
        'old_value': 'str'
    }

    attribute_map = {
        'field_name': 'fieldName',
        'old_value': 'oldValue'
    }

    def __init__(self, field_name=None, old_value=None):  # noqa: E501
        """IValueDelete - a model defined in Swagger"""  # noqa: E501

        self._field_name = None
        self._old_value = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if old_value is not None:
            self.old_value = old_value

    @property
    def field_name(self):
        """Gets the field_name of this IValueDelete.  # noqa: E501


        :return: The field_name of this IValueDelete.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this IValueDelete.


        :param field_name: The field_name of this IValueDelete.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def old_value(self):
        """Gets the old_value of this IValueDelete.  # noqa: E501


        :return: The old_value of this IValueDelete.  # noqa: E501
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this IValueDelete.


        :param old_value: The old_value of this IValueDelete.  # noqa: E501
        :type: str
        """

        self._old_value = old_value

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
        if issubclass(IValueDelete, dict):
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
        if not isinstance(other, IValueDelete):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
