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


class IIkeKeepaliveSettings(object):
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
        'threshold': 'int',
        'retry_interval': 'int',
        'ike_keepalive': 'str'
    }

    attribute_map = {
        'threshold': 'threshold',
        'retry_interval': 'retryInterval',
        'ike_keepalive': 'ikeKeepalive'
    }

    def __init__(self, threshold=None, retry_interval=None, ike_keepalive=None):  # noqa: E501
        """IIkeKeepaliveSettings - a model defined in Swagger"""  # noqa: E501

        self._threshold = None
        self._retry_interval = None
        self._ike_keepalive = None
        self.discriminator = None

        if threshold is not None:
            self.threshold = threshold
        if retry_interval is not None:
            self.retry_interval = retry_interval
        if ike_keepalive is not None:
            self.ike_keepalive = ike_keepalive

    @property
    def threshold(self):
        """Gets the threshold of this IIkeKeepaliveSettings.  # noqa: E501


        :return: The threshold of this IIkeKeepaliveSettings.  # noqa: E501
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this IIkeKeepaliveSettings.


        :param threshold: The threshold of this IIkeKeepaliveSettings.  # noqa: E501
        :type: int
        """

        self._threshold = threshold

    @property
    def retry_interval(self):
        """Gets the retry_interval of this IIkeKeepaliveSettings.  # noqa: E501


        :return: The retry_interval of this IIkeKeepaliveSettings.  # noqa: E501
        :rtype: int
        """
        return self._retry_interval

    @retry_interval.setter
    def retry_interval(self, retry_interval):
        """Sets the retry_interval of this IIkeKeepaliveSettings.


        :param retry_interval: The retry_interval of this IIkeKeepaliveSettings.  # noqa: E501
        :type: int
        """

        self._retry_interval = retry_interval

    @property
    def ike_keepalive(self):
        """Gets the ike_keepalive of this IIkeKeepaliveSettings.  # noqa: E501


        :return: The ike_keepalive of this IIkeKeepaliveSettings.  # noqa: E501
        :rtype: str
        """
        return self._ike_keepalive

    @ike_keepalive.setter
    def ike_keepalive(self, ike_keepalive):
        """Sets the ike_keepalive of this IIkeKeepaliveSettings.


        :param ike_keepalive: The ike_keepalive of this IIkeKeepaliveSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["DISABLED", "ENABLED", "ENABLED_INFINITE"]  # noqa: E501
        if ike_keepalive not in allowed_values:
            raise ValueError(
                "Invalid value for `ike_keepalive` ({0}), must be one of {1}"  # noqa: E501
                .format(ike_keepalive, allowed_values)
            )

        self._ike_keepalive = ike_keepalive

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
        if issubclass(IIkeKeepaliveSettings, dict):
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
        if not isinstance(other, IIkeKeepaliveSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other