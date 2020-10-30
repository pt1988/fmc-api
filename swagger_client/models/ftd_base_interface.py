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


class FTDBaseInterface(object):
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
        'metadata': 'IMetadata',
        'description': 'str',
        'type': 'str',
        'enabled': 'bool',
        'mtu': 'int',
        'mode': 'str',
        'arp_config': 'list[IARPConfigContainer]',
        'ipv4': 'IIPv4Container',
        'ifname': 'str',
        'ipv6': 'IIPv6Container',
        'links': 'ILinks',
        'id': 'str',
        'mac_learn': 'bool',
        'management_only': 'bool',
        'enable_sgt_propagate': 'bool',
        'enable_anti_spoofing': 'bool',
        'security_zone': 'ISecurityZoneObjectModel',
        'active_mac_address': 'str',
        'fragment_reassembly': 'bool',
        'mac_table': 'list[str]',
        'standby_mac_address': 'str',
        'enable_dns_lookup': 'bool',
        'override_default_fragment_setting': 'IOverrideDefaultFragmentSetting',
        'version': 'str',
        'name': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'description': 'description',
        'type': 'type',
        'enabled': 'enabled',
        'mtu': 'MTU',
        'mode': 'mode',
        'arp_config': 'arpConfig',
        'ipv4': 'ipv4',
        'ifname': 'ifname',
        'ipv6': 'ipv6',
        'links': 'links',
        'id': 'id',
        'mac_learn': 'macLearn',
        'management_only': 'managementOnly',
        'enable_sgt_propagate': 'enableSGTPropagate',
        'enable_anti_spoofing': 'enableAntiSpoofing',
        'security_zone': 'securityZone',
        'active_mac_address': 'activeMACAddress',
        'fragment_reassembly': 'fragmentReassembly',
        'mac_table': 'macTable',
        'standby_mac_address': 'standbyMACAddress',
        'enable_dns_lookup': 'enableDNSLookup',
        'override_default_fragment_setting': 'overrideDefaultFragmentSetting',
        'version': 'version',
        'name': 'name'
    }

    def __init__(self, metadata=None, description=None, type=None, enabled=None, mtu=None, mode=None, arp_config=None, ipv4=None, ifname=None, ipv6=None, links=None, id=None, mac_learn=None, management_only=None, enable_sgt_propagate=None, enable_anti_spoofing=None, security_zone=None, active_mac_address=None, fragment_reassembly=None, mac_table=None, standby_mac_address=None, enable_dns_lookup=None, override_default_fragment_setting=None, version=None, name=None):  # noqa: E501
        """FTDBaseInterface - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._description = None
        self._type = None
        self._enabled = None
        self._mtu = None
        self._mode = None
        self._arp_config = None
        self._ipv4 = None
        self._ifname = None
        self._ipv6 = None
        self._links = None
        self._id = None
        self._mac_learn = None
        self._management_only = None
        self._enable_sgt_propagate = None
        self._enable_anti_spoofing = None
        self._security_zone = None
        self._active_mac_address = None
        self._fragment_reassembly = None
        self._mac_table = None
        self._standby_mac_address = None
        self._enable_dns_lookup = None
        self._override_default_fragment_setting = None
        self._version = None
        self._name = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if enabled is not None:
            self.enabled = enabled
        if mtu is not None:
            self.mtu = mtu
        if mode is not None:
            self.mode = mode
        if arp_config is not None:
            self.arp_config = arp_config
        if ipv4 is not None:
            self.ipv4 = ipv4
        if ifname is not None:
            self.ifname = ifname
        if ipv6 is not None:
            self.ipv6 = ipv6
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if mac_learn is not None:
            self.mac_learn = mac_learn
        if management_only is not None:
            self.management_only = management_only
        if enable_sgt_propagate is not None:
            self.enable_sgt_propagate = enable_sgt_propagate
        if enable_anti_spoofing is not None:
            self.enable_anti_spoofing = enable_anti_spoofing
        if security_zone is not None:
            self.security_zone = security_zone
        if active_mac_address is not None:
            self.active_mac_address = active_mac_address
        if fragment_reassembly is not None:
            self.fragment_reassembly = fragment_reassembly
        if mac_table is not None:
            self.mac_table = mac_table
        if standby_mac_address is not None:
            self.standby_mac_address = standby_mac_address
        if enable_dns_lookup is not None:
            self.enable_dns_lookup = enable_dns_lookup
        if override_default_fragment_setting is not None:
            self.override_default_fragment_setting = override_default_fragment_setting
        if version is not None:
            self.version = version
        if name is not None:
            self.name = name

    @property
    def metadata(self):
        """Gets the metadata of this FTDBaseInterface.  # noqa: E501


        :return: The metadata of this FTDBaseInterface.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FTDBaseInterface.


        :param metadata: The metadata of this FTDBaseInterface.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this FTDBaseInterface.  # noqa: E501


        :return: The description of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FTDBaseInterface.


        :param description: The description of this FTDBaseInterface.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this FTDBaseInterface.  # noqa: E501


        :return: The type of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FTDBaseInterface.


        :param type: The type of this FTDBaseInterface.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def enabled(self):
        """Gets the enabled of this FTDBaseInterface.  # noqa: E501


        :return: The enabled of this FTDBaseInterface.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this FTDBaseInterface.


        :param enabled: The enabled of this FTDBaseInterface.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def mtu(self):
        """Gets the mtu of this FTDBaseInterface.  # noqa: E501


        :return: The mtu of this FTDBaseInterface.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this FTDBaseInterface.


        :param mtu: The mtu of this FTDBaseInterface.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def mode(self):
        """Gets the mode of this FTDBaseInterface.  # noqa: E501


        :return: The mode of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this FTDBaseInterface.


        :param mode: The mode of this FTDBaseInterface.  # noqa: E501
        :type: str
        """
        allowed_values = ["INLINE", "PASSIVE", "TAP", "ERSPAN", "NONE", "SWITCHPORT"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def arp_config(self):
        """Gets the arp_config of this FTDBaseInterface.  # noqa: E501


        :return: The arp_config of this FTDBaseInterface.  # noqa: E501
        :rtype: list[IARPConfigContainer]
        """
        return self._arp_config

    @arp_config.setter
    def arp_config(self, arp_config):
        """Sets the arp_config of this FTDBaseInterface.


        :param arp_config: The arp_config of this FTDBaseInterface.  # noqa: E501
        :type: list[IARPConfigContainer]
        """

        self._arp_config = arp_config

    @property
    def ipv4(self):
        """Gets the ipv4 of this FTDBaseInterface.  # noqa: E501


        :return: The ipv4 of this FTDBaseInterface.  # noqa: E501
        :rtype: IIPv4Container
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this FTDBaseInterface.


        :param ipv4: The ipv4 of this FTDBaseInterface.  # noqa: E501
        :type: IIPv4Container
        """

        self._ipv4 = ipv4

    @property
    def ifname(self):
        """Gets the ifname of this FTDBaseInterface.  # noqa: E501


        :return: The ifname of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._ifname

    @ifname.setter
    def ifname(self, ifname):
        """Sets the ifname of this FTDBaseInterface.


        :param ifname: The ifname of this FTDBaseInterface.  # noqa: E501
        :type: str
        """

        self._ifname = ifname

    @property
    def ipv6(self):
        """Gets the ipv6 of this FTDBaseInterface.  # noqa: E501


        :return: The ipv6 of this FTDBaseInterface.  # noqa: E501
        :rtype: IIPv6Container
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this FTDBaseInterface.


        :param ipv6: The ipv6 of this FTDBaseInterface.  # noqa: E501
        :type: IIPv6Container
        """

        self._ipv6 = ipv6

    @property
    def links(self):
        """Gets the links of this FTDBaseInterface.  # noqa: E501


        :return: The links of this FTDBaseInterface.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FTDBaseInterface.


        :param links: The links of this FTDBaseInterface.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this FTDBaseInterface.  # noqa: E501


        :return: The id of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FTDBaseInterface.


        :param id: The id of this FTDBaseInterface.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def mac_learn(self):
        """Gets the mac_learn of this FTDBaseInterface.  # noqa: E501


        :return: The mac_learn of this FTDBaseInterface.  # noqa: E501
        :rtype: bool
        """
        return self._mac_learn

    @mac_learn.setter
    def mac_learn(self, mac_learn):
        """Sets the mac_learn of this FTDBaseInterface.


        :param mac_learn: The mac_learn of this FTDBaseInterface.  # noqa: E501
        :type: bool
        """

        self._mac_learn = mac_learn

    @property
    def management_only(self):
        """Gets the management_only of this FTDBaseInterface.  # noqa: E501


        :return: The management_only of this FTDBaseInterface.  # noqa: E501
        :rtype: bool
        """
        return self._management_only

    @management_only.setter
    def management_only(self, management_only):
        """Sets the management_only of this FTDBaseInterface.


        :param management_only: The management_only of this FTDBaseInterface.  # noqa: E501
        :type: bool
        """

        self._management_only = management_only

    @property
    def enable_sgt_propagate(self):
        """Gets the enable_sgt_propagate of this FTDBaseInterface.  # noqa: E501


        :return: The enable_sgt_propagate of this FTDBaseInterface.  # noqa: E501
        :rtype: bool
        """
        return self._enable_sgt_propagate

    @enable_sgt_propagate.setter
    def enable_sgt_propagate(self, enable_sgt_propagate):
        """Sets the enable_sgt_propagate of this FTDBaseInterface.


        :param enable_sgt_propagate: The enable_sgt_propagate of this FTDBaseInterface.  # noqa: E501
        :type: bool
        """

        self._enable_sgt_propagate = enable_sgt_propagate

    @property
    def enable_anti_spoofing(self):
        """Gets the enable_anti_spoofing of this FTDBaseInterface.  # noqa: E501


        :return: The enable_anti_spoofing of this FTDBaseInterface.  # noqa: E501
        :rtype: bool
        """
        return self._enable_anti_spoofing

    @enable_anti_spoofing.setter
    def enable_anti_spoofing(self, enable_anti_spoofing):
        """Sets the enable_anti_spoofing of this FTDBaseInterface.


        :param enable_anti_spoofing: The enable_anti_spoofing of this FTDBaseInterface.  # noqa: E501
        :type: bool
        """

        self._enable_anti_spoofing = enable_anti_spoofing

    @property
    def security_zone(self):
        """Gets the security_zone of this FTDBaseInterface.  # noqa: E501


        :return: The security_zone of this FTDBaseInterface.  # noqa: E501
        :rtype: ISecurityZoneObjectModel
        """
        return self._security_zone

    @security_zone.setter
    def security_zone(self, security_zone):
        """Sets the security_zone of this FTDBaseInterface.


        :param security_zone: The security_zone of this FTDBaseInterface.  # noqa: E501
        :type: ISecurityZoneObjectModel
        """

        self._security_zone = security_zone

    @property
    def active_mac_address(self):
        """Gets the active_mac_address of this FTDBaseInterface.  # noqa: E501


        :return: The active_mac_address of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._active_mac_address

    @active_mac_address.setter
    def active_mac_address(self, active_mac_address):
        """Sets the active_mac_address of this FTDBaseInterface.


        :param active_mac_address: The active_mac_address of this FTDBaseInterface.  # noqa: E501
        :type: str
        """

        self._active_mac_address = active_mac_address

    @property
    def fragment_reassembly(self):
        """Gets the fragment_reassembly of this FTDBaseInterface.  # noqa: E501


        :return: The fragment_reassembly of this FTDBaseInterface.  # noqa: E501
        :rtype: bool
        """
        return self._fragment_reassembly

    @fragment_reassembly.setter
    def fragment_reassembly(self, fragment_reassembly):
        """Sets the fragment_reassembly of this FTDBaseInterface.


        :param fragment_reassembly: The fragment_reassembly of this FTDBaseInterface.  # noqa: E501
        :type: bool
        """

        self._fragment_reassembly = fragment_reassembly

    @property
    def mac_table(self):
        """Gets the mac_table of this FTDBaseInterface.  # noqa: E501


        :return: The mac_table of this FTDBaseInterface.  # noqa: E501
        :rtype: list[str]
        """
        return self._mac_table

    @mac_table.setter
    def mac_table(self, mac_table):
        """Sets the mac_table of this FTDBaseInterface.


        :param mac_table: The mac_table of this FTDBaseInterface.  # noqa: E501
        :type: list[str]
        """

        self._mac_table = mac_table

    @property
    def standby_mac_address(self):
        """Gets the standby_mac_address of this FTDBaseInterface.  # noqa: E501


        :return: The standby_mac_address of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._standby_mac_address

    @standby_mac_address.setter
    def standby_mac_address(self, standby_mac_address):
        """Sets the standby_mac_address of this FTDBaseInterface.


        :param standby_mac_address: The standby_mac_address of this FTDBaseInterface.  # noqa: E501
        :type: str
        """

        self._standby_mac_address = standby_mac_address

    @property
    def enable_dns_lookup(self):
        """Gets the enable_dns_lookup of this FTDBaseInterface.  # noqa: E501


        :return: The enable_dns_lookup of this FTDBaseInterface.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dns_lookup

    @enable_dns_lookup.setter
    def enable_dns_lookup(self, enable_dns_lookup):
        """Sets the enable_dns_lookup of this FTDBaseInterface.


        :param enable_dns_lookup: The enable_dns_lookup of this FTDBaseInterface.  # noqa: E501
        :type: bool
        """

        self._enable_dns_lookup = enable_dns_lookup

    @property
    def override_default_fragment_setting(self):
        """Gets the override_default_fragment_setting of this FTDBaseInterface.  # noqa: E501


        :return: The override_default_fragment_setting of this FTDBaseInterface.  # noqa: E501
        :rtype: IOverrideDefaultFragmentSetting
        """
        return self._override_default_fragment_setting

    @override_default_fragment_setting.setter
    def override_default_fragment_setting(self, override_default_fragment_setting):
        """Sets the override_default_fragment_setting of this FTDBaseInterface.


        :param override_default_fragment_setting: The override_default_fragment_setting of this FTDBaseInterface.  # noqa: E501
        :type: IOverrideDefaultFragmentSetting
        """

        self._override_default_fragment_setting = override_default_fragment_setting

    @property
    def version(self):
        """Gets the version of this FTDBaseInterface.  # noqa: E501


        :return: The version of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FTDBaseInterface.


        :param version: The version of this FTDBaseInterface.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this FTDBaseInterface.  # noqa: E501


        :return: The name of this FTDBaseInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FTDBaseInterface.


        :param name: The name of this FTDBaseInterface.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(FTDBaseInterface, dict):
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
        if not isinstance(other, FTDBaseInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
