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


class AccessPolicyInheritanceSetting(object):
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
        'name': 'str',
        'base_policy': 'IReference',
        'description': 'str',
        'links': 'ILinks',
        'id': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'name': 'name',
        'base_policy': 'basePolicy',
        'description': 'description',
        'links': 'links',
        'id': 'id',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, metadata=None, name=None, base_policy=None, description=None, links=None, id=None, type=None, version=None):  # noqa: E501
        """AccessPolicyInheritanceSetting - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._name = None
        self._base_policy = None
        self._description = None
        self._links = None
        self._id = None
        self._type = None
        self._version = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if base_policy is not None:
            self.base_policy = base_policy
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def metadata(self):
        """Gets the metadata of this AccessPolicyInheritanceSetting.  # noqa: E501

        Object representing metadata attributes for the access policy inheritance settings.  # noqa: E501

        :return: The metadata of this AccessPolicyInheritanceSetting.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AccessPolicyInheritanceSetting.

        Object representing metadata attributes for the access policy inheritance settings.  # noqa: E501

        :param metadata: The metadata of this AccessPolicyInheritanceSetting.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this AccessPolicyInheritanceSetting.  # noqa: E501

        User-specified name of the access policy inheritance setting.  # noqa: E501

        :return: The name of this AccessPolicyInheritanceSetting.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessPolicyInheritanceSetting.

        User-specified name of the access policy inheritance setting.  # noqa: E501

        :param name: The name of this AccessPolicyInheritanceSetting.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def base_policy(self):
        """Gets the base_policy of this AccessPolicyInheritanceSetting.  # noqa: E501

        Object specifying the base access policy for inheritance setting  # noqa: E501

        :return: The base_policy of this AccessPolicyInheritanceSetting.  # noqa: E501
        :rtype: IReference
        """
        return self._base_policy

    @base_policy.setter
    def base_policy(self, base_policy):
        """Sets the base_policy of this AccessPolicyInheritanceSetting.

        Object specifying the base access policy for inheritance setting  # noqa: E501

        :param base_policy: The base_policy of this AccessPolicyInheritanceSetting.  # noqa: E501
        :type: IReference
        """

        self._base_policy = base_policy

    @property
    def description(self):
        """Gets the description of this AccessPolicyInheritanceSetting.  # noqa: E501

        Description of Access Policy Inheritance settings  # noqa: E501

        :return: The description of this AccessPolicyInheritanceSetting.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessPolicyInheritanceSetting.

        Description of Access Policy Inheritance settings  # noqa: E501

        :param description: The description of this AccessPolicyInheritanceSetting.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this AccessPolicyInheritanceSetting.  # noqa: E501

        Object containing links to this resource.  # noqa: E501

        :return: The links of this AccessPolicyInheritanceSetting.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AccessPolicyInheritanceSetting.

        Object containing links to this resource.  # noqa: E501

        :param links: The links of this AccessPolicyInheritanceSetting.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this AccessPolicyInheritanceSetting.  # noqa: E501

        Unique identifier (UUID) representing the access policy inheritance setting.  # noqa: E501

        :return: The id of this AccessPolicyInheritanceSetting.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessPolicyInheritanceSetting.

        Unique identifier (UUID) representing the access policy inheritance setting.  # noqa: E501

        :param id: The id of this AccessPolicyInheritanceSetting.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this AccessPolicyInheritanceSetting.  # noqa: E501

        Type of the access control policy inheritance setting; this value is always AccessPolicyInheritanceSetting.  # noqa: E501

        :return: The type of this AccessPolicyInheritanceSetting.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccessPolicyInheritanceSetting.

        Type of the access control policy inheritance setting; this value is always AccessPolicyInheritanceSetting.  # noqa: E501

        :param type: The type of this AccessPolicyInheritanceSetting.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this AccessPolicyInheritanceSetting.  # noqa: E501

        Version number of the response object.  # noqa: E501

        :return: The version of this AccessPolicyInheritanceSetting.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AccessPolicyInheritanceSetting.

        Version number of the response object.  # noqa: E501

        :param version: The version of this AccessPolicyInheritanceSetting.  # noqa: E501
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
        if issubclass(AccessPolicyInheritanceSetting, dict):
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
        if not isinstance(other, AccessPolicyInheritanceSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
