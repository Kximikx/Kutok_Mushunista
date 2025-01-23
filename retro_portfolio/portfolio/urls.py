from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.gallery, name='gallery'),  # Галерея
    path('upload/', views.upload_image, name='upload_image'),  # Завантаження фото
    path('upload/', views.upload_image, name='upload_image'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
if settings.DEBUG:  # Обробка тільки в режимі розробки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
