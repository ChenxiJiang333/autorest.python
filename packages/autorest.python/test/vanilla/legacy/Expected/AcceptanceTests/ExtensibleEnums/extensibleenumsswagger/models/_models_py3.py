# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional, TYPE_CHECKING, Union

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Pet(_serialization.Model):
    """Pet.

    All required parameters must be populated in order to send to Azure.

    :ivar name: name.
    :vartype name: str
    :ivar days_of_week: Type of Pet. Known values are: "Monday", "Tuesday", "Wednesday",
     "Thursday", "Friday", "Saturday", and "Sunday".
    :vartype days_of_week: str or ~extensibleenumsswagger.models.DaysOfWeekExtensibleEnum
    :ivar int_enum: Required. Known values are: "1", "2", and "3".
    :vartype int_enum: str or ~extensibleenumsswagger.models.IntEnum
    """

    _validation = {
        "int_enum": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "days_of_week": {"key": "DaysOfWeek", "type": "str"},
        "int_enum": {"key": "IntEnum", "type": "str"},
    }

    def __init__(
        self,
        *,
        int_enum: Union[str, "_models.IntEnum"],
        name: Optional[str] = None,
        days_of_week: Union[str, "_models.DaysOfWeekExtensibleEnum"] = "Friday",
        **kwargs
    ):
        """
        :keyword name: name.
        :paramtype name: str
        :keyword days_of_week: Type of Pet. Known values are: "Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", and "Sunday".
        :paramtype days_of_week: str or ~extensibleenumsswagger.models.DaysOfWeekExtensibleEnum
        :keyword int_enum: Required. Known values are: "1", "2", and "3".
        :paramtype int_enum: str or ~extensibleenumsswagger.models.IntEnum
        """
        super().__init__(**kwargs)
        self.name = name
        self.days_of_week = days_of_week
        self.int_enum = int_enum