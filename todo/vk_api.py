# https://api.vk.com/method/wall.get?owner_id=210700286&access_token=TOKEN&v=5.131
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, "ru_RU")
# Сервисный ключ доступа 
TOKEN='8b55c4048b55c4048b55c404d88b28c43188b558b55c404e9f3e47ba05871683ad0ba4d'
ID = '732870827'
import requests
import json
def get_wall():
    content = requests.get(f"https://api.vk.com/method/wall.get?owner_id={ ID }&access_token={ TOKEN }&v=5.131").text
    content = json.loads(content)
    content = content['response']['items']
    posts = []
    for x in content:
        id = x['id']
        data = datetime.fromtimestamp(x['date']).strftime("%d.%m.%Y")
        txt = x['text']
        photo_list = [y for y in x['attachments']]
        siz = []
        for photo in photo_list:
            siz.append(photo['photo'])
        posts.append((id, data, txt, siz))
    return posts