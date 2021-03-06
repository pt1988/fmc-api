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


class LLObservable(object):
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
        'misc_data': 'LLMiscData',
        'type': 'str',
        'observable_type': 'str',
        'version': 'str',
        'un_encrypted_db_id': 'str',
        'indicator_count': 'int',
        'effective_property': 'LLFeedProperty',
        'dbid': 'str',
        'id': 'str',
        'value': 'str',
        'inherited_property': 'LLFeedProperty',
        'custom_property': 'LLFeedProperty',
        'updated_at': 'int'
    }

    attribute_map = {
        'misc_data': 'miscData',
        'type': 'type',
        'observable_type': 'observableType',
        'version': 'version',
        'un_encrypted_db_id': 'unEncryptedDBId',
        'indicator_count': 'indicatorCount',
        'effective_property': 'effectiveProperty',
        'dbid': 'dbid',
        'id': 'id',
        'value': 'value',
        'inherited_property': 'inheritedProperty',
        'custom_property': 'customProperty',
        'updated_at': 'updatedAt'
    }

    def __init__(self, misc_data=None, type=None, observable_type=None, version=None, un_encrypted_db_id=None, indicator_count=None, effective_property=None, dbid=None, id=None, value=None, inherited_property=None, custom_property=None, updated_at=None):  # noqa: E501
        """LLObservable - a model defined in Swagger"""  # noqa: E501

        self._misc_data = None
        self._type = None
        self._observable_type = None
        self._version = None
        self._un_encrypted_db_id = None
        self._indicator_count = None
        self._effective_property = None
        self._dbid = None
        self._id = None
        self._value = None
        self._inherited_property = None
        self._custom_property = None
        self._updated_at = None
        self.discriminator = None

        if misc_data is not None:
            self.misc_data = misc_data
        if type is not None:
            self.type = type
        if observable_type is not None:
            self.observable_type = observable_type
        if version is not None:
            self.version = version
        if un_encrypted_db_id is not None:
            self.un_encrypted_db_id = un_encrypted_db_id
        if indicator_count is not None:
            self.indicator_count = indicator_count
        if effective_property is not None:
            self.effective_property = effective_property
        if dbid is not None:
            self.dbid = dbid
        if id is not None:
            self.id = id
        if value is not None:
            self.value = value
        if inherited_property is not None:
            self.inherited_property = inherited_property
        if custom_property is not None:
            self.custom_property = custom_property
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def misc_data(self):
        """Gets the misc_data of this LLObservable.  # noqa: E501


        :return: The misc_data of this LLObservable.  # noqa: E501
        :rtype: LLMiscData
        """
        return self._misc_data

    @misc_data.setter
    def misc_data(self, misc_data):
        """Sets the misc_data of this LLObservable.


        :param misc_data: The misc_data of this LLObservable.  # noqa: E501
        :type: LLMiscData
        """

        self._misc_data = misc_data

    @property
    def type(self):
        """Gets the type of this LLObservable.  # noqa: E501


        :return: The type of this LLObservable.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LLObservable.


        :param type: The type of this LLObservable.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def observable_type(self):
        """Gets the observable_type of this LLObservable.  # noqa: E501


        :return: The observable_type of this LLObservable.  # noqa: E501
        :rtype: str
        """
        return self._observable_type

    @observable_type.setter
    def observable_type(self, observable_type):
        """Sets the observable_type of this LLObservable.


        :param observable_type: The observable_type of this LLObservable.  # noqa: E501
        :type: str
        """

        self._observable_type = observable_type

    @property
    def version(self):
        """Gets the version of this LLObservable.  # noqa: E501


        :return: The version of this LLObservable.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LLObservable.


        :param version: The version of this LLObservable.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def un_encrypted_db_id(self):
        """Gets the un_encrypted_db_id of this LLObservable.  # noqa: E501


        :return: The un_encrypted_db_id of this LLObservable.  # noqa: E501
        :rtype: str
        """
        return self._un_encrypted_db_id

    @un_encrypted_db_id.setter
    def un_encrypted_db_id(self, un_encrypted_db_id):
        """Sets the un_encrypted_db_id of this LLObservable.


        :param un_encrypted_db_id: The un_encrypted_db_id of this LLObservable.  # noqa: E501
        :type: str
        """

        self._un_encrypted_db_id = un_encrypted_db_id

    @property
    def indicator_count(self):
        """Gets the indicator_count of this LLObservable.  # noqa: E501


        :return: The indicator_count of this LLObservable.  # noqa: E501
        :rtype: int
        """
        return self._indicator_count

    @indicator_count.setter
    def indicator_count(self, indicator_count):
        """Sets the indicator_count of this LLObservable.


        :param indicator_count: The indicator_count of this LLObservable.  # noqa: E501
        :type: int
        """

        self._indicator_count = indicator_count

    @property
    def effective_property(self):
        """Gets the effective_property of this LLObservable.  # noqa: E501


        :return: The effective_property of this LLObservable.  # noqa: E501
        :rtype: LLFeedProperty
        """
        return self._effective_property

    @effective_property.setter
    def effective_property(self, effective_property):
        """Sets the effective_property of this LLObservable.


        :param effective_property: The effective_property of this LLObservable.  # noqa: E501
        :type: LLFeedProperty
        """

        self._effective_property = effective_property

    @property
    def dbid(self):
        """Gets the dbid of this LLObservable.  # noqa: E501


        :return: The dbid of this LLObservable.  # noqa: E501
        :rtype: str
        """
        return self._dbid

    @dbid.setter
    def dbid(self, dbid):
        """Sets the dbid of this LLObservable.


        :param dbid: The dbid of this LLObservable.  # noqa: E501
        :type: str
        """

        self._dbid = dbid

    @property
    def id(self):
        """Gets the id of this LLObservable.  # noqa: E501


        :return: The id of this LLObservable.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LLObservable.


        :param id: The id of this LLObservable.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this LLObservable.  # noqa: E501


        :return: The value of this LLObservable.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LLObservable.


        :param value: The value of this LLObservable.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def inherited_property(self):
        """Gets the inherited_property of this LLObservable.  # noqa: E501


        :return: The inherited_property of this LLObservable.  # noqa: E501
        :rtype: LLFeedProperty
        """
        return self._inherited_property

    @inherited_property.setter
    def inherited_property(self, inherited_property):
        """Sets the inherited_property of this LLObservable.


        :param inherited_property: The inherited_property of this LLObservable.  # noqa: E501
        :type: LLFeedProperty
        """

        self._inherited_property = inherited_property

    @property
    def custom_property(self):
        """Gets the custom_property of this LLObservable.  # noqa: E501


        :return: The custom_property of this LLObservable.  # noqa: E501
        :rtype: LLFeedProperty
        """
        return self._custom_property

    @custom_property.setter
    def custom_property(self, custom_property):
        """Sets the custom_property of this LLObservable.


        :param custom_property: The custom_property of this LLObservable.  # noqa: E501
        :type: LLFeedProperty
        """

        self._custom_property = custom_property

    @property
    def updated_at(self):
        """Gets the updated_at of this LLObservable.  # noqa: E501


        :return: The updated_at of this LLObservable.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LLObservable.


        :param updated_at: The updated_at of this LLObservable.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

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
        if issubclass(LLObservable, dict):
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
        if not isinstance(other, LLObservable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
