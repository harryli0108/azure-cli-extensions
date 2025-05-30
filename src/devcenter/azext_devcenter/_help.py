# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

helps[
    "devcenter dev"
] = """
    type: group
    short-summary: "Manage devcenter developer resources."
"""
helps[
    "devcenter dev project"
] = """
    type: group
    short-summary: Manage projects.
"""

helps[
    "devcenter dev project list"
] = """
    type: command
    short-summary: "List all projects."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev project list --dev-center-name "ContosoDevCenter"
      - name: List using endpoint
        text: |-
               az devcenter dev project list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/"
"""

helps[
    "devcenter dev project show"
] = """
    type: command
    short-summary: "Get a project."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev project show --dev-center-name "ContosoDevCenter" \
--name "DevProject"
      - name: Get using endpoint
        text: |-
               az devcenter dev project show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "DevProject"
"""

helps[
    "devcenter dev project list-abilities"
] = """
    type: command
    short-summary: "List the signed-in user's permitted abilities in a project."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev project list-abilities --dev-center-name "ContosoDevCenter" --user-id "00000000-0000-0000-0000-000000000000" \
--name "DevProject"
      - name: List using endpoint
        text: |-
               az devcenter dev project list-abilities --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --user-id "00000000-0000-0000-0000-000000000000" \
--name "DevProject"
"""

helps[
    "devcenter dev project show-operation"
] = """
    type: command
    short-summary: "Get the status of an operation."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev project show-operation --dev-center-name "ContosoDevCenter" \
--name "DevProject" --operation-id "f5dbdfab-fa0e-4831-8d13-25359aa5e680"
      - name: Get using endpoint
        text: |-
               az devcenter dev project show-operation --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "DevProject" --operation-id "f5dbdfab-fa0e-4831-8d13-25359aa5e680"
"""

helps[
    "devcenter dev pool"
] = """
    type: group
    short-summary: Manage pools.
"""

helps[
    "devcenter dev pool list"
] = """
    type: command
    short-summary: "List available pools."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev pool list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject"
      - name: List using end point
        text: |-
               az devcenter dev pool list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject"
"""

helps[
    "devcenter dev pool show"
] = """
    type: command
    short-summary: "Get a pool."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev pool show --dev-center-name "ContosoDevCenter" --name \
"DevPool" --project-name "DevProject"
      - name: Get using endpoint
        text: |-
               az devcenter dev pool show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --name \
"DevPool" --project-name "DevProject"
"""

helps[
    "devcenter dev schedule"
] = """
    type: group
    short-summary: Manage schedules.
"""

helps[
    "devcenter dev schedule list"
] = """
    type: command
    short-summary: "List schedules."
    examples:
      - name: List schedules by project using dev center
        text: |-
               az devcenter dev schedule list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject"
      - name: List schedules by project using endpoint
        text: |-
               az devcenter dev schedule list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject"
      - name: List schedules by pool using dev center
        text: |-
               az devcenter dev schedule list --dev-center-name "ContosoDevCenter" \
--pool-name "DevPool" --project-name "DevProject"
      - name: List schedules by pool using endpoint
        text: |-
               az devcenter dev schedule list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--pool-name "DevPool" --project-name "DevProject"
"""

helps[
    "devcenter dev schedule show"
] = """
    type: command
    short-summary: "Get a schedule."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev schedule show --dev-center-name "ContosoDevCenter" \
--pool-name "DevPool" --project-name "DevProject"
      - name: Get using endpoint
        text: |-
               az devcenter dev schedule show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--pool-name "DevPool" --project-name "DevProject"
"""

helps[
    "devcenter dev approval"
] = """
    type: group
    short-summary: Manage approvals.
"""

helps[
    "devcenter dev approval list"
] = """
    type: command
    short-summary: "List Dev Box creations that are pending approval."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev approval list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject"
      - name: List using endpoint
        text: |-
               az devcenter dev approval list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject"
"""

helps[
    "devcenter dev add-on"
] = """
    type: group
    short-summary: Manage dev box add ons.
"""

helps[
    "devcenter dev add-on create"
] = """
    type: command
    short-summary: "Create a dev box add on."
    examples:
      - name: Create using dev center
        text: |-
               az devcenter dev add-on create --dev-box-name "myDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
      - name: Create using endpoint
        text: |-
               az devcenter dev add-on create --dev-box-name "myDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
"""

