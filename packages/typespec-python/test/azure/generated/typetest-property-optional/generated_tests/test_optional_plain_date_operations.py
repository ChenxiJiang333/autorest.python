# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OptionalClientTestBase, OptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalPlainDateOperations(OptionalClientTestBase):
    @OptionalPreparer()
    @recorded_by_proxy
    def test_get_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.plain_date.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_get_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.plain_date.get_default()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_put_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.plain_date.put_all(
            body={"property": "2020-02-20"},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_put_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.plain_date.put_default(
            body={"property": "2020-02-20"},
        )

        # please add some check logic here by yourself
        # ...