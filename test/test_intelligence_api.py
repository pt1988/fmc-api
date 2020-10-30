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
from swagger_client.api.intelligence_api import IntelligenceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIntelligenceApi(unittest.TestCase):
    """IntelligenceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.intelligence_api.IntelligenceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_rest_discovery_info(self):
        """Test case for create_rest_discovery_info

        """
        pass

    def test_create_rest_taxii_collection(self):
        """Test case for create_rest_taxii_collection

        """
        pass

    def test_create_rest_tid_source(self):
        """Test case for create_rest_tid_source

        """
        pass

    def test_delete_rest_incident(self):
        """Test case for delete_rest_incident

        """
        pass

    def test_delete_rest_tid_source(self):
        """Test case for delete_rest_tid_source

        """
        pass

    def test_get_all_rest_element(self):
        """Test case for get_all_rest_element

        """
        pass

    def test_get_all_rest_incident(self):
        """Test case for get_all_rest_incident

        """
        pass

    def test_get_all_rest_indicator(self):
        """Test case for get_all_rest_indicator

        """
        pass

    def test_get_all_rest_observable(self):
        """Test case for get_all_rest_observable

        """
        pass

    def test_get_all_rest_tid_source(self):
        """Test case for get_all_rest_tid_source

        """
        pass

    def test_get_rest_element(self):
        """Test case for get_rest_element

        """
        pass

    def test_get_rest_incident(self):
        """Test case for get_rest_incident

        """
        pass

    def test_get_rest_indicator(self):
        """Test case for get_rest_indicator

        """
        pass

    def test_get_rest_observable(self):
        """Test case for get_rest_observable

        """
        pass

    def test_get_rest_settings(self):
        """Test case for get_rest_settings

        """
        pass

    def test_get_rest_tid_source(self):
        """Test case for get_rest_tid_source

        """
        pass

    def test_update_rest_incident(self):
        """Test case for update_rest_incident

        """
        pass

    def test_update_rest_indicator(self):
        """Test case for update_rest_indicator

        """
        pass

    def test_update_rest_observable(self):
        """Test case for update_rest_observable

        """
        pass

    def test_update_rest_settings(self):
        """Test case for update_rest_settings

        """
        pass

    def test_update_rest_tid_source(self):
        """Test case for update_rest_tid_source

        """
        pass


if __name__ == '__main__':
    unittest.main()
