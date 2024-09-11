from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Book

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = Student
        fields = ['username', 'email', 'profile_image', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'm-4 w-full px-3 py-2 border border-gray-300 rounded-lg'
            })
            if field_name in ['username', 'password1', 'password2']:
                field.label = field.label.capitalize()  # Capitalize labels if needed

class BorrowBookForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Select a book to borrow")
