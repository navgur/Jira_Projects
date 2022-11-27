import requests
import json
import io
url='https://uytrfgh.atlassian.net/rest/api/2/user'
headers={
     "Accept": "application/json",
   "Content-Type": "application/json"
}
with io.open("userlist.csv","r",encoding="utf-8") as f1:

    user_data=f1.read()
    f1.close()
user_data=user_data.split("\n")[1:]
i=0
while i<len(user_data):
    displayName=user_data[i].split(",")[0]
    emailAddress=user_data[i].split(",")[2]
    i=i+1
    payroal=json.dumps({
        "emailAddress": emailAddress,
        "displayName":displayName
    })
    response=requests.post(url,headers=headers,data=payroal,auth=("ranisingh21@navgurukul.org","Z6Wb0ny3miznaLMLe2xK4488"))
    print(response.text)
