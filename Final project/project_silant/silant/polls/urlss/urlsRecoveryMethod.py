from django.urls import path

from polls.views import RecoveryMethodList, RecoveryMethodUpdateView, RecoveryMethodCreateView, RecoveryMethodDeleteView

urlpatterns = [
    path('recovery_method/',
         RecoveryMethodList.as_view(),
         name='recovery_method'),
    path('recovery_method_create/',
         RecoveryMethodCreateView.as_view(),
         name='recovery_method_create'),
    path('recovery_method_update/<int:pk>',
         RecoveryMethodUpdateView.as_view(),
         name='recovery_method_update'),
    path('recovery_method_delete/<int:pk>',
         RecoveryMethodDeleteView.as_view(),
         name='recovery_method_delete'),
    ]