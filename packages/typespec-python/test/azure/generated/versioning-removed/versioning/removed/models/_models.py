# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import _types, models as _models


class ModelV2(_model_base.Model):
    """ModelV2.

    All required parameters must be populated in order to send to server.

    :ivar prop: Required.
    :vartype prop: str
    :ivar enum_prop: Required. "enumMemberV2"
    :vartype enum_prop: str or ~versioning.removed.models.EnumV2
    :ivar union_prop: Required. Is either a str type or a float type.
    :vartype union_prop: str or float
    """

    prop: str = rest_field()
    """Required."""
    enum_prop: Union[str, "_models.EnumV2"] = rest_field(name="enumProp")
    """Required. \"enumMemberV2\""""
    union_prop: "_types.UnionV2" = rest_field(name="unionProp")
    """Required. Is either a str type or a float type."""

    @overload
    def __init__(
        self,
        *,
        prop: str,
        enum_prop: Union[str, "_models.EnumV2"],
        union_prop: "_types.UnionV2",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)