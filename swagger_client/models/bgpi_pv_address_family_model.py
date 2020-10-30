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


class BGPIPvAddressFamilyModel(object):
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
        'router_id': 'str',
        'as_number': 'str',
        'name': 'str',
        'address_family_i_pv4': 'IBGPAddressFamilyModel',
        'description': 'str',
        'links': 'ILinks',
        'id': 'str',
        'address_family_i_pv6': 'IBGPAddressFamilyModel',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'router_id': 'routerId',
        'as_number': 'asNumber',
        'name': 'name',
        'address_family_i_pv4': 'addressFamilyIPv4',
        'description': 'description',
        'links': 'links',
        'id': 'id',
        'address_family_i_pv6': 'addressFamilyIPv6',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, metadata=None, router_id=None, as_number=None, name=None, address_family_i_pv4=None, description=None, links=None, id=None, address_family_i_pv6=None, type=None, version=None):  # noqa: E501
        """BGPIPvAddressFamilyModel - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._router_id = None
        self._as_number = None
        self._name = None
        self._address_family_i_pv4 = None
        self._description = None
        self._links = None
        self._id = None
        self._address_family_i_pv6 = None
        self._type = None
        self._version = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        self.router_id = router_id
        if as_number is not None:
            self.as_number = as_number
        if name is not None:
            self.name = name
        if address_family_i_pv4 is not None:
            self.address_family_i_pv4 = address_family_i_pv4
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if address_family_i_pv6 is not None:
            self.address_family_i_pv6 = address_family_i_pv6
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def metadata(self):
        """Gets the metadata of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The metadata of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this BGPIPvAddressFamilyModel.


        :param metadata: The metadata of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def router_id(self):
        """Gets the router_id of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The router_id of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this BGPIPvAddressFamilyModel.


        :param router_id: The router_id of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: str
        """
        if router_id is None:
            raise ValueError("Invalid value for `router_id`, must not be `None`")  # noqa: E501

        self._router_id = router_id

    @property
    def as_number(self):
        """Gets the as_number of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The as_number of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: str
        """
        return self._as_number

    @as_number.setter
    def as_number(self, as_number):
        """Sets the as_number of this BGPIPvAddressFamilyModel.


        :param as_number: The as_number of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: str
        """

        self._as_number = as_number

    @property
    def name(self):
        """Gets the name of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The name of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BGPIPvAddressFamilyModel.


        :param name: The name of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address_family_i_pv4(self):
        """Gets the address_family_i_pv4 of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The address_family_i_pv4 of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: IBGPAddressFamilyModel
        """
        return self._address_family_i_pv4

    @address_family_i_pv4.setter
    def address_family_i_pv4(self, address_family_i_pv4):
        """Sets the address_family_i_pv4 of this BGPIPvAddressFamilyModel.


        :param address_family_i_pv4: The address_family_i_pv4 of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: IBGPAddressFamilyModel
        """

        self._address_family_i_pv4 = address_family_i_pv4

    @property
    def description(self):
        """Gets the description of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The description of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BGPIPvAddressFamilyModel.


        :param description: The description of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The links of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BGPIPvAddressFamilyModel.


        :param links: The links of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The id of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BGPIPvAddressFamilyModel.


        :param id: The id of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def address_family_i_pv6(self):
        """Gets the address_family_i_pv6 of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The address_family_i_pv6 of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: IBGPAddressFamilyModel
        """
        return self._address_family_i_pv6

    @address_family_i_pv6.setter
    def address_family_i_pv6(self, address_family_i_pv6):
        """Sets the address_family_i_pv6 of this BGPIPvAddressFamilyModel.


        :param address_family_i_pv6: The address_family_i_pv6 of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: IBGPAddressFamilyModel
        """

        self._address_family_i_pv6 = address_family_i_pv6

    @property
    def type(self):
        """Gets the type of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The type of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BGPIPvAddressFamilyModel.


        :param type: The type of this BGPIPvAddressFamilyModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this BGPIPvAddressFamilyModel.  # noqa: E501


        :return: The version of this BGPIPvAddressFamilyModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BGPIPvAddressFamilyModel.


        :param version: The version of this BGPIPvAddressFamilyModel.  # noqa: E501
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
        if issubclass(BGPIPvAddressFamilyModel, dict):
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
        if not isinstance(other, BGPIPvAddressFamilyModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
