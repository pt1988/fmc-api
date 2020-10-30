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


class DeviceCopyConfigRequest(object):
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
        'copy_shared_policies': 'bool',
        'target_device_list': 'list[ITarget]',
        'source_device': 'ITarget'
    }

    attribute_map = {
        'copy_shared_policies': 'copySharedPolicies',
        'target_device_list': 'targetDeviceList',
        'source_device': 'sourceDevice'
    }

    def __init__(self, copy_shared_policies=None, target_device_list=None, source_device=None):  # noqa: E501
        """DeviceCopyConfigRequest - a model defined in Swagger"""  # noqa: E501

        self._copy_shared_policies = None
        self._target_device_list = None
        self._source_device = None
        self.discriminator = None

        if copy_shared_policies is not None:
            self.copy_shared_policies = copy_shared_policies
        if target_device_list is not None:
            self.target_device_list = target_device_list
        if source_device is not None:
            self.source_device = source_device

    @property
    def copy_shared_policies(self):
        """Gets the copy_shared_policies of this DeviceCopyConfigRequest.  # noqa: E501

        Boolean value. Copies shared policies from source standalone device or HA to target standalone device based on True or False input  # noqa: E501

        :return: The copy_shared_policies of this DeviceCopyConfigRequest.  # noqa: E501
        :rtype: bool
        """
        return self._copy_shared_policies

    @copy_shared_policies.setter
    def copy_shared_policies(self, copy_shared_policies):
        """Sets the copy_shared_policies of this DeviceCopyConfigRequest.

        Boolean value. Copies shared policies from source standalone device or HA to target standalone device based on True or False input  # noqa: E501

        :param copy_shared_policies: The copy_shared_policies of this DeviceCopyConfigRequest.  # noqa: E501
        :type: bool
        """

        self._copy_shared_policies = copy_shared_policies

    @property
    def target_device_list(self):
        """Gets the target_device_list of this DeviceCopyConfigRequest.  # noqa: E501

        Target device list is a standalone device UUID  # noqa: E501

        :return: The target_device_list of this DeviceCopyConfigRequest.  # noqa: E501
        :rtype: list[ITarget]
        """
        return self._target_device_list

    @target_device_list.setter
    def target_device_list(self, target_device_list):
        """Sets the target_device_list of this DeviceCopyConfigRequest.

        Target device list is a standalone device UUID  # noqa: E501

        :param target_device_list: The target_device_list of this DeviceCopyConfigRequest.  # noqa: E501
        :type: list[ITarget]
        """

        self._target_device_list = target_device_list

    @property
    def source_device(self):
        """Gets the source_device of this DeviceCopyConfigRequest.  # noqa: E501

        Source device is either a standalone device UUID or HA container UUID  # noqa: E501

        :return: The source_device of this DeviceCopyConfigRequest.  # noqa: E501
        :rtype: ITarget
        """
        return self._source_device

    @source_device.setter
    def source_device(self, source_device):
        """Sets the source_device of this DeviceCopyConfigRequest.

        Source device is either a standalone device UUID or HA container UUID  # noqa: E501

        :param source_device: The source_device of this DeviceCopyConfigRequest.  # noqa: E501
        :type: ITarget
        """

        self._source_device = source_device

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
        if issubclass(DeviceCopyConfigRequest, dict):
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
        if not isinstance(other, DeviceCopyConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
