from django.urls import path

from polls.views import SearchCar, CarCreateView, CarUpdateView, CarDeleteView, CarDetail


urlpatterns = [
    path('search_car', SearchCar.as_view(), name='search_car'),
    path('create_car/', CarCreateView.as_view(), name='car_create'),
    path('update_car/<int:pk>', CarUpdateView.as_view(), name='car_update'),
    path('delete_car/<int:pk>', CarDeleteView.as_view(), name='car_delete'),
    path('car_one/<int:pk>', CarDetail.as_view(), name='car_detail'),
    ]