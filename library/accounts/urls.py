from django.urls import path, reverse_lazy
from accounts.views import (AccountCreateView, AccountsDetailView, profile, 
                            ProfileUpdateView, StudentBorrowedBooksListView, 
                            CustomLogoutView, CustomPasswordChangeView)
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', login_required(profile), name='profile'),
    path('profile/<int:pk>/', login_required(AccountsDetailView.as_view()), name='accounts.profile'),
    path('register/', AccountCreateView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),

    # Override the password change done view with a custom template
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'  # Use your custom template path here
    ), name='password_change_done'),

    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('admin_dashboard/', StudentBorrowedBooksListView.as_view(), name='students.data'),
]
