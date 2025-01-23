from django.db import models
class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)  # Назва фото (опціонально)
    image = models.ImageField(upload_to='gallery/')  # Шлях для збереження фото
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Дата завантаження

    def __str__(self):
        return self.title or f"Image {self.id}"
# Create your models here.
