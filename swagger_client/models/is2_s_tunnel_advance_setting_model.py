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


class IS2STunnelAdvanceSettingModel(object):
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
        'nat_keepalive_message_traversal': 'INatKeepaliveTraversal',
        'certificate_map_settings': 'ICertificateMapSettings',
        'enable_spoke_to_spoke_connectivity_through_hub': 'bool',
        'bypass_access_control_traffic_for_decrypted_traffic': 'bool'
    }

    attribute_map = {
        'nat_keepalive_message_traversal': 'natKeepaliveMessageTraversal',
        'certificate_map_settings': 'certificateMapSettings',
        'enable_spoke_to_spoke_connectivity_through_hub': 'enableSpokeToSpokeConnectivityThroughHub',
        'bypass_access_control_traffic_for_decrypted_traffic': 'bypassAccessControlTrafficForDecryptedTraffic'
    }

    def __init__(self, nat_keepalive_message_traversal=None, certificate_map_settings=None, enable_spoke_to_spoke_connectivity_through_hub=None, bypass_access_control_traffic_for_decrypted_traffic=None):  # noqa: E501
        """IS2STunnelAdvanceSettingModel - a model defined in Swagger"""  # noqa: E501

        self._nat_keepalive_message_traversal = None
        self._certificate_map_settings = None
        self._enable_spoke_to_spoke_connectivity_through_hub = None
        self._bypass_access_control_traffic_for_decrypted_traffic = None
        self.discriminator = None

        if nat_keepalive_message_traversal is not None:
            self.nat_keepalive_message_traversal = nat_keepalive_message_traversal
        if certificate_map_settings is not None:
            self.certificate_map_settings = certificate_map_settings
        if enable_spoke_to_spoke_connectivity_through_hub is not None:
            self.enable_spoke_to_spoke_connectivity_through_hub = enable_spoke_to_spoke_connectivity_through_hub
        if bypass_access_control_traffic_for_decrypted_traffic is not None:
            self.bypass_access_control_traffic_for_decrypted_traffic = bypass_access_control_traffic_for_decrypted_traffic

    @property
    def nat_keepalive_message_traversal(self):
        """Gets the nat_keepalive_message_traversal of this IS2STunnelAdvanceSettingModel.  # noqa: E501

        Object representing keepalive message traversal information.  # noqa: E501

        :return: The nat_keepalive_message_traversal of this IS2STunnelAdvanceSettingModel.  # noqa: E501
        :rtype: INatKeepaliveTraversal
        """
        return self._nat_keepalive_message_traversal

    @nat_keepalive_message_traversal.setter
    def nat_keepalive_message_traversal(self, nat_keepalive_message_traversal):
        """Sets the nat_keepalive_message_traversal of this IS2STunnelAdvanceSettingModel.

        Object representing keepalive message traversal information.  # noqa: E501

        :param nat_keepalive_message_traversal: The nat_keepalive_message_traversal of this IS2STunnelAdvanceSettingModel.  # noqa: E501
        :type: INatKeepaliveTraversal
        """

        self._nat_keepalive_message_traversal = nat_keepalive_message_traversal

    @property
    def certificate_map_settings(self):
        """Gets the certificate_map_settings of this IS2STunnelAdvanceSettingModel.  # noqa: E501

        Contains certificate map settings.  # noqa: E501

        :return: The certificate_map_settings of this IS2STunnelAdvanceSettingModel.  # noqa: E501
        :rtype: ICertificateMapSettings
        """
        return self._certificate_map_settings

    @certificate_map_settings.setter
    def certificate_map_settings(self, certificate_map_settings):
        """Sets the certificate_map_settings of this IS2STunnelAdvanceSettingModel.

        Contains certificate map settings.  # noqa: E501

        :param certificate_map_settings: The certificate_map_settings of this IS2STunnelAdvanceSettingModel.  # noqa: E501
        :type: ICertificateMapSettings
        """

        self._certificate_map_settings = certificate_map_settings

    @property
    def enable_spoke_to_spoke_connectivity_through_hub(self):
        """Gets the enable_spoke_to_spoke_connectivity_through_hub of this IS2STunnelAdvanceSettingModel.  # noqa: E501

        Indicates whether spoke-to-spoke connectivity is enabled through the hub.  # noqa: E501

        :return: The enable_spoke_to_spoke_connectivity_through_hub of this IS2STunnelAdvanceSettingModel.  # noqa: E501
        :rtype: bool
        """
        return self._enable_spoke_to_spoke_connectivity_through_hub

    @enable_spoke_to_spoke_connectivity_through_hub.setter
    def enable_spoke_to_spoke_connectivity_through_hub(self, enable_spoke_to_spoke_connectivity_through_hub):
        """Sets the enable_spoke_to_spoke_connectivity_through_hub of this IS2STunnelAdvanceSettingModel.

        Indicates whether spoke-to-spoke connectivity is enabled through the hub.  # noqa: E501

        :param enable_spoke_to_spoke_connectivity_through_hub: The enable_spoke_to_spoke_connectivity_through_hub of this IS2STunnelAdvanceSettingModel.  # noqa: E501
        :type: bool
        """

        self._enable_spoke_to_spoke_connectivity_through_hub = enable_spoke_to_spoke_connectivity_through_hub

    @property
    def bypass_access_control_traffic_for_decrypted_traffic(self):
        """Gets the bypass_access_control_traffic_for_decrypted_traffic of this IS2STunnelAdvanceSettingModel.  # noqa: E501

        Indicates whether to bypass access control for decrypted traffic.  # noqa: E501

        :return: The bypass_access_control_traffic_for_decrypted_traffic of this IS2STunnelAdvanceSettingModel.  # noqa: E501
        :rtype: bool
        """
        return self._bypass_access_control_traffic_for_decrypted_traffic

    @bypass_access_control_traffic_for_decrypted_traffic.setter
    def bypass_access_control_traffic_for_decrypted_traffic(self, bypass_access_control_traffic_for_decrypted_traffic):
        """Sets the bypass_access_control_traffic_for_decrypted_traffic of this IS2STunnelAdvanceSettingModel.

        Indicates whether to bypass access control for decrypted traffic.  # noqa: E501

        :param bypass_access_control_traffic_for_decrypted_traffic: The bypass_access_control_traffic_for_decrypted_traffic of this IS2STunnelAdvanceSettingModel.  # noqa: E501
        :type: bool
        """

        self._bypass_access_control_traffic_for_decrypted_traffic = bypass_access_control_traffic_for_decrypted_traffic

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
        if issubclass(IS2STunnelAdvanceSettingModel, dict):
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
        if not isinstance(other, IS2STunnelAdvanceSettingModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other