from django.db import models
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='books/images/', null=True, blank=True)
    copies_left = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self):
        url = reverse("book.details", args=[self.id])
        return url
