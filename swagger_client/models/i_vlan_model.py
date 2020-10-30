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


class IVlanModel(object):
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
        'data': 'IVlanTagLiteral',
        'overridable': 'bool',
        'name': 'str',
        'description': 'str',
        'links': 'ILinks',
        'overrides': 'IOverride',
        'id': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'data': 'data',
        'overridable': 'overridable',
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'overrides': 'overrides',
        'id': 'id',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, metadata=None, data=None, overridable=None, name=None, description=None, links=None, overrides=None, id=None, type=None, version=None):  # noqa: E501
        """IVlanModel - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._data = None
        self._overridable = None
        self._name = None
        self._description = None
        self._links = None
        self._overrides = None
        self._id = None
        self._type = None
        self._version = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if data is not None:
            self.data = data
        if overridable is not None:
            self.overridable = overridable
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if overrides is not None:
            self.overrides = overrides
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def metadata(self):
        """Gets the metadata of this IVlanModel.  # noqa: E501


        :return: The metadata of this IVlanModel.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IVlanModel.


        :param metadata: The metadata of this IVlanModel.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def data(self):
        """Gets the data of this IVlanModel.  # noqa: E501


        :return: The data of this IVlanModel.  # noqa: E501
        :rtype: IVlanTagLiteral
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this IVlanModel.


        :param data: The data of this IVlanModel.  # noqa: E501
        :type: IVlanTagLiteral
        """

        self._data = data

    @property
    def overridable(self):
        """Gets the overridable of this IVlanModel.  # noqa: E501


        :return: The overridable of this IVlanModel.  # noqa: E501
        :rtype: bool
        """
        return self._overridable

    @overridable.setter
    def overridable(self, overridable):
        """Sets the overridable of this IVlanModel.


        :param overridable: The overridable of this IVlanModel.  # noqa: E501
        :type: bool
        """

        self._overridable = overridable

    @property
    def name(self):
        """Gets the name of this IVlanModel.  # noqa: E501


        :return: The name of this IVlanModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IVlanModel.


        :param name: The name of this IVlanModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this IVlanModel.  # noqa: E501


        :return: The description of this IVlanModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IVlanModel.


        :param description: The description of this IVlanModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this IVlanModel.  # noqa: E501


        :return: The links of this IVlanModel.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IVlanModel.


        :param links: The links of this IVlanModel.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def overrides(self):
        """Gets the overrides of this IVlanModel.  # noqa: E501


        :return: The overrides of this IVlanModel.  # noqa: E501
        :rtype: IOverride
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this IVlanModel.


        :param overrides: The overrides of this IVlanModel.  # noqa: E501
        :type: IOverride
        """

        self._overrides = overrides

    @property
    def id(self):
        """Gets the id of this IVlanModel.  # noqa: E501


        :return: The id of this IVlanModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IVlanModel.


        :param id: The id of this IVlanModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this IVlanModel.  # noqa: E501


        :return: The type of this IVlanModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IVlanModel.


        :param type: The type of this IVlanModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this IVlanModel.  # noqa: E501


        :return: The version of this IVlanModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IVlanModel.


        :param version: The version of this IVlanModel.  # noqa: E501
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
        if issubclass(IVlanModel, dict):
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
        if not isinstance(other, IVlanModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
