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


class LLElement(object):
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
        'capabilities': 'list[str]',
        'ca_cert': 'str',
        'description': 'str',
        'misc_data': 'LLMiscData',
        'cert': 'str',
        'type': 'str',
        'version': 'str',
        'name': 'str',
        'registration_date': 'int',
        'action': 'str',
        'model': 'str',
        'id': 'str',
        'key': 'str',
        'status': 'str'
    }

    attribute_map = {
        'capabilities': 'capabilities',
        'ca_cert': 'caCert',
        'description': 'description',
        'misc_data': 'miscData',
        'cert': 'cert',
        'type': 'type',
        'version': 'version',
        'name': 'name',
        'registration_date': 'registrationDate',
        'action': 'action',
        'model': 'model',
        'id': 'id',
        'key': 'key',
        'status': 'status'
    }

    def __init__(self, capabilities=None, ca_cert=None, description=None, misc_data=None, cert=None, type=None, version=None, name=None, registration_date=None, action=None, model=None, id=None, key=None, status=None):  # noqa: E501
        """LLElement - a model defined in Swagger"""  # noqa: E501

        self._capabilities = None
        self._ca_cert = None
        self._description = None
        self._misc_data = None
        self._cert = None
        self._type = None
        self._version = None
        self._name = None
        self._registration_date = None
        self._action = None
        self._model = None
        self._id = None
        self._key = None
        self._status = None
        self.discriminator = None

        if capabilities is not None:
            self.capabilities = capabilities
        if ca_cert is not None:
            self.ca_cert = ca_cert
        if description is not None:
            self.description = description
        if misc_data is not None:
            self.misc_data = misc_data
        if cert is not None:
            self.cert = cert
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if registration_date is not None:
            self.registration_date = registration_date
        if action is not None:
            self.action = action
        if model is not None:
            self.model = model
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if status is not None:
            self.status = status

    @property
    def capabilities(self):
        """Gets the capabilities of this LLElement.  # noqa: E501


        :return: The capabilities of this LLElement.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this LLElement.


        :param capabilities: The capabilities of this LLElement.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

    @property
    def ca_cert(self):
        """Gets the ca_cert of this LLElement.  # noqa: E501


        :return: The ca_cert of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this LLElement.


        :param ca_cert: The ca_cert of this LLElement.  # noqa: E501
        :type: str
        """

        self._ca_cert = ca_cert

    @property
    def description(self):
        """Gets the description of this LLElement.  # noqa: E501


        :return: The description of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LLElement.


        :param description: The description of this LLElement.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def misc_data(self):
        """Gets the misc_data of this LLElement.  # noqa: E501


        :return: The misc_data of this LLElement.  # noqa: E501
        :rtype: LLMiscData
        """
        return self._misc_data

    @misc_data.setter
    def misc_data(self, misc_data):
        """Sets the misc_data of this LLElement.


        :param misc_data: The misc_data of this LLElement.  # noqa: E501
        :type: LLMiscData
        """

        self._misc_data = misc_data

    @property
    def cert(self):
        """Gets the cert of this LLElement.  # noqa: E501


        :return: The cert of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this LLElement.


        :param cert: The cert of this LLElement.  # noqa: E501
        :type: str
        """

        self._cert = cert

    @property
    def type(self):
        """Gets the type of this LLElement.  # noqa: E501


        :return: The type of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LLElement.


        :param type: The type of this LLElement.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this LLElement.  # noqa: E501


        :return: The version of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LLElement.


        :param version: The version of this LLElement.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this LLElement.  # noqa: E501


        :return: The name of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LLElement.


        :param name: The name of this LLElement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def registration_date(self):
        """Gets the registration_date of this LLElement.  # noqa: E501


        :return: The registration_date of this LLElement.  # noqa: E501
        :rtype: int
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this LLElement.


        :param registration_date: The registration_date of this LLElement.  # noqa: E501
        :type: int
        """

        self._registration_date = registration_date

    @property
    def action(self):
        """Gets the action of this LLElement.  # noqa: E501


        :return: The action of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this LLElement.


        :param action: The action of this LLElement.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def model(self):
        """Gets the model of this LLElement.  # noqa: E501


        :return: The model of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this LLElement.


        :param model: The model of this LLElement.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def id(self):
        """Gets the id of this LLElement.  # noqa: E501


        :return: The id of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LLElement.


        :param id: The id of this LLElement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this LLElement.  # noqa: E501


        :return: The key of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LLElement.


        :param key: The key of this LLElement.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def status(self):
        """Gets the status of this LLElement.  # noqa: E501


        :return: The status of this LLElement.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LLElement.


        :param status: The status of this LLElement.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(LLElement, dict):
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
        if not isinstance(other, LLElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
