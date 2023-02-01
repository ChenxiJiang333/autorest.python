# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, Optional, overload

from .. import _model_base
from .._model_base import rest_field


class Project(_model_base.Model):
    """Project.

    :ivar produced_by: Only valid value is 'DPG'.
    :vartype produced_by: str
    :ivar builtfrom: Only valid value is 'DPG'.
    :vartype builtfrom: str
    :ivar was_made_for: Only valid value is 'customers'.
    :vartype was_made_for: str
    """

    produced_by: Optional[str] = rest_field(name="producedBy")
    """Only valid value is 'DPG'. """
    builtfrom: Optional[str] = rest_field()
    """Only valid value is 'DPG'. """
    was_made_for: Optional[str] = rest_field(name="wasMadeFor")
    """Only valid value is 'customers'. """

    @overload
    def __init__(
        self,
        *,
        produced_by: Optional[str] = None,
        builtfrom: Optional[str] = None,
        was_made_for: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)