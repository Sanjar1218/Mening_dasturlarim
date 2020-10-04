import requests
import json
def getUpdates():
    r=requests.get(f'https://api.telegram.org/bot1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU/getUpdates')
    data=r.json()
    chat_id=data['result'][-1]['message']['from']['id']
    text=data['result'][-1]['message']['text']
    update_id=data['result'][-1]['update_id']
    r=requests.get(f'https://ismlar.com/name/{text}')
    x=r.text
    s=x.find('<p>')
    s1=x.find('</p>')
    p=x[s+3:s1]
    return chat_id,text,update_id,x,p
def sendMessage(chat_id,text):
    re=requests.get(f'https://api.telegram.org/bot1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU/sendMessage?chat_id={chat_id}&text={text}')
    print(re)
last_update_id=-1
while True:
    chat_id,text,update_id,x,p=getUpdates()
    a=p.find(' oʻzbek ismlarining toʻliq')
    if a==-1:
        if last_update_id!=update_id:
            print(p)
            print(text)
            sendMessage(chat_id,p)
            last_update_id=update_id
    else:
        if last_update_id!=update_id:
            p="I can't find that kind of name.Sorry!"
            sendMessage(chat_id,p)
            last_update_id=update_id
