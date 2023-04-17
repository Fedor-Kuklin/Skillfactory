from django.urls import path

from polls.views import TypeMaintenanceList, TypeMaintenanceUpdateView, TypeMaintenanceCreateView, \
    TypeMaintenanceDeleteView

urlpatterns = [
    path('type_maintenance/',
         TypeMaintenanceList.as_view(),
         name='type_maintenance'),
    path('type_maintenance_create/',
         TypeMaintenanceCreateView.as_view(),
         name='type_maintenance_create'),
    path('type_maintenance_update/<int:pk>',
         TypeMaintenanceUpdateView.as_view(),
         name='type_maintenance_update'),
    path('type_maintenance_delete/<int:pk>',
         TypeMaintenanceDeleteView.as_view(),
         name='type_maintenance_delete'),
    ]