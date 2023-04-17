from django.urls import path

from polls.views import ModelTransmissionsList, ModelTransmissionsCreateView, ModelTransmissionsUpdateView, \
    ModelTransmissionsDeleteView

urlpatterns = [
    path('model_transmissions/',
         ModelTransmissionsList.as_view(),
         name='model_transmissions'),
    path('model_transmissions_create/',
         ModelTransmissionsCreateView.as_view(),
         name='model_transmissions_create'),
    path('model_transmissions_update/<int:pk>',
         ModelTransmissionsUpdateView.as_view(),
         name='model_transmissions_update'),
    path('model_transmissions_delete/<int:pk>',
         ModelTransmissionsDeleteView.as_view(),
         name='model_transmissions_delete'),
    ]