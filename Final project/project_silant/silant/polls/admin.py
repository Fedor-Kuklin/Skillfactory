from django.contrib import admin
from .models import *


class CarAdmin(admin.ModelAdmin):
    list_display = ('factory_num_car',
                    'model_technics',
                    'model_motor',
                    'factory_num_motor',
                    'model_transmissions',
                    'factory_num_transmissions',
                    'model_driving_bridge',
                    'factory_num_driving_bridge',
                    'model_controlled_bridge',
                    'factory_num_controlled_bridge',
                    'contract_num_data',
                    'ship_date',
                    'consignee',
                    'delivery_address',
                    'equipment',
                    'client',
                    'service_company',)
    list_filter = ('factory_num_car',)


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('car',
                    'type_maintenance',
                    'data_maintenance',
                    'operating_time',
                    'num_order',
                    'data_order',
                    'service_company',)


class ClaimAdmin(admin.ModelAdmin):
    list_display = ('data_rejection',
                    'operating_time',
                    'node_failure',
                    'description_failure',
                    'recovery_method',
                    'spare_parts',
                    'data_restoration',
                    'downtime_technic',
                    'car',
                    'service_company',)


class ModelTechnicsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',)


class ModelMotorAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',)


class ModelTransmissionsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',)


class ModelDrivingBridgeAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',)


class ModelControlledBridgeAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',)


class TypeMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',)


class TypeFaultAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',)


class RecoveryMethodAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',)


class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('title','name','description',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('title','name','description',)


class ReferencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'ref',)
    ordering = ('id',)


admin.site.register(Car, CarAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(ModelTechnics, ModelTechnicsAdmin)
admin.site.register(ModelMotor, ModelMotorAdmin)
admin.site.register(ModelTransmissions, ModelTransmissionsAdmin)
admin.site.register(ModelDrivingBridge, ModelDrivingBridgeAdmin)
admin.site.register(ModelControlledBridge, ModelControlledBridgeAdmin)
admin.site.register(TypeMaintenance, TypeMaintenanceAdmin)
admin.site.register(TypeFault, TypeFaultAdmin)
admin.site.register(RecoveryMethod, RecoveryMethodAdmin)
admin.site.register(ServiceCompany, ServiceCompanyAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(References, ReferencesAdmin)
