from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import RegistrationForm
from .models import Student 
from django.utils.decorators import method_decorator


# @login_required
# def profile(request):
#     return redirect(reverse("home"))

@method_decorator(login_required, name='dispatch')
class AccountsDetailView(LoginRequiredMixin, DetailView):
    model = Student  # Use the Student model instead of User
    template_name = 'accounts/account_details.html'

class AccountCreateView(CreateView):
    model = Student
    template_name = 'accounts/create.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
