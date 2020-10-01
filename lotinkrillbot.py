import requests
import json
from pprint import pprint
def getUpdates():
    lst1=[]
    r=requests.get(f'https://api.telegram.org/bot1395602363:AAHFmnjEMWTF9BJajHu2Pm8rdRSKgGM4dCo/getUpdates')
    data=r.json()
    for i in data['result']:
        dct={}
        chat_id=i['message']['from']['id']
        dct['chat_id']=chat_id
        text=i['message']['text']
        dct['text']=text
        username=i['message']['chat']['username']
        lst1.append(dct)
        #print(text)
    return lst1
def sendMessage(chat_id,text):
    lst=[]
    for i in text:
        lst.append(i)
    for i in range(len(lst)):
        if lst[i]=='A':
            lst[i]='А'
        elif lst[i]=='Y' and lst[i+1]=='a':
            lst[i]='Я'
            lst[i+1]=''
        elif lst[i]=='y' and lst[i+1]=='a':
            lst[i]='я'
            lst[i+1]=''
        elif lst[i]=='Y' and lst[i+1]=='e':
            lst[i]='Е'
            lst[i+1]=''
        elif lst[i]=='y' and lst[i+1]=='e':
            lst[i]='е'
            lst[i+1]=''
        elif lst[i]=='Y' and lst[i+1]=='o':
            lst[i]='Ё'
            lst[i+1]=''
        elif lst[i]=='y' and lst[i+1]=='o':
            lst[i]='ё'
            lst[i+1]=''
        elif lst[i]=='Y' and lst[i+1]=='u':
            lst[i]='Ю'
            lst[i+1]=''
        elif lst[i]=='y' and lst[i+1]=='u':
            lst[i]='ю'
            lst[i+1]=''
        elif lst[i]=="O" and lst[i+1]=="'":
            lst[i]='Ў'
            lst[i+1]=''
        elif lst[i]=="o" and lst[i+1]=="'":
            lst[i]='ў'
            lst[i+1]=''
        elif lst[i]=='C' and lst[i+1]=='h':
            lst[i]='Ч'
            lst[i+1]=''
        elif lst[i]=='c' and lst[i+1]=='h':
            lst[i]='ч'
            lst[i+1]=''
        elif lst[i]=='S' and lst[i+1]=='h':
            lst[i]='Ш'
            lst[i+1]=''
        elif lst[i]=='s' and lst[i+1]=='h':
            lst[i]='ш'
            lst[i+1]=''
        elif lst[i]=='G' and lst[i+1]=="'":
            lst[i]='Ғ'
            lst[i+1]=''
        elif lst[i]=='g' and lst[i+1]=="'":
            lst[i]='ғ'
            lst[i+1]=''
        elif lst[i]=='a':
            lst[i]='а'
        elif lst[i]=='B':
            lst[i]='Б'
        elif lst[i]=='b':
            lst[i]='б'
        elif lst[i]=='V':
            lst[i]='В'
        elif lst[i]=='v':
            lst[i]='в'
        elif lst[i]=='G':
            lst[i]='Г'
        elif lst[i]=='g':
            lst[i]='г'
        elif lst[i]=='D':
            lst[i]='Д'
        elif lst[i]=='d':
            lst[i]='д'
        elif lst[i]=='J':
            lst[i]='Ж'
        elif lst[i]=='j':
            lst[i]='ж'
        elif lst[i]=='Z':
            lst[i]='З'
        elif lst[i]=='z':
            lst[i]='з'
        elif lst[i]=='I':
            lst[i]='И'
        elif lst[i]=='i':
            lst[i]='и'
        elif lst[i]=='Y':
            lst[i]='Й'
        elif lst[i]=='y':
            lst[i]='й'
        elif lst[i]=='K':
            lst[i]='К'
        elif lst[i]=='k':
            lst[i]='к'
        elif lst[i]=='L':
            lst[i]='Л'
        elif lst[i]=='l':
            lst[i]='л'
        elif lst[i]=='M':
            lst[i]='М'
        elif lst[i]=='m':
            lst[i]='м'
        elif lst[i]=='N':
            lst[i]='Н'
        elif lst[i]=='n':
            lst[i]='н'
        elif lst[i]=='O':
            lst[i]='О'
        elif lst[i]=='o':
            lst[i]='о'
        elif lst[i]=='P':
            lst[i]='П'
        elif lst[i]=='p':
            lst[i]='п'
        elif lst[i]=='R':
            lst[i]='Р'
        elif lst[i]=='r':
            lst[i]='р'
        elif lst[i]=='S':
            lst[i]='С'
        elif lst[i]=='s':
            lst[i]='с'
        elif lst[i]=='T':
            lst[i]='Т'
        elif lst[i]=='t':
            lst[i]='т'
        elif lst[i]=='U':
            lst[i]='У'
        elif lst[i]=='u':
            lst[i]='у'
        elif lst[i]=='F':
            lst[i]='Ф'
        elif lst[i]=='f':
            lst[i]='ф'
        elif lst[i]=='X':
            lst[i]='Х'
        elif lst[i]=='x':
            lst[i]='х'
        elif lst[i]=="'":
            lst[i]='ъ'
        elif lst[i]=='E' and lst[i-1]!=' ':
            lst[i]='Е'
        elif lst[i]=='e' and lst[i-1]!=' ':
            lst[i]='е'
        elif lst[i]=='E' or lst[0]=='E' and lst[i-1]==' ':
            lst[i]='Э'
        elif lst[i]=='e' or lst[0]=='e' and lst[i-1]==' ':
            lst[i]='э'
        elif lst[i]=='Q':
            lst[i]='Қ'
        elif lst[i]=='q':
            lst[i]='қ'
        elif lst[i]=='H':
            lst[i]='Ҳ'
        elif lst[i]=='h':
            lst[i]='ҳ'
        elif lst[i]=="'":
            lst[i]=''
        else:
            continue
    x=''.join(lst)
    text=x
    re=requests.get(f'https://api.telegram.org/bot1395602363:AAHFmnjEMWTF9BJajHu2Pm8rdRSKgGM4dCo/sendMessage?chat_id={chat_id}&text={text}')
    mes=re.json()
    print(mes)
a=9
while a<30:
    try:
        lst1=getUpdates()
        pprint(lst1[a])
        d=lst1[a]
        chat_id=d['chat_id']
        text=d['text']
        sendMessage(chat_id,text)
        a+=1
    
    except:
        #print('ishlamadi')
        continue


    
    
    