helps[
    "devcenter dev add-on delete"
] = """
    type: command
    short-summary: "Delete a dev box add on."
    examples:
      - name: Delete using dev center
        text: |-
               az devcenter dev add-on delete --dev-box-name "myDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
      - name: Delete using endpoint
        text: |-
               az devcenter dev add-on delete --dev-box-name "myDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
"""

helps[
    "devcenter dev add-on disable"
] = """
    type: command
    short-summary: "Disable a dev box add on."
    examples:
      - name: Disable using dev center
        text: |-
               az devcenter dev add-on disable --dev-box-name "myDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
      - name: Disable using endpoint
        text: |-
               az devcenter dev add-on disable --dev-box-name "myDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
"""

helps[
    "devcenter dev add-on enable"
] = """
    type: command
    short-summary: "Enable a dev box add on."
    examples:
      - name: Enable using dev center
        text: |-
               az devcenter dev add-on enable --dev-box-name "myDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
      - name: Enable using endpoint
        text: |-
               az devcenter dev add-on enable --dev-box-name "myDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
"""

helps[
    "devcenter dev add-on list"
] = """
    type: command
    short-summary: "List add ons for a dev box"
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev add-on list --dev-box-name "myDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List using endpoint
        text: |-
               az devcenter dev add-on list --dev-box-name "myDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev add-on show"
] = """
    type: command
    short-summary: "Get a dev box add on."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev add-on show --dev-box-name "myDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
      - name: Get using endpoint
        text: |-
               az devcenter dev add-on show --dev-box-name "myDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --add-on-name "devboxtunnel-sys-default"
"""

helps[
    "devcenter dev dev-box"
] = """
    type: group
    short-summary: Manage dev boxes.
"""

helps[
    "devcenter dev dev-box list"
] = """
    type: command
    short-summary: "List dev boxes for a user, list dev boxes in the dev center for a \
project and user, or list dev boxes that the caller has access to in the dev center."
    examples:
      - name: List all dev boxes in the dev center
        text: |-
               az devcenter dev dev-box list --dev-center-name "ContosoDevCenter"
      - name: List all dev boxes in the dev center using endpoint
        text: |-
               az devcenter dev dev-box list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/"
      - name: List by user using dev center
        text: |-
               az devcenter dev dev-box list --dev-center-name "ContosoDevCenter" \
--user-id "00000000-0000-0000-0000-000000000000"
      - name: List by user using endpoint
        text: |-
               az devcenter dev dev-box list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--user-id "00000000-0000-0000-0000-000000000000"
      - name: List by user and project using dev center
        text: |-
               az devcenter dev dev-box list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List by user and project using endpoint
        text: |-
               az devcenter dev dev-box list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box show"
] = """
    type: command
    short-summary: "Get a dev box."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev dev-box show --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Get using endpoint
        text: |-
               az devcenter dev dev-box show --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""


helps[
    "devcenter dev dev-box create"
] = """
    type: command
    short-summary: "Create a dev box."
    examples:
      - name: Create using dev center
        text: |-
               az devcenter dev dev-box create --pool-name "LargeDevWorkStationPool" --name "MyDevBox" --dev-center-name \
"ContosoDevCenter" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Create using endpoint
        text: |-
               az devcenter dev dev-box create --pool-name "LargeDevWorkStationPool" --name "MyDevBox" --endpoint \
