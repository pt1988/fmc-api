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


class RESTIndicatorEquationNode(object):
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
        'op': 'str',
        'item': 'LLEquationNode',
        'condition': 'str',
        'is_realized': 'bool',
        'children': 'list[RESTIndicatorEquationNode]',
        'type': 'str',
        'value': 'str',
        'apply_condition': 'str'
    }

    attribute_map = {
        'op': 'op',
        'item': 'item',
        'condition': 'condition',
        'is_realized': 'isRealized',
        'children': 'children',
        'type': 'type',
        'value': 'value',
        'apply_condition': 'applyCondition'
    }

    def __init__(self, op=None, item=None, condition=None, is_realized=None, children=None, type=None, value=None, apply_condition=None):  # noqa: E501
        """RESTIndicatorEquationNode - a model defined in Swagger"""  # noqa: E501

        self._op = None
        self._item = None
        self._condition = None
        self._is_realized = None
        self._children = None
        self._type = None
        self._value = None
        self._apply_condition = None
        self.discriminator = None

        if op is not None:
            self.op = op
        if item is not None:
            self.item = item
        if condition is not None:
            self.condition = condition
        if is_realized is not None:
            self.is_realized = is_realized
        if children is not None:
            self.children = children
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if apply_condition is not None:
            self.apply_condition = apply_condition

    @property
    def op(self):
        """Gets the op of this RESTIndicatorEquationNode.  # noqa: E501


        :return: The op of this RESTIndicatorEquationNode.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this RESTIndicatorEquationNode.


        :param op: The op of this RESTIndicatorEquationNode.  # noqa: E501
        :type: str
        """

        self._op = op

    @property
    def item(self):
        """Gets the item of this RESTIndicatorEquationNode.  # noqa: E501


        :return: The item of this RESTIndicatorEquationNode.  # noqa: E501
        :rtype: LLEquationNode
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this RESTIndicatorEquationNode.


        :param item: The item of this RESTIndicatorEquationNode.  # noqa: E501
        :type: LLEquationNode
        """

        self._item = item

    @property
    def condition(self):
        """Gets the condition of this RESTIndicatorEquationNode.  # noqa: E501


        :return: The condition of this RESTIndicatorEquationNode.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this RESTIndicatorEquationNode.


        :param condition: The condition of this RESTIndicatorEquationNode.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def is_realized(self):
        """Gets the is_realized of this RESTIndicatorEquationNode.  # noqa: E501


        :return: The is_realized of this RESTIndicatorEquationNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_realized

    @is_realized.setter
    def is_realized(self, is_realized):
        """Sets the is_realized of this RESTIndicatorEquationNode.


        :param is_realized: The is_realized of this RESTIndicatorEquationNode.  # noqa: E501
        :type: bool
        """

        self._is_realized = is_realized

    @property
    def children(self):
        """Gets the children of this RESTIndicatorEquationNode.  # noqa: E501


        :return: The children of this RESTIndicatorEquationNode.  # noqa: E501
        :rtype: list[RESTIndicatorEquationNode]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this RESTIndicatorEquationNode.


        :param children: The children of this RESTIndicatorEquationNode.  # noqa: E501
        :type: list[RESTIndicatorEquationNode]
        """

        self._children = children

    @property
    def type(self):
        """Gets the type of this RESTIndicatorEquationNode.  # noqa: E501


        :return: The type of this RESTIndicatorEquationNode.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RESTIndicatorEquationNode.


        :param type: The type of this RESTIndicatorEquationNode.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this RESTIndicatorEquationNode.  # noqa: E501


        :return: The value of this RESTIndicatorEquationNode.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RESTIndicatorEquationNode.


        :param value: The value of this RESTIndicatorEquationNode.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def apply_condition(self):
        """Gets the apply_condition of this RESTIndicatorEquationNode.  # noqa: E501


        :return: The apply_condition of this RESTIndicatorEquationNode.  # noqa: E501
        :rtype: str
        """
        return self._apply_condition

    @apply_condition.setter
    def apply_condition(self, apply_condition):
        """Sets the apply_condition of this RESTIndicatorEquationNode.


        :param apply_condition: The apply_condition of this RESTIndicatorEquationNode.  # noqa: E501
        :type: str
        """

        self._apply_condition = apply_condition

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
        if issubclass(RESTIndicatorEquationNode, dict):
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
        if not isinstance(other, RESTIndicatorEquationNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
