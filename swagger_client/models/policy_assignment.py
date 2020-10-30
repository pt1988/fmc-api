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


class PolicyAssignment(object):
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
        'description': 'str',
        'links': 'Links',
        'id': 'str',
        'type': 'str',
        'targets': 'list[ITarget]',
        'version': 'str',
        'policy': 'IPolicyModel'
    }

    attribute_map = {
        'metadata': 'metadata',
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'id': 'id',
        'type': 'type',
        'targets': 'targets',
        'version': 'version',
        'policy': 'policy'
    }

    def __init__(self, metadata=None, name=None, description=None, links=None, id=None, type=None, targets=None, version=None, policy=None):  # noqa: E501
        """PolicyAssignment - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._name = None
        self._description = None
        self._links = None
        self._id = None
        self._type = None
        self._targets = None
        self._version = None
        self._policy = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if targets is not None:
            self.targets = targets
        if version is not None:
            self.version = version
        if policy is not None:
            self.policy = policy

    @property
    def metadata(self):
        """Gets the metadata of this PolicyAssignment.  # noqa: E501


        :return: The metadata of this PolicyAssignment.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PolicyAssignment.


        :param metadata: The metadata of this PolicyAssignment.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PolicyAssignment.  # noqa: E501


        :return: The name of this PolicyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyAssignment.


        :param name: The name of this PolicyAssignment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PolicyAssignment.  # noqa: E501


        :return: The description of this PolicyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyAssignment.


        :param description: The description of this PolicyAssignment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this PolicyAssignment.  # noqa: E501


        :return: The links of this PolicyAssignment.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyAssignment.


        :param links: The links of this PolicyAssignment.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this PolicyAssignment.  # noqa: E501


        :return: The id of this PolicyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyAssignment.


        :param id: The id of this PolicyAssignment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this PolicyAssignment.  # noqa: E501


        :return: The type of this PolicyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyAssignment.


        :param type: The type of this PolicyAssignment.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def targets(self):
        """Gets the targets of this PolicyAssignment.  # noqa: E501


        :return: The targets of this PolicyAssignment.  # noqa: E501
        :rtype: list[ITarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this PolicyAssignment.


        :param targets: The targets of this PolicyAssignment.  # noqa: E501
        :type: list[ITarget]
        """

        self._targets = targets

    @property
    def version(self):
        """Gets the version of this PolicyAssignment.  # noqa: E501


        :return: The version of this PolicyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PolicyAssignment.


        :param version: The version of this PolicyAssignment.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def policy(self):
        """Gets the policy of this PolicyAssignment.  # noqa: E501


        :return: The policy of this PolicyAssignment.  # noqa: E501
        :rtype: IPolicyModel
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PolicyAssignment.


        :param policy: The policy of this PolicyAssignment.  # noqa: E501
        :type: IPolicyModel
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
        if issubclass(PolicyAssignment, dict):
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
        if not isinstance(other, PolicyAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
