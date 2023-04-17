
from django.contrib.auth.models import User
from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from .models import Car, Maintenance, Claim, TypeMaintenance, ServiceCompany, ModelTechnics, ModelMotor, \
    ModelTransmissions, ModelDrivingBridge, ModelControlledBridge, TypeFault, RecoveryMethod


class CarFilter(FilterSet):

    model_technics = ModelChoiceFilter(queryset=ModelTechnics.objects.all(),
                                       label='Модель техники')
    model_motor = ModelChoiceFilter(queryset=ModelMotor.objects.all(),
                                    label='Модель двигателя')
    model_transmissions = ModelChoiceFilter(queryset=ModelTransmissions.objects.all(),
                                            label='Модель трансмиссии')
    model_driving_bridge = ModelChoiceFilter(queryset=ModelDrivingBridge.objects.all(),
                                             label='Модель ведущего моста')
    model_controlled_bridge = ModelChoiceFilter(queryset=ModelControlledBridge.objects.all(),
                                                label='Модель управляемого моста')

    class Meta:
        model = Car

        fields = {
            # 'model_technics',
            # 'model_motor',
            # 'model_transmissions',
            # 'model_driving_bridge',
            # 'model_controlled_bridge',
        }


class AllFilter(FilterSet):

    factory_num_car = CharFilter(field_name='factory_num_car',
                                 lookup_expr='exact',
                                 label='Заводской номер',)

    class Meta:
        model = Car

        fields = {

        }


class MaintenanceFilter(FilterSet):

    type_maintenance = ModelChoiceFilter(queryset=TypeMaintenance.objects.all(),
                                         label='Вид ТО')
    car = ModelChoiceFilter(queryset=Car.objects.all(),
                            label='Заводской номер', )
    service_company = ModelChoiceFilter(queryset=ServiceCompany.objects.all(),
                                        label='Сервисная компания')

    class Meta:
        model = Maintenance

        fields = {
            # 'type_maintenance',
            # 'car',
            # 'service_company',
        }


class ClaimFilter(FilterSet):
    node_failure = ModelChoiceFilter(queryset=TypeFault.objects.all(),
                                     label='Узел отказа')
    recovery_method = ModelChoiceFilter(queryset=RecoveryMethod.objects.all(),
                                        label='Способ восстановления', )
    service_company = ModelChoiceFilter(queryset=ServiceCompany.objects.all(),
                                        label='Сервисная компания')

    class Meta:
        model = Claim

        fields = {
            'node_failure',
            'recovery_method',
            'service_company',
        }
