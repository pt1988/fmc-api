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


class NetworkObject(object):
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
        'overridable': 'bool',
        'name': 'str',
        'description': 'str',
        'links': 'Links',
        'overrides': 'IOverride',
        'id': 'str',
        'type': 'str',
        'value': 'str',
        'version': 'str',
        'override_target_id': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'overridable': 'overridable',
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'overrides': 'overrides',
        'id': 'id',
        'type': 'type',
        'value': 'value',
        'version': 'version',
        'override_target_id': 'overrideTargetId'
    }

    def __init__(self, metadata=None, overridable=None, name=None, description=None, links=None, overrides=None, id=None, type=None, value=None, version=None, override_target_id=None):  # noqa: E501
        """NetworkObject - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._overridable = None
        self._name = None
        self._description = None
        self._links = None
        self._overrides = None
        self._id = None
        self._type = None
        self._value = None
        self._version = None
        self._override_target_id = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
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
        if value is not None:
            self.value = value
        if version is not None:
            self.version = version
        if override_target_id is not None:
            self.override_target_id = override_target_id

    @property
    def metadata(self):
        """Gets the metadata of this NetworkObject.  # noqa: E501

        Object representing metadata properties of NetworkObject.  # noqa: E501

        :return: The metadata of this NetworkObject.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NetworkObject.

        Object representing metadata properties of NetworkObject.  # noqa: E501

        :param metadata: The metadata of this NetworkObject.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def overridable(self):
        """Gets the overridable of this NetworkObject.  # noqa: E501

        Boolean indicating whether object values can be overridden.  # noqa: E501

        :return: The overridable of this NetworkObject.  # noqa: E501
        :rtype: bool
        """
        return self._overridable

    @overridable.setter
    def overridable(self, overridable):
        """Sets the overridable of this NetworkObject.

        Boolean indicating whether object values can be overridden.  # noqa: E501

        :param overridable: The overridable of this NetworkObject.  # noqa: E501
        :type: bool
        """

        self._overridable = overridable

    @property
    def name(self):
        """Gets the name of this NetworkObject.  # noqa: E501

        User assigned resource name.  # noqa: E501

        :return: The name of this NetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkObject.

        User assigned resource name.  # noqa: E501

        :param name: The name of this NetworkObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this NetworkObject.  # noqa: E501

        User provided resource description.   # noqa: E501

        :return: The description of this NetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetworkObject.

        User provided resource description.   # noqa: E501

        :param description: The description of this NetworkObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this NetworkObject.  # noqa: E501

        Object containing related links.  # noqa: E501

        :return: The links of this NetworkObject.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NetworkObject.

        Object containing related links.  # noqa: E501

        :param links: The links of this NetworkObject.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def overrides(self):
        """Gets the overrides of this NetworkObject.  # noqa: E501

        An object override allows you to define an alternate value for an object on a device or domain.  # noqa: E501

        :return: The overrides of this NetworkObject.  # noqa: E501
        :rtype: IOverride
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this NetworkObject.

        An object override allows you to define an alternate value for an object on a device or domain.  # noqa: E501

        :param overrides: The overrides of this NetworkObject.  # noqa: E501
        :type: IOverride
        """

        self._overrides = overrides

    @property
    def id(self):
        """Gets the id of this NetworkObject.  # noqa: E501

        Unique identifier representing response object.  # noqa: E501

        :return: The id of this NetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkObject.

        Unique identifier representing response object.  # noqa: E501

        :param id: The id of this NetworkObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this NetworkObject.  # noqa: E501

        Type associated with resource: NetworkObject.  # noqa: E501

        :return: The type of this NetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkObject.

        Type associated with resource: NetworkObject.  # noqa: E501

        :param type: The type of this NetworkObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this NetworkObject.  # noqa: E501

        Actual value of the network.  # noqa: E501

        :return: The value of this NetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NetworkObject.

        Actual value of the network.  # noqa: E501

        :param value: The value of this NetworkObject.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def version(self):
        """Gets the version of this NetworkObject.  # noqa: E501

        Version number of the response object.  # noqa: E501

        :return: The version of this NetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NetworkObject.

        Version number of the response object.  # noqa: E501

        :param version: The version of this NetworkObject.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def override_target_id(self):
        """Gets the override_target_id of this NetworkObject.  # noqa: E501

        Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain).  # noqa: E501

        :return: The override_target_id of this NetworkObject.  # noqa: E501
        :rtype: str
        """
        return self._override_target_id

    @override_target_id.setter
    def override_target_id(self, override_target_id):
        """Sets the override_target_id of this NetworkObject.

        Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain).  # noqa: E501

        :param override_target_id: The override_target_id of this NetworkObject.  # noqa: E501
        :type: str
        """

        self._override_target_id = override_target_id

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
        if issubclass(NetworkObject, dict):
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
        if not isinstance(other, NetworkObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
