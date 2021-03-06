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


class Device(object):
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
        'host_name': 'str',
        'metadata': 'IMetadata',
        'model_id': 'str',
        'advanced': 'IAdvanced',
        'nat_id': 'str',
        'description': 'str',
        'license_caps': 'list[str]',
        'ftd_mode': 'str',
        'model_type': 'str',
        'type': 'str',
        'reg_key': 'str',
        'keep_local_events': 'bool',
        'version': 'str',
        'sw_version': 'str',
        'health_status': 'str',
        'health_policy': 'IHealthPolicy',
        'name': 'str',
        'links': 'ILinks',
        'model': 'str',
        'model_number': 'str',
        'id': 'str',
        'access_policy': 'IPolicyModel',
        'prohibit_packet_transfer': 'bool',
        'device_group': 'IDeviceGroup'
    }

    attribute_map = {
        'host_name': 'hostName',
        'metadata': 'metadata',
        'model_id': 'modelId',
        'advanced': 'advanced',
        'nat_id': 'natID',
        'description': 'description',
        'license_caps': 'license_caps',
        'ftd_mode': 'ftdMode',
        'model_type': 'modelType',
        'type': 'type',
        'reg_key': 'regKey',
        'keep_local_events': 'keepLocalEvents',
        'version': 'version',
        'sw_version': 'sw_version',
        'health_status': 'healthStatus',
        'health_policy': 'healthPolicy',
        'name': 'name',
        'links': 'links',
        'model': 'model',
        'model_number': 'modelNumber',
        'id': 'id',
        'access_policy': 'accessPolicy',
        'prohibit_packet_transfer': 'prohibitPacketTransfer',
        'device_group': 'deviceGroup'
    }

    def __init__(self, host_name=None, metadata=None, model_id=None, advanced=None, nat_id=None, description=None, license_caps=None, ftd_mode=None, model_type=None, type=None, reg_key=None, keep_local_events=None, version=None, sw_version=None, health_status=None, health_policy=None, name=None, links=None, model=None, model_number=None, id=None, access_policy=None, prohibit_packet_transfer=None, device_group=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501

        self._host_name = None
        self._metadata = None
        self._model_id = None
        self._advanced = None
        self._nat_id = None
        self._description = None
        self._license_caps = None
        self._ftd_mode = None
        self._model_type = None
        self._type = None
        self._reg_key = None
        self._keep_local_events = None
        self._version = None
        self._sw_version = None
        self._health_status = None
        self._health_policy = None
        self._name = None
        self._links = None
        self._model = None
        self._model_number = None
        self._id = None
        self._access_policy = None
        self._prohibit_packet_transfer = None
        self._device_group = None
        self.discriminator = None

        self.host_name = host_name
        if metadata is not None:
            self.metadata = metadata
        if model_id is not None:
            self.model_id = model_id
        if advanced is not None:
            self.advanced = advanced
        if nat_id is not None:
            self.nat_id = nat_id
        if description is not None:
            self.description = description
        self.license_caps = license_caps
        if ftd_mode is not None:
            self.ftd_mode = ftd_mode
        if model_type is not None:
            self.model_type = model_type
        if type is not None:
            self.type = type
        self.reg_key = reg_key
        if keep_local_events is not None:
            self.keep_local_events = keep_local_events
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
        if links is not None:
            self.links = links
        if model is not None:
            self.model = model
        if model_number is not None:
            self.model_number = model_number
        if id is not None:
            self.id = id
        if access_policy is not None:
            self.access_policy = access_policy
        if prohibit_packet_transfer is not None:
            self.prohibit_packet_transfer = prohibit_packet_transfer
        if device_group is not None:
            self.device_group = device_group

    @property
    def host_name(self):
        """Gets the host_name of this Device.  # noqa: E501

        Hostname or IP address of the device. If the device is behind NAT, you can leave the host name as blank, and enter the NAT_ID string in the 'Unique NAT ID' text box. Use the same NAT_ID string that you used while configuring FMC on the device.  # noqa: E501

        :return: The host_name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this Device.

        Hostname or IP address of the device. If the device is behind NAT, you can leave the host name as blank, and enter the NAT_ID string in the 'Unique NAT ID' text box. Use the same NAT_ID string that you used while configuring FMC on the device.  # noqa: E501

        :param host_name: The host_name of this Device.  # noqa: E501
        :type: str
        """
        if host_name is None:
            raise ValueError("Invalid value for `host_name`, must not be `None`")  # noqa: E501

        self._host_name = host_name

    @property
    def metadata(self):
        """Gets the metadata of this Device.  # noqa: E501

        Object representing metadata attributes of the Device.  # noqa: E501

        :return: The metadata of this Device.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Device.

        Object representing metadata attributes of the Device.  # noqa: E501

        :param metadata: The metadata of this Device.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def model_id(self):
        """Gets the model_id of this Device.  # noqa: E501

        Model ID of the registered device.  # noqa: E501

        :return: The model_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this Device.

        Model ID of the registered device.  # noqa: E501

        :param model_id: The model_id of this Device.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

    @property
    def advanced(self):
        """Gets the advanced of this Device.  # noqa: E501

        Object representing Device Advanced Configuration.  # noqa: E501

        :return: The advanced of this Device.  # noqa: E501
        :rtype: IAdvanced
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this Device.

        Object representing Device Advanced Configuration.  # noqa: E501

        :param advanced: The advanced of this Device.  # noqa: E501
        :type: IAdvanced
        """

        self._advanced = advanced

    @property
    def nat_id(self):
        """Gets the nat_id of this Device.  # noqa: E501

        Unique ID for a Network address translation (NAT) device (optional; used for device registration). If the device to be registered and the Firepower Management Center are separated by a NAT device, enter a unique NAT ID.  # noqa: E501

        :return: The nat_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._nat_id

    @nat_id.setter
    def nat_id(self, nat_id):
        """Sets the nat_id of this Device.

        Unique ID for a Network address translation (NAT) device (optional; used for device registration). If the device to be registered and the Firepower Management Center are separated by a NAT device, enter a unique NAT ID.  # noqa: E501

        :param nat_id: The nat_id of this Device.  # noqa: E501
        :type: str
        """

        self._nat_id = nat_id

    @property
    def description(self):
        """Gets the description of this Device.  # noqa: E501

        User-specified description of the registered device.  # noqa: E501

        :return: The description of this Device.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Device.

        User-specified description of the registered device.  # noqa: E501

        :param description: The description of this Device.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def license_caps(self):
        """Gets the license_caps of this Device.  # noqa: E501

        License capabilities on the managed device.  # noqa: E501

        :return: The license_caps of this Device.  # noqa: E501
        :rtype: list[str]
        """
        return self._license_caps

    @license_caps.setter
    def license_caps(self, license_caps):
        """Sets the license_caps of this Device.

        License capabilities on the managed device.  # noqa: E501

        :param license_caps: The license_caps of this Device.  # noqa: E501
        :type: list[str]
        """
        if license_caps is None:
            raise ValueError("Invalid value for `license_caps`, must not be `None`")  # noqa: E501

        self._license_caps = license_caps

    @property
    def ftd_mode(self):
        """Gets the ftd_mode of this Device.  # noqa: E501

        FTD mode (Example: ROUTED or TRANSPARENT)  # noqa: E501

        :return: The ftd_mode of this Device.  # noqa: E501
        :rtype: str
        """
        return self._ftd_mode

    @ftd_mode.setter
    def ftd_mode(self, ftd_mode):
        """Sets the ftd_mode of this Device.

        FTD mode (Example: ROUTED or TRANSPARENT)  # noqa: E501

        :param ftd_mode: The ftd_mode of this Device.  # noqa: E501
        :type: str
        """
        allowed_values = ["ROUTED", "TRANSPARENT"]  # noqa: E501
        if ftd_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `ftd_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(ftd_mode, allowed_values)
            )

        self._ftd_mode = ftd_mode

    @property
    def model_type(self):
        """Gets the model_type of this Device.  # noqa: E501

        Model type of the registered device.  # noqa: E501

        :return: The model_type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this Device.

        Model type of the registered device.  # noqa: E501

        :param model_type: The model_type of this Device.  # noqa: E501
        :type: str
        """

        self._model_type = model_type

    @property
    def type(self):
        """Gets the type of this Device.  # noqa: E501

        Type of the device; this value is always Device.  # noqa: E501

        :return: The type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Device.

        Type of the device; this value is always Device.  # noqa: E501

        :param type: The type of this Device.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def reg_key(self):
        """Gets the reg_key of this Device.  # noqa: E501

        Registration Key that you entered while configuring FMC on the device.  # noqa: E501

        :return: The reg_key of this Device.  # noqa: E501
        :rtype: str
        """
        return self._reg_key

    @reg_key.setter
    def reg_key(self, reg_key):
        """Sets the reg_key of this Device.

        Registration Key that you entered while configuring FMC on the device.  # noqa: E501

        :param reg_key: The reg_key of this Device.  # noqa: E501
        :type: str
        """
        if reg_key is None:
            raise ValueError("Invalid value for `reg_key`, must not be `None`")  # noqa: E501

        self._reg_key = reg_key

    @property
    def keep_local_events(self):
        """Gets the keep_local_events of this Device.  # noqa: E501

        Boolean indicating whether local events are recorded and kept on the device.  # noqa: E501

        :return: The keep_local_events of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._keep_local_events

    @keep_local_events.setter
    def keep_local_events(self, keep_local_events):
        """Sets the keep_local_events of this Device.

        Boolean indicating whether local events are recorded and kept on the device.  # noqa: E501

        :param keep_local_events: The keep_local_events of this Device.  # noqa: E501
        :type: bool
        """

        self._keep_local_events = keep_local_events

    @property
    def version(self):
        """Gets the version of this Device.  # noqa: E501

        Version number of the response object.  # noqa: E501

        :return: The version of this Device.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Device.

        Version number of the response object.  # noqa: E501

        :param version: The version of this Device.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def sw_version(self):
        """Gets the sw_version of this Device.  # noqa: E501

        Device version  # noqa: E501

        :return: The sw_version of this Device.  # noqa: E501
        :rtype: str
        """
        return self._sw_version

    @sw_version.setter
    def sw_version(self, sw_version):
        """Sets the sw_version of this Device.

        Device version  # noqa: E501

        :param sw_version: The sw_version of this Device.  # noqa: E501
        :type: str
        """

        self._sw_version = sw_version

    @property
    def health_status(self):
        """Gets the health_status of this Device.  # noqa: E501

        Current health status of the device.  # noqa: E501

        :return: The health_status of this Device.  # noqa: E501
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this Device.

        Current health status of the device.  # noqa: E501

        :param health_status: The health_status of this Device.  # noqa: E501
        :type: str
        """

        self._health_status = health_status

    @property
    def health_policy(self):
        """Gets the health_policy of this Device.  # noqa: E501

        Object representing the system health policy applied to the registered device.  # noqa: E501

        :return: The health_policy of this Device.  # noqa: E501
        :rtype: IHealthPolicy
        """
        return self._health_policy

    @health_policy.setter
    def health_policy(self, health_policy):
        """Sets the health_policy of this Device.

        Object representing the system health policy applied to the registered device.  # noqa: E501

        :param health_policy: The health_policy of this Device.  # noqa: E501
        :type: IHealthPolicy
        """

        self._health_policy = health_policy

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501

        User-specified name of the registered device. (Example: Device 01 - 192.168.0.152.)  # noqa: E501

        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.

        User-specified name of the registered device. (Example: Device 01 - 192.168.0.152.)  # noqa: E501

        :param name: The name of this Device.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this Device.  # noqa: E501

        Object containing links to this resource.  # noqa: E501

        :return: The links of this Device.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Device.

        Object containing links to this resource.  # noqa: E501

        :param links: The links of this Device.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def model(self):
        """Gets the model of this Device.  # noqa: E501

        Model name of the registered device.  # noqa: E501

        :return: The model of this Device.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Device.

        Model name of the registered device.  # noqa: E501

        :param model: The model of this Device.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def model_number(self):
        """Gets the model_number of this Device.  # noqa: E501

        Model number of the registered device.  # noqa: E501

        :return: The model_number of this Device.  # noqa: E501
        :rtype: str
        """
        return self._model_number

    @model_number.setter
    def model_number(self, model_number):
        """Sets the model_number of this Device.

        Model number of the registered device.  # noqa: E501

        :param model_number: The model_number of this Device.  # noqa: E501
        :type: str
        """

        self._model_number = model_number

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501

        Unique identifier (UUID) representing the registered device.  # noqa: E501

        :return: The id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.

        Unique identifier (UUID) representing the registered device.  # noqa: E501

        :param id: The id of this Device.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def access_policy(self):
        """Gets the access_policy of this Device.  # noqa: E501

        Object representing the currently assigned access control policy. You need to specify an existing access control policy when registering a device.  # noqa: E501

        :return: The access_policy of this Device.  # noqa: E501
        :rtype: IPolicyModel
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this Device.

        Object representing the currently assigned access control policy. You need to specify an existing access control policy when registering a device.  # noqa: E501

        :param access_policy: The access_policy of this Device.  # noqa: E501
        :type: IPolicyModel
        """

        self._access_policy = access_policy

    @property
    def prohibit_packet_transfer(self):
        """Gets the prohibit_packet_transfer of this Device.  # noqa: E501

        Boolean indicating whether to prohibit the registered device from sending packet data with events to the Firepower Management Center (true) or to allow transfer (false). If this field is set to false (the default), the device transfers packets when a certain event is triggered. Not all traffic data is sent; connection events do not include a payload, only connection metadata.  # noqa: E501

        :return: The prohibit_packet_transfer of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._prohibit_packet_transfer

    @prohibit_packet_transfer.setter
    def prohibit_packet_transfer(self, prohibit_packet_transfer):
        """Sets the prohibit_packet_transfer of this Device.

        Boolean indicating whether to prohibit the registered device from sending packet data with events to the Firepower Management Center (true) or to allow transfer (false). If this field is set to false (the default), the device transfers packets when a certain event is triggered. Not all traffic data is sent; connection events do not include a payload, only connection metadata.  # noqa: E501

        :param prohibit_packet_transfer: The prohibit_packet_transfer of this Device.  # noqa: E501
        :type: bool
        """

        self._prohibit_packet_transfer = prohibit_packet_transfer

    @property
    def device_group(self):
        """Gets the device_group of this Device.  # noqa: E501

        Object representing the device group.  # noqa: E501

        :return: The device_group of this Device.  # noqa: E501
        :rtype: IDeviceGroup
        """
        return self._device_group

    @device_group.setter
    def device_group(self, device_group):
        """Sets the device_group of this Device.

        Object representing the device group.  # noqa: E501

        :param device_group: The device_group of this Device.  # noqa: E501
        :type: IDeviceGroup
        """

        self._device_group = device_group

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
