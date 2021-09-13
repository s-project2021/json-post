import requests
import json
from datetime import date,datetime
from pytz import timezone

url = "http://127.0.0.1:8000/ai/"

now_time = datetime.now()
timez = timezone('Asia/Tokyo')
then_time = timez.localize(now_time)

data = {"place_id":"1","then_time":then_time,"crowd":"4"}

def json_serial(obj):

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError (f'Type {obj} not serializable')

r = requests.post(url,headers = {'Content-Type':'application/json',},data =json.dumps(data,default=json_serial))
