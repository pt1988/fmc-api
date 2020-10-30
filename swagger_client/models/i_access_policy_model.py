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


class IAccessPolicyModel(object):
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
        'default_action': 'IAccessPolicyDefaultAction',
        'name': 'str',
        'description': 'str',
        'rules': 'list[IAccessRuleModel]',
        'links': 'ILinks',
        'prefilter_policy_setting': 'IAccessPolicyPrefilterPolicySettingModel',
        'id': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'default_action': 'defaultAction',
        'name': 'name',
        'description': 'description',
        'rules': 'rules',
        'links': 'links',
        'prefilter_policy_setting': 'prefilterPolicySetting',
        'id': 'id',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, metadata=None, default_action=None, name=None, description=None, rules=None, links=None, prefilter_policy_setting=None, id=None, type=None, version=None):  # noqa: E501
        """IAccessPolicyModel - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._default_action = None
        self._name = None
        self._description = None
        self._rules = None
        self._links = None
        self._prefilter_policy_setting = None
        self._id = None
        self._type = None
        self._version = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        self.default_action = default_action
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if rules is not None:
            self.rules = rules
        if links is not None:
            self.links = links
        if prefilter_policy_setting is not None:
            self.prefilter_policy_setting = prefilter_policy_setting
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def metadata(self):
        """Gets the metadata of this IAccessPolicyModel.  # noqa: E501


        :return: The metadata of this IAccessPolicyModel.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IAccessPolicyModel.


        :param metadata: The metadata of this IAccessPolicyModel.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def default_action(self):
        """Gets the default_action of this IAccessPolicyModel.  # noqa: E501


        :return: The default_action of this IAccessPolicyModel.  # noqa: E501
        :rtype: IAccessPolicyDefaultAction
        """
        return self._default_action

    @default_action.setter
    def default_action(self, default_action):
        """Sets the default_action of this IAccessPolicyModel.


        :param default_action: The default_action of this IAccessPolicyModel.  # noqa: E501
        :type: IAccessPolicyDefaultAction
        """
        if default_action is None:
            raise ValueError("Invalid value for `default_action`, must not be `None`")  # noqa: E501

        self._default_action = default_action

    @property
    def name(self):
        """Gets the name of this IAccessPolicyModel.  # noqa: E501


        :return: The name of this IAccessPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IAccessPolicyModel.


        :param name: The name of this IAccessPolicyModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this IAccessPolicyModel.  # noqa: E501


        :return: The description of this IAccessPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IAccessPolicyModel.


        :param description: The description of this IAccessPolicyModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rules(self):
        """Gets the rules of this IAccessPolicyModel.  # noqa: E501


        :return: The rules of this IAccessPolicyModel.  # noqa: E501
        :rtype: list[IAccessRuleModel]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this IAccessPolicyModel.


        :param rules: The rules of this IAccessPolicyModel.  # noqa: E501
        :type: list[IAccessRuleModel]
        """

        self._rules = rules

    @property
    def links(self):
        """Gets the links of this IAccessPolicyModel.  # noqa: E501


        :return: The links of this IAccessPolicyModel.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IAccessPolicyModel.


        :param links: The links of this IAccessPolicyModel.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def prefilter_policy_setting(self):
        """Gets the prefilter_policy_setting of this IAccessPolicyModel.  # noqa: E501


        :return: The prefilter_policy_setting of this IAccessPolicyModel.  # noqa: E501
        :rtype: IAccessPolicyPrefilterPolicySettingModel
        """
        return self._prefilter_policy_setting

    @prefilter_policy_setting.setter
    def prefilter_policy_setting(self, prefilter_policy_setting):
        """Sets the prefilter_policy_setting of this IAccessPolicyModel.


        :param prefilter_policy_setting: The prefilter_policy_setting of this IAccessPolicyModel.  # noqa: E501
        :type: IAccessPolicyPrefilterPolicySettingModel
        """

        self._prefilter_policy_setting = prefilter_policy_setting

    @property
    def id(self):
        """Gets the id of this IAccessPolicyModel.  # noqa: E501


        :return: The id of this IAccessPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IAccessPolicyModel.


        :param id: The id of this IAccessPolicyModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this IAccessPolicyModel.  # noqa: E501


        :return: The type of this IAccessPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IAccessPolicyModel.


        :param type: The type of this IAccessPolicyModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this IAccessPolicyModel.  # noqa: E501


        :return: The version of this IAccessPolicyModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IAccessPolicyModel.


        :param version: The version of this IAccessPolicyModel.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(IAccessPolicyModel, dict):
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
        if not isinstance(other, IAccessPolicyModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other