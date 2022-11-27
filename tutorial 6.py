import requests
import json
import io
url='https://uytrfgh.atlassian.net/rest/api/3/issue/REET-1/comment'
header={
      "Accept": "application/json",
   "Content-Type": "application/json"
}

data=json.dumps({"body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "text": "comment-1 added by python",
            "type": "text"
          }
        ]
      }
    ]
  }
})

response=requests.post(url,headers=header,data=data,auth=("ranisingh21@navgurukul.org","Z6Wb0ny3miznaLMLe2xK4488"))
print(response.text)
