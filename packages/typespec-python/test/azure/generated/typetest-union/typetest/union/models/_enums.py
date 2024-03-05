# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class EnumsOnlyCasesLr(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of EnumsOnlyCasesLr."""

    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


class EnumsOnlyCasesUd(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of EnumsOnlyCasesUd."""

    UP = "up"
    DOWN = "down"


class GetResponseProp2(float, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of GetResponseProp2."""

    ENUM_1_1 = 1.1
    ENUM_2_2 = 2.2
    ENUM_3_3 = 3.3


class GetResponseProp3(int, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of GetResponseProp3."""

    ENUM_1 = 1
    ENUM_2 = 2
    ENUM_3 = 3


class GetResponseProp4(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of GetResponseProp4."""

    B = "b"
    C = "c"


class GetResponseProp5(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of GetResponseProp5."""

    A = "a"
    B = "b"
    C = "c"


class StringExtensibleNamedUnion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of StringExtensibleNamedUnion."""

    OPTION_B = "b"
    C = "c"