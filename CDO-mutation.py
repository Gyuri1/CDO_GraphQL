import requests
"""This is for US Cloud: """
url = "https://edge.us.cdo.cisco.com/api/public"
json = {'query': '''mutation{
    updateNetworkObject(
      baseInput: { uid: "<YOUR OBJECT'S UUID>" }
      ipAddressRangeInput: { start: "1.1.1.1", end: "4.4.4.8" }
    ) {
      name
      uid
      objectType
      description
      }
}'''}

"""TOKEN can be generated on this page in advance: 
    https://www.defenseorchestrator.com/settings
"""
header= {"Authorization": "Bearer TOKEN"}

r = requests.post(url, json=json, headers=header)
print(r, r.text)
