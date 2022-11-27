import requests
import json
import io
url='https://uytrfgh.atlassian.net/rest/api/3/issue/REET-35/assignee'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
with io.open("issue_user.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
data=data.split("\n")
row=0
while row<len(data)-2:
    issue_id=data[row].split(",")[0]
    user_id=data[row].split(",")[1]
    row=row+1
    url='https://uytrfgh.atlassian.net/rest/api/3/issue/'+issue_id+'/assignee'
    payload=json.dumps({
    "accountId": user_id
    }
    )
    response=requests.put(url,headers=header,data=payload,auth=("ranisingh21@navgurukul.org","OpE9DfPiwLRoW63kotU740A3"))
    print(response.text)
