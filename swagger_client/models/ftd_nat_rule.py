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


class FTDNatRule(object):
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
        'metadata': 'Metadata',
        'fall_through': 'bool',
        'nat_type': 'str',
        'dns': 'bool',
        'description': 'str',
        'section': 'str',
        'pat_options': 'IPatOptionsContainer',
        'type': 'str',
        'version': 'str',
        'no_proxy_arp': 'bool',
        'source_interface': 'IInterfaceObjectModel',
        'route_lookup': 'bool',
        'name': 'str',
        'net_to_net': 'bool',
        'links': 'ILinks',
        'destination_interface': 'IInterfaceObjectModel',
        'id': 'str',
        'interface_ipv6': 'bool'
    }

    attribute_map = {
        'metadata': 'metadata',
        'fall_through': 'fallThrough',
        'nat_type': 'natType',
        'dns': 'dns',
        'description': 'description',
        'section': 'section',
        'pat_options': 'patOptions',
        'type': 'type',
        'version': 'version',
        'no_proxy_arp': 'noProxyArp',
        'source_interface': 'sourceInterface',
        'route_lookup': 'routeLookup',
        'name': 'name',
        'net_to_net': 'netToNet',
        'links': 'links',
        'destination_interface': 'destinationInterface',
        'id': 'id',
        'interface_ipv6': 'interfaceIpv6'
    }

    def __init__(self, metadata=None, fall_through=None, nat_type=None, dns=None, description=None, section=None, pat_options=None, type=None, version=None, no_proxy_arp=None, source_interface=None, route_lookup=None, name=None, net_to_net=None, links=None, destination_interface=None, id=None, interface_ipv6=None):  # noqa: E501
        """FTDNatRule - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._fall_through = None
        self._nat_type = None
        self._dns = None
        self._description = None
        self._section = None
        self._pat_options = None
        self._type = None
        self._version = None
        self._no_proxy_arp = None
        self._source_interface = None
        self._route_lookup = None
        self._name = None
        self._net_to_net = None
        self._links = None
        self._destination_interface = None
        self._id = None
        self._interface_ipv6 = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if fall_through is not None:
            self.fall_through = fall_through
        self.nat_type = nat_type
        if dns is not None:
            self.dns = dns
        if description is not None:
            self.description = description
        if section is not None:
            self.section = section
        if pat_options is not None:
            self.pat_options = pat_options
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if no_proxy_arp is not None:
            self.no_proxy_arp = no_proxy_arp
        if source_interface is not None:
            self.source_interface = source_interface
        if route_lookup is not None:
            self.route_lookup = route_lookup
        if name is not None:
            self.name = name
        if net_to_net is not None:
            self.net_to_net = net_to_net
        if links is not None:
            self.links = links
        if destination_interface is not None:
            self.destination_interface = destination_interface
        if id is not None:
            self.id = id
        if interface_ipv6 is not None:
            self.interface_ipv6 = interface_ipv6

    @property
    def metadata(self):
        """Gets the metadata of this FTDNatRule.  # noqa: E501


        :return: The metadata of this FTDNatRule.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FTDNatRule.


        :param metadata: The metadata of this FTDNatRule.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def fall_through(self):
        """Gets the fall_through of this FTDNatRule.  # noqa: E501


        :return: The fall_through of this FTDNatRule.  # noqa: E501
        :rtype: bool
        """
        return self._fall_through

    @fall_through.setter
    def fall_through(self, fall_through):
        """Sets the fall_through of this FTDNatRule.


        :param fall_through: The fall_through of this FTDNatRule.  # noqa: E501
        :type: bool
        """

        self._fall_through = fall_through

    @property
    def nat_type(self):
        """Gets the nat_type of this FTDNatRule.  # noqa: E501


        :return: The nat_type of this FTDNatRule.  # noqa: E501
        :rtype: str
        """
        return self._nat_type

    @nat_type.setter
    def nat_type(self, nat_type):
        """Sets the nat_type of this FTDNatRule.


        :param nat_type: The nat_type of this FTDNatRule.  # noqa: E501
        :type: str
        """
        if nat_type is None:
            raise ValueError("Invalid value for `nat_type`, must not be `None`")  # noqa: E501
        allowed_values = ["STATIC", "DYNAMIC"]  # noqa: E501
        if nat_type not in allowed_values:
            raise ValueError(
                "Invalid value for `nat_type` ({0}), must be one of {1}"  # noqa: E501
                .format(nat_type, allowed_values)
            )

        self._nat_type = nat_type

    @property
    def dns(self):
        """Gets the dns of this FTDNatRule.  # noqa: E501


        :return: The dns of this FTDNatRule.  # noqa: E501
        :rtype: bool
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this FTDNatRule.


        :param dns: The dns of this FTDNatRule.  # noqa: E501
        :type: bool
        """

        self._dns = dns

    @property
    def description(self):
        """Gets the description of this FTDNatRule.  # noqa: E501


        :return: The description of this FTDNatRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FTDNatRule.


        :param description: The description of this FTDNatRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def section(self):
        """Gets the section of this FTDNatRule.  # noqa: E501


        :return: The section of this FTDNatRule.  # noqa: E501
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this FTDNatRule.


        :param section: The section of this FTDNatRule.  # noqa: E501
        :type: str
        """

        self._section = section

    @property
    def pat_options(self):
        """Gets the pat_options of this FTDNatRule.  # noqa: E501


        :return: The pat_options of this FTDNatRule.  # noqa: E501
        :rtype: IPatOptionsContainer
        """
        return self._pat_options

    @pat_options.setter
    def pat_options(self, pat_options):
        """Sets the pat_options of this FTDNatRule.


        :param pat_options: The pat_options of this FTDNatRule.  # noqa: E501
        :type: IPatOptionsContainer
        """

        self._pat_options = pat_options

    @property
    def type(self):
        """Gets the type of this FTDNatRule.  # noqa: E501


        :return: The type of this FTDNatRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FTDNatRule.


        :param type: The type of this FTDNatRule.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this FTDNatRule.  # noqa: E501


        :return: The version of this FTDNatRule.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FTDNatRule.


        :param version: The version of this FTDNatRule.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def no_proxy_arp(self):
        """Gets the no_proxy_arp of this FTDNatRule.  # noqa: E501


        :return: The no_proxy_arp of this FTDNatRule.  # noqa: E501
        :rtype: bool
        """
        return self._no_proxy_arp

    @no_proxy_arp.setter
    def no_proxy_arp(self, no_proxy_arp):
        """Sets the no_proxy_arp of this FTDNatRule.


        :param no_proxy_arp: The no_proxy_arp of this FTDNatRule.  # noqa: E501
        :type: bool
        """

        self._no_proxy_arp = no_proxy_arp

    @property
    def source_interface(self):
        """Gets the source_interface of this FTDNatRule.  # noqa: E501


        :return: The source_interface of this FTDNatRule.  # noqa: E501
        :rtype: IInterfaceObjectModel
        """
        return self._source_interface

    @source_interface.setter
    def source_interface(self, source_interface):
        """Sets the source_interface of this FTDNatRule.


        :param source_interface: The source_interface of this FTDNatRule.  # noqa: E501
        :type: IInterfaceObjectModel
        """

        self._source_interface = source_interface

    @property
    def route_lookup(self):
        """Gets the route_lookup of this FTDNatRule.  # noqa: E501


        :return: The route_lookup of this FTDNatRule.  # noqa: E501
        :rtype: bool
        """
        return self._route_lookup

    @route_lookup.setter
    def route_lookup(self, route_lookup):
        """Sets the route_lookup of this FTDNatRule.


        :param route_lookup: The route_lookup of this FTDNatRule.  # noqa: E501
        :type: bool
        """

        self._route_lookup = route_lookup

    @property
    def name(self):
        """Gets the name of this FTDNatRule.  # noqa: E501


        :return: The name of this FTDNatRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FTDNatRule.


        :param name: The name of this FTDNatRule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def net_to_net(self):
        """Gets the net_to_net of this FTDNatRule.  # noqa: E501


        :return: The net_to_net of this FTDNatRule.  # noqa: E501
        :rtype: bool
        """
        return self._net_to_net

    @net_to_net.setter
    def net_to_net(self, net_to_net):
        """Sets the net_to_net of this FTDNatRule.


        :param net_to_net: The net_to_net of this FTDNatRule.  # noqa: E501
        :type: bool
        """

        self._net_to_net = net_to_net

    @property
    def links(self):
        """Gets the links of this FTDNatRule.  # noqa: E501


        :return: The links of this FTDNatRule.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FTDNatRule.


        :param links: The links of this FTDNatRule.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def destination_interface(self):
        """Gets the destination_interface of this FTDNatRule.  # noqa: E501


        :return: The destination_interface of this FTDNatRule.  # noqa: E501
        :rtype: IInterfaceObjectModel
        """
        return self._destination_interface

    @destination_interface.setter
    def destination_interface(self, destination_interface):
        """Sets the destination_interface of this FTDNatRule.


        :param destination_interface: The destination_interface of this FTDNatRule.  # noqa: E501
        :type: IInterfaceObjectModel
        """

        self._destination_interface = destination_interface

    @property
    def id(self):
        """Gets the id of this FTDNatRule.  # noqa: E501


        :return: The id of this FTDNatRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FTDNatRule.


        :param id: The id of this FTDNatRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def interface_ipv6(self):
        """Gets the interface_ipv6 of this FTDNatRule.  # noqa: E501


        :return: The interface_ipv6 of this FTDNatRule.  # noqa: E501
        :rtype: bool
        """
        return self._interface_ipv6

    @interface_ipv6.setter
    def interface_ipv6(self, interface_ipv6):
        """Sets the interface_ipv6 of this FTDNatRule.


        :param interface_ipv6: The interface_ipv6 of this FTDNatRule.  # noqa: E501
        :type: bool
        """

        self._interface_ipv6 = interface_ipv6

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
        if issubclass(FTDNatRule, dict):
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
        if not isinstance(other, FTDNatRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
