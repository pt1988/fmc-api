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


class IOspfLogAdjChanges(object):
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
        'log_type': 'str'
    }

    attribute_map = {
        'log_type': 'logType'
    }

    def __init__(self, log_type=None):  # noqa: E501
        """IOspfLogAdjChanges - a model defined in Swagger"""  # noqa: E501

        self._log_type = None
        self.discriminator = None

        if log_type is not None:
            self.log_type = log_type

    @property
    def log_type(self):
        """Gets the log_type of this IOspfLogAdjChanges.  # noqa: E501


        :return: The log_type of this IOspfLogAdjChanges.  # noqa: E501
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this IOspfLogAdjChanges.


        :param log_type: The log_type of this IOspfLogAdjChanges.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "DETAILED"]  # noqa: E501
        if log_type not in allowed_values:
            raise ValueError(
                "Invalid value for `log_type` ({0}), must be one of {1}"  # noqa: E501
                .format(log_type, allowed_values)
            )

        self._log_type = log_type

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
        if issubclass(IOspfLogAdjChanges, dict):
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
        if not isinstance(other, IOspfLogAdjChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
