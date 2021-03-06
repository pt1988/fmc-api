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


class IKEv2IPsecProposalListContainer(object):
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
        'links': 'ILinks',
        'paging': 'PagingContainer',
        'items': 'list[IKEv2IPsecProposal]'
    }

    attribute_map = {
        'links': 'links',
        'paging': 'paging',
        'items': 'items'
    }

    def __init__(self, links=None, paging=None, items=None):  # noqa: E501
        """IKEv2IPsecProposalListContainer - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._paging = None
        self._items = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if paging is not None:
            self.paging = paging
        if items is not None:
            self.items = items

    @property
    def links(self):
        """Gets the links of this IKEv2IPsecProposalListContainer.  # noqa: E501


        :return: The links of this IKEv2IPsecProposalListContainer.  # noqa: E501
        :rtype: ILinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IKEv2IPsecProposalListContainer.


        :param links: The links of this IKEv2IPsecProposalListContainer.  # noqa: E501
        :type: ILinks
        """

        self._links = links

    @property
    def paging(self):
        """Gets the paging of this IKEv2IPsecProposalListContainer.  # noqa: E501


        :return: The paging of this IKEv2IPsecProposalListContainer.  # noqa: E501
        :rtype: PagingContainer
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this IKEv2IPsecProposalListContainer.


        :param paging: The paging of this IKEv2IPsecProposalListContainer.  # noqa: E501
        :type: PagingContainer
        """

        self._paging = paging

    @property
    def items(self):
        """Gets the items of this IKEv2IPsecProposalListContainer.  # noqa: E501


        :return: The items of this IKEv2IPsecProposalListContainer.  # noqa: E501
        :rtype: list[IKEv2IPsecProposal]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this IKEv2IPsecProposalListContainer.


        :param items: The items of this IKEv2IPsecProposalListContainer.  # noqa: E501
        :type: list[IKEv2IPsecProposal]
        """

        self._items = items

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
        if issubclass(IKEv2IPsecProposalListContainer, dict):
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
        if not isinstance(other, IKEv2IPsecProposalListContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
