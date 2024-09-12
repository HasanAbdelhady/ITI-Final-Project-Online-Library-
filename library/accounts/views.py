from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import RegistrationForm
from .models import Student  # Ensure you're importing the correct model

@login_required
def profile(request):
    return render(template_name='accounts/account_details.html', request=request)

class AccountsDetailView(LoginRequiredMixin, DetailView):
    model = Student  # Use the Student model instead of User
    template_name = 'accounts/account_details.html'

class AccountCreateView(CreateView):
    model = Student
    template_name = 'accounts/create.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')  # Redirect to home after successful registration

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response  # No need to redirect here; `success_url` will handle it
