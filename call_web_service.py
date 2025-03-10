import requests
import json

url = 'http://127.0.0.1:5000/simpleAPI'

# url = 'http://52.187.149.111:5006/simpleAPI'
# url = 'http://20.205.16.95:5006/simpleAPI'
# url = 'http://20.196.127.192:5006/simpleAPI'
myobj = {'message_key': 'message_val',
         'msg':'puttipong'} #json

x = requests.post(url, data = json.dumps(myobj)) #requests ใช้เรียก // data // รับ output จาก webb
     