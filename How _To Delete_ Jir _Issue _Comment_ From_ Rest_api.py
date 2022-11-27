import requests
import json
import io
url='https://uytrfgh.atlassian.net/rest/api/3/issue/REET-1/comment/10011'
header={
      "Accept": "application/json",
   "Content-Type": "application/json"
}

response=requests.delete(url,headers=header,auth=("ranisingh21@navgurukul.org","PYgbij5PWwWb4lNhpy67D689"))
data=response.text
print(data)