"https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box delete"
] = """
    type: command
    short-summary: "Delete a dev box."
    examples:
      - name: Delete using dev center
        text: |-
               az devcenter dev dev-box delete --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Delete using endpoint
        text: |-
               az devcenter dev dev-box delete --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box show-remote-connection"
] = """
    type: command
    short-summary: "Get remote connection info."
    examples:
      - name: Get remote connection using dev center
        text: |-
               az devcenter dev dev-box show-remote-connection --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Get remote connection using dev center
        text: |-
               az devcenter dev dev-box show-remote-connection --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box start"
] = """
    type: command
    short-summary: "Start a dev box."
    examples:
      - name: Start using dev center
        text: |-
               az devcenter dev dev-box start --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Start using endpoint
        text: |-
               az devcenter dev dev-box start --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box align"
] = """
    type: command
    short-summary: "Align a dev box to the pools current pool configuration."
    examples:
      - name: Align using dev center
        text: |-
               az devcenter dev dev-box align --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Align using endpoint
        text: |-
               az devcenter dev dev-box align --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box approve"
] = """
    type: command
    short-summary: "Approve the creation of a dev box."
    examples:
      - name: Approve using dev center
        text: |-
               az devcenter dev dev-box approve --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Approve using endpoint
        text: |-
               az devcenter dev dev-box approve --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box set-active-hours"
] = """
    type: command
    short-summary: "Lets a user set their own active hours for their Dev Box, overriding the defaults set at the pool level."
    examples:
      - name: Set active hours using dev center
        text: |-
               az devcenter dev dev-box set-active-hours --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --time-zone "America/Los_Angeles" --start-time-hour "9" --end-time-hour "17"
      - name: Set active hours using endpoint
        text: |-
               az devcenter dev dev-box set-active-hours --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --time-zone "America/Los_Angeles" --start-time-hour "9" --end-time-hour "17"
"""

helps[
    "devcenter dev dev-box restart"
] = """
    type: command
    short-summary: "Restart a dev box."
    examples:
      - name: Restart using dev center
        text: |-
               az devcenter dev dev-box restart --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Restart using endpoint
        text: |-
               az devcenter dev dev-box restart --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box repair"
] = """
    type: command
    short-summary: "Attempts automated repair steps to resolve common problems on a Dev Box. The dev box may restart during this operation."
    examples:
      - name: Repair using dev center
        text: |-
               az devcenter dev dev-box repair --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Repair using endpoint
        text: |-
               az devcenter dev dev-box repair --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box stop"
] = """
    type: command
    short-summary: "Stop a dev box."
    examples:
      - name: Stop using dev center
        text: |-
               az devcenter dev dev-box stop --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Stop using endpoint
        text: |-
               az devcenter dev dev-box stop --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box list-action"
] = """
    type: command
    short-summary: "List actions on a dev box."
    examples:
      - name: List actions using dev center
        text: |-
               az devcenter dev dev-box list-action --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --name "myDevBox" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List actions using endpoint
        text: |-
               az devcenter dev dev-box list-action --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --name "myDevBox" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box delay-action"
] = """
    type: command
    short-summary: "Delay an action."
    examples:
      - name: Delay action using dev center
        text: |-
               az devcenter dev dev-box delay-action --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --delay-time "04:30" --name "myDevBox" \
--action-name "schedule-default" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Delay action using endpoint
        text: |-
               az devcenter dev dev-box delay-action --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --delay-time "04:30" --name "myDevBox" \
--action-name "schedule-default" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box delay-all-actions"
] = """
    type: command
    short-summary: "Delay all actions."
    examples:
      - name: Delay all actions using dev center
        text: |-
               az devcenter dev dev-box delay-all-actions --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --delay-time "04:30" --name "myDevBox" \
--user-id "00000000-0000-0000-0000-000000000000"
      - name: Delay all actions using endpoint
        text: |-
               az devcenter dev dev-box delay-all-actions --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --delay-time "04:30" --name "myDevBox" \
--user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box list-operation"
] = """
    type: command
    short-summary: "Lists operations on the dev box which have occurred within the past 90 days."
    examples:
      - name: List operations using dev center
        text: |-
               az devcenter dev dev-box list-operation --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --name "myDevBox" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List operations using endpoint
        text: |-
               az devcenter dev dev-box list-operation --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --name "myDevBox" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box show-operation"
] = """
    type: command
    short-summary: "Get an operation on a dev box."
    examples:
      - name: Get operation using dev center
        text: |-
               az devcenter dev dev-box show-operation --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --name "myDevBox" --operation-id \
"f5dbdfab-fa0e-4831-8d13-25359aa5e680" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Get operation using endpoint
        text: |-
               az devcenter dev dev-box show-operation --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --name "myDevBox" --operation-id \
"f5dbdfab-fa0e-4831-8d13-25359aa5e680" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box show-action"
] = """
    type: command
    short-summary: "Get an action."
    examples:
      - name: Get action using dev center
        text: |-
               az devcenter dev dev-box show-action --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --name "myDevBox" --action-name \
"schedule-default" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Get action using endpoint
        text: |-
               az devcenter dev dev-box show-action --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --name "myDevBox" --action-name \
