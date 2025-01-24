from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GalleryImage
from .forms import GalleryImageForm

def home(request):
    """Вигляд для головної сторінки."""
    return render(request, 'index.html')

def gallery(request):
    """Вигляд для сторінки галереї."""
    images = GalleryImage.objects.all()  # Всі фото з бази даних
    return render(request, 'gallery.html', {'images': images})

# Декоратор для перевірки доступу (тільки суперкористувач)
def superuser_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            return redirect('login')  # Перенаправлення на сторінку логіну
        return function(request, *args, **kwargs)
    return wrapper

@superuser_required
def upload_image(request):
    """Вигляд для завантаження фото (доступ лише суперкористувачам)."""
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Перенаправлення до галереї
    else:
        form = GalleryImageForm()
    return render(request, 'upload_image.html', {'form': form})
