from django.urls import path

from polls.views import ModelDrivingBridgeList, ModelDrivingBridgeCreateView, ModelDrivingBridgeUpdateView, \
    ModelDrivingBridgeDeleteView

urlpatterns = [
    path('model_driving_bridge/',
         ModelDrivingBridgeList.as_view(),
         name='model_driving_bridge'),
    path('model_driving_bridge_create/',
         ModelDrivingBridgeCreateView.as_view(),
         name='model_driving_bridge_create'),
    path('model_driving_bridge_update/<int:pk>',
         ModelDrivingBridgeUpdateView.as_view(),
         name='model_driving_bridge_update'),
    path('model_driving_bridge_delete/<int:pk>',
         ModelDrivingBridgeDeleteView.as_view(),
         name='model_driving_bridge_delete'),
    ]