import requests
import json
import io
url='https://uytrfgh.atlassian.net/rest/api/3/search'
header={
      "Accept": "application/json",
   "Content-Type": "application/json"
}
query={
    'jql':"project=REET"
}
response=requests.get(url,headers=header,params=query,auth=("ranisingh21@navgurukul.org","Z6Wb0ny3miznaLMLe2xK4488"))
data=response.json()
issues=data["issues"]
for issue in issues:
    print(issue["key"])