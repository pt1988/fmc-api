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


class IRouteInjection(object):
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
        'inject_map': 'IRouteMap',
        'name': 'str',
        'copy_attributes': 'bool',
        'links': 'ILinks',
        'id': 'str',
        'exist_map': 'IRouteMap',
        'type': 'str'
    }

    attribute_map = {
        'inject_map': 'injectMap',
        'name': 'name',
        'copy_attributes': 'copyAttributes',
        'links': 'links',
        'id': 'id',
        'exist_map': 'existMap',
        'type': 'type'
    }

    def __init__(self, inject_map=None, name=None, copy_attributes=None, links=None, id=None, exist_map=None, type=None):  # noqa: E501
        """IRouteInjection - a model defined in Swagger"""  # noqa: E501

        self._inject_map = None
        self._name = None
        self._copy_attributes = None
        self._links = None
        self._id = None
        self._exist_map = None
        self._type = None
        self.discriminator = None

        if inject_map is not None:
            self.inject_map = inject_map
        if name is not None:
            self.name = name
        if copy_attributes is not None:
            self.copy_attributes = copy_attributes
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if exist_map is not None:
            self.exist_map = exist_map
        if type is not None:
            self.type = type

    @property
    def inject_map(self):
        """Gets the inject_map of this IRouteInjection.  # noqa: E501


        :return: The inject_map of this IRouteInjection.  # noqa: E501
        :rtype: IRouteMap
        """
        return self._inject_map

    @inject_map.setter
    def inject_map(self, inject_map):
        """Sets the inject_map of this IRouteInjection.


        :param inject_map: The inject_map of this IRouteInjection.  # noqa: E501
        :type: IRouteMap
        """

        self._inject_map = inject_map

    @property
    def name(self):
        """Gets the name of this IRouteInjection.  # noqa: E501


        :return: The name of this IRouteInjection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IRouteInjection.


        :param name: The name of this IRouteInjection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def copy_attributes(self):
        """Gets the copy_attributes of this IRouteInjection.  # noqa: E501


        :return: The copy_attributes of this IRouteInjection.  # noqa: E501
        :rtype: bool
        """
        return self._copy_attributes

    @copy_attributes.setter
    def copy_attributes(self, copy_attributes):
        """Sets the copy_attributes of this IRouteInjection.


        :param copy_attributes: The copy_attributes of this IRouteInjection.  # noqa: E501
        :type: bool
        """

        self._copy_attributes = copy_attributes

    @property
    def links(self):
        """Gets the links of this IRouteInjection.  # noqa: E501


        :return: The links of this IRouteInjection.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IRouteInjection.


        :param links: The links of this IRouteInjection.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IRouteInjection.  # noqa: E501


        :return: The id of this IRouteInjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IRouteInjection.


        :param id: The id of this IRouteInjection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def exist_map(self):
        """Gets the exist_map of this IRouteInjection.  # noqa: E501


        :return: The exist_map of this IRouteInjection.  # noqa: E501
        :rtype: IRouteMap
        """
        return self._exist_map

    @exist_map.setter
    def exist_map(self, exist_map):
        """Sets the exist_map of this IRouteInjection.


        :param exist_map: The exist_map of this IRouteInjection.  # noqa: E501
        :type: IRouteMap
        """

        self._exist_map = exist_map

    @property
    def type(self):
        """Gets the type of this IRouteInjection.  # noqa: E501


        :return: The type of this IRouteInjection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IRouteInjection.


        :param type: The type of this IRouteInjection.  # noqa: E501
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
        if issubclass(IRouteInjection, dict):
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
        if not isinstance(other, IRouteInjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
