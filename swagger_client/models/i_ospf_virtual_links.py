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


class IOspfVirtualLinks(object):
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
        'retransmit_interval': 'int',
        'dead_interval': 'int',
        'router_id': 'str',
        'name': 'str',
        'hello_interval': 'int',
        'links': 'ILinks',
        'id': 'str',
        'type': 'str',
        'transmit_delay': 'int',
        'authentication': 'IOspfAuthentication'
    }

    attribute_map = {
        'retransmit_interval': 'retransmitInterval',
        'dead_interval': 'deadInterval',
        'router_id': 'routerId',
        'name': 'name',
        'hello_interval': 'helloInterval',
        'links': 'links',
        'id': 'id',
        'type': 'type',
        'transmit_delay': 'transmitDelay',
        'authentication': 'authentication'
    }

    def __init__(self, retransmit_interval=None, dead_interval=None, router_id=None, name=None, hello_interval=None, links=None, id=None, type=None, transmit_delay=None, authentication=None):  # noqa: E501
        """IOspfVirtualLinks - a model defined in Swagger"""  # noqa: E501

        self._retransmit_interval = None
        self._dead_interval = None
        self._router_id = None
        self._name = None
        self._hello_interval = None
        self._links = None
        self._id = None
        self._type = None
        self._transmit_delay = None
        self._authentication = None
        self.discriminator = None

        if retransmit_interval is not None:
            self.retransmit_interval = retransmit_interval
        if dead_interval is not None:
            self.dead_interval = dead_interval
        if router_id is not None:
            self.router_id = router_id
        if name is not None:
            self.name = name
        if hello_interval is not None:
            self.hello_interval = hello_interval
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if transmit_delay is not None:
            self.transmit_delay = transmit_delay
        if authentication is not None:
            self.authentication = authentication

    @property
    def retransmit_interval(self):
        """Gets the retransmit_interval of this IOspfVirtualLinks.  # noqa: E501


        :return: The retransmit_interval of this IOspfVirtualLinks.  # noqa: E501
        :rtype: int
        """
        return self._retransmit_interval

    @retransmit_interval.setter
    def retransmit_interval(self, retransmit_interval):
        """Sets the retransmit_interval of this IOspfVirtualLinks.


        :param retransmit_interval: The retransmit_interval of this IOspfVirtualLinks.  # noqa: E501
        :type: int
        """

        self._retransmit_interval = retransmit_interval

    @property
    def dead_interval(self):
        """Gets the dead_interval of this IOspfVirtualLinks.  # noqa: E501


        :return: The dead_interval of this IOspfVirtualLinks.  # noqa: E501
        :rtype: int
        """
        return self._dead_interval

    @dead_interval.setter
    def dead_interval(self, dead_interval):
        """Sets the dead_interval of this IOspfVirtualLinks.


        :param dead_interval: The dead_interval of this IOspfVirtualLinks.  # noqa: E501
        :type: int
        """

        self._dead_interval = dead_interval

    @property
    def router_id(self):
        """Gets the router_id of this IOspfVirtualLinks.  # noqa: E501


        :return: The router_id of this IOspfVirtualLinks.  # noqa: E501
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this IOspfVirtualLinks.


        :param router_id: The router_id of this IOspfVirtualLinks.  # noqa: E501
        :type: str
        """

        self._router_id = router_id

    @property
    def name(self):
        """Gets the name of this IOspfVirtualLinks.  # noqa: E501


        :return: The name of this IOspfVirtualLinks.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IOspfVirtualLinks.


        :param name: The name of this IOspfVirtualLinks.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def hello_interval(self):
        """Gets the hello_interval of this IOspfVirtualLinks.  # noqa: E501


        :return: The hello_interval of this IOspfVirtualLinks.  # noqa: E501
        :rtype: int
        """
        return self._hello_interval

    @hello_interval.setter
    def hello_interval(self, hello_interval):
        """Sets the hello_interval of this IOspfVirtualLinks.


        :param hello_interval: The hello_interval of this IOspfVirtualLinks.  # noqa: E501
        :type: int
        """

        self._hello_interval = hello_interval

    @property
    def links(self):
        """Gets the links of this IOspfVirtualLinks.  # noqa: E501


        :return: The links of this IOspfVirtualLinks.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IOspfVirtualLinks.


        :param links: The links of this IOspfVirtualLinks.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this IOspfVirtualLinks.  # noqa: E501


        :return: The id of this IOspfVirtualLinks.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IOspfVirtualLinks.


        :param id: The id of this IOspfVirtualLinks.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this IOspfVirtualLinks.  # noqa: E501


        :return: The type of this IOspfVirtualLinks.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IOspfVirtualLinks.


        :param type: The type of this IOspfVirtualLinks.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def transmit_delay(self):
        """Gets the transmit_delay of this IOspfVirtualLinks.  # noqa: E501


        :return: The transmit_delay of this IOspfVirtualLinks.  # noqa: E501
        :rtype: int
        """
        return self._transmit_delay

    @transmit_delay.setter
    def transmit_delay(self, transmit_delay):
        """Sets the transmit_delay of this IOspfVirtualLinks.


        :param transmit_delay: The transmit_delay of this IOspfVirtualLinks.  # noqa: E501
        :type: int
        """

        self._transmit_delay = transmit_delay

    @property
    def authentication(self):
        """Gets the authentication of this IOspfVirtualLinks.  # noqa: E501


        :return: The authentication of this IOspfVirtualLinks.  # noqa: E501
        :rtype: IOspfAuthentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this IOspfVirtualLinks.


        :param authentication: The authentication of this IOspfVirtualLinks.  # noqa: E501
        :type: IOspfAuthentication
        """

        self._authentication = authentication

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
        if issubclass(IOspfVirtualLinks, dict):
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
        if not isinstance(other, IOspfVirtualLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
