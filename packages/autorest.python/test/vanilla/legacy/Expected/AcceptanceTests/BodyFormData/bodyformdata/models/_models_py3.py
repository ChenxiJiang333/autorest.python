# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import IO, List, Optional

from .. import _serialization


class Error(_serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.message = message


class Paths1MqqetpFormdataStreamUploadfilePostRequestbodyContentMultipartFormDataSchema(_serialization.Model):
    """Paths1MqqetpFormdataStreamUploadfilePostRequestbodyContentMultipartFormDataSchema.

    All required parameters must be populated in order to send to Azure.

    :ivar file_content: File to upload. Required.
    :vartype file_content: IO
    :ivar file_name: File name to upload. Name has to be spelled exactly as written here. Required.
    :vartype file_name: str
    """

    _validation = {
        "file_content": {"required": True},
        "file_name": {"required": True},
    }

    _attribute_map = {
        "file_content": {"key": "fileContent", "type": "IO"},
        "file_name": {"key": "fileName", "type": "str"},
    }

    def __init__(self, *, file_content: IO, file_name: str, **kwargs):
        """
        :keyword file_content: File to upload. Required.
        :paramtype file_content: IO
        :keyword file_name: File name to upload. Name has to be spelled exactly as written here.
         Required.
        :paramtype file_name: str
        """
        super().__init__(**kwargs)
        self.file_content = file_content
        self.file_name = file_name


class Paths1P3Stk3FormdataStreamUploadfilesPostRequestbodyContentMultipartFormDataSchema(_serialization.Model):
    """Paths1P3Stk3FormdataStreamUploadfilesPostRequestbodyContentMultipartFormDataSchema.

    All required parameters must be populated in order to send to Azure.

    :ivar file_content: Files to upload. Required.
    :vartype file_content: list[IO]
    """

    _validation = {
        "file_content": {"required": True},
    }

    _attribute_map = {
        "file_content": {"key": "fileContent", "type": "[IO]"},
    }

    def __init__(self, *, file_content: List[IO], **kwargs):
        """
        :keyword file_content: Files to upload. Required.
        :paramtype file_content: list[IO]
        """
        super().__init__(**kwargs)
        self.file_content = file_content