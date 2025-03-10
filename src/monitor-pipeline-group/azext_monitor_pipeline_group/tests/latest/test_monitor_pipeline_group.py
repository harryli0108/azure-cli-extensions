# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import *


class MonitorPipelineGroupScenario(ScenarioTest):
    @ResourceGroupPreparer()
    def test_monitor_pipeline_group(self, resource_group):
        import os
        data_path = os.path.relpath(os.path.join(os.path.abspath(__file__), '..', 'data_files'))
        self.kwargs.update({
            'rg': resource_group,
            'name': 'mygroup',
            'location': 'eastus2euap',
            'exporters_path': os.path.join(data_path, "exporters.json").replace('\\', '\\\\'),
            'extended_location_path': os.path.join(data_path, "extendedLocation.json").replace('\\', '\\\\'),
            'processors_path': os.path.join(data_path, "processors.json").replace('\\', '\\\\'),
            'receivers_path': os.path.join(data_path, "receivers.json").replace('\\', '\\\\'),
            'service_path': os.path.join(data_path, "service.json").replace('\\', '\\\\'),
            'servicepatch_path': os.path.join(data_path, "servicepatch.json").replace('\\', '\\\\')
        })

        self.cmd('az monitor pipeline-group create -g {rg} -n {name} -l {location} ' 
                 '--exporters @{exporters_path} '
                 '--processors @{processors_path} '
                 '--receivers @{receivers_path} '
                 '--service @{service_path} '
                 '--extended-location @{extended_location_path} '
                 '--network-config [] '
                 '--replicas 1 ',
                 checks=[self.check('properties.provisioningState', 'Succeeded')])
        
        self.cmd('az monitor pipeline-group show -g {rg} -n {name}', checks=[
            self.check('name', '{name}'),
            self.check('properties.provisioningState', 'Succeeded')
        ])

        self.cmd('az monitor pipeline-group list -g {rg}', checks=[
            self.check('length(@)', 1)
        ])

        self.cmd('az monitor pipeline-group update -g {rg} -n {name} --service @{servicepatch_path}', checks=[
            self.check('properties.service.pipelines[0].name', 'MyPipeline2')
        ])

        self.cmd('az monitor pipeline-group delete -g {rg} -n {name} -y')

        self.cmd('az monitor pipeline-group list -g {rg}', checks=[
            self.check('length(@)', 0)
        ])