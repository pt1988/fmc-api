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


class InterfaceEvent(object):
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
        'has_pending_changes': 'bool',
        'metadata': 'Metadata',
        'change': 'str',
        'name': 'str',
        'action': 'str',
        'description': 'str',
        'links': 'ILinks',
        'state': 'str',
        'id': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'has_pending_changes': 'hasPendingChanges',
        'metadata': 'metadata',
        'change': 'change',
        'name': 'name',
        'action': 'action',
        'description': 'description',
        'links': 'links',
        'state': 'state',
        'id': 'id',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, has_pending_changes=None, metadata=None, change=None, name=None, action=None, description=None, links=None, state=None, id=None, type=None, version=None):  # noqa: E501
        """InterfaceEvent - a model defined in Swagger"""  # noqa: E501

        self._has_pending_changes = None
        self._metadata = None
        self._change = None
        self._name = None
        self._action = None
        self._description = None
        self._links = None
        self._state = None
        self._id = None
        self._type = None
        self._version = None
        self.discriminator = None

        if has_pending_changes is not None:
            self.has_pending_changes = has_pending_changes
        if metadata is not None:
            self.metadata = metadata
        if change is not None:
            self.change = change
        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if state is not None:
            self.state = state
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def has_pending_changes(self):
        """Gets the has_pending_changes of this InterfaceEvent.  # noqa: E501


        :return: The has_pending_changes of this InterfaceEvent.  # noqa: E501
        :rtype: bool
        """
        return self._has_pending_changes

    @has_pending_changes.setter
    def has_pending_changes(self, has_pending_changes):
        """Sets the has_pending_changes of this InterfaceEvent.


        :param has_pending_changes: The has_pending_changes of this InterfaceEvent.  # noqa: E501
        :type: bool
        """

        self._has_pending_changes = has_pending_changes

    @property
    def metadata(self):
        """Gets the metadata of this InterfaceEvent.  # noqa: E501


        :return: The metadata of this InterfaceEvent.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InterfaceEvent.


        :param metadata: The metadata of this InterfaceEvent.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def change(self):
        """Gets the change of this InterfaceEvent.  # noqa: E501


        :return: The change of this InterfaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this InterfaceEvent.


        :param change: The change of this InterfaceEvent.  # noqa: E501
        :type: str
        """

        self._change = change

    @property
    def name(self):
        """Gets the name of this InterfaceEvent.  # noqa: E501


        :return: The name of this InterfaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InterfaceEvent.


        :param name: The name of this InterfaceEvent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def action(self):
        """Gets the action of this InterfaceEvent.  # noqa: E501


        :return: The action of this InterfaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InterfaceEvent.


        :param action: The action of this InterfaceEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYNC_WITH_DEVICE", "ACCEPT_CHANGES"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def description(self):
        """Gets the description of this InterfaceEvent.  # noqa: E501


        :return: The description of this InterfaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InterfaceEvent.


        :param description: The description of this InterfaceEvent.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this InterfaceEvent.  # noqa: E501


        :return: The links of this InterfaceEvent.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InterfaceEvent.


        :param links: The links of this InterfaceEvent.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def state(self):
        """Gets the state of this InterfaceEvent.  # noqa: E501


        :return: The state of this InterfaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InterfaceEvent.


        :param state: The state of this InterfaceEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["DISASSOCIATED", "ASSOCIATED", "MODIFIED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def id(self):
        """Gets the id of this InterfaceEvent.  # noqa: E501


        :return: The id of this InterfaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InterfaceEvent.


        :param id: The id of this InterfaceEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this InterfaceEvent.  # noqa: E501


        :return: The type of this InterfaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InterfaceEvent.


        :param type: The type of this InterfaceEvent.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this InterfaceEvent.  # noqa: E501


        :return: The version of this InterfaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InterfaceEvent.


        :param version: The version of this InterfaceEvent.  # noqa: E501
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
        if issubclass(InterfaceEvent, dict):
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
        if not isinstance(other, InterfaceEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
