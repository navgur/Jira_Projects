import requests
import json
import io
url="https://uytrfgh.atlassian.net/rest/api/3/issue/REET-15/assignee"
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload=json.dumps(
    {
        "accountId": "6380d3879960988ef6be614f"
}
)

response=requests.put(url,headers=header,data=payload,auth=("ranisingh21@navgurukul.org","Z6Wb0ny3miznaLMLe2xK4488"))
print(response.text)