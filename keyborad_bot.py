import requests
import json
def getUpdates(token):
    r=requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    data=r.json()
    chat_id=data['result'][-1]['message']['from']['id']
    txt=data['result'][-1]['message']['text']
    update_id=data['result'][-1]['update_id']
    return chat_id,txt,update_id
def sendMessage(chat_id,txt,token):
    s={'text':'7'}
    e={'text':'8'}
    n={'text':'9'}
    m={'text':'*'}
    f={'text':'4'}
    fi={'text':'5'}
    si={'text':'6'}
    d={'text':'/'}
    o={'text':'1'}
    t={'text':'2'}
    th={'text':'3'}
    mi={'text':'-'}
    z={'text':'0'}
    p={'text':'.'}
    eq={'text':'='}
    pl={'text':'+'}
    keyboard=[
            [s,e,n,m],
            [f,fi,si,d],
            [o,t,th,mi],
            [z,p,eq,pl]
    ]

    replyKeyboardMarkup={
            'keyboard':keyboard
    }

    parameter={
            'chat_id':chat_id,
            'text':txt,
            'reply_markup':replyKeyboardMarkup,
    }
    
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    re=requests.get(url=url, json=parameter)
token='1345758482:AAGWIdwbWrKaNQH5UcRUzBCrFyKvxsCivyA'
last_update_id=-1
while True:
    chat_id,txt,update_id=getUpdates(token)
    if last_update_id!=update_id:
        sendMessage(chat_id,txt,token)
        last_update_id=update_id
    
