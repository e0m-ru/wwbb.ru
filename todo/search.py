from django.shortcuts import render
from .models import Project 
import re
from .img_handler import insert_thumbnail

def search(request):
    search_phrase=request.GET['search'].lower()
    query = Project.objects.filter(public=True)

    query_result = list(filter(lambda x: search_phrase in ' '.join([x.title.lower(), x.description.lower(), x.tags.lower(), str(x.id)]), query))
    query_result = insert_thumbnail(query_result)
    context = {
        'title': 'Результаты поиска',
        'aaa': search_phrase,
        'posts': query_result,
        'description':'Поиск фотографий корпусной мебели на сайте wwbb.ru',
    }
    return render(request, 'todo/search.html', context)