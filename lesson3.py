import requests
import json
while True:
    METHOD_NAME='getUpdates'
    token="1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU"
    r=requests.get(f'https://api.telegram.org/bot{token}/{METHOD_NAME}')
    data=r.json()
    i=data['result'][-1]['message']['from']['id']
    txt='hi'
    re=requests.get(f'https://api.telegram.org/bot1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU/sendMessage?chat_id={i}&text={txt}')
    
