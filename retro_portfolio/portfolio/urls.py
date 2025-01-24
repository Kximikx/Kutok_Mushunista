from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # Головна сторінка
    path('gallery/', views.gallery, name='gallery'),  # Галерея
    path('upload/', views.upload_image, name='upload_image'),  # Завантаження фото
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Логін
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Логаут
]

# Додавання медіафайлів у режимі DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
