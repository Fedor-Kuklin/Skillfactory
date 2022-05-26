from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, SignupSuccessView, add_authors, remove_authors

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='signup'),
    path('signup_success/',
         SignupSuccessView.as_view(template_name='sign/signup_success.html'),
         name='signup_success'),
    path('upgrade_add/', add_authors, name='upgrade_add'),
    path('upgrade_del/', remove_authors, name='upgrade_del'),
]