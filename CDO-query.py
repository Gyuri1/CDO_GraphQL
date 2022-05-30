import requests
"""This is for US Cloud: """
url = "https://edge.us.cdo.cisco.com/api/public"
json = {'query': '''{
  objects(
    limit: 100
    objectType: [NETWORK_GROUP, NETWORK_OBJECT]
    offset: 0
    sortOrder: DESC
    sortField: OBJECT_TYPE
  ) {
    metadata {
      count
    }
    items {
      name
      uid
      objectType
      description
      details {
        ... on NetworkDetailsBase {
          wildcardMask
        }
        ... on NetworkDetailsIpEq {
          value
        }
        ... on NetworkDetailsIpRange {
          start
          end
        }

        ... on NetworkGroupDetails {
          items {
            ... on ObjectReferenceDetails {
              uid
              name
              type
            }
            ... on NetworkDetailsIpEq {
              value
            }
          }
        }
      }
    }
  }
}
'''}

"""TOKEN can be generated on this page in advance: 
    https://www.defenseorchestrator.com/settings
"""
header= {"Authorization": "Bearer TOKEN"}

r = requests.post(url, json=json, headers=header)
print(r.json())
