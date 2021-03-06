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


class IOspfSummaryAddresses(object):
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
        'tag_number': 'int',
        'summary_network': 'list[INetworkAddress]',
        'advertise': 'bool'
    }

    attribute_map = {
        'tag_number': 'tagNumber',
        'summary_network': 'summaryNetwork',
        'advertise': 'advertise'
    }

    def __init__(self, tag_number=None, summary_network=None, advertise=None):  # noqa: E501
        """IOspfSummaryAddresses - a model defined in Swagger"""  # noqa: E501

        self._tag_number = None
        self._summary_network = None
        self._advertise = None
        self.discriminator = None

        if tag_number is not None:
            self.tag_number = tag_number
        if summary_network is not None:
            self.summary_network = summary_network
        if advertise is not None:
            self.advertise = advertise

    @property
    def tag_number(self):
        """Gets the tag_number of this IOspfSummaryAddresses.  # noqa: E501


        :return: The tag_number of this IOspfSummaryAddresses.  # noqa: E501
        :rtype: int
        """
        return self._tag_number

    @tag_number.setter
    def tag_number(self, tag_number):
        """Sets the tag_number of this IOspfSummaryAddresses.


        :param tag_number: The tag_number of this IOspfSummaryAddresses.  # noqa: E501
        :type: int
        """

        self._tag_number = tag_number

    @property
    def summary_network(self):
        """Gets the summary_network of this IOspfSummaryAddresses.  # noqa: E501


        :return: The summary_network of this IOspfSummaryAddresses.  # noqa: E501
        :rtype: list[INetworkAddress]
        """
        return self._summary_network

    @summary_network.setter
    def summary_network(self, summary_network):
        """Sets the summary_network of this IOspfSummaryAddresses.


        :param summary_network: The summary_network of this IOspfSummaryAddresses.  # noqa: E501
        :type: list[INetworkAddress]
        """

        self._summary_network = summary_network

    @property
    def advertise(self):
        """Gets the advertise of this IOspfSummaryAddresses.  # noqa: E501


        :return: The advertise of this IOspfSummaryAddresses.  # noqa: E501
        :rtype: bool
        """
        return self._advertise

    @advertise.setter
    def advertise(self, advertise):
        """Sets the advertise of this IOspfSummaryAddresses.


        :param advertise: The advertise of this IOspfSummaryAddresses.  # noqa: E501
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
        if issubclass(IOspfSummaryAddresses, dict):
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
        if not isinstance(other, IOspfSummaryAddresses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
