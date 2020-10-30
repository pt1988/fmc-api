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


class IOspfProcessModel(object):
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
        'ignore_lsa_mospf': 'bool',
        'timers': 'IOspfTimers',
        'metadata': 'IMetadata',
        'description': 'str',
        'type': 'str',
        'version': 'str',
        'nsf_graceful_restart': 'IOspfNsfGracefulRestart',
        'default_information_originate': 'IOspfDefaultInfoOriginate',
        'router_id': 'str',
        'rfc1583_compatible': 'bool',
        'name': 'str',
        'links': 'ILinks',
        'id': 'str',
        'administrative_distance': 'IOspfAdministrativeDistance'
    }

    attribute_map = {
        'ignore_lsa_mospf': 'ignoreLsaMospf',
        'timers': 'timers',
        'metadata': 'metadata',
        'description': 'description',
        'type': 'type',
        'version': 'version',
        'nsf_graceful_restart': 'nsfGracefulRestart',
        'default_information_originate': 'defaultInformationOriginate',
        'router_id': 'routerId',
        'rfc1583_compatible': 'rfc1583Compatible',
        'name': 'name',
        'links': 'links',
        'id': 'id',
        'administrative_distance': 'administrativeDistance'
    }

    def __init__(self, ignore_lsa_mospf=None, timers=None, metadata=None, description=None, type=None, version=None, nsf_graceful_restart=None, default_information_originate=None, router_id=None, rfc1583_compatible=None, name=None, links=None, id=None, administrative_distance=None):  # noqa: E501
        """IOspfProcessModel - a model defined in Swagger"""  # noqa: E501

        self._ignore_lsa_mospf = None
        self._timers = None
        self._metadata = None
        self._description = None
        self._type = None
        self._version = None
        self._nsf_graceful_restart = None
        self._default_information_originate = None
        self._router_id = None
        self._rfc1583_compatible = None
        self._name = None
        self._links = None
        self._id = None
        self._administrative_distance = None
        self.discriminator = None

        if ignore_lsa_mospf is not None:
            self.ignore_lsa_mospf = ignore_lsa_mospf
        if timers is not None:
            self.timers = timers
        if metadata is not None:
            self.metadata = metadata
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if nsf_graceful_restart is not None:
            self.nsf_graceful_restart = nsf_graceful_restart
        if default_information_originate is not None:
            self.default_information_originate = default_information_originate
        if router_id is not None:
            self.router_id = router_id
        if rfc1583_compatible is not None:
            self.rfc1583_compatible = rfc1583_compatible
        if name is not None:
            self.name = name
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if administrative_distance is not None:
            self.administrative_distance = administrative_distance

    @property
    def ignore_lsa_mospf(self):
        """Gets the ignore_lsa_mospf of this IOspfProcessModel.  # noqa: E501


        :return: The ignore_lsa_mospf of this IOspfProcessModel.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_lsa_mospf

    @ignore_lsa_mospf.setter
    def ignore_lsa_mospf(self, ignore_lsa_mospf):
        """Sets the ignore_lsa_mospf of this IOspfProcessModel.


        :param ignore_lsa_mospf: The ignore_lsa_mospf of this IOspfProcessModel.  # noqa: E501
        :type: bool
        """

        self._ignore_lsa_mospf = ignore_lsa_mospf

    @property
    def timers(self):
        """Gets the timers of this IOspfProcessModel.  # noqa: E501


        :return: The timers of this IOspfProcessModel.  # noqa: E501
        :rtype: IOspfTimers
        """
        return self._timers

    @timers.setter
    def timers(self, timers):
        """Sets the timers of this IOspfProcessModel.


        :param timers: The timers of this IOspfProcessModel.  # noqa: E501
        :type: IOspfTimers
        """

        self._timers = timers

    @property
    def metadata(self):
        """Gets the metadata of this IOspfProcessModel.  # noqa: E501


        :return: The metadata of this IOspfProcessModel.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IOspfProcessModel.


        :param metadata: The metadata of this IOspfProcessModel.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this IOspfProcessModel.  # noqa: E501


        :return: The description of this IOspfProcessModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IOspfProcessModel.


        :param description: The description of this IOspfProcessModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this IOspfProcessModel.  # noqa: E501


        :return: The type of this IOspfProcessModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IOspfProcessModel.


        :param type: The type of this IOspfProcessModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this IOspfProcessModel.  # noqa: E501


        :return: The version of this IOspfProcessModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IOspfProcessModel.


        :param version: The version of this IOspfProcessModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def nsf_graceful_restart(self):
        """Gets the nsf_graceful_restart of this IOspfProcessModel.  # noqa: E501


        :return: The nsf_graceful_restart of this IOspfProcessModel.  # noqa: E501
        :rtype: IOspfNsfGracefulRestart
        """
        return self._nsf_graceful_restart

    @nsf_graceful_restart.setter
    def nsf_graceful_restart(self, nsf_graceful_restart):
        """Sets the nsf_graceful_restart of this IOspfProcessModel.


        :param nsf_graceful_restart: The nsf_graceful_restart of this IOspfProcessModel.  # noqa: E501
        :type: IOspfNsfGracefulRestart
        """

        self._nsf_graceful_restart = nsf_graceful_restart

    @property
    def default_information_originate(self):
        """Gets the default_information_originate of this IOspfProcessModel.  # noqa: E501


        :return: The default_information_originate of this IOspfProcessModel.  # noqa: E501
        :rtype: IOspfDefaultInfoOriginate
        """
        return self._default_information_originate

    @default_information_originate.setter
    def default_information_originate(self, default_information_originate):
        """Sets the default_information_originate of this IOspfProcessModel.


        :param default_information_originate: The default_information_originate of this IOspfProcessModel.  # noqa: E501
        :type: IOspfDefaultInfoOriginate
        """

        self._default_information_originate = default_information_originate

    @property
    def router_id(self):
        """Gets the router_id of this IOspfProcessModel.  # noqa: E501


        :return: The router_id of this IOspfProcessModel.  # noqa: E501
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this IOspfProcessModel.


        :param router_id: The router_id of this IOspfProcessModel.  # noqa: E501
        :type: str
        """

        self._router_id = router_id

    @property
    def rfc1583_compatible(self):
        """Gets the rfc1583_compatible of this IOspfProcessModel.  # noqa: E501


        :return: The rfc1583_compatible of this IOspfProcessModel.  # noqa: E501
        :rtype: bool
        """
        return self._rfc1583_compatible

    @rfc1583_compatible.setter
    def rfc1583_compatible(self, rfc1583_compatible):
        """Sets the rfc1583_compatible of this IOspfProcessModel.


        :param rfc1583_compatible: The rfc1583_compatible of this IOspfProcessModel.  # noqa: E501
        :type: bool
        """

        self._rfc1583_compatible = rfc1583_compatible

    @property
    def name(self):
        """Gets the name of this IOspfProcessModel.  # noqa: E501


        :return: The name of this IOspfProcessModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IOspfProcessModel.


        :param name: The name of this IOspfProcessModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def links(self):
        """Gets the links of this IOspfProcessModel.  # noqa: E501


        :return: The links of this IOspfProcessModel.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IOspfProcessModel.


        :param links: The links of this IOspfProcessModel.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IOspfProcessModel.  # noqa: E501


        :return: The id of this IOspfProcessModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IOspfProcessModel.


        :param id: The id of this IOspfProcessModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def administrative_distance(self):
        """Gets the administrative_distance of this IOspfProcessModel.  # noqa: E501


        :return: The administrative_distance of this IOspfProcessModel.  # noqa: E501
        :rtype: IOspfAdministrativeDistance
        """
        return self._administrative_distance

    @administrative_distance.setter
    def administrative_distance(self, administrative_distance):
        """Sets the administrative_distance of this IOspfProcessModel.


        :param administrative_distance: The administrative_distance of this IOspfProcessModel.  # noqa: E501
        :type: IOspfAdministrativeDistance
        """

        self._administrative_distance = administrative_distance

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
        if issubclass(IOspfProcessModel, dict):
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
        if not isinstance(other, IOspfProcessModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other