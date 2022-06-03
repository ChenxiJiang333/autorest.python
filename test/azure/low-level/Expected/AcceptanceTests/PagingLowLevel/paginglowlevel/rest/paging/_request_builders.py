# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._vendor import _format_url_section

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_get_no_item_name_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that must return result of the default 'value' node.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/noitemname"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_null_next_link_name_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that must ignore any kind of nextLink, and stop after page 1.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/nullnextlink"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_single_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that finishes on the first call without a nextlink.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/single"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_first_response_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation whose first response's items list is empty, but still returns a next link.
    Second (and final) call, will give you an items list of 1.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/firstResponseEmpty/1"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a nextLink that has 10 pages.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword client_request_id: Default value is None.
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response. Default value
     is None.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds. Default value is 30.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    client_request_id = kwargs.pop('client_request_id', _headers.pop('client-request-id', None))  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', _headers.pop('maxresults', None))  # type: Optional[int]
    timeout = kwargs.pop('timeout', _headers.pop('timeout', 30))  # type: int
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple"

    # Construct headers
    if client_request_id is not None:
        _headers['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        _headers['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        _headers['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_with_query_params_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a next operation. It has a different query parameter from it's
    next operation nextOperationWithQueryParams. Returns a ProductResult.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword required_query_parameter: A required integer query parameter. Put in value '100' to
     pass test. Required.
    :paramtype required_query_parameter: int
    :keyword query_constant: A constant. Must be True and will be passed as a query parameter to
     nextOperationWithQueryParams. Default value is True. Note that overriding this default value
     may result in unsupported behavior.
    :paramtype query_constant: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    query_constant = kwargs.pop('query_constant', _params.pop('queryConstant', True))  # type: bool
    required_query_parameter = kwargs.pop('required_query_parameter')  # type: int
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/getWithQueryParams"

    # Construct parameters
    _params['requiredQueryParameter'] = _SERIALIZER.query("required_query_parameter", required_query_parameter, 'int')
    _params['queryConstant'] = _SERIALIZER.query("query_constant", query_constant, 'bool')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_next_operation_with_query_params_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Next operation for getWithQueryParams. Pass in next=True to pass test. Returns a ProductResult

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword query_constant: A constant. Must be True Default value is True. Note that overriding
     this default value may result in unsupported behavior.
    :paramtype query_constant: bool
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    query_constant = kwargs.pop('query_constant', _params.pop('queryConstant', True))  # type: bool
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/nextOperationWithQueryParams"

    # Construct parameters
    _params['queryConstant'] = _SERIALIZER.query("query_constant", query_constant, 'bool')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_duplicate_params_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Define ``filter`` as a query param for all calls. However, the returned next link will also
    include the ``filter`` as part of it. Make sure you don't end up duplicating the ``filter``
    param in the url sent.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword filter: OData filter options. Pass in 'foo'. Default value is None.
    :paramtype filter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    filter = kwargs.pop('filter', _params.pop('$filter', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/duplicateParams/1"

    # Construct parameters
    if filter is not None:
        _params['$filter'] = _SERIALIZER.query("filter", filter, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_odata_multiple_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a nextLink in odata format that has 10 pages.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword client_request_id: Default value is None.
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response. Default value
     is None.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds. Default value is 30.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    client_request_id = kwargs.pop('client_request_id', _headers.pop('client-request-id', None))  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', _headers.pop('maxresults', None))  # type: Optional[int]
    timeout = kwargs.pop('timeout', _headers.pop('timeout', 30))  # type: int
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/odata"

    # Construct headers
    if client_request_id is not None:
        _headers['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        _headers['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        _headers['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_with_offset_request(
    offset,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a nextLink that has 10 pages.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param offset: Offset of return value. Required.
    :type offset: int
    :keyword client_request_id: Default value is None.
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response. Default value
     is None.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds. Default value is 30.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    client_request_id = kwargs.pop('client_request_id', _headers.pop('client-request-id', None))  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', _headers.pop('maxresults', None))  # type: Optional[int]
    timeout = kwargs.pop('timeout', _headers.pop('timeout', 30))  # type: int
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/withpath/{offset}"
    path_format_arguments = {
        "offset": _SERIALIZER.url("offset", offset, 'int'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    if client_request_id is not None:
        _headers['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        _headers['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        _headers['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_retry_first_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that fails on the first call with 500 and then retries and then get a
    response including a nextLink that has 10 pages.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/retryfirst"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_retry_second_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a nextLink that has 10 pages, of which the 2nd call fails
    first with 500. The client should retry and finish all 10 pages eventually.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/retrysecond"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_single_pages_failure_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that receives a 400 on the first call.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/single/failure"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_failure_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that receives a 400 on the second call.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/failure"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_failure_uri_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that receives an invalid nextLink.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/failureuri"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_fragment_next_link_request(
    tenant,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that doesn't return a full URL, just a fragment.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param tenant: Sets the tenant to use. Required.
    :type tenant: str
    :keyword api_version: Sets the api version to use. Required.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/fragment/{tenant}"
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api_version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_next_fragment_request(
    tenant,  # type: str
    next_link,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that doesn't return a full URL, just a fragment

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param tenant: Sets the tenant to use. Required.
    :type tenant: str
    :param next_link: Next link for list operation. Required.
    :type next_link: str
    :keyword api_version: Sets the api version to use. Required.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/fragment/{tenant}/{nextLink}"
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, 'str'),
        "nextLink": _SERIALIZER.url("next_link", next_link, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api_version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_fragment_with_grouping_next_link_request(
    tenant,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that doesn't return a full URL, just a fragment with parameters grouped.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param tenant: Sets the tenant to use. Required.
    :type tenant: str
    :keyword api_version: Sets the api version to use. Required.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/fragmentwithgrouping/{tenant}"
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api_version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_next_fragment_with_grouping_request(
    tenant,  # type: str
    next_link,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that doesn't return a full URL, just a fragment

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param tenant: Sets the tenant to use. Required.
    :type tenant: str
    :param next_link: Next link for list operation. Required.
    :type next_link: str
    :keyword api_version: Sets the api version to use. Required.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/fragmentwithgrouping/{tenant}/{nextLink}"
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, 'str'),
        "nextLink": _SERIALIZER.url("next_link", next_link, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api_version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_multiple_pages_lro_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A long-running paging operation that includes a nextLink that has 10 pages.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword client_request_id: Default value is None.
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response. Default value
     is None.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds. Default value is 30.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    client_request_id = kwargs.pop('client_request_id', _headers.pop('client-request-id', None))  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', _headers.pop('maxresults', None))  # type: Optional[int]
    timeout = kwargs.pop('timeout', _headers.pop('timeout', 30))  # type: int
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/multiple/lro"

    # Construct headers
    if client_request_id is not None:
        _headers['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        _headers['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        _headers['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_paging_model_with_item_name_with_xms_client_name_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that returns a paging model whose item name is is overriden by
    x-ms-client-name 'indexes'.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/paging/itemNameWithXMSClientName"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )
