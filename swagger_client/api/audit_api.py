# coding: utf-8

"""
    Cisco Firepower Management Center Open API Specification

    **Specifies the REST URLs and methods supported in the Cisco Firepower Management Center API. Refer to the version specific [REST API Quick Start Guide](https://www.cisco.com/c/en/us/support/security/defense-center/products-programming-reference-guides-list.html) for additional information.**  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: tac@cisco.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AuditApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_audit_model(self, domain_uuid, **kwargs):  # noqa: E501
        """get_all_audit_model  # noqa: E501

        **API Operations on audit objects.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_audit_model(domain_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_uuid: Domain UUID (required)
        :param int offset: Index of first item to return.
        :param int limit: Number of items to return.
        :param bool expanded: If set to true, the GET response displays a list of objects with additional attributes.
        :return: AuditModelListContainer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_audit_model_with_http_info(domain_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_audit_model_with_http_info(domain_uuid, **kwargs)  # noqa: E501
            return data

    def get_all_audit_model_with_http_info(self, domain_uuid, **kwargs):  # noqa: E501
        """get_all_audit_model  # noqa: E501

        **API Operations on audit objects.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_audit_model_with_http_info(domain_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain_uuid: Domain UUID (required)
        :param int offset: Index of first item to return.
        :param int limit: Number of items to return.
        :param bool expanded: If set to true, the GET response displays a list of objects with additional attributes.
        :return: AuditModelListContainer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_uuid', 'offset', 'limit', 'expanded']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_audit_model" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_uuid' is set
        if ('domain_uuid' not in params or
                params['domain_uuid'] is None):
            raise ValueError("Missing the required parameter `domain_uuid` when calling `get_all_audit_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_uuid' in params:
            path_params['domainUUID'] = params['domain_uuid']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'expanded' in params:
            query_params.append(('expanded', params['expanded']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/fmc_platform/v1/domain/{domainUUID}/audit/auditrecords', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuditModelListContainer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audit_model(self, object_id, domain_uuid, **kwargs):  # noqa: E501
        """get_audit_model  # noqa: E501

        **API Operations on audit objects.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_model(object_id, domain_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str object_id: Unique identifier of the object. (required)
        :param str domain_uuid: Domain UUID (required)
        :return: AuditModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_model_with_http_info(object_id, domain_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_model_with_http_info(object_id, domain_uuid, **kwargs)  # noqa: E501
            return data

    def get_audit_model_with_http_info(self, object_id, domain_uuid, **kwargs):  # noqa: E501
        """get_audit_model  # noqa: E501

        **API Operations on audit objects.**  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_model_with_http_info(object_id, domain_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str object_id: Unique identifier of the object. (required)
        :param str domain_uuid: Domain UUID (required)
        :return: AuditModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['object_id', 'domain_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_model" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'object_id' is set
        if ('object_id' not in params or
                params['object_id'] is None):
            raise ValueError("Missing the required parameter `object_id` when calling `get_audit_model`")  # noqa: E501
        # verify the required parameter 'domain_uuid' is set
        if ('domain_uuid' not in params or
                params['domain_uuid'] is None):
            raise ValueError("Missing the required parameter `domain_uuid` when calling `get_audit_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_id' in params:
            path_params['objectId'] = params['object_id']  # noqa: E501
        if 'domain_uuid' in params:
            path_params['domainUUID'] = params['domain_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/fmc_platform/v1/domain/{domainUUID}/audit/auditrecords/{objectId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuditModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
