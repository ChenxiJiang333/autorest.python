# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import build_internal_get_internal_request, build_internal_post_internal_request
from .._vendor import InternalClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class InternalClientOperationsMixin(InternalClientMixinABC):
    @distributed_trace_async
    async def _get_internal(self, *, name: str, **kwargs: Any) -> _models._models.InternalModel:
        """get_internal.

        :keyword name: Required.
        :paramtype name: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: InternalModel. The InternalModel is compatible with MutableMapping
        :rtype: ~internal.models.InternalModel
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

        cls: ClsType[_models._models.InternalModel] = kwargs.pop("cls", None)  # pylint: disable=protected-access

        request = build_internal_get_internal_request(
            name=name,
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
            deserialized = _deserialize(
                _models._models.InternalModel, response.json()  # pylint: disable=protected-access
            )

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def _post_internal(
        self, body: _models.ModelOnlyUsedByInternalOperation, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ModelOnlyUsedByInternalOperation:
        ...

    @overload
    async def _post_internal(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ModelOnlyUsedByInternalOperation:
        ...

    @overload
    async def _post_internal(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ModelOnlyUsedByInternalOperation:
        ...

    @distributed_trace_async
    async def _post_internal(
        self, body: Union[_models.ModelOnlyUsedByInternalOperation, JSON, IO], **kwargs: Any
    ) -> _models.ModelOnlyUsedByInternalOperation:
        """post_internal.

        :param body: Is one of the following types: ModelOnlyUsedByInternalOperation, JSON, IO
         Required.
        :type body: ~internal.models.ModelOnlyUsedByInternalOperation or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: ModelOnlyUsedByInternalOperation. The ModelOnlyUsedByInternalOperation is compatible
         with MutableMapping
        :rtype: ~internal.models.ModelOnlyUsedByInternalOperation
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ModelOnlyUsedByInternalOperation] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore

        request = build_internal_post_internal_request(
            content_type=content_type,
            content=_content,
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
            deserialized = _deserialize(_models.ModelOnlyUsedByInternalOperation, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
