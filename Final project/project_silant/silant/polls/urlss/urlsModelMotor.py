from django.urls import path

from polls.views import ModelMotorCreateView, ModelMotorUpdateView, ModelMotorDeleteView, ModelMotorList

urlpatterns = [
    path('model_motor/', ModelMotorList.as_view(), name='model_motor'),
    path('model_motor_create/', ModelMotorCreateView.as_view(), name='model_motor_create'),
    path('model_motor_update/<int:pk>', ModelMotorUpdateView.as_view(), name='model_motor_update'),
    path('model_motor_delete/<int:pk>', ModelMotorDeleteView.as_view(), name='model_motor_delete'),
    ]
