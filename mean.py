import requests
import json


def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'q7hHeC5QJdgIkDXMj1NobPTuxZSUti4WAEvL3csf0wlGrn96pYEQhIoysTmpxNa6b5fu2zFg9LtHPGJ4',
        'sender_id' : 'Fast2SMS',
        'message' : message,
        'language' : 'english',
        'route' : 'p',
        'numbers' : number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)

send_sms("7057438749", "This is my first msg send by my own codding")