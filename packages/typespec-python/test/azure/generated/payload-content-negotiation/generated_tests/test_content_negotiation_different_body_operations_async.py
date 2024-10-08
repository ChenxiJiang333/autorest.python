# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import ContentNegotiationPreparer
from testpreparer_async import ContentNegotiationClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContentNegotiationDifferentBodyOperationsAsync(ContentNegotiationClientTestBaseAsync):
    @ContentNegotiationPreparer()
    @recorded_by_proxy_async
    async def test_different_body_get_avatar_as_png(self, contentnegotiation_endpoint):
        client = self.create_async_client(endpoint=contentnegotiation_endpoint)
        response = await client.different_body.get_avatar_as_png(
            accept="image/png",
        )

        # please add some check logic here by yourself
        # ...

    @ContentNegotiationPreparer()
    @recorded_by_proxy_async
    async def test_different_body_get_avatar_as_json(self, contentnegotiation_endpoint):
        client = self.create_async_client(endpoint=contentnegotiation_endpoint)
        response = await client.different_body.get_avatar_as_json(
            accept="application/json",
        )

        # please add some check logic here by yourself
        # ...
