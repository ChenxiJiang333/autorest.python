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
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import (
    build_dev_driven_get_model_request,
    build_dev_driven_get_pages_request,
    build_dev_driven_lro_request,
    build_dev_driven_post_model_request,
)
from .._vendor import DevDrivenClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DevDrivenClientOperationsMixin(DevDrivenClientMixinABC):
    @distributed_trace_async
    async def get_model(self, mode: Union[str, _models.Mode], **kwargs: Any) -> _models.Product:
        """Get models that you will either return to end users as a raw body, or with a model added during
        grow up.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
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

        cls: ClsType[_models.Product] = kwargs.pop("cls", None)

        request = build_dev_driven_get_model_request(
            mode=mode,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = _deserialize(_models.Product, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def post_model(
        self,
        mode: Union[str, _models.Mode],
        input: _models.Input,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Required.
        :type input: ~resiliency.devdriven.models.Input
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_model(
        self, mode: Union[str, _models.Mode], input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_model(
        self, mode: Union[str, _models.Mode], input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def post_model(
        self, mode: Union[str, _models.Mode], input: Union[_models.Input, JSON, IO], **kwargs: Any
    ) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Is one of the following types: model, JSON, IO
         Required.
        :type input: ~resiliency.devdriven.models.Input or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: Product. The Product is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
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
        cls: ClsType[_models.Product] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder)

        request = build_dev_driven_post_model_request(
            mode=mode,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = _deserialize(_models.Product, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_pages(self, **kwargs: Any) -> AsyncIterable["_models.Product"]:
        """Get pages that you will either return to users in pages of raw bodies, or pages of models
        following group.

        :return: An iterator like instance of Product. The Product is compatible with MutableMapping
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~resiliency.devdriven.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.CustomPageProduct] = kwargs.pop("cls", None)  # pylint: disable=protected-access

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_dev_driven_get_pages_request(
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request.url = self._client.format_url(request.url)

            return request

        async def extract_data(pipeline_response):
            deserialized = _deserialize(_models._models.CustomPageProduct, pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def lro(self, mode: Union[str, _models.Mode], **kwargs: Any) -> _models.LROProduct:
        """Long running put request that will either return to end users a final payload of a raw body, or
        a final payload of a model after the SDK has grown up.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :return: LROProduct. The LROProduct is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.LROProduct
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

        cls: ClsType[_models.LROProduct] = kwargs.pop("cls", None)

        request = build_dev_driven_lro_request(
            mode=mode,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = _deserialize(_models.LROProduct, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
