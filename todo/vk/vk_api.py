# https://api.vk.com/method/wall.get?owner_id=210700286&access_token=TOKEN&v=5.131
from datetime import datetime
import locale
from .config import SERVICE_ACCESS_KEY, PROTECTED_KEY
import requests
import json

# locale.setlocale(locale.LC_TIME, "ru_RU")

requests.get(f'https://oauth.vk.com/authorize?client_id=1&group_ids=1,123456&display=page&redirect_uri=http://example.com/callback&scope=messages&response_type=token&v=5.131')
