from django.urls import path
from polls.views import UserView, UserCreateView, UserUpdateView, MyPasswordChangeView

urlpatterns = [
    path('user_list/',
         UserView.as_view(),
         name='user_list'),
    path('user_create/',
         UserCreateView.as_view(),
         name='user_create'),
    path('user_update/<int:pk>',
         UserUpdateView.as_view(),
         name='user_update'),
    path('password/',
         MyPasswordChangeView.as_view())
]
