from django.urls import path

from polls.views import ModelControlledBridgeList, ModelControlledBridgeCreateView, ModelControlledBridgeUpdateView, \
    ModelControlledBridgeDeleteView

urlpatterns = [
    path('model_controlled_bridge/',
         ModelControlledBridgeList.as_view(),
         name='model_controlled_bridge'),
    path('model_controlled_bridge_create/',
         ModelControlledBridgeCreateView.as_view(),
         name='model_controlled_bridge_create'),
    path('model_controlled_bridge_update/<int:pk>',
         ModelControlledBridgeUpdateView.as_view(),
         name='model_controlled_bridge_update'),
    path('model_controlled_bridge_delete/<int:pk>',
         ModelControlledBridgeDeleteView.as_view(),
         name='model_controlled_bridge_delete'),
    ]