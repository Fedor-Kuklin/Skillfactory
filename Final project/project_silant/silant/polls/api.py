from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class CarViewset(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MaintenanceViewset(ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ClaimViewset(ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ModelTechnicsViewset(ModelViewSet):
    queryset = ModelTechnics.objects.all()
    serializer_class = ModelTechnicsSerializer


class ModelMotorViewset(ModelViewSet):
    queryset = ModelMotor.objects.all()
    serializer_class = ModelMotorSerializer


class ModelTransmissionsViewset(ModelViewSet):
    queryset = ModelTransmissions.objects.all()
    serializer_class = ModelTransmissionsSerializer


class ModelDrivingBridgeViewset(ModelViewSet):
    queryset = ModelDrivingBridge.objects.all()
    serializer_class = ModelDrivingBridgeSerializer


class ModelControlledBridgeViewset(ModelViewSet):
    queryset = ModelControlledBridge.objects.all()
    serializer_class = ModelControlledBridgeSerializer


class TypeMaintenanceViewset(ModelViewSet):
    queryset = TypeMaintenance.objects.all()
    serializer_class = TypeMaintenanceSerializer


class TypeFaultViewset(ModelViewSet):
    queryset = TypeFault.objects.all()
    serializer_class = TypeFaultSerializer


class RecoveryMethodViewset(ModelViewSet):
    queryset = RecoveryMethod.objects.all()
    serializer_class = RecoveryMethodSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ServiceCompanyViewset(ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceCompanySerializer
