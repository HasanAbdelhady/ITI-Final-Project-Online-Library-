from django.contrib import admin

from accounts.models import Student, BorrowedBook

admin.site.register(Student)
admin.site.register(BorrowedBook)