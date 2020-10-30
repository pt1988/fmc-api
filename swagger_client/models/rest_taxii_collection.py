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


class RESTTaxiiCollection(object):
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
        'ca_cert': 'str',
        'feed_content': 'str',
        'description': 'str',
        'feed_status': 'str',
        'invalid_observables': 'int',
        'type': 'str',
        'download_on': 'bool',
        'next_run': 'int',
        'consumed_indicators': 'int',
        'total_indicators': 'int',
        'total_observables': 'int',
        'total_unsupported_observables': 'int',
        'checksum': 'str',
        '_property': 'RESTFeedProperty',
        'llfeed_config': 'LLFeedConfig',
        'links': 'ILinks',
        'id': 'str',
        'client_private_key': 'str',
        'client_cert': 'str',
        'delivery': 'str',
        'subscribed_collections': 'list[RESTCollectionTopic]',
        'finish_time': 'int',
        'last_run': 'int',
        'available_collections': 'list[RESTCollectionTopic]',
        'run_now': 'bool',
        'refresh': 'int',
        'consumed_observables': 'int',
        'total_discarded_indicators': 'int',
        'params': 'LLParams',
        'uri': 'str',
        'feed_config': 'LLFeedConfig',
        'version': 'str',
        'discovery_info': 'list[RESTCollectionTopic]',
        'total_invalid_observables': 'int',
        'status_msg': 'LLStatusMsg',
        'passwd': 'str',
        'start_hour': 'int',
        'feed_type': 'str',
        'discarded_indicators': 'int',
        'consumed_unsupported_observables': 'int',
        'name': 'str',
        'username': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'ca_cert': 'caCert',
        'feed_content': 'feedContent',
        'description': 'description',
        'feed_status': 'feedStatus',
        'invalid_observables': 'invalidObservables',
        'type': 'type',
        'download_on': 'downloadOn',
        'next_run': 'nextRun',
        'consumed_indicators': 'consumedIndicators',
        'total_indicators': 'totalIndicators',
        'total_observables': 'totalObservables',
        'total_unsupported_observables': 'totalUnsupportedObservables',
        'checksum': 'checksum',
        '_property': 'property',
        'llfeed_config': 'llfeedConfig',
        'links': 'links',
        'id': 'id',
        'client_private_key': 'clientPrivateKey',
        'client_cert': 'clientCert',
        'delivery': 'delivery',
        'subscribed_collections': 'subscribedCollections',
        'finish_time': 'finishTime',
        'last_run': 'lastRun',
        'available_collections': 'availableCollections',
        'run_now': 'runNow',
        'refresh': 'refresh',
        'consumed_observables': 'consumedObservables',
        'total_discarded_indicators': 'totalDiscardedIndicators',
        'params': 'params',
        'uri': 'uri',
        'feed_config': 'feedConfig',
        'version': 'version',
        'discovery_info': 'discoveryInfo',
        'total_invalid_observables': 'totalInvalidObservables',
        'status_msg': 'statusMsg',
        'passwd': 'passwd',
        'start_hour': 'startHour',
        'feed_type': 'feedType',
        'discarded_indicators': 'discardedIndicators',
        'consumed_unsupported_observables': 'consumedUnsupportedObservables',
        'name': 'name',
        'username': 'username'
    }

    def __init__(self, metadata=None, ca_cert=None, feed_content=None, description=None, feed_status=None, invalid_observables=None, type=None, download_on=None, next_run=None, consumed_indicators=None, total_indicators=None, total_observables=None, total_unsupported_observables=None, checksum=None, _property=None, llfeed_config=None, links=None, id=None, client_private_key=None, client_cert=None, delivery=None, subscribed_collections=None, finish_time=None, last_run=None, available_collections=None, run_now=None, refresh=None, consumed_observables=None, total_discarded_indicators=None, params=None, uri=None, feed_config=None, version=None, discovery_info=None, total_invalid_observables=None, status_msg=None, passwd=None, start_hour=None, feed_type=None, discarded_indicators=None, consumed_unsupported_observables=None, name=None, username=None):  # noqa: E501
        """RESTTaxiiCollection - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._ca_cert = None
        self._feed_content = None
        self._description = None
        self._feed_status = None
        self._invalid_observables = None
        self._type = None
        self._download_on = None
        self._next_run = None
        self._consumed_indicators = None
        self._total_indicators = None
        self._total_observables = None
        self._total_unsupported_observables = None
        self._checksum = None
        self.__property = None
        self._llfeed_config = None
        self._links = None
        self._id = None
        self._client_private_key = None
        self._client_cert = None
        self._delivery = None
        self._subscribed_collections = None
        self._finish_time = None
        self._last_run = None
        self._available_collections = None
        self._run_now = None
        self._refresh = None
        self._consumed_observables = None
        self._total_discarded_indicators = None
        self._params = None
        self._uri = None
        self._feed_config = None
        self._version = None
        self._discovery_info = None
        self._total_invalid_observables = None
        self._status_msg = None
        self._passwd = None
        self._start_hour = None
        self._feed_type = None
        self._discarded_indicators = None
        self._consumed_unsupported_observables = None
        self._name = None
        self._username = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if ca_cert is not None:
            self.ca_cert = ca_cert
        if feed_content is not None:
            self.feed_content = feed_content
        if description is not None:
            self.description = description
        if feed_status is not None:
            self.feed_status = feed_status
        if invalid_observables is not None:
            self.invalid_observables = invalid_observables
        if type is not None:
            self.type = type
        if download_on is not None:
            self.download_on = download_on
        if next_run is not None:
            self.next_run = next_run
        if consumed_indicators is not None:
            self.consumed_indicators = consumed_indicators
        if total_indicators is not None:
            self.total_indicators = total_indicators
        if total_observables is not None:
            self.total_observables = total_observables
        if total_unsupported_observables is not None:
            self.total_unsupported_observables = total_unsupported_observables
        if checksum is not None:
            self.checksum = checksum
        if _property is not None:
            self._property = _property
        if llfeed_config is not None:
            self.llfeed_config = llfeed_config
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if client_private_key is not None:
            self.client_private_key = client_private_key
        if client_cert is not None:
            self.client_cert = client_cert
        if delivery is not None:
            self.delivery = delivery
        if subscribed_collections is not None:
            self.subscribed_collections = subscribed_collections
        if finish_time is not None:
            self.finish_time = finish_time
        if last_run is not None:
            self.last_run = last_run
        if available_collections is not None:
            self.available_collections = available_collections
        if run_now is not None:
            self.run_now = run_now
        if refresh is not None:
            self.refresh = refresh
        if consumed_observables is not None:
            self.consumed_observables = consumed_observables
        if total_discarded_indicators is not None:
            self.total_discarded_indicators = total_discarded_indicators
        if params is not None:
            self.params = params
        if uri is not None:
            self.uri = uri
        if feed_config is not None:
            self.feed_config = feed_config
        if version is not None:
            self.version = version
        if discovery_info is not None:
            self.discovery_info = discovery_info
        if total_invalid_observables is not None:
            self.total_invalid_observables = total_invalid_observables
        if status_msg is not None:
            self.status_msg = status_msg
        if passwd is not None:
            self.passwd = passwd
        if start_hour is not None:
            self.start_hour = start_hour
        if feed_type is not None:
            self.feed_type = feed_type
        if discarded_indicators is not None:
            self.discarded_indicators = discarded_indicators
        if consumed_unsupported_observables is not None:
            self.consumed_unsupported_observables = consumed_unsupported_observables
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username

    @property
    def metadata(self):
        """Gets the metadata of this RESTTaxiiCollection.  # noqa: E501


        :return: The metadata of this RESTTaxiiCollection.  # noqa: E501
        :rtype: IMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RESTTaxiiCollection.


        :param metadata: The metadata of this RESTTaxiiCollection.  # noqa: E501
        :type: IMetadata
        """

        self._metadata = metadata

    @property
    def ca_cert(self):
        """Gets the ca_cert of this RESTTaxiiCollection.  # noqa: E501


        :return: The ca_cert of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this RESTTaxiiCollection.


        :param ca_cert: The ca_cert of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._ca_cert = ca_cert

    @property
    def feed_content(self):
        """Gets the feed_content of this RESTTaxiiCollection.  # noqa: E501


        :return: The feed_content of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._feed_content

    @feed_content.setter
    def feed_content(self, feed_content):
        """Sets the feed_content of this RESTTaxiiCollection.


        :param feed_content: The feed_content of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._feed_content = feed_content

    @property
    def description(self):
        """Gets the description of this RESTTaxiiCollection.  # noqa: E501


        :return: The description of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RESTTaxiiCollection.


        :param description: The description of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def feed_status(self):
        """Gets the feed_status of this RESTTaxiiCollection.  # noqa: E501


        :return: The feed_status of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._feed_status

    @feed_status.setter
    def feed_status(self, feed_status):
        """Sets the feed_status of this RESTTaxiiCollection.


        :param feed_status: The feed_status of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._feed_status = feed_status

    @property
    def invalid_observables(self):
        """Gets the invalid_observables of this RESTTaxiiCollection.  # noqa: E501


        :return: The invalid_observables of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._invalid_observables

    @invalid_observables.setter
    def invalid_observables(self, invalid_observables):
        """Sets the invalid_observables of this RESTTaxiiCollection.


        :param invalid_observables: The invalid_observables of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._invalid_observables = invalid_observables

    @property
    def type(self):
        """Gets the type of this RESTTaxiiCollection.  # noqa: E501


        :return: The type of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RESTTaxiiCollection.


        :param type: The type of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def download_on(self):
        """Gets the download_on of this RESTTaxiiCollection.  # noqa: E501


        :return: The download_on of this RESTTaxiiCollection.  # noqa: E501
        :rtype: bool
        """
        return self._download_on

    @download_on.setter
    def download_on(self, download_on):
        """Sets the download_on of this RESTTaxiiCollection.


        :param download_on: The download_on of this RESTTaxiiCollection.  # noqa: E501
        :type: bool
        """

        self._download_on = download_on

    @property
    def next_run(self):
        """Gets the next_run of this RESTTaxiiCollection.  # noqa: E501


        :return: The next_run of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._next_run

    @next_run.setter
    def next_run(self, next_run):
        """Sets the next_run of this RESTTaxiiCollection.


        :param next_run: The next_run of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._next_run = next_run

    @property
    def consumed_indicators(self):
        """Gets the consumed_indicators of this RESTTaxiiCollection.  # noqa: E501


        :return: The consumed_indicators of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._consumed_indicators

    @consumed_indicators.setter
    def consumed_indicators(self, consumed_indicators):
        """Sets the consumed_indicators of this RESTTaxiiCollection.


        :param consumed_indicators: The consumed_indicators of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._consumed_indicators = consumed_indicators

    @property
    def total_indicators(self):
        """Gets the total_indicators of this RESTTaxiiCollection.  # noqa: E501


        :return: The total_indicators of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._total_indicators

    @total_indicators.setter
    def total_indicators(self, total_indicators):
        """Sets the total_indicators of this RESTTaxiiCollection.


        :param total_indicators: The total_indicators of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._total_indicators = total_indicators

    @property
    def total_observables(self):
        """Gets the total_observables of this RESTTaxiiCollection.  # noqa: E501


        :return: The total_observables of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._total_observables

    @total_observables.setter
    def total_observables(self, total_observables):
        """Sets the total_observables of this RESTTaxiiCollection.


        :param total_observables: The total_observables of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._total_observables = total_observables

    @property
    def total_unsupported_observables(self):
        """Gets the total_unsupported_observables of this RESTTaxiiCollection.  # noqa: E501


        :return: The total_unsupported_observables of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._total_unsupported_observables

    @total_unsupported_observables.setter
    def total_unsupported_observables(self, total_unsupported_observables):
        """Sets the total_unsupported_observables of this RESTTaxiiCollection.


        :param total_unsupported_observables: The total_unsupported_observables of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._total_unsupported_observables = total_unsupported_observables

    @property
    def checksum(self):
        """Gets the checksum of this RESTTaxiiCollection.  # noqa: E501


        :return: The checksum of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this RESTTaxiiCollection.


        :param checksum: The checksum of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def _property(self):
        """Gets the _property of this RESTTaxiiCollection.  # noqa: E501


        :return: The _property of this RESTTaxiiCollection.  # noqa: E501
        :rtype: RESTFeedProperty
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this RESTTaxiiCollection.


        :param _property: The _property of this RESTTaxiiCollection.  # noqa: E501
        :type: RESTFeedProperty
        """

        self.__property = _property

    @property
    def llfeed_config(self):
        """Gets the llfeed_config of this RESTTaxiiCollection.  # noqa: E501


        :return: The llfeed_config of this RESTTaxiiCollection.  # noqa: E501
        :rtype: LLFeedConfig
        """
        return self._llfeed_config

    @llfeed_config.setter
    def llfeed_config(self, llfeed_config):
        """Sets the llfeed_config of this RESTTaxiiCollection.


        :param llfeed_config: The llfeed_config of this RESTTaxiiCollection.  # noqa: E501
        :type: LLFeedConfig
        """

        self._llfeed_config = llfeed_config

    @property
    def links(self):
        """Gets the links of this RESTTaxiiCollection.  # noqa: E501


        :return: The links of this RESTTaxiiCollection.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RESTTaxiiCollection.


        :param links: The links of this RESTTaxiiCollection.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this RESTTaxiiCollection.  # noqa: E501


        :return: The id of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RESTTaxiiCollection.


        :param id: The id of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def client_private_key(self):
        """Gets the client_private_key of this RESTTaxiiCollection.  # noqa: E501


        :return: The client_private_key of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._client_private_key

    @client_private_key.setter
    def client_private_key(self, client_private_key):
        """Sets the client_private_key of this RESTTaxiiCollection.


        :param client_private_key: The client_private_key of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._client_private_key = client_private_key

    @property
    def client_cert(self):
        """Gets the client_cert of this RESTTaxiiCollection.  # noqa: E501


        :return: The client_cert of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._client_cert

    @client_cert.setter
    def client_cert(self, client_cert):
        """Sets the client_cert of this RESTTaxiiCollection.


        :param client_cert: The client_cert of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._client_cert = client_cert

    @property
    def delivery(self):
        """Gets the delivery of this RESTTaxiiCollection.  # noqa: E501


        :return: The delivery of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this RESTTaxiiCollection.


        :param delivery: The delivery of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._delivery = delivery

    @property
    def subscribed_collections(self):
        """Gets the subscribed_collections of this RESTTaxiiCollection.  # noqa: E501


        :return: The subscribed_collections of this RESTTaxiiCollection.  # noqa: E501
        :rtype: list[RESTCollectionTopic]
        """
        return self._subscribed_collections

    @subscribed_collections.setter
    def subscribed_collections(self, subscribed_collections):
        """Sets the subscribed_collections of this RESTTaxiiCollection.


        :param subscribed_collections: The subscribed_collections of this RESTTaxiiCollection.  # noqa: E501
        :type: list[RESTCollectionTopic]
        """

        self._subscribed_collections = subscribed_collections

    @property
    def finish_time(self):
        """Gets the finish_time of this RESTTaxiiCollection.  # noqa: E501


        :return: The finish_time of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this RESTTaxiiCollection.


        :param finish_time: The finish_time of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._finish_time = finish_time

    @property
    def last_run(self):
        """Gets the last_run of this RESTTaxiiCollection.  # noqa: E501


        :return: The last_run of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._last_run

    @last_run.setter
    def last_run(self, last_run):
        """Sets the last_run of this RESTTaxiiCollection.


        :param last_run: The last_run of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._last_run = last_run

    @property
    def available_collections(self):
        """Gets the available_collections of this RESTTaxiiCollection.  # noqa: E501


        :return: The available_collections of this RESTTaxiiCollection.  # noqa: E501
        :rtype: list[RESTCollectionTopic]
        """
        return self._available_collections

    @available_collections.setter
    def available_collections(self, available_collections):
        """Sets the available_collections of this RESTTaxiiCollection.


        :param available_collections: The available_collections of this RESTTaxiiCollection.  # noqa: E501
        :type: list[RESTCollectionTopic]
        """

        self._available_collections = available_collections

    @property
    def run_now(self):
        """Gets the run_now of this RESTTaxiiCollection.  # noqa: E501


        :return: The run_now of this RESTTaxiiCollection.  # noqa: E501
        :rtype: bool
        """
        return self._run_now

    @run_now.setter
    def run_now(self, run_now):
        """Sets the run_now of this RESTTaxiiCollection.


        :param run_now: The run_now of this RESTTaxiiCollection.  # noqa: E501
        :type: bool
        """

        self._run_now = run_now

    @property
    def refresh(self):
        """Gets the refresh of this RESTTaxiiCollection.  # noqa: E501


        :return: The refresh of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this RESTTaxiiCollection.


        :param refresh: The refresh of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._refresh = refresh

    @property
    def consumed_observables(self):
        """Gets the consumed_observables of this RESTTaxiiCollection.  # noqa: E501


        :return: The consumed_observables of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._consumed_observables

    @consumed_observables.setter
    def consumed_observables(self, consumed_observables):
        """Sets the consumed_observables of this RESTTaxiiCollection.


        :param consumed_observables: The consumed_observables of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._consumed_observables = consumed_observables

    @property
    def total_discarded_indicators(self):
        """Gets the total_discarded_indicators of this RESTTaxiiCollection.  # noqa: E501


        :return: The total_discarded_indicators of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._total_discarded_indicators

    @total_discarded_indicators.setter
    def total_discarded_indicators(self, total_discarded_indicators):
        """Sets the total_discarded_indicators of this RESTTaxiiCollection.


        :param total_discarded_indicators: The total_discarded_indicators of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._total_discarded_indicators = total_discarded_indicators

    @property
    def params(self):
        """Gets the params of this RESTTaxiiCollection.  # noqa: E501


        :return: The params of this RESTTaxiiCollection.  # noqa: E501
        :rtype: LLParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this RESTTaxiiCollection.


        :param params: The params of this RESTTaxiiCollection.  # noqa: E501
        :type: LLParams
        """

        self._params = params

    @property
    def uri(self):
        """Gets the uri of this RESTTaxiiCollection.  # noqa: E501


        :return: The uri of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this RESTTaxiiCollection.


        :param uri: The uri of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def feed_config(self):
        """Gets the feed_config of this RESTTaxiiCollection.  # noqa: E501


        :return: The feed_config of this RESTTaxiiCollection.  # noqa: E501
        :rtype: LLFeedConfig
        """
        return self._feed_config

    @feed_config.setter
    def feed_config(self, feed_config):
        """Sets the feed_config of this RESTTaxiiCollection.


        :param feed_config: The feed_config of this RESTTaxiiCollection.  # noqa: E501
        :type: LLFeedConfig
        """

        self._feed_config = feed_config

    @property
    def version(self):
        """Gets the version of this RESTTaxiiCollection.  # noqa: E501


        :return: The version of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RESTTaxiiCollection.


        :param version: The version of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def discovery_info(self):
        """Gets the discovery_info of this RESTTaxiiCollection.  # noqa: E501


        :return: The discovery_info of this RESTTaxiiCollection.  # noqa: E501
        :rtype: list[RESTCollectionTopic]
        """
        return self._discovery_info

    @discovery_info.setter
    def discovery_info(self, discovery_info):
        """Sets the discovery_info of this RESTTaxiiCollection.


        :param discovery_info: The discovery_info of this RESTTaxiiCollection.  # noqa: E501
        :type: list[RESTCollectionTopic]
        """

        self._discovery_info = discovery_info

    @property
    def total_invalid_observables(self):
        """Gets the total_invalid_observables of this RESTTaxiiCollection.  # noqa: E501


        :return: The total_invalid_observables of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._total_invalid_observables

    @total_invalid_observables.setter
    def total_invalid_observables(self, total_invalid_observables):
        """Sets the total_invalid_observables of this RESTTaxiiCollection.


        :param total_invalid_observables: The total_invalid_observables of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._total_invalid_observables = total_invalid_observables

    @property
    def status_msg(self):
        """Gets the status_msg of this RESTTaxiiCollection.  # noqa: E501


        :return: The status_msg of this RESTTaxiiCollection.  # noqa: E501
        :rtype: LLStatusMsg
        """
        return self._status_msg

    @status_msg.setter
    def status_msg(self, status_msg):
        """Sets the status_msg of this RESTTaxiiCollection.


        :param status_msg: The status_msg of this RESTTaxiiCollection.  # noqa: E501
        :type: LLStatusMsg
        """

        self._status_msg = status_msg

    @property
    def passwd(self):
        """Gets the passwd of this RESTTaxiiCollection.  # noqa: E501


        :return: The passwd of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """Sets the passwd of this RESTTaxiiCollection.


        :param passwd: The passwd of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._passwd = passwd

    @property
    def start_hour(self):
        """Gets the start_hour of this RESTTaxiiCollection.  # noqa: E501


        :return: The start_hour of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        """Sets the start_hour of this RESTTaxiiCollection.


        :param start_hour: The start_hour of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._start_hour = start_hour

    @property
    def feed_type(self):
        """Gets the feed_type of this RESTTaxiiCollection.  # noqa: E501


        :return: The feed_type of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._feed_type

    @feed_type.setter
    def feed_type(self, feed_type):
        """Sets the feed_type of this RESTTaxiiCollection.


        :param feed_type: The feed_type of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._feed_type = feed_type

    @property
    def discarded_indicators(self):
        """Gets the discarded_indicators of this RESTTaxiiCollection.  # noqa: E501


        :return: The discarded_indicators of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._discarded_indicators

    @discarded_indicators.setter
    def discarded_indicators(self, discarded_indicators):
        """Sets the discarded_indicators of this RESTTaxiiCollection.


        :param discarded_indicators: The discarded_indicators of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._discarded_indicators = discarded_indicators

    @property
    def consumed_unsupported_observables(self):
        """Gets the consumed_unsupported_observables of this RESTTaxiiCollection.  # noqa: E501


        :return: The consumed_unsupported_observables of this RESTTaxiiCollection.  # noqa: E501
        :rtype: int
        """
        return self._consumed_unsupported_observables

    @consumed_unsupported_observables.setter
    def consumed_unsupported_observables(self, consumed_unsupported_observables):
        """Sets the consumed_unsupported_observables of this RESTTaxiiCollection.


        :param consumed_unsupported_observables: The consumed_unsupported_observables of this RESTTaxiiCollection.  # noqa: E501
        :type: int
        """

        self._consumed_unsupported_observables = consumed_unsupported_observables

    @property
    def name(self):
        """Gets the name of this RESTTaxiiCollection.  # noqa: E501


        :return: The name of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RESTTaxiiCollection.


        :param name: The name of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def username(self):
        """Gets the username of this RESTTaxiiCollection.  # noqa: E501


        :return: The username of this RESTTaxiiCollection.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RESTTaxiiCollection.


        :param username: The username of this RESTTaxiiCollection.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(RESTTaxiiCollection, dict):
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
        if not isinstance(other, RESTTaxiiCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
