from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room_create/', RoomCreate.as_view(), name='room_create'),
    path('room_update/<int:pk>', RoomUpdate.as_view(), name='room_update'),
    path('room_delete/<int:pk>', RoomDelete.as_view(), name='room_delete'),
    path('<slug:slug>/', views.room, name='room'),
]