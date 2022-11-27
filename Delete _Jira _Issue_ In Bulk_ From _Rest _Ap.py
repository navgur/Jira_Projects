
import requests
import json
import io
headers={
     "Accept": "application/json",
   "Content-Type":"application/json"
}
with io.open("issue_delete.csv","r",encoding="utf-8")as f1:
    data=f1.read()
data=data.split()  
for id in data:
    url="https://uytrfgh.atlassian.net/rest/api/3/issue/"+id
    response=requests.delete(url,headers=headers,auth=("ranisingh21@navgurukul.org","RgScuWcqedhuqkFeXz0i947D"))
