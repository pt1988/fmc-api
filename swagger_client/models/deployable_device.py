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


class DeployableDevice(object):
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
        'device_members': 'list[IDevice]',
        'can_be_deployed': 'bool',
        'metadata': 'Metadata',
        'policy_status_list': 'list[IPolicyStatus]',
        'description': 'str',
        'message': 'str',
        'type': 'str',
        'version': 'str',
        'entry': 'DeviceStatusEntry',
        'up_to_date': 'bool',
        'domain': 'IDomain',
        'is_deploying': 'bool',
        'is_selected': 'bool',
        'name': 'str',
        'links': 'ILinks',
        'id': 'str',
        'traffic_interruption': 'str',
        'device': 'IDevice',
        'group': 'IDeviceGroup'
    }

    attribute_map = {
        'device_members': 'deviceMembers',
        'can_be_deployed': 'canBeDeployed',
        'metadata': 'metadata',
        'policy_status_list': 'policyStatusList',
        'description': 'description',
        'message': 'message',
        'type': 'type',
        'version': 'version',
        'entry': 'entry',
        'up_to_date': 'upToDate',
        'domain': 'domain',
        'is_deploying': 'isDeploying',
        'is_selected': 'isSelected',
        'name': 'name',
        'links': 'links',
        'id': 'id',
        'traffic_interruption': 'trafficInterruption',
        'device': 'device',
        'group': 'group'
    }

    def __init__(self, device_members=None, can_be_deployed=None, metadata=None, policy_status_list=None, description=None, message=None, type=None, version=None, entry=None, up_to_date=None, domain=None, is_deploying=None, is_selected=None, name=None, links=None, id=None, traffic_interruption=None, device=None, group=None):  # noqa: E501
        """DeployableDevice - a model defined in Swagger"""  # noqa: E501

        self._device_members = None
        self._can_be_deployed = None
        self._metadata = None
        self._policy_status_list = None
        self._description = None
        self._message = None
        self._type = None
        self._version = None
        self._entry = None
        self._up_to_date = None
        self._domain = None
        self._is_deploying = None
        self._is_selected = None
        self._name = None
        self._links = None
        self._id = None
        self._traffic_interruption = None
        self._device = None
        self._group = None
        self.discriminator = None

        if device_members is not None:
            self.device_members = device_members
        if can_be_deployed is not None:
            self.can_be_deployed = can_be_deployed
        if metadata is not None:
            self.metadata = metadata
        if policy_status_list is not None:
            self.policy_status_list = policy_status_list
        if description is not None:
            self.description = description
        if message is not None:
            self.message = message
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if entry is not None:
            self.entry = entry
        if up_to_date is not None:
            self.up_to_date = up_to_date
        if domain is not None:
            self.domain = domain
        if is_deploying is not None:
            self.is_deploying = is_deploying
        if is_selected is not None:
            self.is_selected = is_selected
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if traffic_interruption is not None:
            self.traffic_interruption = traffic_interruption
        if device is not None:
            self.device = device
        if group is not None:
            self.group = group

    @property
    def device_members(self):
        """Gets the device_members of this DeployableDevice.  # noqa: E501


        :return: The device_members of this DeployableDevice.  # noqa: E501
        :rtype: list[IDevice]
        """
        return self._device_members

    @device_members.setter
    def device_members(self, device_members):
        """Sets the device_members of this DeployableDevice.


        :param device_members: The device_members of this DeployableDevice.  # noqa: E501
        :type: list[IDevice]
        """

        self._device_members = device_members

    @property
    def can_be_deployed(self):
        """Gets the can_be_deployed of this DeployableDevice.  # noqa: E501


        :return: The can_be_deployed of this DeployableDevice.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_deployed

    @can_be_deployed.setter
    def can_be_deployed(self, can_be_deployed):
        """Sets the can_be_deployed of this DeployableDevice.


        :param can_be_deployed: The can_be_deployed of this DeployableDevice.  # noqa: E501
        :type: bool
        """

        self._can_be_deployed = can_be_deployed

    @property
    def metadata(self):
        """Gets the metadata of this DeployableDevice.  # noqa: E501


        :return: The metadata of this DeployableDevice.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DeployableDevice.


        :param metadata: The metadata of this DeployableDevice.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def policy_status_list(self):
        """Gets the policy_status_list of this DeployableDevice.  # noqa: E501


        :return: The policy_status_list of this DeployableDevice.  # noqa: E501
        :rtype: list[IPolicyStatus]
        """
        return self._policy_status_list

    @policy_status_list.setter
    def policy_status_list(self, policy_status_list):
        """Sets the policy_status_list of this DeployableDevice.


        :param policy_status_list: The policy_status_list of this DeployableDevice.  # noqa: E501
        :type: list[IPolicyStatus]
        """

        self._policy_status_list = policy_status_list

    @property
    def description(self):
        """Gets the description of this DeployableDevice.  # noqa: E501


        :return: The description of this DeployableDevice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeployableDevice.


        :param description: The description of this DeployableDevice.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def message(self):
        """Gets the message of this DeployableDevice.  # noqa: E501


        :return: The message of this DeployableDevice.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeployableDevice.


        :param message: The message of this DeployableDevice.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def type(self):
        """Gets the type of this DeployableDevice.  # noqa: E501


        :return: The type of this DeployableDevice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeployableDevice.


        :param type: The type of this DeployableDevice.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this DeployableDevice.  # noqa: E501


        :return: The version of this DeployableDevice.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeployableDevice.


        :param version: The version of this DeployableDevice.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def entry(self):
        """Gets the entry of this DeployableDevice.  # noqa: E501


        :return: The entry of this DeployableDevice.  # noqa: E501
        :rtype: DeviceStatusEntry
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this DeployableDevice.


        :param entry: The entry of this DeployableDevice.  # noqa: E501
        :type: DeviceStatusEntry
        """

        self._entry = entry

    @property
    def up_to_date(self):
        """Gets the up_to_date of this DeployableDevice.  # noqa: E501


        :return: The up_to_date of this DeployableDevice.  # noqa: E501
        :rtype: bool
        """
        return self._up_to_date

    @up_to_date.setter
    def up_to_date(self, up_to_date):
        """Sets the up_to_date of this DeployableDevice.


        :param up_to_date: The up_to_date of this DeployableDevice.  # noqa: E501
        :type: bool
        """

        self._up_to_date = up_to_date

    @property
    def domain(self):
        """Gets the domain of this DeployableDevice.  # noqa: E501


        :return: The domain of this DeployableDevice.  # noqa: E501
        :rtype: IDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DeployableDevice.


        :param domain: The domain of this DeployableDevice.  # noqa: E501
        :type: IDomain
        """

        self._domain = domain

    @property
    def is_deploying(self):
        """Gets the is_deploying of this DeployableDevice.  # noqa: E501


        :return: The is_deploying of this DeployableDevice.  # noqa: E501
        :rtype: bool
        """
        return self._is_deploying

    @is_deploying.setter
    def is_deploying(self, is_deploying):
        """Sets the is_deploying of this DeployableDevice.


        :param is_deploying: The is_deploying of this DeployableDevice.  # noqa: E501
        :type: bool
        """

        self._is_deploying = is_deploying

    @property
    def is_selected(self):
        """Gets the is_selected of this DeployableDevice.  # noqa: E501


        :return: The is_selected of this DeployableDevice.  # noqa: E501
        :rtype: bool
        """
        return self._is_selected

    @is_selected.setter
    def is_selected(self, is_selected):
        """Sets the is_selected of this DeployableDevice.


        :param is_selected: The is_selected of this DeployableDevice.  # noqa: E501
        :type: bool
        """

        self._is_selected = is_selected

    @property
    def name(self):
        """Gets the name of this DeployableDevice.  # noqa: E501


        :return: The name of this DeployableDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeployableDevice.


        :param name: The name of this DeployableDevice.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this DeployableDevice.  # noqa: E501


        :return: The links of this DeployableDevice.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DeployableDevice.


        :param links: The links of this DeployableDevice.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this DeployableDevice.  # noqa: E501


        :return: The id of this DeployableDevice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeployableDevice.


        :param id: The id of this DeployableDevice.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def traffic_interruption(self):
        """Gets the traffic_interruption of this DeployableDevice.  # noqa: E501


        :return: The traffic_interruption of this DeployableDevice.  # noqa: E501
        :rtype: str
        """
        return self._traffic_interruption

    @traffic_interruption.setter
    def traffic_interruption(self, traffic_interruption):
        """Sets the traffic_interruption of this DeployableDevice.


        :param traffic_interruption: The traffic_interruption of this DeployableDevice.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO", "UNDETERMINED", "ERROR"]  # noqa: E501
        if traffic_interruption not in allowed_values:
            raise ValueError(
                "Invalid value for `traffic_interruption` ({0}), must be one of {1}"  # noqa: E501
                .format(traffic_interruption, allowed_values)
            )

        self._traffic_interruption = traffic_interruption

    @property
    def device(self):
        """Gets the device of this DeployableDevice.  # noqa: E501


        :return: The device of this DeployableDevice.  # noqa: E501
        :rtype: IDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DeployableDevice.


        :param device: The device of this DeployableDevice.  # noqa: E501
        :type: IDevice
        """

        self._device = device

    @property
    def group(self):
        """Gets the group of this DeployableDevice.  # noqa: E501


        :return: The group of this DeployableDevice.  # noqa: E501
        :rtype: IDeviceGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this DeployableDevice.


        :param group: The group of this DeployableDevice.  # noqa: E501
        :type: IDeviceGroup
        """

        self._group = group

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
        if issubclass(DeployableDevice, dict):
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
        if not isinstance(other, DeployableDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other