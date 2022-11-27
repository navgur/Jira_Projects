import requests
import json
url='https://uytrfgh.atlassian.net/rest/api/3/issue/REET-40/transitions'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload=json.dumps(
   {
    
    "transition": {
        "id": "11"
    }
}
        
)
response=requests.post(url,headers=header,data=payload,auth=("ranisingh21@navgurukul.org","Df1RZ1YEcETMt1F3wzne1F1C"))
print(response.text)