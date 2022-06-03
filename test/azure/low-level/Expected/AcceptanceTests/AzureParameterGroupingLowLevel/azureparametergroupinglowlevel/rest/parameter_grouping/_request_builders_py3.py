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

# fmt: off

def build_post_required_request(
    path: str,
    *,
    json: int,
    custom_header: Optional[str] = None,
    query: int = 30,
    **kwargs: Any
) -> HttpRequest:
    """Post a bunch of required parameters grouped.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param path: Path parameter. Required.
    :type path: str
    :keyword json: Required.
    :paramtype json: int
    :keyword custom_header: Default value is None.
    :paramtype custom_header: str
    :keyword query: Query parameter with default. Default value is 30.
    :paramtype query: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/parameterGrouping/postRequired/{path}"
    path_format_arguments = {
        "path": _SERIALIZER.url("path", path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if query is not None:
        _params['query'] = _SERIALIZER.query("query", query, 'int')

    # Construct headers
    if custom_header is not None:
        _headers['customHeader'] = _SERIALIZER.header("custom_header", custom_header, 'str')
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        json=json,
        **kwargs
    )


def build_post_optional_request(
    *,
    custom_header: Optional[str] = None,
    query: int = 30,
    **kwargs: Any
) -> HttpRequest:
    """Post a bunch of optional parameters grouped.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword custom_header: Default value is None.
    :paramtype custom_header: str
    :keyword query: Query parameter with default. Default value is 30.
    :paramtype query: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/parameterGrouping/postOptional"

    # Construct parameters
    if query is not None:
        _params['query'] = _SERIALIZER.query("query", query, 'int')

    # Construct headers
    if custom_header is not None:
        _headers['customHeader'] = _SERIALIZER.header("custom_header", custom_header, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_post_reserved_words_request(
    *,
    from_parameter: Optional[str] = None,
    accept_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Post a grouped parameters with reserved words.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword from_parameter: 'from' is a reserved word. Pass in 'bob' to pass. Default value is
     None.
    :paramtype from_parameter: str
    :keyword accept_parameter: 'accept' is a reserved word. Pass in 'yes' to pass. Default value is
     None.
    :paramtype accept_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/parameterGrouping/postReservedWords"

    # Construct parameters
    if from_parameter is not None:
        _params['from'] = _SERIALIZER.query("from_parameter", from_parameter, 'str')
    if accept_parameter is not None:
        _params['accept'] = _SERIALIZER.query("accept_parameter", accept_parameter, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_post_multi_param_groups_request(
    *,
    header_one: Optional[str] = None,
    query_one: int = 30,
    header_two: Optional[str] = None,
    query_two: int = 30,
    **kwargs: Any
) -> HttpRequest:
    """Post parameters from multiple different parameter groups.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword header_one: Default value is None.
    :paramtype header_one: str
    :keyword query_one: Query parameter with default. Default value is 30.
    :paramtype query_one: int
    :keyword header_two: Default value is None.
    :paramtype header_two: str
    :keyword query_two: Query parameter with default. Default value is 30.
    :paramtype query_two: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/parameterGrouping/postMultipleParameterGroups"

    # Construct parameters
    if query_one is not None:
        _params['query-one'] = _SERIALIZER.query("query_one", query_one, 'int')
    if query_two is not None:
        _params['query-two'] = _SERIALIZER.query("query_two", query_two, 'int')

    # Construct headers
    if header_one is not None:
        _headers['header-one'] = _SERIALIZER.header("header_one", header_one, 'str')
    if header_two is not None:
        _headers['header-two'] = _SERIALIZER.header("header_two", header_two, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_post_shared_parameter_group_object_request(
    *,
    header_one: Optional[str] = None,
    query_one: int = 30,
    **kwargs: Any
) -> HttpRequest:
    """Post parameters with a shared parameter group object.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword header_one: Default value is None.
    :paramtype header_one: str
    :keyword query_one: Query parameter with default. Default value is 30.
    :paramtype query_one: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/parameterGrouping/sharedParameterGroupObject"

    # Construct parameters
    if query_one is not None:
        _params['query-one'] = _SERIALIZER.query("query_one", query_one, 'int')

    # Construct headers
    if header_one is not None:
        _headers['header-one'] = _SERIALIZER.header("header_one", header_one, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_group_with_constant_request(
    *,
    grouped_constant: str = "foo",
    grouped_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Parameter group with a constant. Pass in 'foo' for groupedConstant and 'bar' for
    groupedParameter.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword grouped_constant: A grouped parameter that is a constant. Known values are "foo" and
     None. Default value is "foo".
    :paramtype grouped_constant: str
    :keyword grouped_parameter: Optional parameter part of a parameter grouping. Default value is
     None.
    :paramtype grouped_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/parameterGrouping/groupWithConstant"

    # Construct headers
    if grouped_constant is not None:
        _headers['groupedConstant'] = _SERIALIZER.header("grouped_constant", grouped_constant, 'str')
    if grouped_parameter is not None:
        _headers['groupedParameter'] = _SERIALIZER.header("grouped_parameter", grouped_parameter, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )
