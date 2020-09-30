import requests
import json
def getUpdates(a):
    r=requests.get(f'https://api.telegram.org/bot1159902341:AAG37H4f31qdH5OB2-2LEMNMrTAJDo2OeQ4/getUpdates')
    data=r.json()
    chat_id=data['result'][a]['message']['from']['id']
    text=data['result'][a]['message']['text']
    return chat_id,text
def sendMessage(chat_id,text):
    re=requests.get(f'https://api.telegram.org/bot1159902341:AAG37H4f31qdH5OB2-2LEMNMrTAJDo2OeQ4/sendMessage?chat_id={chat_id}&text={text}')
    print(re)
a=0
while a<20:
    try:
        chat_id,text=getUpdates(a)
        sendMessage(chat_id,text)
        a+=1
    except:
        print('waiting')
        continue
