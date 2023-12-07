from random import shuffle
from django.shortcuts import render
from .CRUD_Posts import *
from .comments import *
from .search import search
import re
from djsite.settings import MEDIA_ROOT


def main_page(request):
    all_posts = Project.objects.filter(public=True)
    all_posts = list(all_posts)
    all_posts.sort(reverse=True, key=lambda x: x.rating)
    insert_thumbnail(all_posts)
    all_posts = all_posts[:12]
    shuffle(all_posts)
    context = {
        'title': 'МебелЯ',
        'example_01': all_posts[:4],
        'example_02': all_posts[4:8],
        'example_03': all_posts[8:12],
        'description': 'Сайт производителя корпусной мебели на заказ https://wwbb.ru.',
    }
    return render(request, 'todo/index.html', context)


def feedback(request):
    all_posts = Project.objects.filter(public=True)
    insert_thumbnail(all_posts)
    all_posts = random.choices(all_posts)
    context = {
        'title': 'МебелЯ: Контакты',
        'description': 'Контактная информация мебельного производства wwbb.ru',
        'projects': all_posts,
    }
    return render(request, 'todo/feedback.html', context)


def all_photos(request):
    dr = MEDIA_ROOT+'/photos/'
    all = os.listdir(dr)
    all_ph = []
    for i in all:
        for y in os.listdir(dr+i):
            if re.search('jpg', y):
                all_ph.append('/media/photos/'+i+'/'+(y.split('.')[0]))
    context = {
        'title': 'МебелЯ: Контакты',
        'projects': all_ph,
        'description': 'Все фотограии корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/all_photo.html', context)


def vk_api(request):
    context = {
        'title': 'МебелЯ: VK API',
        'description': 'Сайт производителя корпусной мебели на заказ https://wwbb.ru.',
        'posts': [],
    }
    return render(request, 'todo/vk_wall.html', context)
