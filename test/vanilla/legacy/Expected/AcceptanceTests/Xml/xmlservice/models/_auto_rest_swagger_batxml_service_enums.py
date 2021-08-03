# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AccessTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    P4 = "P4"
    P6 = "P6"
    P10 = "P10"
    P20 = "P20"
    P30 = "P30"
    P40 = "P40"
    P50 = "P50"
    HOT = "Hot"
    COOL = "Cool"
    ARCHIVE = "Archive"


class ArchiveStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    REHYDRATE_PENDING_TO_HOT = "rehydrate-pending-to-hot"
    REHYDRATE_PENDING_TO_COOL = "rehydrate-pending-to-cool"


class BlobType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    BLOCK_BLOB = "BlockBlob"
    PAGE_BLOB = "PageBlob"
    APPEND_BLOB = "AppendBlob"


class CopyStatusType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    PENDING = "pending"
    SUCCESS = "success"
    ABORTED = "aborted"
    FAILED = "failed"


class LeaseDurationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    INFINITE = "infinite"
    FIXED = "fixed"


class LeaseStateType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    AVAILABLE = "available"
    LEASED = "leased"
    EXPIRED = "expired"
    BREAKING = "breaking"
    BROKEN = "broken"


class LeaseStatusType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    LOCKED = "locked"
    UNLOCKED = "unlocked"


class PublicAccessType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    CONTAINER = "container"
    BLOB = "blob"