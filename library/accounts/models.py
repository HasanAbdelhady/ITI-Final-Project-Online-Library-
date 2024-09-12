from django.contrib.auth.models import AbstractUser
from django.db import models
from books.models import Book
from django.utils import timezone

class Student(AbstractUser):  # Inherit from AbstractUser
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    borrowed_books = models.ManyToManyField(Book, through='BorrowedBook')

    def __str__(self):
        return self.username  # This comes from AbstractUser

    @property
    def image_url(self):
        return f'/media/{self.profile_image}'
    


class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='borrowed_books_set')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowers')
    date_borrowed = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if the book is being borrowed (i.e., it's a new borrow entry)
        if not self.pk and self.book.copies_left > 0:  # Ensure there are copies left
            self.book.copies_left -= 1
            self.book.save()  # Save the updated book copies
        elif self.pk and self.return_date:  # If it's a return, increase the copies
            self.book.copies_left += 1
            self.book.save()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.book.name} borrowed by {self.student.username}"
