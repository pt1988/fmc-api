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


class IFTDHAFailoverInterfacePolicyTrigger(object):
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
        'percent_failed_interface_exceed': 'int',
        'metadata': 'IMetadata',
        'peer_hold_time_unit': 'str',
        'description': 'str',
        'peer_hold_time': 'int',
        'type': 'str',
        'version': 'str',
        'interface_poll_time': 'int',
        'no_of_failed_interface_limit': 'int',
        'peer_poll_time': 'int',
        'interface_hold_time': 'int',
        'name': 'str',
        'links': 'ILinks',
        'id': 'str',
        'peer_poll_time_unit': 'str',
        'interface_poll_time_unit': 'str'
    }

    attribute_map = {
        'percent_failed_interface_exceed': 'percentFailedInterfaceExceed',
        'metadata': 'metadata',
        'peer_hold_time_unit': 'peerHoldTimeUnit',
        'description': 'description',
        'peer_hold_time': 'peerHoldTime',
        'type': 'type',
        'version': 'version',
        'interface_poll_time': 'interfacePollTime',
        'no_of_failed_interface_limit': 'noOfFailedInterfaceLimit',
        'peer_poll_time': 'peerPollTime',
        'interface_hold_time': 'interfaceHoldTime',
        'name': 'name',
        'links': 'links',
        'id': 'id',
        'peer_poll_time_unit': 'peerPollTimeUnit',
        'interface_poll_time_unit': 'interfacePollTimeUnit'
    }

    def __init__(self, percent_failed_interface_exceed=None, metadata=None, peer_hold_time_unit=None, description=None, peer_hold_time=None, type=None, version=None, interface_poll_time=None, no_of_failed_interface_limit=None, peer_poll_time=None, interface_hold_time=None, name=None, links=None, id=None, peer_poll_time_unit=None, interface_poll_time_unit=None):  # noqa: E501
        """IFTDHAFailoverInterfacePolicyTrigger - a model defined in Swagger"""  # noqa: E501

        self._percent_failed_interface_exceed = None
        self._metadata = None
        self._peer_hold_time_unit = None
        self._description = None
        self._peer_hold_time = None
        self._type = None
        self._version = None
        self._interface_poll_time = None
        self._no_of_failed_interface_limit = None
        self._peer_poll_time = None
        self._interface_hold_time = None
        self._name = None
        self._links = None
        self._id = None
        self._peer_poll_time_unit = None
        self._interface_poll_time_unit = None
        self.discriminator = None

        if percent_failed_interface_exceed is not None:
            self.percent_failed_interface_exceed = percent_failed_interface_exceed
        if metadata is not None:
            self.metadata = metadata
        self.peer_hold_time_unit = peer_hold_time_unit
        if description is not None:
            self.description = description
        self.peer_hold_time = peer_hold_time
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        self.interface_poll_time = interface_poll_time
        if no_of_failed_interface_limit is not None:
            self.no_of_failed_interface_limit = no_of_failed_interface_limit
        self.peer_poll_time = peer_poll_time
        self.interface_hold_time = interface_hold_time
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        self.peer_poll_time_unit = peer_poll_time_unit
        self.interface_poll_time_unit = interface_poll_time_unit

    @property
    def percent_failed_interface_exceed(self):
        """Gets the percent_failed_interface_exceed of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The percent_failed_interface_exceed of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: int
        """
        return self._percent_failed_interface_exceed

    @percent_failed_interface_exceed.setter
    def percent_failed_interface_exceed(self, percent_failed_interface_exceed):
        """Sets the percent_failed_interface_exceed of this IFTDHAFailoverInterfacePolicyTrigger.


        :param percent_failed_interface_exceed: The percent_failed_interface_exceed of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: int
        """

        self._percent_failed_interface_exceed = percent_failed_interface_exceed

    @property
    def metadata(self):
        """Gets the metadata of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The metadata of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IFTDHAFailoverInterfacePolicyTrigger.


        :param metadata: The metadata of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def peer_hold_time_unit(self):
        """Gets the peer_hold_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The peer_hold_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: str
        """
        return self._peer_hold_time_unit

    @peer_hold_time_unit.setter
    def peer_hold_time_unit(self, peer_hold_time_unit):
        """Sets the peer_hold_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.


        :param peer_hold_time_unit: The peer_hold_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: str
        """
        if peer_hold_time_unit is None:
            raise ValueError("Invalid value for `peer_hold_time_unit`, must not be `None`")  # noqa: E501
        allowed_values = ["SEC", "MSEC"]  # noqa: E501
        if peer_hold_time_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `peer_hold_time_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(peer_hold_time_unit, allowed_values)
            )

        self._peer_hold_time_unit = peer_hold_time_unit

    @property
    def description(self):
        """Gets the description of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The description of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IFTDHAFailoverInterfacePolicyTrigger.


        :param description: The description of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def peer_hold_time(self):
        """Gets the peer_hold_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The peer_hold_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: int
        """
        return self._peer_hold_time

    @peer_hold_time.setter
    def peer_hold_time(self, peer_hold_time):
        """Sets the peer_hold_time of this IFTDHAFailoverInterfacePolicyTrigger.


        :param peer_hold_time: The peer_hold_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: int
        """
        if peer_hold_time is None:
            raise ValueError("Invalid value for `peer_hold_time`, must not be `None`")  # noqa: E501

        self._peer_hold_time = peer_hold_time

    @property
    def type(self):
        """Gets the type of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The type of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IFTDHAFailoverInterfacePolicyTrigger.


        :param type: The type of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The version of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IFTDHAFailoverInterfacePolicyTrigger.


        :param version: The version of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def interface_poll_time(self):
        """Gets the interface_poll_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The interface_poll_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: int
        """
        return self._interface_poll_time

    @interface_poll_time.setter
    def interface_poll_time(self, interface_poll_time):
        """Sets the interface_poll_time of this IFTDHAFailoverInterfacePolicyTrigger.


        :param interface_poll_time: The interface_poll_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: int
        """
        if interface_poll_time is None:
            raise ValueError("Invalid value for `interface_poll_time`, must not be `None`")  # noqa: E501

        self._interface_poll_time = interface_poll_time

    @property
    def no_of_failed_interface_limit(self):
        """Gets the no_of_failed_interface_limit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The no_of_failed_interface_limit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: int
        """
        return self._no_of_failed_interface_limit

    @no_of_failed_interface_limit.setter
    def no_of_failed_interface_limit(self, no_of_failed_interface_limit):
        """Sets the no_of_failed_interface_limit of this IFTDHAFailoverInterfacePolicyTrigger.


        :param no_of_failed_interface_limit: The no_of_failed_interface_limit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: int
        """

        self._no_of_failed_interface_limit = no_of_failed_interface_limit

    @property
    def peer_poll_time(self):
        """Gets the peer_poll_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The peer_poll_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: int
        """
        return self._peer_poll_time

    @peer_poll_time.setter
    def peer_poll_time(self, peer_poll_time):
        """Sets the peer_poll_time of this IFTDHAFailoverInterfacePolicyTrigger.


        :param peer_poll_time: The peer_poll_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: int
        """
        if peer_poll_time is None:
            raise ValueError("Invalid value for `peer_poll_time`, must not be `None`")  # noqa: E501

        self._peer_poll_time = peer_poll_time

    @property
    def interface_hold_time(self):
        """Gets the interface_hold_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The interface_hold_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: int
        """
        return self._interface_hold_time

    @interface_hold_time.setter
    def interface_hold_time(self, interface_hold_time):
        """Sets the interface_hold_time of this IFTDHAFailoverInterfacePolicyTrigger.


        :param interface_hold_time: The interface_hold_time of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: int
        """
        if interface_hold_time is None:
            raise ValueError("Invalid value for `interface_hold_time`, must not be `None`")  # noqa: E501

        self._interface_hold_time = interface_hold_time

    @property
    def name(self):
        """Gets the name of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The name of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IFTDHAFailoverInterfacePolicyTrigger.


        :param name: The name of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The links of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IFTDHAFailoverInterfacePolicyTrigger.


        :param links: The links of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The id of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IFTDHAFailoverInterfacePolicyTrigger.


        :param id: The id of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def peer_poll_time_unit(self):
        """Gets the peer_poll_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The peer_poll_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: str
        """
        return self._peer_poll_time_unit

    @peer_poll_time_unit.setter
    def peer_poll_time_unit(self, peer_poll_time_unit):
        """Sets the peer_poll_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.


        :param peer_poll_time_unit: The peer_poll_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: str
        """
        if peer_poll_time_unit is None:
            raise ValueError("Invalid value for `peer_poll_time_unit`, must not be `None`")  # noqa: E501
        allowed_values = ["SEC", "MSEC"]  # noqa: E501
        if peer_poll_time_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `peer_poll_time_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(peer_poll_time_unit, allowed_values)
            )

        self._peer_poll_time_unit = peer_poll_time_unit

    @property
    def interface_poll_time_unit(self):
        """Gets the interface_poll_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501


        :return: The interface_poll_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :rtype: str
        """
        return self._interface_poll_time_unit

    @interface_poll_time_unit.setter
    def interface_poll_time_unit(self, interface_poll_time_unit):
        """Sets the interface_poll_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.


        :param interface_poll_time_unit: The interface_poll_time_unit of this IFTDHAFailoverInterfacePolicyTrigger.  # noqa: E501
        :type: str
        """
        if interface_poll_time_unit is None:
            raise ValueError("Invalid value for `interface_poll_time_unit`, must not be `None`")  # noqa: E501
        allowed_values = ["SEC", "MSEC"]  # noqa: E501
        if interface_poll_time_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `interface_poll_time_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(interface_poll_time_unit, allowed_values)
            )

        self._interface_poll_time_unit = interface_poll_time_unit

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
        if issubclass(IFTDHAFailoverInterfacePolicyTrigger, dict):
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
        if not isinstance(other, IFTDHAFailoverInterfacePolicyTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
