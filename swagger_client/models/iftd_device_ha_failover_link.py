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


class IFTDDeviceHAFailoverLink(object):
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
        'interface_object': 'IFTDBaseInterface',
        'use_i_pv6_address': 'bool',
        'standby_ip': 'str',
        'active_ip': 'str',
        'logical_name': 'str',
        'subnet_mask': 'str'
    }

    attribute_map = {
        'interface_object': 'interfaceObject',
        'use_i_pv6_address': 'useIPv6Address',
        'standby_ip': 'standbyIP',
        'active_ip': 'activeIP',
        'logical_name': 'logicalName',
        'subnet_mask': 'subnetMask'
    }

    def __init__(self, interface_object=None, use_i_pv6_address=None, standby_ip=None, active_ip=None, logical_name=None, subnet_mask=None):  # noqa: E501
        """IFTDDeviceHAFailoverLink - a model defined in Swagger"""  # noqa: E501

        self._interface_object = None
        self._use_i_pv6_address = None
        self._standby_ip = None
        self._active_ip = None
        self._logical_name = None
        self._subnet_mask = None
        self.discriminator = None

        self.interface_object = interface_object
        if use_i_pv6_address is not None:
            self.use_i_pv6_address = use_i_pv6_address
        self.standby_ip = standby_ip
        self.active_ip = active_ip
        self.logical_name = logical_name
        if subnet_mask is not None:
            self.subnet_mask = subnet_mask

    @property
    def interface_object(self):
        """Gets the interface_object of this IFTDDeviceHAFailoverLink.  # noqa: E501


        :return: The interface_object of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :rtype: IFTDBaseInterface
        """
        return self._interface_object

    @interface_object.setter
    def interface_object(self, interface_object):
        """Sets the interface_object of this IFTDDeviceHAFailoverLink.


        :param interface_object: The interface_object of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :type: IFTDBaseInterface
        """
        if interface_object is None:
            raise ValueError("Invalid value for `interface_object`, must not be `None`")  # noqa: E501

        self._interface_object = interface_object

    @property
    def use_i_pv6_address(self):
        """Gets the use_i_pv6_address of this IFTDDeviceHAFailoverLink.  # noqa: E501


        :return: The use_i_pv6_address of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :rtype: bool
        """
        return self._use_i_pv6_address

    @use_i_pv6_address.setter
    def use_i_pv6_address(self, use_i_pv6_address):
        """Sets the use_i_pv6_address of this IFTDDeviceHAFailoverLink.


        :param use_i_pv6_address: The use_i_pv6_address of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :type: bool
        """

        self._use_i_pv6_address = use_i_pv6_address

    @property
    def standby_ip(self):
        """Gets the standby_ip of this IFTDDeviceHAFailoverLink.  # noqa: E501


        :return: The standby_ip of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :rtype: str
        """
        return self._standby_ip

    @standby_ip.setter
    def standby_ip(self, standby_ip):
        """Sets the standby_ip of this IFTDDeviceHAFailoverLink.


        :param standby_ip: The standby_ip of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :type: str
        """
        if standby_ip is None:
            raise ValueError("Invalid value for `standby_ip`, must not be `None`")  # noqa: E501

        self._standby_ip = standby_ip

    @property
    def active_ip(self):
        """Gets the active_ip of this IFTDDeviceHAFailoverLink.  # noqa: E501


        :return: The active_ip of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :rtype: str
        """
        return self._active_ip

    @active_ip.setter
    def active_ip(self, active_ip):
        """Sets the active_ip of this IFTDDeviceHAFailoverLink.


        :param active_ip: The active_ip of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :type: str
        """
        if active_ip is None:
            raise ValueError("Invalid value for `active_ip`, must not be `None`")  # noqa: E501

        self._active_ip = active_ip

    @property
    def logical_name(self):
        """Gets the logical_name of this IFTDDeviceHAFailoverLink.  # noqa: E501


        :return: The logical_name of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :rtype: str
        """
        return self._logical_name

    @logical_name.setter
    def logical_name(self, logical_name):
        """Sets the logical_name of this IFTDDeviceHAFailoverLink.


        :param logical_name: The logical_name of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :type: str
        """
        if logical_name is None:
            raise ValueError("Invalid value for `logical_name`, must not be `None`")  # noqa: E501

        self._logical_name = logical_name

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this IFTDDeviceHAFailoverLink.  # noqa: E501


        :return: The subnet_mask of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this IFTDDeviceHAFailoverLink.


        :param subnet_mask: The subnet_mask of this IFTDDeviceHAFailoverLink.  # noqa: E501
        :type: str
        """

        self._subnet_mask = subnet_mask

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
        if issubclass(IFTDDeviceHAFailoverLink, dict):
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
        if not isinstance(other, IFTDDeviceHAFailoverLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
