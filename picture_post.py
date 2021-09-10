import cv2
from datetime import datetime
import os
import time
import base64
import requests
import json

#撮影処理
def picGet(c_num):
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    dir_path = './' + date + '/'
    os.makedirs(dir_path)

    cap = cv2.VideoCapture(0)
    count = 0
    time.sleep(0.3)


    #撮影ループ
    while True:
        if count >= c_num:
            break

        ret, frame = cap.read()
        path = dir_path + str(count) + ".png"
        cv2.imwrite(path, frame)
        url = 'http://127.0.0.1:8000/photo/in/'

        f = open(path, 'rb')
        # base64编码
        base64_data = base64.b64encode(f.read())
        f.close()
        base64_data = base64_data.decode()
        # 传输的数据格式
        data = {'img': base64_data}

        r = requests.post(url, headers={'Content-Type': 'application/json', }, data=json.dumps(data))
        print(r.text)
        time.sleep(0.2)
        count += 1

    #開放
    cap.release()
    cv2.destroyAllWindows()

picGet(10)
