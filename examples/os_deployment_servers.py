# -*- coding: utf-8 -*-
###
# (C) Copyright [2019] Hewlett Packard Enterprise Development LP
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

from examples.CONFIG_loader import try_load_from_file
from hpeOneView.oneview_client import OneViewClient

CONFIG = {
    "ip": "",
    "credentials": {
        "userName": "",
        "password": ""
    }
}

# Try load CONFIG from a file (if there is a CONFIG file)
CONFIG = try_load_from_file(CONFIG)

oneview_client = OneViewClient(CONFIG)

# To run this example you must set valid URI of the network RESOURCE and of the image streamer
# appliance
MANAGEMENT_NETWORK_URI = ""
APPLIANCE_URI = ""

print("Add an Os Deployment Server:")
RESOURCE = {
    "description": "OS Deployment Server",
    "name": "I3s-Deployment Server",
    "mgmtNetworkUri": MANAGEMENT_NETWORK_URI,
    "applianceUri": APPLIANCE_URI,
}
os_deployment_server_added = oneview_client.os_deployment_servers.add(RESOURCE)
pprint(os_deployment_server_added)

print("Get all Os Deployment Servers:")
os_deployment_servers_all = oneview_client.os_deployment_servers.get_all(start=0, count=-1,
	 filter='state=Connected')
pprint(os_deployment_servers_all)

OS_DEPLOYMENT_SERVER_URI = os_deployment_server_added['uri']

print("Get an Os Deployment Server by URI:")
os_deployment_server = oneview_client.os_deployment_servers.get(OS_DEPLOYMENT_SERVER_URI)
pprint(os_deployment_server)

print("Get Os Deployment Servers by Filter:")
os_deployment_servers = oneview_client.os_deployment_servers.get_by('state', 'Connected')
pprint(os_deployment_servers)

print("Get the Os Deployment Server by Name:")
os_deployment_servers = oneview_client.os_deployment_servers.get_by_name("OS Deployment Server")
pprint(os_deployment_servers)

print("Get all Deployment Servers Networks:")
networks = oneview_client.os_deployment_servers.get_networks()
pprint(networks)

print("List all the Image Streamer RESOURCEs associated with deployment-server:")
appliances = oneview_client.os_deployment_servers.get_appliances()
pprint(appliances)

print("List the particular Image Streamer RESOURCE with an given URI:")
appliance = oneview_client.os_deployment_servers.get_appliance(appliances[0]['uri'], 'name')
pprint(appliance)

print("Update the Deployment Server description:")
os_deployment_server_added['description'] = "Description Updated"
os_deployment_server_updated = oneview_client.os_deployment_servers.update(os_deployment_server_added)
pprint(os_deployment_server_updated)

print("Delete the added Deployment Server:")
oneview_client.os_deployment_servers.delete(os_deployment_server_updated)
print("Done")
