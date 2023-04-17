from django.urls import path

from polls.views import TypeFaultList, TypeFaultCreateView, TypeFaultUpdateView, TypeFaultDeleteView

urlpatterns = [
    path('type_fault/',
         TypeFaultList.as_view(),
         name='type_fault'),
    path('type_fault_create/',
         TypeFaultCreateView.as_view(),
         name='type_fault_create'),
    path('type_fault_update/<int:pk>',
         TypeFaultUpdateView.as_view(),
         name='type_fault_update'),
    path('type_fault_delete/<int:pk>',
         TypeFaultDeleteView.as_view(),
         name='type_fault_delete'),
    ]