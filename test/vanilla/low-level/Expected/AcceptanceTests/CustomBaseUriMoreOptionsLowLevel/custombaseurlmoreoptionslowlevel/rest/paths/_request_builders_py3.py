# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_get_empty_request(
    key_name: str, subscription_id: str, *, key_version: Optional[str] = "v1", **kwargs: Any
) -> HttpRequest:
    """Get a 200 to test a valid base uri.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param key_name: The key name with value 'key1'.
    :type key_name: str
    :param subscription_id: The subscription id with value 'test12'.
    :type subscription_id: str
    :keyword key_version: The key version. Default value 'v1'.
    :paramtype key_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/customuri/{subscriptionId}/{keyName}")
    path_format_arguments = {
        "keyName": _SERIALIZER.url("key_name", key_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if key_version is not None:
        query_parameters["keyVersion"] = _SERIALIZER.query("key_version", key_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)