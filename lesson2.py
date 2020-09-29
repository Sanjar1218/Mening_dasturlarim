import requests
import json
METHOD_NAME='getUpdates'
token="1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU"
r=requests.get(f'https://api.telegram.org/bot{token}/{METHOD_NAME}')
data=r.json()
update_id=data['result'][0]['update_id']
message=data['result'][0]['message']
chat=data['result'][0]['message']['chat']
frm=data['result'][0]['message']['from']
print(frm,update_id,massage,frm)
