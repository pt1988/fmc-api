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


class InlineSet(object):
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
        'mac_filtering': 'bool',
        'load_balancing_mode_vlan': 'str',
        'tap_mode': 'bool',
        'metadata': 'IMetadata',
        'stand_by': 'bool',
        'fail_open_snort_busy': 'bool',
        'description': 'str',
        'type': 'str',
        'version': 'str',
        'strict_tcp_enforcement': 'bool',
        'failopen': 'bool',
        'mtu': 'int',
        'bypass': 'bool',
        'fail_safe': 'bool',
        'load_balancing_mode': 'str',
        'fail_open_snort_down': 'bool',
        'inlinepairs': 'list[IInlinePair]',
        'name': 'str',
        'propogate_link_state': 'bool',
        'links': 'Links',
        'id': 'str'
    }

    attribute_map = {
        'mac_filtering': 'macFiltering',
        'load_balancing_mode_vlan': 'loadBalancingModeVlan',
        'tap_mode': 'tapMode',
        'metadata': 'metadata',
        'stand_by': 'standBy',
        'fail_open_snort_busy': 'failOpenSnortBusy',
        'description': 'description',
        'type': 'type',
        'version': 'version',
        'strict_tcp_enforcement': 'strictTCPEnforcement',
        'failopen': 'failopen',
        'mtu': 'mtu',
        'bypass': 'bypass',
        'fail_safe': 'failSafe',
        'load_balancing_mode': 'loadBalancingMode',
        'fail_open_snort_down': 'failOpenSnortDown',
        'inlinepairs': 'inlinepairs',
        'name': 'name',
        'propogate_link_state': 'propogateLinkState',
        'links': 'links',
        'id': 'id'
    }

    def __init__(self, mac_filtering=None, load_balancing_mode_vlan=None, tap_mode=None, metadata=None, stand_by=None, fail_open_snort_busy=None, description=None, type=None, version=None, strict_tcp_enforcement=None, failopen=None, mtu=None, bypass=None, fail_safe=None, load_balancing_mode=None, fail_open_snort_down=None, inlinepairs=None, name=None, propogate_link_state=None, links=None, id=None):  # noqa: E501
        """InlineSet - a model defined in Swagger"""  # noqa: E501

        self._mac_filtering = None
        self._load_balancing_mode_vlan = None
        self._tap_mode = None
        self._metadata = None
        self._stand_by = None
        self._fail_open_snort_busy = None
        self._description = None
        self._type = None
        self._version = None
        self._strict_tcp_enforcement = None
        self._failopen = None
        self._mtu = None
        self._bypass = None
        self._fail_safe = None
        self._load_balancing_mode = None
        self._fail_open_snort_down = None
        self._inlinepairs = None
        self._name = None
        self._propogate_link_state = None
        self._links = None
        self._id = None
        self.discriminator = None

        if mac_filtering is not None:
            self.mac_filtering = mac_filtering
        if load_balancing_mode_vlan is not None:
            self.load_balancing_mode_vlan = load_balancing_mode_vlan
        if tap_mode is not None:
            self.tap_mode = tap_mode
        if metadata is not None:
            self.metadata = metadata
        if stand_by is not None:
            self.stand_by = stand_by
        if fail_open_snort_busy is not None:
            self.fail_open_snort_busy = fail_open_snort_busy
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if strict_tcp_enforcement is not None:
            self.strict_tcp_enforcement = strict_tcp_enforcement
        if failopen is not None:
            self.failopen = failopen
        if mtu is not None:
            self.mtu = mtu
        if bypass is not None:
            self.bypass = bypass
        if fail_safe is not None:
            self.fail_safe = fail_safe
        if load_balancing_mode is not None:
            self.load_balancing_mode = load_balancing_mode
        if fail_open_snort_down is not None:
            self.fail_open_snort_down = fail_open_snort_down
        if inlinepairs is not None:
            self.inlinepairs = inlinepairs
        if name is not None:
            self.name = name
        if propogate_link_state is not None:
            self.propogate_link_state = propogate_link_state
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id

    @property
    def mac_filtering(self):
        """Gets the mac_filtering of this InlineSet.  # noqa: E501


        :return: The mac_filtering of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._mac_filtering

    @mac_filtering.setter
    def mac_filtering(self, mac_filtering):
        """Sets the mac_filtering of this InlineSet.


        :param mac_filtering: The mac_filtering of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._mac_filtering = mac_filtering

    @property
    def load_balancing_mode_vlan(self):
        """Gets the load_balancing_mode_vlan of this InlineSet.  # noqa: E501


        :return: The load_balancing_mode_vlan of this InlineSet.  # noqa: E501
        :rtype: str
        """
        return self._load_balancing_mode_vlan

    @load_balancing_mode_vlan.setter
    def load_balancing_mode_vlan(self, load_balancing_mode_vlan):
        """Sets the load_balancing_mode_vlan of this InlineSet.


        :param load_balancing_mode_vlan: The load_balancing_mode_vlan of this InlineSet.  # noqa: E501
        :type: str
        """

        self._load_balancing_mode_vlan = load_balancing_mode_vlan

    @property
    def tap_mode(self):
        """Gets the tap_mode of this InlineSet.  # noqa: E501


        :return: The tap_mode of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._tap_mode

    @tap_mode.setter
    def tap_mode(self, tap_mode):
        """Sets the tap_mode of this InlineSet.


        :param tap_mode: The tap_mode of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._tap_mode = tap_mode

    @property
    def metadata(self):
        """Gets the metadata of this InlineSet.  # noqa: E501


        :return: The metadata of this InlineSet.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InlineSet.


        :param metadata: The metadata of this InlineSet.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def stand_by(self):
        """Gets the stand_by of this InlineSet.  # noqa: E501


        :return: The stand_by of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._stand_by

    @stand_by.setter
    def stand_by(self, stand_by):
        """Sets the stand_by of this InlineSet.


        :param stand_by: The stand_by of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._stand_by = stand_by

    @property
    def fail_open_snort_busy(self):
        """Gets the fail_open_snort_busy of this InlineSet.  # noqa: E501


        :return: The fail_open_snort_busy of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._fail_open_snort_busy

    @fail_open_snort_busy.setter
    def fail_open_snort_busy(self, fail_open_snort_busy):
        """Sets the fail_open_snort_busy of this InlineSet.


        :param fail_open_snort_busy: The fail_open_snort_busy of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._fail_open_snort_busy = fail_open_snort_busy

    @property
    def description(self):
        """Gets the description of this InlineSet.  # noqa: E501


        :return: The description of this InlineSet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineSet.


        :param description: The description of this InlineSet.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this InlineSet.  # noqa: E501


        :return: The type of this InlineSet.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineSet.


        :param type: The type of this InlineSet.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this InlineSet.  # noqa: E501


        :return: The version of this InlineSet.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InlineSet.


        :param version: The version of this InlineSet.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def strict_tcp_enforcement(self):
        """Gets the strict_tcp_enforcement of this InlineSet.  # noqa: E501


        :return: The strict_tcp_enforcement of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._strict_tcp_enforcement

    @strict_tcp_enforcement.setter
    def strict_tcp_enforcement(self, strict_tcp_enforcement):
        """Sets the strict_tcp_enforcement of this InlineSet.


        :param strict_tcp_enforcement: The strict_tcp_enforcement of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._strict_tcp_enforcement = strict_tcp_enforcement

    @property
    def failopen(self):
        """Gets the failopen of this InlineSet.  # noqa: E501


        :return: The failopen of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._failopen

    @failopen.setter
    def failopen(self, failopen):
        """Sets the failopen of this InlineSet.


        :param failopen: The failopen of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._failopen = failopen

    @property
    def mtu(self):
        """Gets the mtu of this InlineSet.  # noqa: E501


        :return: The mtu of this InlineSet.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this InlineSet.


        :param mtu: The mtu of this InlineSet.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def bypass(self):
        """Gets the bypass of this InlineSet.  # noqa: E501


        :return: The bypass of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._bypass

    @bypass.setter
    def bypass(self, bypass):
        """Sets the bypass of this InlineSet.


        :param bypass: The bypass of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._bypass = bypass

    @property
    def fail_safe(self):
        """Gets the fail_safe of this InlineSet.  # noqa: E501


        :return: The fail_safe of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._fail_safe

    @fail_safe.setter
    def fail_safe(self, fail_safe):
        """Sets the fail_safe of this InlineSet.


        :param fail_safe: The fail_safe of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._fail_safe = fail_safe

    @property
    def load_balancing_mode(self):
        """Gets the load_balancing_mode of this InlineSet.  # noqa: E501


        :return: The load_balancing_mode of this InlineSet.  # noqa: E501
        :rtype: str
        """
        return self._load_balancing_mode

    @load_balancing_mode.setter
    def load_balancing_mode(self, load_balancing_mode):
        """Sets the load_balancing_mode of this InlineSet.


        :param load_balancing_mode: The load_balancing_mode of this InlineSet.  # noqa: E501
        :type: str
        """

        self._load_balancing_mode = load_balancing_mode

    @property
    def fail_open_snort_down(self):
        """Gets the fail_open_snort_down of this InlineSet.  # noqa: E501


        :return: The fail_open_snort_down of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._fail_open_snort_down

    @fail_open_snort_down.setter
    def fail_open_snort_down(self, fail_open_snort_down):
        """Sets the fail_open_snort_down of this InlineSet.


        :param fail_open_snort_down: The fail_open_snort_down of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._fail_open_snort_down = fail_open_snort_down

    @property
    def inlinepairs(self):
        """Gets the inlinepairs of this InlineSet.  # noqa: E501


        :return: The inlinepairs of this InlineSet.  # noqa: E501
        :rtype: list[IInlinePair]
        """
        return self._inlinepairs

    @inlinepairs.setter
    def inlinepairs(self, inlinepairs):
        """Sets the inlinepairs of this InlineSet.


        :param inlinepairs: The inlinepairs of this InlineSet.  # noqa: E501
        :type: list[IInlinePair]
        """

        self._inlinepairs = inlinepairs

    @property
    def name(self):
        """Gets the name of this InlineSet.  # noqa: E501


        :return: The name of this InlineSet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineSet.


        :param name: The name of this InlineSet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def propogate_link_state(self):
        """Gets the propogate_link_state of this InlineSet.  # noqa: E501


        :return: The propogate_link_state of this InlineSet.  # noqa: E501
        :rtype: bool
        """
        return self._propogate_link_state

    @propogate_link_state.setter
    def propogate_link_state(self, propogate_link_state):
        """Sets the propogate_link_state of this InlineSet.


        :param propogate_link_state: The propogate_link_state of this InlineSet.  # noqa: E501
        :type: bool
        """

        self._propogate_link_state = propogate_link_state

    @property
    def links(self):
        """Gets the links of this InlineSet.  # noqa: E501


        :return: The links of this InlineSet.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InlineSet.


        :param links: The links of this InlineSet.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this InlineSet.  # noqa: E501


        :return: The id of this InlineSet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineSet.


        :param id: The id of this InlineSet.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(InlineSet, dict):
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
        if not isinstance(other, InlineSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
