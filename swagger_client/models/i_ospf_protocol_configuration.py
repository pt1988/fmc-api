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


class IOspfProtocolConfiguration(object):
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
        'retransmit_interval': 'int',
        'ignore_mtu_mismatch': 'bool',
        'ospf_authentication': 'IOspfAuthentication',
        'filter_outgoing_lsa': 'bool',
        'ospf_interval': 'IOspfInterval',
        'priority': 'int',
        'ptp_non_broadcast': 'bool',
        'transmit_delay': 'int',
        'packet_cost': 'int'
    }

    attribute_map = {
        'retransmit_interval': 'retransmitInterval',
        'ignore_mtu_mismatch': 'ignoreMtuMismatch',
        'ospf_authentication': 'ospfAuthentication',
        'filter_outgoing_lsa': 'filterOutgoingLSA',
        'ospf_interval': 'ospfInterval',
        'priority': 'priority',
        'ptp_non_broadcast': 'ptpNonBroadcast',
        'transmit_delay': 'transmitDelay',
        'packet_cost': 'packetCost'
    }

    def __init__(self, retransmit_interval=None, ignore_mtu_mismatch=None, ospf_authentication=None, filter_outgoing_lsa=None, ospf_interval=None, priority=None, ptp_non_broadcast=None, transmit_delay=None, packet_cost=None):  # noqa: E501
        """IOspfProtocolConfiguration - a model defined in Swagger"""  # noqa: E501

        self._retransmit_interval = None
        self._ignore_mtu_mismatch = None
        self._ospf_authentication = None
        self._filter_outgoing_lsa = None
        self._ospf_interval = None
        self._priority = None
        self._ptp_non_broadcast = None
        self._transmit_delay = None
        self._packet_cost = None
        self.discriminator = None

        if retransmit_interval is not None:
            self.retransmit_interval = retransmit_interval
        if ignore_mtu_mismatch is not None:
            self.ignore_mtu_mismatch = ignore_mtu_mismatch
        if ospf_authentication is not None:
            self.ospf_authentication = ospf_authentication
        if filter_outgoing_lsa is not None:
            self.filter_outgoing_lsa = filter_outgoing_lsa
        if ospf_interval is not None:
            self.ospf_interval = ospf_interval
        if priority is not None:
            self.priority = priority
        if ptp_non_broadcast is not None:
            self.ptp_non_broadcast = ptp_non_broadcast
        if transmit_delay is not None:
            self.transmit_delay = transmit_delay
        if packet_cost is not None:
            self.packet_cost = packet_cost

    @property
    def retransmit_interval(self):
        """Gets the retransmit_interval of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The retransmit_interval of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._retransmit_interval

    @retransmit_interval.setter
    def retransmit_interval(self, retransmit_interval):
        """Sets the retransmit_interval of this IOspfProtocolConfiguration.


        :param retransmit_interval: The retransmit_interval of this IOspfProtocolConfiguration.  # noqa: E501
        :type: int
        """

        self._retransmit_interval = retransmit_interval

    @property
    def ignore_mtu_mismatch(self):
        """Gets the ignore_mtu_mismatch of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The ignore_mtu_mismatch of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_mtu_mismatch

    @ignore_mtu_mismatch.setter
    def ignore_mtu_mismatch(self, ignore_mtu_mismatch):
        """Sets the ignore_mtu_mismatch of this IOspfProtocolConfiguration.


        :param ignore_mtu_mismatch: The ignore_mtu_mismatch of this IOspfProtocolConfiguration.  # noqa: E501
        :type: bool
        """

        self._ignore_mtu_mismatch = ignore_mtu_mismatch

    @property
    def ospf_authentication(self):
        """Gets the ospf_authentication of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The ospf_authentication of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: IOspfAuthentication
        """
        return self._ospf_authentication

    @ospf_authentication.setter
    def ospf_authentication(self, ospf_authentication):
        """Sets the ospf_authentication of this IOspfProtocolConfiguration.


        :param ospf_authentication: The ospf_authentication of this IOspfProtocolConfiguration.  # noqa: E501
        :type: IOspfAuthentication
        """

        self._ospf_authentication = ospf_authentication

    @property
    def filter_outgoing_lsa(self):
        """Gets the filter_outgoing_lsa of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The filter_outgoing_lsa of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._filter_outgoing_lsa

    @filter_outgoing_lsa.setter
    def filter_outgoing_lsa(self, filter_outgoing_lsa):
        """Sets the filter_outgoing_lsa of this IOspfProtocolConfiguration.


        :param filter_outgoing_lsa: The filter_outgoing_lsa of this IOspfProtocolConfiguration.  # noqa: E501
        :type: bool
        """

        self._filter_outgoing_lsa = filter_outgoing_lsa

    @property
    def ospf_interval(self):
        """Gets the ospf_interval of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The ospf_interval of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: IOspfInterval
        """
        return self._ospf_interval

    @ospf_interval.setter
    def ospf_interval(self, ospf_interval):
        """Sets the ospf_interval of this IOspfProtocolConfiguration.


        :param ospf_interval: The ospf_interval of this IOspfProtocolConfiguration.  # noqa: E501
        :type: IOspfInterval
        """

        self._ospf_interval = ospf_interval

    @property
    def priority(self):
        """Gets the priority of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The priority of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this IOspfProtocolConfiguration.


        :param priority: The priority of this IOspfProtocolConfiguration.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def ptp_non_broadcast(self):
        """Gets the ptp_non_broadcast of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The ptp_non_broadcast of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._ptp_non_broadcast

    @ptp_non_broadcast.setter
    def ptp_non_broadcast(self, ptp_non_broadcast):
        """Sets the ptp_non_broadcast of this IOspfProtocolConfiguration.


        :param ptp_non_broadcast: The ptp_non_broadcast of this IOspfProtocolConfiguration.  # noqa: E501
        :type: bool
        """

        self._ptp_non_broadcast = ptp_non_broadcast

    @property
    def transmit_delay(self):
        """Gets the transmit_delay of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The transmit_delay of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._transmit_delay

    @transmit_delay.setter
    def transmit_delay(self, transmit_delay):
        """Sets the transmit_delay of this IOspfProtocolConfiguration.


        :param transmit_delay: The transmit_delay of this IOspfProtocolConfiguration.  # noqa: E501
        :type: int
        """

        self._transmit_delay = transmit_delay

    @property
    def packet_cost(self):
        """Gets the packet_cost of this IOspfProtocolConfiguration.  # noqa: E501


        :return: The packet_cost of this IOspfProtocolConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._packet_cost

    @packet_cost.setter
    def packet_cost(self, packet_cost):
        """Sets the packet_cost of this IOspfProtocolConfiguration.


        :param packet_cost: The packet_cost of this IOspfProtocolConfiguration.  # noqa: E501
        :type: int
        """

        self._packet_cost = packet_cost

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
        if issubclass(IOspfProtocolConfiguration, dict):
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
        if not isinstance(other, IOspfProtocolConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