"schedule-default" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box skip-action"
] = """
    type: command
    short-summary: "Skip an action."
    examples:
      - name: Skip action using dev center
        text: |-
               az devcenter dev dev-box skip-action --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --name "myDevBox" --action-name \
"schedule-default" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Skip action using endpoint
        text: |-
               az devcenter dev dev-box skip-action --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --name "myDevBox" --action-name \
"schedule-default" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box capture-snapshot"
] = """
    type: command
    short-summary: "Captures a manual snapshot of the dev box."
    examples:
      - name: Capture snapshot using dev center
        text: |-
               az devcenter dev dev-box capture-snapshot --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Capture snapshot using endpoint
        text: |-
               az devcenter dev dev-box capture-snapshot --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev dev-box restore-snapshot"
] = """
    type: command
    short-summary: "Restores a dev box to a specified snapshot."
    examples:
      - name: Restore snapshot using dev center
        text: |-
               az devcenter dev dev-box restore-snapshot --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --snapshot-id "CPC_f5dbdfab-fa0e-4831-8d13-25359aa5e680"
      - name: Restore snapshot using endpoint
        text: |-
               az devcenter dev dev-box restore-snapshot --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --snapshot-id "CPC_f5dbdfab-fa0e-4831-8d13-25359aa5e680"
"""

helps[
    "devcenter dev dev-box show-snapshot"
] = """
    type: command
    short-summary: "Get a snapshot by snapshot id."
    examples:
      - name: Get snapshot using dev center
        text: |-
               az devcenter dev dev-box show-snapshot --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --snapshot-id "CPC_f5dbdfab-fa0e-4831-8d13-25359aa5e680"
      - name: Get snapshot using endpoint
        text: |-
               az devcenter dev dev-box show-snapshot --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --snapshot-id "CPC_f5dbdfab-fa0e-4831-8d13-25359aa5e680"
"""

helps[
    "devcenter dev dev-box list-snapshot"
] = """
    type: command
    short-summary: "List snapshots for a dev box"
    examples:
      - name: List snapshots using dev center
        text: |-
               az devcenter dev dev-box list-snapshot --name "MyDevBox" --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List snapshots using endpoint
        text: |-
               az devcenter dev dev-box list-snapshot --name "MyDevBox" --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev environment"
] = """
    type: group
    short-summary: Manage environments.
"""

helps[
    "devcenter dev environment list"
] = """
    type: command
    short-summary: "List the environments for a project or list the environments for a user within a project."
    examples:
      - name: List by project using dev center
        text: |-
              az devcenter dev environment list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject"
      - name: List by project using endpoint
        text: |-
              az devcenter dev environment list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject"
      - name: List by user and project using dev center
        text: |-
               az devcenter dev environment list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List by user and project using endpoint
        text: |-
               az devcenter dev environment list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev environment show"
] = """
    type: command
    short-summary: "Get an environment."
    examples:
      - name: Get using dev center
        text: |-
              az devcenter dev environment show --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Get using endpoint
        text: |-
              az devcenter dev environment show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""


helps[
    "devcenter dev environment create"
] = """
    type: command
    short-summary: "Create an environment."
    examples:
      - name: Create using dev center
        text: |-
               az devcenter dev environment create --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--catalog-name "main" --environment-definition-name "helloworld" --environment-type "DevTest" --parameters "{\\"functionAppRuntime\\":\\"node\
\\",\\"storageAccountType\\":\\"Standard_LRS\\"}" --name "mydevenv" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Create using endpoint
        text: |-
               az devcenter dev environment create --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--catalog-name "main" --environment-definition-name "helloworld" --environment-type "DevTest" --parameters "{\\"functionAppRuntime\\":\\"node\
\\",\\"storageAccountType\\":\\"Standard_LRS\\"}" --name "mydevenv" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev environment update"
] = """
    type: command
    short-summary: "Update an environment."
    examples:
      - name: Update using dev center
        text: |-
               az devcenter dev environment update --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--name "mydevenv" --user-id "00000000-0000-0000-0000-000000000000" --parameters "{\\"functionAppRuntime\\":\\"node\
\\",\\"storageAccountType\\":\\"Standard_LRS\\"}"
      - name: Update using endpoint
        text: |-
               az devcenter dev environment update --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--name "mydevenv" --user-id "00000000-0000-0000-0000-000000000000" --parameters "{\\"functionAppRuntime\\":\\"node\
\\",\\"storageAccountType\\":\\"Standard_LRS\\"}"
"""

