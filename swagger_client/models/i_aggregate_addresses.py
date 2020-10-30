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


class IAggregateAddresses(object):
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
        'summary_only': 'bool',
        'ipv6_aggregate_network': 'INetworkAddress',
        'ipv4_aggregate_network': 'INetworkAddress',
        'attribute_map': 'IRouteMap',
        'name': 'str',
        'links': 'ILinks',
        'id': 'str',
        'suppress_map': 'IRouteMap',
        'as_set': 'bool',
        'type': 'str',
        'advertise_map': 'IRouteMap'
    }

    attribute_map = {
        'summary_only': 'summaryOnly',
        'ipv6_aggregate_network': 'ipv6AggregateNetwork',
        'ipv4_aggregate_network': 'ipv4AggregateNetwork',
        'attribute_map': 'attributeMap',
        'name': 'name',
        'links': 'links',
        'id': 'id',
        'suppress_map': 'suppressMap',
        'as_set': 'asSet',
        'type': 'type',
        'advertise_map': 'advertiseMap'
    }

    def __init__(self, summary_only=None, ipv6_aggregate_network=None, ipv4_aggregate_network=None, attribute_map=None, name=None, links=None, id=None, suppress_map=None, as_set=None, type=None, advertise_map=None):  # noqa: E501
        """IAggregateAddresses - a model defined in Swagger"""  # noqa: E501

        self._summary_only = None
        self._ipv6_aggregate_network = None
        self._ipv4_aggregate_network = None
        self._attribute_map = None
        self._name = None
        self._links = None
        self._id = None
        self._suppress_map = None
        self._as_set = None
        self._type = None
        self._advertise_map = None
        self.discriminator = None

        if summary_only is not None:
            self.summary_only = summary_only
        if ipv6_aggregate_network is not None:
            self.ipv6_aggregate_network = ipv6_aggregate_network
        if ipv4_aggregate_network is not None:
            self.ipv4_aggregate_network = ipv4_aggregate_network
        if attribute_map is not None:
            self.attribute_map = attribute_map
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if suppress_map is not None:
            self.suppress_map = suppress_map
        if as_set is not None:
            self.as_set = as_set
        if type is not None:
            self.type = type
        if advertise_map is not None:
            self.advertise_map = advertise_map

    @property
    def summary_only(self):
        """Gets the summary_only of this IAggregateAddresses.  # noqa: E501


        :return: The summary_only of this IAggregateAddresses.  # noqa: E501
        :rtype: bool
        """
        return self._summary_only

    @summary_only.setter
    def summary_only(self, summary_only):
        """Sets the summary_only of this IAggregateAddresses.


        :param summary_only: The summary_only of this IAggregateAddresses.  # noqa: E501
        :type: bool
        """

        self._summary_only = summary_only

    @property
    def ipv6_aggregate_network(self):
        """Gets the ipv6_aggregate_network of this IAggregateAddresses.  # noqa: E501


        :return: The ipv6_aggregate_network of this IAggregateAddresses.  # noqa: E501
        :rtype: INetworkAddress
        """
        return self._ipv6_aggregate_network

    @ipv6_aggregate_network.setter
    def ipv6_aggregate_network(self, ipv6_aggregate_network):
        """Sets the ipv6_aggregate_network of this IAggregateAddresses.


        :param ipv6_aggregate_network: The ipv6_aggregate_network of this IAggregateAddresses.  # noqa: E501
        :type: INetworkAddress
        """

        self._ipv6_aggregate_network = ipv6_aggregate_network

    @property
    def ipv4_aggregate_network(self):
        """Gets the ipv4_aggregate_network of this IAggregateAddresses.  # noqa: E501


        :return: The ipv4_aggregate_network of this IAggregateAddresses.  # noqa: E501
        :rtype: INetworkAddress
        """
        return self._ipv4_aggregate_network

    @ipv4_aggregate_network.setter
    def ipv4_aggregate_network(self, ipv4_aggregate_network):
        """Sets the ipv4_aggregate_network of this IAggregateAddresses.


        :param ipv4_aggregate_network: The ipv4_aggregate_network of this IAggregateAddresses.  # noqa: E501
        :type: INetworkAddress
        """

        self._ipv4_aggregate_network = ipv4_aggregate_network

    @property
    def attribute_map(self):
        """Gets the attribute_map of this IAggregateAddresses.  # noqa: E501


        :return: The attribute_map of this IAggregateAddresses.  # noqa: E501
        :rtype: IRouteMap
        """
        return self._attribute_map

    @attribute_map.setter
    def attribute_map(self, attribute_map):
        """Sets the attribute_map of this IAggregateAddresses.


        :param attribute_map: The attribute_map of this IAggregateAddresses.  # noqa: E501
        :type: IRouteMap
        """

        self._attribute_map = attribute_map

    @property
    def name(self):
        """Gets the name of this IAggregateAddresses.  # noqa: E501


        :return: The name of this IAggregateAddresses.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IAggregateAddresses.


        :param name: The name of this IAggregateAddresses.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this IAggregateAddresses.  # noqa: E501


        :return: The links of this IAggregateAddresses.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IAggregateAddresses.


        :param links: The links of this IAggregateAddresses.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IAggregateAddresses.  # noqa: E501


        :return: The id of this IAggregateAddresses.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IAggregateAddresses.


        :param id: The id of this IAggregateAddresses.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def suppress_map(self):
        """Gets the suppress_map of this IAggregateAddresses.  # noqa: E501


        :return: The suppress_map of this IAggregateAddresses.  # noqa: E501
        :rtype: IRouteMap
        """
        return self._suppress_map

    @suppress_map.setter
    def suppress_map(self, suppress_map):
        """Sets the suppress_map of this IAggregateAddresses.


        :param suppress_map: The suppress_map of this IAggregateAddresses.  # noqa: E501
        :type: IRouteMap
        """

        self._suppress_map = suppress_map

    @property
    def as_set(self):
        """Gets the as_set of this IAggregateAddresses.  # noqa: E501


        :return: The as_set of this IAggregateAddresses.  # noqa: E501
        :rtype: bool
        """
        return self._as_set

    @as_set.setter
    def as_set(self, as_set):
        """Sets the as_set of this IAggregateAddresses.


        :param as_set: The as_set of this IAggregateAddresses.  # noqa: E501
        :type: bool
        """

        self._as_set = as_set

    @property
    def type(self):
        """Gets the type of this IAggregateAddresses.  # noqa: E501


        :return: The type of this IAggregateAddresses.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IAggregateAddresses.


        :param type: The type of this IAggregateAddresses.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def advertise_map(self):
        """Gets the advertise_map of this IAggregateAddresses.  # noqa: E501


        :return: The advertise_map of this IAggregateAddresses.  # noqa: E501
        :rtype: IRouteMap
        """
        return self._advertise_map

    @advertise_map.setter
    def advertise_map(self, advertise_map):
        """Sets the advertise_map of this IAggregateAddresses.


        :param advertise_map: The advertise_map of this IAggregateAddresses.  # noqa: E501
        :type: IRouteMap
        """

        self._advertise_map = advertise_map

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
        if issubclass(IAggregateAddresses, dict):
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
        if not isinstance(other, IAggregateAddresses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
