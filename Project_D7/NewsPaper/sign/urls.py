from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, SignupSuccessView, upgrade_me

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
    path('signup_success/',
         SignupSuccessView.as_view(template_name = 'sign/signup_success.html'),
         name='signup_success'),
    path('upgrade/', upgrade_me, name = 'upgrade')
]