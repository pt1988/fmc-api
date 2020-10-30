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
from swagger_client.api.updates_api import UpdatesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUpdatesApi(unittest.TestCase):
    """UpdatesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.updates_api.UpdatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_upgrade(self):
        """Test case for create_upgrade

        """
        pass

    def test_delete_upgrade_package(self):
        """Test case for delete_upgrade_package

        """
        pass

    def test_get_all_applicable_device(self):
        """Test case for get_all_applicable_device

        """
        pass

    def test_get_all_upgrade_package(self):
        """Test case for get_all_upgrade_package

        """
        pass

    def test_get_upgrade_package(self):
        """Test case for get_upgrade_package

        """
        pass


if __name__ == '__main__':
    unittest.main()
