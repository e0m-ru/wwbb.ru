from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
import os
from .img_handler import *
import random
from .vk_repost import get_wall_posts
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


# CRUD Projects views functions

@login_required
def post_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            img_path = os.path.join(PHOTO_PATH, str(project.id))
            os.makedirs(img_path, exist_ok=True)
            for index, image in enumerate(files):
                img_handler(image, project.id, index)
            return redirect(f'/post/{str(project.id)}')
        else:
            context = {
                'title': 'Добавить пост',
                'form': form,
                'description': 'Создание поста на сайте wwbb.ru',
                'posts': get_wall_posts(),
                'errors': form.errors,
            }
            return render(request, 'todo/CRUD/post_create.html', context)
    
    form = ProjectForm()
    context = {
        'title': 'Добавить пост',
        'form': form,
        'description': 'Создание поста на сайте wwbb.ru',
        'posts': get_wall_posts(),
    }
    return render(request, 'todo/CRUD/post_create.html', context)


def post_read(request, post_id):
    post = get_object_or_404(Project,id=post_id)
    context = {
        'title': 'Мебеля',
        'project': post,
        'tags': [*map(str.strip, post.tags.lower().split(','))],
        'album': collect_album(post_id),
        'description': f'Проект {post.title} wwbb.ru ',
        'similar': insert_thumbnail(similar_posts(post_id)),
    }
    return render(request, 'todo/CRUD/post_read.html', context)


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
    return render(request, 'todo/CRUD/post_update.html', context)


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
    return render(request, 'todo/CRUD/post_delete.html', {'project': db_Obj, 'title': 'Удаление поста', 'album': album})


def posts(request):
    all_posts = Project.objects.filter(public=True)
    insert_thumbnail(all_posts)
    all_posts.sort(key = lambda x: x.id , reverse=True)
    context = {
        'title': 'примеры работ',
        'projects': all_posts,
        'description': 'Список проектов производства корпусной мебели wwbb.ru',
    }
    return render(request, 'todo/posts.html', context)



def posts_by_tag(request, tag):
    db_Obj = Project.objects.filter(
        public=True,
        tags__icontains=tag
    )
    insert_thumbnail(db_Obj)
    paginator = Paginator(db_Obj, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'title': f'МебелЯ: {tag}',
        'header': tag,
        'projects': db_Obj,
        'description': f'Фото мебели {tag} wwbb.ru',
        "page_obj": page_obj,
        "paginator": paginator,
    }
    return render(request, 'todo/posts.html', context)

