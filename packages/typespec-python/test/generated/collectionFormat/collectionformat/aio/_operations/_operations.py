# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._model_base import _deserialize
from ..._operations._operations import (
    build_collection_format_test_csv_header_request,
    build_collection_format_test_csv_request,
    build_collection_format_test_default_header_request,
    build_collection_format_test_multi_request,
)
from .._vendor import CollectionFormatClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CollectionFormatClientOperationsMixin(CollectionFormatClientMixinABC):
    @distributed_trace_async
    async def test_multi(self, *, colors: List[str], **kwargs: Any) -> _models.MessageResponse:
        """test_multi.

        :keyword colors: Possible values for colors are [blue,red,green]. Required.
        :paramtype colors: list[str]
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: MessageResponse. The MessageResponse is compatible with MutableMapping
        :rtype: ~collectionformat.models.MessageResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.MessageResponse] = kwargs.pop("cls", None)

        request = build_collection_format_test_multi_request(
            colors=colors,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.MessageResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def test_csv(self, *, colors: List[str], **kwargs: Any) -> _models.MessageResponse:
        """test_csv.

        :keyword colors: Possible values for colors are [blue,red,green]. Required.
        :paramtype colors: list[str]
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: MessageResponse. The MessageResponse is compatible with MutableMapping
        :rtype: ~collectionformat.models.MessageResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.MessageResponse] = kwargs.pop("cls", None)

        request = build_collection_format_test_csv_request(
            colors=colors,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.MessageResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def test_csv_header(self, *, colors: List[str], **kwargs: Any) -> _models.MessageResponse:
        """test_csv_header.

        :keyword colors: Possible values for colors are [blue,red,green]. Required.
        :paramtype colors: list[str]
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: MessageResponse. The MessageResponse is compatible with MutableMapping
        :rtype: ~collectionformat.models.MessageResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.MessageResponse] = kwargs.pop("cls", None)

        request = build_collection_format_test_csv_header_request(
            colors=colors,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.MessageResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def test_default_header(self, *, colors: List[str], **kwargs: Any) -> _models.MessageResponse:
        """test_default_header.

        :keyword colors: Possible values for colors are [blue,red,green]. Required.
        :paramtype colors: list[str]
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: MessageResponse. The MessageResponse is compatible with MutableMapping
        :rtype: ~collectionformat.models.MessageResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.MessageResponse] = kwargs.pop("cls", None)

        request = build_collection_format_test_default_header_request(
            colors=colors,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.MessageResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore