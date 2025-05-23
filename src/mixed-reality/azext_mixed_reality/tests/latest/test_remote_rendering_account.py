# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
from .recording_processors import KeyReplacer


class RemoteRenderingAccountScenarioTest(ScenarioTest):
    def __init__(self, method_name):
        super(RemoteRenderingAccountScenarioTest, self).__init__(
            method_name, recording_processors=[KeyReplacer()]
        )

    @ResourceGroupPreparer(location="eastus2", parameter_name_for_location="location")
    def test_remote_rendering_account_scenario(self, resource_group, location):
        self.kwargs.update(
            {
                "rg": resource_group,
                "account_name": "remote-rendering-account-name",
                "account_name1": "remote-rendering-account-name1",
                "storage_account_name": "storage_account_name",
                "storage_account_name1": "storage_account_name1",
            }
        )

        # Create with minimum parameters
        self.cmd(
            "remote-rendering-account create -g {rg} -n {account_name}",
            checks=self.not_exists("tags"),
        )

        # Create with more parameters
        self.cmd(
            "remote-rendering-account create -g {rg} -n {account_name1} "
            "--storage-account-name {storage_account_name} --tag tag=tag --kind name=P3",
            checks=[
                self.exists("tags"),
                self.check("storageAccountName", "{storage_account_name}"),
            ],
        )

        self.cmd(
            "remote-rendering-account update -g {rg} -n {account_name} "
            "--storage-account-name {storage_account_name1}",
            checks=self.check("storageAccountName", "{storage_account_name1}"),
        )

        self.cmd("remote-rendering-account show -g {rg} -n {account_name}")
        self.cmd(
            "remote-rendering-account list -g {rg}", checks=self.check("length(@)", 2)
        )
        self.cmd("remote-rendering-account delete -g {rg} -n {account_name1}")
        self.cmd(
            "remote-rendering-account list -g {rg}", checks=self.check("length(@)", 1)
        )

        # key
        x = "primaryKey"
        y = "secondaryKey"
        key = self.cmd(
            "remote-rendering-account key show -g {rg} -n {account_name}"
        ).get_output_in_json()
        key1 = self.cmd(
            "remote-rendering-account key renew -g {rg} -n {account_name}"
        ).get_output_in_json()
        self.assertEqual(key[y], key1[y])
        # self.assertNotEqual(key[x], key1[x])  # only for live test

        key2 = self.cmd(
            "remote-rendering-account key renew -g {rg} -n {account_name} -k primary"
        ).get_output_in_json()
        self.assertEqual(key2[y], key1[y])
        # self.assertNotEqual(key2[x], key1[x])  # only for live test

        key3 = self.cmd(
            "remote-rendering-account key renew -g {rg} -n {account_name} -k secondary"
        ).get_output_in_json()
        self.assertEqual(key2[x], key3[x])
        # self.assertNotEqual(key2[y], key3[y])  # only for live test
