# -*- coding: utf-8 -*-
###
# (C) Copyright [2021] Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###

from pprint import pprint
from hpeOneView.oneview_client import OneViewClient
from CONFIG_loader import try_load_from_file

CONFIG = {
    "ip": "<oneview_ip>",
    "credentials": {
        "userName": "<username>",
        "password": "<password>"
    }
}

OPTIONS = {
    "destination": "1.1.1.2",
    "communityString": "testOne",
    "port": 162
}

DESTINATION_IP = '2.2.2.2'

# Try load CONFIG from a file (if there is a CONFIG file)
CONFIG = try_load_from_file(CONFIG)
oneview_client = OneViewClient(CONFIG)
appliance_device_SNMP_V1_TRAP_destinations = oneview_client.appliance_device_SNMP_V1_TRAP_destinations

# Lists the appliance device SNMP v1 Trap Destination
print("\n Get list of appliance SNMP v1 trap destination")
SNMP_V1_TRAP_ALL = appliance_device_SNMP_V1_TRAP_destinations.get_all()
for snmp_trap in SNMP_V1_TRAP_ALL:
    print('  - {}: {}'.format(snmp_trap['destination'], snmp_trap['uri']))

# Add appliance device SNMP v1 Trap Destination
SNMP_V1_TRAP = appliance_device_SNMP_V1_TRAP_destinations.create(OPTIONS)
print("\n Created appliance SNMP v1 trap destination successfully!")
pprint(SNMP_V1_TRAP.DATA)

# Get by name
print("\n## Find an SNMPv1 trap destination by name")
SNMP_V1_TRAP = appliance_device_SNMP_V1_TRAP_destinations.get_by_name(SNMP_V1_TRAP.DATA['destination'])
pprint(SNMP_V1_TRAP.DATA)

# Add appliance device SNMP v1 Trap Destination with ID
TRAP_ID = 9
OPTIONS['destination'] = DESTINATION_IP
SNMP_V1_TRAP_ID = appliance_device_SNMP_V1_TRAP_destinations.create(OPTIONS, TRAP_ID)
print("\n Created appliance SNMP v1 trap destination by id successfully!")
pprint(SNMP_V1_TRAP_ID.DATA)

# Get the appliance device SNMP v1 Trap Destination by id
print("\n Get appliance SNMP v1 trap destination by id")
SNMP_V1_TRAP_BY_ID = appliance_device_SNMP_V1_TRAP_destinations.get_by_id(1)
pprint(SNMP_V1_TRAP_BY_ID.DATA)

# Lists the appliance device SNMP v1 Trap Destination by destination (unique)
print("\n## Get appliance SNMP v1 trap by destination..")
SNMP_V1_TRAPS = appliance_device_SNMP_V1_TRAP_destinations.get_by('destination',
	 OPTIONS['destination'])
for snmp_trap in SNMP_V1_TRAPS:
    print(' - {} : {}'.format(snmp_trap['destination'], snmp_trap['communityString']))

# Get by URI
print("\n Find an SNMP v1 trap destination by URI")
SNMP_V1_TRAP = appliance_device_SNMP_V1_TRAP_destinations.get_by_uri(SNMP_V1_TRAP.DATA['uri'])
pprint(SNMP_V1_TRAP.DATA)

# Change appliance device SNMP v1 Trap Destination - Only Community String and Port can be changed
DATA = {'communityString': 'testTwo'}
SNMP_V1_TRAP = SNMP_V1_TRAP.update(DATA)
print("\n## Update appliance SNMP v1 trap destination successfully!")
pprint(SNMP_V1_TRAP.DATA)

# Delete Created Entry
SNMP_V1_TRAP.delete()
SNMP_V1_TRAP_ID.delete()
print("\n## Delete appliance SNMP v1 trap destination successfully!")
