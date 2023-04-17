from django.urls import path

from polls.views import SearchMaintenance, MaintenanceDetail, MaintenanceCreateView, MaintenanceUpdateView, \
    MaintenanceDeleteView


urlpatterns = [
    path('search_maintenance/', SearchMaintenance.as_view(), name='maintenance'),
    path('maintenance_one/<int:pk>', MaintenanceDetail.as_view(), name='maintenance_detail'),
    path('create_maintenance/', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('update_maintenance/<int:pk>', MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('delete_maintenance/<int:pk>', MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    ]