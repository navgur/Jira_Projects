import requests
import json
url="https://uytrfgh.atlassian.net/rest/api/3/users/search"
headers={
     "Accept": "application/json",
   "Content-Type": "application/json"
}
response=requests.get(url,headers=headers,auth=("ranisingh21@navgurukul.org","8YEegSmHZAcbfT8lLEo95BEF"))
data=response.json()
print(len(data))
for users in data:
    print(users["displayName"])