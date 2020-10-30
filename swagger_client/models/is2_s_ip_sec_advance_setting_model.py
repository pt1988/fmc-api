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


class IS2SIpSecAdvanceSettingModel(object):
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
        'enable_fragmentation_before_encryption': 'bool',
        'maximum_transmission_unit_aging': 'IMaximumTransmissionUnitAging'
    }

    attribute_map = {
        'enable_fragmentation_before_encryption': 'enableFragmentationBeforeEncryption',
        'maximum_transmission_unit_aging': 'maximumTransmissionUnitAging'
    }

    def __init__(self, enable_fragmentation_before_encryption=None, maximum_transmission_unit_aging=None):  # noqa: E501
        """IS2SIpSecAdvanceSettingModel - a model defined in Swagger"""  # noqa: E501

        self._enable_fragmentation_before_encryption = None
        self._maximum_transmission_unit_aging = None
        self.discriminator = None

        if enable_fragmentation_before_encryption is not None:
            self.enable_fragmentation_before_encryption = enable_fragmentation_before_encryption
        if maximum_transmission_unit_aging is not None:
            self.maximum_transmission_unit_aging = maximum_transmission_unit_aging

    @property
    def enable_fragmentation_before_encryption(self):
        """Gets the enable_fragmentation_before_encryption of this IS2SIpSecAdvanceSettingModel.  # noqa: E501

        Indicates whether to enable transmission unit fragmentation before encryption.  # noqa: E501

        :return: The enable_fragmentation_before_encryption of this IS2SIpSecAdvanceSettingModel.  # noqa: E501
        :rtype: bool
        """
        return self._enable_fragmentation_before_encryption

    @enable_fragmentation_before_encryption.setter
    def enable_fragmentation_before_encryption(self, enable_fragmentation_before_encryption):
        """Sets the enable_fragmentation_before_encryption of this IS2SIpSecAdvanceSettingModel.

        Indicates whether to enable transmission unit fragmentation before encryption.  # noqa: E501

        :param enable_fragmentation_before_encryption: The enable_fragmentation_before_encryption of this IS2SIpSecAdvanceSettingModel.  # noqa: E501
        :type: bool
        """

        self._enable_fragmentation_before_encryption = enable_fragmentation_before_encryption

    @property
    def maximum_transmission_unit_aging(self):
        """Gets the maximum_transmission_unit_aging of this IS2SIpSecAdvanceSettingModel.  # noqa: E501

        Duration of the MTU aging window.  # noqa: E501

        :return: The maximum_transmission_unit_aging of this IS2SIpSecAdvanceSettingModel.  # noqa: E501
        :rtype: IMaximumTransmissionUnitAging
        """
        return self._maximum_transmission_unit_aging

    @maximum_transmission_unit_aging.setter
    def maximum_transmission_unit_aging(self, maximum_transmission_unit_aging):
        """Sets the maximum_transmission_unit_aging of this IS2SIpSecAdvanceSettingModel.

        Duration of the MTU aging window.  # noqa: E501

        :param maximum_transmission_unit_aging: The maximum_transmission_unit_aging of this IS2SIpSecAdvanceSettingModel.  # noqa: E501
        :type: IMaximumTransmissionUnitAging
        """

        self._maximum_transmission_unit_aging = maximum_transmission_unit_aging

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
        if issubclass(IS2SIpSecAdvanceSettingModel, dict):
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
        if not isinstance(other, IS2SIpSecAdvanceSettingModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