helps[
    "devcenter dev environment deploy"
] = """
    type: command
    short-summary: "Update an environment."
    examples:
      - name: Update using dev center
        text: |-
               az devcenter dev environment deploy --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--name "mydevenv" --user-id "00000000-0000-0000-0000-000000000000" --parameters "{\\"functionAppRuntime\\":\\"node\
\\",\\"storageAccountType\\":\\"Standard_LRS\\"}"
      - name: Update using endpoint
        text: |-
               az devcenter dev environment deploy --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--name "mydevenv" --user-id "00000000-0000-0000-0000-000000000000" --parameters "{\\"functionAppRuntime\\":\\"node\
\\",\\"storageAccountType\\":\\"Standard_LRS\\"}"
"""

helps[
    "devcenter dev environment delete"
] = """
    type: command
    short-summary: "Delete an environment and all its associated resources."
    examples:
      - name: Delete using dev center
        text: |-
              az devcenter dev environment delete --dev-center-name "ContosoDevCenter"  \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Delete using endpoint
        text: |-
              az devcenter dev environment delete --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev catalog"
] = """
    type: group
    short-summary: Manage catalogs.
"""

helps[
    "devcenter dev catalog list"
] = """
    type: command
    short-summary: "List all of the catalogs available for a project."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev catalog list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject"
      - name: List using endpoint
        text: |-
               az devcenter dev catalog list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject"
"""

helps[
    "devcenter dev catalog show"
] = """
    type: command
    short-summary: "Get the specified catalog within the project."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev catalog show --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --catalog-name "foo"
      - name: Get using endpoint
        text: |-
               az devcenter dev catalog show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --catalog-name "foo"
"""

helps[
    "devcenter dev environment-type"
] = """
    type: group
    short-summary: Manage environment types.
"""

helps[
    "devcenter dev environment-type list"
] = """
    type: command
    short-summary: "List all environment types configured for a project."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev environment-type list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject"
      - name: List using endpoint
        text: |-
               az devcenter dev environment-type list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject"
"""

helps[
    "devcenter dev environment-type show"
] = """
    type: command
    short-summary: "Get an environment type configured for a project."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev environment-type show --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --environment-type-name "foo"
      - name: Get using endpoint
        text: |-
               az devcenter dev environment-type show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --environment-type-name "foo"
"""

helps[
    "devcenter dev environment-type list-abilities"
] = """
    type: command
    short-summary: "List the signed-in user's permitted abilities in an environment type."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev environment-type list-abilities --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --environment-type-name "foo" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List using endpoint
        text: |-
               az devcenter dev environment-type list-abilities --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --environment-type-name "foo" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev image-build"
] = """
    type: group
    short-summary: Manage image builds.
"""

helps[
    "devcenter dev image-build show-log"
] = """
    type: command
    short-summary: "Get the log for an imaging build task."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev image-build show-log --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --image-build-log-id "f5dbdfab-fa0e-4831-8d13-25359aa5e680"
      - name: Get using endpoint
        text: |-
               az devcenter dev image-build show-log --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --image-build-log-id "f5dbdfab-fa0e-4831-8d13-25359aa5e680"
"""

helps[
    "devcenter dev environment-definition"
] = """
    type: group
    short-summary: Manage environment definitions.
"""

helps[
    "devcenter dev environment-definition list"
] = """
    type: command
    short-summary: "List all environment definitions available within a catalog or list all environment \
definitions available for a project."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev environment-definition list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject"
      - name: List using endpoint
        text: |-
               az devcenter dev environment-definition list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject"
      - name: List by catalog using dev center
        text: |-
               az devcenter dev environment-definition list --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --catalog-name "myCatalog"
      - name: List by catalog using endpoint
        text: |-
               az devcenter dev environment-definition list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --catalog-name "myCatalog"
"""

helps[
    "devcenter dev environment-definition show"
] = """
    type: command
    short-summary: "Get an environment definition from a catalog."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev environment-definition show --dev-center-name "ContosoDevCenter" \
--project-name "DevProject" --catalog-name "myCatalog" --definition-name "foo"
      - name: Get using endpoint
        text: |-
               az devcenter dev environment-definition show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--project-name "DevProject" --catalog-name "myCatalog" --definition-name "foo"
"""

