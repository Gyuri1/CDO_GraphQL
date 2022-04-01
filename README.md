# CDO_GraphQL


This python script shows the device info in Cisco Defense Orchestrator (CDO).

Example:

``python3 graphql_cdo_query.py
Devices in CDO: https://edge.us.cdo.cisco.com/api/public
{
  "data": {
    "devices": {
      "metadata": {
        "count": 1
      },
      "items": [
        {
          "softwareVersion": null,
          "name": "asa",
          "uid": "3056c5ff-1551-4aeb-a7c5-87cb142fdbca",
          "isModel": true,
          "conflictDetectionState": "IN_SYNC",
          "ipv4": null,
          "deviceType": "ASA",
          "serial": null,
          "configurationStatus": "SYNCED",
          "interfaces": null,
          "connectivityState": "UNKNOWN",
          "highAvailability": null,
          "specificDevice": {
            "namespace": "asa",
            "uid": "d4c529a6-f52b-45f5-9a78-c01c35675c74",
            "type": "configs",
            "vpnId": null
          }
        }
      ]
    }
  }
}
`` 
