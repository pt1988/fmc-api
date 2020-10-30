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


class PrefilterHitCount(object):
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
        'metadata': 'HitCountMetadata',
        'last_fetch_time_stamp': 'str',
        'hit_count': 'int',
        'first_hit_time_stamp': 'str',
        'rule': 'IPolicyModel',
        'last_hit_time_stamp': 'str',
        'description': 'str',
        'links': 'ILinks',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'last_fetch_time_stamp': 'lastFetchTimeStamp',
        'hit_count': 'hitCount',
        'first_hit_time_stamp': 'firstHitTimeStamp',
        'rule': 'rule',
        'last_hit_time_stamp': 'lastHitTimeStamp',
        'description': 'description',
        'links': 'links',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, metadata=None, last_fetch_time_stamp=None, hit_count=None, first_hit_time_stamp=None, rule=None, last_hit_time_stamp=None, description=None, links=None, type=None, version=None):  # noqa: E501
        """PrefilterHitCount - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._last_fetch_time_stamp = None
        self._hit_count = None
        self._first_hit_time_stamp = None
        self._rule = None
        self._last_hit_time_stamp = None
        self._description = None
        self._links = None
        self._type = None
        self._version = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if last_fetch_time_stamp is not None:
            self.last_fetch_time_stamp = last_fetch_time_stamp
        if hit_count is not None:
            self.hit_count = hit_count
        if first_hit_time_stamp is not None:
            self.first_hit_time_stamp = first_hit_time_stamp
        if rule is not None:
            self.rule = rule
        if last_hit_time_stamp is not None:
            self.last_hit_time_stamp = last_hit_time_stamp
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def metadata(self):
        """Gets the metadata of this PrefilterHitCount.  # noqa: E501

        Object representing metadata attributes for the hit count entry.  # noqa: E501

        :return: The metadata of this PrefilterHitCount.  # noqa: E501
        :rtype: HitCountMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PrefilterHitCount.

        Object representing metadata attributes for the hit count entry.  # noqa: E501

        :param metadata: The metadata of this PrefilterHitCount.  # noqa: E501
        :type: HitCountMetadata
        """

        self._metadata = metadata

    @property
    def last_fetch_time_stamp(self):
        """Gets the last_fetch_time_stamp of this PrefilterHitCount.  # noqa: E501

        Indicates the last time (in ISO 8601 format) the hit count was retrieved for the mentioned rule.  # noqa: E501

        :return: The last_fetch_time_stamp of this PrefilterHitCount.  # noqa: E501
        :rtype: str
        """
        return self._last_fetch_time_stamp

    @last_fetch_time_stamp.setter
    def last_fetch_time_stamp(self, last_fetch_time_stamp):
        """Sets the last_fetch_time_stamp of this PrefilterHitCount.

        Indicates the last time (in ISO 8601 format) the hit count was retrieved for the mentioned rule.  # noqa: E501

        :param last_fetch_time_stamp: The last_fetch_time_stamp of this PrefilterHitCount.  # noqa: E501
        :type: str
        """

        self._last_fetch_time_stamp = last_fetch_time_stamp

    @property
    def hit_count(self):
        """Gets the hit_count of this PrefilterHitCount.  # noqa: E501

        Indicates the number of times the prefilter rule was hit on the target device. It is based on the data from the last FMC hit count refresh operation.  # noqa: E501

        :return: The hit_count of this PrefilterHitCount.  # noqa: E501
        :rtype: int
        """
        return self._hit_count

    @hit_count.setter
    def hit_count(self, hit_count):
        """Sets the hit_count of this PrefilterHitCount.

        Indicates the number of times the prefilter rule was hit on the target device. It is based on the data from the last FMC hit count refresh operation.  # noqa: E501

        :param hit_count: The hit_count of this PrefilterHitCount.  # noqa: E501
        :type: int
        """

        self._hit_count = hit_count

    @property
    def first_hit_time_stamp(self):
        """Gets the first_hit_time_stamp of this PrefilterHitCount.  # noqa: E501

        Indicates the time (in ISO 8601 format) when the hit count was first hit for the mentioned rule.  # noqa: E501

        :return: The first_hit_time_stamp of this PrefilterHitCount.  # noqa: E501
        :rtype: str
        """
        return self._first_hit_time_stamp

    @first_hit_time_stamp.setter
    def first_hit_time_stamp(self, first_hit_time_stamp):
        """Sets the first_hit_time_stamp of this PrefilterHitCount.

        Indicates the time (in ISO 8601 format) when the hit count was first hit for the mentioned rule.  # noqa: E501

        :param first_hit_time_stamp: The first_hit_time_stamp of this PrefilterHitCount.  # noqa: E501
        :type: str
        """

        self._first_hit_time_stamp = first_hit_time_stamp

    @property
    def rule(self):
        """Gets the rule of this PrefilterHitCount.  # noqa: E501

        Object representing the prefilter rule against which the hit count information is retrieved.  # noqa: E501

        :return: The rule of this PrefilterHitCount.  # noqa: E501
        :rtype: IPolicyModel
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this PrefilterHitCount.

        Object representing the prefilter rule against which the hit count information is retrieved.  # noqa: E501

        :param rule: The rule of this PrefilterHitCount.  # noqa: E501
        :type: IPolicyModel
        """

        self._rule = rule

    @property
    def last_hit_time_stamp(self):
        """Gets the last_hit_time_stamp of this PrefilterHitCount.  # noqa: E501

        Indicates the time (in ISO 8601 format) when the hit count was last hit for the mentioned rule.  # noqa: E501

        :return: The last_hit_time_stamp of this PrefilterHitCount.  # noqa: E501
        :rtype: str
        """
        return self._last_hit_time_stamp

    @last_hit_time_stamp.setter
    def last_hit_time_stamp(self, last_hit_time_stamp):
        """Sets the last_hit_time_stamp of this PrefilterHitCount.

        Indicates the time (in ISO 8601 format) when the hit count was last hit for the mentioned rule.  # noqa: E501

        :param last_hit_time_stamp: The last_hit_time_stamp of this PrefilterHitCount.  # noqa: E501
        :type: str
        """

        self._last_hit_time_stamp = last_hit_time_stamp

    @property
    def description(self):
        """Gets the description of this PrefilterHitCount.  # noqa: E501


        :return: The description of this PrefilterHitCount.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PrefilterHitCount.


        :param description: The description of this PrefilterHitCount.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this PrefilterHitCount.  # noqa: E501

        Object containing links to this resource.  # noqa: E501

        :return: The links of this PrefilterHitCount.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PrefilterHitCount.

        Object containing links to this resource.  # noqa: E501

        :param links: The links of this PrefilterHitCount.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def type(self):
        """Gets the type of this PrefilterHitCount.  # noqa: E501

        Type must be PrefilterHitCount.  # noqa: E501

        :return: The type of this PrefilterHitCount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PrefilterHitCount.

        Type must be PrefilterHitCount.  # noqa: E501

        :param type: The type of this PrefilterHitCount.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this PrefilterHitCount.  # noqa: E501


        :return: The version of this PrefilterHitCount.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PrefilterHitCount.


        :param version: The version of this PrefilterHitCount.  # noqa: E501
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
        if issubclass(PrefilterHitCount, dict):
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
        if not isinstance(other, PrefilterHitCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
