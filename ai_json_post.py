import requests
import json
from datetime import date,datetime

url = "http://127.0.0.1:8000/ai/"


data = {"place_id":"1","then_time":datetime.now(),"crowd":"4"}

def json_serial(obj):

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError (f'Type {obj} not serializable')

r = requests.post(url,headers = {'Content-Type':'application/json',},data =json.dumps(data,default=json_serial))
