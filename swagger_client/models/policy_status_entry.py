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


class PolicyStatusEntry(object):
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
        'is_up_to_date': 'bool',
        'policy_id': 'str',
        'policy_name': 'str',
        'policy_type': 'str',
        'referred_policy_list': 'list[PolicyStatusEntry]',
        'selected': 'bool',
        'current_version': 'int'
    }

    attribute_map = {
        'is_up_to_date': 'isUpToDate',
        'policy_id': 'policyId',
        'policy_name': 'policyName',
        'policy_type': 'policyType',
        'referred_policy_list': 'referredPolicyList',
        'selected': 'selected',
        'current_version': 'currentVersion'
    }

    def __init__(self, is_up_to_date=None, policy_id=None, policy_name=None, policy_type=None, referred_policy_list=None, selected=None, current_version=None):  # noqa: E501
        """PolicyStatusEntry - a model defined in Swagger"""  # noqa: E501

        self._is_up_to_date = None
        self._policy_id = None
        self._policy_name = None
        self._policy_type = None
        self._referred_policy_list = None
        self._selected = None
        self._current_version = None
        self.discriminator = None

        if is_up_to_date is not None:
            self.is_up_to_date = is_up_to_date
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_type is not None:
            self.policy_type = policy_type
        if referred_policy_list is not None:
            self.referred_policy_list = referred_policy_list
        if selected is not None:
            self.selected = selected
        if current_version is not None:
            self.current_version = current_version

    @property
    def is_up_to_date(self):
        """Gets the is_up_to_date of this PolicyStatusEntry.  # noqa: E501


        :return: The is_up_to_date of this PolicyStatusEntry.  # noqa: E501
        :rtype: bool
        """
        return self._is_up_to_date

    @is_up_to_date.setter
    def is_up_to_date(self, is_up_to_date):
        """Sets the is_up_to_date of this PolicyStatusEntry.


        :param is_up_to_date: The is_up_to_date of this PolicyStatusEntry.  # noqa: E501
        :type: bool
        """

        self._is_up_to_date = is_up_to_date

    @property
    def policy_id(self):
        """Gets the policy_id of this PolicyStatusEntry.  # noqa: E501


        :return: The policy_id of this PolicyStatusEntry.  # noqa: E501
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this PolicyStatusEntry.


        :param policy_id: The policy_id of this PolicyStatusEntry.  # noqa: E501
        :type: str
        """

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this PolicyStatusEntry.  # noqa: E501


        :return: The policy_name of this PolicyStatusEntry.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this PolicyStatusEntry.


        :param policy_name: The policy_name of this PolicyStatusEntry.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def policy_type(self):
        """Gets the policy_type of this PolicyStatusEntry.  # noqa: E501


        :return: The policy_type of this PolicyStatusEntry.  # noqa: E501
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this PolicyStatusEntry.


        :param policy_type: The policy_type of this PolicyStatusEntry.  # noqa: E501
        :type: str
        """

        self._policy_type = policy_type

    @property
    def referred_policy_list(self):
        """Gets the referred_policy_list of this PolicyStatusEntry.  # noqa: E501


        :return: The referred_policy_list of this PolicyStatusEntry.  # noqa: E501
        :rtype: list[PolicyStatusEntry]
        """
        return self._referred_policy_list

    @referred_policy_list.setter
    def referred_policy_list(self, referred_policy_list):
        """Sets the referred_policy_list of this PolicyStatusEntry.


        :param referred_policy_list: The referred_policy_list of this PolicyStatusEntry.  # noqa: E501
        :type: list[PolicyStatusEntry]
        """

        self._referred_policy_list = referred_policy_list

    @property
    def selected(self):
        """Gets the selected of this PolicyStatusEntry.  # noqa: E501


        :return: The selected of this PolicyStatusEntry.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this PolicyStatusEntry.


        :param selected: The selected of this PolicyStatusEntry.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def current_version(self):
        """Gets the current_version of this PolicyStatusEntry.  # noqa: E501


        :return: The current_version of this PolicyStatusEntry.  # noqa: E501
        :rtype: int
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this PolicyStatusEntry.


        :param current_version: The current_version of this PolicyStatusEntry.  # noqa: E501
        :type: int
        """

        self._current_version = current_version

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
        if issubclass(PolicyStatusEntry, dict):
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
        if not isinstance(other, PolicyStatusEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
