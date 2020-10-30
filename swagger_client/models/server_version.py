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


class ServerVersion(object):
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
        'server_version': 'str',
        'vdb_version': 'str',
        'metadata': 'IMetadata',
        'name': 'str',
        'description': 'str',
        'links': 'ILinks',
        'geo_version': 'str',
        'id': 'str',
        'sru_version': 'str',
        'type': 'str'
    }

    attribute_map = {
        'server_version': 'serverVersion',
        'vdb_version': 'vdbVersion',
        'metadata': 'metadata',
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'geo_version': 'geoVersion',
        'id': 'id',
        'sru_version': 'sruVersion',
        'type': 'type'
    }

    def __init__(self, server_version=None, vdb_version=None, metadata=None, name=None, description=None, links=None, geo_version=None, id=None, sru_version=None, type=None):  # noqa: E501
        """ServerVersion - a model defined in Swagger"""  # noqa: E501

        self._server_version = None
        self._vdb_version = None
        self._metadata = None
        self._name = None
        self._description = None
        self._links = None
        self._geo_version = None
        self._id = None
        self._sru_version = None
        self._type = None
        self.discriminator = None

        if server_version is not None:
            self.server_version = server_version
        if vdb_version is not None:
            self.vdb_version = vdb_version
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if geo_version is not None:
            self.geo_version = geo_version
        if id is not None:
            self.id = id
        if sru_version is not None:
            self.sru_version = sru_version
        if type is not None:
            self.type = type

    @property
    def server_version(self):
        """Gets the server_version of this ServerVersion.  # noqa: E501


        :return: The server_version of this ServerVersion.  # noqa: E501
        :rtype: str
        """
        return self._server_version

    @server_version.setter
    def server_version(self, server_version):
        """Sets the server_version of this ServerVersion.


        :param server_version: The server_version of this ServerVersion.  # noqa: E501
        :type: str
        """

        self._server_version = server_version

    @property
    def vdb_version(self):
        """Gets the vdb_version of this ServerVersion.  # noqa: E501


        :return: The vdb_version of this ServerVersion.  # noqa: E501
        :rtype: str
        """
        return self._vdb_version

    @vdb_version.setter
    def vdb_version(self, vdb_version):
        """Sets the vdb_version of this ServerVersion.


        :param vdb_version: The vdb_version of this ServerVersion.  # noqa: E501
        :type: str
        """

        self._vdb_version = vdb_version

    @property
    def metadata(self):
        """Gets the metadata of this ServerVersion.  # noqa: E501


        :return: The metadata of this ServerVersion.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ServerVersion.


        :param metadata: The metadata of this ServerVersion.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ServerVersion.  # noqa: E501


        :return: The name of this ServerVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerVersion.


        :param name: The name of this ServerVersion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ServerVersion.  # noqa: E501


        :return: The description of this ServerVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServerVersion.


        :param description: The description of this ServerVersion.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this ServerVersion.  # noqa: E501


        :return: The links of this ServerVersion.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ServerVersion.


        :param links: The links of this ServerVersion.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def geo_version(self):
        """Gets the geo_version of this ServerVersion.  # noqa: E501


        :return: The geo_version of this ServerVersion.  # noqa: E501
        :rtype: str
        """
        return self._geo_version

    @geo_version.setter
    def geo_version(self, geo_version):
        """Sets the geo_version of this ServerVersion.


        :param geo_version: The geo_version of this ServerVersion.  # noqa: E501
        :type: str
        """

        self._geo_version = geo_version

    @property
    def id(self):
        """Gets the id of this ServerVersion.  # noqa: E501


        :return: The id of this ServerVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerVersion.


        :param id: The id of this ServerVersion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sru_version(self):
        """Gets the sru_version of this ServerVersion.  # noqa: E501


        :return: The sru_version of this ServerVersion.  # noqa: E501
        :rtype: str
        """
        return self._sru_version

    @sru_version.setter
    def sru_version(self, sru_version):
        """Sets the sru_version of this ServerVersion.


        :param sru_version: The sru_version of this ServerVersion.  # noqa: E501
        :type: str
        """

        self._sru_version = sru_version

    @property
    def type(self):
        """Gets the type of this ServerVersion.  # noqa: E501


        :return: The type of this ServerVersion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServerVersion.


        :param type: The type of this ServerVersion.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ServerVersion, dict):
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
        if not isinstance(other, ServerVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
