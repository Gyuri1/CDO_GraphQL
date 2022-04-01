import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Token from here:
# https://www.defenseorchestrator.com/settings
cdo_id="xyz"

# US CDO URL!
url= "https://edge.us.cdo.cisco.com/api/public"
headers = {'Authorization': 'Bearer {}'.format(cdo_id)}

query="""{
  devices(limit: 50, sortField: NAME, deviceType: [FIREPOWER, ASA, FTD]) {
    metadata {
      count
    }
    items {
      softwareVersion
      name
      uid
      isModel
      conflictDetectionState
      ipv4
      deviceType
      serial
      configurationStatus
      interfaces
      connectivityState
      highAvailability
      specificDevice {
        namespace
        ... on FtdSpecificDevice {
          uid
        }
        ... on AsaSpecificDevice {
          uid
          type
          vpnId
        }
        ... on MerakiSpecificDevice {
          uid
          type
        }
        ... on AwsSpecificDevice {
          vpcId
          region
        }
      }
    }
  }
}
"""


print(f"Devices in CDO: {url}")
response = requests.post(url, headers=headers, json={'query': query})
response.raise_for_status()
print(json.dumps(response.json(), indent=2))    

