# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ChildFlattenModel(_model_base.Model):
    """This is the child model to be flattened. And it has flattened property as well.


    :ivar summary: Required.
    :vartype summary: str
    :ivar properties: Required.
    :vartype properties: ~specs.azure.clientgenerator.core.flattenproperty.models.ChildModel
    """

    summary: str = rest_field()
    """Required."""
    properties: "_models.ChildModel" = rest_field()
    """Required."""

    __flattened_items = ["description", "age"]

    @overload
    def __init__(
        self,
        *,
        summary: str,
        properties: "_models.ChildModel",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        _flattened_input = {k: kwargs.pop(k) for k in kwargs.keys() & self.__flattened_items}
        super().__init__(*args, **kwargs)
        for k, v in _flattened_input.items():
            setattr(self, k, v)

    def __getattr__(self, name: str) -> Any:
        if name in self.__flattened_items:
            if self.properties is None:
                return None
            return getattr(self.properties, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.__flattened_items:
            if self.properties is None:
                self.properties = self._attr_to_rest_field["properties"]._class_type()
            setattr(self.properties, key, value)
        else:
            super().__setattr__(key, value)


class ChildModel(_model_base.Model):
    """This is the child model to be flattened.


    :ivar description: Required.
    :vartype description: str
    :ivar age: Required.
    :vartype age: int
    """

    description: str = rest_field()
    """Required."""
    age: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        description: str,
        age: int,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FlattenModel(_model_base.Model):
    """This is the model with one level of flattening.


    :ivar name: Required.
    :vartype name: str
    :ivar properties: Required.
    :vartype properties: ~specs.azure.clientgenerator.core.flattenproperty.models.ChildModel
    """

    name: str = rest_field()
    """Required."""
    properties: "_models.ChildModel" = rest_field()
    """Required."""

    __flattened_items = ["description", "age"]

    @overload
    def __init__(
        self,
        *,
        name: str,
        properties: "_models.ChildModel",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        _flattened_input = {k: kwargs.pop(k) for k in kwargs.keys() & self.__flattened_items}
        super().__init__(*args, **kwargs)
        for k, v in _flattened_input.items():
            setattr(self, k, v)

    def __getattr__(self, name: str) -> Any:
        if name in self.__flattened_items:
            if self.properties is None:
                return None
            return getattr(self.properties, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.__flattened_items:
            if self.properties is None:
                self.properties = self._attr_to_rest_field["properties"]._class_type()
            setattr(self.properties, key, value)
        else:
            super().__setattr__(key, value)


class NestedFlattenModel(_model_base.Model):
    """This is the model with two levels of flattening.


    :ivar name: Required.
    :vartype name: str
    :ivar properties: Required.
    :vartype properties: ~specs.azure.clientgenerator.core.flattenproperty.models.ChildFlattenModel
    """

    name: str = rest_field()
    """Required."""
    properties: "_models.ChildFlattenModel" = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        properties: "_models.ChildFlattenModel",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)