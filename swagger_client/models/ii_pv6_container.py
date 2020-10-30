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


class IIPv6Container(object):
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
        'link_local_address': 'str',
        'addresses': 'list[IAddressContainer]',
        'ra_interval': 'int',
        'enable_auto_config': 'bool',
        'ns_interval': 'int',
        'prefixes': 'list[IPrefixContainer]',
        'enable_ra': 'bool',
        'enforce_eui64': 'bool',
        'dad_attempts': 'int',
        'enable_dhcp_addr_config': 'bool',
        'enable_dhcp_non_addr_config': 'bool',
        'ra_life_time': 'int',
        'enable_ipv6': 'bool',
        'reachable_time': 'int'
    }

    attribute_map = {
        'link_local_address': 'linkLocalAddress',
        'addresses': 'addresses',
        'ra_interval': 'raInterval',
        'enable_auto_config': 'enableAutoConfig',
        'ns_interval': 'nsInterval',
        'prefixes': 'prefixes',
        'enable_ra': 'enableRA',
        'enforce_eui64': 'enforceEUI64',
        'dad_attempts': 'dadAttempts',
        'enable_dhcp_addr_config': 'enableDHCPAddrConfig',
        'enable_dhcp_non_addr_config': 'enableDHCPNonAddrConfig',
        'ra_life_time': 'raLifeTime',
        'enable_ipv6': 'enableIPV6',
        'reachable_time': 'reachableTime'
    }

    def __init__(self, link_local_address=None, addresses=None, ra_interval=None, enable_auto_config=None, ns_interval=None, prefixes=None, enable_ra=None, enforce_eui64=None, dad_attempts=None, enable_dhcp_addr_config=None, enable_dhcp_non_addr_config=None, ra_life_time=None, enable_ipv6=None, reachable_time=None):  # noqa: E501
        """IIPv6Container - a model defined in Swagger"""  # noqa: E501

        self._link_local_address = None
        self._addresses = None
        self._ra_interval = None
        self._enable_auto_config = None
        self._ns_interval = None
        self._prefixes = None
        self._enable_ra = None
        self._enforce_eui64 = None
        self._dad_attempts = None
        self._enable_dhcp_addr_config = None
        self._enable_dhcp_non_addr_config = None
        self._ra_life_time = None
        self._enable_ipv6 = None
        self._reachable_time = None
        self.discriminator = None

        if link_local_address is not None:
            self.link_local_address = link_local_address
        if addresses is not None:
            self.addresses = addresses
        if ra_interval is not None:
            self.ra_interval = ra_interval
        if enable_auto_config is not None:
            self.enable_auto_config = enable_auto_config
        if ns_interval is not None:
            self.ns_interval = ns_interval
        if prefixes is not None:
            self.prefixes = prefixes
        if enable_ra is not None:
            self.enable_ra = enable_ra
        if enforce_eui64 is not None:
            self.enforce_eui64 = enforce_eui64
        if dad_attempts is not None:
            self.dad_attempts = dad_attempts
        if enable_dhcp_addr_config is not None:
            self.enable_dhcp_addr_config = enable_dhcp_addr_config
        if enable_dhcp_non_addr_config is not None:
            self.enable_dhcp_non_addr_config = enable_dhcp_non_addr_config
        if ra_life_time is not None:
            self.ra_life_time = ra_life_time
        if enable_ipv6 is not None:
            self.enable_ipv6 = enable_ipv6
        if reachable_time is not None:
            self.reachable_time = reachable_time

    @property
    def link_local_address(self):
        """Gets the link_local_address of this IIPv6Container.  # noqa: E501


        :return: The link_local_address of this IIPv6Container.  # noqa: E501
        :rtype: str
        """
        return self._link_local_address

    @link_local_address.setter
    def link_local_address(self, link_local_address):
        """Sets the link_local_address of this IIPv6Container.


        :param link_local_address: The link_local_address of this IIPv6Container.  # noqa: E501
        :type: str
        """

        self._link_local_address = link_local_address

    @property
    def addresses(self):
        """Gets the addresses of this IIPv6Container.  # noqa: E501


        :return: The addresses of this IIPv6Container.  # noqa: E501
        :rtype: list[IAddressContainer]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this IIPv6Container.


        :param addresses: The addresses of this IIPv6Container.  # noqa: E501
        :type: list[IAddressContainer]
        """

        self._addresses = addresses

    @property
    def ra_interval(self):
        """Gets the ra_interval of this IIPv6Container.  # noqa: E501


        :return: The ra_interval of this IIPv6Container.  # noqa: E501
        :rtype: int
        """
        return self._ra_interval

    @ra_interval.setter
    def ra_interval(self, ra_interval):
        """Sets the ra_interval of this IIPv6Container.


        :param ra_interval: The ra_interval of this IIPv6Container.  # noqa: E501
        :type: int
        """

        self._ra_interval = ra_interval

    @property
    def enable_auto_config(self):
        """Gets the enable_auto_config of this IIPv6Container.  # noqa: E501


        :return: The enable_auto_config of this IIPv6Container.  # noqa: E501
        :rtype: bool
        """
        return self._enable_auto_config

    @enable_auto_config.setter
    def enable_auto_config(self, enable_auto_config):
        """Sets the enable_auto_config of this IIPv6Container.


        :param enable_auto_config: The enable_auto_config of this IIPv6Container.  # noqa: E501
        :type: bool
        """

        self._enable_auto_config = enable_auto_config

    @property
    def ns_interval(self):
        """Gets the ns_interval of this IIPv6Container.  # noqa: E501


        :return: The ns_interval of this IIPv6Container.  # noqa: E501
        :rtype: int
        """
        return self._ns_interval

    @ns_interval.setter
    def ns_interval(self, ns_interval):
        """Sets the ns_interval of this IIPv6Container.


        :param ns_interval: The ns_interval of this IIPv6Container.  # noqa: E501
        :type: int
        """

        self._ns_interval = ns_interval

    @property
    def prefixes(self):
        """Gets the prefixes of this IIPv6Container.  # noqa: E501


        :return: The prefixes of this IIPv6Container.  # noqa: E501
        :rtype: list[IPrefixContainer]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """Sets the prefixes of this IIPv6Container.


        :param prefixes: The prefixes of this IIPv6Container.  # noqa: E501
        :type: list[IPrefixContainer]
        """

        self._prefixes = prefixes

    @property
    def enable_ra(self):
        """Gets the enable_ra of this IIPv6Container.  # noqa: E501


        :return: The enable_ra of this IIPv6Container.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ra

    @enable_ra.setter
    def enable_ra(self, enable_ra):
        """Sets the enable_ra of this IIPv6Container.


        :param enable_ra: The enable_ra of this IIPv6Container.  # noqa: E501
        :type: bool
        """

        self._enable_ra = enable_ra

    @property
    def enforce_eui64(self):
        """Gets the enforce_eui64 of this IIPv6Container.  # noqa: E501


        :return: The enforce_eui64 of this IIPv6Container.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_eui64

    @enforce_eui64.setter
    def enforce_eui64(self, enforce_eui64):
        """Sets the enforce_eui64 of this IIPv6Container.


        :param enforce_eui64: The enforce_eui64 of this IIPv6Container.  # noqa: E501
        :type: bool
        """

        self._enforce_eui64 = enforce_eui64

    @property
    def dad_attempts(self):
        """Gets the dad_attempts of this IIPv6Container.  # noqa: E501


        :return: The dad_attempts of this IIPv6Container.  # noqa: E501
        :rtype: int
        """
        return self._dad_attempts

    @dad_attempts.setter
    def dad_attempts(self, dad_attempts):
        """Sets the dad_attempts of this IIPv6Container.


        :param dad_attempts: The dad_attempts of this IIPv6Container.  # noqa: E501
        :type: int
        """

        self._dad_attempts = dad_attempts

    @property
    def enable_dhcp_addr_config(self):
        """Gets the enable_dhcp_addr_config of this IIPv6Container.  # noqa: E501


        :return: The enable_dhcp_addr_config of this IIPv6Container.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dhcp_addr_config

    @enable_dhcp_addr_config.setter
    def enable_dhcp_addr_config(self, enable_dhcp_addr_config):
        """Sets the enable_dhcp_addr_config of this IIPv6Container.


        :param enable_dhcp_addr_config: The enable_dhcp_addr_config of this IIPv6Container.  # noqa: E501
        :type: bool
        """

        self._enable_dhcp_addr_config = enable_dhcp_addr_config

    @property
    def enable_dhcp_non_addr_config(self):
        """Gets the enable_dhcp_non_addr_config of this IIPv6Container.  # noqa: E501


        :return: The enable_dhcp_non_addr_config of this IIPv6Container.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dhcp_non_addr_config

    @enable_dhcp_non_addr_config.setter
    def enable_dhcp_non_addr_config(self, enable_dhcp_non_addr_config):
        """Sets the enable_dhcp_non_addr_config of this IIPv6Container.


        :param enable_dhcp_non_addr_config: The enable_dhcp_non_addr_config of this IIPv6Container.  # noqa: E501
        :type: bool
        """

        self._enable_dhcp_non_addr_config = enable_dhcp_non_addr_config

    @property
    def ra_life_time(self):
        """Gets the ra_life_time of this IIPv6Container.  # noqa: E501


        :return: The ra_life_time of this IIPv6Container.  # noqa: E501
        :rtype: int
        """
        return self._ra_life_time

    @ra_life_time.setter
    def ra_life_time(self, ra_life_time):
        """Sets the ra_life_time of this IIPv6Container.


        :param ra_life_time: The ra_life_time of this IIPv6Container.  # noqa: E501
        :type: int
        """

        self._ra_life_time = ra_life_time

    @property
    def enable_ipv6(self):
        """Gets the enable_ipv6 of this IIPv6Container.  # noqa: E501


        :return: The enable_ipv6 of this IIPv6Container.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ipv6

    @enable_ipv6.setter
    def enable_ipv6(self, enable_ipv6):
        """Sets the enable_ipv6 of this IIPv6Container.


        :param enable_ipv6: The enable_ipv6 of this IIPv6Container.  # noqa: E501
        :type: bool
        """

        self._enable_ipv6 = enable_ipv6

    @property
    def reachable_time(self):
        """Gets the reachable_time of this IIPv6Container.  # noqa: E501


        :return: The reachable_time of this IIPv6Container.  # noqa: E501
        :rtype: int
        """
        return self._reachable_time

    @reachable_time.setter
    def reachable_time(self, reachable_time):
        """Sets the reachable_time of this IIPv6Container.


        :param reachable_time: The reachable_time of this IIPv6Container.  # noqa: E501
        :type: int
        """

        self._reachable_time = reachable_time

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
        if issubclass(IIPv6Container, dict):
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
        if not isinstance(other, IIPv6Container):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other