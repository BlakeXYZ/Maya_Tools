
import json
import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth

from auth import BK_EMAIL, AUTH_TOKEN

URL_PROJECTS = "https://artificialblakek.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth(BK_EMAIL, AUTH_TOKEN)

headers = {
    "Accept": "application/json",
}

query = {
  'query': '{query}'
}

response = requests.get(
    URL_PROJECTS,
    headers=headers,
    params=query,
    auth=auth
)

projects_data = json.loads(response.text)

# Get all project issues,by using the 
# json loads method. json dumps will format response. (equivalent of viewing json in firefox using URL)
# json_dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

# print(json_dump)

# for project in projects_data:
#     print(project["name"])
#     print(project["key"])
#     print(project["id"])
#     print("----")
 

 ########
 ########
 ########

URL_SEARCH = "https://artificialblakek.atlassian.net/rest/api/3/search"

# How to get ALL ISSUES from selected PROJECT

headers = {
"Accept": "application/json",
}

project_01 = projects_data[0]["key"]

# QUERY in browser equivalent: rest/api/3/search/?jql=project=TP01
query = {
'query': f'project={project_01}'
}

response = requests.get(
    URL_SEARCH,
    headers=headers,
    params=query,
    auth=auth
)

search_data = json.loads(response.text)

for issue in search_data["issues"]:
    
    print(issue["fields"]["summary"])

    if issue["fields"]["assignee"]:
        print(f'Assigned to: {issue["fields"]["assignee"]["displayName"]}')
    else:
        print("MISSING ASSIGNEE")

    print("----")

