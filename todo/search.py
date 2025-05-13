from django.shortcuts import render
from requests import Request
from .models import Project 
import re
from .img_handler import insert_thumbnail
from django.core.paginator import Paginator


def search(request):
    search_phrase = request.GET.get('search', '').lower()
    query = Project.objects.filter(public=True).order_by('-id')

    query_result = list(filter(lambda x: search_phrase in ' '.join([x.title.lower(), x.description.lower(), x.tags.lower(), str(x.id)]), query))
    query_result = insert_thumbnail(query_result)
    paginator = Paginator(query_result, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Результаты поиска корпусной мебели',
        'search_text': search_phrase,
        'posts': query_result,
        'description':'Поиск проектов корпусной мебели на сайте wwbb.ru',
        'page_obj':  page_obj,
        'search_phrase': search_phrase,
    }
    return render(request, 'todo/search.html', context)