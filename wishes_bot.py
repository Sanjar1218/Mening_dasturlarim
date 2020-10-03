import requests
import json
from pprint import pprint 
def getUpdates():
    r=requests.get(f'https://api.telegram.org/bot1148663975:AAEACks3oCJAuMDToqKM6HUnXTsOOgrMRTw/getUpdates')
    data=r.json()
    username=data['result'][-1]['message']['chat']['username']
    chat_id=data['result'][-1]['message']['chat']['id']
    text=data['result'][-1]['message']['text']
    update_id=data['result'][-1]['update_id']
     #pprint(data['result'])
    return chat_id,text,update_id,username
def wishes():
    t={
    'mother':{
        1:"Today is a special day for you, I went to buy a gift for you but I didn’t know what to choose for the most loving and wonderful gift ever given to me by God. You are a valuable person, Happy birthday to you mom",
        2:"Lots of love from me as you celebrate your birthday. All the best",
        3:"Without you, in my world, I would have smiled less, hoped less, and even loved less. It is your positive influence that has taught me to be a better person. As you celebrate your birthday I take the opportunity to wish the best, happy birthday mum",
        4:" They say “the good gifts in life are the best”, every time I spend time with you I see the reality of this saying. No value can be attached to the love you have shown me. Cheers to many more birthdays together",
        5:" Your love is so broad to accept me even when I go far away, so deep it cuts through my heart. I celebrate this wonderful day.",
        5:"Mom, you are the most adorable mother in the world. As you celebrate your birthday, I want to wish you the best that life has to offer. I will at all times love you, happy birthday to you",
        6:"A darling mom you are to me, to me you are my mentor, role model, superhero, and many things that words cannot describe. I wish you’re a very delightful birthday and may God bless you",
        7:"Dear mum, as you celebrate your birthday today my prayers is that you may live many more years. Have many years ahead that to celebrate your birthday we’ll need to buy dozens of candles to just place them on your birthday cake. Love you",
        8:"Nothing gives me so much joy than to see you smile if only I knew what makes you happy in every unique day I would give it to you just to see you smile once more. Happy birthday mum",
        9:"Having you around makes me happy, I count every moment with you as a blessing. May the Lord bless you this day as you celebrate your birthday",
        10:"Many years ago, on a day like this, the world was given a beautiful child, she would later become my mum. I am delighted to be one of your children. It’s another day to celebrate with you for the additional year God has given you. Cheers to a wonderful birthday ahead.",
        },
    'friend':{
        1:" To the best friend I have ever known, i wish you a birthday filled with joy, happiness and lots of memories.",
        2:"Thank you for being that amazing friend. Our friendship has come long way. I will also be there for you forever. Happy Birthday friend!",
        3:"It’s a beautiful thought of how long we have known each other. We have been best friends since childhood. I believe we will continue to celebrate more and more years to come. Happy birthday my dear friend!",
        4:"Every year we celebrate the gift of life God has given us. May this new-year in your life bring more friendship. Happy Birthday my best friend",
        5:"Wishing you a birthday filled with blessings. May the love and happiness that comes with it be with you throughout the year. Happy birthday",
        6:"The fun has not ended. It has just begun. Happy birthday friend, May you blow 1001 candles.",
        7:"The fun has not ended. It has just begun. Happy birthday friend, May you blow 1001 candles.",
        8:"I have never had a friend like you. On this special day, may all your dreams come true. Happy Birthday friend",
        9:"Get ready for a wonderful birthday celebration on this special day. It will be more than memorable. Happy birthday, friend!",
        10:" I can’t stop thinking on how beautiful our friendship has been. You are an amazing friend. Happy birthday, friend!"
        },
    'brother':{
        1:"Even when everything else stops, my love for you shall last forever. Happy Birthday, bro!",
        2:"Thank you for being the best brother ever. Happy Birthday Bro!",
        3:"You are my role model and mentor. You have shaped my life. Happy birthday bro!",
        3:"On this special day in your life. May God blesses you with every good life; love, happiness and joy. Happy birthday Brother!",
        4:" I am lucky to have you as my brother and best friend. I wish you a happy birthday with lots of love on this special day in your life.",
        5:"There is nothing in the world that compares the love of a brother. I wish you an amazing birthday.",
        6:"This day is special to me. It’s a day to remember someone special in my life. The day you came to this world. Happy birthday, Bro!",
        7:"Your birthday is special to me. It reminds me the day you came into this world. Happy birthday, bro!",
        8:"May God bless you with every joy and happiness in life. Happy Birthday Brother!",
        9:"You are my hero. I have always wanted to be like you. I wish you a happy and wonderful birthday.",
        10:"Happy Birthday, brother. Best wishes on your birthday, after you are done. Let’s party!"
        },
    'sister':{
        1:" I am blessed to have a sister like you, may you have a wonderful day on your birthday. Warm birthday wishes for a perfect sister. Happy birthday my beautiful sister.",
        2:"We can choose our friends but we cannot choose our family. I am lucky to have you as a family and friend. Happy birthday young sister.",
        3:"Happy birthday sister; may this day bring blessings to your life.",
        4:"Wish you a day filled with happiness, laughter, fun and love. Happy Birthday sister.",
        5:"The day you were born was such a memorable moment in my life; you have been a true friend and sister. Wish you a happy birthday my dear sister.",
        6:"Thank you for being there for me during the difficult moments and happy moments. You are the best sister I have ever had. Happy birthday sister.",
        7:" May this day bring you happiness and joy; Happy Birthday dear sister.",
        8:"Happy birthday young sister. Wishing you a long life full of blessings.",
        9:"We have shared a lot since childhood; they are great moments to remember. Happy to have you as my sister. Happy Birthday my sweet sister.",
        10:"You are my younger sister but you inspire me a lot. May this day make your dreams come true. Happy birthday sister."
        }
       }
    return t
def sendMessage(chat_id,text):
    re=requests.get(f'https://api.telegram.org/bot1148663975:AAEACks3oCJAuMDToqKM6HUnXTsOOgrMRTw/sendMessage?chat_id={chat_id}&text={text}')
    print(re)
last_update_id=-1
a=1
while True:
    chat_id,text,update_id,username=getUpdates()
    wish=wishes()
    print(username)
    if last_update_id!=update_id:
        if text=='/start':
            text='Which one of these do you want just click it /mother,/friend,/brother,/sister'
            sendMessage(chat_id,text)
        elif text=='/mother':
            text=f"{wish['mother'][a]} /start "
            sendMessage(chat_id,text)
            a+=1
            a=a%10
        elif text=='/friend':
            text=f"{wish['friend'][a]} /start"
            sendMessage(chat_id,text)
            a+=1
            a=a%10
        elif text=='/brother':
            text=f"{wish['brother'][a]} /start"
            sendMessage(chat_id,text)
            a+=1
            a=a%10
        elif text=='/sister':
            text=f"{wish['sister'][a]} /start"
            sendMessage(chat_id,text)
            a+=1
            a=a%10
            
        last_update_id=update_id








        
