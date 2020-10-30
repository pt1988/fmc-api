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


class FTDHADeviceContainer(object):
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
        'model_id': 'str',
        'advanced': 'IAdvanced',
        'description': 'str',
        'ftd_ha_failover_trigger_criteria': 'IFTDHAFailoverInterfacePolicyTrigger',
        'model_type': 'str',
        'type': 'str',
        'version': 'str',
        'ftd_ha_bootstrap': 'IFTDDeviceHABootStrap',
        'sw_version': 'str',
        'secondary': 'IBaseDevice',
        'health_status': 'str',
        'health_policy': 'IHealthPolicy',
        'name': 'str',
        'action': 'str',
        'links': 'ILinks',
        'model': 'str',
        'model_number': 'str',
        'force_break': 'bool',
        'id': 'str',
        'access_policy': 'IPolicyModel',
        'primary': 'IBaseDevice'
    }

    attribute_map = {
        'metadata': 'metadata',
        'model_id': 'modelId',
        'advanced': 'advanced',
        'description': 'description',
        'ftd_ha_failover_trigger_criteria': 'ftdHAFailoverTriggerCriteria',
        'model_type': 'modelType',
        'type': 'type',
        'version': 'version',
        'ftd_ha_bootstrap': 'ftdHABootstrap',
        'sw_version': 'sw_version',
        'secondary': 'secondary',
        'health_status': 'healthStatus',
        'health_policy': 'healthPolicy',
        'name': 'name',
        'action': 'action',
        'links': 'links',
        'model': 'model',
        'model_number': 'modelNumber',
        'force_break': 'forceBreak',
        'id': 'id',
        'access_policy': 'accessPolicy',
        'primary': 'primary'
    }

    def __init__(self, metadata=None, model_id=None, advanced=None, description=None, ftd_ha_failover_trigger_criteria=None, model_type=None, type=None, version=None, ftd_ha_bootstrap=None, sw_version=None, secondary=None, health_status=None, health_policy=None, name=None, action=None, links=None, model=None, model_number=None, force_break=None, id=None, access_policy=None, primary=None):  # noqa: E501
        """FTDHADeviceContainer - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._model_id = None
        self._advanced = None
        self._description = None
        self._ftd_ha_failover_trigger_criteria = None
        self._model_type = None
        self._type = None
        self._version = None
        self._ftd_ha_bootstrap = None
        self._sw_version = None
        self._secondary = None
        self._health_status = None
        self._health_policy = None
        self._name = None
        self._action = None
        self._links = None
        self._model = None
        self._model_number = None
        self._force_break = None
        self._id = None
        self._access_policy = None
        self._primary = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if model_id is not None:
            self.model_id = model_id
        if advanced is not None:
            self.advanced = advanced
        if description is not None:
            self.description = description
        if ftd_ha_failover_trigger_criteria is not None:
            self.ftd_ha_failover_trigger_criteria = ftd_ha_failover_trigger_criteria
        if model_type is not None:
            self.model_type = model_type
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        self.ftd_ha_bootstrap = ftd_ha_bootstrap
        if sw_version is not None:
            self.sw_version = sw_version
        self.secondary = secondary
        if health_status is not None:
            self.health_status = health_status
        if health_policy is not None:
            self.health_policy = health_policy
        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if links is not None:
            self.links = links
        if model is not None:
            self.model = model
        if model_number is not None:
            self.model_number = model_number
        if force_break is not None:
            self.force_break = force_break
        if id is not None:
            self.id = id
        if access_policy is not None:
            self.access_policy = access_policy
        self.primary = primary

    @property
    def metadata(self):
        """Gets the metadata of this FTDHADeviceContainer.  # noqa: E501

        Object representing metadata properties  # noqa: E501

        :return: The metadata of this FTDHADeviceContainer.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FTDHADeviceContainer.

        Object representing metadata properties  # noqa: E501

        :param metadata: The metadata of this FTDHADeviceContainer.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def model_id(self):
        """Gets the model_id of this FTDHADeviceContainer.  # noqa: E501

        Model ID of the FTD Devices used in FTD HA pair.  # noqa: E501

        :return: The model_id of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this FTDHADeviceContainer.

        Model ID of the FTD Devices used in FTD HA pair.  # noqa: E501

        :param model_id: The model_id of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

    @property
    def advanced(self):
        """Gets the advanced of this FTDHADeviceContainer.  # noqa: E501

        Object representing Device Advanced Configuration.  # noqa: E501

        :return: The advanced of this FTDHADeviceContainer.  # noqa: E501
        :rtype: IAdvanced
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this FTDHADeviceContainer.

        Object representing Device Advanced Configuration.  # noqa: E501

        :param advanced: The advanced of this FTDHADeviceContainer.  # noqa: E501
        :type: IAdvanced
        """

        self._advanced = advanced

    @property
    def description(self):
        """Gets the description of this FTDHADeviceContainer.  # noqa: E501

        Retrieves or modifies the FTD HA record associated with the specified ID. Creates or breaks or deletes a FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA pairs.  # noqa: E501

        :return: The description of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FTDHADeviceContainer.

        Retrieves or modifies the FTD HA record associated with the specified ID. Creates or breaks or deletes a FTD HA pair. If no ID is specified for a GET, retrieves list of all FTD HA pairs.  # noqa: E501

        :param description: The description of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ftd_ha_failover_trigger_criteria(self):
        """Gets the ftd_ha_failover_trigger_criteria of this FTDHADeviceContainer.  # noqa: E501

        Conditions on which HA failover would be triggered.  # noqa: E501

        :return: The ftd_ha_failover_trigger_criteria of this FTDHADeviceContainer.  # noqa: E501
        :rtype: IFTDHAFailoverInterfacePolicyTrigger
        """
        return self._ftd_ha_failover_trigger_criteria

    @ftd_ha_failover_trigger_criteria.setter
    def ftd_ha_failover_trigger_criteria(self, ftd_ha_failover_trigger_criteria):
        """Sets the ftd_ha_failover_trigger_criteria of this FTDHADeviceContainer.

        Conditions on which HA failover would be triggered.  # noqa: E501

        :param ftd_ha_failover_trigger_criteria: The ftd_ha_failover_trigger_criteria of this FTDHADeviceContainer.  # noqa: E501
        :type: IFTDHAFailoverInterfacePolicyTrigger
        """

        self._ftd_ha_failover_trigger_criteria = ftd_ha_failover_trigger_criteria

    @property
    def model_type(self):
        """Gets the model_type of this FTDHADeviceContainer.  # noqa: E501

        Model type of the FTD Devices used in FTD HA pair.  # noqa: E501

        :return: The model_type of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this FTDHADeviceContainer.

        Model type of the FTD Devices used in FTD HA pair.  # noqa: E501

        :param model_type: The model_type of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._model_type = model_type

    @property
    def type(self):
        """Gets the type of this FTDHADeviceContainer.  # noqa: E501

        DeviceHAPair.  # noqa: E501

        :return: The type of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FTDHADeviceContainer.

        DeviceHAPair.  # noqa: E501

        :param type: The type of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this FTDHADeviceContainer.  # noqa: E501

        FTD HA model version.  # noqa: E501

        :return: The version of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FTDHADeviceContainer.

        FTD HA model version.  # noqa: E501

        :param version: The version of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def ftd_ha_bootstrap(self):
        """Gets the ftd_ha_bootstrap of this FTDHADeviceContainer.  # noqa: E501

        FTD HA Bootstrap object used during POST operation.  # noqa: E501

        :return: The ftd_ha_bootstrap of this FTDHADeviceContainer.  # noqa: E501
        :rtype: IFTDDeviceHABootStrap
        """
        return self._ftd_ha_bootstrap

    @ftd_ha_bootstrap.setter
    def ftd_ha_bootstrap(self, ftd_ha_bootstrap):
        """Sets the ftd_ha_bootstrap of this FTDHADeviceContainer.

        FTD HA Bootstrap object used during POST operation.  # noqa: E501

        :param ftd_ha_bootstrap: The ftd_ha_bootstrap of this FTDHADeviceContainer.  # noqa: E501
        :type: IFTDDeviceHABootStrap
        """
        if ftd_ha_bootstrap is None:
            raise ValueError("Invalid value for `ftd_ha_bootstrap`, must not be `None`")  # noqa: E501

        self._ftd_ha_bootstrap = ftd_ha_bootstrap

    @property
    def sw_version(self):
        """Gets the sw_version of this FTDHADeviceContainer.  # noqa: E501

        FTD HA device version.  # noqa: E501

        :return: The sw_version of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._sw_version

    @sw_version.setter
    def sw_version(self, sw_version):
        """Sets the sw_version of this FTDHADeviceContainer.

        FTD HA device version.  # noqa: E501

        :param sw_version: The sw_version of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._sw_version = sw_version

    @property
    def secondary(self):
        """Gets the secondary of this FTDHADeviceContainer.  # noqa: E501

        Represents the secondary device.  # noqa: E501

        :return: The secondary of this FTDHADeviceContainer.  # noqa: E501
        :rtype: IBaseDevice
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary):
        """Sets the secondary of this FTDHADeviceContainer.

        Represents the secondary device.  # noqa: E501

        :param secondary: The secondary of this FTDHADeviceContainer.  # noqa: E501
        :type: IBaseDevice
        """
        if secondary is None:
            raise ValueError("Invalid value for `secondary`, must not be `None`")  # noqa: E501

        self._secondary = secondary

    @property
    def health_status(self):
        """Gets the health_status of this FTDHADeviceContainer.  # noqa: E501

        Health status of the FTD Devices used in FTD HA pair.  # noqa: E501

        :return: The health_status of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this FTDHADeviceContainer.

        Health status of the FTD Devices used in FTD HA pair.  # noqa: E501

        :param health_status: The health_status of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._health_status = health_status

    @property
    def health_policy(self):
        """Gets the health_policy of this FTDHADeviceContainer.  # noqa: E501

        Health Policy of the FTD Devices used in FTD HA pair.  # noqa: E501

        :return: The health_policy of this FTDHADeviceContainer.  # noqa: E501
        :rtype: IHealthPolicy
        """
        return self._health_policy

    @health_policy.setter
    def health_policy(self, health_policy):
        """Sets the health_policy of this FTDHADeviceContainer.

        Health Policy of the FTD Devices used in FTD HA pair.  # noqa: E501

        :param health_policy: The health_policy of this FTDHADeviceContainer.  # noqa: E501
        :type: IHealthPolicy
        """

        self._health_policy = health_policy

    @property
    def name(self):
        """Gets the name of this FTDHADeviceContainer.  # noqa: E501

        User-chosen name.  # noqa: E501

        :return: The name of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FTDHADeviceContainer.

        User-chosen name.  # noqa: E501

        :param name: The name of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def action(self):
        """Gets the action of this FTDHADeviceContainer.  # noqa: E501

        FTD HA PUT operation action. Specifically used for breaking FTD HA or manual switch.  # noqa: E501

        :return: The action of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this FTDHADeviceContainer.

        FTD HA PUT operation action. Specifically used for breaking FTD HA or manual switch.  # noqa: E501

        :param action: The action of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """
        allowed_values = ["SWITCH", "HABREAK"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def links(self):
        """Gets the links of this FTDHADeviceContainer.  # noqa: E501

        Object containing related links.  # noqa: E501

        :return: The links of this FTDHADeviceContainer.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FTDHADeviceContainer.

        Object containing related links.  # noqa: E501

        :param links: The links of this FTDHADeviceContainer.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def model(self):
        """Gets the model of this FTDHADeviceContainer.  # noqa: E501

        FTDHADeviceContainer  # noqa: E501

        :return: The model of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this FTDHADeviceContainer.

        FTDHADeviceContainer  # noqa: E501

        :param model: The model of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def model_number(self):
        """Gets the model_number of this FTDHADeviceContainer.  # noqa: E501

        Model Number of the FTD Devices used in FTD HA pair.  # noqa: E501

        :return: The model_number of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._model_number

    @model_number.setter
    def model_number(self, model_number):
        """Sets the model_number of this FTDHADeviceContainer.

        Model Number of the FTD Devices used in FTD HA pair.  # noqa: E501

        :param model_number: The model_number of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._model_number = model_number

    @property
    def force_break(self):
        """Gets the force_break of this FTDHADeviceContainer.  # noqa: E501

        FTD HA Force Break option.  # noqa: E501

        :return: The force_break of this FTDHADeviceContainer.  # noqa: E501
        :rtype: bool
        """
        return self._force_break

    @force_break.setter
    def force_break(self, force_break):
        """Sets the force_break of this FTDHADeviceContainer.

        FTD HA Force Break option.  # noqa: E501

        :param force_break: The force_break of this FTDHADeviceContainer.  # noqa: E501
        :type: bool
        """

        self._force_break = force_break

    @property
    def id(self):
        """Gets the id of this FTDHADeviceContainer.  # noqa: E501

        FTD HA container UUID.  # noqa: E501

        :return: The id of this FTDHADeviceContainer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FTDHADeviceContainer.

        FTD HA container UUID.  # noqa: E501

        :param id: The id of this FTDHADeviceContainer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def access_policy(self):
        """Gets the access_policy of this FTDHADeviceContainer.  # noqa: E501

        Object representing the access control policy associated with device  # noqa: E501

        :return: The access_policy of this FTDHADeviceContainer.  # noqa: E501
        :rtype: IPolicyModel
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this FTDHADeviceContainer.

        Object representing the access control policy associated with device  # noqa: E501

        :param access_policy: The access_policy of this FTDHADeviceContainer.  # noqa: E501
        :type: IPolicyModel
        """

        self._access_policy = access_policy

    @property
    def primary(self):
        """Gets the primary of this FTDHADeviceContainer.  # noqa: E501

        Primary Device object for FTD HA.  # noqa: E501

        :return: The primary of this FTDHADeviceContainer.  # noqa: E501
        :rtype: IBaseDevice
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this FTDHADeviceContainer.

        Primary Device object for FTD HA.  # noqa: E501

        :param primary: The primary of this FTDHADeviceContainer.  # noqa: E501
        :type: IBaseDevice
        """
        if primary is None:
            raise ValueError("Invalid value for `primary`, must not be `None`")  # noqa: E501

        self._primary = primary

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
        if issubclass(FTDHADeviceContainer, dict):
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
        if not isinstance(other, FTDHADeviceContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other