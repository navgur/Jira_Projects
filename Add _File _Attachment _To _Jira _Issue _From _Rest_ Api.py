import requests
import json
import io
url='https://uytrfgh.atlassian.net/rest/api/3/issue/REET-1/attachments'
header={
      "X-Atlassian-Token": "no-check"
}
files={"file":("userlist.csv",open("userlist.csv","rb"))}

response=requests.post(url,headers=header,files=files,auth=("ranisingh21@navgurukul.org","eKYVle7eNixWcJBGZJeZE525"))
print(response.text)
