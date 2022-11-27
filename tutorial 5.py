import requests
import json
import io
url='https://uytrfgh.atlassian.net/rest/api/3/issue/REET-1/comment'
header={
      "Accept": "application/json",
   "Content-Type": "application/json"
}

response=requests.get(url,headers=header,auth=("ranisingh21@navgurukul.org","Z6Wb0ny3miznaLMLe2xK4488"))
data=response.json()
print(data["total"])
with io.open("comments.csv","w",encoding="utf-8")as f1:
    f1.write("comment id"+","+"comment text"+"\n")
    for comments in data["comments"]:
     f1.write(comments["id"]+", "+comments["body"]["content"][0]["content"][0]["text"])
    f1.close()   