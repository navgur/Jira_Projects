import requests
import json
url="https://uytrfgh.atlassian.net/rest/api/3/users/search"
headers={
     "Accept": "application/json",
   "Content-Type": "application/json"
}
response=requests.get(url,headers=headers,auth=("ranisingh21@navgurukul.org","gXnj0OXTjZ3XDcIOpHSM68BD"))
data=response.json()
print(len(data))
for users in data:
    print(users["displayName"])
