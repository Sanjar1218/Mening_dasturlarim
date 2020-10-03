import requests
import json
def getUpdates():
    r=requests.get(f'https://api.telegram.org/bot1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU/getUpdates')
    data=r.json()
    chat_id=data['result'][-1]['message']['from']['id']
    text=data['result'][-1]['message']['text']
    update_id=data['result'][-1]['update_id']
    r=requests.get(f'https://ismlar.com/search/{text}')
    x=r.text[13200:13400]
    print(x)
    return chat_id,text,update_id,x
def sendMessage(chat_id,text):
    re=requests.get(f'https://api.telegram.org/bot1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU/sendMessage?chat_id={chat_id}&text={text}')
    print(re)
last_update_id=-1
while True:
    chat_id,text,update_id,x=getUpdates()
    print(text)
    if last_update_id!=update_id:
        sendMessage(chat_id,x)
        last_update_id=update_id
