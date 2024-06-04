# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.clientgenerator.core.usage import UsageClient


class UsageClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(UsageClient)
        return self.create_client_from_credential(
            UsageClient,
            credential=credential,
            endpoint=endpoint,
        )


UsagePreparer = functools.partial(PowerShellPreparer, "usage", usage_endpoint="https://fake_usage_endpoint.com")