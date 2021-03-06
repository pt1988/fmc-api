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


class IBGPGSGracefulRestart(object):
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
        'graceful_restart': 'bool',
        'graceful_restart_stale_path_time': 'int',
        'name': 'str',
        'graceful_restart_restart_time': 'int',
        'links': 'ILinks',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'graceful_restart': 'gracefulRestart',
        'graceful_restart_stale_path_time': 'gracefulRestartStalePathTime',
        'name': 'name',
        'graceful_restart_restart_time': 'gracefulRestartRestartTime',
        'links': 'links',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, graceful_restart=None, graceful_restart_stale_path_time=None, name=None, graceful_restart_restart_time=None, links=None, id=None, type=None):  # noqa: E501
        """IBGPGSGracefulRestart - a model defined in Swagger"""  # noqa: E501

        self._graceful_restart = None
        self._graceful_restart_stale_path_time = None
        self._name = None
        self._graceful_restart_restart_time = None
        self._links = None
        self._id = None
        self._type = None
        self.discriminator = None

        if graceful_restart is not None:
            self.graceful_restart = graceful_restart
        if graceful_restart_stale_path_time is not None:
            self.graceful_restart_stale_path_time = graceful_restart_stale_path_time
        if name is not None:
            self.name = name
        if graceful_restart_restart_time is not None:
            self.graceful_restart_restart_time = graceful_restart_restart_time
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def graceful_restart(self):
        """Gets the graceful_restart of this IBGPGSGracefulRestart.  # noqa: E501


        :return: The graceful_restart of this IBGPGSGracefulRestart.  # noqa: E501
        :rtype: bool
        """
        return self._graceful_restart

    @graceful_restart.setter
    def graceful_restart(self, graceful_restart):
        """Sets the graceful_restart of this IBGPGSGracefulRestart.


        :param graceful_restart: The graceful_restart of this IBGPGSGracefulRestart.  # noqa: E501
        :type: bool
        """

        self._graceful_restart = graceful_restart

    @property
    def graceful_restart_stale_path_time(self):
        """Gets the graceful_restart_stale_path_time of this IBGPGSGracefulRestart.  # noqa: E501


        :return: The graceful_restart_stale_path_time of this IBGPGSGracefulRestart.  # noqa: E501
        :rtype: int
        """
        return self._graceful_restart_stale_path_time

    @graceful_restart_stale_path_time.setter
    def graceful_restart_stale_path_time(self, graceful_restart_stale_path_time):
        """Sets the graceful_restart_stale_path_time of this IBGPGSGracefulRestart.


        :param graceful_restart_stale_path_time: The graceful_restart_stale_path_time of this IBGPGSGracefulRestart.  # noqa: E501
        :type: int
        """

        self._graceful_restart_stale_path_time = graceful_restart_stale_path_time

    @property
    def name(self):
        """Gets the name of this IBGPGSGracefulRestart.  # noqa: E501


        :return: The name of this IBGPGSGracefulRestart.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IBGPGSGracefulRestart.


        :param name: The name of this IBGPGSGracefulRestart.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def graceful_restart_restart_time(self):
        """Gets the graceful_restart_restart_time of this IBGPGSGracefulRestart.  # noqa: E501


        :return: The graceful_restart_restart_time of this IBGPGSGracefulRestart.  # noqa: E501
        :rtype: int
        """
        return self._graceful_restart_restart_time

    @graceful_restart_restart_time.setter
    def graceful_restart_restart_time(self, graceful_restart_restart_time):
        """Sets the graceful_restart_restart_time of this IBGPGSGracefulRestart.


        :param graceful_restart_restart_time: The graceful_restart_restart_time of this IBGPGSGracefulRestart.  # noqa: E501
        :type: int
        """

        self._graceful_restart_restart_time = graceful_restart_restart_time

    @property
    def links(self):
        """Gets the links of this IBGPGSGracefulRestart.  # noqa: E501


        :return: The links of this IBGPGSGracefulRestart.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IBGPGSGracefulRestart.


        :param links: The links of this IBGPGSGracefulRestart.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IBGPGSGracefulRestart.  # noqa: E501


        :return: The id of this IBGPGSGracefulRestart.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IBGPGSGracefulRestart.


        :param id: The id of this IBGPGSGracefulRestart.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this IBGPGSGracefulRestart.  # noqa: E501


        :return: The type of this IBGPGSGracefulRestart.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IBGPGSGracefulRestart.


        :param type: The type of this IBGPGSGracefulRestart.  # noqa: E501
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
        if issubclass(IBGPGSGracefulRestart, dict):
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
        if not isinstance(other, IBGPGSGracefulRestart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
