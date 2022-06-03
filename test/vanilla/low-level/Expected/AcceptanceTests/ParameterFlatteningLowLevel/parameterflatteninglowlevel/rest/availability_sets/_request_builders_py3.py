# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, IO, Optional, Union, overload

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._vendor import _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

@overload
def build_update_request(
    resource_group_name: str,
    avset: str,
    *,
    json: JSON,
    content_type: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Updates the tags for an availability set.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param resource_group_name: The name of the resource group. Required.
    :type resource_group_name: str
    :param avset: The name of the storage availability set. Required.
    :type avset: str
    :keyword json: The tags. Required.
    :paramtype json: JSON
    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "tags": {
                    "str": "str"  # A description about the set of tags. Required.
                }
            }
    """


@overload
def build_update_request(
    resource_group_name: str,
    avset: str,
    *,
    content: IO,
    content_type: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Updates the tags for an availability set.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param resource_group_name: The name of the resource group. Required.
    :type resource_group_name: str
    :param avset: The name of the storage availability set. Required.
    :type avset: str
    :keyword content: The tags. Required.
    :paramtype content: IO
    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_update_request(
    resource_group_name: str,
    avset: str,
    **kwargs: Any
) -> HttpRequest:
    """Updates the tags for an availability set.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :param resource_group_name: The name of the resource group. Required.
    :type resource_group_name: str
    :param avset: The name of the storage availability set. Required.
    :type avset: str
    :keyword json: The tags. Is either a model type or a IO type. Required.
    :paramtype json: JSON or IO
    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    # Construct URL
    _url = "/parameterFlattening/{resourceGroupName}/{availabilitySetName}"
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "availabilitySetName": _SERIALIZER.url("avset", avset, 'str', max_length=80),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="PATCH",
        url=_url,
        headers=_headers,
        **kwargs
    )
