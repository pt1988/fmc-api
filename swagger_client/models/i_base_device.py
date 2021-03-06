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


class IBaseDevice(object):
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
        'advanced': 'IAdvanced',
        'model_id': 'str',
        'description': 'str',
        'model_type': 'str',
        'type': 'str',
        'version': 'str',
        'sw_version': 'str',
        'health_status': 'str',
        'health_policy': 'IHealthPolicy',
        'name': 'str',
        'model_number': 'str',
        'model': 'str',
        'links': 'ILinks',
        'access_policy': 'IPolicyModel',
        'id': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'advanced': 'advanced',
        'model_id': 'modelId',
        'description': 'description',
        'model_type': 'modelType',
        'type': 'type',
        'version': 'version',
        'sw_version': 'sw_version',
        'health_status': 'healthStatus',
        'health_policy': 'healthPolicy',
        'name': 'name',
        'model_number': 'modelNumber',
        'model': 'model',
        'links': 'links',
        'access_policy': 'accessPolicy',
        'id': 'id'
    }

    def __init__(self, metadata=None, advanced=None, model_id=None, description=None, model_type=None, type=None, version=None, sw_version=None, health_status=None, health_policy=None, name=None, model_number=None, model=None, links=None, access_policy=None, id=None):  # noqa: E501
        """IBaseDevice - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._advanced = None
        self._model_id = None
        self._description = None
        self._model_type = None
        self._type = None
        self._version = None
        self._sw_version = None
        self._health_status = None
        self._health_policy = None
        self._name = None
        self._model_number = None
        self._model = None
        self._links = None
        self._access_policy = None
        self._id = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if advanced is not None:
            self.advanced = advanced
        if model_id is not None:
            self.model_id = model_id
        if description is not None:
            self.description = description
        if model_type is not None:
            self.model_type = model_type
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if sw_version is not None:
            self.sw_version = sw_version
        if health_status is not None:
            self.health_status = health_status
        if health_policy is not None:
            self.health_policy = health_policy
        if name is not None:
            self.name = name
        if model_number is not None:
            self.model_number = model_number
        if model is not None:
            self.model = model
        if links is not None:
            self.links = links
        if access_policy is not None:
            self.access_policy = access_policy
        if id is not None:
            self.id = id

    @property
    def metadata(self):
        """Gets the metadata of this IBaseDevice.  # noqa: E501


        :return: The metadata of this IBaseDevice.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IBaseDevice.


        :param metadata: The metadata of this IBaseDevice.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def advanced(self):
        """Gets the advanced of this IBaseDevice.  # noqa: E501


        :return: The advanced of this IBaseDevice.  # noqa: E501
        :rtype: IAdvanced
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this IBaseDevice.


        :param advanced: The advanced of this IBaseDevice.  # noqa: E501
        :type: IAdvanced
        """

        self._advanced = advanced

    @property
    def model_id(self):
        """Gets the model_id of this IBaseDevice.  # noqa: E501


        :return: The model_id of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this IBaseDevice.


        :param model_id: The model_id of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

    @property
    def description(self):
        """Gets the description of this IBaseDevice.  # noqa: E501


        :return: The description of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IBaseDevice.


        :param description: The description of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def model_type(self):
        """Gets the model_type of this IBaseDevice.  # noqa: E501


        :return: The model_type of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this IBaseDevice.


        :param model_type: The model_type of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._model_type = model_type

    @property
    def type(self):
        """Gets the type of this IBaseDevice.  # noqa: E501


        :return: The type of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IBaseDevice.


        :param type: The type of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this IBaseDevice.  # noqa: E501


        :return: The version of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IBaseDevice.


        :param version: The version of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def sw_version(self):
        """Gets the sw_version of this IBaseDevice.  # noqa: E501


        :return: The sw_version of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._sw_version

    @sw_version.setter
    def sw_version(self, sw_version):
        """Sets the sw_version of this IBaseDevice.


        :param sw_version: The sw_version of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._sw_version = sw_version

    @property
    def health_status(self):
        """Gets the health_status of this IBaseDevice.  # noqa: E501


        :return: The health_status of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this IBaseDevice.


        :param health_status: The health_status of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._health_status = health_status

    @property
    def health_policy(self):
        """Gets the health_policy of this IBaseDevice.  # noqa: E501


        :return: The health_policy of this IBaseDevice.  # noqa: E501
        :rtype: IHealthPolicy
        """
        return self._health_policy

    @health_policy.setter
    def health_policy(self, health_policy):
        """Sets the health_policy of this IBaseDevice.


        :param health_policy: The health_policy of this IBaseDevice.  # noqa: E501
        :type: IHealthPolicy
        """

        self._health_policy = health_policy

    @property
    def name(self):
        """Gets the name of this IBaseDevice.  # noqa: E501


        :return: The name of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IBaseDevice.


        :param name: The name of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def model_number(self):
        """Gets the model_number of this IBaseDevice.  # noqa: E501


        :return: The model_number of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._model_number

    @model_number.setter
    def model_number(self, model_number):
        """Sets the model_number of this IBaseDevice.


        :param model_number: The model_number of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._model_number = model_number

    @property
    def model(self):
        """Gets the model of this IBaseDevice.  # noqa: E501


        :return: The model of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this IBaseDevice.


        :param model: The model of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def links(self):
        """Gets the links of this IBaseDevice.  # noqa: E501


        :return: The links of this IBaseDevice.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IBaseDevice.


        :param links: The links of this IBaseDevice.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def access_policy(self):
        """Gets the access_policy of this IBaseDevice.  # noqa: E501


        :return: The access_policy of this IBaseDevice.  # noqa: E501
        :rtype: IPolicyModel
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this IBaseDevice.


        :param access_policy: The access_policy of this IBaseDevice.  # noqa: E501
        :type: IPolicyModel
        """

        self._access_policy = access_policy

    @property
    def id(self):
        """Gets the id of this IBaseDevice.  # noqa: E501


        :return: The id of this IBaseDevice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IBaseDevice.


        :param id: The id of this IBaseDevice.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(IBaseDevice, dict):
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
        if not isinstance(other, IBaseDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
