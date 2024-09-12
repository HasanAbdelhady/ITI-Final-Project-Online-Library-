from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import RegistrationForm, ProfileUpdateForm
from .models import Student 
from django.utils.decorators import method_decorator


@login_required
def profile(request):
    url = reverse('home')
    return redirect(url)

class AccountsDetailView(LoginRequiredMixin, DetailView):
    model = Student  # Use the Student model
    template_name = 'accounts/account_details.html'
    context_object_name = 'student'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        student = self.get_object()  # Get the student object
        form = ProfileUpdateForm(request.POST, instance=student)  # Handle profile update form

        if form.is_valid():
            form.save()  # Save the updated profile
            return redirect('accounts.profile', pk=student.pk)  # Redirect to profile page
        else:
            # If the form is invalid, render the page with errors
            return self.render_to_response(self.get_context_data(form=form))

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
    


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = ProfileUpdateForm
    template_name = 'accounts/edit_profile.html'

    def get_object(self):
        return self.request.user  # Get the current logged-in user

    def get_success_url(self):
        return reverse_lazy('accounts.profile', kwargs={'pk': self.request.user.pk})