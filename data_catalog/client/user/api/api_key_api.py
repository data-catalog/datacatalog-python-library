# coding: utf-8

"""
    Data Catalog User Service API

    The user handling service of the Data Catalog application.  Provides API endpoints to register, and log in to the application.  It communicates with other services to tell informations about tokens, thus authorizing a request made at another service. Provides endpoints to delete, and list users for administrative purposes.  The api supports JWT token, and API key authentication.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: szilard.tumo@stud.ubbcluj.ro
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from data_catalog.client.user.api_client import ApiClient
from data_catalog.client.user.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ApiKeyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user_api_key(self, **kwargs):  # noqa: E501
        """Create an API Key for the Authenticated User  # noqa: E501

        Generates a new API key for the authenticated user.  Requires authentication.   The key will be returned only with this request. It cannot be viewed again.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_api_key(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ApiKeyCreationRequest api_key_creation_request:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiKeyCreationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_user_api_key_with_http_info(**kwargs)  # noqa: E501

    def create_user_api_key_with_http_info(self, **kwargs):  # noqa: E501
        """Create an API Key for the Authenticated User  # noqa: E501

        Generates a new API key for the authenticated user.  Requires authentication.   The key will be returned only with this request. It cannot be viewed again.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_api_key_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ApiKeyCreationRequest api_key_creation_request:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiKeyCreationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'api_key_creation_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_api_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'api_key_creation_request' in local_var_params:
            body_params = local_var_params['api_key_creation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/user/keys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyCreationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user_api_key(self, key_id, **kwargs):  # noqa: E501
        """Delete an API Key  # noqa: E501

        Removes an API key from the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_api_key(key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key_id: The ID of the API key. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_user_api_key_with_http_info(key_id, **kwargs)  # noqa: E501

    def delete_user_api_key_with_http_info(self, key_id, **kwargs):  # noqa: E501
        """Delete an API Key  # noqa: E501

        Removes an API key from the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_api_key_with_http_info(key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key_id: The ID of the API key. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_api_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key_id' is set
        if self.api_client.client_side_validation and ('key_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['key_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key_id` when calling `delete_user_api_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['keyId'] = local_var_params['key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey', 'JWT']  # noqa: E501

        return self.api_client.call_api(
            '/user/keys/{keyId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_api_key(self, key_id, **kwargs):  # noqa: E501
        """Get an API Key  # noqa: E501

        View a single API key of the authenticated user. For security reasons, it only returns the name and ID, not the key itself.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_key(key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key_id: The ID of the API key. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_api_key_with_http_info(key_id, **kwargs)  # noqa: E501

    def get_user_api_key_with_http_info(self, key_id, **kwargs):  # noqa: E501
        """Get an API Key  # noqa: E501

        View a single API key of the authenticated user. For security reasons, it only returns the name and ID, not the key itself.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_key_with_http_info(key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str key_id: The ID of the API key. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiKeyResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'key_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_api_key" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'key_id' is set
        if self.api_client.client_side_validation and ('key_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['key_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key_id` when calling `get_user_api_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['keyId'] = local_var_params['key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey', 'JWT']  # noqa: E501

        return self.api_client.call_api(
            '/user/keys/{keyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_api_keys(self, **kwargs):  # noqa: E501
        """Get the API Keys of the Authenticated User  # noqa: E501

        Lists the API keys for the authenticated user. For security reasons, it only returns the name and ID, not the key itself.  Requires authentication.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_keys(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ApiKeyResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_api_keys_with_http_info(**kwargs)  # noqa: E501

    def get_user_api_keys_with_http_info(self, **kwargs):  # noqa: E501
        """Get the API Keys of the Authenticated User  # noqa: E501

        Lists the API keys for the authenticated user. For security reasons, it only returns the name and ID, not the key itself.  Requires authentication.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_keys_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ApiKeyResponse], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_api_keys" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/user/keys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApiKeyResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
