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


class RESTIndicator(object):
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
        'indicator': 'LLIndicator',
        'metadata': 'IMetadata',
        'pending': 'list[str]',
        'description': 'str',
        'raw_data': 'str',
        'type': 'str',
        'no_realized_incidents': 'int',
        'observables': 'list[RESTObservable]',
        'feed_id': 'str',
        'effective_property': 'RESTFeedProperty',
        'links': 'ILinks',
        'id': 'str',
        'no_partial_incidents': 'int',
        'custom_property': 'RESTFeedProperty',
        'updated_at': 'int',
        'equation': 'RESTIndicatorEquationNode',
        'contains_unsupported': 'bool',
        'version': 'str',
        'iterator_id': 'str',
        'indicator_version': 'str',
        'contains_invalid': 'bool',
        'name': 'str',
        'source_name': 'str',
        'inherited_property': 'RESTFeedProperty',
        'file_id': 'str'
    }

    attribute_map = {
        'indicator': 'indicator',
        'metadata': 'metadata',
        'pending': 'pending',
        'description': 'description',
        'raw_data': 'rawData',
        'type': 'type',
        'no_realized_incidents': 'noRealizedIncidents',
        'observables': 'observables',
        'feed_id': 'feedId',
        'effective_property': 'effectiveProperty',
        'links': 'links',
        'id': 'id',
        'no_partial_incidents': 'noPartialIncidents',
        'custom_property': 'customProperty',
        'updated_at': 'updatedAt',
        'equation': 'equation',
        'contains_unsupported': 'containsUnsupported',
        'version': 'version',
        'iterator_id': 'iteratorId',
        'indicator_version': 'indicatorVersion',
        'contains_invalid': 'containsInvalid',
        'name': 'name',
        'source_name': 'sourceName',
        'inherited_property': 'inheritedProperty',
        'file_id': 'fileId'
    }

    def __init__(self, indicator=None, metadata=None, pending=None, description=None, raw_data=None, type=None, no_realized_incidents=None, observables=None, feed_id=None, effective_property=None, links=None, id=None, no_partial_incidents=None, custom_property=None, updated_at=None, equation=None, contains_unsupported=None, version=None, iterator_id=None, indicator_version=None, contains_invalid=None, name=None, source_name=None, inherited_property=None, file_id=None):  # noqa: E501
        """RESTIndicator - a model defined in Swagger"""  # noqa: E501

        self._indicator = None
        self._metadata = None
        self._pending = None
        self._description = None
        self._raw_data = None
        self._type = None
        self._no_realized_incidents = None
        self._observables = None
        self._feed_id = None
        self._effective_property = None
        self._links = None
        self._id = None
        self._no_partial_incidents = None
        self._custom_property = None
        self._updated_at = None
        self._equation = None
        self._contains_unsupported = None
        self._version = None
        self._iterator_id = None
        self._indicator_version = None
        self._contains_invalid = None
        self._name = None
        self._source_name = None
        self._inherited_property = None
        self._file_id = None
        self.discriminator = None

        if indicator is not None:
            self.indicator = indicator
        if metadata is not None:
            self.metadata = metadata
        if pending is not None:
            self.pending = pending
        if description is not None:
            self.description = description
        if raw_data is not None:
            self.raw_data = raw_data
        if type is not None:
            self.type = type
        if no_realized_incidents is not None:
            self.no_realized_incidents = no_realized_incidents
        if observables is not None:
            self.observables = observables
        if feed_id is not None:
            self.feed_id = feed_id
        if effective_property is not None:
            self.effective_property = effective_property
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if no_partial_incidents is not None:
            self.no_partial_incidents = no_partial_incidents
        if custom_property is not None:
            self.custom_property = custom_property
        if updated_at is not None:
            self.updated_at = updated_at
        if equation is not None:
            self.equation = equation
        if contains_unsupported is not None:
            self.contains_unsupported = contains_unsupported
        if version is not None:
            self.version = version
        if iterator_id is not None:
            self.iterator_id = iterator_id
        if indicator_version is not None:
            self.indicator_version = indicator_version
        if contains_invalid is not None:
            self.contains_invalid = contains_invalid
        if name is not None:
            self.name = name
        if source_name is not None:
            self.source_name = source_name
        if inherited_property is not None:
            self.inherited_property = inherited_property
        if file_id is not None:
            self.file_id = file_id

    @property
    def indicator(self):
        """Gets the indicator of this RESTIndicator.  # noqa: E501


        :return: The indicator of this RESTIndicator.  # noqa: E501
        :rtype: LLIndicator
        """
        return self._indicator

    @indicator.setter
    def indicator(self, indicator):
        """Sets the indicator of this RESTIndicator.


        :param indicator: The indicator of this RESTIndicator.  # noqa: E501
        :type: LLIndicator
        """

        self._indicator = indicator

    @property
    def metadata(self):
        """Gets the metadata of this RESTIndicator.  # noqa: E501


        :return: The metadata of this RESTIndicator.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RESTIndicator.


        :param metadata: The metadata of this RESTIndicator.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def pending(self):
        """Gets the pending of this RESTIndicator.  # noqa: E501


        :return: The pending of this RESTIndicator.  # noqa: E501
        :rtype: list[str]
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this RESTIndicator.


        :param pending: The pending of this RESTIndicator.  # noqa: E501
        :type: list[str]
        """

        self._pending = pending

    @property
    def description(self):
        """Gets the description of this RESTIndicator.  # noqa: E501


        :return: The description of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RESTIndicator.


        :param description: The description of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def raw_data(self):
        """Gets the raw_data of this RESTIndicator.  # noqa: E501


        :return: The raw_data of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this RESTIndicator.


        :param raw_data: The raw_data of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._raw_data = raw_data

    @property
    def type(self):
        """Gets the type of this RESTIndicator.  # noqa: E501


        :return: The type of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RESTIndicator.


        :param type: The type of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def no_realized_incidents(self):
        """Gets the no_realized_incidents of this RESTIndicator.  # noqa: E501


        :return: The no_realized_incidents of this RESTIndicator.  # noqa: E501
        :rtype: int
        """
        return self._no_realized_incidents

    @no_realized_incidents.setter
    def no_realized_incidents(self, no_realized_incidents):
        """Sets the no_realized_incidents of this RESTIndicator.


        :param no_realized_incidents: The no_realized_incidents of this RESTIndicator.  # noqa: E501
        :type: int
        """

        self._no_realized_incidents = no_realized_incidents

    @property
    def observables(self):
        """Gets the observables of this RESTIndicator.  # noqa: E501


        :return: The observables of this RESTIndicator.  # noqa: E501
        :rtype: list[RESTObservable]
        """
        return self._observables

    @observables.setter
    def observables(self, observables):
        """Sets the observables of this RESTIndicator.


        :param observables: The observables of this RESTIndicator.  # noqa: E501
        :type: list[RESTObservable]
        """

        self._observables = observables

    @property
    def feed_id(self):
        """Gets the feed_id of this RESTIndicator.  # noqa: E501


        :return: The feed_id of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this RESTIndicator.


        :param feed_id: The feed_id of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._feed_id = feed_id

    @property
    def effective_property(self):
        """Gets the effective_property of this RESTIndicator.  # noqa: E501


        :return: The effective_property of this RESTIndicator.  # noqa: E501
        :rtype: RESTFeedProperty
        """
        return self._effective_property

    @effective_property.setter
    def effective_property(self, effective_property):
        """Sets the effective_property of this RESTIndicator.


        :param effective_property: The effective_property of this RESTIndicator.  # noqa: E501
        :type: RESTFeedProperty
        """

        self._effective_property = effective_property

    @property
    def links(self):
        """Gets the links of this RESTIndicator.  # noqa: E501


        :return: The links of this RESTIndicator.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RESTIndicator.


        :param links: The links of this RESTIndicator.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this RESTIndicator.  # noqa: E501


        :return: The id of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RESTIndicator.


        :param id: The id of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def no_partial_incidents(self):
        """Gets the no_partial_incidents of this RESTIndicator.  # noqa: E501


        :return: The no_partial_incidents of this RESTIndicator.  # noqa: E501
        :rtype: int
        """
        return self._no_partial_incidents

    @no_partial_incidents.setter
    def no_partial_incidents(self, no_partial_incidents):
        """Sets the no_partial_incidents of this RESTIndicator.


        :param no_partial_incidents: The no_partial_incidents of this RESTIndicator.  # noqa: E501
        :type: int
        """

        self._no_partial_incidents = no_partial_incidents

    @property
    def custom_property(self):
        """Gets the custom_property of this RESTIndicator.  # noqa: E501


        :return: The custom_property of this RESTIndicator.  # noqa: E501
        :rtype: RESTFeedProperty
        """
        return self._custom_property

    @custom_property.setter
    def custom_property(self, custom_property):
        """Sets the custom_property of this RESTIndicator.


        :param custom_property: The custom_property of this RESTIndicator.  # noqa: E501
        :type: RESTFeedProperty
        """

        self._custom_property = custom_property

    @property
    def updated_at(self):
        """Gets the updated_at of this RESTIndicator.  # noqa: E501


        :return: The updated_at of this RESTIndicator.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RESTIndicator.


        :param updated_at: The updated_at of this RESTIndicator.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def equation(self):
        """Gets the equation of this RESTIndicator.  # noqa: E501


        :return: The equation of this RESTIndicator.  # noqa: E501
        :rtype: RESTIndicatorEquationNode
        """
        return self._equation

    @equation.setter
    def equation(self, equation):
        """Sets the equation of this RESTIndicator.


        :param equation: The equation of this RESTIndicator.  # noqa: E501
        :type: RESTIndicatorEquationNode
        """

        self._equation = equation

    @property
    def contains_unsupported(self):
        """Gets the contains_unsupported of this RESTIndicator.  # noqa: E501


        :return: The contains_unsupported of this RESTIndicator.  # noqa: E501
        :rtype: bool
        """
        return self._contains_unsupported

    @contains_unsupported.setter
    def contains_unsupported(self, contains_unsupported):
        """Sets the contains_unsupported of this RESTIndicator.


        :param contains_unsupported: The contains_unsupported of this RESTIndicator.  # noqa: E501
        :type: bool
        """

        self._contains_unsupported = contains_unsupported

    @property
    def version(self):
        """Gets the version of this RESTIndicator.  # noqa: E501


        :return: The version of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RESTIndicator.


        :param version: The version of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def iterator_id(self):
        """Gets the iterator_id of this RESTIndicator.  # noqa: E501


        :return: The iterator_id of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._iterator_id

    @iterator_id.setter
    def iterator_id(self, iterator_id):
        """Sets the iterator_id of this RESTIndicator.


        :param iterator_id: The iterator_id of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._iterator_id = iterator_id

    @property
    def indicator_version(self):
        """Gets the indicator_version of this RESTIndicator.  # noqa: E501


        :return: The indicator_version of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._indicator_version

    @indicator_version.setter
    def indicator_version(self, indicator_version):
        """Sets the indicator_version of this RESTIndicator.


        :param indicator_version: The indicator_version of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._indicator_version = indicator_version

    @property
    def contains_invalid(self):
        """Gets the contains_invalid of this RESTIndicator.  # noqa: E501


        :return: The contains_invalid of this RESTIndicator.  # noqa: E501
        :rtype: bool
        """
        return self._contains_invalid

    @contains_invalid.setter
    def contains_invalid(self, contains_invalid):
        """Sets the contains_invalid of this RESTIndicator.


        :param contains_invalid: The contains_invalid of this RESTIndicator.  # noqa: E501
        :type: bool
        """

        self._contains_invalid = contains_invalid

    @property
    def name(self):
        """Gets the name of this RESTIndicator.  # noqa: E501


        :return: The name of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RESTIndicator.


        :param name: The name of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_name(self):
        """Gets the source_name of this RESTIndicator.  # noqa: E501


        :return: The source_name of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this RESTIndicator.


        :param source_name: The source_name of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._source_name = source_name

    @property
    def inherited_property(self):
        """Gets the inherited_property of this RESTIndicator.  # noqa: E501


        :return: The inherited_property of this RESTIndicator.  # noqa: E501
        :rtype: RESTFeedProperty
        """
        return self._inherited_property

    @inherited_property.setter
    def inherited_property(self, inherited_property):
        """Sets the inherited_property of this RESTIndicator.


        :param inherited_property: The inherited_property of this RESTIndicator.  # noqa: E501
        :type: RESTFeedProperty
        """

        self._inherited_property = inherited_property

    @property
    def file_id(self):
        """Gets the file_id of this RESTIndicator.  # noqa: E501


        :return: The file_id of this RESTIndicator.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this RESTIndicator.


        :param file_id: The file_id of this RESTIndicator.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

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
        if issubclass(RESTIndicator, dict):
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
        if not isinstance(other, RESTIndicator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
