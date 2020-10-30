# coding: utf-8

"""
    Cisco Firepower Management Center Open API Specification

    **Specifies the REST URLs and methods supported in the Cisco Firepower Management Center API. Refer to the version specific [REST API Quick Start Guide](https://www.cisco.com/c/en/us/support/security/defense-center/products-programming-reference-guides-list.html) for additional information.**  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: tac@cisco.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.audit_api import AuditApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAuditApi(unittest.TestCase):
    """AuditApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.audit_api.AuditApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_audit_model(self):
        """Test case for get_all_audit_model

        """
        pass

    def test_get_audit_model(self):
        """Test case for get_audit_model

        """
        pass


if __name__ == '__main__':
    unittest.main()
