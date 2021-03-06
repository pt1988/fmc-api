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


class VpnIPSecSettings(object):
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
        'ike_v1_ipsec_proposal': 'list[IReference]',
        'lifetime_seconds': 'int',
        'perfect_forward_secrecy': 'IPFSSettings',
        'ike_v2_ipsec_proposal': 'list[IReference]',
        'tfc_packets': 'ITFCPackets',
        'ike_v2_mode': 'str',
        'description': 'str',
        'crypto_map_type': 'str',
        'enable_sa_strength_enforcement': 'bool',
        'type': 'str',
        'version': 'str',
        'validate_incoming_icmp_error_message': 'bool',
        'lifetime_kilobytes': 'int',
        'do_not_fragment_policy': 'str',
        'name': 'str',
        'links': 'ILinks',
        'id': 'str',
        'enable_rri': 'bool'
    }

    attribute_map = {
        'metadata': 'metadata',
        'ike_v1_ipsec_proposal': 'ikeV1IpsecProposal',
        'lifetime_seconds': 'lifetimeSeconds',
        'perfect_forward_secrecy': 'perfectForwardSecrecy',
        'ike_v2_ipsec_proposal': 'ikeV2IpsecProposal',
        'tfc_packets': 'tfcPackets',
        'ike_v2_mode': 'ikeV2Mode',
        'description': 'description',
        'crypto_map_type': 'cryptoMapType',
        'enable_sa_strength_enforcement': 'enableSaStrengthEnforcement',
        'type': 'type',
        'version': 'version',
        'validate_incoming_icmp_error_message': 'validateIncomingIcmpErrorMessage',
        'lifetime_kilobytes': 'lifetimeKilobytes',
        'do_not_fragment_policy': 'doNotFragmentPolicy',
        'name': 'name',
        'links': 'links',
        'id': 'id',
        'enable_rri': 'enableRRI'
    }

    def __init__(self, metadata=None, ike_v1_ipsec_proposal=None, lifetime_seconds=None, perfect_forward_secrecy=None, ike_v2_ipsec_proposal=None, tfc_packets=None, ike_v2_mode=None, description=None, crypto_map_type=None, enable_sa_strength_enforcement=None, type=None, version=None, validate_incoming_icmp_error_message=None, lifetime_kilobytes=None, do_not_fragment_policy=None, name=None, links=None, id=None, enable_rri=None):  # noqa: E501
        """VpnIPSecSettings - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._ike_v1_ipsec_proposal = None
        self._lifetime_seconds = None
        self._perfect_forward_secrecy = None
        self._ike_v2_ipsec_proposal = None
        self._tfc_packets = None
        self._ike_v2_mode = None
        self._description = None
        self._crypto_map_type = None
        self._enable_sa_strength_enforcement = None
        self._type = None
        self._version = None
        self._validate_incoming_icmp_error_message = None
        self._lifetime_kilobytes = None
        self._do_not_fragment_policy = None
        self._name = None
        self._links = None
        self._id = None
        self._enable_rri = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if ike_v1_ipsec_proposal is not None:
            self.ike_v1_ipsec_proposal = ike_v1_ipsec_proposal
        if lifetime_seconds is not None:
            self.lifetime_seconds = lifetime_seconds
        if perfect_forward_secrecy is not None:
            self.perfect_forward_secrecy = perfect_forward_secrecy
        if ike_v2_ipsec_proposal is not None:
            self.ike_v2_ipsec_proposal = ike_v2_ipsec_proposal
        if tfc_packets is not None:
            self.tfc_packets = tfc_packets
        if ike_v2_mode is not None:
            self.ike_v2_mode = ike_v2_mode
        if description is not None:
            self.description = description
        if crypto_map_type is not None:
            self.crypto_map_type = crypto_map_type
        if enable_sa_strength_enforcement is not None:
            self.enable_sa_strength_enforcement = enable_sa_strength_enforcement
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if validate_incoming_icmp_error_message is not None:
            self.validate_incoming_icmp_error_message = validate_incoming_icmp_error_message
        if lifetime_kilobytes is not None:
            self.lifetime_kilobytes = lifetime_kilobytes
        if do_not_fragment_policy is not None:
            self.do_not_fragment_policy = do_not_fragment_policy
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if enable_rri is not None:
            self.enable_rri = enable_rri

    @property
    def metadata(self):
        """Gets the metadata of this VpnIPSecSettings.  # noqa: E501


        :return: The metadata of this VpnIPSecSettings.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VpnIPSecSettings.


        :param metadata: The metadata of this VpnIPSecSettings.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def ike_v1_ipsec_proposal(self):
        """Gets the ike_v1_ipsec_proposal of this VpnIPSecSettings.  # noqa: E501


        :return: The ike_v1_ipsec_proposal of this VpnIPSecSettings.  # noqa: E501
        :rtype: list[IReference]
        """
        return self._ike_v1_ipsec_proposal

    @ike_v1_ipsec_proposal.setter
    def ike_v1_ipsec_proposal(self, ike_v1_ipsec_proposal):
        """Sets the ike_v1_ipsec_proposal of this VpnIPSecSettings.


        :param ike_v1_ipsec_proposal: The ike_v1_ipsec_proposal of this VpnIPSecSettings.  # noqa: E501
        :type: list[IReference]
        """

        self._ike_v1_ipsec_proposal = ike_v1_ipsec_proposal

    @property
    def lifetime_seconds(self):
        """Gets the lifetime_seconds of this VpnIPSecSettings.  # noqa: E501


        :return: The lifetime_seconds of this VpnIPSecSettings.  # noqa: E501
        :rtype: int
        """
        return self._lifetime_seconds

    @lifetime_seconds.setter
    def lifetime_seconds(self, lifetime_seconds):
        """Sets the lifetime_seconds of this VpnIPSecSettings.


        :param lifetime_seconds: The lifetime_seconds of this VpnIPSecSettings.  # noqa: E501
        :type: int
        """

        self._lifetime_seconds = lifetime_seconds

    @property
    def perfect_forward_secrecy(self):
        """Gets the perfect_forward_secrecy of this VpnIPSecSettings.  # noqa: E501


        :return: The perfect_forward_secrecy of this VpnIPSecSettings.  # noqa: E501
        :rtype: IPFSSettings
        """
        return self._perfect_forward_secrecy

    @perfect_forward_secrecy.setter
    def perfect_forward_secrecy(self, perfect_forward_secrecy):
        """Sets the perfect_forward_secrecy of this VpnIPSecSettings.


        :param perfect_forward_secrecy: The perfect_forward_secrecy of this VpnIPSecSettings.  # noqa: E501
        :type: IPFSSettings
        """

        self._perfect_forward_secrecy = perfect_forward_secrecy

    @property
    def ike_v2_ipsec_proposal(self):
        """Gets the ike_v2_ipsec_proposal of this VpnIPSecSettings.  # noqa: E501


        :return: The ike_v2_ipsec_proposal of this VpnIPSecSettings.  # noqa: E501
        :rtype: list[IReference]
        """
        return self._ike_v2_ipsec_proposal

    @ike_v2_ipsec_proposal.setter
    def ike_v2_ipsec_proposal(self, ike_v2_ipsec_proposal):
        """Sets the ike_v2_ipsec_proposal of this VpnIPSecSettings.


        :param ike_v2_ipsec_proposal: The ike_v2_ipsec_proposal of this VpnIPSecSettings.  # noqa: E501
        :type: list[IReference]
        """

        self._ike_v2_ipsec_proposal = ike_v2_ipsec_proposal

    @property
    def tfc_packets(self):
        """Gets the tfc_packets of this VpnIPSecSettings.  # noqa: E501


        :return: The tfc_packets of this VpnIPSecSettings.  # noqa: E501
        :rtype: ITFCPackets
        """
        return self._tfc_packets

    @tfc_packets.setter
    def tfc_packets(self, tfc_packets):
        """Sets the tfc_packets of this VpnIPSecSettings.


        :param tfc_packets: The tfc_packets of this VpnIPSecSettings.  # noqa: E501
        :type: ITFCPackets
        """

        self._tfc_packets = tfc_packets

    @property
    def ike_v2_mode(self):
        """Gets the ike_v2_mode of this VpnIPSecSettings.  # noqa: E501


        :return: The ike_v2_mode of this VpnIPSecSettings.  # noqa: E501
        :rtype: str
        """
        return self._ike_v2_mode

    @ike_v2_mode.setter
    def ike_v2_mode(self, ike_v2_mode):
        """Sets the ike_v2_mode of this VpnIPSecSettings.


        :param ike_v2_mode: The ike_v2_mode of this VpnIPSecSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["TUNNEL", "TRANSPORT_PREFERRED", "TRANSPORT_REQUIRE"]  # noqa: E501
        if ike_v2_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `ike_v2_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(ike_v2_mode, allowed_values)
            )

        self._ike_v2_mode = ike_v2_mode

    @property
    def description(self):
        """Gets the description of this VpnIPSecSettings.  # noqa: E501


        :return: The description of this VpnIPSecSettings.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VpnIPSecSettings.


        :param description: The description of this VpnIPSecSettings.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def crypto_map_type(self):
        """Gets the crypto_map_type of this VpnIPSecSettings.  # noqa: E501


        :return: The crypto_map_type of this VpnIPSecSettings.  # noqa: E501
        :rtype: str
        """
        return self._crypto_map_type

    @crypto_map_type.setter
    def crypto_map_type(self, crypto_map_type):
        """Sets the crypto_map_type of this VpnIPSecSettings.


        :param crypto_map_type: The crypto_map_type of this VpnIPSecSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["STATIC", "DYNAMIC"]  # noqa: E501
        if crypto_map_type not in allowed_values:
            raise ValueError(
                "Invalid value for `crypto_map_type` ({0}), must be one of {1}"  # noqa: E501
                .format(crypto_map_type, allowed_values)
            )

        self._crypto_map_type = crypto_map_type

    @property
    def enable_sa_strength_enforcement(self):
        """Gets the enable_sa_strength_enforcement of this VpnIPSecSettings.  # noqa: E501


        :return: The enable_sa_strength_enforcement of this VpnIPSecSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_sa_strength_enforcement

    @enable_sa_strength_enforcement.setter
    def enable_sa_strength_enforcement(self, enable_sa_strength_enforcement):
        """Sets the enable_sa_strength_enforcement of this VpnIPSecSettings.


        :param enable_sa_strength_enforcement: The enable_sa_strength_enforcement of this VpnIPSecSettings.  # noqa: E501
        :type: bool
        """

        self._enable_sa_strength_enforcement = enable_sa_strength_enforcement

    @property
    def type(self):
        """Gets the type of this VpnIPSecSettings.  # noqa: E501


        :return: The type of this VpnIPSecSettings.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VpnIPSecSettings.


        :param type: The type of this VpnIPSecSettings.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this VpnIPSecSettings.  # noqa: E501


        :return: The version of this VpnIPSecSettings.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VpnIPSecSettings.


        :param version: The version of this VpnIPSecSettings.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def validate_incoming_icmp_error_message(self):
        """Gets the validate_incoming_icmp_error_message of this VpnIPSecSettings.  # noqa: E501


        :return: The validate_incoming_icmp_error_message of this VpnIPSecSettings.  # noqa: E501
        :rtype: bool
        """
        return self._validate_incoming_icmp_error_message

    @validate_incoming_icmp_error_message.setter
    def validate_incoming_icmp_error_message(self, validate_incoming_icmp_error_message):
        """Sets the validate_incoming_icmp_error_message of this VpnIPSecSettings.


        :param validate_incoming_icmp_error_message: The validate_incoming_icmp_error_message of this VpnIPSecSettings.  # noqa: E501
        :type: bool
        """

        self._validate_incoming_icmp_error_message = validate_incoming_icmp_error_message

    @property
    def lifetime_kilobytes(self):
        """Gets the lifetime_kilobytes of this VpnIPSecSettings.  # noqa: E501


        :return: The lifetime_kilobytes of this VpnIPSecSettings.  # noqa: E501
        :rtype: int
        """
        return self._lifetime_kilobytes

    @lifetime_kilobytes.setter
    def lifetime_kilobytes(self, lifetime_kilobytes):
        """Sets the lifetime_kilobytes of this VpnIPSecSettings.


        :param lifetime_kilobytes: The lifetime_kilobytes of this VpnIPSecSettings.  # noqa: E501
        :type: int
        """

        self._lifetime_kilobytes = lifetime_kilobytes

    @property
    def do_not_fragment_policy(self):
        """Gets the do_not_fragment_policy of this VpnIPSecSettings.  # noqa: E501


        :return: The do_not_fragment_policy of this VpnIPSecSettings.  # noqa: E501
        :rtype: str
        """
        return self._do_not_fragment_policy

    @do_not_fragment_policy.setter
    def do_not_fragment_policy(self, do_not_fragment_policy):
        """Sets the do_not_fragment_policy of this VpnIPSecSettings.


        :param do_not_fragment_policy: The do_not_fragment_policy of this VpnIPSecSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["SET", "COPY", "CLEAR", "NONE"]  # noqa: E501
        if do_not_fragment_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `do_not_fragment_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(do_not_fragment_policy, allowed_values)
            )

        self._do_not_fragment_policy = do_not_fragment_policy

    @property
    def name(self):
        """Gets the name of this VpnIPSecSettings.  # noqa: E501


        :return: The name of this VpnIPSecSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VpnIPSecSettings.


        :param name: The name of this VpnIPSecSettings.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this VpnIPSecSettings.  # noqa: E501


        :return: The links of this VpnIPSecSettings.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VpnIPSecSettings.


        :param links: The links of this VpnIPSecSettings.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this VpnIPSecSettings.  # noqa: E501


        :return: The id of this VpnIPSecSettings.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VpnIPSecSettings.


        :param id: The id of this VpnIPSecSettings.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def enable_rri(self):
        """Gets the enable_rri of this VpnIPSecSettings.  # noqa: E501


        :return: The enable_rri of this VpnIPSecSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_rri

    @enable_rri.setter
    def enable_rri(self, enable_rri):
        """Sets the enable_rri of this VpnIPSecSettings.


        :param enable_rri: The enable_rri of this VpnIPSecSettings.  # noqa: E501
        :type: bool
        """

        self._enable_rri = enable_rri

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
        if issubclass(VpnIPSecSettings, dict):
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
        if not isinstance(other, VpnIPSecSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
