import requests
import json
import io
url='https://uytrfgh.atlassian.net/rest/api/3/issue/REET-1/comment/10005'
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
            "text": "comment1 updated by python",
            "type": "text"
          }
        ]
      }
    ]
  }
})

response=requests.put(url,headers=header,data=data,auth=("ranisingh21@navgurukul.org","JN96uGIGMcUSkoIbMYyvC26E"))
print(response.text)
