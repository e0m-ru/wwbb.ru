from .models import Comment
from .forms import CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
import sys
import json


def add_comment(request):
    token = request.POST.get('smart-token',None)
    if request.method == 'POST':
        if check_captcha(request, token):
            form = CommentForm(request.POST, request.FILES, instance=Comment())
            if form.is_valid():
                f = form.save(commit=False)
                f.save()
                # return redirect('/comment/' + str(f.id))
                context = {
                'title': 'Отзыв',
                'CommentForm': CommentForm(),
                'Comment': Comment(), }
                return redirect('/comments', )
        else:
            return redirect('/comments')
    context = {
    'title': 'Добавить отзыв',
    'CommentForm': CommentForm(),
    'Comment': Comment(), 
    'description':'Добавление отзыва на производство и установку корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/comments/add_comment.html', context)


@login_required
def update_comment(request, com_id):
    db_Obj = Comment.objects.get(id=com_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=db_Obj)
        if form.is_valid():
            form.save()
            return redirect('/comments')
    form = CommentForm(instance=db_Obj)
    context = {
        'title': 'Редактор отзыва',
        'comment': db_Obj,
        'form': form,
        'description':'Редактирование отзыва на производство и установку корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/comments/update_comment.html', context)


@login_required
def delete_comment(request, com_id):
    db_Obj = Comment.objects.get(id=com_id)
    if request.method == 'POST':
        db_Obj.delete()
        return redirect('/comments')
    context = {
        'comment': db_Obj,
        'description':'Удаление отзыва на производство и установку корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/comments/delete_comment.html', context)


def read_comment(request, com_id):
    comment = Comment.objects.get(pk=com_id)
    context = {
        'comment': comment,
        'description': f'{comment.comment} Отзыв на производство и установку корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/comments/comment.html', context)


def comments(request):
    comments = Comment.objects.filter(public=True)
    context = {
        'comments': comments,
        'title': 'МебелЯ: Все отзывы',
        'description':'Все отзывы на производство и установку корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/comments/comments.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
       ip = x_forwarded_for.split(',')[0]
    else:
       ip = request.META.get('REMOTE_ADDR')
    return ip

# ----------------SMART CAPCHA YANDEX
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
       ip = x_forwarded_for.split(',')[0]
    else:
       ip = request.META.get('REMOTE_ADDR')
    return ip

SMARTCAPTCHA_SERVER_KEY = "kFajSJl59kuzxjz0XJ6SfgTSmlLinK58Jhj4sH16"


def check_captcha(request, token):
    resp = requests.get(
        "https://captcha-api.yandex.ru/validate",
        {
            "secret": SMARTCAPTCHA_SERVER_KEY,
            "token": token,
            "ip": get_client_ip(request)
        },
        timeout=1
    )
    server_output = resp.content.decode()
    if resp.status_code != 200:
        print(
            f"Allow access due to an error: code={resp.status_code}; message={server_output}", file=sys.stderr)
        return True
    return json.loads(server_output)["status"] == "ok"

