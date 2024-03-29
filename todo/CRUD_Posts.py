from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
import os
from .img_handler import *
import random


# CRUD Projects views functions


@login_required
def post_create(request):
    # Multiple file upload
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=Project())
        files = request.FILES.getlist('image')
        form.album = 'assa'
        form.save()
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            img_path = f'{PHOTO_PATH}{f.id}'
            os.mkdir(img_path)
            for s, i in enumerate(files):
                img = img_handler(i, f.id, s)
            return redirect('/post/' + str(f.id))
    
    form = ProjectForm()
    context = {
        'title': 'Добавить пост',
        'form': form,
        'description': 'Создание поста на сайте wwbb.ru',
    }
    return render(request, 'todo/post_create.html', context)


def post_read(request, post_id):
    post = Project.objects.all().get(id=post_id)
    context = {
        'title': 'Мебеля',
        'project': post,
        'tags': [*map(str.strip, post.tags.lower().split(','))],
        'album': collect_album(post_id),
        'description': f'Проект {post.title} wwbb.ru ',
        'similar': insert_thumbnail(similar_posts(post_id)),
    }
    return render(request, 'todo/post_read.html', context)


@login_required
def post_update(request, post_id):
    db_Obj = Project.objects.get(id=post_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=db_Obj)
        files = request.FILES.getlist('image')
        if form.is_valid():
            form.save()
            return redirect('/post/' + str(db_Obj.id))
    form = ProjectForm(instance=db_Obj)
    context = {
        'title': 'Редактор проекта',
        'project': db_Obj,
        'album': collect_album(post_id),
        'form': form,
        'description': 'Редактирование материала wwbb.ru',
    }
    return render(request, 'todo/post_update.html', context)


@login_required
def post_delete(request, post_id):
    db_Obj = Project.objects.get(id=post_id)
    album = collect_album(post_id)
    if request.method == 'POST':
        for img in album:
            os.remove(f'{PHOTO_PATH}{post_id}/{img}.jpg')
            os.remove(f'{PHOTO_PATH}{post_id}/{img}.thumbnail')
        os.rmdir(f'{PHOTO_PATH}{post_id}/')
        db_Obj.delete()
        return redirect('/posts')
    return render(request, 'todo/post_delete.html', {'project': db_Obj, 'title': 'Удаление поста', 'album': collect_album(post_id)})


def posts(request):
    all_posts = Project.objects.filter(public=True)
    insert_thumbnail(all_posts)
    all_posts.sort(key = lambda x: x.rating , reverse=True)
    context = {
        'title': 'примеры работ',
        'projects': all_posts,
        'description': 'Список проектов производства корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/posts.html', context)

    
def posts_by_tag(request, tag):
    db_Obj = Project.objects.all()
    insert_thumbnail(db_Obj)

    by_tags = []
    for i in db_Obj:
        tags = i.tags.lower().split(',')
        tags = map(lambda x: x.strip(), tags)
        if tag.lower() in tags:
            by_tags.append(i)
    by_tags.sort(key = lambda x: x.rating , reverse=True)
    context = {
        'title': 'МебелЯ: ' + str(tag),
        'header': str(tag),
        'projects': by_tags,
        'description': f'Фото по тегу {tag} wwbb.ru',
    }
    return render(request, 'todo/posts.html', context)