helps[
    "devcenter dev environment list-operation"
] = """
    type: command
    short-summary: "Lists operations on the environment which have occurred within the past 90 days."
    examples:
      - name: List using dev center
        text: |-
              az devcenter dev environment list-operation --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List using endpoint
        text: |-
              az devcenter dev environment list-operation --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev environment show-operation"
] = """
    type: command
    short-summary: "Gets an environment action result."
    examples:
      - name: Get using dev center
        text: |-
              az devcenter dev environment show-operation --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --operation-id \
"f5dbdfab-fa0e-4831-8d13-25359aa5e680"
      - name: Get using endpoint
        text: |-
              az devcenter dev environment show-operation --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --operation-id "f5dbdfab-fa0e-4831-8d13-25359aa5e680"
"""

helps[
    "devcenter dev environment show-logs-by-operation"
] = """
    type: command
    short-summary: "Gets the logs for an operation on an environment."
    examples:
      - name: Get using dev center
        text: |-
              az devcenter dev environment show-logs-by-operation --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --operation-id \
"f5dbdfab-fa0e-4831-8d13-25359aa5e680"
      - name: Get using endpoint
        text: |-
              az devcenter dev environment show-logs-by-operation --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --operation-id "f5dbdfab-fa0e-4831-8d13-25359aa5e680"
"""

helps[
    "devcenter dev environment show-action"
] = """
    type: command
    short-summary: "Retrieve a specific environment action."
    examples:
      - name: Get using dev center
        text: |-
              az devcenter dev environment show-action --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --action-name \
"myEnv-Delete"
      - name: Get using endpoint
        text: |-
              az devcenter dev environment show-action --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --action-name "myEnv-Delete"
"""

helps[
    "devcenter dev environment list-action"
] = """
    type: command
    short-summary: "List specific environment actions."
    examples:
      - name: List using dev center
        text: |-
              az devcenter dev environment list-action --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: List using endpoint
        text: |-
              az devcenter dev environment list-action --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev environment delay-action"
] = """
    type: command
    short-summary: "Delay an environment action."
    examples:
      - name: Delay using dev center
        text: |-
              az devcenter dev environment delay-action --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --action-name \
"myEnv-Delete" --delay-time "04:30"
      - name: Delay using endpoint
        text: |-
              az devcenter dev environment delay-action --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --action-name "myEnv-Delete" --delay-time "04:30"
"""

helps[
    "devcenter dev environment skip-action"
] = """
    type: command
    short-summary: "Skip a specific environment action."
    examples:
      - name: Skip using dev center
        text: |-
              az devcenter dev environment skip-action --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --action-name \
"myEnv-Delete"
      - name: Skip using endpoint
        text: |-
              az devcenter dev environment skip-action --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --action-name "myEnv-Delete"
"""

helps[
    "devcenter dev environment show-outputs"
] = """
    type: command
    short-summary: "Gets outputs from the environment."
    examples:
      - name: Get using dev center
        text: |-
              az devcenter dev environment show-outputs --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Get using endpoint
        text: |-
              az devcenter dev environment show-outputs --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev environment update-expiration-date"
] = """
    type: command
    short-summary: "Update the environment expiration"
    examples:
      - name: Get using dev center
        text: |-
              az devcenter dev environment update-expiration-date --dev-center-name "ContosoDevCenter" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --expiration "2026-11-30T22:35:00+00:00"
      - name: Get using endpoint
        text: |-
              az devcenter dev environment update-expiration-date --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" \
--name "mydevenv" --project-name "DevProject" --user-id "00000000-0000-0000-0000-000000000000" --expiration "2026-11-30T22:35:00+00:00"

"""

helps[
    "devcenter dev customization-group"
] = """
    type: group
    short-summary: Manage customization groups.
"""

helps[
    "devcenter dev customization-group create"
] = """
    type: command
    short-summary: "Create a customization group."
    examples:
      - name: Create using dev center
        text: |-
               az devcenter dev customization-group create --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--dev-box-name "myDevBox" --tasks "[{\\"name\\": \\"catalogName/choco\\", \\"displayName\\": \\"Install VS Code\\", \\"parameters\\": {\\"packageName\\": \\"vscode\
