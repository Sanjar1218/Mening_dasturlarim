import requests
import json
a=11
while a<20:
    METHOD_NAME='getUpdates'
    token="1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU"
    r=requests.get(f'https://api.telegram.org/bot{token}/{METHOD_NAME}')
    data=r.json()
    i=data['result'][0]['message']['from']['id']

    try:
        mes=data['result'][a]['message']['text']
        if mes=='hello':
            txt='hi'
            re=requests.get(f'https://api.telegram.org/bot1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU/sendMessage?chat_id={i}&text={txt}')
            
            print(re)
        elif mes=='how are you':
            txt='i\'m fine what about you'
            re=requests.get(f'https://api.telegram.org/bot1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU/sendMessage?chat_id={i}&text={txt}')
        elif mes=='good':
            txt='can i help you'
            re=requests.get(f'https://api.telegram.org/bot1364927812:AAE0e-V-sJpspbrqkJdqa-Ye_L-Io_iYrmU/sendMessage?chat_id={i}&text={txt}')
        a+=1
    except:
        print('kutayapman')
        continue

    
