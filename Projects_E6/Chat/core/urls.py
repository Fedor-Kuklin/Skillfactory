from django.contrib.auth import views as auth_views
from django.urls import path
# from .views import ShowProfilePageView, CreateProfilePageView,
from .views import UserList
from .views import  profile
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('profile/', profile, name='users-profile'),
    path('users/', UserList.as_view(), name='users'),
    # path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    # path('create_profile_page/<int:pk>/', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)