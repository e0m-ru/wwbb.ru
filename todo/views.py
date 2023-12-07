from django.shortcuts import render
from .CRUD_Posts import *
from django.db.models import Q
from .comments import *
from .search import search
import re
from djsite.settings import MEDIA_ROOT
from .vk import vk_api

def main_page(request):
    all_posts = Project.objects.filter(public=True)
    all_posts=list(all_posts)
    all_posts.sort(reverse=True, key = lambda x:x.rating)
    insert_thumbnail(all_posts)
    context = {
        'title': 'МебелЯ',
        'example_01': random.choices(all_posts, k=4),
        'example_02': random.choices(all_posts, k=4),
        'example_03': random.choices(all_posts, k=4),
        'description':'Сайт производителя корпусной мебели на заказ https://wwbb.ru.',
    }
    return render(request, 'todo/index.html', context)

def feedback(request):
    all_posts = Project.objects.filter(public=True)
    insert_thumbnail(all_posts)
    all_posts = random.choices(all_posts, k=4)
    context = {
        'title': 'МебелЯ: Контакты',
        'description':'Контактная информация мебельного производства wwbb.ru',
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
        'description':'Все фотограии корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/all_photo.html', context)

def image_gallery(request):
    all_posts = Project.objects.filter(public=True)
    insert_thumbnail(all_posts)
    all_posts = random.choices(all_posts, k=1)
    context = {
        'title': 'МебелЯ: Галерея',
        'projects': all_posts,
        'description':'Сайт производителя корпусной мебели на заказ https://wwbb.ru.',
    }
    return render(request, 'todo/image_gallery.html', context)    

def vk_api(request):
    context = {
        'title': 'МебелЯ: VK API',
        'description':'Сайт производителя корпусной мебели на заказ https://wwbb.ru.',
        'posts': [],
    }
    return render(request, 'todo/vk_wall.html', context)    
