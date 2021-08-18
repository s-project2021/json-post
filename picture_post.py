import base64
import requests
import json

url = 'http://127.0.0.1:8000/photo/in/'

f = open('1.png', 'rb')
#base64
base64_data = base64.b64encode(f.read())
f.close()
base64_data = base64_data.decode()

data = {'img':base64_data}

r = requests.post(url,headers = {'Content-Type':'application/json',},data =json.dumps(data))
print(r.text)
