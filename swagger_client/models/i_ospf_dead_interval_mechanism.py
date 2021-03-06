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


class IOspfDeadIntervalMechanism(object):
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
        'dead_interval': 'int',
        'hello_interval': 'int',
        'neighbor_detection_type': 'str'
    }

    attribute_map = {
        'dead_interval': 'deadInterval',
        'hello_interval': 'helloInterval',
        'neighbor_detection_type': 'neighborDetectionType'
    }

    def __init__(self, dead_interval=None, hello_interval=None, neighbor_detection_type=None):  # noqa: E501
        """IOspfDeadIntervalMechanism - a model defined in Swagger"""  # noqa: E501

        self._dead_interval = None
        self._hello_interval = None
        self._neighbor_detection_type = None
        self.discriminator = None

        if dead_interval is not None:
            self.dead_interval = dead_interval
        if hello_interval is not None:
            self.hello_interval = hello_interval
        if neighbor_detection_type is not None:
            self.neighbor_detection_type = neighbor_detection_type

    @property
    def dead_interval(self):
        """Gets the dead_interval of this IOspfDeadIntervalMechanism.  # noqa: E501


        :return: The dead_interval of this IOspfDeadIntervalMechanism.  # noqa: E501
        :rtype: int
        """
        return self._dead_interval

    @dead_interval.setter
    def dead_interval(self, dead_interval):
        """Sets the dead_interval of this IOspfDeadIntervalMechanism.


        :param dead_interval: The dead_interval of this IOspfDeadIntervalMechanism.  # noqa: E501
        :type: int
        """

        self._dead_interval = dead_interval

    @property
    def hello_interval(self):
        """Gets the hello_interval of this IOspfDeadIntervalMechanism.  # noqa: E501


        :return: The hello_interval of this IOspfDeadIntervalMechanism.  # noqa: E501
        :rtype: int
        """
        return self._hello_interval

    @hello_interval.setter
    def hello_interval(self, hello_interval):
        """Sets the hello_interval of this IOspfDeadIntervalMechanism.


        :param hello_interval: The hello_interval of this IOspfDeadIntervalMechanism.  # noqa: E501
        :type: int
        """

        self._hello_interval = hello_interval

    @property
    def neighbor_detection_type(self):
        """Gets the neighbor_detection_type of this IOspfDeadIntervalMechanism.  # noqa: E501


        :return: The neighbor_detection_type of this IOspfDeadIntervalMechanism.  # noqa: E501
        :rtype: str
        """
        return self._neighbor_detection_type

    @neighbor_detection_type.setter
    def neighbor_detection_type(self, neighbor_detection_type):
        """Sets the neighbor_detection_type of this IOspfDeadIntervalMechanism.


        :param neighbor_detection_type: The neighbor_detection_type of this IOspfDeadIntervalMechanism.  # noqa: E501
        :type: str
        """

        self._neighbor_detection_type = neighbor_detection_type

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
        if issubclass(IOspfDeadIntervalMechanism, dict):
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
        if not isinstance(other, IOspfDeadIntervalMechanism):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
