
import requests
import json
url='https://uytrfgh.atlassian.net//rest/api/2/issue'
headers={
     "Accept": "application/json",
   "Content-Type": "application/json"
}
payroal=json.dumps({
    "fields": {
       "project":
       {
          "key": "REET"
       },
       "summary": "REST ye merry gentlemen.",
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "name": "Task"
       }
   }
}

)
response=requests.post(url,headers=headers,data=payroal,auth=("ranisingh21@navgurukul.org","BOPd8E2hvtMv5VS6wPuc1CC3"))
print(response.text)
