import requests
import json
import io
url='https://uytrfgh.atlassian.net//rest/api/2/issue'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
with io.open("issue.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
    data=data.split("\n")
for rows in data:
 payload=json.dumps({
    "fields": {
       "project":
       {
          "key": rows.split(",")[0]
       },
       "summary": rows.split(",")[1],
       "description": rows.split(",")[2],
       "issuetype": {
          "name": "Task"
       }
   }
}
)
 response=requests.post(url,headers=header,data=payload,auth=("ranisingh21@navgurukul.org","Z6Wb0ny3miznaLMLe2xK4488"))
 print(response.text)