from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class CarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Car
        fields = ['id',
                  'factory_num_car',
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
                  'service_company',
                 ]


class MaintenanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maintenance
        fields = ['id',
                  'type_maintenance',
                  'data_maintenance',
                  'operating_time',
                  'num_order',
                  'data_order',
                  'car',
                  'service_company',
                  ]


class ClaimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Claim
        fields = ['id',
                  'data_rejection',
                  'operating_time',
                  'node_failure',
                  'description_failure',
                  'recovery_method',
                  'spare_parts',
                  'data_restoration',
                  'downtime_technic',
                  'car',
                  'service_company',
                  ]


class ModelTechnicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelTechnics
        fields = ['id', 'title', 'description', ]


class ModelMotorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelMotor
        fields = ['id', 'title', 'description', ]


class ModelTransmissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelTransmissions
        fields = ['id', 'title', 'description', ]


class ModelDrivingBridgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelDrivingBridge
        fields = ['id', 'title', 'description', ]


class ModelControlledBridgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelControlledBridge
        fields = ['id', 'title', 'description', ]


class TypeMaintenanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeMaintenance
        fields = ['id', 'title', 'description', ]


class TypeFaultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeFault
        fields = ['id', 'title', 'description', ]


class RecoveryMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecoveryMethod
        fields = ['id', 'title', 'description', ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'title',  'name', 'description']


class ServiceCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = ['id', 'name', 'description']