\\", \\"packageVersion\\": \\"1.0.0\\"}}, {\\"name\\": \\"catalogName/write-to-file\\", \\"runAs\\": \\"User\\"}]" --name "Provisioning" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Create using endpoint
        text: |-
               az devcenter dev customization-group create --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--dev-box-name "myDevBox" --tasks "[{\\"name\\": \\"catalogName/choco\\", \\"displayName\\": \\"Install VS Code\\", \\"parameters\\": {\\"packageName\\": \\"vscode\
\\", \\"packageVersion\\": \\"1.0.0\\"}}, {\\"name\\": \\"catalogName/write-to-file\\", \\"runAs\\": \\"User\\"}]" --name "Provisioning" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev customization-group show"
] = """
    type: command
    short-summary: "Get a customization group."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev customization-group show --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--dev-box-name "myDevBox" --name "Provisioning" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Get using endpoint
        text: |-
               az devcenter dev customization-group show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--dev-box-name "myDevBox" --name "Provisioning" --user-id "00000000-0000-0000-0000-000000000000"
"""

helps[
    "devcenter dev customization-group list"
] = """
    type: command
    short-summary: "List customization groups on the dev box"
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev customization-group list --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--dev-box-name "myDevBox" --user-id "00000000-0000-0000-0000-000000000000" --include-tasks
      - name: List using endpoint
        text: |-
               az devcenter dev customization-group list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--dev-box-name "myDevBox" --user-id "00000000-0000-0000-0000-000000000000" --include-tasks
"""

helps[
    "devcenter dev customization-task"
] = """
    type: group
    short-summary: Manage customization tasks.
"""

helps[
    "devcenter dev customization-task show"
] = """
    type: command
    short-summary: "Get a customization task."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev customization-task show --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--task-name "choco" --catalog-name "myCatalog"
      - name: Get using endpoint
        text: |-
               az devcenter dev customization-task show --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--task-name "choco" --catalog-name "myCatalog"
"""

helps[
    "devcenter dev customization-task list"
] = """
    type: command
    short-summary: "List customization task."
    examples:
      - name: List using dev center
        text: |-
               az devcenter dev customization-task list --dev-center-name "ContosoDevCenter" --project-name "DevProject"
      - name: List using endpoint
        text: |-
               az devcenter dev customization-task list --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject"
"""

helps[
    "devcenter dev customization-task validate"
] = """
    type: command
    short-summary: "Validate customization tasks."
    examples:
      - name: Validate using dev center
        text: |-
               az devcenter dev customization-task validate --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--tasks "[{\\"name\\": \\"catalogName/choco\\", \\"displayName\\": \\"Install VS Code\\", \\"parameters\\": {\\"packageName\\": \\"vscode\
\\", \\"packageVersion\\": \\"1.0.0\\"}}, {\\"name\\": \\"catalogName/write-to-file\\", \\"runAs\\": \\"User\\"}]"
      - name: Validate using endpoint
        text: |-
               az devcenter dev customization-task validate --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--tasks "[{\\"name\\": \\"catalogName/choco\\", \\"displayName\\": \\"Install VS Code\\", \\"parameters\\": {\\"packageName\\": \\"vscode\
\\", \\"packageVersion\\": \\"1.0.0\\"}}, {\\"name\\": \\"catalogName/write-to-file\\", \\"runAs\\": \\"User\\"}]"
"""

helps[
    "devcenter dev customization-task show-logs"
] = """
    type: command
    short-summary: "Show logs of a customization task."
    examples:
      - name: Get using dev center
        text: |-
               az devcenter dev customization-task show-logs --dev-center-name "ContosoDevCenter" --project-name "DevProject" \
--dev-box-name "myDevBox" --customization-group-name "Provisioning" --customization-task-id "91835dc0-ef5a-4f58-9e3a-099aea8481f4" --user-id "00000000-0000-0000-0000-000000000000"
      - name: Get using endpoint
        text: |-
               az devcenter dev customization-task show-logs --endpoint "https://8a40af38-3b4c-4672-a6a4-5e964b1870ed-contosodevcenter.centralus.devcenter.azure.com/" --project-name "DevProject" \
--dev-box-name "myDevBox" --customization-group-name "Provisioning" --customization-task-id "91835dc0-ef5a-4f58-9e3a-099aea8481f4" --user-id "00000000-0000-0000-0000-000000000000"
"""
