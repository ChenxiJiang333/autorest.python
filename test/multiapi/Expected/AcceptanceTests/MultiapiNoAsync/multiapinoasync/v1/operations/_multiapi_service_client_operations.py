# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class MultiapiServiceClientOperationsMixin(object):

    def test_one(
        self,
        id,  # type: int
        message=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """TestOne should be in an FirstVersionOperationsMixin.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "1.0.0"

        # Construct URL
        url = self.test_one.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['id'] = self._serialize.query("id", id, 'int')
        if message is not None:
            query_parameters['message'] = self._serialize.query("message", message, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    test_one.metadata = {'url': '/multiapi/testOneEndpoint'}  # type: ignore

    def _test_lro_initial(
        self,
        product=None,  # type: Optional["models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Product"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Product"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._test_lro_initial.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _test_lro_initial.metadata = {'url': '/multiapi/lro'}  # type: ignore

    def begin_test_lro(
        self,
        product=None,  # type: Optional["models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put.
        :type product: ~multiapinoasync.v1.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns Product
        :rtype: ~azure.core.polling.LROPoller[~multiapinoasync.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Product"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._test_lro_initial(
            product=product,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Product', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = LROBasePolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_test_lro.metadata = {'url': '/multiapi/lro'}  # type: ignore