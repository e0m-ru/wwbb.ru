from django.urls import include, path

from django.contrib import admin
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin', admin.site.urls),
    path('register', user_views.register, name='register'),
    path('profile', user_views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('', include('todo.urls'))
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "djsite.views.page_not_found_view"