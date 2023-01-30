from django.urls import path, re_path

from . import views

urlpatterns = [
    path('feedback', views.feedback),
    re_path('search', views.search, name="search"),
    
    # CRUD Project urls
    path('posts', views.posts, name='posts'),
    path('photo', views.all_photos, name='photo'),
    path('create', views.post_create, name='post_create'),
    path('update/<int:post_id>', views.post_update, name='post_update'),
    path('delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('post/<int:post_id>', views.post_read, name='post'),
   
    # Comments CRUD urls
    path('comments', views.comments, name='comments'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('update_comment/<int:com_id>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:com_id>', views.delete_comment, name='delete_comment'),
    path('comment/<int:com_id>', views.read_comment, name='read_comment'),

    path('tag/<str:tag>', views.posts_by_tag, name="tag"),
    path('image', views.image_gallery, name='image_gallery'),
    # In all other cases
    path('', views.main_page),    
]
