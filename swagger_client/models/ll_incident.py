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


class LLIncident(object):
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
        'indicator_name': 'str',
        'equation': 'LLEquationNode',
        'description': 'str',
        'type': 'str',
        'version': 'str',
        'indicator_id': 'str',
        'action_taken': 'str',
        'feed_id': 'str',
        'observations': 'list[LLObservation]',
        'publish': 'bool',
        'name': 'str',
        '_property': 'LLFeedProperty',
        'id': 'str',
        'source_name': 'str',
        'realized_at': 'int',
        'status': 'str',
        'updated_at': 'int'
    }

    attribute_map = {
        'indicator_name': 'indicatorName',
        'equation': 'equation',
        'description': 'description',
        'type': 'type',
        'version': 'version',
        'indicator_id': 'indicatorId',
        'action_taken': 'actionTaken',
        'feed_id': 'feedId',
        'observations': 'observations',
        'publish': 'publish',
        'name': 'name',
        '_property': 'property',
        'id': 'id',
        'source_name': 'sourceName',
        'realized_at': 'realizedAt',
        'status': 'status',
        'updated_at': 'updatedAt'
    }

    def __init__(self, indicator_name=None, equation=None, description=None, type=None, version=None, indicator_id=None, action_taken=None, feed_id=None, observations=None, publish=None, name=None, _property=None, id=None, source_name=None, realized_at=None, status=None, updated_at=None):  # noqa: E501
        """LLIncident - a model defined in Swagger"""  # noqa: E501

        self._indicator_name = None
        self._equation = None
        self._description = None
        self._type = None
        self._version = None
        self._indicator_id = None
        self._action_taken = None
        self._feed_id = None
        self._observations = None
        self._publish = None
        self._name = None
        self.__property = None
        self._id = None
        self._source_name = None
        self._realized_at = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        if indicator_name is not None:
            self.indicator_name = indicator_name
        if equation is not None:
            self.equation = equation
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if indicator_id is not None:
            self.indicator_id = indicator_id
        if action_taken is not None:
            self.action_taken = action_taken
        if feed_id is not None:
            self.feed_id = feed_id
        if observations is not None:
            self.observations = observations
        if publish is not None:
            self.publish = publish
        if name is not None:
            self.name = name
        if _property is not None:
            self._property = _property
        if id is not None:
            self.id = id
        if source_name is not None:
            self.source_name = source_name
        if realized_at is not None:
            self.realized_at = realized_at
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def indicator_name(self):
        """Gets the indicator_name of this LLIncident.  # noqa: E501


        :return: The indicator_name of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._indicator_name

    @indicator_name.setter
    def indicator_name(self, indicator_name):
        """Sets the indicator_name of this LLIncident.


        :param indicator_name: The indicator_name of this LLIncident.  # noqa: E501
        :type: str
        """

        self._indicator_name = indicator_name

    @property
    def equation(self):
        """Gets the equation of this LLIncident.  # noqa: E501


        :return: The equation of this LLIncident.  # noqa: E501
        :rtype: LLEquationNode
        """
        return self._equation

    @equation.setter
    def equation(self, equation):
        """Sets the equation of this LLIncident.


        :param equation: The equation of this LLIncident.  # noqa: E501
        :type: LLEquationNode
        """

        self._equation = equation

    @property
    def description(self):
        """Gets the description of this LLIncident.  # noqa: E501


        :return: The description of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LLIncident.


        :param description: The description of this LLIncident.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this LLIncident.  # noqa: E501


        :return: The type of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LLIncident.


        :param type: The type of this LLIncident.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this LLIncident.  # noqa: E501


        :return: The version of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LLIncident.


        :param version: The version of this LLIncident.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def indicator_id(self):
        """Gets the indicator_id of this LLIncident.  # noqa: E501


        :return: The indicator_id of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this LLIncident.


        :param indicator_id: The indicator_id of this LLIncident.  # noqa: E501
        :type: str
        """

        self._indicator_id = indicator_id

    @property
    def action_taken(self):
        """Gets the action_taken of this LLIncident.  # noqa: E501


        :return: The action_taken of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._action_taken

    @action_taken.setter
    def action_taken(self, action_taken):
        """Sets the action_taken of this LLIncident.


        :param action_taken: The action_taken of this LLIncident.  # noqa: E501
        :type: str
        """

        self._action_taken = action_taken

    @property
    def feed_id(self):
        """Gets the feed_id of this LLIncident.  # noqa: E501


        :return: The feed_id of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this LLIncident.


        :param feed_id: The feed_id of this LLIncident.  # noqa: E501
        :type: str
        """

        self._feed_id = feed_id

    @property
    def observations(self):
        """Gets the observations of this LLIncident.  # noqa: E501


        :return: The observations of this LLIncident.  # noqa: E501
        :rtype: list[LLObservation]
        """
        return self._observations

    @observations.setter
    def observations(self, observations):
        """Sets the observations of this LLIncident.


        :param observations: The observations of this LLIncident.  # noqa: E501
        :type: list[LLObservation]
        """

        self._observations = observations

    @property
    def publish(self):
        """Gets the publish of this LLIncident.  # noqa: E501


        :return: The publish of this LLIncident.  # noqa: E501
        :rtype: bool
        """
        return self._publish

    @publish.setter
    def publish(self, publish):
        """Sets the publish of this LLIncident.


        :param publish: The publish of this LLIncident.  # noqa: E501
        :type: bool
        """

        self._publish = publish

    @property
    def name(self):
        """Gets the name of this LLIncident.  # noqa: E501


        :return: The name of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LLIncident.


        :param name: The name of this LLIncident.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def _property(self):
        """Gets the _property of this LLIncident.  # noqa: E501


        :return: The _property of this LLIncident.  # noqa: E501
        :rtype: LLFeedProperty
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this LLIncident.


        :param _property: The _property of this LLIncident.  # noqa: E501
        :type: LLFeedProperty
        """

        self.__property = _property

    @property
    def id(self):
        """Gets the id of this LLIncident.  # noqa: E501


        :return: The id of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LLIncident.


        :param id: The id of this LLIncident.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source_name(self):
        """Gets the source_name of this LLIncident.  # noqa: E501


        :return: The source_name of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this LLIncident.


        :param source_name: The source_name of this LLIncident.  # noqa: E501
        :type: str
        """

        self._source_name = source_name

    @property
    def realized_at(self):
        """Gets the realized_at of this LLIncident.  # noqa: E501


        :return: The realized_at of this LLIncident.  # noqa: E501
        :rtype: int
        """
        return self._realized_at

    @realized_at.setter
    def realized_at(self, realized_at):
        """Sets the realized_at of this LLIncident.


        :param realized_at: The realized_at of this LLIncident.  # noqa: E501
        :type: int
        """

        self._realized_at = realized_at

    @property
    def status(self):
        """Gets the status of this LLIncident.  # noqa: E501


        :return: The status of this LLIncident.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LLIncident.


        :param status: The status of this LLIncident.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this LLIncident.  # noqa: E501


        :return: The updated_at of this LLIncident.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LLIncident.


        :param updated_at: The updated_at of this LLIncident.  # noqa: E501
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
        if issubclass(LLIncident, dict):
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
        if not isinstance(other, LLIncident):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
