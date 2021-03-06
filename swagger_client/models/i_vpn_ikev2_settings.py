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


class IVpnIkev2Settings(object):
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
        'automatic_pre_shared_key_length': 'int',
        'certificate_auth': 'IReference',
        'enforce_hex_based_pre_shared_key_only': 'bool',
        'authentication_type': 'str',
        'manual_pre_shared_key': 'str',
        'policy': 'IReference'
    }

    attribute_map = {
        'automatic_pre_shared_key_length': 'automaticPreSharedKeyLength',
        'certificate_auth': 'certificateAuth',
        'enforce_hex_based_pre_shared_key_only': 'enforceHexBasedPreSharedKeyOnly',
        'authentication_type': 'authenticationType',
        'manual_pre_shared_key': 'manualPreSharedKey',
        'policy': 'policy'
    }

    def __init__(self, automatic_pre_shared_key_length=None, certificate_auth=None, enforce_hex_based_pre_shared_key_only=None, authentication_type=None, manual_pre_shared_key=None, policy=None):  # noqa: E501
        """IVpnIkev2Settings - a model defined in Swagger"""  # noqa: E501

        self._automatic_pre_shared_key_length = None
        self._certificate_auth = None
        self._enforce_hex_based_pre_shared_key_only = None
        self._authentication_type = None
        self._manual_pre_shared_key = None
        self._policy = None
        self.discriminator = None

        if automatic_pre_shared_key_length is not None:
            self.automatic_pre_shared_key_length = automatic_pre_shared_key_length
        if certificate_auth is not None:
            self.certificate_auth = certificate_auth
        if enforce_hex_based_pre_shared_key_only is not None:
            self.enforce_hex_based_pre_shared_key_only = enforce_hex_based_pre_shared_key_only
        if authentication_type is not None:
            self.authentication_type = authentication_type
        if manual_pre_shared_key is not None:
            self.manual_pre_shared_key = manual_pre_shared_key
        if policy is not None:
            self.policy = policy

    @property
    def automatic_pre_shared_key_length(self):
        """Gets the automatic_pre_shared_key_length of this IVpnIkev2Settings.  # noqa: E501


        :return: The automatic_pre_shared_key_length of this IVpnIkev2Settings.  # noqa: E501
        :rtype: int
        """
        return self._automatic_pre_shared_key_length

    @automatic_pre_shared_key_length.setter
    def automatic_pre_shared_key_length(self, automatic_pre_shared_key_length):
        """Sets the automatic_pre_shared_key_length of this IVpnIkev2Settings.


        :param automatic_pre_shared_key_length: The automatic_pre_shared_key_length of this IVpnIkev2Settings.  # noqa: E501
        :type: int
        """

        self._automatic_pre_shared_key_length = automatic_pre_shared_key_length

    @property
    def certificate_auth(self):
        """Gets the certificate_auth of this IVpnIkev2Settings.  # noqa: E501

        Signing authority used for the VPN certificate.  # noqa: E501

        :return: The certificate_auth of this IVpnIkev2Settings.  # noqa: E501
        :rtype: IReference
        """
        return self._certificate_auth

    @certificate_auth.setter
    def certificate_auth(self, certificate_auth):
        """Sets the certificate_auth of this IVpnIkev2Settings.

        Signing authority used for the VPN certificate.  # noqa: E501

        :param certificate_auth: The certificate_auth of this IVpnIkev2Settings.  # noqa: E501
        :type: IReference
        """

        self._certificate_auth = certificate_auth

    @property
    def enforce_hex_based_pre_shared_key_only(self):
        """Gets the enforce_hex_based_pre_shared_key_only of this IVpnIkev2Settings.  # noqa: E501


        :return: The enforce_hex_based_pre_shared_key_only of this IVpnIkev2Settings.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_hex_based_pre_shared_key_only

    @enforce_hex_based_pre_shared_key_only.setter
    def enforce_hex_based_pre_shared_key_only(self, enforce_hex_based_pre_shared_key_only):
        """Sets the enforce_hex_based_pre_shared_key_only of this IVpnIkev2Settings.


        :param enforce_hex_based_pre_shared_key_only: The enforce_hex_based_pre_shared_key_only of this IVpnIkev2Settings.  # noqa: E501
        :type: bool
        """

        self._enforce_hex_based_pre_shared_key_only = enforce_hex_based_pre_shared_key_only

    @property
    def authentication_type(self):
        """Gets the authentication_type of this IVpnIkev2Settings.  # noqa: E501

        Type of authentication used for the VPN.  # noqa: E501

        :return: The authentication_type of this IVpnIkev2Settings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this IVpnIkev2Settings.

        Type of authentication used for the VPN.  # noqa: E501

        :param authentication_type: The authentication_type of this IVpnIkev2Settings.  # noqa: E501
        :type: str
        """
        allowed_values = ["MANUAL_PRE_SHARED_KEY", "AUTOMATIC_PRE_SHARED_KEY", "CERTIFICATE"]  # noqa: E501
        if authentication_type not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_type` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_type, allowed_values)
            )

        self._authentication_type = authentication_type

    @property
    def manual_pre_shared_key(self):
        """Gets the manual_pre_shared_key of this IVpnIkev2Settings.  # noqa: E501

        Contains the manual pre-shared key for the VPN, if any.  # noqa: E501

        :return: The manual_pre_shared_key of this IVpnIkev2Settings.  # noqa: E501
        :rtype: str
        """
        return self._manual_pre_shared_key

    @manual_pre_shared_key.setter
    def manual_pre_shared_key(self, manual_pre_shared_key):
        """Sets the manual_pre_shared_key of this IVpnIkev2Settings.

        Contains the manual pre-shared key for the VPN, if any.  # noqa: E501

        :param manual_pre_shared_key: The manual_pre_shared_key of this IVpnIkev2Settings.  # noqa: E501
        :type: str
        """

        self._manual_pre_shared_key = manual_pre_shared_key

    @property
    def policy(self):
        """Gets the policy of this IVpnIkev2Settings.  # noqa: E501

        VPN policy.  # noqa: E501

        :return: The policy of this IVpnIkev2Settings.  # noqa: E501
        :rtype: IReference
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this IVpnIkev2Settings.

        VPN policy.  # noqa: E501

        :param policy: The policy of this IVpnIkev2Settings.  # noqa: E501
        :type: IReference
        """

        self._policy = policy

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
        if issubclass(IVpnIkev2Settings, dict):
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
        if not isinstance(other, IVpnIkev2Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
