from django.urls import include, path
from accounts.views import  AccountCreateView, AccountsDetailView, profile
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/<int:pk>', login_required(AccountsDetailView.as_view()), name='accounts.profile'),
    path("register", AccountCreateView.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),

]
