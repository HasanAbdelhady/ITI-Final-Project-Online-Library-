from django.contrib.auth.models import AbstractUser
from django.db import models
from books.models import Book
from django.utils import timezone

class Student(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    borrowed_books = models.ManyToManyField(Book, through='BorrowedBook')

    def __str__(self):
        return self.username  
    @property
    def image_url(self):
        return f'/media/{self.profile_image}'
    


class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='borrowed_books_set')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowers')
    date_borrowed = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and self.book.copies_left > 0:
            self.book.copies_left -= 1
            self.book.save()
        elif self.pk and self.return_date:
            self.book.copies_left += 1
            self.book.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.name} borrowed by {self.student.username} on {self.date_borrowed:%Y-%m-%d}"
